#!/usr/bin/env python3
"""
Live discovery of Pueblo, CO meeting agendas via the CivicClerk portal API.

WHY THIS MODULE EXISTS
----------------------
Until 2026-07 this project scraped the CivicPlus "Archive Center":
    https://www.pueblo.us/Archive.aspx?AMID=37
That archive is DEFUNCT. Its newest entry is 2022-05-23 and almost everything
in it is 2013 or older. The agenda PDFs it handed us (e.g. city_council-626.pdf)
are the *January 14, 2013* agenda. Because the old scraper walked the list
oldest-first and never checked meeting dates, a keyword scan of a 13-year-old
document was logged as "no surveillance/immigration matches found" -- a false
all-clear. See the staleness guard below: that specific failure mode must never
again look like a clean result.

WHERE THE DOCUMENTS ACTUALLY LIVE (verified 2026-07-29)
------------------------------------------------------
Both the City and the County migrated to CivicClerk. Two separate tenants:

  City of Pueblo             portal: https://puebloco.portal.civicclerk.com
                             api:    https://puebloco.api.civicclerk.com/v1
  Pueblo County (BOCC)       portal: https://pueblococo.portal.civicclerk.com
                             api:    https://pueblococo.api.civicclerk.com/v1

The portal pages are JavaScript single-page apps (plain urllib sees no links),
but they are backed by a public, unauthenticated OData REST API that needs no
key -- only a browser-ish User-Agent.

ACCESS PATTERN
--------------
List events, newest first:
  GET {api}/Events
      ?$filter=startDateTime lt <ISO-Z> and contains(eventCategoryName,'City Council')
      &$orderby=startDateTime desc
      &$top=25
  Accept: application/json

Response is JSON: {"value": [ {event}, ... ]}. Useful fields per event:
  id                    int   event id (portal URL: /event/<id>/overview)
  startDateTime         str   ISO-8601 Zulu -- THE MEETING DATE
  eventCategoryName     str   e.g. "City Council Regular Meeting",
                              "City Council Work Session",
                              "Board of County Commissioners"
  publishedFiles        list  inline, no $expand needed; each entry has
                              fileId (int), type ("Agenda", "Agenda Packet",
                              "Minutes", "Notice", "Events Memo"), name

Download a document (returns application/pdf):
  GET {api}/Meetings/GetMeetingFileStream(fileId=<fileId>,plainText=false)

Gotcha: the Events collection contains hidden *template* rows with absurd future
dates (e.g. eventDate 2100-01-12). Always bound the query with
"startDateTime lt <now + small window>" -- which is what upcoming_cutoff() does.
"""

from __future__ import annotations

import datetime
import json
import urllib.error
import urllib.parse
import urllib.request

# A browser-style User-Agent is required; the API rejects/ignores some default
# python-urllib agents.
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

# If the newest meeting we can discover is older than this, the source is
# probably dead (exactly what happened with the Archive Center). Shout about it.
STALENESS_DAYS = 45

CIVICCLERK_TENANTS = {
    "city_council": {
        "name": "Pueblo City Council",
        "api": "https://puebloco.api.civicclerk.com/v1",
        "portal": "https://puebloco.portal.civicclerk.com",
        # Matches both "City Council Regular Meeting" and "... Work Session".
        "category_contains": "City Council",
    },
    "county_commissioners": {
        "name": "Pueblo County Board of County Commissioners",
        "api": "https://pueblococo.api.civicclerk.com/v1",
        "portal": "https://pueblococo.portal.civicclerk.com",
        "category_contains": "Board of County Commissioners",
    },
}

# Legacy CivicPlus Archive Center. DEFUNCT (newest entry 2022-05-23, most
# content 2013 and older). Retained only as an explicitly-labeled last-resort
# fallback so we can tell "the new API broke" apart from "we have no source".
LEGACY_ARCHIVE_FALLBACK = {
    "city_council": "https://www.pueblo.us/Archive.aspx?AMID=37",
}

# Document types worth pulling for keyword scanning, in priority order.
DEFAULT_FILE_TYPES = ("Agenda", "Agenda Packet")


