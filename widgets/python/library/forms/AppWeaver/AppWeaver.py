#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from py_compile import main
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from prompt_toolkit import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, HSplit, VSplit, Window, ConditionalContainer
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Checkbox, Label, RadioList, TextArea
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.filters import Condition


# -----------------------------
# Default schema (used if no file argument is provided)
# -----------------------------
DEFAULT_SCHEMA = {
	"element": ".AppWeaver",
	"title": "Full Field Type Coverage",
	"collection": "sample",
	"db": "snippets",
	"fields": [
		{"db": "_id", "_hidden": True, "label": "", "type": "hidden", "value": "_id", "attributes": {"id": "_id"}},
		{"db": "_public", "_hidden": True, "type": "hidden", "value": "", "attributes": {"id": "_public"}},

		{"type": "labelOnly", "label": "🔐 Identification"},

		{"type": "fieldsetStart", "label": "Default", "classList": ["bordered"], "showToggle": True},
		{"db": "one", "label": "One", "type": "text", "value": "", "attributes": {"id": "one"}},
		{"db": "two", "label": "Two", "type": "text", "value": "", "attributes": {"id": "two"}},
		{"type": "fieldsetEnd"},

		{"type": "fieldsetStart", "label": "Login In", "classList": ["bordered"], "showToggle": True},
		{"db": "username", "label": "Username", "type": "text", "value": "admin", "attributes": {"id": "username"}},
		{"db": "password", "label": "Password", "type": "password", "value": "", "attributes": {"id": "password"}},
		{"type": "fieldsetEnd"},

		{"type": "groupStart", "label": "Contact", "showToggle": True, "roles": ["admin", "editor"], "classList": ["gray"]},
		{"db": "email", "label": "Email", "type": "email", "value": "example@test.com", "attributes": {"id": "email"}},
		{"db": "url", "label": "Website", "type": "url", "value": "https://example.com", "attributes": {"id": "url"}},
		{"db": "phone", "label": "Phone", "type": "tel", "value": "+1234567890", "attributes": {"id": "phone"}},
		{"type": "groupEnd"},

		{"type": "sectionStart", "label": "Numeric", "classList": ["lightbox"], "showToggle": True},
		{"db": "number", "label": "Quantity", "type": "number", "value": 5},
		{"db": "range", "label": "Slider", "type": "range", "value": 50, "attributes": {"min": 0, "max": 100}},
		{"db": "color", "label": "Favorite Color", "type": "color", "value": "#ff0000"},
		{"db": "birth_date", "label": "Birthday", "type": "date", "value": "2000-01-01"},
		{"db": "meeting", "label": "Meeting Time", "type": "datetime-local", "value": "2025-06-30T10:00"},
		{"db": "wake_time", "label": "Wake Up", "type": "time", "value": "07:30"},
		{"type": "sectionEnd"},

		{"type": "labelOnly", "label": "🧠 Preferences"},
		{"db": "theme", "label": "Theme", "type": "radio", "value": "dark", "options": ["light", "dark", "system"]},
		{"db": "language", "label": "Preferred Language", "type": "text", "list": "langList", "value": "javascript"},
		{"db": "tags", "is": "tags", "label": "Tags", "type": "text", "list": "tagList", "value": "form,example"},
		{"db": "bio", "label": "Bio", "type": "textarea", "value": "This is a test user profile."},
		{"db": "role", "label": "Role", "type": "select", "value": "editor", "options": ["admin", "editor", "viewer"]},
		{"db": "enable_feature", "label": "Enable Feature", "type": "checkbox", "value": True},
		{"db": "auto_save", "label": "Auto Save", "type": "switch", "value": True},

		{"type": "labelOnly", "label": "📁 Uploads"},
		{"db": "upload", "label": "Upload File", "type": "file", "attributes": {"id": "upload"}},
		{"db": "gallery", "label": "Upload Multiple", "type": "file", "multiple": True},

		{"db": "remoteAssets", "label": "Remote File URLs", "type": "textarea", "is": "upload",
		"value": "https://example.com/test.pdf\nhttps://example.com/image.jpg"}
	],
	"datalists": [
		{"id": "langList", "options": ["javascript", "python", "php", "html", "css", "sql"]},
		{"id": "tagList", "options": ["form", "example", "demo", "advanced"]}
	]
}


# -----------------------------
# Utility dataclasses
# -----------------------------
@dataclass
class FieldBinding:
	db_key: str
	ftype: str
	widget: Any
	hidden: bool = False
	is_tags: bool = False
	multiple_files: bool = False


