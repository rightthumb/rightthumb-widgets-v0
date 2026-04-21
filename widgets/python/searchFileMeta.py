import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    # ---- Database ----
    _.switches.register('DB', '-db', group='Database')

    # ---- Core search ----
    _.switches.register('Search', '-search', group='Search')
    _.switches.register('Omit', '-omit', group='Search')
    _.switches.register('Regex', '-regex', group='Search')

    # ---- Filters ----
    _.switches.register('Ext', '-ext', group='Filters')
    _.switches.register('NotExt', '-notext', group='Filters')
    _.switches.register('Mime', '-mime', group='Filters')
    _.switches.register('InPath', '-inpath', group='Filters')
    _.switches.register('InPathRe', '-inpathre', group='Filters')

    _.switches.register('MinBytes', '-minbytes', group='Filters')
    _.switches.register('MaxBytes', '-maxbytes', group='Filters')
    _.switches.register('MinLen', '-minlen', group='Filters')
    _.switches.register('MaxLen', '-maxlen', group='Filters')

    _.switches.register('AfterMtime', '-aftermtime', group='Filters')
    _.switches.register('BeforeMtime', '-beforemtime', group='Filters')

    _.switches.register('MissingEXIF', '-missingexif', group='Filters')
    _.switches.register('MissingOnDisk', '-missingondisk', group='Filters')

    # ---- Duplicates ----
    _.switches.register('Duplicates', '-duplicates', group='Duplicates')
    _.switches.register('DupThreshold', '-dupthreshold', group='Duplicates')
    _.switches.register('Hash', '-hash', group='Duplicates')

    # ---- Grouping & reporting ----
    _.switches.register('GroupBy', '-groupby', group='Reporting')
    _.switches.register('Top', '-top', group='Reporting')

    # ---- Sorting & projection ----
    _.switches.register('SortBy', '-sortby', group='Output')
    _.switches.register('Fields', '-fields', group='Output')
    _.switches.register('Limit', '-limit', group='Output')

    # ---- Output ----
    _.switches.register('Output', '-output', group='Output')

_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'relatedapps': [],
    'prerequisite': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start






#!/usr/bin/env python3
# meta_search_unqlite.py
# Search/report over metadata saved by meta_to_unqlite.py
# Outputs TSV or JSONL. Designed for RightThumb _.switches (no argparse).
# Indentation = 4 spaces

import os, sys, json, re, time, hashlib
from datetime import datetime, timezone

# ---------- Optional UnQLite ----------
try:
    from unqlite import UnQLite
except Exception:
    UnQLite = None

# ---------- RightThumb shims (so file can import without crashing) ----------
try:
    import _rightThumb._base3 as _
except Exception:
    class _ShimSwitches:
        def isActive(self, name): return False
        def values(self, name): return []
    class _Shim:
        switches = _ShimSwitches()
        def pr(*a, **k): print(*a, **k)
    _ = _Shim()  # minimal shim; you will use the real one

# ---------- Utilities ----------
def iso(ts: float | int | None):
    if ts is None: return None
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat().replace('+00:00','Z')
    except Exception:
        return None

def get_in(d: dict, dotted: str, default=None):
    cur = d
    for part in dotted.split('.'):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur

def set_default(obj: dict, dotted: str, val):
    parts = dotted.split('.')
    cur = obj
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = val

def as_float(x, default=None):
    try:
        return float(x)
    except Exception:
        return default

def as_int(x, default=None):
    try:
        return int(float(x))
    except Exception:
        return default

def file_exists(path: str) -> bool:
    try:
        return os.path.isfile(path)
    except Exception:
        return False

def human_bytes(n: int | float | None):
    if n is None: return ''
    n = float(n)
    units = ['B','KB','MB','GB','TB','PB']
    i = 0
    while n >= 1024 and i < len(units)-1:
        n /= 1024.0
        i += 1
    return f"{n:.2f} {units[i]}"

