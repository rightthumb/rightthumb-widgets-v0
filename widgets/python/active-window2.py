import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Log', '-log' )
	_.switches.register( 'Stop', '-stop' )
	_.switches.register( 'Start', '-start' )
     

_._default_settings_()

_.appInfo[focus()] = {
    'file': 'active-window2.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p active-window -file file.txt'),
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
# -*- coding: utf-8 -*-

"""
Desktop tracker that mirrors the Chrome extension's behavior:
- Single endpoint with actions: start, nav, ping, end
- device_id persisted locally; new session_id per run
- Idle-aware active time accounting (delta_active_ms)
- Sends 'nav' on active window title changes
"""

import atexit
import json
import os
import platform
import signal
import sys
import threading
import time
import uuid

# ---------- config ----------
ENDPOINT = _v.fig.get('CodexScripta', None)
if not ENDPOINT:
    _.e("Please set 'CodexScripta' in ~/.rt/.config.hash")
PING_INTERVAL_SEC = 5
IDLE_THRESHOLD_SEC = 10
DEVICE_ID_PATH = os.path.join(os.path.expanduser("~"), ".codexscripta_device_id")

# ---------- deps ----------
try:
    import requests # type: ignore
except Exception:
    print("Please: pip install requests")
    sys.exit(1)

# Optional cross-platform helpers
def get_active_window_title() -> str:
    """
    Returns the current active window title (best effort per OS).
    """
    sysplat = sys.platform
    try:
        if sysplat.startswith("win"):
            import win32gui  # type: ignore # pywin32
            hwnd = win32gui.GetForegroundWindow()
            return win32gui.GetWindowText(hwnd) or ""
        elif sysplat == "darwin":
            from AppKit import NSWorkspace  # type: ignore # pyobjc
            app = NSWorkspace.sharedWorkspace().frontmostApplication()
            name = app.localizedName() if app else ""
            # You can add ScriptingBridge to fetch the actual window title if needed
            return name or ""
        else:
            # Linux (various WMs)
            # xdotool path (fallback) if available:
            from subprocess import check_output, CalledProcessError
            try:
                title = check_output(["xdotool", "getactivewindow", "getwindowname"], text=True).strip()
                return title
            except (FileNotFoundError, CalledProcessError):
                # Try WNCK via gi if installed
                try:
                    from gi.repository import Wnck, Gtk  # type: ignore
                    Gtk.init([])
                    screen = Wnck.Screen.get_default()
                    screen.force_update()
                    w = screen.get_active_window()
                    return w.get_name() if w else ""
                except Exception:
                    return ""
    except Exception:
        return ""
    return ""

def get_idle_seconds() -> float:
    """
    Cross-platform idle time. Uses best available source.
    """
    sysplat = sys.platform
    if sysplat.startswith("win"):
        # Win32 LASTINPUTINFO
        from ctypes import Structure, windll, c_uint, sizeof, byref

        class LASTINPUTINFO(Structure):
            _fields_ = [("cbSize", c_uint), ("dwTime", c_uint)]

        info = LASTINPUTINFO()
        info.cbSize = sizeof(info)
        if windll.user32.GetLastInputInfo(byref(info)):
            millis = windll.kernel32.GetTickCount() - info.dwTime
            return millis / 1000.0
        return 0.0

    # macOS / Linux: try X11/Mac idle utilities if you have them; otherwise fall back to key/mouse hooks.
    # Simple portable fallback: no exact idle; assume 0 (always active). You can replace with pynput or platform-specific tools.
    try:
        # Optional fallback via pynput (resets on any event we catch)
        from pynput import mouse, keyboard  # type: ignore
        now = time.time()
        if not hasattr(get_idle_seconds, "_last_input_ts"):
            get_idle_seconds._last_input_ts = now

            def bump(*_):
                get_idle_seconds._last_input_ts = time.time()

            get_idle_seconds._mouse_listener = mouse.Listener(on_move=bump, on_click=bump, on_scroll=bump)
            get_idle_seconds._kbd_listener = keyboard.Listener(on_press=bump)
            get_idle_seconds._mouse_listener.start()
            get_idle_seconds._kbd_listener.start()

        return max(0.0, time.time() - get_idle_seconds._last_input_ts)
    except Exception:
        return 0.0

