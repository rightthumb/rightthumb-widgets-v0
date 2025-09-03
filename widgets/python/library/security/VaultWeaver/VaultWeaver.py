# vaultweaver.py
# ======================================================================
# VaultWeaver — per-user keychain, terminal-scoped sessions, and rewrap
# ======================================================================

from __future__ import annotations

import base64
import dataclasses
import getpass
import hashlib
import hmac
import json
import os
import platform
import secrets
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, List

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except Exception as e:
    raise RuntimeError(
        "[VaultWeaver] Missing dependency: cryptography\n"
        "  pip install cryptography\n"
        f"Original import error: {e}"
    )

# ======================================================================
# 0) FOLDERS & FILES (edit here)
# ======================================================================

IS_WINDOWS = os.name == "nt"

VAULTWEAVER_BASE: Path = Path(
    os.environ.get(
        "VAULTWEAVER_BASE",
        (Path(os.environ.get("ProgramData", "C:/ProgramData")) / "VaultWeaver").as_posix()
        if IS_WINDOWS else "/opt/VaultWeaver"
    )
)

PATHS = {
    "BASE": VAULTWEAVER_BASE,
    "SECRETS_DIR": VAULTWEAVER_BASE / "secrets",
    "PEPPER_FILE": VAULTWEAVER_BASE / "secrets" / "pepper.bin",
    "CONFIG_FILE": VAULTWEAVER_BASE / "config.json",
    "USERS_DIR": VAULTWEAVER_BASE / "users",
    "SESSIONS_DIR": VAULTWEAVER_BASE / "sessions",
    "AUDIT_LOG": VAULTWEAVER_BASE / "audit.jsonl",
    "RUN_DIR": Path(os.environ.get("XDG_RUNTIME_DIR", (VAULTWEAVER_BASE / "run").as_posix())),
}

# Per-user directory layout under users/<username>/:
#   creds.json        -> salts/params (no raw secrets)
#   enc_ls.bin        -> Login Secret (LS) encrypted by PIN-derived key
#   enc_mk.bin        -> Master Key (MK) encrypted by password-derived key
#   keychain.bin      -> entire keychain (JSON) encrypted by a key derived from LS
#   policy.json       -> per-user policy overrides (optional)
#   items/<id>.json   -> registry entries for files (DEK wrapped by MK)

# ======================================================================
# 1) HELPERS & CRYPTO
# ======================================================================

def _ensure_dirs() -> None:
    for key, p in PATHS.items():
        if key in ("CONFIG_FILE", "PEPPER_FILE", "AUDIT_LOG"):
            p.parent.mkdir(parents=True, exist_ok=True)
        else:
            p.mkdir(parents=True, exist_ok=True)
    # permissions best-effort
    for name in ("SECRETS_DIR", "USERS_DIR", "SESSIONS_DIR", "RUN_DIR"):
        try:
            os.chmod(PATHS[name], 0o700)
        except Exception:
            pass
    # app-level pepper
    if not PATHS["PEPPER_FILE"].exists():
        PATHS["PEPPER_FILE"].write_bytes(secrets.token_bytes(32))
        try:
            os.chmod(PATHS["PEPPER_FILE"], 0o600)
        except Exception:
            pass
    # default config
    if not PATHS["CONFIG_FILE"].exists():
        default_config = {
            "global_policy": {
                "session_ttl_seconds": 12 * 3600,
                "absolute_lifetime_seconds": 7 * 24 * 3600,
                "idle_timeout_seconds": 30 * 60,
                "default_persistence": "terminal_only",  # terminal_only | terminal_across_attach | device_persistent
                "roaming": "forbid",                     # forbid | constrain | allow
                "pin_kdf": {"type": "scrypt", "n": 2**14, "r": 8, "p": 1, "length": 32},
                "pw_kdf": { "type": "scrypt", "n": 16384, "r": 8, "p": 1, "length": 32 },
                "max_pin_attempts_soft": 5,
                "max_pin_attempts_hard": 20,
                "cooloff_seconds_soft": 15 * 60,
                "cooloff_seconds_hard": 12 * 3600,
            },
            "device_overrides": {},
            "user_overrides": {},
            "tmux_temp_persistence": {}
        }
        PATHS["CONFIG_FILE"].write_text(json.dumps(default_config, indent=2), encoding="utf-8")

