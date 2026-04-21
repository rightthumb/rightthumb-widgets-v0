import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Servers', '-ip,-ips,-server,-servers','fqdn.com' )
    _.switches.register( 'Websites', '-web,-site,-website','fqdn.com' )
    _.switches.register( 'WebsitesContents', '-has,-content','fqdn.com "text"' )
    _.switches.register( 'Continuous', '--c,-continuous,-loop' )
    _.switches.register( 'Notify', '-n,-notify' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'online.py',
    'description': 'Check if servers or websites are online',
    'categories': [
                        'networking',
                ],
    'examples': [
                        _.hp('p online -servers fqdn.com another.com 3.3.3.3 -web example.com another.com -has example.com "Welcome to Example" -continuous -notify'),
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



import subprocess
import platform

def is_host_alive(host: str, timeout: int = 4) -> bool:
    """
    Returns True if host responds to ping, otherwise False.
    Works with IPs and hostnames.
    """
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", str(timeout * 1000), host]
    else:
        cmd = ["ping", "-c", "1", "-W", str(timeout), host]

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False







import requests

def is_website_online(
    url: str,
    timeout: int = 5,
    follow_redirects: bool = True,
    session: requests.Session | None = None
) -> bool:
    """
    Returns True if the website responds with any valid HTTP status.
    Uses HEAD first (fast), falls back to GET if needed.
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    s = session or requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WebsiteOnlineCheck/1.0)"
    }

    try:
        # Try HEAD first
        r = s.head(
            url,
            timeout=timeout,
            allow_redirects=follow_redirects,
            headers=headers
        )

        # Common real-world failures for HEAD
        if r.status_code in (403, 405):
            r = s.get(
                url,
                timeout=timeout,
                allow_redirects=follow_redirects,
                headers=headers,
                stream=True
            )

        return 100 <= r.status_code < 600

    except requests.RequestException:
        return False








import requests # type: ignore


def page_contains_text(
    url: str,
    text: str,
    timeout: int = 5,
    case_sensitive: bool = False,
    follow_redirects: bool = True,
    session: requests.Session | None = None
) -> bool:
    """
    Returns True if the webpage (after redirects) contains the given text.
    """
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    s = session or requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; PageContainsText/1.0)"
    }

    try:
        r = s.get(
            url,
            timeout=timeout,
            allow_redirects=follow_redirects,
            headers=headers
        )
        r.raise_for_status()

        content = r.text
        needle = text

        if not case_sensitive:
            content = content.lower()
            needle = needle.lower()

        return needle in content

    except requests.RequestException:
        return False




import requests # type: ignore
from typing import List, Optional

def _header_safe(value: str) -> str:
    """
    Make a string safe for HTTP headers (latin-1).
    Replaces unsupported chars with '?'.
    """
    return value.encode("latin-1", "replace").decode("latin-1")

def send_ntfy(
    server: str,
    topic: str,
    message: str,
    title: Optional[str] = None,
    priority: int = 3,
    tags: Optional[List[str]] = None,
    timeout: int = 5
) -> bool:
    url = f"{server.rstrip('/')}/{topic}"

    headers = {"Priority": str(priority)}

    if title:
        headers["Title"] = _header_safe(title)   # <- prevents UnicodeEncodeError
    if tags:
        headers["Tags"] = _header_safe(",".join(tags))

    try:
        r = requests.post(url, data=message.encode("utf-8"), headers=headers, timeout=timeout)
        return r.ok
    except requests.RequestException:
        return False


def notify(srv: str, what: str) -> bool:
    if _.switches.isActive('Notify') is False:
        return False
    server = _v.fig.get("ntfy", _.switches.value('Notify'))
    if not server:
        return False
    # Keep headers clean; put emoji in the message where UTF-8 is fine.
    title = f"{what} OFFLINE"
    msg = f"🚨 {what} OFFLINE\n{srv}"

    return send_ntfy(
        server=server,
        topic="server-alerts",
        title=title,
        message=msg,
        priority=5,
        tags=["offline", what.lower()],
    )

import re

def _looks_like_host(token: str) -> bool:
    """
    True if token looks like a host/URL like:
    - example.com
    - https://example.com/path
    - 1.2.3.4
    """
    t = (token or "").strip()
    if not t:
        return False

    if re.match(r"^https?://", t, re.I):
        return True

    # IP
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", t):
        return True

    # hostname / domain (simple heuristic)
    # requires a dot and only safe chars
    if "." in t and re.match(r"^[A-Za-z0-9.-]+$", t):
        return True

    return False


def _ensure_url(host_or_url: str) -> str:
    s = host_or_url.strip()
    if re.match(r"^https?://", s, re.I):
        return s
    return "https://" + s


import requests

def _resolve_redirects(url: str, timeout: float = 8.0, session: requests.Session | None = None) -> str:
    """
    Return the final URL after following redirects.
    Uses HEAD first (cheaper), falls back to GET if needed.
    """
    s = session or requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WebsitesContents/1.0; +https://example.com)"
    }

    # Try HEAD first
    try:
        r = s.head(url, allow_redirects=True, timeout=timeout, headers=headers)
        # Some servers return 405/403 for HEAD or behave oddly; still may have .url.
        if r.url:
            return r.url
    except requests.RequestException:
        pass

    # Fallback to GET (stream=True to avoid downloading full body)
    try:
        r = s.get(url, allow_redirects=True, timeout=timeout, headers=headers, stream=True)
        if r.url:
            return r.url
    except requests.RequestException:
        pass

    # If anything fails, keep original
    return url


def parse_websites_contents(tokens, *, follow_redirects: bool = True, timeout: float = 8.0):
    """
    tokens: flat list like:
      [host, word, word, host, word, word, host, word]
    Returns list of (final_url, text)

    If follow_redirects is False, final_url is just _ensure_url(host).
    """
    toks = [str(x).strip() for x in tokens if str(x).strip()]
    out: list[tuple[str, str]] = []
    i = 0

    # reuse one session for speed / connection pooling
    session = requests.Session() if follow_redirects else None

    while i < len(toks):
        host = toks[i]
        if not _looks_like_host(host):
            i += 1
            continue

        i += 1
        text_parts = []
        while i < len(toks) and not _looks_like_host(toks[i]):
            text_parts.append(toks[i])
            i += 1

        text = " ".join(text_parts).strip()
        url = _ensure_url(host)

        if follow_redirects:
            url = _resolve_redirects(url, timeout=timeout, session=session)

        # preserve your "keep it so you can warn" behavior
        out.append((url, text if text else ""))

    return out


def check_with_retries(fn, retries: int):
    """
    Runs fn() up to `retries` times.
    Returns True immediately on first success.
    """
    for _ in range(retries):
        if fn():
            return True
    return False

def once():
    RETRIES = 3  # ← change this to 1, 5, 10, etc.

    # --------------------
    # Servers
    # --------------------
    if _.switches.isActive('Servers'):
        for srv in _.switches.values('Servers'):

            alive = check_with_retries(
                lambda: is_host_alive(srv),
                RETRIES
            )

            status = 'ONLINE' if alive else 'OFFLINE'
            color = 'green' if alive else 'red'
            _.pr(f'{srv}: {status}', c=color)

            if not alive:
                notify(srv, 'SERVER')

    # --------------------
    # Websites (online check)
    # --------------------
    if _.switches.isActive('Websites'):
        for web in _.switches.values('Websites'):

            online = check_with_retries(
                lambda: is_website_online(web),
                RETRIES
            )

            status = 'ONLINE' if online else 'OFFLINE'
            color = 'green' if online else 'red'
            _.pr(f'{web}: {status}', c=color)

            if not online:
                notify(web, 'WEBSITE')

    # --------------------
    # WebsitesContents
    # --------------------
    if _.switches.isActive('WebsitesContents'):
        tokens = _.switches.values('WebsitesContents')
        checks = parse_websites_contents(tokens)

        for web, text in checks:
            if not text:
                _.pr(f'Invalid input for WebsitesContents: {web} (missing text)', c='red')
                continue

            contains = check_with_retries(
                lambda: page_contains_text(web, text),
                RETRIES
            )

            status = 'FOUND' if contains else 'NOT FOUND'
            color = 'green' if contains else 'red'
            _.pr(f'"{text}" in {web}: {status}', c=color)

            if not contains:
                notify(web, 'CONTENT')


    

def action():
    if not _.switches.isActive('Continuous'):
        once()
        return
    elif _.switches.isActive('Continuous'):
        wait = 5
        if len(_.switches.value('Continuous')):
            wait = int(_.switches.value('Continuous'))
        import time
        cnt = 0
        try:
            while True:
                cnt += 1
                _.pr(f'\n\n--- Iteration {cnt} ---', c='cyan')
                once()
                time.sleep(wait)

        except KeyboardInterrupt:
            print("\nCtrl+C received — exiting cleanly.")



########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)