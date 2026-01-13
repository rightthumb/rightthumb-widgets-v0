#!/usr/bin/env python3
"""
ips.py — Extract unique, sorted IP addresses from piped text.

Usage:
  netstat -tupan | python3 ips.py
  ccat established.log | python3 ips.py --v4-only
  cat file | python3 ips.py --v6-only
"""

import sys
import re
import argparse
import ipaddress

def parse_args():
    ap = argparse.ArgumentParser(add_help=True)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--v4-only", dest="v4_only", action="store_true", help="Only output IPv4 addresses")
    g.add_argument("--v6-only", dest="v6_only", action="store_true", help="Only output IPv6 addresses")

    # parse_known_args returns (known, unknown)
    args, unknown = ap.parse_known_args()

    # Keep only the unknown args that start with "-" (ignore others)
    leftover = [u for u in unknown if u.startswith("-")]
    if leftover:
        print(f"Ignoring unrecognized options: {leftover}", file=sys.stderr)

    return args

# IPv4 (optionally with :port) — capture the IP
_IPV4 = re.compile(r'(?<!\d)(\d{1,3}(?:\.\d{1,3}){3})(?::\d+)?')
# [IPv6]:port form — capture inside brackets
_IPV6_BR = re.compile(r'\[([A-Fa-f0-9:]+)\](?::\d+)?')
# Plain IPv6 candidates — will validate to avoid false positives (e.g., times)
_IPV6_PLAIN = re.compile(r'(?<![A-Za-z0-9])([A-Fa-f0-9:]{2,})(?![A-Za-z0-9])')

def extract_ips(text: str):
    found = set()

    # IPv4
    for m in _IPV4.finditer(text):
        ip = m.group(1)
        try:
            addr = ipaddress.ip_address(ip)
            if isinstance(addr, ipaddress.IPv4Address):
                found.add(addr)
        except ValueError:
            pass

    # Bracketed IPv6
    for m in _IPV6_BR.finditer(text):
        ip = m.group(1).split('%', 1)[0]  # strip zone id if present
        try:
            addr = ipaddress.ip_address(ip)
            if isinstance(addr, ipaddress.IPv6Address):
                found.add(addr)
        except ValueError:
            pass

    # Plain IPv6
    for m in _IPV6_PLAIN.finditer(text):
        cand = m.group(1)
        if '.' in cand:
            continue
        if cand.count(':') < 2:
            continue
        ip = cand.split('%', 1)[0]
        # If it looks like host:port (unbracketed), try full then sans :port
        try:
            addr = ipaddress.ip_address(ip)
        except ValueError:
            if ':' in ip and ip.rsplit(':', 1)[-1].isdigit():
                ip = ip.rsplit(':', 1)[0]
        try:
            addr = ipaddress.ip_address(ip)
            if isinstance(addr, ipaddress.IPv6Address):
                found.add(addr)
        except ValueError:
            pass

    return found

def main():
    args = parse_args()
    data = sys.stdin.read()

    addrs = extract_ips(data)

    if args.v4_only:
        addrs = {a for a in addrs if isinstance(a, ipaddress.IPv4Address)}
    elif args.v6_only:
        addrs = {a for a in addrs if isinstance(a, ipaddress.IPv6Address)}

    # Sort: IPv4 before IPv6, then numeric value
    for a in sorted(addrs, key=lambda a: (a.version, int(a))):
        print(str(a))

if __name__ == "__main__":
    main()
