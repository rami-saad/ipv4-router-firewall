from ipaddress import ip_address, ip_network

INTERNAL_NETS = [ip_network('10.0.0.0/8'), ip_network('192.168.0.0/16')]

def is_internal(ip: str)->bool:
    a = ip_address(ip)
    return any(a in n for n in INTERNAL_NETS)

def allow_packet(src_ip: str, dst_ip: str, protocol: str)->bool:
    protocol = protocol.lower()

    # Anti-spoof (simplified)
    if not is_internal(src_ip) and (dst_ip.startswith('10.') or dst_ip.startswith('192.168.')) and protocol == 'icmp':
        return False

    # Block external ICMP into internal network
    if protocol == 'icmp' and not is_internal(src_ip) and is_internal(dst_ip):
        return False

    # Default allow
    return True
