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

import atexit
import json
import os
import signal
import socket
import sys
import threading
import time
import uuid
from pathlib import Path
from subprocess import check_output, CalledProcessError

# =========================
# Config
# =========================
ENDPOINT = _v.fig.get('CodexScripta', None)
if not ENDPOINT:
	_.e("Please set 'CodexScripta' in ~/.rt/.config.hash")
PING_INTERVAL_SEC = 5
IDLE_THRESHOLD_SEC = 10

STATE_DIR = Path.home() / ".codexscripta" / "active-window"
DEVICE_FILE = Path.home() / ".codexscripta_device_id"

# =========================
# Deps
# =========================
try:
	import requests
except Exception:
	print("Please: pip install requests")
	sys.exit(1)

HOSTNAME = socket.gethostname()

# =========================
# FS helpers
# =========================
def ensure_dirs():
	STATE_DIR.mkdir(parents=True, exist_ok=True)

def get_device_id():
	try:
		if DEVICE_FILE.exists():
			v = DEVICE_FILE.read_text(encoding="utf-8").strip()
			if v:
				return v
		v = str(uuid.uuid4())
		DEVICE_FILE.write_text(v, encoding="utf-8")
		return v
	except Exception:
		return str(uuid.uuid4())

DEVICE_ID = get_device_id()
SESSION_ID = str(uuid.uuid4())

# =========================
# Active window (cross-platform)
# =========================
_HAS_WIN32 = False
if sys.platform.startswith("win"):
	try:
		import win32gui  # pywin32
		_HAS_WIN32 = True
	except Exception:
		_HAS_WIN32 = False

def get_active_window_title():
	# Windows
	if sys.platform.startswith("win") and _HAS_WIN32:
		try:
			hwnd = win32gui.GetForegroundWindow()
			return win32gui.GetWindowText(hwnd) or ""
		except Exception:
			return ""
	# macOS
	if sys.platform == "darwin":
		try:
			app = check_output(
				['osascript', '-e', 'tell application "System Events" to get name of first process whose frontmost is true'],
				text=True
			).strip()
		except Exception:
			app = ""
		title = ""
		if app:
			script = f'tell application "{app}" to try\nget name of window 1\nend try'
			try:
				title = check_output(['osascript', '-e', script], text=True).strip()
			except Exception:
				title = ""
		return f"{title} - {app}".strip(" -")
	# Linux
	try:
		return check_output(["xdotool", "getactivewindow", "getwindowname"], text=True).strip()
	except (FileNotFoundError, CalledProcessError):
		pass
	try:
		from gi.repository import Wnck, Gtk  # type: ignore
		Gtk.init([])
		screen = Wnck.Screen.get_default()
		screen.force_update()
		w = screen.get_active_window()
		return w.get_name() if w else ""
	except Exception:
		return ""

# =========================
# Idle detection (cross-platform)
# =========================
def get_idle_seconds_windows():
	from ctypes import Structure, windll, c_uint, sizeof, byref
	class LASTINPUTINFO(Structure):
		_fields_ = [("cbSize", c_uint), ("dwTime", c_uint)]
	info = LASTINPUTINFO()
	info.cbSize = sizeof(info)
	if windll.user32.GetLastInputInfo(byref(info)):
		millis = windll.kernel32.GetTickCount() - info.dwTime
		return millis / 1000.0
	return 0.0

class _IdleFallback:
	def __init__(self):
		self._last = time.time()
		self._ok = False
		self._started = False
	def start(self):
		if self._started:
			return
		self._started = True
		try:
			from pynput import mouse, keyboard  # type: ignore
			def bump(*_):
				self._last = time.time()
			self._mouse = mouse.Listener(on_move=bump, on_click=bump, on_scroll=bump)
			self._kbd = keyboard.Listener(on_press=bump)
			self._mouse.start()
			self._kbd.start()
			self._ok = True
		except Exception:
			self._ok = False
	def idle_seconds(self):
		if not self._ok:
			return 0.0
		return max(0.0, time.time() - self._last)

if sys.platform.startswith("win"):
	get_idle_seconds = get_idle_seconds_windows
else:
	_idlefb = _IdleFallback()
	_idlefb.start()
	get_idle_seconds = _idlefb.idle_seconds

