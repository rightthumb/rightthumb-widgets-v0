def fqdn2ip(value: str) -> str:
	try:
		result = resolveFqdn(value)
	except Exception:
		return '127.0.0.1'

	# fqdn2ip may return:
	# - list[str]
	# - {'ipv4': [...], 'ipv6': [...]}

	ips = []

	if isinstance(result, dict):
		ips.extend(result.get('ipv4', []))
		ips.extend(result.get('ipv6', []))
	elif isinstance(result, list):
		ips.extend(result)

	# remove empties / ensure strings
	ips = [str(ip) for ip in ips if ip]

	if len(ips) == 1:
		return ips[0]

	return '127.0.0.1'



import socket
import ipaddress
from typing import List, Dict, Union

def resolveFqdn(value: str, *, family: str = "any", unique: bool = True) -> Union[List[str], Dict[str, List[str]]]:
    """
    Resolve an FQDN or return IPs directly if already an IP.
    """

    # ---- short-circuit if already an IP ----
    try:
        ip = ipaddress.ip_address(value)
        if ip.version == 4:
            return [value] if family in ("any", "ipv4") else []
        else:
            return [value] if family in ("any", "ipv6") else []
    except ValueError:
        pass  # not an IP → continue with DNS

    fam_map = {
        "any": socket.AF_UNSPEC,
        "ipv4": socket.AF_INET,
        "ipv6": socket.AF_INET6,
    }
    if family not in fam_map:
        raise ValueError('family must be "any", "ipv4", or "ipv6"')

    infos = socket.getaddrinfo(value, None, fam_map[family], socket.SOCK_STREAM)

    ipv4, ipv6 = [], []

    for fam, _, _, _, sockaddr in infos:
        ip = sockaddr[0]
        if fam == socket.AF_INET:
            ipv4.append(ip)
        elif fam == socket.AF_INET6:
            ipv6.append(ip)

    if unique:
        ipv4 = list(dict.fromkeys(ipv4))
        ipv6 = list(dict.fromkeys(ipv6))

    if family == "ipv4":
        return ipv4
    if family == "ipv6":
        return ipv6

    return {"ipv4": ipv4, "ipv6": ipv6}



def fqdn2ip1(fqdn: str, *, family: str = "any", unique: bool = True) -> Union[List[str], Dict[str, List[str]]]:
    """
    Resolve an FQDN (e.g., "example.com") to IP address(es).

    Args:
        fqdn: Hostname / FQDN to resolve.
        family: "any" (default), "ipv4", or "ipv6".
        unique: If True, de-duplicate results while preserving order.

    Returns:
        If family != "any": a list of IP strings.
        If family == "any":  {"ipv4": [...], "ipv6": [...]}.

    Raises:
        ValueError: if family is invalid.
        socket.gaierror: if DNS resolution fails.
    """
    import socket
    from typing import List, Dict, Union, Optional
    fam_map = {
        "any": socket.AF_UNSPEC,
        "ipv4": socket.AF_INET,
        "ipv6": socket.AF_INET6,
    }
    if family not in fam_map:
        raise ValueError('family must be "any", "ipv4", or "ipv6"')

    infos = socket.getaddrinfo(fqdn, None, fam_map[family], socket.SOCK_STREAM)

    ipv4: List[str] = []
    ipv6: List[str] = []

    for fam, _, _, _, sockaddr in infos:
        ip = sockaddr[0]
        if fam == socket.AF_INET:
            ipv4.append(ip)
        elif fam == socket.AF_INET6:
            ipv6.append(ip)

    def _dedupe(items: List[str]) -> List[str]:
        if not unique:
            return items
        seen = set()
        out = []
        for x in items:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    ipv4 = _dedupe(ipv4)
    ipv6 = _dedupe(ipv6)

    if family == "ipv4":
        return ipv4
    if family == "ipv6":
        return ipv6
    return {"ipv4": ipv4, "ipv6": ipv6}


# Examples:
# print(fqdn2ip("example.com"))                 # both families
# print(fqdn2ip("example.com", family="ipv4"))  # only IPv4
# print(fqdn2ip("example.com", family="ipv6"))  # only IPv6
