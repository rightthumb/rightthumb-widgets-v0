#!/usr/bin/env python3
"""
Offline IP → Country lookups using only public-download databases.

Providers:
  - DBIPLiteProvider          (CSV monthly, public)
  - IPDenyCountryZonesProvider (CIDR lists per country, public)
  - IP2LocationLiteProvider   (DB1 CSV, public)

Usage:
  python ip_geo.py 8.8.8.8

Data directory:
  /opt/ip_geo   (created automatically; requires permissions)
"""

import os
import io
import sys
import csv
import gzip
import zipfile
import tarfile
import shutil
import typing as t
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime, timezone
from ipaddress import ip_address, ip_network

if os.path.isdir('/opt'):
    DATA_ROOT = Path("/opt/ip_geo")
else:
    DATA_ROOT = Path.home() / ".ip_geo"
# ------------- Utilities -------------
def ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def http_get(url: str, dest: Path, chunk: int = 1 << 16, timeout: int = 60) -> Path:
    import urllib.request
    ensure_dir(dest.parent)
    req = urllib.request.Request(url, headers={"User-Agent": "OfflineGeo/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r, open(dest, "wb") as f:
        while True:
            buf = r.read(chunk)
            if not buf:
                break
            f.write(buf)
    return dest

def ip_to_int_and_ver(ip: str) -> t.Tuple[int, int]:
    ipa = ip_address(ip)
    return int(ipa), ipa.version

# ------------- Base class -------------
@dataclass
class GeoProvider(ABC):
    name: str
    data_dir: Path
    last_updated: t.Optional[str] = field(default=None)

    def __post_init__(self):
        ensure_dir(self.data_dir)

    @abstractmethod
    def download(self) -> None:
        ...

    @abstractmethod
    def load(self) -> None:
        ...

    @abstractmethod
    def country(self, ip: str) -> t.Optional[str]:
        """Return ISO country code (e.g., 'US') or None."""
        ...

# ------------- DB-IP Lite (public monthly CSV) -------------
@dataclass
class DBIPLiteProvider(GeoProvider):
    """
    Uses: https://download.db-ip.com/free/dbip-country-lite-YYYY-MM.csv.gz
    CSV columns: start_ip, end_ip, country_code
    """
    year_month: t.Optional[str] = None  # default: current UTC YYYY-MM

    _v4_starts: t.List[int] = field(default_factory=list, init=False)
    _v4_ends: t.List[int] = field(default_factory=list, init=False)
    _v4_cc: t.List[str] = field(default_factory=list, init=False)

    _v6_starts: t.List[int] = field(default_factory=list, init=False)
    _v6_ends: t.List[int] = field(default_factory=list, init=False)
    _v6_cc: t.List[str] = field(default_factory=list, init=False)

    def _ym(self) -> str:
        return self.year_month or datetime.utcnow().strftime("%Y-%m")

    def _url(self) -> str:
        ym = self._ym()
        return f"https://download.db-ip.com/free/dbip-country-lite-{ym}.csv.gz"

    def download(self) -> None:
        out = ensure_dir(self.data_dir / "dbip")
        gz = out / f"dbip-country-lite-{self._ym()}.csv.gz"
        csv_path = out / "dbip-country-lite-latest.csv"

        # If we already have a CSV, skip; otherwise try to fetch current month
        if not csv_path.exists():
            print(f"[DB-IP] Downloading {gz.name} ...")
            http_get(self._url(), gz)
            # Decompress
            with gzip.open(gz, "rb") as zf, open(csv_path, "wb") as f:
                shutil.copyfileobj(zf, f)
        self.last_updated = now_iso()

    def load(self) -> None:
        csv_path = self.data_dir / "dbip" / "dbip-country-lite-latest.csv"
        if not csv_path.exists():
            raise FileNotFoundError("[DB-IP] CSV missing; run download() first.")

        self._v4_starts.clear(); self._v4_ends.clear(); self._v4_cc.clear()
        self._v6_starts.clear(); self._v6_ends.clear(); self._v6_cc.clear()

        with open(csv_path, newline="", encoding="utf-8") as f:
            rdr = csv.reader(f)
            for row in rdr:
                if len(row) < 3:
                    continue
                s, e, cc = row[0].strip(), row[1].strip(), row[2].strip().upper()
                try:
                    s_int, s_ver = ip_to_int_and_ver(s)
                    e_int, e_ver = ip_to_int_and_ver(e)
                except Exception:
                    continue
                if s_ver != e_ver:
                    continue
                if s_ver == 4:
                    self._v4_starts.append(s_int); self._v4_ends.append(e_int); self._v4_cc.append(cc)
                else:
                    self._v6_starts.append(s_int); self._v6_ends.append(e_int); self._v6_cc.append(cc)

    def _lookup(self, ip_str: str) -> t.Optional[str]:
        import bisect
        ip_int, ver = ip_to_int_and_ver(ip_str)
        if ver == 4 and self._v4_starts:
            i = bisect.bisect_right(self._v4_starts, ip_int) - 1
            if i >= 0 and ip_int <= self._v4_ends[i]:
                return self._v4_cc[i]
        elif ver == 6 and self._v6_starts:
            i = bisect.bisect_right(self._v6_starts, ip_int) - 1
            if i >= 0 and ip_int <= self._v6_ends[i]:
                return self._v6_cc[i]
        return None

    def country(self, ip: str) -> t.Optional[str]:
        try:
            return self._lookup(ip)
        except Exception:
            return None

# ------------- IPdeny (public per-country CIDRs) -------------
@dataclass
class IPDenyCountryZonesProvider(GeoProvider):
    """
    Uses: https://www.ipdeny.com/ipblocks/data/countries/{cc}.zone
    We download many country files and build (network -> ISO) mapping.
    """
    base_url: str = "https://www.ipdeny.com/ipblocks/data/countries"
    iso_list: t.Optional[t.List[str]] = None  # None -> use default world list

    _nets: t.List[t.Tuple[t.Any, str]] = field(default_factory=list, init=False)

    def _default_iso_list(self) -> t.List[str]:
        # ISO-3166 alpha-2 (broad list; you can trim if you only care about US vs not-US)
        return [  # (trimmed but still wide coverage)
            "us","ca","mx","br","ar","gb","ie","de","fr","es","it","pt","nl","be","dk","se","no","fi","is","pl","cz",
            "sk","hu","at","ch","ro","bg","gr","ru","ua","by","lt","lv","ee","tr","cy","mt","si","hr","ba","rs","al",
            "mk","md","ge","am","az","kz","kg","uz","tm","af","ir","iq","sy","jo","il","lb","sa","ae","qa","kw","om",
            "ye","eg","ly","tn","dz","ma","sn","gh","ng","za","ke","ug","tz","mz","ao","cm","ci","et","sd","ss","rw",
            "bi","bw","na","zm","zw","mu","sc","in","pk","bd","lk","np","bt","mv","mm","th","la","kh","vn","my","sg",
            "id","ph","cn","hk","mo","tw","jp","kr","mn","au","nz","pg","fj","sb","vu","tl"
        ]

    def download(self) -> None:
        out = ensure_dir(self.data_dir / "ipdeny")
        iso_list = self.iso_list or self._default_iso_list()
        for cc in iso_list:
            url = f"{self.base_url}/{cc}.zone"
            dest = out / f"{cc}.zone"
            if dest.exists():
                continue
            try:
                print(f"[IPdeny] Downloading {cc}.zone ...")
                http_get(url, dest)
            except Exception as e:
                print(f"[IPdeny] Skip {cc}: {e}")
        self.last_updated = now_iso()

    def load(self) -> None:
        self._nets.clear()
        zone_dir = self.data_dir / "ipdeny"
        for f in zone_dir.glob("*.zone"):
            cc = f.stem.upper()
            with open(f, "r", encoding="utf-8", errors="ignore") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    try:
                        net = ip_network(line, strict=False)
                        self._nets.append((net, cc))
                    except Exception:
                        continue
        # Match most specific first
        self._nets.sort(key=lambda x: (x[0].version, -x[0].prefixlen))

    def country(self, ip: str) -> t.Optional[str]:
        try:
            ipa = ip_address(ip)
        except Exception:
            return None
        for net, cc in self._nets:
            if net.version != ipa.version:
                continue
            if ipa in net:
                return cc
        return None

# ------------- IP2Location LITE DB1 (public ZIP) -------------
@dataclass
class IP2LocationLiteProvider(GeoProvider):
    """
    Uses: https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP
    CSV columns: IP_FROM, IP_TO, COUNTRY_CODE, COUNTRY_NAME
    (IP_FROM/TO are integers for IPv4; some variants also include IPv6 integers)
    """
    url: str = "https://download.ip2location.com/lite/IP2LOCATION-LITE-DB1.CSV.ZIP"

    _v4_from: t.List[int] = field(default_factory=list, init=False)
    _v4_to: t.List[int] = field(default_factory=list, init=False)
    _v4_cc: t.List[str] = field(default_factory=list, init=False)

    _v6_from: t.List[int] = field(default_factory=list, init=False)
    _v6_to: t.List[int] = field(default_factory=list, init=False)
    _v6_cc: t.List[str] = field(default_factory=list, init=False)

    def download(self) -> None:
        out = ensure_dir(self.data_dir / "ip2location")
        zpath = out / "IP2LOCATION-LITE-DB1.CSV.ZIP"
        if not any(out.glob("IP2LOCATION-LITE-DB1*.CSV")):
            print("[IP2Location] Downloading DB1 ZIP ...")
            http_get(self.url, zpath)
            with zipfile.ZipFile(zpath, "r") as zf:
                zf.extractall(out)
        self.last_updated = now_iso()

    def load(self) -> None:
        out = self.data_dir / "ip2location"
        csv_path = next((p for p in out.glob("IP2LOCATION-LITE-DB1*.CSV")), None)
        if not csv_path:
            raise FileNotFoundError("[IP2Location] CSV not found; run download() first.")

        self._v4_from.clear(); self._v4_to.clear(); self._v4_cc.clear()
        self._v6_from.clear(); self._v6_to.clear(); self._v6_cc.clear()

        with open(csv_path, newline="", encoding="utf-8") as f:
            rdr = csv.reader(f)
            for row in rdr:
                if len(row) < 4:
                    continue
                try:
                    ip_from = int(row[0]); ip_to = int(row[1]); cc = row[2].strip().upper()
                except Exception:
                    continue
                # Heuristic: > 2^32-1 → use IPv6 bucket
                if ip_from > 0xFFFFFFFF or ip_to > 0xFFFFFFFF:
                    self._v6_from.append(ip_from); self._v6_to.append(ip_to); self._v6_cc.append(cc)
                else:
                    self._v4_from.append(ip_from); self._v4_to.append(ip_to); self._v4_cc.append(cc)

        # Defensive sorting
        if self._v4_from and any(self._v4_from[i] > self._v4_from[i+1] for i in range(len(self._v4_from)-1)):
            zipped = sorted(zip(self._v4_from, self._v4_to, self._v4_cc))
            self._v4_from, self._v4_to, self._v4_cc = map(list, zip(*zipped))
        if self._v6_from and any(self._v6_from[i] > self._v6_from[i+1] for i in range(len(self._v6_from)-1)):
            zipped = sorted(zip(self._v6_from, self._v6_to, self._v6_cc))
            self._v6_from, self._v6_to, self._v6_cc = map(list, zip(*zipped))

    def _lookup_v4(self, ip_int: int) -> t.Optional[str]:
        import bisect
        if not self._v4_from:
            return None
        i = bisect.bisect_right(self._v4_from, ip_int) - 1
        if i >= 0 and ip_int <= self._v4_to[i]:
            return self._v4_cc[i]
        return None

    def _lookup_v6(self, ip_int: int) -> t.Optional[str]:
        import bisect
        if not self._v6_from:
            return None
        i = bisect.bisect_right(self._v6_from, ip_int) - 1
        if i >= 0 and ip_int <= self._v6_to[i]:
            return self._v6_cc[i]
        return None

    def country(self, ip: str) -> t.Optional[str]:
        try:
            ipa = ip_address(ip)
        except Exception:
            return None
        ip_int = int(ipa)
        if ipa.version == 4:
            return self._lookup_v4(ip_int)
        else:
            return self._lookup_v6(ip_int)

# ------------- One-shot runner -------------
def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python ip_geo.py <ip>")
        sys.exit(1)

    test_ip = sys.argv[1].strip()
    ensure_dir(DATA_ROOT)

    providers: t.List[GeoProvider] = [
        DBIPLiteProvider(name="dbip", data_dir=DATA_ROOT),
        IPDenyCountryZonesProvider(name="ipdeny", data_dir=DATA_ROOT),
        IP2LocationLiteProvider(name="ip2location", data_dir=DATA_ROOT),
    ]

    results = {}
    for p in providers:
        try:
            # If provider data is missing, download it
            try:
                p.load()
            except FileNotFoundError:
                p.download()
                p.load()

            cc = p.country(test_ip)
            results[p.name] = cc
        except Exception as e:
            results[p.name] = f"ERROR: {e}"

    print(f"IP: {test_ip}")
    for name, val in results.items():
        print(f"{name:>12}: {val}")

    # Quick helper: USA vs not-USA (majority vote)
    votes = [cc for cc in results.values() if isinstance(cc, str) and len(cc) == 2]
    is_us = votes and sum(1 for v in votes if v == "US") >= (len(votes) // 2 + 1)
    print(f"\nMajority says USA: {bool(is_us)}")

if __name__ == "__main__":
    main()