# =========================
# Networking
# =========================
def post(action, extra=None):
	payload = {
		"action": action,
		"device_id": DEVICE_ID,
		"session_id": SESSION_ID,
		"url": f"desktop://{sys.platform}",
		"domain": HOSTNAME,
		"title": CURRENT["title"],   # server extracts file path from THIS
		"visible": True,
	}
	if action in ("start", "nav"):
		payload["headings"] = []     # parity with your web payload shape
	if extra:
		payload.update(extra)
	try:
		requests.post(ENDPOINT, json=payload, timeout=8)
	except Exception:
		# Silent failure (don’t interrupt local tracking)
		pass

def send_start():
	post("start")

def send_nav():
	post("nav")

def send_ping(delta_active_ms):
	post("ping", {"delta_active_ms": int(delta_active_ms)})

def send_end():
	post("end")

# =========================
# Local accounting (for your eyes; server is the source of truth)
# =========================
def ymd():
	return time.strftime("%Y-%m-%d", time.gmtime())

def totals_path():
	return STATE_DIR / f"pc-aw-{ymd()}-totals.json"

def load_totals():
	try:
		return json.loads(totals_path().read_text(encoding="utf-8"))
	except Exception:
		return {}

def save_totals(totals):
	p = totals_path()
	tmp = str(p) + ".tmp"
	Path(tmp).write_text(json.dumps(totals, indent=2, ensure_ascii=False), encoding="utf-8")
	os.replace(tmp, p)

# =========================
# Core loop
# =========================
CURRENT = {"title": "", "active_acc": 0.0}  # seconds (local view)
TOTALS = {}
IS_IDLE = False
LAST_PING = time.time()
STOP = threading.Event()

def switch_window(new_title):
	global CURRENT
	# flush the active_acc into totals for the old title
	if CURRENT["title"] and CURRENT["active_acc"] > 0:
		TOTALS[CURRENT["title"]] = TOTALS.get(CURRENT["title"], 0.0) + CURRENT["active_acc"]
		CURRENT["active_acc"] = 0.0
		save_totals(TOTALS)
	CURRENT["title"] = new_title
	send_nav()

def tick():
	global IS_IDLE, LAST_PING
	ts = time.time()

	# detect window title change
	title = (get_active_window_title() or "").strip()
	if title != CURRENT["title"]:
		switch_window(title)

	# idle
	idle_sec = get_idle_seconds()
	IS_IDLE = idle_sec >= IDLE_THRESHOLD_SEC

	# ping every N seconds
	if (ts - LAST_PING) >= PING_INTERVAL_SEC:
		elapsed_ms = int((ts - LAST_PING) * 1000)
		LAST_PING = ts
		add_ms = 0 if IS_IDLE else elapsed_ms
		if CURRENT["title"] and add_ms > 0:
			CURRENT["active_acc"] += add_ms / 1000.0
		send_ping(add_ms)

def console_status():
	last = 0
	while not STOP.is_set():
		if time.time() - last >= 1:
			last = time.time()
			total_for_cur = TOTALS.get(CURRENT["title"], 0.0) + CURRENT["active_acc"]
			sys.stdout.write(
				f"\r[{'IDLE' if IS_IDLE else 'ACTIVE':<6}] {int(total_for_cur)}s  |  {(CURRENT['title'] or '')[:140]:<140}"
			)
			sys.stdout.flush()
		time.sleep(0.1)

def run():
	ensure_dirs()
	global TOTALS
	TOTALS = load_totals()

	# initial window + start
	first = (get_active_window_title() or "(unknown)").strip()
	CURRENT["title"] = first
	send_start()

	try:
		while not STOP.is_set():
			tick()
			time.sleep(0.2)
	except KeyboardInterrupt:
		pass

def shutdown():
	# flush current title into totals
	if CURRENT["title"] and CURRENT["active_acc"] > 0:
		TOTALS[CURRENT["title"]] = TOTALS.get(CURRENT["title"], 0.0) + CURRENT["active_acc"]
	save_totals(TOTALS)
	send_end()

def _sigterm(_s, _f):
	STOP.set()
	shutdown()
	os._exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, _sigterm)
	try:
		signal.signal(signal.SIGTERM, _sigterm)
	except Exception:
		pass
	atexit.register(shutdown)

	t_status = threading.Thread(target=console_status, daemon=True)
	t_status.start()

	run()









########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)