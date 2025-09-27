import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','HAR file path',  description='Files', isRequired=False )

    _.switches.register('url', '-url', 'Exact URL to fetch cached body for (repeatable)', isData='name' )
    _.switches.register('contains', '-contains', 'Substring filter for URLs (repeatable)')
    _.switches.register('re', '-re', 'Regex filter for URLs')
    _.switches.register('domain', '-domain', 'Only URLs whose netloc ends with this')
    _.switches.register('status', '-status', 'HTTP status code(s), comma delimited')
    _.switches.register('method', '-method', 'HTTP method(s), comma delimited (GET,POST,...)')
    _.switches.register('mime', '-mime', 'MIME startswith filter(s), comma delimited (e.g. text/, application/json)')
    _.switches.register('list', '-list', 'List matching URLs only')
    _.switches.register('unique', '-unique', 'De-duplicate URLs')
    _.switches.register('headers', '-headers', 'Print request & response headers')
    _.switches.register('cookies', '-cookies', 'Print request & response cookies')
    _.switches.register('query', '-query', 'Print URL query params')
    _.switches.register('post', '-post', 'Print postData (if present)')
    _.switches.register('body', '-body', 'Print response body for matches')
    _.switches.register('dump', '-dump', 'Dump response bodies to folder')
    _.switches.register('search', '-search', 'Search substring inside decoded body (repeatable)')
    _.switches.register('since', '-since', 'ISO timestamp lower bound (e.g. 2025-09-16T00:00:00)')
    _.switches.register('until', '-until', 'ISO timestamp upper bound (exclusive)')
    _.switches.register('force-latin1', '-force-latin1', 'Force latin-1 decode if JSON fails')
    _.switches.register('max', '-max', 'Limit number of results')


_._default_settings_()

