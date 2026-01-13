#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict, Iterator

from pymongo import MongoClient, UpdateOne, ASCENDING
from pymongo.errors import BulkWriteError
from bson.binary import Binary
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId

# Optional streaming
try:
    import ijson
    HAVE_IJSON = True
except Exception:
    HAVE_IJSON = False

# Optional ISO-8601 parsing
try:
    from dateutil import parser as date_parser
    HAVE_DATEUTIL = True
except Exception:
    HAVE_DATEUTIL = False

INT64_MIN = -(2**63)
INT64_MAX = (2**63) - 1
HEX24_RE = re.compile(r"^[0-9a-fA-F]{24}$")
ISO_DATE_HINT_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:")

# Mongo key rules: keys cannot contain '.' and cannot start with '$'
def sanitize_key(key: str) -> str:
    if not isinstance(key, str):
        key = str(key)
    # Replace '.' with a visible safe char (middle dot) to preserve readability
    k = key.replace(".", "·")
    if k.startswith("$"):
        k = "﹩" + k[1:]
    return k

def sanitize_dict_keys(d: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(d, dict):
        return d
    out = {}
    for k, v in d.items():
        out[sanitize_key(k)] = v
    return out

def to_bson_safe(obj: Any, *, coerce_objectid: bool, coerce_isodate: bool) -> Any:
    """
    Recursively convert Python/parsed JSON values into types accepted by PyMongo/BSON.
    - Decimal -> Decimal128
    - oversized int -> Decimal128
    - floats NaN/Inf -> None
    - bytes/bytearray -> Binary
    - set/tuple -> list
    - dict keys sanitized for Mongo
    - Optionally convert 24-hex strings to ObjectId
    - Optionally convert ISO-8601-ish strings to datetime
    """
    # Primitives
    if obj is None or isinstance(obj, (bool, str)):
        # Optional coercions for strings
        if isinstance(obj, str):
            if coerce_objectid and HEX24_RE.match(obj):
                try:
                    return ObjectId(obj)
                except Exception:
                    pass
            if coerce_isodate and (ISO_DATE_HINT_RE.search(obj) or obj.endswith("Z")) and HAVE_DATEUTIL:
                try:
                    dt = date_parser.isoparse(obj)
                    if not dt.tzinfo:
                        dt = dt.replace(tzinfo=timezone.utc)
                    return dt
                except Exception:
                    pass
        return obj

    if isinstance(obj, Decimal):
        # Convert to Decimal128 via string for precision
        try:
            return Decimal128(str(obj))
        except Exception:
            return float(obj)

    if isinstance(obj, float):
        # Handle NaN/Inf which Mongo can't store
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj

    if isinstance(obj, int):
        if obj < INT64_MIN or obj > INT64_MAX:
            # Preserve value as Decimal128
            return Decimal128(str(obj))
        return obj

    if isinstance(obj, (bytes, bytearray)):
        return Binary(bytes(obj))

    if isinstance(obj, (set, tuple, list)):
        return [to_bson_safe(x, coerce_objectid=coerce_objectid, coerce_isodate=coerce_isodate) for x in obj]

    if isinstance(obj, dict):
        # Sanitize keys then recurse
        clean = sanitize_dict_keys(obj)
        return {
            k: to_bson_safe(v, coerce_objectid=coerce_objectid, coerce_isodate=coerce_isodate)
            for k, v in clean.items()
        }

    # Fallback: stringify unknowns
    return str(obj)

def iter_json_array(path: str) -> Iterator[Dict[str, Any]]:
    """
    Yields dict items from a top-level JSON array.
    Uses ijson for streaming if available; otherwise loads into memory.
    """
    if HAVE_IJSON:
        with open(path, "rb") as f:
            # Return floats (not Decimal) to avoid Decimal sneaking in
            for obj in ijson.items(f, "item", use_float=True):
                if isinstance(obj, dict):
                    yield obj
    else:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Top-level JSON must be an array.")
            for obj in data:
                if isinstance(obj, dict):
                    yield obj

def ensure_indexes(coll, unique_on=("id", "backup")):
    """
    Create indexes helpful for your workload.
    """
    if unique_on:
        coll.create_index([(f, ASCENDING) for f in unique_on], unique=True, name="uniq_id_backup")
    coll.create_index([("timestamp_dt", ASCENDING)], name="idx_timestamp_dt")
    coll.create_index([("file", ASCENDING)], name="idx_file")

def maybe_add_timestamp_dt(doc: Dict[str, Any]) -> None:
    """
    Adds timestamp_dt from numeric 'timestamp' if present.
    """
    ts = doc.get("timestamp")
    if isinstance(ts, (int, float)):
        try:
            doc["timestamp_dt"] = datetime.fromtimestamp(float(ts), tz=timezone.utc)
        except Exception:
            pass

def migrate(
    path: str,
    mongo_uri: str,
    db_name: str,
    coll_name: str,
    batch_size: int,
    dry_run: bool,
    quiet: bool,
    coerce_objectid: bool,
    coerce_isodate: bool,
    unique_by: str
):
    client = MongoClient(mongo_uri)
    coll = client[db_name][coll_name]

    unique_fields = None
    if unique_by:
        unique_fields = tuple(x.strip() for x in unique_by.split(",") if x.strip())
    ensure_indexes(coll, unique_on=unique_fields)

    ops = []
    total = inserted = modified = skipped = failed = 0

    def flush():
        nonlocal ops, inserted, modified, failed
        if not ops or dry_run:
            ops.clear()
            return
        try:
            res = coll.bulk_write(ops, ordered=False)
            inserted += res.upserted_count or 0
            modified += res.modified_count or 0
        except BulkWriteError as e:
            details = e.details or {}
            failed += len(details.get("writeErrors", []))
        finally:
            ops.clear()

    for rec in iter_json_array(path):
        total += 1
        safe = to_bson_safe(rec, coerce_objectid=coerce_objectid, coerce_isodate=coerce_isodate)
        if not isinstance(safe, dict):
            skipped += 1
            continue

        maybe_add_timestamp_dt(safe)

        # Build upsert filter from chosen unique fields
        if unique_fields:
            filt = {f: safe.get(f) for f in unique_fields}
            # If any unique field missing, skip (or generate a deterministic _id here)
            if any(v is None for v in filt.values()):
                skipped += 1
                continue
        else:
            # If not using a unique combo, fall back to id if present; else allow duplicates
            if "id" in safe and "backup" in safe:
                filt = {"id": safe["id"], "backup": safe["backup"]}
            elif "id" in safe:
                filt = {"id": safe["id"]}
            else:
                # No stable key; insert as-is (no upsert)
                ops.append(UpdateOne({"_id": ObjectId()}, {"$setOnInsert": safe}, upsert=True))
                if len(ops) >= batch_size:
                    flush()
                continue

        ops.append(UpdateOne(filt, {"$set": safe}, upsert=True))
        if len(ops) >= batch_size:
            flush()
            if not quiet and total % (batch_size * 2) == 0:
                print(f"[progress] processed={total} inserted~={inserted} modified~={modified} skipped={skipped}", file=sys.stderr)

    flush()

    if not quiet:
        print(f"[done] total={total} inserted~={inserted} modified~={modified} skipped={skipped} failed={failed}")

def main():
    p = argparse.ArgumentParser(description="Migrate JSON array of backup logs into MongoDB with BSON-safe coercions.")
    p.add_argument("json_path", help="Path to JSON file (top-level array).")
    p.add_argument("--mongo", default="mongodb://localhost:27017", help="MongoDB URI")
    p.add_argument("--db", default="codexscripta", help="Database name")
    p.add_argument("--coll", default="pc_backup_log", help="Collection name")
    p.add_argument("--batch", type=int, default=5000, help="Bulk upsert batch size")
    p.add_argument("--dry-run", action="store_true", help="Parse only; do not write")
    p.add_argument("-q", "--quiet", action="store_true", help="Less output")
    p.add_argument("--coerce-objectid", action="store_true", help="Convert 24-hex strings to ObjectId")
    p.add_argument("--coerce-isodate", action="store_true", help="Parse ISO-8601 strings to datetime")
    p.add_argument(
        "--unique-by",
        default="id,backup",
        help="Comma-separated fields for unique upsert key (e.g., 'id' or 'id,backup'). Set empty to disable."
    )
    args = p.parse_args()

    migrate(
        path=args.json_path,
        mongo_uri=args.mongo,
        db_name=args.db,
        coll_name=args.coll,
        batch_size=args.batch,
        dry_run=args.dry_run,
        quiet=args.quiet,
        coerce_objectid=args.coerce_objectid,
        coerce_isodate=args.coerce_isodate,
        unique_by=args.unique_by,
    )

if __name__ == "__main__":
    main()




'''




px migrate_backup_json_to_mongo.py fileBackup.json --mongo "mongodb://localhost:27017" --db widgets --coll fileBackup --batch 5000 --coerce-isodate



'''