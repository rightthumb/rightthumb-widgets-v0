#!/usr/bin/env python3
from __future__ import annotations

"""
server_snips.py — A tiny “server snippet manager” you can import or run.

- Stores common server snippets in a nested dict (categories -> items).
- Uses dot-delimited keys like: php.phpinfo, web.apache_vhost, systemd.service_simple
- No-arg run prints a help menu (available keys + descriptions).
- Can create OR append to a target file (with a timestamped backup by default).

Examples:
  ./server_snips.py
  ./server_snips.py list
  ./server_snips.py show php.phpinfo
  ./server_snips.py apply php.phpinfo --to /var/www/html/phpinfo.php --mode create
  ./server_snips.py apply security.sshd_hardening --to /etc/ssh/sshd_config --mode append
  ./server_snips.py apply web.nginx_server_block --to /etc/nginx/conf.d/example.conf --var domain=example.com --var root=/var/www/example
"""



import argparse
import datetime as _dt
import os
import re
import shutil
import sys
from dataclasses import dataclass
from typing import Dict, Any, Tuple, List, Optional


# -----------------------------
# Snippet registry (nested dict)
# -----------------------------

SNIPS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "php": {
        "phpinfo": {
            "desc": "Create a phpinfo() page (safe-ish; remove after use).",
            "default_filename": "phpinfo.php",
            "content": """<?php
// phpinfo.php
// NOTE: Remove this file after debugging.
phpinfo();
""",
        },
        "opcache_status": {
            "desc": "Simple OPcache status page (requires opcache enabled).",
            "default_filename": "opcache.php",
            "content": """<?php
// opcache.php
header('Content-Type: text/plain; charset=utf-8');
if (!function_exists('opcache_get_status')) {
    echo "opcache_get_status() not available\\n";
    exit;
}
$status = opcache_get_status(false);
print_r($status);
""",
        },
        "composer_auth_json_stub": {
            "desc": "Composer auth.json stub (private repos / tokens).",
            "default_filename": "auth.json",
            "content": """{
  "http-basic": {
    "example.com": {
      "username": "YOUR_USER",
      "password": "YOUR_TOKEN_OR_PASSWORD"
    }
  },
  "github-oauth": {
    "github.com": "YOUR_GITHUB_TOKEN"
  }
}
""",
        },
    },

    "web": {
        "apache_vhost": {
            "desc": "Apache VirtualHost (80) basic template.",
            "default_filename": "{domain}.conf",
            "content": """<VirtualHost *:80>
    ServerName {domain}
    DocumentRoot {root}

    <Directory "{root}">
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog {log_dir}/{domain}_error.log
    CustomLog {log_dir}/{domain}_access.log combined
</VirtualHost>
""",
            "vars": {"domain": "example.com", "root": "/var/www/example", "log_dir": "/var/log/httpd"},
        },
        "nginx_server_block": {
            "desc": "Nginx server block (80) basic template.",
            "default_filename": "{domain}.conf",
            "content": """server {
    listen 80;
    server_name {domain};

    root {root};
    index index.php index.html;

    access_log {log_dir}/{domain}_access.log;
    error_log  {log_dir}/{domain}_error.log;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \\.php$ {
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass {php_fpm};
    }
}
""",
            "vars": {
                "domain": "example.com",
                "root": "/var/www/example",
                "log_dir": "/var/log/nginx",
                "php_fpm": "127.0.0.1:9000",
            },
        },
        "robots_allow_all": {
            "desc": "robots.txt allow all.",
            "default_filename": "robots.txt",
            "content": """User-agent: *
Disallow:
""",
        },
        "robots_disallow_all": {
            "desc": "robots.txt disallow all.",
            "default_filename": "robots.txt",
            "content": """User-agent: *
Disallow: /
""",
        },
    },

    "systemd": {
        "service_simple": {
            "desc": "Systemd service template for a long-running app.",
            "default_filename": "{name}.service",
            "content": """[Unit]
Description={desc}
After=network.target

[Service]
Type=simple
User={user}
WorkingDirectory={workdir}
ExecStart={exec_start}
Restart=always
RestartSec=2
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
""",
            "vars": {
                "name": "myapp",
                "desc": "My App Service",
                "user": "root",
                "workdir": "/opt/myapp",
                "exec_start": "/usr/bin/python3 /opt/myapp/app.py",
            },
        },
        "timer_daily": {
            "desc": "Systemd timer (daily) + matching service stub name.",
            "default_filename": "{name}.timer",
            "content": """[Unit]
Description=Daily timer for {name}

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
""",
            "vars": {"name": "myjob"},
        },
    },

    "security": {
        "sshd_hardening": {
            "desc": "Append-friendly sshd_config hardening lines (review before enabling).",
            "default_filename": "sshd_config",
            "content": """# --- Hardening (review before enabling) ---
PasswordAuthentication no
PermitRootLogin prohibit-password
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding no
# Consider: AllowUsers youruser
# ------------------------------------------
""",
        },
        "fail2ban_jail_local": {
            "desc": "fail2ban jail.local minimal defaults.",
            "default_filename": "jail.local",
            "content": """[DEFAULT]
bantime  = 1h
findtime = 10m
maxretry = 5

[sshd]
enabled = true
""",
        },
        "ufw_basics": {
            "desc": "UFW basics (commands as comments).",
            "default_filename": "ufw_basics.txt",
            "content": """# UFW quick setup (run as root)
# ufw default deny incoming
# ufw default allow outgoing
# ufw allow 22/tcp
# ufw allow 80/tcp
# ufw allow 443/tcp
# ufw enable
# ufw status verbose
""",
        },
    },

    "ops": {
        "logrotate_app": {
            "desc": "logrotate snippet for /var/log/<app>/*.log",
            "default_filename": "{app}",
            "content": """/var/log/{app}/*.log {
    daily
    rotate 14
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
}
""",
            "vars": {"app": "myapp"},
        },
        "cron_daily_stub": {
            "desc": "Crontab line stub for daily job.",
            "default_filename": "crontab_snip.txt",
            "content": """# Run daily at 03:17
17 3 * * * {user} {cmd} >> {log} 2>&1
""",
            "vars": {"user": "root", "cmd": "/usr/local/bin/myjob", "log": "/var/log/myjob/cron.log"},
        },
        "docker_compose_web_php": {
            "desc": "docker-compose.yml: nginx + php-fpm skeleton.",
            "default_filename": "docker-compose.yml",
            "content": """services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./public:/var/www/html:ro
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - php

  php:
    image: php:8.3-fpm-alpine
    volumes:
      - ./public:/var/www/html:rw
""",
        },
        "nginx_conf_php_fpm": {
            "desc": "nginx.conf for the compose setup (php-fpm upstream = php:9000).",
            "default_filename": "nginx.conf",
            "content": """server {
    listen 80;
    server_name _;
    root /var/www/html;
    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \\.php$ {
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass php:9000;
    }
}
""",
        },
    },
}


