#### WiFi Direction Finding
1. **How WiFi Direction Finding Works**:
   - WiFi-enabled devices periodically broadcast signals (such as probe requests) to identify nearby access points.
   - By measuring signal strength (RSSI – Received Signal Strength Indicator) and triangulating signals from multiple access points or antennas, it's possible to locate the transmitting device.
   
2. **Tools for WiFi Direction Finding**:
   - **Kismet**: A popular WiFi monitoring tool that captures packets and shows the presence of nearby devices.
   - **airodump-ng**: Part of the **Aircrack-ng** suite, used for capturing and displaying WiFi traffic.
   - **WiFi Pineapple**: A tool used to create fake access points and track connected devices.
   - **Angry Oxide**: A newer suite of tools used to monitor wifi packets

   #### Kismet Overview
1. **Features**:
   - **Passive Monitoring**: Captures packets without sending any, reducing the chance of detection during security audits or tracking.
   - **WiFi Device Detection**: Identifies not just access points, but also devices connected to or scanning for WiFi networks.
   - **GPS Integration**: Combines GPS data to map out the physical location of WiFi networks, making it ideal for large-area coverage.

2. **Use Case**:
   - **Network Auditing**: Identify all WiFi devices and networks within range for security auditing or penetration testing.
   - **WiFi Direction Finding**: Use Kismet's signal strength indicators (RSSI) to locate specific devices broadcasting WiFi signals.
   - **Wireless Reconnaissance**: For reconnaissance purposes, Kismet can be used to collect detailed information about networks and devices without alerting targets.

3. **How to Use**:
   - Install Kismet on a Linux system with a compatible WiFi adapter in monitor mode.
   - Launch the Kismet server and web interface to monitor nearby WiFi activity in real time.
   - Move with your equipment to track changes in signal strength for targeted devices.
   - For more accurate direction finding, use Kismet with a GPS receiver and map integration.

4. **Best Practices**:
   - Use Kismet with external antennas and GPS for large-scale, outdoor direction finding.
   - Be mindful of noise and interference in urban environments, which can affect the accuracy of RSSI readings.

  #### Angry Oxide Overview
1. **Features**:
   - Designed specifically for WiFi direction finding using **RSSI** (Received Signal Strength Indicator) to estimate the proximity of WiFi devices.
   - Supports **real-time tracking** with a graphical interface, providing visual feedback as you move closer to or further from the target.
   - Can track both **access points** and **client devices** (e.g., smartphones, laptops) that broadcast probe requests.

2. **Use Case**:
   - **Rogue Access Point Detection**: Find unauthorized or malicious WiFi access points that may be compromising a network.
   - **Device Location**: Track down specific devices by following changes in RSSI, typically by physically moving toward stronger signals.
   - **Physical Security Audits**: Identify where WiFi devices are broadcasting to ensure they are not within sensitive areas.

3. **How to Use**:
   - Install Angry Oxide on a Linux system with a supported WiFi adapter capable of monitor mode.
   - Run the tool, which will display a list of nearby WiFi devices (APs and clients).
   - Use a directional antenna to focus on signals from a specific direction.
   - Monitor RSSI values as you move around to find the strongest signal, helping you locate the device.
     
   #### airodump-ng Overview
1. **Features**:
   - **Monitor Mode Capture**: Captures all WiFi traffic within range in real-time.
   - **Client-Access Point Correlation**: Displays which devices are connected to which access points.
   - **Signal Strength (PWR)**: Shows signal strength in decibels, which can be used to locate the source of the transmission.
   - **Channel Hopping**: Scans across WiFi channels to ensure full coverage of all nearby networks and devices.

2. **Use Case**:
   - **Rogue Device Detection**: Find and track unauthorized WiFi devices broadcasting within a network environment.
   - **Signal Direction Finding**: Use signal strength information (PWR values) to estimate the location of a WiFi device.
   - **WiFi Security Testing**: Perform reconnaissance on WiFi networks for security testing or penetration testing purposes.

3. **How to Use**:
   - Run `airodump-ng` with a compatible WiFi adapter in monitor mode.
   - Monitor the PWR values in the airodump-ng output to find the strongest signal. Higher (less negative) PWR values indicate proximity to the target device.
   - Move around with your equipment to track changes in the PWR values, using a directional antenna for more accurate location.

4. **Best Practices**:
   - Combine airodump-ng with **airmon-ng** to ensure that your WiFi adapter is in monitor mode and capturing the correct packets.
   - Rotate between different WiFi channels if the device you are tracking operates on multiple frequencies.
   - Be aware that signal strength can fluctuate depending on environmental factors (e.g., walls, interference), so combine airodump-ng with physical movement for accuracy.


4. **Best Practices**:
   - Combine Angry Oxide with a **Yagi antenna** for more accurate direction finding.
   - Use in environments with minimal signal interference to get more reliable results.

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

