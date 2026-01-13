# vaultweaver.py
# ======================================================================
# VaultWeaver 2FA — master password + PIN required to decrypt anything
# ======================================================================

from __future__ import annotations

import base64
import getpass
import hashlib
import json
import os
import secrets
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except Exception as e:
    raise RuntimeError(
        "[VaultWeaver] Missing dependency: cryptography\n"
        "  pip install cryptography\n"
        f"Original import error: {e}"
    )

# ======================================================================
# 0) FOLDERS & FILES
# ======================================================================

IS_WINDOWS = os.name == "nt"

VAULTWEAVER_BASE: Path = Path(
    os.environ.get(
        "VAULTWEAVER_BASE",
        (Path(os.environ.get("ProgramData", "C:/ProgramData")) / "VaultWeaver").as_posix()
        if IS_WINDOWS else "/opt/VaultWeaver"
    )
)

PATHS: Dict[str, Path] = {
    "BASE": VAULTWEAVER_BASE,
    "SECRETS_DIR": VAULTWEAVER_BASE / "secrets",
    "PEPPER_FILE": VAULTWEAVER_BASE / "secrets" / "pepper.bin",
    "CONFIG_FILE": VAULTWEAVER_BASE / "config.json",
    "USERS_DIR": VAULTWEAVER_BASE / "users",
    "AUDIT_LOG": VAULTWEAVER_BASE / "audit.jsonl",
}