# ---------- DB helpers ----------
class MetaDB:
    def __init__(self, db_path: str):
        if UnQLite is None:
            raise RuntimeError("unqlite module not installed. pip install unqlite")
        self.db = UnQLite(db_path)

    def iter_files(self):
        # Keys are "file:<path>"
        for k, v in self.db:
            if isinstance(k, bytes): k = k.decode('utf-8','ignore')
            if not k.startswith('file:'): continue
            try:
                if isinstance(v, bytes): v = v.decode('utf-8','ignore')
                doc = json.loads(v)
                yield doc
            except Exception:
                continue

    def get_by_hash(self, algo: str, hexdig: str):
        try:
            k = f"index:hash:{hexdig}"
            raw = self.db[k]
            arr = json.loads(raw.decode('utf-8') if isinstance(raw, bytes) else raw)
            docs = []
            for key in arr:
                try:
                    val = self.db[key]
                    docs.append(json.loads(val.decode('utf-8') if isinstance(val, bytes) else val))
                except Exception:
                    pass
            return docs
        except Exception:
            return []

# ---------- Duplicate detection ----------
def quick_sample_hash(path: str, sample_bytes: int = 1024*1024) -> str | None:
    """Hash first+last sample_bytes to reduce false positives for large files."""
    try:
        size = os.path.getsize(path)
        h = hashlib.sha256()
        with open(path, 'rb') as f:
            h.update(f.read(min(sample_bytes, size)))
            if size > sample_bytes:
                f.seek(max(0, size - sample_bytes))
                h.update(f.read(sample_bytes))
        return h.hexdigest()
    except Exception:
        return None

def find_duplicates(records, threshold_bytes: int = 256 * 1024 * 1024, algo: str = 'sha256'):
    """
    If file size <= threshold, use full hash field if present (collector) or compute.
    If > threshold, group by byte-size and confirm with quick sample hash to avoid huge reads.
    Returns list of groups; each group is list of docs with same content.
    """
    # Pre-bucket by size
    by_size = {}
    for doc in records:
        size = get_in(doc, 'fs.size')
        path = doc.get('path')
        if size is None or not path: continue
        by_size.setdefault(size, []).append(doc)

    groups = []
    for size, bucket in by_size.items():
        if len(bucket) < 2:  # cannot be duplicates
            continue

        # Small/medium files: prefer full content hash if we have it
        if size <= threshold_bytes:
            by_hash = {}
            for doc in bucket:
                h = get_in(doc, 'hash.sha256') or get_in(doc, 'hash.sha1') or get_in(doc, 'hash.md5')
                # If no stored hash, compute sha256 now
                if not h and os.path.isfile(doc.get('path','')):
                    h = quick_sample_hash(doc['path'], sample_bytes=max(1024*1024, int(size)))  # full for small files
                if not h: 
                    continue
                by_hash.setdefault(h, []).append(doc)
            for h, grp in by_hash.items():
                if len(grp) > 1:
                    groups.append(grp)
        else:
            # Large files: size-bucket then sample-hash (first/last 1MB)
            by_smpl = {}
            for doc in bucket:
                p = doc.get('path')
                if not p or not os.path.isfile(p): 
                    continue
                smpl = quick_sample_hash(p, sample_bytes=1024*1024)
                if not smpl: 
                    continue
                key = f"{size}:{smpl}"
                by_smpl.setdefault(key, []).append(doc)
            for key, grp in by_smpl.items():
                if len(grp) > 1:
                    groups.append(grp)

    return groups

# ---------- Filtering / Sorting / Grouping ----------
def match_search(doc: dict, needles: list[str], omits: list[str]) -> bool:
    """Case-insensitive substring search across flattened text fields plus path/name."""
    if not needles and not omits:
        return True
    hay = []
    # Core text fields
    for k in ['path', 'name', 'parent', 'type.ext', 'type.mime_guess']:
        v = get_in(doc, k)
        if isinstance(v, str): hay.append(v.lower())
    # Some metadata areas
    for k in ['pdf.Title', 'pdf.Author', 'office.title', 'office.description', 'image.exiftool.Model', 'image.exiftool.Make']:
        v = get_in(doc, k)
        if isinstance(v, str): hay.append(v.lower())
    blob = ' | '.join(hay)

    for n in needles:
        n = n.lower()
        if n not in blob:
            return False
    for o in omits:
        o = o.lower()
        if o in blob:
            return False
    return True

