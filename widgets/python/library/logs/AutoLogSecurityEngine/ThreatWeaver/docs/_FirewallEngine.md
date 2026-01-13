# FirewallEngine — CLI Switch Reference & Tuning Guide

This file explains every switch supported by `FirewallEngine.py`, their defaults, and how they influence detection and blocking.
It also includes rationale (“why you might change it”) and sample values for common use cases.

---

## 1. Global CLI Switches

### `--file PATH`

**Required.**
The path to the log file you want to process. Supports plain text, `.csv`, or `.gz`.

* **Example:** `--file /var/log/secure`

---

### `--log-type {auto, secure, auth, ssh, syslog, apache_access, apache_error, dmesg, exim_mail, windows_event, procmon, csv, unknown}`

Force the parser type.

* **`auto`** = attempt to detect based on filename or line regex.
* Use explicit type when auto-detection is unreliable.

---

### `--firewall {json, db, iptables, iptables, ufw, csf, firewalld, shorewall, nftables, pfsense, ipfire, vyos}`

Choose how block decisions are recorded or applied.

* **json** → appends actions to `decisions.jsonl`.
* **db** → stores actions in SQLite ledger.
* **iptables** → logs iptables DROP commands (does *not* execute).
* **iptables\_exec** → actually executes DROP rules.
* **csf** → executes CSF deny rules (cPanel/WHM).
* Others (ufw, firewalld, etc.) log the command you could run manually.

---

### `--json-out PATH`

Where to write JSON decisions if `--firewall json` is used.

---

### `--sqlite PATH`

Where to write decisions if `--firewall db` is used.

---

### `--event-sqlite PATH`

**Deprecated.** Older option to archive parsed events. Prefer `--ingest-events-sqlite`.

---

### `--ingest-events-sqlite PATH`

Path to the event ledger (normalized log events).
This DB can be queried later with SQL and used for **ledger-wide blocking**.

---

### `--ingest-summary`

Prints a one-line summary of parsed and inserted rows.

---

### `--dry`

Do not actually perform block/allow actions. Log only.

---

### `--max-decisions N`

Stop after **N blocks** in a single run. Useful for testing.

---

### `--whitelist-ip PATH`

File containing IPs or CIDRs to never block.

* Supports `.txt` or `.csv`.
* CSV must have a header with `ip` or `cidr` column.

---

### `--whitelist-fp PATH`

JSON file containing fingerprints (e.g., device IDs) to exempt from blocking.

---

### Logging controls

* `--verbose` → DEBUG-level logs.
* `--quiet` → WARNING+ only.
* `--log-json` → structured JSON logs to stdout.

---

### `--version`

Show version and exit.

---

## 2. Global Rule Thresholds & Scoring

All log-type-specific rules feed into the **same scoring system**.

### `--score-block N`

**Default:** 10
Minimum score required before an IP is blocked.

---

### SSH / Auth Log Parameters

* `--ssh-fail-thresh N`
  **Default:** 6
  Failed login count before adding a bonus.
* `--ssh-fail-score N`
  **Default:** 2
  Points per failed login.
* `--ssh-fail-bonus N`
  **Default:** 6
  Extra points once the threshold is hit.

---

### Apache Access Parameters

* `--wp-score N`
  **Default:** 5
  Points per `wp-*` probe (`wp-login.php`, etc.).
* `--susp-score N`
  **Default:** 4
  Points per suspicious extension (`.php`, `.env`, `.git`, `.bak`).
* `--burst-404-thresh N`
  **Default:** 20
  Number of 404s in window to consider a “burst.”
* `--burst-404-bonus N`
  **Default:** 10
  Points added once burst triggered.

---

### Apache Error Parameters

* `--apache-err-thresh N`
  **Default:** 8
  Error events per IP before adding bonus.
* `--apache-err-bonus N`
  **Default:** 8
  Points added if threshold exceeded.

---

### Windowing

* `--window-min N`
  **Default:** 5
  Size of sliding time window (minutes) used for scoring **per run**.
  Only events newer than `now - N minutes` are considered.
  Larger values widen detection; smaller = faster reaction.

---

