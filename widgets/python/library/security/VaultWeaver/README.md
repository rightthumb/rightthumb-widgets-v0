# VaultWeaver Documentation

*Last updated: 2025-09-03*

## What is VaultWeaver?

VaultWeaver is a local, multi-user authentication and vault manager designed for terminal-centric workflows. It provides:

* **PIN-only daily login** with **terminal-scoped** sessions (uses `Session_ID`).
* Optional **tmux attach/detach persistence** with temporary, admin-granted exceptions.
* **Per-user keychain** for app/API secrets, encrypted-at-rest (LS-derived).
* **File registry** with per-item **DEKs** wrapped by a per-user **Master Key (MK)**.
* **Dual-wrap MK** (password *and* LS), so after a PIN login you can perform MK operations **without password prompts**.
* **Export/import** keychains across users/machines.
* Root-only **policy controls** per device and per user.
* Minimal, auditable file layout with tight permissions.

> ⚠️ **Pepper is critical**. `pepper.bin` participates in the KDF inputs for both PIN and password. If it is lost or changed, existing users **cannot** be unlocked. Back it up securely.

---

## Install

```bash
pip install cryptography
# set a custom base (optional)
# export VAULTWEAVER_BASE=/var/lib/vaultweaver
```

Drop `vaultweaver.py` into your project and import:

```python
from vaultweaver import VaultWeaver
```

---

## Default Folders & Files

By default (if `VAULTWEAVER_BASE` is unset):

* **Windows:** `C:\ProgramData\VaultWeaver`
* **Linux/macOS:** `/opt/VaultWeaver`

Structure:

```
<BASE>/
  secrets/
    pepper.bin               # CRITICAL secret; back it up
  config.json                # global and device/user policy
  audit.jsonl                # append-only audit log
  users/<USERNAME>/
    creds.json               # salts + KDF params (no raw secrets)
    enc_ls.bin               # Login Secret (LS) wrapped by PIN-derived key
    enc_mk.bin               # Master Key (MK) wrapped by password-derived key
    enc_mk_ls.bin            # MK wrapped by LS (enables MK ops after PIN login)
    keychain.bin             # encrypted key-value map (LS-derived key)
    policy.json              # optional per-user overrides
    items/<ITEM_ID>.json     # file registry entries (DEK wrapped by MK)
  sessions/<USERNAME>/<DEVICE_ID>/<TERMINAL_ID>/
    token.json               # terminal-scoped session token
    ls.sealed                # LS sealed to {device,terminal,nonce,expiry}
  run/
```

To change the base:

```bash
# Linux/macOS
export VAULTWEAVER_BASE=/var/lib/vaultweaver
# Windows (PowerShell)
$env:VAULTWEAVER_BASE='C:\\VaultWeaver'
```

---

## Configuration (`config.json`)

Example (recommended):

```json
{
  "global_policy": {
    "session_ttl_seconds": 43200,
    "absolute_lifetime_seconds": 604800,
    "idle_timeout_seconds": 1800,
    "default_persistence": "terminal_only",
    "roaming": "forbid",
    "pin_kdf": { "type": "scrypt", "n": 16384, "r": 8, "p": 1, "length": 32 },
    "pw_kdf":  { "type": "scrypt", "n": 16384, "r": 8, "p": 1, "length": 32 },
    "allow_mk_via_pin": true,
    "max_pin_attempts_soft": 5,
    "max_pin_attempts_hard": 20,
    "cooloff_seconds_soft": 900,
    "cooloff_seconds_hard": 43200,
    "ls_cache": { "mode": "terminal", "ttl_seconds": 43200 }
  },
  "device_overrides": {},
  "user_overrides": {},
  "tmux_temp_persistence": {}
}
```

* `allow_mk_via_pin`: if `true`, MK can be unlocked with the PIN session (via LS) → no password prompts after PIN login.
* `ls_cache.mode`: `terminal` caches LS **per terminal**; `none` disables.
* `device_overrides[device_id]`: `{ allow_persistence, default_persistence, roaming }`.
* `user_overrides[username]`: `{ allow_persistence }` (root/admin only).
* `tmux_temp_persistence["user|device_id|tmux_id"] = expires_at_epoch`.

---

## Security Model (Keys & Wraps)

