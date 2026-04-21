import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
    _.switches.register( 'IP', '-ip', isData='name' )
    _.switches.register( 'JustResolve', '-r' )
    _.switches.register( 'Netblock', '-nb' )
    _.switches.register( 'Refresh', '-nc,-rr,-refresh' )
    _.switches.register( 'Ports', '-p,-port,-ports' )
    _.switches.register( 'StatusCodeHTTP', '-http,-www,-status' )
    _.switches.register( 'Prefix', '-pre,-prefix' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': '-ip.py',
    'description': 'Information about an IP Address',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p -ip -ip 8.8.8.8'),
                        _.hp('p -ip -r domain.com'),
                        _.hp('p -ip -ip 8.8.8.8 -p 53'),
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

import json
from typing import Iterable, Union, List, Any

JSONLike = Union[dict, list, str]

def extract_unique_by_key_substrings(
        data: JSONLike,
        keys: Iterable[str] = (
            "org", "organization", "company", "owner",
            "registrant", "as", "netname", "nethandle", "name"
        ),
        case_insensitive: bool = True,
        strip_whitespace: bool = True,
        min_len: int = 1
    ) -> List[str]:
    """
    Recursively traverse dict/list JSON-like input and return unique string values
    whose parent key *contains* any of the substrings in `keys`.

    Args:
        data: dict/list object, or a JSON string.
        keys: substrings to match in key names (substring match, not equality).
        case_insensitive: case-insensitive key matching if True.
        strip_whitespace: collapse internal whitespace and strip ends in collected values.
        min_len: minimum length after normalization.

    Returns:
        Ordered list of unique strings (first-seen preserved).
    """

    # Normalize input: if string, try to parse as JSON; if not JSON, treat as scalar and return []
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            # Not JSON; nothing to traverse
            return []

    # Prepare key matching
    needles = tuple(s.lower() for s in keys) if case_insensitive else tuple(keys)

    def key_matches(k: str) -> bool:
        hay = k.lower() if case_insensitive else k
        return any(sub in hay for sub in needles)

    # Normalize collected values
    def norm(s: str) -> str:
        return " ".join(s.split()) if strip_whitespace else s

    results: List[str] = []
    seen = set()

    def add_value(val: Any):
        if isinstance(val, str):
            v = norm(val)
            if len(v) >= min_len:
                key = v.lower()
                if key not in seen:
                    seen.add(key)
                    results.append(v)

    def collect_from_matched_value(v: Any):
        """
        When a matching key is found, collect:
        - If str: add directly.
        - If dict: look for inner keys that also match OR are 'name'-ish; still walk deeper.
        - If list/tuple/set: collect strings and inspect inner dicts/lists.
        """
        if isinstance(v, str):
            add_value(v)
        elif isinstance(v, dict):
            # Prefer inner 'name'-ish or matching keys
            for kk, vv in v.items():
                if isinstance(kk, str) and (key_matches(kk) or "name" in kk.lower()):
                    if isinstance(vv, str):
                        add_value(vv)
            walk(v)  # keep traversing deep
        elif isinstance(v, (list, tuple, set)):
            for item in v:
                if isinstance(item, str):
                    add_value(item)
                else:
                    collect_from_matched_value(item)

    def walk(node: Any):
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(k, str) and key_matches(k):
                    collect_from_matched_value(v)
                # Always traverse deeper
                walk(v)
        elif isinstance(node, (list, tuple, set)):
            for item in node:
                walk(item)
        # Scalars are terminal

    walk(data)
    return results

def get_ip(hostname):
    import socket
    return socket.gethostbyname(hostname)


import socket

def ping_port(host, port, timeout=3):
    """
    Try to connect to a host:port using TCP.

    Returns True if open, False otherwise.
    """
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


import requests

def get_status_code(url: str) -> int:
    """
    Send a HEAD request to the given URL and return the HTTP status code.

    Args:
        url (str): The URL to check.

    Returns:
        int: The HTTP status code (e.g., 200, 404, 500).
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code
    except requests.RequestException:
        return None  # or return something like 0 or -1 if you prefer



def action():
    prefix = ''
    if _.switches.isActive('Prefix'):
        prefix = _.switches.value('Prefix')
    if _.switches.isActive('StatusCodeHTTP'):
        # print(_.isData(2))
        if len(_.switches.values('StatusCodeHTTP')):
            urls = _.switches.values('StatusCodeHTTP')
        elif _.isData(2):
            urls = _.isData(2)
        else:
            urls = []
        codes = {}
        statuses = {}
        for dat in urls:
            if not len(dat.strip()): continue
            dat = dat.strip()
            if prefix:
                dat = prefix + dat
            url = False
            for part in dat.split():
                if 'http' in part:
                    url = part
                    break
            if not url:
                continue


            url = url.strip()
            if not len(url): continue
            # if not url.startswith('http'): url = 'http://' + url
            if not url.startswith('http'): continue
            # print(url)
            status = get_status_code(url)
            if status is None:
                status = 0
            if status is not None:
                statuses[url] = status
            if not status in codes:
                codes[status] = []
            codes[status].append(url)
        for status in sorted(codes.keys()):
            _.pr(f"{status}", c='yellow')
            for url in codes[status]:
                if status >= 200 and status < 400:
                    _.pr(f"    {url}", c='green')
                else:
                    _.pr(f"    {url}", c='red')
        return None

    # 22  25  443  2077  2078  2079  2080  993  2082  2083  995  2086  2087  3306  2091  587  5355  110  143  111  80  465 2222

    if _.switches.isActive('Ports'):
        for fqdn in _.switches.values('IP'):
            fqdn = fqdn.strip()
            _.pr()
            _.pr(fqdn, c='yellow')
            for port in _.switches.values('Ports'):
                port = int(port)
                res = ping_port(fqdn, port)
                if res:
                    _.pr(f"{res} {port}",c='green')
                else:
                    _.pr(f"{res} {port}",c='red')
        return None


    if _.switches.isActive('JustResolve'):
        IPs = []
        if _.switches.values('JustResolve'):
            IPs = _.switches.values('JustResolve')
        if _.switches.values('IP'):
            IPs = _.switches.values('IP')
        
        for ip in IPs:
            _.pr(  get_ip(ip)  , c='yellow' )

        return None


    for ip in _.isData(2):
        _.pr(line=1, h=_.Pallet('sunrise','primary'))
        cacheGEO = _.getTable('-ip__geo.hash')
        api = _v.fig['WhoisXML']
        if _.switches.isActive('Netblock'):
            cacheNB = _.getTable('-ip__netblocks.hash')
            # import ipinfo
            _.pr(ip, c='yellow')
            # ipinfo.ip(ip)
            
            if ip in cacheNB and not _.switches.isActive('Refresh'):
                # _.pr('','- from cacheNB', c='cyan')
                netblock = cacheNB[ip]
            else:
                netblock = _.URL3(f'https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey={api}&ip={ip}')
            l = len(str(netblock))
            # _.pr(_.addComma(l), h=_.Pallet('cyberpunk','secondary'))
            if l > 30:
                try:
                    netblock = json.loads(netblock)
                except: pass
                cacheNB[ip] = netblock
                _.saveTable(cacheNB, '-ip__netblocks.hash',p=0)
            companies = extract_unique_by_key_substrings(netblock)
            if companies:
                _.pr('Associated Companies/Organizations:', h=_.Pallet('cyberpunk','primary'))
                for company in companies:
                    _.pr(f'- {company}', h=_.Pallet('sandbar','primary'))
            
            _.pr()
            _.pr()
            _.pr()
        if ip in cacheGEO and not _.switches.isActive('Refresh'):
            # _.pr('','- from cacheGEO', c='cyan')
            geo = cacheGEO[ip]
        else:
            geo = _.URL3(f'https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={api}&ipAddress={ip}')
        l = len(str(geo))
        # _.pr(_.addComma(l), h=_.Pallet('cyberpunk','secondary'))
        if l > 15:
            try:
                geo = json.loads(geo)
            except: pass
            cacheGEO[ip] = geo
            _.saveTable(cacheGEO, '-ip__geo.hash',p=0)
            _.pr('Info & Location:', h=_.Pallet('cyberpunk','primary'))
            
            _.ymlColor( geo )
        # _.pr(netblock)
        

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)