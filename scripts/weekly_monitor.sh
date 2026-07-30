#!/bin/bash
#
# Weekly monitoring script for La Raza VII.I.IX
#
# This script:
# 1. Downloads latest City Council agendas
# 2. Scans for surveillance/immigration keywords
# 3. Generates alert report
# 4. Optionally sends notification
#
# Usage:
#   ./weekly_monitor.sh              # Run all checks
#   ./weekly_monitor.sh --notify     # Run and send notification if alerts found
#
# Cron setup (run every Sunday at 6pm):
#   0 18 * * 0 /path/to/laraza/scripts/weekly_monitor.sh >> /path/to/laraza/logs/weekly.log 2>&1
#

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$PROJECT_DIR/logs"
ALERT_FILE="$PROJECT_DIR/docs/agenda_alerts.md"

# Ensure we're in the project directory
cd "$PROJECT_DIR"

# Create logs directory if needed
mkdir -p "$LOG_DIR"

echo "========================================"
echo "La Raza Weekly Monitor"
echo "Date: $(date)"
echo "========================================"

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: python3 not found"
    exit 1
fi

# Run the agenda monitor.
# `set -e` is active, so guard the call — exit 2 (matches) and exit 3 (stale source)
# are expected outcomes, not script failures.
echo ""
echo "Running agenda monitor..."
MONITOR_EXIT=0
python3 scripts/monitor_agendas.py --source all --limit 5 --output "$ALERT_FILE" || MONITOR_EXIT=$?

# Check results
if [ $MONITOR_EXIT -eq 2 ]; then
    echo ""
    echo "⚠️  ALERTS FOUND - Review $ALERT_FILE"

    # If --notify flag passed, could add notification here
    if [ "$1" == "--notify" ]; then
        echo ""
        echo "Notification requested - add your notification method here"
        # Examples:
        # - Send email: mail -s "La Raza Alert" user@example.com < "$ALERT_FILE"
        # - Post to webhook: curl -X POST -d @"$ALERT_FILE" https://webhook.url
        # - Desktop notification: notify-send "La Raza Alert" "Keyword matches found"
    fi
elif [ $MONITOR_EXIT -eq 3 ]; then
    # This is the failure mode that went undetected from Nov 2025 to Jul 2026:
    # a dead source produces an empty scan that LOOKS like good news.
    echo ""
    echo "########################################################################"
    echo "🛑 STALE OR EMPTY SOURCE - THIS IS *NOT* AN ALL-CLEAR."
    echo ""
    echo "   No agenda was verified as current, so an empty keyword scan means"
    echo "   nothing. Pueblo may have migrated platforms again."
    echo "   Check scripts/pueblo_sources.py and the newest-meeting date above."
    echo "########################################################################"

    if [ "$1" == "--notify" ]; then
        echo "Notification requested - a stale source deserves one as much as an alert."
    fi
elif [ $MONITOR_EXIT -eq 0 ]; then
    echo ""
    echo "✓ No keyword matches - and the source was verified fresh."
else
    echo ""
    echo "ERROR: Monitor script failed with exit code $MONITOR_EXIT"
fi

# Optional: Update the git repo
# Uncomment if you want automatic commits of new data
# echo ""
# echo "Checking for changes to commit..."
# if [ -n "$(git status --porcelain docs/agendas/)" ]; then
#     git add docs/agendas/
#     git commit -m "Auto: Downloaded new agendas $(date +%Y-%m-%d)"
# fi

echo ""
echo "========================================"
echo "Monitor complete: $(date)"
echo "========================================"

exit $MONITOR_EXIT