def _ensure_dirs() -> None:
    for key, p in PATHS.items():
        if key in ("CONFIG_FILE", "PEPPER_FILE", "AUDIT_LOG"):
            p.parent.mkdir(parents=True, exist_ok=True)
        else:
            p.mkdir(parents=True, exist_ok=True)

    # permissions best-effort
    for name in ("SECRETS_DIR", "USERS_DIR"):
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

    # default config (mainly KDF params)
    if not PATHS["CONFIG_FILE"].exists():
        cfg = {
            "kdf": {
                "type": "scrypt",
                "n": 2**14,
                "r": 8,
                "p": 1,
                "length": 32,
            },
            "version": 1,
        }
        PATHS["CONFIG_FILE"].write_text(json.dumps(cfg, indent=2), encoding="utf-8")


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
    Scrypt KDF helper; tolerates extra keys like 'type'.
    Expected keys: n, r, p, length, (optional) maxmem.
    """
    n = int(params.get("n", 2**14))
    r = int(params.get("r", 8))
    p = int(params.get("p", 1))
    dklen = int(params.get("length", 32))
    maxmem = int(params.get("maxmem", 0))
    pw = secret.encode("utf-8")

    try:
        return hashlib.scrypt(pw, salt=salt, n=n, r=r, p=p, dklen=dklen, maxmem=maxmem)
    except ValueError as e:
        if "memory limit exceeded" not in str(e).lower():
            raise

    # simple fallback: reduce N until memory looks safe-ish
    target_bytes = 24 * 1024 * 1024  # 24 MiB
    while n > 2**10 and (128 * r * n) > target_bytes:
        n //= 2
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
    return hashlib.sha256(label.encode() + b"|" + key).digest()


def _rand_id(n: int = 12) -> str:
    return secrets.token_hex(n)


# ======================================================================
# VaultWeaver 2FA: master password + PIN everywhere
# ======================================================================

class VaultWeaver:
    """
    Design:
      - Each user has a random 32-byte DATA_KEY.
      - DATA_KEY is *only* stored encrypted by a ROOT_KEY.
      - ROOT_KEY = HKDF( PIN_KEY || PW_KEY, "ROOT" )
      - PIN_KEY = scrypt(pin + "|" + pepper_id, pin_salt)
      - PW_KEY  = scrypt(password + "|" + pepper_id, pw_salt)

    So to recover DATA_KEY, you must know BOTH:
      - correct PIN
      - correct master password

    DATA_KEY is then used to:
      - encrypt/decrypt the keychain (string secrets)
      - wrap per-file DEKs for file encryption
    """

    def __init__(self) -> None:
        _ensure_dirs()
        self.cfg = json.loads(PATHS["CONFIG_FILE"].read_text(encoding="utf-8"))
        self._data_keys: Dict[str, bytes] = {}  # in-memory only, per-process

    # ------------- paths -------------

    def _u_dir(self, username: str) -> Path:
        return PATHS["USERS_DIR"] / username

    def _user_creds_path(self, username: str) -> Path:
        return self._u_dir(username) / "creds.json"

    def _enc_data_key_path(self, username: str) -> Path:
        return self._u_dir(username) / "enc_data_key.bin"

    def _keychain_path(self, username: str) -> Path:
        return self._u_dir(username) / "keychain.bin"

    def _items_dir(self, username: str) -> Path:
        return self._u_dir(username) / "items"

    # ------------- audit -------------

    def _audit(self, event: str, details: Dict[str, Any]) -> None:
        entry = {"ts": int(time.time()), "event": event, "details": details}
        with open(PATHS["AUDIT_LOG"], "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, separators=(",", ":")) + "\n")
        try:
            os.chmod(PATHS["AUDIT_LOG"], 0o600)
        except Exception:
            pass

    # ------------- user management -------------

    def create_user(self, username: str, password: str, pin: str) -> None:
        """
        Initialize a user with:
          - creds.json (salts + KDF params, no raw secrets)
          - enc_data_key.bin (DATA_KEY encrypted by ROOT_KEY)
          - empty encrypted keychain
          - items/ directory for file metadata
        """
        udir = self._u_dir(username)
        udir.mkdir(parents=True, exist_ok=True)

        kdf_cfg = self.cfg["kdf"]
        pin_salt = secrets.token_bytes(16)
        pw_salt = secrets.token_bytes(16)

        pepper = _read_pepper()
        pepper_id = base64.b64encode(hashlib.sha256(pepper).digest()).decode()

        pin_key = kdf_scrypt(pin + "|" + pepper_id, pin_salt, **kdf_cfg)
        pw_key = kdf_scrypt(password + "|" + pepper_id, pw_salt, **kdf_cfg)

        root_key = hkdf_simple(pin_key + pw_key, "VW2-ROOT")
        data_key = secrets.token_bytes(32)

        enc_data_key = aead_encrypt(root_key, data_key, aad=username.encode())

        creds = {
            "pin_salt_b64": base64.b64encode(pin_salt).decode(),
            "pw_salt_b64": base64.b64encode(pw_salt).decode(),
            "kdf": kdf_cfg,
            "created_at": int(time.time()),
            "version": 1,
        }

        _tight_write(self._user_creds_path(username), json.dumps(creds, indent=2), text=True)
        _tight_write(self._enc_data_key_path(username), enc_data_key)

        # empty keychain
        empty_kc = {"__meta__": {"ver": 1, "created_at": int(time.time())}}
        self._save_keychain(username, data_key, empty_kc)

        self._items_dir(username).mkdir(parents=True, exist_ok=True)
        self._audit("user_created", {"user": username})

    def change_pin(self, username: str, old_pin: str, new_pin: str, password: str) -> None:
        """
        Change PIN:
          - require both old PIN and current password
          - rewrap DATA_KEY with new ROOT_KEY
        """
        data_key = self._unlock_data_key(username, pin=old_pin, password=password)

        creds = json.loads(self._user_creds_path(username).read_text(encoding="utf-8"))
        kdf_cfg = creds["kdf"]
        pw_salt = base64.b64decode(creds["pw_salt_b64"])
        pin_salt = secrets.token_bytes(16)

        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        pin_key = kdf_scrypt(new_pin + "|" + pepper_id, pin_salt, **kdf_cfg)
        pw_key = kdf_scrypt(password + "|" + pepper_id, pw_salt, **kdf_cfg)
        root_key = hkdf_simple(pin_key + pw_key, "VW2-ROOT")

        enc_data_key = aead_encrypt(root_key, data_key, aad=username.encode())
        creds["pin_salt_b64"] = base64.b64encode(pin_salt).decode()

        _tight_write(self._user_creds_path(username), json.dumps(creds, indent=2), text=True)
        _tight_write(self._enc_data_key_path(username), enc_data_key)
        self._data_keys[username] = data_key
        self._audit("pin_changed", {"user": username})

    def change_password(self, username: str, pin: str, old_password: str, new_password: str) -> None:
        """
        Change master password:
          - require PIN and old password
          - rewrap DATA_KEY with new ROOT_KEY
        """
        data_key = self._unlock_data_key(username, pin=pin, password=old_password)

        creds = json.loads(self._user_creds_path(username).read_text(encoding="utf-8"))
        kdf_cfg = creds["kdf"]
        pin_salt = base64.b64decode(creds["pin_salt_b64"])
        pw_salt = secrets.token_bytes(16)

        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        pin_key = kdf_scrypt(pin + "|" + pepper_id, pin_salt, **kdf_cfg)
        pw_key = kdf_scrypt(new_password + "|" + pepper_id, pw_salt, **kdf_cfg)
        root_key = hkdf_simple(pin_key + pw_key, "VW2-ROOT")

        enc_data_key = aead_encrypt(root_key, data_key, aad=username.encode())
        creds["pw_salt_b64"] = base64.b64encode(pw_salt).decode()

        _tight_write(self._user_creds_path(username), json.dumps(creds, indent=2), text=True)
        _tight_write(self._enc_data_key_path(username), enc_data_key)
        self._data_keys[username] = data_key
        self._audit("password_changed", {"user": username})

    # ------------- unlocking (2FA core) -------------

    def _derive_root_key(self, username: str, pin: str, password: str) -> bytes:
        creds_path = self._user_creds_path(username)
        if not creds_path.exists():
            raise FileNotFoundError(f"User '{username}' not found")

        creds = json.loads(creds_path.read_text(encoding="utf-8"))
        kdf_cfg = creds["kdf"]
        pin_salt = base64.b64decode(creds["pin_salt_b64"])
        pw_salt = base64.b64decode(creds["pw_salt_b64"])

        pepper_id = base64.b64encode(hashlib.sha256(_read_pepper()).digest()).decode()
        pin_key = kdf_scrypt(pin + "|" + pepper_id, pin_salt, **kdf_cfg)
        pw_key = kdf_scrypt(password + "|" + pepper_id, pw_salt, **kdf_cfg)
        return hkdf_simple(pin_key + pw_key, "VW2-ROOT")

    def _unlock_data_key(self, username: str, pin: Optional[str] = None, password: Optional[str] = None) -> bytes:
        """
        Low-level: derive DATA_KEY using PIN + master password.
        Prompts interactively if values are missing.
        """
        if username in self._data_keys:
            return self._data_keys[username]

        if pin is None:
            pin = getpass.getpass(prompt=f"[{username}] PIN: ")
        if password is None:
            password = getpass.getpass(prompt=f"[{username}] Master password: ")

        root_key = self._derive_root_key(username, pin, password)
        enc_data_key = self._enc_data_key_path(username).read_bytes()
        try:
            data_key = aead_decrypt(root_key, enc_data_key, aad=username.encode())
        except Exception as e:
            self._audit("auth_failed", {"user": username})
            raise PermissionError("Invalid PIN and/or password") from e

        self._data_keys[username] = data_key
        self._audit("unlock_success", {"user": username})
        return data_key

    def unlock(self, username: str, pin: Optional[str] = None, password: Optional[str] = None) -> None:
        """
        Public helper: unlock DATA_KEY for this process.
        After this, keychain and file operations will not re-prompt
        until you call lock() or exit the process.
        """
        self._unlock_data_key(username, pin=pin, password=password)

    def lock(self, username: Optional[str] = None) -> None:
        """
        Forget DATA_KEY for one user (or all users if username is None).
        """
        if username is None:
            self._data_keys.clear()
        else:
            self._data_keys.pop(username, None)
        self._audit("lock", {"user": username or "*"})

    # ------------- keychain -------------

    def _kc_key(self, data_key: bytes) -> bytes:
        return hkdf_simple(data_key, "VW2-KEYCHAIN")

    def _load_keychain(self, username: str, data_key: bytes) -> Dict[str, str]:
        kc_path = self._keychain_path(username)
        if not kc_path.exists():
            return {"__meta__": {"ver": 1, "created_at": int(time.time())}}
        blob = kc_path.read_bytes()
        key = self._kc_key(data_key)
        raw = aead_decrypt(key, blob, aad=b"VW2-KC")
        data = json.loads(raw.decode("utf-8"))
        if "__meta__" not in data:
            data["__meta__"] = {"ver": 1}
        return data

    def _save_keychain(self, username: str, data_key: bytes, mapping: Dict[str, str]) -> None:
        key = self._kc_key(data_key)
        blob = aead_encrypt(key, json.dumps(mapping).encode("utf-8"), aad=b"VW2-KC")
        _tight_write(self._keychain_path(username), blob)

    def set_secret(self, username: str, label: str, value: str, overwrite: bool = True,
                   pin: Optional[str] = None, password: Optional[str] = None) -> None:
        data_key = self._unlock_data_key(username, pin=pin, password=password)
        kc = self._load_keychain(username, data_key)
        if not overwrite and label in kc:
            return
        kc[label] = value
        self._save_keychain(username, data_key, kc)
        self._audit("secret_set", {"user": username, "label": label})

    def get_secret(self, username: str, label: str, default: Optional[str] = None,
                   pin: Optional[str] = None, password: Optional[str] = None) -> Optional[str]:
        data_key = self._unlock_data_key(username, pin=pin, password=password)
        kc = self._load_keychain(username, data_key)
        return kc.get(label, default)

    def list_secrets(self, username: str,
                     pin: Optional[str] = None, password: Optional[str] = None) -> List[str]:
        data_key = self._unlock_data_key(username, pin=pin, password=password)
        kc = self._load_keychain(username, data_key)
        return sorted([k for k in kc.keys() if k != "__meta__"])

    # ------------- file registry -------------

    def _file_wrap_key(self, data_key: bytes) -> bytes:
        return hkdf_simple(data_key, "VW2-FILE-WRAP")

    def register_file(self, username: str, label: str, path: Path,
                      encrypt_now: bool = True, out_suffix: str = ".vwenc",
                      pin: Optional[str] = None, password: Optional[str] = None) -> str:
        """
        Register a file:
          - generate a random DEK
          - wrap DEK with a key derived from DATA_KEY
          - optionally encrypt the file immediately to path+suffix
        """
        data_key = self._unlock_data_key(username, pin=pin, password=password)
        wrap_key = self._file_wrap_key(data_key)

        items_dir = self._items_dir(username)
        items_dir.mkdir(parents=True, exist_ok=True)

        item_id = _rand_id(8)
        dek = secrets.token_bytes(32)
        dek_wrap = aead_encrypt(wrap_key, dek, aad=f"DEK|{label}".encode("utf-8"))

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

        _tight_write(items_dir / f"{item_id}.json", json.dumps(meta, indent=2), text=True)

        if encrypt_now:
            data = Path(path).read_bytes()
            ct = aead_encrypt(dek, data, aad=f"FILE|{meta['path']}".encode("utf-8"))
            _tight_write(Path(meta["out_path"]), ct)

        self._audit("file_registered", {"user": username, "item_id": item_id, "label": label})
        return item_id

    def _load_item_meta(self, username: str, item_id: str) -> Dict[str, Any]:
        f = self._items_dir(username) / f"{item_id}.json"
        if not f.exists():
            raise FileNotFoundError(f"Item '{item_id}' not found for user '{username}'")
        return json.loads(f.read_text(encoding="utf-8"))

    def decrypt_file(self, username: str, item_id: str,
                     out_path: Optional[Path] = None,
                     pin: Optional[str] = None, password: Optional[str] = None) -> Path:
        """
        Decrypt a registered file:
          - unwrap DEK with DATA_KEY-derived wrap key
          - decrypt encrypted file
        """
        data_key = self._unlock_data_key(username, pin=pin, password=password)
        wrap_key = self._file_wrap_key(data_key)

        meta = self._load_item_meta(username, item_id)
        enc_path = Path(meta["out_path"])
        raw = enc_path.read_bytes()

        dek_wrap = base64.b64decode(meta["dek_wrap_b64"])
        dek = aead_decrypt(wrap_key, dek_wrap, aad=f"DEK|{meta['label']}".encode("utf-8"))

        plaintext = aead_decrypt(dek, raw, aad=f"FILE|{meta['path']}".encode("utf-8"))

        if out_path is None:
            if enc_path.suffix == ".vwenc":
                out_path = enc_path.with_suffix("")
            else:
                out_path = enc_path.parent / (enc_path.name + ".dec")

        _tight_write(out_path, plaintext)
        self._audit("file_decrypted", {"user": username, "item_id": item_id, "out": str(out_path)})
        return out_path


# ======================================================================
# Demo usage: python3 vaultweaver.py
# ======================================================================

def demo() -> None:
    print("\n=== VaultWeaver 2FA demo (PIN + master password) ===")
    vw = VaultWeaver()

    user = "demo_user_" + _rand_id(3)
    pin = "12345678"
    pw = "StrongPass!42"

    print(f"[setup] create_user('{user}')")
    vw.create_user(user, password=pw, pin=pin)

    print("[unlock] using PIN + master password")
    vw.unlock(user, pin=pin, password=pw)

    print("[keychain] set_secret/get_secret")
    vw.set_secret(user, "gpt", "sk-EXAMPLE-KEY-123")
    print("  -> gpt =", vw.get_secret(user, "gpt"))

    print("[files] register + encrypt + decrypt")
    sample = PATHS["BASE"] / "sample.txt"
    sample.write_text("Top secret 2FA document.\n", encoding="utf-8")
    item_id = vw.register_file(user, "doc1", sample, encrypt_now=True)
    dec_path = vw.decrypt_file(user, item_id)
    print(f"  -> decrypted to: {dec_path}")

    print("[security] change PIN and password")
    vw.change_pin(user, old_pin=pin, new_pin="11223344", password=pw)
    vw.change_password(user, pin="11223344", old_password=pw, new_password="EvenStronger!99")

    print("[verify] unlock again with new creds, decrypt again")
    vw.unlock(user, pin="11223344", password="EvenStronger!99")
    dec_path2 = vw.decrypt_file(user, item_id)
    print(f"  -> decrypted again to: {dec_path2}")

    print("[lock] clear in-memory keys")
    vw.lock(user)
    print("=== done ===\n")


if __name__ == "__main__":
    demo()