_.appInfo[focus()] = {
    'file': 'harTool.py',
    'description': 'List urls or specify a url and view the cached data',
    'categories': [
                        'har',
                        'web',
                        'browser',
                        'research',
                ],
    'examples': [
                        _.hp('p harTool '),
                        _.hp('p harTool -url https://etc.ac/'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
    ],
    'aliases': [],
    'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
    _._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


# import json

# def load_har_file(file_path):
#     with open(file_path, 'r') as f:
#         return json.load(f)

# def extract_urls(har_data):
#     urls = []
#     for entry in har_data['log']['entries']:
#         urls.append(entry['request']['url'])
#     return urls

# def get_cache_by_url(har_data, search_url):
#     for entry in har_data['log']['entries']:
#         request_url = entry['request']['url']
#         if request_url == search_url:
#             if 'response' in entry and 'content' in entry['response']:
#                 return entry['response']['content']['text'].replace('\r','').replace(chr(10), '\n').replace(chr(27), '')
#             else:
#                 return "No cached data found for this URL."
#     return "URL not found in HAR file."

# def main(har_file, search_url=None):
#     har_data = load_har_file(har_file)
#     if search_url:
#         cached_data = get_cache_by_url(har_data, search_url)
#         # _.pr(f"Cached data for {search_url}:")
#         _.pr(cached_data)
#     else:
#         urls = extract_urls(har_data)
#         # print("List of URLs in the HAR file:")
#         for url in urls:
#             if _.showLine(url):
#                 _.pr(url)


# def run(file,url=None,urls=[]):
#     # print(file,url); return file
#     har_file_path = file
#     search_url = None
#     if url:
#         search_url = url
#     if url and len(urls) > 1:
#         _.pr(line=1,c='yellow')
#         _.pr(url,c='cyan')
#         _.pr()
#     main(har_file_path, search_url)

# def action():
#     if not _.switches.isActive('Files'):
#         _.e('No files specified')
#     else:
#         file = _.switches.values('Files')[0]
#     urls = _.isData()
#     # print(urls); return urls
#     if not urls:
#         run(file)
#     else:
#         for url in urls:
#             run(file,url.strip(),urls)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
harTool.py — robust HAR inspector

Examples:
  p harTool -f www.fiverr.com.har
  p harTool -f www.fiverr.com.har -url https://www.fiverr.com/
  p harTool -f site.har -contains /search -status 200 -body
  p harTool -f site.har -re "api/v1/.*" -method POST -post
  p harTool -f site.har -domain fiverr.com -dump ./har_dump
  p harTool -f site.har -mime text/html -search "checkout"
"""

import sys, os, re, json, base64, datetime

# ── Optional RightThumb helpers (safe fallbacks if not present) ───────────────
try:
    _
except NameError:
    class _Shim:
        class switchesShim:
            def __init__(self):
                self._vals = {}
            def register(self, *args, **kwargs): pass
            def isActive(self, name): return name in self._vals
            def value(self, name, default=None):
                v = self._vals.get(name)
                if v is None: return default
                if isinstance(v, list): return v[0] if v else default
                return v
            def values(self, name):
                v = self._vals.get(name)
                if v is None: return []
                return v if isinstance(v, list) else [v]
            def process(self, argv):
                # Minimal parser: -flag value OR -flag
                i = 0
                while i < len(argv):
                    a = argv[i]
                    if a.startswith('-'):
                        key = a.lstrip('-')
                        if i+1 < len(argv) and not argv[i+1].startswith('-'):
                            self._vals.setdefault(key, []).append(argv[i+1])
                            i += 2
                        else:
                            self._vals[key] = True
                            i += 1
                    else:
                        i += 1
        def __init__(self):
            self.switches = _Shim.switchesShim()
        def pr(self, *args, c=None, p=0, line=0, **kwargs):
            if line: print('-' * 60)
            print(*args)
        def e(self, *args):
            print('[error]', *args, file=sys.stderr)
        def showLine(self, text):
            return True
        def isData(self):
            return None
        def isExit(self, *_): pass
    _ = _Shim()


# ── Utilities ────────────────────────────────────────────────────────────────
def parse_iso(ts):
    # HAR startedDateTime looks like "2025-09-18T16:05:12.123Z"
    try:
        return datetime.datetime.fromisoformat(ts.replace('Z','+00:00'))
    except Exception:
        return None

def try_load_json_bytes(b, force_latin1=False):
    tried = []
    for enc in (['utf-8','utf-8-sig','utf-16'] + (['latin-1'] if force_latin1 else ['cp1252','latin-1'])):
        try:
            return json.loads(b.decode(enc))
        except Exception as e:
            tried.append(f'{enc}: {e.__class__.__name__}')
    raise UnicodeDecodeError('harTool', b, 0, 0, 'Could not decode JSON. Tried -> ' + ' | '.join(tried))

def load_har_file(file_path, force_latin1=False):
    with open(file_path, 'rb') as f:
        data = f.read()
    return try_load_json_bytes(data, force_latin1=force_latin1)

def entry_matches(entry, flt):
    req = entry.get('request', {})
    res = entry.get('response', {})
    url = req.get('url','')
    method = req.get('method','')
    status = res.get('status', None)
    mime = (res.get('content') or {}).get('mimeType','') or ''
    t0 = entry.get('startedDateTime')
    t0dt = parse_iso(t0) if t0 else None

    # URL filters
    if flt['urls'] and url not in flt['urls']:
        return False
    if flt['contains'] and not any(sub in url for sub in flt['contains']):
        return False
    if flt['regex'] and not flt['regex'].search(url):
        return False
    if flt['domain']:
        try:
            from urllib.parse import urlparse
            host = urlparse(url).netloc.split('@')[-1].split(':')[0]
            if not (host == flt['domain'] or host.endswith('.' + flt['domain'])):
                return False
        except Exception:
            return False

    # Method
    if flt['methods'] and method.upper() not in flt['methods']:
        return False

    # Status
    if flt['statuses'] and (status is None or str(status) not in flt['statuses']):
        return False

    # MIME
    if flt['mimes']:
        ok = False
        for m in flt['mimes']:
            if mime.startswith(m):
                ok = True
                break
        if not ok:
            return False

    # Time range
    if flt['since'] and (not t0dt or t0dt < flt['since']):
        return False
    if flt['until'] and (not t0dt or t0dt >= flt['until']):
        return False

    return True

def decode_body(entry):
    res = entry.get('response', {})
    content = res.get('content') or {}
    text = content.get('text')
    if text is None:
        return None, False, 'No content.text captured (network pane may not have "Preserve log" or body capture).'
    enc = content.get('encoding')
    if enc == 'base64':
        try:
            raw = base64.b64decode(text)
            try:
                return raw.decode('utf-8', errors='replace'), True, None
            except Exception:
                # Return binary-ish as latin-1 to keep bytes printable
                return raw.decode('latin-1', errors='replace'), True, None
        except Exception as e:
            return None, False, f'Base64 decode failed: {e}'
    # Plain text
    return (text.replace('\r', '').replace('\x1b','')), False, None

def print_headers(entry):
    def to_dict(lst):
        d = {}
        for h in lst or []:
            n = h.get('name'); v = h.get('value')
            if n is None: continue
            d.setdefault(n, []).append(v)
        return d
    req = entry.get('request', {})
    res = entry.get('response', {})
    _.pr('> Request headers:', p=0)
    for k, vals in to_dict(req.get('headers')).items():
        _.pr(f'  {k}: {", ".join(vals)}')
    _.pr('< Response headers:', p=0)
    for k, vals in to_dict(res.get('headers')).items():
        _.pr(f'  {k}: {", ".join(vals)}')

def print_cookies(entry):
    req = entry.get('request', {})
    res = entry.get('response', {})
    if req.get('cookies'):
        _.pr('> Request cookies:', p=0)
        for c in req['cookies']:
            _.pr('  ' + '; '.join([f'{k}={c.get(k)}' for k in ('name','value','domain','path','expires','httpOnly','secure','sameSite') if c.get(k) is not None]))
    if res.get('cookies'):
        _.pr('< Response cookies:', p=0)
        for c in res['cookies']:
            _.pr('  ' + '; '.join([f'{k}={c.get(k)}' for k in ('name','value','domain','path','expires','httpOnly','secure','sameSite') if c.get(k) is not None]))

def print_query(entry):
    req = entry.get('request', {})
    qp = req.get('queryString') or []
    if qp:
        _.pr('? Query params:', p=0)
        for kv in qp:
            _.pr(f"  {kv.get('name')} = {kv.get('value')}")

def print_post(entry):
    req = entry.get('request', {})
    pd = req.get('postData')
    if not pd:
        _.pr('(no postData)', p=0); return
    mime = pd.get('mimeType','')
    _.pr(f'POST mimeType: {mime}', p=0)
    if pd.get('params'):
        _.pr('POST params:', p=0)
        for kv in pd['params']:
            _.pr(f"  {kv.get('name')} = {kv.get('value')}")
    if pd.get('text'):
        _.pr('POST raw text:', p=0)
        _.pr(pd['text'])

def dump_body(entry, dump_dir, idx):
    os.makedirs(dump_dir, exist_ok=True)
    req = entry.get('request', {})
    url = req.get('url','')
    res = entry.get('response', {})
    mime = (res.get('content') or {}).get('mimeType','') or 'application/octet-stream'
    body, is_b64, err = decode_body(entry)
    if body is None:
        return None, err
    # choose extension
    ext = 'txt'
    if mime.startswith('application/json'): ext = 'json'
    elif mime.startswith('text/html'): ext = 'html'
    elif mime.startswith('text/'): ext = 'txt'
    elif mime.startswith('image/'): ext = mime.split('/',1)[-1]
    safe_name = re.sub(r'[^A-Za-z0-9._-]+', '_', url)[:150]
    path = os.path.join(dump_dir, f'{idx:06d}_{ext}__{safe_name}.{ext}')
    try:
        with open(path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(body)
        return path, None
    except Exception as e:
        return None, str(e)

# ── Core logic ───────────────────────────────────────────────────────────────
def main(har_file, cli):
    force_latin1 = _.switches.isActive('force-latin1')
    har = load_har_file(har_file, force_latin1=force_latin1)

    entries = (har.get('log') or {}).get('entries') or []
    if not entries:
        _.e('No entries found in HAR'); return

    # Build filters
    contains = _.switches.values('contains') if _.switches.isActive('contains') else []
    regex = _.switches.value('re')
    regex = re.compile(regex) if regex else None
    domain = _.switches.value('domain')
    statuses = set(s.strip() for s in (_.switches.value('status','') or '').split(',') if s.strip())
    methods = set(m.strip().upper() for m in (_.switches.value('method','') or '').split(',') if m.strip())
    mimes = set(m.strip() for m in (_.switches.value('mime','') or '').split(',') if m.strip())
    urls_exact = _.switches.values('url') if _.switches.isActive('url') else []
    since = _.switches.value('since')
    until = _.switches.value('until')
    since_dt = None
    until_dt = None
    if since:
        try: since_dt = datetime.datetime.fromisoformat(since.replace('Z','+00:00'))
        except: _.e('Bad --since ISO format; ignoring')
    if until:
        try: until_dt = datetime.datetime.fromisoformat(until.replace('Z','+00:00'))
        except: _.e('Bad --until ISO format; ignoring')

    flt = {
        'contains': contains,
        'regex': regex,
        'domain': domain,
        'statuses': statuses,
        'methods': methods,
        'mimes': mimes,
        'urls': set(urls_exact),
        'since': since_dt,
        'until': until_dt,
    }

    flags = {
        'list_only': _.switches.isActive('list'),
        'unique': _.switches.isActive('unique'),
        'print_headers': _.switches.isActive('headers'),
        'print_cookies': _.switches.isActive('cookies'),
        'print_query': _.switches.isActive('query'),
        'print_post': _.switches.isActive('post'),
        'print_body': _.switches.isActive('body'),
        'dump_dir': _.switches.value('dump'),
        'search_terms': _.switches.values('search') if _.switches.isActive('search') else [],
        'max': int(_.switches.value('max', '0') or '0'),
    }

    seen = set()
    count = 0
    idx = 0

    for entry in entries:
        if not entry_matches(entry, flt):
            continue

        req = entry.get('request', {})
        res = entry.get('response', {})
        url = req.get('url','')

        if _.isData(2) and not url in _.isData(2):
            continue

        if flags['unique']:
            if url in seen: continue
            seen.add(url)

        idx += 1

        # Optional body/search pre-check (so we can filter by --search)
        body_text = None
        if flags['search_terms'] or flags['print_body'] or flags['dump_dir']:
            body_text, is_b64, err = decode_body(entry)
            if flags['search_terms']:
                if body_text is None:
                    continue
                found = any(term in body_text for term in flags['search_terms'])
                if not found:
                    continue
        

        # Output
        if flags['list_only']:
            if _.showLine(url):
                _.pr(url)
        else:
            if _.showLine(url):
                method = req.get('method','')
                status = res.get('status','')
                mime = (res.get('content') or {}).get('mimeType','') or ''
                t0 = entry.get('startedDateTime','')
                _.pr('-' * 60)
                _.pr(f'{method} {url}')
                _.pr(f'Status: {status} | MIME: {mime} | Time: {t0}')
                if flags['print_query']: print_query(entry)
                if flags['print_post']: print_post(entry)
                if flags['print_headers']: print_headers(entry)
                if flags['print_cookies']: print_cookies(entry)
                if flags['print_body']:
                    if body_text is None:
                        _.pr('(no body captured)')
                    else:
                        _.pr('')
                        _.pr(body_text)

        # Dump to files if requested
        if flags['dump_dir']:
            path, err = dump_body(entry, flags['dump_dir'], idx)
            if err:
                _.e(f'Dump failed: {err}')
            else:
                _.pr(f'[dumped] {path}')

        count += 1
        if flags['max'] and count >= flags['max']:
            break

def run(file, url=None, urls=[]):
    if url and len(urls) > 1:
        _.pr(line=1, c='yellow')
        _.pr(url, c='cyan')
        _.pr()
    # Push exact URL filter in switches if provided directly
    if url:
        _.switches._vals.setdefault('url', []).append(url)
    main(file, cli=True)

def action():
    if not _.switches.isActive('Files'):
        _.e('No files specified')
        return
    file = _.switches.values('Files')[0]
    urls = _.isData()
    if not urls:
        main(file, cli=True)
    else:
        for url in urls:
            run(file, url.strip(), urls)





########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__);