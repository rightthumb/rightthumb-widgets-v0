#!/usr/bin/env python3
import sqlite3
import sys

db = sys.argv[1] if len(sys.argv) > 1 else "/opt/FirewallEngine_actions.sqlite"
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute("SELECT ts, action, ip, reason, seconds FROM firewall_actions ORDER BY ts DESC LIMIT 100")
rows = cur.fetchall()

print(f"{'TS':25} {'ACTION':8} {'IP':20} {'SECONDS':7} REASON")
print("-"*80)
for ts, action, ip, reason, seconds in rows:
    print(f"{ts:25} {action:8} {ip or '-':20} {seconds or '-':7} {reason or ''}")