# -----------------------------
# Collapsible Section helper
# -----------------------------
class Collapsible:
	def __init__(self, title: str, body_container, initially_open: bool = True):
		self.title = title
		self.open_state: List[bool] = [initially_open]

		self.header = Button(text=self._header_text(), handler=self.toggle)
		self.body = ConditionalContainer(
			content=body_container,
			filter=Condition(lambda: self.open_state[0])
		)
		self.container = HSplit([
			Window(height=1, char="-", style="class:separator"),
			Box(self.header, padding_left=1, padding_right=1),
			self.body,
		])

	def _header_text(self) -> str:
		return f" {'▼' if self.open_state[0] else '▶'} {self.title} "

	def set_open(self, is_open: bool):
		self.open_state[0] = bool(is_open)
		self.header.text = self._header_text()

	def toggle(self):
		self.set_open(not self.open_state[0])
		try:
			get_app().invalidate()
		except Exception:
			pass

	def __pt_container__(self):
		return self.container


# -----------------------------
# Form App
# -----------------------------
class AppWeaver:
	def __init__(self, schema: Dict[str, Any], out_path: Optional[str] = None):
		self.out_path = out_path
		self.schema = schema
		self.title = schema.get("title") or "Form"
		self.fields: List[Dict[str, Any]] = schema.get("fields", [])
		self.datalists = {d["id"]: d.get("options", []) for d in schema.get("datalists", [])}
		self.bindings: List[FieldBinding] = []

		self.sections: List[Collapsible] = []
		self.active_section: int = 0

		self.root_container = None
		self.status_bar = Label(
			text="  [Tab] next  [Shift+Tab] prev  [Ctrl-S] save  [Esc/Ctrl-Q/Ctrl-C/q] exit  [F6/F7] next/prev section"
		)
		self.output_area = TextArea(read_only=True, height=6, style="class:output", scrollbar=True)
		self.app: Optional[Application] = None


	# ------------- Widget Builders -------------
	def _label_row(self, label_text: str) -> Any:
		return Box(VSplit([Label(text=label_text, dont_extend_width=True)]), padding_left=2, padding_right=2)

	def _field_row(self, label_text: str, widget) -> Any:
		return Box(VSplit([Label(text=label_text, width=24, dont_extend_width=True), widget]),
				padding_left=2, padding_right=2)

	def _make_text(self, value: str = "", completer: Optional[WordCompleter] = None, password: bool = False) -> TextArea:
		return TextArea(text=str(value) if value is not None else "", multiline=False, password=password, completer=completer)

	def _make_textarea(self, value: str = "") -> TextArea:
		return TextArea(text=str(value) if value is not None else "", multiline=True, height=4, scrollbar=True)

	def _make_checkbox(self, value: bool = False) -> Checkbox:
		return Checkbox(text="", checked=bool(value))

	def _make_radiolist(self, options: List[str], value: Optional[str]) -> RadioList:
		items = [(opt, opt) for opt in options]
		rl = RadioList(values=items)  # some versions don’t accept current_value in ctor
		if value in options:
			try:
				rl.current_value = value
			except Exception:
				pass
		return rl

	# ------------- Schema Parsing -------------
	def build_form(self):
		body_children: List[Any] = [
			Label(text=f"== {self.title} ==", style="class:title"),
			Window(height=1, char=" "),
		]

		stack: List[List[Any]] = [body_children]
		group_titles: List[Collapsible] = []

		for f in self.fields:
			ftype = f.get("type", "text")
			label = f.get("label", "")
			is_hidden = (ftype == "hidden") or f.get("_hidden", False)

			if ftype in ("fieldsetStart", "groupStart", "sectionStart"):
				title = label or ftype.replace("Start", "").title()
				inner_list: List[Any] = []
				stack.append(inner_list)
				stack[-1].append(("__PENDING_COLLAPSE__", title, f.get("showToggle", True)))
				continue

			if ftype in ("fieldsetEnd", "groupEnd", "sectionEnd"):
				inner = stack.pop()
				if inner and isinstance(inner[0], tuple) and inner[0][0] == "__PENDING_COLLAPSE__":
					_, title, show = inner.pop(0)
					body = HSplit(inner)
					if show:
						coll = Collapsible(title, body_container=body, initially_open=False)
						group_titles.append(coll)
						stack[-1].append(coll)
					else:
						stack[-1].append(body)
				else:
					stack[-1].append(HSplit(inner))
				continue

			if ftype == "labelOnly":
				stack[-1].append(self._label_row(label))
				continue

			if is_hidden:
				db_key = f.get("db") or f.get("name") or ""
				self.bindings.append(FieldBinding(db_key=db_key, ftype="hidden", widget=f.get("value", ""), hidden=True))
				continue

			db_key = f.get("db") or f.get("name") or ""
			value = f.get("value", "")
			attrs = f.get("attributes", {}) or {}

			completer = None
			list_id = f.get("list")
			if list_id and list_id in self.datalists:
				completer = WordCompleter(self.datalists[list_id], ignore_case=True)

			binding_kwargs: Dict[str, Any] = {"db_key": db_key, "ftype": ftype, "widget": None, "hidden": False}

			if ftype in ("text", "email", "url", "tel", "date", "time", "datetime-local", "color"):
				widget = self._make_text(value=value, completer=completer, password=False)

			elif ftype == "password":
				widget = self._make_text(value=value, completer=None, password=True)

			elif ftype == "textarea":
				widget = self._make_textarea(value=value)

			elif ftype in ("number", "range"):
				min_v = attrs.get("min")
				max_v = attrs.get("max")
				if ftype == "range":
					label = f"{label}  (min={min_v if min_v is not None else '-∞'}, max={max_v if max_v is not None else '+∞'})"
				widget = self._make_text(value=str(value) if value is not None else "")

			elif ftype == "radio":
				options = f.get("options", [])
				widget = self._make_radiolist(options, value)

			elif ftype == "select":
				options = f.get("options", [])
				widget = self._make_radiolist(options, value)

			elif ftype in ("checkbox", "switch"):
				widget = self._make_checkbox(value=bool(value))

			elif ftype == "file":
				widget = self._make_text(value=str(value) if value is not None else "")
				binding_kwargs["multiple_files"] = bool(f.get("multiple", False))

			else:
				widget = self._make_text(value=str(value) if value is not None else "")

			fb = FieldBinding(**binding_kwargs)  # type: ignore
			fb.widget = widget
			fb.is_tags = (f.get("is") == "tags")
			self.bindings.append(fb)

			row = self._field_row(label, widget)
			stack[-1].append(row)

		while len(stack) > 1:
			inner = stack.pop()
			stack[-1].append(HSplit(inner))

		self.sections = group_titles
		self.active_section = 0
		for i, c in enumerate(self.sections):
			c.set_open(i == 0)

		btn_save = Button(text=" Save (Ctrl-S) ", handler=self.save)
		btn_cancel = Button(text=" Cancel (Esc) ", handler=self.cancel)
		footer = VSplit([
			btn_save,
			Window(width=2),
			btn_cancel,
			Window(width=1, char="|", style="class:separator"),
			self.status_bar,
		])

		form_body = HSplit(body_children)
		self.root_container = HSplit([
			form_body,
			Window(height=1, char=" "),
			self.output_area,
			Window(height=1, char=" "),
			footer,
		])

		# Key bindings
		kb = KeyBindings()

		# --- Navigation: make Tab/Shift+Tab move focus ---
		@kb.add('tab')
		def _(e):
			e.app.layout.focus_next()

		@kb.add('s-tab')
		def _(e):
			e.app.layout.focus_previous()

		@kb.add('f9')
		def _(e):
			e.app.layout.focus_next()

		@kb.add('f8')
		def _(e):
			e.app.layout.focus_previous()

		# Emergency exits
		@kb.add('c-c')
		def _(e): e.app.exit()

		@kb.add('c-q')
		def _(e): e.app.exit()

		@kb.add('q')
		def _(e): e.app.exit()

		# Save / Cancel
		@kb.add("c-s")
		def _(event): self.save()

		@kb.add("escape")
		def _(event): self.cancel()

		# Toggle all collapsibles
		@kb.add("f2")
		def _(event):
			for c in self.sections:
				c.toggle()
			get_app().invalidate()

		# Next/Prev section (F6 next, F7 prev)
		@kb.add('f6')
		def _(e):
			if self.sections:
				self.active_section = (self.active_section + 1) % len(self.sections)
				for i, c in enumerate(self.sections):
					c.set_open(i == self.active_section)
				get_app().invalidate()

		@kb.add('f7')
		def _(e):
			if self.sections:
				self.active_section = (self.active_section - 1) % len(self.sections)
				for i, c in enumerate(self.sections):
					c.set_open(i == self.active_section)
				get_app().invalidate()

		# Pick a sensible initial focus: first non-hidden widget
		first_focus = None
		for b in self.bindings:
			if not b.hidden and b.widget is not None:
				first_focus = b.widget
				break

		self.app = Application(
			layout=Layout(self.root_container, focused_element=first_focus),
			key_bindings=kb,
			full_screen=True,
			mouse_support=True,
			style=Style.from_dict({
				"title": "bold underline",
				"separator": "#666666",
				"output": "bg:#202020 #a8ffa8",
				"section.header": "bold",
			})
		)

	# ------------- Actions -------------
	def save(self):
		data: Dict[str, Any] = {}
		for b in self.bindings:
			if b.hidden:
				# hidden widget holds raw value directly
				data[b.db_key] = b.widget
				continue

			w = b.widget
			if isinstance(w, TextArea):
				val = w.text
				if b.is_tags:
					data[b.db_key] = [t.strip() for t in val.split(",") if t.strip()]
				elif b.ftype == "file" and b.multiple_files:
					data[b.db_key] = [p.strip() for p in val.split(",") if p.strip()]
				else:
					data[b.db_key] = val

			elif isinstance(w, Checkbox):
				data[b.db_key] = bool(w.checked)

			elif isinstance(w, RadioList):
				# current_value is standard; guard for older versions
				try:
					data[b.db_key] = w.current_value
				except Exception:
					data[b.db_key] = None

			else:
				# best-effort fallback
				data[b.db_key] = getattr(w, "text", None)

		pretty = json.dumps(data, indent=2)
		self.output_area.text = pretty
		print(pretty, flush=True)

		# Write to file if --out/-o was provided
		if getattr(self, "out_path", None):
			try:
				Path(self.out_path).write_text(pretty + "\n", encoding="utf-8")
				self.status_bar.text = f"  Saved to {self.out_path}  |  [Ctrl-S] save again"
			except Exception as e:
				self.status_bar.text = f"  Save failed: {e}"

	# def save(self):
	#     data: Dict[str, Any] = {}
	#     for b in self.bindings:
	#         if b.hidden:
	#             data[b.db_key] = b.widget
	#             continue

	#         if isinstance(b.widget, TextArea):
	#             val = b.widget.text
	#             if b.is_tags:
	#                 data[b.db_key] = [t.strip() for t in val.split(",") if t.strip()]
	#             elif b.ftype == "file" and b.multiple_files:
	#                 data[b.db_key] = [p.strip() for p in val.split(",") if p.strip()]
	#             else:
	#                 data[b.db_key] = val

	#         elif isinstance(b.widget, Checkbox):
	#             data[b.db_key] = bool(b.widget.checked)

	#         elif isinstance(b.widget, RadioList):
	#             data[b.db_key] = b.widget.current_value

	#         else:
	#             data[b.db_key] = None

	#     pretty = json.dumps(data, indent=2)
	#     self.output_area.text = pretty
	#     print(pretty, flush=True)

	def cancel(self):
		if self.app:
			self.app.exit()

	def run(self):
		self.build_form()
		assert self.app is not None
		self.app.run()