* **LS (Login Secret)**: random 32 bytes. Stored as `enc_ls.bin = Enc(LS, KEK_pin)`.
* **MK (Master Key)**: random 32 bytes. Stored as:

  * `enc_mk.bin = Enc(MK, KEK_pw)` (password wrap, for rewrap on password change).
  * `enc_mk_ls.bin = Enc(MK, HKDF(LS,"VW-MK-WRAP"))` (enables MK usage after PIN login).
* **Keychain**: JSON map encrypted under `HKDF(LS,"VW-KEYCHAIN")`.
* **Files**: each item has a fresh **DEK**; registry stores `Enc(DEK, MK)`.
* **Sessions**: terminal-scoped token signed with `HKDF(LS,"VW-MAC")` and stored under `sessions/.../token.json`.
* **LS cache**: `ls.sealed` = `Enc(LS, K(device,terminal,nonce), AAD=expiry)`; cleared on logout; expires with session.

> Password changes **rewrap MK** only; files/keychain do not re-encrypt. PIN changes **rewrap LS** only; MK wraps remain valid.

---

## Terminal, tmux & Persistence

* **Terminal scope** uses `Session_ID` (or creates one). Default persistence: `terminal_only`.
* **tmux persistence** is **off by default**. Admin can grant a temporary allow window for a specific tmux pane:

```python
vw.grant_tmux_persistence_temp(username, device_id, tmux_id, ttl_seconds=3600)
```

* Devices can **forbid persistence** outright; per-user allow is also controlled by root.

---

## Python API Quick Start

```python
from vaultweaver import VaultWeaver
vw = VaultWeaver()

# create user
vw.create_user("alice", password="Strong!Pass42", pin="123456")

# one-time PIN per terminal
vw.login_with_pin("alice", pin="123456")

# keychain
vw.set_key("gpt", "sk-...", user="alice")     # no prompt after PIN
print(vw.key("gpt", user="alice"))             # → "sk-..."

# export/import (portable, passphrase-protected)
pkg = vw.export_keychain("alice", passphrase="carry")

vw.create_user("bob", password="AnotherPass!55", pin="876543")
vw.login_with_pin("bob", pin="876543")
vw.import_keychain("bob", pkg, passphrase="carry")

# files (MK via PIN; no password prompt)
item_id = vw.register_file("alice", label="doc1", path=Path("/path/secret.txt"), encrypt_now=True)
plain = vw.decrypt_file("alice", item_id)  # writes output next to .vwenc

# policy (root-only)
vw.set_user_persistence_allowed("alice", True)
vw.set_device_policy(compute_device_id(), allow_persistence=False)
```

---

## Admin & Policy Controls (root only)

* **Forbid persistence on a device** (forces `terminal_only`):

```python
vw.set_device_policy(compute_device_id(), allow_persistence=False, default_persistence="terminal_only")
```

* **Allow a user** to use persistence features:

```python
vw.set_user_persistence_allowed("alice", True)
```

* **Temporary tmux grant** for a pane (e.g., 2 hours):

```python
vw.grant_tmux_persistence_temp("alice", compute_device_id(), tmux_id, ttl_seconds=7200)
```

* Revoke with `revoke_tmux_persistence_temp(...)`.

---

## Export / Import Keychains

* **Export** creates a portable bundle (`KC1` header) encrypted with a **passphrase** via scrypt + AES-GCM. It contains only keychain entries (no LS/MK).
* **Import** merges into destination user’s keychain and re-encrypts under that user’s LS.

**Tip:** Sync the exported bundle across machines; each device/user imports (re-encrypts) locally.

---

## Working With Files

* **Register & encrypt** a file:

```python
item_id = vw.register_file("alice", "db_backup", Path("/backups/db.sql"), encrypt_now=True)
# encrypted output defaults to /backups/db.sql.vwenc
```

* **Decrypt** later:

```python
out = vw.decrypt_file("alice", item_id)
```

> All file DEKs are wrapped by MK. Password changes are constant-time (MK rewrap only).

---

## Migration (existing users → add LS wrap for MK)

If a user was created **before** dual-wrap existed (no `enc_mk_ls.bin`), run this once:

```python
from vaultweaver import VaultWeaver, hkdf_simple, aead_encrypt
vw = VaultWeaver()
user = "alice"
# unlock MK with password one time
mk = vw._unlock_mk(user, getpass.getpass(f"[{user}] Password: "))
# unlock LS (PIN or active session)
ls = vw._require_ls(user)
# write LS-wrapped MK
k_ls = hkdf_simple(ls, "VW-MK-WRAP")
(vw._u_dir(user) / "enc_mk_ls.bin").write_bytes(aead_encrypt(k_ls, mk, aad=user.encode()))
```

