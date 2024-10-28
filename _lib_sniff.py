from scapy.all import sniff, wrpcap
import os
import colorlog

logger = colorlog.getLogger()
logger.setLevel('DEBUG')
handler = colorlog.StreamHandler()
log_colors = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
}

formatter = colorlog.ColoredFormatter(
    log_colors=log_colors,
)

handler.setFormatter(formatter)
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
))
logger.addHandler(handler)


def enable_monitor_mode(interface='wlan0'):
    if os.name == 'nt':
        logger.error("Monitor mode is not supported on Windows.")
        return
    try:
        os.system(f'ip link set {interface} down')
        os.system(f'iw dev {interface} set type monitor')
        os.system(f'ip link set {interface} up')
        logger.info(f"Monitor mode enabled on {interface}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def sniff_packets(interface='wlan0', count=100, output='capture.pcap'):
    try:
        if os.name == 'nt':
            logger.error("Packet sniffing is not supported on Windows.")
            return
        if not os.path.isdir(os.path.dirname(output)) and os.path.dirname(output) != '':
            logger.error(f"Invalid directory in output path: {os.path.dirname(output)}")
            return
        packets = sniff(iface=interface, count=count)
        wrpcap(output, packets)
        logger.info(f"Captured {len(packets)} packets and saved to {output}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