def match_regex(doc: dict, patterns: list[str]) -> bool:
    if not patterns: return True
    txt = json.dumps(doc, ensure_ascii=False)
    for pat in patterns:
        try:
            if not re.search(pat, txt, flags=re.IGNORECASE|re.MULTILINE):
                return False
        except Exception:
            return False
    return True

def filter_records(records, action):
    res = []
    exts = set([e.lower().lstrip('.') for e in action.get('ext', []) if e])
    not_exts = set([e.lower().lstrip('.') for e in action.get('notExt', []) if e])
    mimes = set([m.lower() for m in action.get('mime', []) if m])
    minB = as_int(action.get('minBytes'))
    maxB = as_int(action.get('maxBytes'))
    minLen = as_float(action.get('minLengthSec'))
    maxLen = as_float(action.get('maxLengthSec'))
    must_missing_exif = bool(action.get('missingEXIF'))
    must_missing_ondisk = bool(action.get('missingOnDisk'))
    path_contains = [s.lower() for s in action.get('pathContains', [])]
    path_regex = action.get('pathRegex', [])
    after_mtime = as_float(action.get('afterMtime'))
    before_mtime = as_float(action.get('beforeMtime'))

    for doc in records:
        path = doc.get('path','')
        ext = (get_in(doc,'type.ext') or '').lower()
        mime = (get_in(doc,'type.mime_guess') or '').lower()
        size = get_in(doc,'fs.size')
        mtime = get_in(doc,'fs.mtime')
        av_len = get_in(doc,'av_tags._length_seconds')

        # ext/mime includes/excludes
        if exts and ext not in exts: continue
        if not_exts and ext in not_exts: continue
        if mimes and mime not in mimes: continue

        # bytes / length ranges
        if minB is not None and (size is None or size < minB): continue
        if maxB is not None and (size is None or size > maxB): continue
        if minLen is not None and (av_len is None or av_len < minLen): continue
        if maxLen is not None and (av_len is None or av_len > maxLen): continue

        # EXIF requirement
        if must_missing_exif:
            exif = get_in(doc, 'image.exiftool') or get_in(doc,'image.exif_pillow')
            if exif: 
                continue

        # On-disk requirement
        if must_missing_ondisk and file_exists(path):
            continue

        # Path filters
        path_lc = path.lower()
        if path_contains:
            ok = True
            for s in path_contains:
                if s not in path_lc:
                    ok = False; break
            if not ok: continue
        if path_regex:
            try:
                ok = all([re.search(p, path, flags=re.IGNORECASE) for p in path_regex])
            except Exception:
                ok = False
            if not ok: continue

        # mtime range
        if after_mtime is not None and (mtime is None or mtime < after_mtime): continue
        if before_mtime is not None and (mtime is None or mtime > before_mtime): continue

        # Text search / omit
        if not match_search(doc, action.get('searchFor', []), action.get('searchForOmit', [])):
            continue

        # Regex over entire doc json
        if not match_regex(doc, action.get('regex', [])):
            continue

        res.append(doc)
    return res

def sort_records(records, sort_fields):
    def keyer(doc):
        keys = []
        for fld in sort_fields:
            order = 1
            f = fld
            if f.startswith('a.'):
                f = f[2:]
            elif f.startswith('d.'):
                f = f[2:]
                order = -1
            val = get_in(doc, f)
            # normalize types for sorting
            if isinstance(val, str):
                keys.append((order, ('S', val.lower())))
            elif isinstance(val, (int,float)):
                keys.append((order, ('N', val)))
            elif val is None:
                keys.append((order, ('Z', None)))
            else:
                keys.append((order, ('O', str(val))))
        return tuple([(o, v) for o, v in keys])

    # Python can't see order without custom; we invert numeric if order=-1 at compare time:
    # Easier: sort many times in reverse order of fields.
    data = list(records)
    # Stable sort: process from last to first
    for fld in reversed(sort_fields or []):
        rev = False
        f = fld
        if f.startswith('d.'):
            rev = True
            f = f[2:]
        elif f.startswith('a.'):
            f = f[2:]
        data.sort(key=lambda d: get_in(d, f), reverse=rev)
    return data