def upcoming_cutoff(days_ahead: int = 21) -> str:
    """ISO-Z upper bound for $filter, to exclude year-2100 template rows."""
    when = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=days_ahead)
    return when.strftime("%Y-%m-%dT%H:%M:%SZ")


def file_url(api_base: str, file_id: int) -> str:
    """Direct PDF stream URL for a published file."""
    return f"{api_base}/Meetings/GetMeetingFileStream(fileId={file_id},plainText=false)"


def _get_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", "ignore"))


def fetch_meetings(
    source: str,
    limit: int = 10,
    file_types: tuple[str, ...] = DEFAULT_FILE_TYPES,
    days_ahead: int = 21,
    timeout: int = 30,
) -> list[dict]:
    """
    Return up to `limit` meetings for `source`, NEWEST FIRST.

    Each meeting is a dict:
        {"date": "2026-07-27", "category": "City Council Regular Meeting",
         "event_id": 1507, "portal_url": "...",
         "files": [{"type": "Agenda", "file_id": 7227, "name": ..., "url": ...}]}

    Raises urllib.error.URLError / ValueError on transport or payload failure so
    callers can decide whether to fall back.
    """
    if source not in CIVICCLERK_TENANTS:
        raise KeyError(f"unknown source {source!r}")
    tenant = CIVICCLERK_TENANTS[source]
    api = tenant["api"]

    query = urllib.parse.urlencode(
        {
            "$filter": (
                f"startDateTime lt {upcoming_cutoff(days_ahead)} "
                f"and contains(eventCategoryName,'{tenant['category_contains']}')"
            ),
            "$orderby": "startDateTime desc",
            # Over-fetch: some events publish no documents at all.
            "$top": str(max(limit * 3, 15)),
        }
    )
    payload = _get_json(f"{api}/Events?{query}", timeout=timeout)

    meetings: list[dict] = []
    for event in payload.get("value", []):
        start = (event.get("startDateTime") or "")[:10]
        if not start:
            continue
        files = []
        for published in event.get("publishedFiles") or []:
            if file_types and published.get("type") not in file_types:
                continue
            fid = published.get("fileId")
            if not fid:
                continue
            files.append(
                {
                    "type": published.get("type") or "Document",
                    "file_id": fid,
                    "name": published.get("name") or "",
                    "url": file_url(api, fid),
                }
            )
        if not files:
            continue
        meetings.append(
            {
                "date": start,
                "category": event.get("eventCategoryName") or tenant["name"],
                "event_id": event.get("id"),
                "portal_url": f"{tenant['portal']}/event/{event.get('id')}/overview",
                "files": files,
            }
        )

    # The API already sorts desc, but never trust it -- walking backwards
    # through 2012 is the bug we are fixing.
    meetings.sort(key=lambda m: m["date"], reverse=True)
    return meetings[:limit]


def staleness_warning(source_label: str, meetings: list[dict]) -> str | None:
    """
    Return a loud multi-line WARNING if the newest meeting looks too old (or if
    there are no meetings at all), else None.

    This is the guard that stops a dead source from masquerading as
    "no keyword matches found".
    """
    banner = "!" * 72
    if not meetings:
        return (
            f"\n{banner}\n"
            f"WARNING: NO MEETINGS DISCOVERED for {source_label}.\n"
            f"The data source may be DEAD or its API contract may have changed.\n"
            f"Do NOT read an empty keyword scan as an all-clear.\n"
            f"{banner}\n"
        )

    newest = meetings[0]["date"]
    try:
        newest_date = datetime.date.fromisoformat(newest)
    except ValueError:
        return (
            f"\n{banner}\n"
            f"WARNING: unparseable newest meeting date {newest!r} for {source_label}.\n"
            f"{banner}\n"
        )

    age = (datetime.date.today() - newest_date).days
    if age > STALENESS_DAYS:
        return (
            f"\n{banner}\n"
            f"WARNING: STALE SOURCE for {source_label}.\n"
            f"Newest discovered meeting is {newest} ({age} days old; "
            f"threshold {STALENESS_DAYS} days).\n"
            f"This is how the defunct Archive Center produced a FALSE ALL-CLEAR\n"
            f"on a 2013 agenda. Verify the source before trusting any scan result.\n"
            f"{banner}\n"
        )
    return None