def _is_root_admin() -> bool:
    if not IS_WINDOWS:
        try:
            return os.geteuid() == 0
        except Exception:
            return False
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def _read_pepper() -> bytes:
    return PATHS["PEPPER_FILE"].read_bytes()

def _tight_write(path: Path, data: bytes | str, text: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if text:
        path.write_text(data, encoding="utf-8")  # type: ignore[arg-type]
    else:
        path.write_bytes(data)  # type: ignore[arg-type]
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass

def kdf_scrypt(secret: str, salt: bytes, **params) -> bytes:
    """
    Scrypt KDF helper that tolerates extra keys like 'type' and adapts
    if OpenSSL rejects the requested memory (e.g., on Windows).
    Expected params: n, r, p, length, (optional) maxmem.
    """
    n = int(params.get("n", 2**14))
    r = int(params.get("r", 8))
    p = int(params.get("p", 1))
    dklen = int(params.get("length", 32))
    # 0 disables OpenSSL's internal cap on many builds
    maxmem = int(params.get("maxmem", 0))

    pw = secret.encode("utf-8")

    # First try as requested
    try:
        return hashlib.scrypt(pw, salt=salt, n=n, r=r, p=p, dklen=dklen, maxmem=maxmem)
    except ValueError as e:
        # Fall back only on memory-limit errors
        if "memory limit exceeded" not in str(e).lower():
            raise

    # Adaptive fallback: reduce N until ≲ 24 MiB (or hit a safe floor)
    # scrypt memory ≈ 128 * r * n bytes
    target_bytes = 24 * 1024 * 1024  # 24 MiB target to avoid 32 MiB caps
    while n > 2**10 and (128 * r * n) > target_bytes:
        n //= 2

    # Force maxmem=0 (unlimited) in case the build still enforces a small default
    return hashlib.scrypt(pw, salt=salt, n=n, r=r, p=p, dklen=dklen, maxmem=0)


def aead_encrypt(key: bytes, plaintext: bytes, aad: bytes = b"") -> bytes:
    aead = AESGCM(key)
    nonce = secrets.token_bytes(12)
    return nonce + aead.encrypt(nonce, plaintext, aad)

def aead_decrypt(key: bytes, blob: bytes, aad: bytes = b"") -> bytes:
    aead = AESGCM(key)
    nonce, ct = blob[:12], blob[12:]
    return aead.decrypt(nonce, ct, aad)

def hkdf_simple(key: bytes, label: str) -> bytes:
    # cheap, adequate here: SHA-256(label || key)
    return hashlib.sha256(label.encode() + b"|" + key).digest()

def _rand_id(n: int = 12) -> str:
    return secrets.token_hex(n)

# ======================================================================
# 2) CONTEXT & IDS
# ======================================================================

def _machine_tuple() -> str:
    parts = [
        platform.system(),
        platform.release(),
        platform.node(),
        hex(uuid.getnode()),
    ]
    if not IS_WINDOWS:
        try:
            parts.append(Path("/etc/machine-id").read_text(encoding="utf-8").strip())
        except Exception:
            pass
    else:
        try:
            import subprocess
            who = subprocess.check_output(["whoami", "/user"], text=True)
            for tok in who.split():
                if tok.startswith("S-1-"):
                    parts.append(tok)
                    break
        except Exception:
            pass
    return "|".join(parts)

def compute_device_id() -> str:
    pepper = _read_pepper()
    raw = _machine_tuple().encode("utf-8")
    return hmac.new(pepper, raw, hashlib.sha256).hexdigest()

def discover_terminal_ids() -> Tuple[str, Optional[str]]:
    term = os.environ.get("Session_ID") or os.environ.get("SESSION_ID")
    if not term:
        base = f"{os.getpid()}|{int(time.time())}|{os.environ.get('TTY','')}"
        term = hashlib.sha256(base.encode()).hexdigest()[:16]
        os.environ["Session_ID"] = term
    tmux_id = os.environ.get("TMUX_PANE") or os.environ.get("TMUX")
    return term, tmux_id

def current_username() -> str:
    # prefer env; fallback to getpass
    return os.environ.get("USER") or os.environ.get("USERNAME") or getpass.getuser()

# ======================================================================
# 3) DATA OBJECTS
# ======================================================================

@dataclasses.dataclass
class SessionToken:
    user: str
    device_id: str
    terminal_id: str
    tmux_id: Optional[str]
    issued_at: int
    expires_at: int
    absolute_deadline: int
    persistence: str
    nonce: str
    sig: str

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self), separators=(",", ":"))