def group_counts(records, fields):
    """Return list of {group: {field:value...}, count, bytes} sorted by count desc."""
    buckets = {}
    for doc in records:
        key = tuple([get_in(doc, f) for f in fields])
        if key not in buckets:
            buckets[key] = {"group": dict(zip(fields, key)), "count": 0, "bytes": 0}
        buckets[key]["count"] += 1
        sz = get_in(doc,'fs.size') or 0
        buckets[key]["bytes"] += sz
    out = list(buckets.values())
    out.sort(key=lambda x: (x["count"], x["bytes"]), reverse=True)
    return out

# ---------- Output helpers ----------
def print_jsonl(records):
    for doc in records:
        sys.stdout.write(json.dumps(doc, ensure_ascii=False) + "\n")

def print_tsv(records, fields):
    # Resolve dotted fields and print TSV
    fields = fields or ['path','type.ext','type.mime_guess','fs.size','fs.mtime_iso']
    sys.stdout.write("\t".join(fields) + "\n")
    for d in records:
        vals = []
        for f in fields:
            v = get_in(d, f)
            if f.endswith('.size') or f == 'fs.size':
                # add human size as convenience, keep number in cell
                vals.append(str(v if v is not None else ''))
            elif f.endswith('.mtime') or f == 'fs.mtime':
                vals.append(str(v if v is not None else ''))
            else:
                if isinstance(v, (dict, list)):
                    vals.append(json.dumps(v, ensure_ascii=False))
                else:
                    vals.append('' if v is None else str(v))
        sys.stdout.write("\t".join(vals) + "\n")

def print_duplicate_groups(groups):
    for i, grp in enumerate(groups, 1):
        print(f"# DUPLICATE GROUP {i} (n={len(grp)}, size={human_bytes(get_in(grp[0],'fs.size'))})")
        for doc in grp:
            print("  ", doc.get('path'))
        print()

# ---------- Public entry point ----------
def run(action: dict):
    """
    action: dict of switches/values from your framework (see usage()).
    Required: action['db'] — path to UnQLite db
    """
    db_path = action.get('db') or 'meta.unqlite'
    if not os.path.isfile(db_path):
        print(f"[error] DB not found: {db_path}", file=sys.stderr)
        return

    # Load all docs (filter down afterward)
    db = MetaDB(db_path)
    records = list(db.iter_files())

    # Optional basic filters/search
    records = filter_records(records, action)

    # Duplicates
    if action.get('find_duplicates'):
        thr = as_int(action.get('dupThresholdBytes'), 256 * 1024 * 1024)
        algo = (action.get('hashAlgo') or 'sha256').lower()
        groups = find_duplicates(records, threshold_bytes=thr, algo=algo)
        if action.get('output') == 'json':
            # output as json array of groups (each group is list of docs)
            sys.stdout.write(json.dumps(groups, ensure_ascii=False) + "\n")
        else:
            print_duplicate_groups(groups)
        return  # duplicates is terminal

    # Group counts
    if action.get('groupBy'):
        counts = group_counts(records, action['groupBy'])
        if action.get('output') == 'json':
            sys.stdout.write(json.dumps(counts, ensure_ascii=False) + "\n")
        else:
            # TSV by default for groups
            sys.stdout.write("count\tbytes\t" + "\t".join(action['groupBy']) + "\n")
            for row in counts[: as_int(action.get('topN'), 1000000) ]:
                sys.stdout.write(f"{row['count']}\t{row['bytes']}\t" + "\t".join([str(row['group'].get(f,'')) for f in action['groupBy']]) + "\n")
        return

    # Sorting
    sort_fields = action.get('sortByField') or []
    if sort_fields:
        records = sort_records(records, sort_fields)

    # Limit & projection
    limit = as_int(action.get('limit'))
    if limit is not None and limit >= 0:
        records = records[:limit]

    fields = action.get('fields')
    if fields:
        # project to requested fields
        proj = []
        for d in records:
            row = {}
            for f in fields:
                set_default(row, f, get_in(d, f))
            proj.append(row)
        records = proj

    # Output
    outfmt = (action.get('output') or 'tsv').lower()
    if outfmt == 'json':
        print_jsonl(records)
    else:
        print_tsv(records, fields)