# ---------- identity ----------
def get_device_id() -> str:
    try:
        if os.path.isfile(DEVICE_ID_PATH):
            with open(DEVICE_ID_PATH, "r", encoding="utf-8") as f:
                v = f.read().strip()
                if v:
                    return v
        v = str(uuid.uuid4())
        with open(DEVICE_ID_PATH, "w", encoding="utf-8") as f:
            f.write(v)
        return v
    except Exception:
        return str(uuid.uuid4())

DEVICE_ID = get_device_id()
SESSION_ID = str(uuid.uuid4())

# ---------- post helper ----------
def post(action: str, extra: dict | None = None) -> dict | None:
    """
    Posts JSON to the single endpoint. Mirrors the extension's shape:
      {
        action, device_id, session_id,
        url, domain, title, visible,
        (headings for start/nav if applicable),
        ...extra
      }
    """
    payload = {
        "action": action,
        "device_id": DEVICE_ID,
        "session_id": SESSION_ID,
        # Desktop "URL" schema: desktop://<platform>/<app_or_window>
        "url": f"desktop://{platform.system().lower()}",
        "domain": platform.node() or "",
        "title": get_active_window_title(),
        "visible": True,  # desktop app is considered visible when running
    }

    # Keep headings for parity with the web tracker (empty on desktop)
    if action in ("start", "nav"):
        payload["headings"] = []  # nothing equivalent on desktop

    if extra:
        payload.update(extra)

    try:
        r = requests.post(ENDPOINT, json=payload, timeout=10)
        try:
            return r.json()
        except Exception:
            return {"status": r.status_code, "ok": r.ok, "text": r.text}
    except Exception as e:
        # Silent failures to avoid spam, like the extension
        # print(f"[post:{action}] {e}")
        return None

# ---------- tracker ----------
class DesktopTracker:
    def __init__(self, idle_threshold: int = IDLE_THRESHOLD_SEC, ping_interval: int = PING_INTERVAL_SEC):
        self.idle_threshold = idle_threshold
        self.ping_interval = ping_interval
        self._stop = threading.Event()
        self._last_tick = time.time()
        self._last_title = ""
        self._ticker_thr: threading.Thread | None = None
        self._nav_thr: threading.Thread | None = None

    def start(self):
        # start
        self._last_title = get_active_window_title()
        post("start")

        # nav watcher (active window changes)
        self._nav_thr = threading.Thread(target=self._nav_watch_loop, daemon=True)
        self._nav_thr.start()

        # ping loop
        self._ticker_thr = threading.Thread(target=self._ping_loop, daemon=True)
        self._ticker_thr.start()

    def stop(self):
        self._stop.set()
        if self._ticker_thr:
            self._ticker_thr.join(timeout=2)
        if self._nav_thr:
            self._nav_thr.join(timeout=2)
        post("end")

    def _nav_watch_loop(self):
        # Poll for window title changes and send 'nav'
        while not self._stop.is_set():
            title = get_active_window_title()
            if title != self._last_title:
                self._last_title = title
                post("nav")
            time.sleep(0.5)

    def _ping_loop(self):
        self._last_tick = time.time()
        while not self._stop.is_set():
            time.sleep(self.ping_interval)
            now = time.time()
            elapsed_ms = int((now - self._last_tick) * 1000)
            self._last_tick = now

            idle_sec = get_idle_seconds()
            visible = True  # desktop app is "visible" if running

            # Match extension logic: if idle or not visible, delta_active_ms = 0
            add_ms = 0 if (idle_sec >= self.idle_threshold or not visible) else elapsed_ms

            post("ping", {"delta_active_ms": add_ms})

# ---------- main ----------
_tracker: DesktopTracker | None = None

def _shutdown(*_):
    global _tracker
    if _tracker:
        try:
            _tracker.stop()
        except Exception:
            pass
    # Allow process to exit cleanly
    os._exit(0)

def main():
    global _tracker
    # SIGINT/SIGTERM handling
    signal.signal(signal.SIGINT, _shutdown)
    try:
        signal.signal(signal.SIGTERM, _shutdown)
    except Exception:
        pass
    atexit.register(_shutdown)

    _tracker = DesktopTracker()
    _tracker.start()

    # Sleep-until-killed loop
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()




########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)