# ======================================================================
# 4) VAULTWEAVER
# ======================================================================

class VaultWeaver:
    """
    Multi-user directory with:
      - PIN-only terminal-scoped sessions (Session_ID, tmux temp persistence)
      - per-user keychain (encrypted under LS-derived key)
      - Master Key (MK) protected by password, used to wrap file DEKs
      - change_pin (rewrap LS) and change_password (rewrap MK)
      - export/import of keychains across machines/users (re-encrypt at import)
    """

    # ---------- init / config ----------

    def __init__(self) -> None:
        _ensure_dirs()
        self.cfg = json.loads(PATHS["CONFIG_FILE"].read_text(encoding="utf-8"))

    def _save_cfg(self) -> None:
        _tight_write(PATHS["CONFIG_FILE"], json.dumps(self.cfg, indent=2), text=True)

    # ---------- admin policy (root only) ----------

    def set_user_persistence_allowed(self, username: str, allowed: bool) -> None:
        if not _is_root_admin():
            raise PermissionError("Root/admin required")
        self.cfg.setdefault("user_overrides", {})[username] = {"allow_persistence": bool(allowed)}
        self._save_cfg()
        self._audit("policy_user_persistence", {"user": username, "allowed": allowed})

    def set_device_policy(self, device_id: str, *, allow_persistence: Optional[bool] = None,
                          default_persistence: Optional[str] = None, roaming: Optional[str] = None) -> None:
        if not _is_root_admin():
            raise PermissionError("Root/admin required")
        dev = self.cfg.setdefault("device_overrides", {}).setdefault(device_id, {})
        if allow_persistence is not None:
            dev["allow_persistence"] = bool(allow_persistence)
        if default_persistence is not None:
            dev["default_persistence"] = default_persistence
        if roaming is not None:
            dev["roaming"] = roaming
        self._save_cfg()
        self._audit("policy_device_update", {"device_id": device_id, **dev})

    def grant_tmux_persistence_temp(self, username: str, device_id: str, tmux_id: str, ttl_seconds: int) -> None:
        if not _is_root_admin():
            raise PermissionError("Root/admin required")
        key = f"{username}|{device_id}|{tmux_id}"
        self.cfg.setdefault("tmux_temp_persistence", {})[key] = int(time.time()) + int(ttl_seconds)
        self._save_cfg()
        self._audit("tmux_persist_granted", {"user": username, "device_id": device_id, "tmux_id": tmux_id, "ttl": ttl_seconds})

    def revoke_tmux_persistence_temp(self, username: str, device_id: str, tmux_id: str) -> None:
        if not _is_root_admin():
            raise PermissionError("Root/admin required")
        key = f"{username}|{device_id}|{tmux_id}"
        self.cfg.get("tmux_temp_persistence", {}).pop(key, None)
        self._save_cfg()
        self._audit("tmux_persist_revoked", {"user": username, "device_id": device_id, "tmux_id": tmux_id})

    # ---------- user lifecycle ----------

    def create_user(self, username: str, password: str, pin: str) -> None:
        up = self._u_dir(username)
        up.mkdir(parents=True, exist_ok=True)

        global_pol = self.cfg["global_policy"]
        pin_salt = secrets.token_bytes(16)
        pw_salt = secrets.token_bytes(16)

        pepper = _read_pepper()
        pepper_id = base64.b64encode(hashlib.sha256(pepper).digest()).decode()

        pin_key = kdf_scrypt(pin + "|" + pepper_id, pin_salt, **global_pol["pin_kdf"])
        pw_key  = kdf_scrypt(password + "|" + pepper_id, pw_salt, **global_pol["pw_kdf"])

        # Generate LS and MK
        ls = secrets.token_bytes(32)
        mk = secrets.token_bytes(32)

        _tight_write(up / "enc_ls.bin", aead_encrypt(pin_key, ls, aad=username.encode()))
        _tight_write(up / "enc_mk.bin", aead_encrypt(pw_key, mk, aad=username.encode()))

        creds = {
            "pin": {"salt_b64": base64.b64encode(pin_salt).decode(), "kdf": global_pol["pin_kdf"]},
            "pw":  {"salt_b64": base64.b64encode(pw_salt).decode(),  "kdf": global_pol["pw_kdf"]},
            "created_at": int(time.time()),
            "version": 1,
        }
        _tight_write(up / "creds.json", json.dumps(creds, indent=2), text=True)

        # Initialize empty keychain (encrypted under LS-derived key)
        self._save_keychain_blob(username, ls, {"__meta__": {"ver": 1, "created_at": int(time.time())}})

        # Default per-user policy
        _tight_write(up / "policy.json", json.dumps({"allow_persistence": False}, indent=2), text=True)

        self._audit("user_created", {"user": username})

    def change_pin(self, username: str, old_pin: str, new_pin: str) -> None:
        ls = self._unlock_ls(username, old_pin)
        # rewrap LS
        global_pol = self.cfg["global_policy"]
        pin_salt = secrets.token_bytes(16)
        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        pin_key = kdf_scrypt(new_pin + "|" + pepper_id, pin_salt, **global_pol["pin_kdf"])
        _tight_write(self._u_dir(username) / "enc_ls.bin", aead_encrypt(pin_key, ls, aad=username.encode()))
        # update salt
        creds = json.loads((self._u_dir(username) / "creds.json").read_text(encoding="utf-8"))
        creds["pin"]["salt_b64"] = base64.b64encode(pin_salt).decode()
        _tight_write(self._u_dir(username) / "creds.json", json.dumps(creds, indent=2), text=True)
        self._audit("pin_changed", {"user": username})

    def change_password(self, username: str, old_password: str, new_password: str) -> None:
        mk = self._unlock_mk(username, old_password)
        # rewrap MK
        global_pol = self.cfg["global_policy"]
        pw_salt = secrets.token_bytes(16)
        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        pw_key = kdf_scrypt(new_password + "|" + pepper_id, pw_salt, **global_pol["pw_kdf"])
        _tight_write(self._u_dir(username) / "enc_mk.bin", aead_encrypt(pw_key, mk, aad=username.encode()))
        # update salt
        creds = json.loads((self._u_dir(username) / "creds.json").read_text(encoding="utf-8"))
        creds["pw"]["salt_b64"] = base64.b64encode(pw_salt).decode()
        _tight_write(self._u_dir(username) / "creds.json", json.dumps(creds, indent=2), text=True)
        self._audit("password_changed", {"user": username})

    # ---------- login / session ----------

    def login_with_pin(self, username: str, pin: str, *, persistence: Optional[str] = None) -> SessionToken:
        device_id = compute_device_id()
        terminal_id, tmux_id = discover_terminal_ids()
        ls = self._unlock_ls(username, pin)

        pol = self._resolve_policy(username, device_id, tmux_id)
        if persistence is None:
            persistence = pol["default_persistence"]

        if not pol["allow_persistence"] and persistence != "terminal_only":
            raise PermissionError("Persistence disabled for this user/device")
        if not pol["device_allow_persistence"] and persistence != "terminal_only":
            raise PermissionError("Device forbids persistence; use 'terminal_only'")

        now = int(time.time())
        ttl = int(self.cfg["global_policy"]["session_ttl_seconds"])
        absmax = int(self.cfg["global_policy"]["absolute_lifetime_seconds"])

        st = SessionToken(
            user=username,
            device_id=device_id,
            terminal_id=terminal_id,
            tmux_id=tmux_id,
            issued_at=now,
            expires_at=now + ttl,
            absolute_deadline=now + absmax,
            persistence=persistence,
            nonce=base64.urlsafe_b64encode(secrets.token_bytes(16)).decode(),
            sig="",
        )
        st.sig = self._sign_token(ls, st)
        self._store_session(st)
        self._audit("login_success", {"user": username, "device_id": device_id, "terminal_id": terminal_id, "persistence": persistence})
        return st

    def resume_session(self, username: str) -> Optional[SessionToken]:
        st = self._load_session(username)
        if not st:
            return None
        device_id = compute_device_id()
        terminal_id, tmux_id = discover_terminal_ids()
        if st.device_id != device_id:
            return None
        if st.terminal_id != terminal_id:
            if st.persistence == "device_persistent":
                pass
            elif st.persistence == "terminal_across_attach":
                if not (st.tmux_id and tmux_id and st.tmux_id == tmux_id and self._tmux_allowed(username, device_id, tmux_id)):
                    return None
            else:
                return None
        now = int(time.time())
        if now > st.expires_at or now > st.absolute_deadline:
            return None
        return st

    def logout(self, username: str) -> None:
        sf = self._session_file(username)
        if sf.exists():
            sf.unlink(missing_ok=True)
        self._audit("logout", {"user": username})

    # ---------- keychain (per user; LS-derived key) ----------

    def key(self, label: str, user: Optional[str] = None, pin: Optional[str] = None, default: Optional[str] = None) -> Optional[str]:
        """
        Convenience accessor: return secret string for `label` from user's keychain.
        Tries to resume session; if none and `pin` is provided, unlocks via pin.
        """
        username = user or current_username()
        st = self.resume_session(username)
        if st:
            ls = self._unlock_ls_from_session(username)  # quick, using PIN only prompt if rotation needed
        elif pin is not None:
            ls = self._unlock_ls(username, pin)
        else:
            raise PermissionError("No active session. Call login_with_pin(...) or pass pin=.")
        kc = self._load_keychain(username, ls)
        return kc.get(label, default)

    def set_key(self, label: str, secret: str, user: Optional[str] = None, pin: Optional[str] = None, overwrite: bool = True) -> None:
        username = user or current_username()
        st = self.resume_session(username)
        if st:
            ls = self._unlock_ls_from_session(username)
        elif pin is not None:
            ls = self._unlock_ls(username, pin)
        else:
            raise PermissionError("No active session. Call login_with_pin(...) or pass pin=.")
        kc = self._load_keychain(username, ls)
        if not overwrite and label in kc:
            return
        kc[label] = secret
        self._save_keychain_blob(username, ls, kc)
        self._audit("keychain_set", {"user": username, "label": label})

    def list_keys(self, user: Optional[str] = None, pin: Optional[str] = None) -> List[str]:
        username = user or current_username()
        st = self.resume_session(username)
        if st:
            ls = self._unlock_ls_from_session(username)
        elif pin is not None:
            ls = self._unlock_ls(username, pin)
        else:
            raise PermissionError("No active session. Call login_with_pin(...) or pass pin=.")
        return sorted([k for k in self._load_keychain(username, ls).keys() if k != "__meta__"])

    def export_keychain(self, username: str, passphrase: str) -> bytes:
        """
        Export encrypted bundle of the user's keychain (no LS/MK secrets).
        Protected by the given passphrase (scrypt + AES-GCM).
        """
        ls = self._require_ls(username)
        kc = self._load_keychain(username, ls)
        salt = secrets.token_bytes(16)
        k = kdf_scrypt(passphrase, salt, **self.cfg["global_policy"]["pw_kdf"])
        payload = {
            "format": "VW-KC-1",
            "user": username,
            "ts": int(time.time()),
            "entries": kc,
        }
        blob = aead_encrypt(k, json.dumps(payload).encode(), aad=b"VWKC")
        return b"KC1" + salt + blob

    def import_keychain(self, username: str, bundle: bytes, passphrase: str, *, merge: bool = True, overwrite: bool = False) -> None:
        """
        Import bundle created by export_keychain(); re-encrypt for destination user.
        """
        if not bundle.startswith(b"KC1"):
            raise ValueError("Unknown keychain package")
        salt = bundle[3:19]
        blob = bundle[19:]
        k = kdf_scrypt(passphrase, salt, **self.cfg["global_policy"]["pw_kdf"])
        payload = json.loads(aead_decrypt(k, blob, aad=b"VWKC").decode())
        if payload.get("format") != "VW-KC-1":
            raise ValueError("Invalid keychain format")
        ls = self._require_ls(username)
        kc = self._load_keychain(username, ls)
        src_entries = payload.get("entries", {})
        for label, value in src_entries.items():
            if label == "__meta__":
                continue
            if label in kc and not (overwrite or not merge):
                continue
            kc[label] = value
        kc["__meta__"] = {"ver": 1, "imported_at": int(time.time())}
        self._save_keychain_blob(username, ls, kc)
        self._audit("keychain_import", {"user": username, "count": len(src_entries)})

    # ---------- file registry (DEK wrapped by MK) ----------

    def register_file(self, username: str, label: str, path: Path, *, encrypt_now: bool = True, out_suffix: str = ".vwenc") -> str:
        """
        Register a file: generate DEK, wrap by MK, (optionally) encrypt immediately to path+suffix.
        """
        mk = self._require_mk(username)
        udir = self._u_dir(username) / "items"
        udir.mkdir(parents=True, exist_ok=True)

        item_id = _rand_id(8)
        dek = secrets.token_bytes(32)
        dek_wrap = aead_encrypt(mk, dek, aad=f"DEK|{label}".encode())

        meta = {
            "id": item_id,
            "kind": "file",
            "label": label,
            "path": str(Path(path).resolve()),
            "algo": "AESGCM",
            "dek_wrap_b64": base64.b64encode(dek_wrap).decode(),
            "created_at": int(time.time()),
            "out_path": str(Path(str(path) + out_suffix).resolve()),
        }
        _tight_write(udir / f"{item_id}.json", json.dumps(meta, indent=2), text=True)

        if encrypt_now:
            data = Path(path).read_bytes()
            ct = aead_encrypt(dek, data, aad=f"FILE|{meta['path']}".encode())
            _tight_write(Path(meta["out_path"]), ct)
        self._audit("file_registered", {"user": username, "item_id": item_id, "label": label})
        return item_id

    def decrypt_file(self, username: str, item_id: str, out_path: Optional[Path] = None) -> Path:
        """
        Decrypt previously registered (and encrypted) file to out_path (default: strip .vwenc).
        """
        meta = self._item_meta(username, item_id)
        mk = self._require_mk(username)
        dek = aead_decrypt(mk, base64.b64decode(meta["dek_wrap_b64"]), aad=f"DEK|{meta['label']}".encode())
        enc_p = Path(meta["out_path"])
        raw = aead_decrypt(dek, enc_p.read_bytes(), aad=f"FILE|{meta['path']}".encode())
        if out_path is None:
            if enc_p.suffix == ".vwenc":
                out_path = enc_p.with_suffix("")
            else:
                out_path = enc_p.parent / (enc_p.name + ".dec")
        _tight_write(out_path, raw)
        self._audit("file_decrypted", {"user": username, "item_id": item_id, "out": str(out_path)})
        return out_path

    # ---------- internals: LS/MK, keychain io, sessions ----------

    def _u_dir(self, username: str) -> Path:
        return PATHS["USERS_DIR"] / username

    def _load_creds(self, username: str) -> Dict[str, Any]:
        return json.loads((self._u_dir(username) / "creds.json").read_text(encoding="utf-8"))

    def _unlock_ls(self, username: str, pin: str) -> bytes:
        creds = self._load_creds(username)
        salt = base64.b64decode(creds["pin"]["salt_b64"])
        pin_kdf = creds["pin"]["kdf"]
        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        key = kdf_scrypt(pin + "|" + pepper_id, salt, **pin_kdf)
        blob = (self._u_dir(username) / "enc_ls.bin").read_bytes()
        try:
            return aead_decrypt(key, blob, aad=username.encode())
        except Exception as e:
            self._audit("pin_failed", {"user": username})
            raise PermissionError("Invalid PIN") from e

    def _unlock_mk(self, username: str, password: str) -> bytes:
        creds = self._load_creds(username)
        salt = base64.b64decode(creds["pw"]["salt_b64"])
        pw_kdf = creds["pw"]["kdf"]
        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        key = kdf_scrypt(password + "|" + pepper_id, salt, **pw_kdf)
        blob = (self._u_dir(username) / "enc_mk.bin").read_bytes()
        try:
            return aead_decrypt(key, blob, aad=username.encode())
        except Exception as e:
            self._audit("password_failed", {"user": username})
            raise PermissionError("Invalid password") from e

    def _require_ls(self, username: str) -> bytes:
        st = self.resume_session(username)
        if st:
            return self._unlock_ls_from_session(username)
        # if no session, prompt
        pin = getpass.getpass(prompt=f"[{username}] PIN: ")
        return self._unlock_ls(username, pin)

    def _require_mk(self, username: str) -> bytes:
        # by design, MK is password-protected; prompt when needed
        pwd = getpass.getpass(prompt=f"[{username}] Password for MK: ")
        return self._unlock_mk(username, pwd)

    def _kc_key_from_ls(self, ls: bytes) -> bytes:
        return hkdf_simple(ls, "VW-KEYCHAIN")

    def _load_keychain(self, username: str, ls: bytes) -> Dict[str, str]:
        kc_path = self._u_dir(username) / "keychain.bin"
        if not kc_path.exists():
            return {"__meta__": {"ver": 1, "created_at": int(time.time())}}
        blob = kc_path.read_bytes()
        key = self._kc_key_from_ls(ls)
        data = json.loads(aead_decrypt(key, blob, aad=b"VW-KC").decode())
        if "__meta__" not in data:
            data["__meta__"] = {"ver": 1}
        return data

    def _save_keychain_blob(self, username: str, ls: bytes, mapping: Dict[str, str]) -> None:
        key = self._kc_key_from_ls(ls)
        blob = aead_encrypt(key, json.dumps(mapping).encode(), aad=b"VW-KC")
        _tight_write(self._u_dir(username) / "keychain.bin", blob)

    def _unlock_ls_from_session(self, username: str) -> bytes:
        # For rotation we do not cache LS; we just prompt for PIN when necessary.
        # Here, we re-use resume_session() guarantee and ask PIN if needed.
        st = self.resume_session(username)
        if not st:
            raise PermissionError("No active session")
        # We still need LS to MAC or keychain ops; safest is to prompt minimal PIN if absent.
        # Optionally you can cache LS via an agent; kept simple here:
        pin = getpass.getpass(prompt=f"[{username}] PIN (for secure op): ")
        return self._unlock_ls(username, pin)

    # sessions storage

    def _session_file(self, username: str) -> Path:
        device_id = compute_device_id()
        terminal_id, _ = discover_terminal_ids()
        return PATHS["SESSIONS_DIR"] / username / device_id / terminal_id / "token.json"

    def _store_session(self, st: SessionToken) -> None:
        _tight_write(self._session_file(st.user), st.to_json(), text=True)

    def _load_session(self, username: str) -> Optional[SessionToken]:
        f = self._session_file(username)
        if not f.exists():
            return None
        try:
            return SessionToken(**json.loads(f.read_text(encoding="utf-8")))
        except Exception:
            return None

    def _mac_key(self, ls: bytes) -> bytes:
        return hkdf_simple(ls, "VW-MAC")

    def _sign_token(self, ls: bytes, st: SessionToken) -> str:
        mac_key = self._mac_key(ls)
        msg = f"{st.user}|{st.device_id}|{st.terminal_id}|{st.tmux_id}|{st.issued_at}|{st.expires_at}|{st.absolute_deadline}|{st.persistence}|{st.nonce}".encode()
        return base64.urlsafe_b64encode(hmac.new(mac_key, msg, hashlib.sha256).digest()).decode()

    # ---------- policy ----------

    def _resolve_policy(self, username: str, device_id: str, tmux_id: Optional[str]) -> Dict[str, Any]:
        g = self.cfg["global_policy"]
        u_over = self.cfg.get("user_overrides", {}).get(username, {})
        d_over = self.cfg.get("device_overrides", {}).get(device_id, {})

        # per-user file
        upol_path = self._u_dir(username) / "policy.json"
        ufile = {}
        if upol_path.exists():
            try:
                ufile = json.loads(upol_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        allow_persistence = bool(u_over.get("allow_persistence", ufile.get("allow_persistence", False)))
        device_allow = bool(d_over.get("allow_persistence", True))
        default_persist = d_over.get("default_persistence", g["default_persistence"])
        roaming = d_over.get("roaming", g["roaming"])

        # temporary tmux grant
        tmux_ok = False
        if tmux_id:
            tmux_ok = self._tmux_allowed(username, device_id, tmux_id)

        return {
            "allow_persistence": allow_persistence or tmux_ok,
            "device_allow_persistence": device_allow,
            "default_persistence": default_persist,
            "roaming": roaming,
        }

    def _tmux_allowed(self, username: str, device_id: str, tmux_id: str) -> bool:
        key = f"{username}|{device_id}|{tmux_id}"
        exp = self.cfg.get("tmux_temp_persistence", {}).get(key)
        return bool(exp and int(time.time()) <= int(exp))

    # ---------- items helpers ----------

    def _item_meta(self, username: str, item_id: str) -> Dict[str, Any]:
        f = self._u_dir(username) / "items" / f"{item_id}.json"
        if not f.exists():
            raise FileNotFoundError(f"Item {item_id} not found")
        return json.loads(f.read_text(encoding="utf-8"))

    # ---------- audit ----------

    def _audit(self, event: str, details: Dict[str, Any]) -> None:
        entry = {"ts": int(time.time()), "event": event, "details": details}
        with open(PATHS["AUDIT_LOG"], "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, separators=(",", ":")) + "\n")
        try:
            os.chmod(PATHS["AUDIT_LOG"], 0o600)
        except Exception:
            pass

# ======================================================================
# 5) DEMO (run: python3 vaultweaver.py)
# ======================================================================

def demo():
    print("\n=== VaultWeaver demo ===")
    vw = VaultWeaver()
    device = compute_device_id()
    term, tmux = discover_terminal_ids()
    print(f"[context] device={device[:12]}… term={term} tmux={tmux}")

    userA = f"vw_user_{_rand_id(3)}"
    pinA = "12345678"
    pwA  = "StrongPass!42"

    print(f"[setup] create_user {userA}")
    vw.create_user(userA, password=pwA, pin=pinA)
    print("[files] register + encrypt a sample file")
    sample = PATHS["BASE"] / "sample.txt"
    sample.write_text("Top secret document.\n", encoding="utf-8")
    item_id = vw.register_file(userA, "doc1", sample, encrypt_now=True)
    dec_path = vw.decrypt_file(userA, item_id)
    print(f"  -> decrypted to {dec_path}")


def demo1():
    print("\n=== VaultWeaver demo ===")
    vw = VaultWeaver()
    device = compute_device_id()
    term, tmux = discover_terminal_ids()
    print(f"[context] device={device[:12]}… term={term} tmux={tmux}")

    userA = f"vw_user_{_rand_id(3)}"
    pinA = "12345678"
    pwA  = "StrongPass!42"

    print(f"[setup] create_user {userA}")
    vw.create_user(userA, password=pwA, pin=pinA)

    # admin: allow persistence for this user on this device for demo
    try:
        vw.set_user_persistence_allowed(userA, True)
        vw.set_device_policy(device, allow_persistence=True, default_persistence="terminal_only", roaming="constrain")
        if not tmux:
            os.environ["TMUX_PANE"] = tmux = f"%{_rand_id(2)}"
        vw.grant_tmux_persistence_temp(userA, device, tmux, ttl_seconds=120)
        print("[admin] temp tmux persistence granted (120s)")
    except PermissionError:
        print("[admin] not root/admin; skipping grants (demo still runs)")

    print("[login] with PIN (terminal_only default)")
    vw.login_with_pin(userA, pin=pinA)

    print("[keychain] set & get 'gpt'")
    vw.set_key("gpt", "sk-EXAMPLE-KEY-123", user=userA)     # uses session
    print("  -> key('gpt') =", vw.key("gpt", user=userA))

    print("[export] keychain with passphrase 'carry'")
    pkg = vw.export_keychain(userA, passphrase="carry")

    userB = f"vw_user_{_rand_id(3)}"
    print(f"[setup] create_user {userB}")
    vw.create_user(userB, password="AnotherPass!55", pin="87654321")

    print("[import] keychain into userB (merge)")
    vw.import_keychain(userB, pkg, passphrase="carry", merge=True, overwrite=False)

    print("  -> userB key('gpt') =", vw.key("gpt", user=userB, pin="87654321"))

    print("[files] register + encrypt a sample file")
    sample = PATHS["BASE"] / "sample.txt"
    sample.write_text("Top secret document.\n", encoding="utf-8")
    item_id = vw.register_file(userA, "doc1", sample, encrypt_now=True)
    dec_path = vw.decrypt_file(userA, item_id)
    print(f"  -> decrypted to {dec_path}")

    print("[security] change PIN & Password")
    vw.change_pin(userA, old_pin=pinA, new_pin="11223344")
    vw.change_password(userA, old_password=pwA, new_password="EvenStronger!99")
    print("=== done ===\n")

if __name__ == "__main__":
    demo()


# VAULTWEAVER_BASE