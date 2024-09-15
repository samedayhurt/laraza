#### WiFi Direction Finding
1. **How WiFi Direction Finding Works**:
   - WiFi-enabled devices periodically broadcast signals (such as probe requests) to identify nearby access points.
   - By measuring signal strength (RSSI – Received Signal Strength Indicator) and triangulating signals from multiple access points or antennas, it's possible to locate the transmitting device.
   
2. **Tools for WiFi Direction Finding**:
   - **Kismet**: A popular WiFi monitoring tool that captures packets and shows the presence of nearby devices.
   - **airodump-ng**: Part of the **Aircrack-ng** suite, used for capturing and displaying WiFi traffic.
   - **WiFi Pineapple**: A tool used to create fake access points and track connected devices.
   
3. **Setting Up for Direction Finding**:
   - Use a directional antenna (such as a Yagi antenna) to focus on a specific area and enhance your ability to determine the direction of a signal source.
   - Move around to different locations to triangulate the position of the target device using the signal strength.

4. **Defending Against WiFi Tracking**:
   - Use a **Faraday bag** to block WiFi signals when not in use.
   - Disable WiFi on devices when not needed, or use a randomized MAC address to prevent tracking by hardware identifiers.
   - Regularly audit which devices are connecting to your network and ensure unauthorized devices are blocked.
     
#### Bluetooth Direction Finding
1. **How Bluetooth Tracking Works**:
   - Bluetooth devices broadcast their presence when in discoverable mode, making them easy to detect.
   - Even when not in discoverable mode, devices that communicate via Bluetooth (e.g., BLE devices) can still be tracked by sniffing their communication signals.
   - Direction finding can be performed using **RSSI** or **Angle of Arrival (AoA)** techniques to pinpoint the location of a Bluetooth device.

2. **Tools for Bluetooth Direction Finding**:
   - **Blue Hydra**: A tool for detecting and identifying Bluetooth devices, including BLE.
   - **ubertooth**: A device and toolset for capturing and analyzing Bluetooth signals, including raw Bluetooth traffic.
   - **Blue Sonar**: A script used with **Kismet** to map out Bluetooth devices and track their movement over time.
   
3. **Setting Up for Bluetooth Direction Finding**:
   - Use a **Ubertooth One** or similar device to capture Bluetooth signals and analyze signal strength.
   - As with WiFi, you can use a directional antenna to narrow down the location of a target device.

4. **Defending Against Bluetooth Tracking**:
   - Disable Bluetooth when not in use, especially in public areas where tracking is more likely.
   - Use randomized Bluetooth addresses to prevent devices from being easily identifiable.
   - Be cautious of connecting to unknown Bluetooth devices, as they may be used for tracking or exploitation.

#### Practical Use Cases:
1. **Security Audits**:
   - WiFi and Bluetooth direction finding can be used to detect unauthorized devices in a secured facility.
   - Identify rogue access points or unauthorized Bluetooth devices that could pose a security risk.

2. **Tracking Devices**:
   - Law enforcement or security personnel can use direction finding to locate stolen devices or track suspicious activities in public spaces.
   - Protesters or activists could be tracked if their devices are broadcasting WiFi or Bluetooth signals, making it essential to minimize broadcast exposure.

3. **Network Diagnostics**:
   - Use WiFi direction finding to troubleshoot network issues, identify areas with weak coverage, or locate network interference sources.
   - Bluetooth direction finding can be used to track down malfunctioning IoT devices that are disrupting network communications.

