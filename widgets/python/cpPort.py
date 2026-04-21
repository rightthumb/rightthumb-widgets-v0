#!/usr/bin/env python3

import sys
import socket
import threading
import time
import ipaddress


class CpanelWhmPortScanner:
    def __init__(self, cfg=None):
        self.cfg = cfg if isinstance(cfg, dict) else {}

        self.host = self.cfg.get('host')
        self.timeout = float(self.cfg.get('timeout', 0.75))
        self.threads = int(self.cfg.get('threads', 40))
        self.show_closed = bool(self.cfg.get('show_closed', False))
        self.only_open = bool(self.cfg.get('only_open', False))

        self.ports = self._default_ports()

        self._lock = threading.Lock()
        self.open_ports = []
        self.closed_ports = []
        self.errors = []

    def _default_ports(self):
        """
        Core and common cPanel/WHM ports.
        Includes common redirects and WebDAV/WebDisk-related ports.
        """
        return sorted(set([
            20,    # FTP data
            21,    # FTP
            22,    # SSH
            25,    # SMTP
            26,    # Alternate SMTP
            53,    # DNS
            80,    # HTTP
            110,   # POP3
            143,   # IMAP
            443,   # HTTPS
            465,   # SMTPS
            587,   # SMTP submission
            993,   # IMAPS
            995,   # POP3S
            2077,  # WebDAV
            2078,  # WebDAV SSL
            2079,  # WebDisk redirect
            2080,  # cPanel redirect
            2082,  # cPanel
            2083,  # cPanel SSL
            2086,  # WHM
            2087,  # WHM SSL
            2089,  # WHM SSL services / proxy usage in some setups
            2095,  # Webmail
            2096,  # Webmail SSL
        ]))

    def _scan_one(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)

        try:
            result = sock.connect_ex((self.host, port))
            with self._lock:
                if result == 0:
                    self.open_ports.append(port)
                else:
                    self.closed_ports.append(port)
        except Exception as e:
            with self._lock:
                self.closed_ports.append(port)
                self.errors.append({'port': port, 'error': str(e)})
        finally:
            try:
                sock.close()
            except Exception:
                pass

    def run(self):
        started = time.time()
        running = []

        for port in self.ports:
            while True:
                alive = [t for t in running if t.is_alive()]
                running = alive
                if len(running) < self.threads:
                    break
                time.sleep(0.01)

            t = threading.Thread(target=self._scan_one, args=(port,))
            t.daemon = True
            t.start()
            running.append(t)

        for t in running:
            t.join()

        ended = time.time()

        return {
            'host': self.host,
            'open': sorted(self.open_ports),
            'closed': sorted(self.closed_ports),
            'open_count': len(self.open_ports),
            'closed_count': len(self.closed_ports),
            'total': len(self.ports),
            'seconds': round(ended - started, 3),
            'ports_scanned': self.ports[:],
            'errors': self.errors[:],
        }


def is_valid_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except Exception:
        return False


def is_valid_fqdn(value):
    if not isinstance(value, str):
        return False

    value = value.strip()

    if not value:
        return False

    if len(value) > 253:
        return False

    if value.endswith('.'):
        value = value[:-1]

    labels = value.split('.')

    if len(labels) < 2:
        return False

    for label in labels:
        if not label:
            return False
        if len(label) > 63:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        for ch in label:
            if not (ch.isalnum() or ch == '-'):
                return False

    return True


def is_valid_host(value):
    return is_valid_ip(value) or is_valid_fqdn(value)


def print_help():
    script = sys.argv[0] if sys.argv else 'cpanel_scan.py'yes
    UsePAM 
    print(f'''
cPanel / WHM Port Scanner

Usage:
    python3 {script} [switches] <fqdn-or-ip>

Rules:
    - The LAST argument must be the host
    - If the last argument is not a valid FQDN or IP, help is shown

Scans:
    20,21,22,25,26,53,80,110,143,443,465,587,993,995,2077,2078,2079,2080,2082,2083,2086,2087,2089,2095,2096

Switches:
    -1                 Show only open ports
    -closed            Also print closed ports
    -threads <int>     Max worker threads (default: 40)
    -timeout <float>   Socket timeout in seconds (default: 0.75)
    -h
    --help             Show this help

Examples:
    python3 {script} server.example.com
    python3 {script} -1 1.2.3.4
    python3 {script} -threads 80 -timeout 0.35 host.example.com
    python3 {script} -closed host.example.com
'''.strip())


def parse_cli(argv):
    if not argv:
        return None

    if argv[0] in ['-h', '--help']:
        return None

    host = argv[-1]

    if not is_valid_host(host):
        return None

    cfg = {
        'host': host,
        'timeout': 0.75,
        'threads': 40,
        'show_closed': False,
        'only_open': False,
    }

    i = 0
    end = len(argv) - 1  # last arg is reserved for host

    while i < end:
        arg = argv[i]

        if arg in ['-h', '--help']:
            return None

        elif arg == '-1':
            cfg['only_open'] = True

        elif arg == '-closed':
            cfg['show_closed'] = True

        elif arg == '-threads':
            if i + 1 >= end:
                return None
            try:
                cfg['threads'] = int(argv[i + 1])
            except Exception:
                return None
            i += 1

        elif arg == '-timeout':
            if i + 1 >= end:
                return None
            try:
                cfg['timeout'] = float(argv[i + 1])
            except Exception:
                return None
            i += 1

        else:
            return None

        i += 1

    if cfg['threads'] < 1:
        return None

    if cfg['timeout'] <= 0:
        return None

    return cfg


def main():
    argv = sys.argv[1:]
    cfg = parse_cli(argv)

    if not cfg:
        print_help()
        sys.exit(1)

    scanner = CpanelWhmPortScanner(cfg)
    result = scanner.run()

    print(f'Host: {result["host"]}')
    print(f'Total Ports Scanned: {result["total"]}')
    print(f'Open Ports: {result["open_count"]}')
    print(f'Closed Ports: {result["closed_count"]}')
    print(f'Time: {result["seconds"]} seconds')
    print('')

    if result['open']:
        print('Open:')
        for port in result['open']:
            print(f'  {port}')
    else:
        print('Open:')
        print('  none')

    if cfg.get('show_closed') and not cfg.get('only_open'):
        print('')
        print('Closed:')
        for port in result['closed']:
            print(f'  {port}')


if __name__ == '__main__':
    main() 