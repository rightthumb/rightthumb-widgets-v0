# pip install pyotp
# px -m pip install pyotp

'''md

# OTP

## 🧪 Usage Examples

### 1. Generate secret

```py
secret = OTP.secret()
print(secret)
```

---

### 2. Get current code

```py
print(OTP.code({
    'secret': secret
}))
```

---

### 3. Verify code

```py
valid = OTP.verify({
    'secret': secret,
    'code': '123456',
    'window': 1
})
print(valid)
```

---

### 4. Generate QR URI (for Google Authenticator, etc.)

```py
uri = OTP.uri({
    'secret': secret,
    'account': 'scott@sds.sh',
    'issuer': 'SDS'
})
print(uri)
```

---

### 5. CLI live codes

```py
OTP.cli({
    'secret': secret
})
```

'''

import time
import pyotp # type: ignore


class OTP:
    """
    Minimal static-style TOTP helper

    All functions accept a single dict for consistency with your pattern.
    """

    # ----------------------------
    # INIT / DEFAULTS
    # ----------------------------
    DEFAULTS = {
        'digits': 6,
        'interval': 30,
        'issuer': 'App',
        'account': 'user@example.com',
    }

    @staticmethod
    def _cfg(cfg):
        c = OTP.DEFAULTS.copy()
        if isinstance(cfg, dict):
            c.update(cfg)
        return c

    # ----------------------------
    # SECRET GENERATION
    # ----------------------------
    @staticmethod
    def secret(cfg=None):
        """
        Generate a new base32 secret
        """
        return pyotp.random_base32()

    # ----------------------------
    # TOTP OBJECT
    # ----------------------------
    @staticmethod
    def _totp(cfg):
        c = OTP._cfg(cfg)
        return pyotp.TOTP(
            c['secret'],
            digits=c['digits'],
            interval=c['interval']
        )

    # ----------------------------
    # CURRENT CODE
    # ----------------------------
    @staticmethod
    def code(cfg):
        """
        Get current TOTP code
        cfg = {'secret': '...'}
        """
        return OTP._totp(cfg).now()

    # ----------------------------
    # VERIFY CODE
    # ----------------------------
    @staticmethod
    def verify(cfg):
        """
        Verify a code
        cfg = {
            'secret': '...',
            'code': '123456',
            'window': 1   # optional drift window
        }
        """
        c = OTP._cfg(cfg)
        return OTP._totp(c).verify(
            c['code'],
            valid_window=c.get('window', 0)
        )

    # ----------------------------
    # PROVISIONING URI
    # ----------------------------
    @staticmethod
    def uri(cfg):
        """
        Generate QR URI for authenticator apps
        """
        c = OTP._cfg(cfg)
        return OTP._totp(c).provisioning_uri(
            name=c['account'],
            issuer_name=c['issuer']
        )

    # ----------------------------
    # TIME REMAINING
    # ----------------------------
    @staticmethod
    def remaining(cfg=None):
        """
        Seconds remaining in current cycle
        """
        c = OTP._cfg(cfg)
        return c['interval'] - (int(time.time()) % c['interval'])

    # ----------------------------
    # CLI HELPER
    # ----------------------------
    @staticmethod
    def cli(cfg):
        """
        Simple CLI loop
        """
        c = OTP._cfg(cfg)

        while True:
            code = OTP.code(c)
            remaining = OTP.remaining(c)

            print(f"{code} ({remaining}s)", end='\r', flush=True)
            time.sleep(1)

    @staticmethod
    def test(_print=True):
        """
        Simple test code generation with random secret
        """
        secret = OTP.secret()
        code = OTP.code({'secret': secret})
        if _print:
            print(f"Secret: {secret}")
            print(f"Current Code: {code}")

if __name__ == '__main__' and False:
    if False:
        secret = OTP.secret()
        print(f"Secret: {secret}")
        otp = OTP.code({'secret': secret})
        print(f"Current Code: {otp}")
    else:
        start = time.time()
        OTP.test()

        print()

        loops = 1000
        loops -= 1
        for i in range(loops):
            # print(f"Loop {i+1}/{loops}")
            OTP.test(_print=False)
        end = time.time()
        print(f"Elapsed time for {loops+1} loops: {end - start:.2f} seconds")