After this, MK operations can use LS (i.e., no password after PIN login).

---

## Troubleshooting

* **`InvalidTag` on PIN** → wrong PIN (or `pepper.bin` changed). If pepper changed, previous users cannot be unlocked.
* **`memory limit exceeded` (scrypt)** → your platform rejected the KDF cost. The code adapts by lowering `n`; you can also set smaller `n` in `config.json`.
* **No `enc_mk_ls.bin`** → create a new user or run the migration above.
* **Still getting prompts** → ensure `allow_mk_via_pin: true` and that you’ve called `login_with_pin(...)` in the same terminal.

---

## Environment

* `VAULTWEAVER_BASE` — redirect base storage directory.
* `Session_ID` — terminal identity; set by your shell/OS or derived at runtime.
* `TMUX`, `TMUX_PANE` — tmux identifiers; used for across-attach persistence (when granted).

> For development, you may add your own env-based shortcuts (e.g., a `VW_PIN` fallback) but avoid enabling them on production hosts.

---

## Side-note: AppVaultWeaver (PHP)

A future companion library can register apps and keep secrets out of PHP source by storing encrypted blobs and resolving them at runtime:

```php
$vw = new VaultWeaver();
$api = $vw->key('AppName', 'GPT_API');
```

Bindings can incorporate machine attributes (admin SID, `uuid.getnode()`) and a per-host salt, similar to the Python design.

---

## Backup & Recovery

* Back up: `pepper.bin`, `config.json`, and the entire `users/` directory.
* Store backups securely (offline), because they contain encrypted material whose decryption depends on pepper + user secrets.
* If `pepper.bin` is lost or replaced, **existing users cannot be recovered**.

---

## Roadmap (optional)

* Local **agent** (Unix socket / named pipe) to avoid any on-disk LS cache.
* CLI `vwctl` for interactive tasks (login, key get/set, export/import, policy view).
* Per-user/per-device overrides for `ls_cache.mode`.
* Optional TOTP step-up for roaming sessions.

---

## License & Disclaimer

This is a security-sensitive tool. Review the code and configuration for your threat model. No warranty; use at your own risk.

## Configuration Option Reference (allowed values & semantics)

> This section lists every supported knob in `config.json`, their **allowed values**, and whether they are **enforced today** or **reserved** (planned but not fully enforced yet).

### `global_policy`

* **`session_ttl_seconds`** *(int, seconds)* — Time-to-live for a session token. **Enforced.**
* **`absolute_lifetime_seconds`** *(int, seconds)* — Hard cap after which a session cannot be renewed. **Enforced.**
* **`idle_timeout_seconds`** *(int, seconds)* — Planned idle timeout. **Reserved (not yet enforced).**
* **`default_persistence`** *(enum)* — Default token scope when not specified at login. **Enforced.**

  * `"terminal_only"` *(default)* — Valid only for the current `Session_ID`. New terminals cannot resume.
  * `"terminal_across_attach"` — May resume across terminal reattachments **within the same tmux session/pane**, and only when a temporary tmux grant is active and policy allows persistence.
  * `"device_persistent"` — May resume across any terminals on the same device until TTL/absolute cap. Blocked if device or user forbids persistence.
* **`roaming`** *(enum)* — Intended cross-tty/device roaming policy. **Reserved (not yet enforced on top of the persistence rules).**

  * `"forbid"` *(default)* — Do not roam beyond current terminal (behavior is effectively controlled by `default_persistence`).
  * `"constrain"` — Allow constrained roaming (e.g., tmux-only); currently governed by `terminal_across_attach` + tmux grants.
  * `"allow"` — Allow broader roaming; today behavior is mainly determined by persistence mode.
* **`pin_kdf`** *(object)* — Parameters for PIN KDF. **Enforced.**

  * `type`: `"scrypt"` *(only supported)*
  * `n`: power-of-two int, recommended `16384` (≈16 MiB). Range typically `1024`–`32768` depending on host limits.
  * `r`: int, recommended `8`.
  * `p`: int, recommended `1`.
  * `length`: derived key size in bytes, recommended `32`.
