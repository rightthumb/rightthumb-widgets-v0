#!/usr/bin/env python3
import argparse
import math
import os
import platform
import string
import subprocess
import sys
from secrets import choice
from random import shuffle

CONFUSABLES = set("O0oIl1|`'\" ()[]{}:;,.~^")
_SYMBOLS_ = "-_+=/\\*?.:,;@[]{}~'#&|<>()"
_SYMBOLS_ = "-=+_/"


def build_charset(use_lower, use_upper, use_digits, use_symbols, no_confusables):
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        # A conservative symbol set that works in most places
        charset += _SYMBOLS_
    if no_confusables:
        charset = "".join(ch for ch in charset if ch not in CONFUSABLES)
    return "".join(sorted(set(charset)))  # dedupe

def generate_password(length, charset, require_classes, class_sets):
    if not charset:
        raise ValueError("Character set is empty. Enable some classes or disable --no-confusables.")
    if length <= 0:
        raise ValueError("Length must be > 0.")

    password_chars = []
    if require_classes:
        required = [s for s in class_sets if s]
        if len(required) > length:
            raise ValueError(f"Length {length} too short for {len(required)} required classes.")
        for s in required:
            password_chars.append(choice(s))

    while len(password_chars) < length:
        password_chars.append(choice(charset))

    shuffle(password_chars)
    return "".join(password_chars)

def entropy_bits(length, charset_size):
    if charset_size <= 1:
        return 0.0
    return length * math.log2(charset_size)