# -----------------------------
# Helpers
# -----------------------------

@dataclass(frozen=True)
class Snip:
    key: str
    desc: str
    default_filename: str
    content: str
    vars: Dict[str, str]


def _flatten_snips() -> Dict[str, Snip]:
    flat: Dict[str, Snip] = {}
    for cat, items in SNIPS.items():
        for name, meta in items.items():
            key = f"{cat}.{name}"
            flat[key] = Snip(
                key=key,
                desc=str(meta.get("desc", "")).strip(),
                default_filename=str(meta.get("default_filename", name)).strip(),
                content=str(meta.get("content", "")),
                vars=dict(meta.get("vars", {})),
            )
    return flat


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def _safe_mkdirs(path: str) -> None:
    d = os.path.dirname(os.path.abspath(path))
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)


def _backup_file(path: str) -> Optional[str]:
    if not os.path.exists(path):
        return None
    bpath = f"{path}.bak.{_now_stamp()}"
    shutil.copy2(path, bpath)
    return bpath


def _parse_vars(kvs: List[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for kv in kvs:
        if "=" not in kv:
            raise ValueError(f'Bad --var "{kv}" (expected key=value)')
        k, v = kv.split("=", 1)
        k = k.strip()
        if not k:
            raise ValueError(f'Bad --var "{kv}" (empty key)')
        out[k] = v
    return out


def _render(template: str, vars_map: Dict[str, str]) -> str:
    try:
        return template.format(**vars_map)
    except KeyError as e:
        missing = str(e).strip("'")
        raise KeyError(f"Missing variable: {missing}") from None


def _suggest_to_path(s: Snip, vars_map: Dict[str, str]) -> str:
    name = _render(s.default_filename, vars_map) if "{" in s.default_filename else s.default_filename
    return os.path.abspath(name)


def _print_list(flat: Dict[str, Snip]) -> None:
    # grouped by category, stable order
    cats: Dict[str, List[Snip]] = {}
    for k, sn in flat.items():
        cat = k.split(".", 1)[0]
        cats.setdefault(cat, []).append(sn)
    for cat in sorted(cats.keys()):
        print(f"\n{cat}:")
        for sn in sorted(cats[cat], key=lambda x: x.key):
            print(f"  {sn.key:<28}  {sn.desc}")


def _print_snip(sn: Snip) -> None:
    print(f"{sn.key} — {sn.desc}\n")
    if sn.vars:
        print("Default vars (override with --var key=value):")
        for k in sorted(sn.vars.keys()):
            print(f"  {k}={sn.vars[k]}")
        print("")
    print(sn.content.rstrip() + "\n")


# -----------------------------
# Core operations
# -----------------------------

def apply_snip(
    sn: Snip,
    to_path: str,
    mode: str,
    vars_override: Dict[str, str],
    make_backup: bool = True,
    ensure_newline: bool = True,
    dry_run: bool = False,
) -> Tuple[str, Optional[str], int]:
    """
    Returns: (to_path, backup_path, bytes_written)
    """
    mode = mode.lower().strip()
    if mode not in {"create", "append"}:
        raise ValueError("mode must be create or append")

    vars_map = dict(sn.vars)
    vars_map.update(vars_override)

    content = _render(sn.content, vars_map)
    if ensure_newline and not content.endswith("\n"):
        content += "\n"

    _safe_mkdirs(to_path)

    backup_path = _backup_file(to_path) if make_backup else None

    if dry_run:
        return to_path, backup_path, len(content.encode("utf-8"))

    if mode == "create":
        with open(to_path, "w", encoding="utf-8") as f:
            f.write(content)
        return to_path, backup_path, len(content.encode("utf-8"))

    # append
    # Ensure a separating newline if file exists and doesn't end with newline.
    if os.path.exists(to_path) and os.path.getsize(to_path) > 0 and ensure_newline:
        with open(to_path, "rb") as rf:
            rf.seek(-1, os.SEEK_END)
            last = rf.read(1)
        if last != b"\n":
            content = "\n" + content

    with open(to_path, "a", encoding="utf-8") as f:
        f.write(content)
    return to_path, backup_path, len(content.encode("utf-8"))


# -----------------------------
# CLI
# -----------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="server_snips.py",
        add_help=True,
        formatter_class=argparse.RawTextHelpFormatter,
        description="Create/append common server snippets by dot-key.",
    )

    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("list", help="List all available snippet keys.")

    show = sub.add_parser("show", help="Print a snippet to stdout.")
    show.add_argument("key", help="Dot key (e.g., php.phpinfo)")

    applyp = sub.add_parser("apply", help="Write a snippet to a file.")
    applyp.add_argument("key", help="Dot key (e.g., web.nginx_server_block)")
    applyp.add_argument("--to", dest="to_path", default=None, help="Target file path.")
    applyp.add_argument("--mode", choices=["create", "append"], default="create", help="Write mode.")
    applyp.add_argument("--no-backup", action="store_true", help="Do not create .bak.* backup if file exists.")
    applyp.add_argument("--dry-run", action="store_true", help="Show what would happen without writing.")
    applyp.add_argument("--var", action="append", default=[], help="Template variables: key=value (repeatable)")
    applyp.add_argument("--print", dest="also_print", action="store_true", help="Also print rendered content.")

    return p


def main(argv: List[str]) -> int:
    flat = _flatten_snips()

    # No-arg help menu
    if len(argv) == 0:
        print("server_snips.py — available snippet keys:")
        _print_list(flat)
        print("\nTry:")
        print("  server_snips.py list")
        print("  server_snips.py show php.phpinfo")
        print("  server_snips.py apply php.phpinfo --to /var/www/html/phpinfo.php --mode create")
        return 0

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd in (None, ""):
        # If they passed flags but no command, argparse will already show help;
        # still, be friendly.
        parser.print_help()
        return 0

    if args.cmd == "list":
        _print_list(flat)
        return 0

    if args.cmd == "show":
        key = args.key.strip()
        sn = flat.get(key)
        if not sn:
            print(f'Unknown key: "{key}"\n', file=sys.stderr)
            _print_list(flat)
            return 2
        _print_snip(sn)
        return 0

    if args.cmd == "apply":
        key = args.key.strip()
        sn = flat.get(key)
        if not sn:
            print(f'Unknown key: "{key}"\n', file=sys.stderr)
            _print_list(flat)
            return 2

        try:
            vars_override = _parse_vars(args.var)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 2

        # Choose target path:
        if args.to_path:
            to_path = os.path.abspath(args.to_path)
        else:
            # default to rendered default filename in CWD
            to_path = _suggest_to_path(sn, {**sn.vars, **vars_override})

        try:
            rendered = _render(sn.content, {**sn.vars, **vars_override})
        except Exception as e:
            print(f"Render error: {e}", file=sys.stderr)
            return 2

        try:
            out_path, bak_path, nbytes = apply_snip(
                sn=sn,
                to_path=to_path,
                mode=args.mode,
                vars_override=vars_override,
                make_backup=not args.no_backup,
                dry_run=args.dry_run,
            )
        except Exception as e:
            print(f"Write error: {e}", file=sys.stderr)
            return 3

        action = "WOULD WRITE" if args.dry_run else "WROTE"
        print(f"{action}: {key}")
        print(f"  to:   {out_path}")
        if bak_path:
            print(f"  bak:  {bak_path}")
        print(f"  bytes:{nbytes}")

        if args.also_print:
            print("\n--- rendered ---")
            print(rendered.rstrip() + "\n")

        return 0

    print("Unknown command.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