## 3. Ledger-Wide Thresholds (Global Counts)

When `--ledger-scan` is used, decisions are based on totals across the **ingest DB**, not just the current window.

* `--ledger-scan`
  Enable global thresholds.
* `--ledger-since-min N`
  **Default:** 1440 (1 day)
  Only count events newer than this. Use `0` for *all time*.
* `--ledger-min-total N`
  **Default:** 500
  Block any IP with at least N events (all kinds).
* `--ledger-min-ssh N`
  **Default:** 100
  Block any IP with at least N SSH failures.

---

## 4. Per-Log-Type Behavior

### Auth / Secure / SSH Logs

* Events: `ssh_failed_login`, or raw lines like “Failed password,” “invalid user.”
* Each fail increments score by `ssh-fail-score`.
* If fails ≥ `ssh-fail-thresh`, add `ssh-fail-bonus`.
* If score ≥ `score-block`, IP is blocked.

---

### Syslog (Generic)

* Looks for `invalid user` messages.
* Each event multiplies by `--syslog-invalid-user-score` (default: 2).
* Block when ≥ `score-block`.

---

### Apache Access Logs

* 404s:

  * Each `wp-*` request adds `wp-score`.
  * Suspicious extensions add `susp-score`.
  * If total 404s ≥ `burst-404-thresh`, add `burst-404-bonus`.
* Block when score ≥ `score-block`.

---

### Apache Error Logs

* Counts errors per IP.
* If ≥ `apache-err-thresh`, add `apache-err-bonus`.
* Block if score ≥ `score-block`.

---

### Dmesg / Exim / Windows / Procmon

* Parsers in place, but blocking rules are stubs (currently no scoring logic).

---

## 5. Profiles (Suggested Tunings)

* **Aggressive:**

  ```
  --window-min 60
  --ssh-fail-thresh 2
  --ssh-fail-score 4
  --ssh-fail-bonus 6
  --score-block 6
  --ledger-scan --ledger-since-min 1440 --ledger-min-ssh 20 --ledger-min-total 100
  ```

* **Balanced (default-ish):**

  ```
  --window-min 300
  --ssh-fail-thresh 3
  --ssh-fail-score 2
  --ssh-fail-bonus 4
  --score-block 8
  --ledger-scan --ledger-since-min 1440 --ledger-min-ssh 50 --ledger-min-total 500
  ```

* **Tolerant:**

  ```
  --window-min 60
  --ssh-fail-thresh 6
  --ssh-fail-score 1
  --ssh-fail-bonus 2
  --score-block 12
  --ledger-scan --ledger-since-min 4320 --ledger-min-ssh 200 --ledger-min-total 2000
  ```

---

# Summary

* **Global switches** control ingestion, whitelists, firewall backend, and logging.
* **Thresholds** (`--ssh-fail-*`, `--apache-*`, etc.) convert raw events into a numeric score.
* **Score ≥ --score-block = block.**
* **Windowing** (`--window-min`) limits analysis to a time slice.
* **Ledger-scan** extends detection across the ingest DB, so you catch long-running attackers.

## Usage

  ```sh
cp -r /opt/rightthumb-widgets-v0/widgets/python/library/logs/AutoLogSecurityEngine/ThreatWeaver/ /opt/ThreatWeaver
  ```

  ```sh
# <ThreatWeaver>

# RHEL/Alma/CentOS secure log (every 5m)
*/5 * * * * /opt/ThreatWeaver/ThreatWeaver_Cron.sh --secure >> /opt/_ThreatWeaver.log 

# Debian/Ubuntu auth.log (every 5m)
*/5 * * * * /opt/ThreatWeaver/ThreatWeaver_Cron.sh --auth >> /opt/_ThreatWeaver.log 

# Apache access (cPanel) (every 10m)
*/10 * * * * /opt/ThreatWeaver/ThreatWeaver_Cron.sh --apache-access >> /opt/_ThreatWeaver.log 

# Apache error (cPanel) (every 10m)
*/10 * * * * /opt/ThreatWeaver/ThreatWeaver_Cron.sh --apache-error >> /opt/_ThreatWeaver.log 

# </ThreatWeaver>
  ```