# -----------------------------
# Entrypoint
# -----------------------------
from typing import Optional

def _find_schema_arg(path: Optional[str] = None) -> Optional[Path]:
	"""
	Choose a schema file from:
	1) explicit 'path' arg
	2) first argv token that looks like a schema path (e.g. *.json) or is an existing file
	"""
	candidates: List[str] = []
	if path:
		candidates.append(str(path))

	# scan cli args after the script name; tolerate extra tokens like 'AppWeaver'
	for tok in sys.argv[1:]:
		if tok.startswith('-'):
			continue
		# prefer *.json; also accept existing files even without .json
		if tok.lower().endswith('.json'):
			candidates.append(tok)
		else:
			p = Path(tok)
			if p.is_file():
				candidates.append(tok)

	for c in candidates:
		p = Path(c)
		if p.is_file():
			return p
	return None


def _load_schema_from_arg(path: Optional[str] = None) -> Dict[str, Any]:
	chosen = _find_schema_arg(path)
	if chosen:
		try:
			return json.loads(chosen.read_text(encoding="utf-8"))
		except Exception:
			# fall back silently if unreadable/invalid JSON
			pass
	return DEFAULT_SCHEMA


def _parse_out_path(argv: List[str]) -> Optional[str]:
	i = 0
	while i < len(argv):
		t = argv[i]
		if t in ("--out", "-o"):
			return argv[i + 1] if i + 1 < len(argv) else None
		if t.startswith("--out="):
			return t.split("=", 1)[1]
		i += 1
	return None



def appWeaver(path: Optional[str] = None):
	schema = _load_schema_from_arg(path)
	out_path = _parse_out_path(sys.argv[1:])
	app = AppWeaver(schema, out_path=out_path)
	app.run()



if __name__ == "__main__":
	appWeaver()