# ---------- usage() that builds your action dict ----------
def usage():
    """
    Build the 'action' dict driven by _.switches (RightThumb).
    Extend this mapping to your exact switch names; defaults provided for safety.
    """
    action = {}

    # Required DB
    action['db'] = ( _.switches.values('DB')[0] if _.switches.isActive('DB') else 'meta.unqlite' )

    # Core search
    action['search'] = _.switches.isActive('Search')
    action['searchFor'] = _.switches.values('Search') if action['search'] else []
    action['searchForOmit'] = _.switches.values('Omit') if _.switches.isActive('Omit') else []
    action['regex'] = _.switches.values('Regex') if _.switches.isActive('Regex') else []

    # Filters
    action['ext'] = _.switches.values('Ext') if _.switches.isActive('Ext') else []
    action['notExt'] = _.switches.values('NotExt') if _.switches.isActive('NotExt') else []
    action['mime'] = _.switches.values('Mime') if _.switches.isActive('Mime') else []
    action['pathContains'] = _.switches.values('InPath') if _.switches.isActive('InPath') else []
    action['pathRegex'] = _.switches.values('InPathRe') if _.switches.isActive('InPathRe') else []
    action['minBytes'] = ( _.switches.values('MinBytes')[0] if _.switches.isActive('MinBytes') else None )
    action['maxBytes'] = ( _.switches.values('MaxBytes')[0] if _.switches.isActive('MaxBytes') else None )
    action['minLengthSec'] = ( _.switches.values('MinLen')[0] if _.switches.isActive('MinLen') else None )
    action['maxLengthSec'] = ( _.switches.values('MaxLen')[0] if _.switches.isActive('MaxLen') else None )
    action['afterMtime'] = ( _.switches.values('AfterMtime')[0] if _.switches.isActive('AfterMtime') else None )
    action['beforeMtime'] = ( _.switches.values('BeforeMtime')[0] if _.switches.isActive('BeforeMtime') else None )
    action['missingEXIF'] = _.switches.isActive('MissingEXIF')
    action['missingOnDisk'] = _.switches.isActive('MissingOnDisk')

    # Duplicates
    action['find_duplicates'] = _.switches.isActive('Duplicates')
    action['dupThresholdBytes'] = ( _.switches.values('DupThreshold')[0] if _.switches.isActive('DupThreshold') else 268435456 )  # 256 MiB default
    action['hashAlgo'] = ( _.switches.values('Hash')[0] if _.switches.isActive('Hash') else 'sha256' )

    # Grouping & reporting
    action['groupBy'] = _.switches.values('GroupBy') if _.switches.isActive('GroupBy') else []  # e.g., ['type.ext'] or ['type.mime_guess']
    action['topN'] = ( _.switches.values('Top')[0] if _.switches.isActive('Top') else None )

    # Sorting & projection
    # sortByField values: ['d.fs.size'] or ['a.fs.mtime','path']  (default ascending)
    action['sortByField'] = _.switches.values('SortBy') if _.switches.isActive('SortBy') else []
    action['fields'] = _.switches.values('Fields') if _.switches.isActive('Fields') else []
    action['limit'] = ( _.switches.values('Limit')[0] if _.switches.isActive('Limit') else None )

    # Output
    action['output'] = ( _.switches.values('Output')[0] if _.switches.isActive('Output') else 'tsv' )  # 'tsv' or 'json'

    # Now run the search with the built action map
    run(action)

# ---------- Main hook ----------
if __name__ == "__main__":
    # In your framework, you'll call usage() after your _.switches are parsed.
    # Here we just call usage() so the script does something by default.
    usage()










def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)