* **`pw_kdf`** *(object)* — Parameters for password KDF. **Enforced.** (Same fields and guidance as `pin_kdf`.)
* **`allow_mk_via_pin`** *(bool)* — If `true`, MK can be unlocked via LS (i.e., after PIN login), eliminating password prompts for file/keychain ops. **Enforced.**
* **`max_pin_attempts_soft`** *(int)* — Soft threshold for PIN failures before short cooloff. **Reserved (not yet enforced).**
* **`max_pin_attempts_hard`** *(int)* — Hard threshold for PIN failures before long cooloff. **Reserved (not yet enforced).**
* **`cooloff_seconds_soft`** *(int)* — Cooloff duration after soft threshold. **Reserved.**
* **`cooloff_seconds_hard`** *(int)* — Cooloff duration after hard threshold. **Reserved.**
* **`ls_cache`** *(object)* — Controls per-terminal LS cache. **Enforced.**

  * `mode`: `"terminal"` (cache LS per `Session_ID`) | `"none"` (disable cache).
  * `ttl_seconds`: recommended to match `session_ttl_seconds` (upper bound enforced by token expiry regardless).

### `device_overrides`

Map of `device_id` → policy override object. **Enforced.**

Each object may contain:

* **`allow_persistence`** *(bool)* — If `false`, forces `terminal_only` on that device.
* **`default_persistence`** *(enum)* — Same enum as `global_policy.default_persistence`.
* **`roaming`** *(enum)* — Same enum as `global_policy.roaming` *(currently reserved)*.

> **Tip:** Get the local device ID via `compute_device_id()` and use it as the key.

### `user_overrides`

Map of `username` → object. **Enforced.**

Each object may contain:

* **`allow_persistence`** *(bool)* — If `true`, this user is allowed to request persistence modes on hosts that permit it. Root/admin only.

### `tmux_temp_persistence`

Map whose key is the string `"<user>|<device_id>|<tmux_id>"` and value is an **epoch timestamp**. **Enforced.**

* When present and not expired, a session with `persistence="terminal_across_attach"` may resume across attach/detach **within the same tmux**.
* Revoke by deleting the entry via `revoke_tmux_persistence_temp(...)`.

---

## Effective Behavior Matrix (quick reference)

| Setting                      | Allowed values                                                 | Enforced today | Notes                                                                     |
| ---------------------------- | -------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------- |
| `default_persistence`        | `terminal_only`, `terminal_across_attach`, `device_persistent` | Yes            | Governs resume scope when not explicitly requested at login.              |
| `roaming`                    | `forbid`, `constrain`, `allow`                                 | **Reserved**   | Planned; current roaming behavior is driven by persistence + tmux grants. |
| `allow_persistence` (device) | `true`/`false`                                                 | Yes            | If `false`, all sessions are effectively `terminal_only` on that host.    |
| `allow_persistence` (user)   | `true`/`false`                                                 | Yes            | Root/admin gate for which users may use persistence.                      |
| `ls_cache.mode`              | `terminal`, `none`                                             | Yes            | Controls whether LS is cached per terminal.                               |
| `allow_mk_via_pin`           | `true`/`false`                                                 | Yes            | If `true`, file/keychain ops avoid password prompts after PIN login.      |
| `session_ttl_seconds`        | integer seconds                                                | Yes            | Token lifetime.                                                           |
| `absolute_lifetime_seconds`  | integer seconds                                                | Yes            | Hard stop for any renewal.                                                |
| `idle_timeout_seconds`       | integer seconds                                                | **Reserved**   | Not yet enforced.                                                         |
| `pin_kdf` / `pw_kdf`         | scrypt params                                                  | Yes            | Adaptive fallback reduces cost if host refuses memory.                    |

---

## Examples

**1) Lock down a server (no persistence):**

```json
{
  "device_overrides": {
    "<device_id>": { "allow_persistence": false, "default_persistence": "terminal_only" }
  }
}
```

**2) Allow tmux-only persistence for a power user (with admin-granted window):**

```json
{
  "user_overrides": { "alice": { "allow_persistence": true } },
  "global_policy": { "default_persistence": "terminal_across_attach" }
}
```

*(Admin must also grant a temporary tmux window via `grant_tmux_persistence_temp`.)*

**3) Disable LS cache globally:**

```json
{ "global_policy": { "ls_cache": { "mode": "none", "ttl_seconds": 0 } } }
```

**4) Turn off MK via PIN (force password for file ops):**

```json
{ "global_policy": { "allow_mk_via_pin": false } }
```