def format_time(seconds):
    units = [
        ("years", 365.25*24*3600),
        ("days", 24*3600),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1),
    ]
    parts = []
    for name, secs in units:
        if seconds >= secs:
            qty = int(seconds // secs)
            seconds -= qty * secs
            parts.append(f"{qty} {name}")
        if len(parts) >= 2:
            break
    return ", ".join(parts) if parts else "less than 1 second"

def set_linux_password(user, password):
    """
    Set a user's password using chpasswd (reads 'user:password' from stdin).
    Requires root. Does not print the password.
    """
    try:
        res = subprocess.run(
            ["chpasswd"],
            input=f"{user}:{password}",
            text=True,
            check=True,
            capture_output=True,
        )
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip() or e.stdout.strip() or str(e)

def make_shadow_hash_sha512(password):
    """
    Return a SHA-512 crypt() hash suitable for /etc/shadow and 'chpasswd -e'.
    """
    try:
        import crypt
    except Exception as e:
        raise RuntimeError(f"crypt module unavailable: {e}")
    # SHA-512 is widely supported and strong for local passwords.
    salt = crypt.mksalt(crypt.METHOD_SHA512)
    return crypt.crypt(password, salt)

def ensure_root_for_set():
    if platform.system().lower() != "linux":
        sys.stderr.write("Error: --set-user only supported on Linux.\n")
        sys.exit(2)
    if hasattr(os, "geteuid") and os.geteuid() != 0:
        sys.stderr.write("Error: --set-user requires root (sudo).\n")
        sys.exit(2)

def main():
    ap = argparse.ArgumentParser(
        description="Generate high-entropy passwords using cryptographically secure randomness."
    )
    ap.add_argument("-l", "--length", type=int, default=20, help="Password length (default: 20).")
    ap.add_argument("-n", "--num", type=int, default=1, help="How many passwords to generate.")
    ap.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters.")
    ap.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters.")
    ap.add_argument("--no-digits", action="store_true", help="Exclude digits.")
    ap.add_argument("--no-symbols", action="store_true", help="Exclude symbols.")
    ap.add_argument("--no-confusables", action="store_true",
                    help="Remove look-alike characters (O/0, l/1/|, etc.).")
    ap.add_argument("--require-classes", action="store_true",
                    help="Ensure at least one of each enabled class (lower/upper/digit/symbol).")
    ap.add_argument("--guesses-per-sec", type=float, default=1e12,
                    help="Cracking speed to estimate time (default: 1e12 guesses/sec).")
    ap.add_argument("--quiet", action="store_true", help="Print only passwords (no metrics).")

    # New operational switches
    ap.add_argument("--set-user", metavar="USER",
                    help="Linux ONLY: set the generated password for USER via 'chpasswd' (requires root).")
    ap.add_argument("--show", action="store_true",
                    help="When used with --set-user, ALSO print the generated password to stdout.")
    ap.add_argument("--hash-only", action="store_true",
                    help="Print a SHA-512 shadow hash instead of plaintext (for use with 'chpasswd -e').")

    # parse_known_args returns (known, unknown)
    args, unknown = ap.parse_known_args(); leftover = [u for u in unknown if u.startswith("-")]
    # (Ignored silently on purpose.)

    # Sanity checks around set-user / num
    if args.set_user and args.num != 1:
        sys.stderr.write("Error: --set-user requires exactly one password (use -n 1).\n")
        sys.exit(2)
    if args.set_user and args.hash_only:
        # You can still do it: we set nothing automatically, just output the hash.
        # But mixing both is confusing; guide the user.
        sys.stderr.write("Note: --hash-only ignores --set-user; you must apply the hash yourself with 'chpasswd -e'.\n")

    use_lower = not args.no_lower
    use_upper = not args.no_upper
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols

    lower_set  = "".join(ch for ch in string.ascii_lowercase if ch not in CONFUSABLES) if args.no_confusables else string.ascii_lowercase
    upper_set  = "".join(ch for ch in string.ascii_uppercase if ch not in CONFUSABLES) if args.no_confusables else string.ascii_uppercase
    digit_set  = "".join(ch for ch in string.digits            if ch not in CONFUSABLES) if args.no_confusables else string.digits
    symbol_set = _SYMBOLS_  # conservative

    class_sets = []
    if use_lower:   class_sets.append(lower_set)
    if use_upper:   class_sets.append(upper_set)
    if use_digits:  class_sets.append(digit_set)
    if use_symbols: class_sets.append(symbol_set)

    charset = build_charset(use_lower, use_upper, use_digits, use_symbols, args.no_confusables)
    if not charset:
        print("Error: After exclusions, the character set is empty.", file=sys.stderr)
        sys.exit(2)

    if not args.quiet and not args.set_user and not args.hash_only:
        print(f"Charset size: {len(charset)}")
        print(f"Length: {args.length}")
        H = entropy_bits(args.length, len(charset))
        print(f"Estimated entropy: {H:.1f} bits")
        worst_case = 2 ** H
        t = worst_case / max(args.guesses_per_sec, 1.0)
        print(f"Brute-force @ {args.guesses_per_sec:,.0f} guesses/sec: ~{format_time(t)} (worst-case)")
        if args.require_classes:
            enabled = []
            if use_lower: enabled.append("lower")
            if use_upper: enabled.append("upper")
            if use_digits: enabled.append("digit")
            if use_symbols: enabled.append("symbol")
            print(f"Class requirements: at least one of: {', '.join(enabled)}")
        print()

    # Generate (usually one) password
    passwords = []
    for _ in range(args.num):
        pwd = generate_password(args.length, charset, args.require_classes, class_sets)
        passwords.append(pwd)

    # --hash-only path: emit a hash and stop (no printing plaintext unless user wants it)
    if args.hash_only:
        try:
            h = make_shadow_hash_sha512(passwords[0])
        except Exception as e:
            sys.stderr.write(f"Error creating hash: {e}\n")
            sys.exit(2)
        print(h)
        sys.exit(0)

    # --set-user path: set via chpasswd; only print password if --show
    if args.set_user:
        ensure_root_for_set()
        ok, err = set_linux_password(args.set_user, passwords[0])
        if not ok:
            sys.stderr.write(f"Failed to set password for '{args.set_user}': {err}\n")
            sys.exit(1)
        sys.stderr.write(f"Password updated for user '{args.set_user}'.\n")
        if args.show:
            print(passwords[0])
        sys.exit(0)

    # Default path: print generated passwords (respect --quiet metrics toggle above)
    for p in passwords:
        print(p)

if __name__ == "__main__":
    main()
