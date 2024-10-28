# WARN : This script has not been tested on Linux.

from _lib_sniff import enable_monitor_mode, sniff_packets

# Enable monitor mode
enable_monitor_mode(interface='wlan0')

# Sniff packets
sniff_packets(interface='wlan0', count=100, output='capture.pcap')
