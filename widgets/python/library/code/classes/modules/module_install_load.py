def load(mod, *items):
    return ModuleLoader().load(mod, items if items else None)

import sys
import subprocess
import importlib
import json
import urllib.request
import urllib.error


class ModuleLoader:
    def __init__(self, timeout=5, upgrade_pip=False, quiet=False):
        self.timeout = timeout
        self.upgrade_pip = upgrade_pip
        self.quiet = quiet

    def _log(self, msg: str):
        if not self.quiet:
            print(msg)

    def _pypi_package_name(self, name: str) -> str:
        url = f"https://pypi.org/pypi/{name}/json"
        try:
            with urllib.request.urlopen(url, timeout=self.timeout) as resp:
                data = json.load(resp)
                return data["info"]["name"]
        except Exception:
            return name

    def _pip(self, args):
        cmd = [sys.executable, "-m", "pip"] + list(args)
        if self.quiet:
            return subprocess.check_call(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        return subprocess.check_call(cmd)

    def _ensure_pip_up_to_date(self):
        if self.upgrade_pip:
            self._log("[i] Upgrading pip...")
            self._pip(["install", "--upgrade", "pip"])

    def install(self, name: str) -> str:
        pkg = self._pypi_package_name(name)
        self._ensure_pip_up_to_date()
        self._log(f"[i] Installing: {pkg}")
        self._pip(["install", pkg])
        return pkg

    def load(self, module_name: str, items: list | None = None):
        """
        Examples:
            mod = load("gtts")
            html = load("lxml", ["html"])
            dt, td = load("datetime", ["datetime", "timedelta"])
        """
        try:
            module = importlib.import_module(module_name)
        except Exception:
            pkg = self.install(module_name)
            try:
                module = importlib.import_module(module_name)
            except Exception as e:
                raise RuntimeError(
                    f"Module '{module_name}' failed to import after installing '{pkg}'"
                ) from e

        if not items:
            return module

        exports = []
        for name in items:
            if not hasattr(module, name):
                raise AttributeError(
                    f"Module '{module_name}' has no attribute '{name}'"
                )
            exports.append(getattr(module, name))

        return exports[0] if len(exports) == 1 else tuple(exports)

def test_module_loader():
    loader = ModuleLoader(upgrade_pip=False, quiet=False)

    tests = [
        # stdlib (no install)
        ("datetime", ["datetime", "timedelta"]),

        # PyPI name == import name
        ("validators", ["url"]),
        ("pytz", ["UTC"]),
        ("iso8601", ["parse_date"]),

        # PyPI name != import name
        ("dateutil", ["parser"]),           # python-dateutil
        ("text_unidecode", ["unidecode"]),   # text-unidecode

        # hyphenated PyPI package
        ("more_itertools", ["chunked"]),

        # submodule imports
        ("boltons.iterutils", ["chunked"]),
        ("rich.console", ["Console"]),

        # compiled extension (environment dependent)
        ("lxml", ["html"]),
    ]

    for module_name, items in tests:
        try:
            result = loader.load(module_name, items)
            if isinstance(result, tuple):
                names = []
                for obj in result:
                    names.append(getattr(obj, "__name__", obj.__class__.__name__))
                print(f"[OK] {module_name} -> {', '.join(names)}")
            else:
                name = getattr(result, "__name__", result.__class__.__name__)
                print(f"[OK] {module_name} -> {name}")
        except Exception as e:
            print(f"[FAIL] {module_name}: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="ModuleLoader app: import a module, optionally install it from PyPI, optionally import items."
    )
    parser.add_argument("-module", help="Module to import (and install if missing). Example: gtts, dateutil, rich.console")
    parser.add_argument(
        "-items",
        help="Comma-separated list of item names to import from the module. Example: datetime,timedelta",
        default="",
    )
    parser.add_argument("--upgrade-pip", action="store_true", help="Upgrade pip before installing packages.")
    parser.add_argument("--quiet", action="store_true", help="Suppress pip output and loader logs.")
    parser.add_argument("--test", action="store_true", help="Run built-in tests (installs may occur).")

    args = parser.parse_args()

    if args.test:
        test_module_loader()
        raise SystemExit(0)

    if not args.module:
        parser.print_help()
        raise SystemExit(1)

    loader = ModuleLoader(upgrade_pip=args.upgrade_pip, quiet=args.quiet)

    items = []
    if args.items.strip():
        items = [x.strip() for x in args.items.split(",") if x.strip()]

    obj = loader.load(args.module, items if items else None)

    if isinstance(obj, tuple):
        print("Loaded:", ", ".join(getattr(x, "__name__", x.__class__.__name__) for x in obj))
    else:
        print("Loaded:", getattr(obj, "__name__", obj.__class__.__name__))
