import time
from typing import Dict, Optional, Any, Iterable, Tuple, Union
import requests
from bs4 import BeautifulSoup

# -------------------------
# Agent profiles (extend me)
# -------------------------
AGENT_PROFILES: Dict[str, Dict[str, str]] = {
    "win11_chrome": {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/126.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    },
    "android_chrome": {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    },
    "ios_safari": {
        "User-Agent": (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    },
    "plain": {
        "User-Agent": "Python-requests",
    },
}

def fetch_advanced(
    url: str,
    *,
    method: Optional[str] = None,                 # "GET", "POST", "PUT", ...
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Union[Dict[str, Any], str]] = None,   # form-encoded or raw
    json: Optional[Any] = None,                   # JSON body
    headers: Optional[Dict[str, str]] = None,     # extra/override headers
    agent: str = "win11_chrome",                  # key in AGENT_PROFILES
    profiles: Optional[Dict[str, Dict[str, str]]] = None,
    timeout: float = 20.0,
    retries: int = 2,                             # total attempts = retries+1
    backoff: float = 0.75,                        # seconds * attempt_index
    retry_on: Iterable[int] = (429, 500, 502, 503, 504),
    allow_redirects: bool = True,
    verify: bool = True,                          # TLS verify
    proxies: Optional[Dict[str, str]] = None,
    cookies: Optional[Dict[str, str]] = None,
    return_type: str = "auto",                    # "auto"|"text"|"json"|"bytes"
    text_mode: str = "html",                      # when returning text: "html"|"plain"
    encoding: Optional[str] = None,               # force decode encoding
) -> Union[str, bytes, Any, Tuple[int, str]]:
    """
    Advanced HTTP fetch with agent profiles, retries, and flexible response parsing.

    - method defaults to POST if (data or json) is provided, else GET.
    - return_type:
        * "auto": JSON if content-type JSON; else text (HTML parsed or plain).
        * "text": always text (BeautifulSoup if text_mode='html').
        * "json": parse JSON (raises on failure).
        * "bytes": raw bytes.
    - On HTTP error after final retry, raises for_status() with the last response.
    """

    profiles = profiles or AGENT_PROFILES
    base_headers = dict(profiles.get(agent, {}))
    if headers:
        base_headers.update(headers)

    # Pick method
    if method is None:
        method = "POST" if (data is not None or json is not None) else "GET"
    method = method.upper()

    session = requests.Session()

    last_exc = None
    for attempt in range(retries + 1):
        try:
            resp = session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                headers=base_headers,
                timeout=timeout,
                allow_redirects=allow_redirects,
                verify=verify,
                proxies=proxies,
                cookies=cookies,
            )

            # Retry on specific status codes
            if resp.status_code in retry_on and attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue

            # Raise if 4xx/5xx and no more retries
            resp.raise_for_status()

            # Force encoding if requested
            if encoding:
                resp.encoding = encoding

            ctype = resp.headers.get("Content-Type", "").lower()

            # Decide return
            if return_type == "bytes":
                return resp.content

            if return_type == "json":
                return resp.json()

            if return_type == "text":
                text = resp.text
                if text_mode == "html":
                    soup = BeautifulSoup(text, "html.parser")
                    return soup.get_text(separator="\n", strip=True)
                return text

            # return_type == "auto"
            if "application/json" in ctype:
                return resp.json()
            else:
                text = resp.text
                if text_mode == "html":
                    soup = BeautifulSoup(text, "html.parser")
                    return soup.get_text(separator="\n", strip=True)
                return text

        except requests.RequestException as e:
            last_exc = e
            # If we can retry, backoff and continue
            if attempt < retries:
                time.sleep(backoff * (attempt + 1))
                continue
            # After final attempt, re-raise
            raise

    # Should never hit here; included for clarity
    if last_exc:
        raise last_exc


