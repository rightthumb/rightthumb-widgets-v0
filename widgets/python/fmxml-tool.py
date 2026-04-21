import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )

	_.switches.register( 'Fields', '--f,-field,-fields','field.txt', isData='data', description='Fields', isRequired=False )
	_.switches.register( 'Scripts', '--s,-script,-scripts','script.txt', isData='data', description='Scripts', isRequired=False )
	_.switches.register( 'Layouts', '--l,-li,-layout,-layouts','layout.txt', isData='data', description='Layouts', isRequired=False )

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Convert FileMaker xml to json or html',
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








import json
import xml.etree.ElementTree as ET
from typing import Optional

def fm_fields_to_json(xml_text: str, pretty: bool = False) -> str:
	"""
	Convert a FileMaker fmxmlsnippet (FIELDS ONLY) string to JSON.

	Args:
		xml_text: The fmxmlsnippet XML text containing <Field> nodes.
		pretty: If True, return pretty-printed JSON.

	Returns:
		str: JSON array string of field dicts.
	"""
	def _t(v: Optional[str]) -> str:
		return (v or "").strip()

	def _as_bool(v: Optional[str]):
		if v is None:
			return None
		s = str(v).strip().lower()
		if s in ("true", "1", "yes"): return True
		if s in ("false", "0", "no"): return False
		return v

	def _attrs_boolified(elem):
		return {
			k: (_as_bool(v) if str(v) in ("True", "False", "true", "false", "0", "1") else v)
			for k, v in elem.attrib.items()
		}

	def _get_child(elem, name):
		return elem.find(name)

	def _get_text(elem, name):
		node = elem.find(name)
		return _t(node.text) if node is not None else None

	def _get_cdata_text(node):
		return _t(node.text) if node is not None else None

	def _parse_serial(auto):
		node = _get_child(auto, "Serial")
		if node is None:
			return None
		out = _attrs_boolified(node)
		for k in ("increment", "nextValue"):
			if k in out:
				try: out[k] = int(out[k])
				except: pass
		return out

	def _parse_lookup(auto):
		node = _get_child(auto, "Lookup")
		if node is None:
			return None
		out = {}
		t = _get_child(node, "Table")
		if t is not None:
			out["table"] = {"id": t.attrib.get("id"), "name": t.attrib.get("name")}
		f = _get_child(node, "Field")
		if f is not None:
			out["field"] = {"id": f.attrib.get("id"), "name": f.attrib.get("name"), "table": f.attrib.get("table")}
		nm = _get_child(node, "NoMatchCopyOption")
		if nm is not None and "value" in nm.attrib:
			out["noMatchCopyOption"] = nm.attrib["value"]
		ce = _get_child(node, "CopyEmptyContent")
		if ce is not None and "value" in ce.attrib:
			out["copyEmptyContent"] = _as_bool(ce.attrib["value"])
		return out or None

	def _parse_autoenter(field):
		auto = _get_child(field, "AutoEnter")
		if auto is None:
			return None
		out = _attrs_boolified(auto)
		out["constantData"] = _get_text(auto, "ConstantData")
		calc = _get_child(auto, "Calculation")
		if calc is not None:
			out["calculation"] = {"table": calc.attrib.get("table"), "expression": _get_cdata_text(calc)}
		serial = _parse_serial(auto)
		if serial: out["serial"] = serial
		lookup = _parse_lookup(auto)
		if lookup: out["lookup"] = lookup
		return {k: v for k, v in out.items() if v not in (None, "", {})}

	def _parse_validation(field):
		val = _get_child(field, "Validation")
		if val is None:
			return None
		out = _attrs_boolified(val)
		for tag in ("NotEmpty", "Unique", "Existing", "StrictValidation"):
			node = _get_child(val, tag)
			if node is not None and "value" in node.attrib:
				out[tag[0].lower() + tag[1:]] = _as_bool(node.attrib["value"])
		return out

	def _parse_storage(field):
		stor = _get_child(field, "Storage")
		if stor is None:
			return None
		out = _attrs_boolified(stor)
		if "maxRepetition" in out:
			try: out["maxRepetition"] = int(out["maxRepetition"])
			except: pass
		return out

	def _parse_field_calc(field):
		calc = _get_child(field, "Calculation")
		if calc is None:
			return None
		return {"table": calc.attrib.get("table"), "expression": _get_cdata_text(calc)}

	# Parse XML, collect fields
	root = ET.fromstring(xml_text)
	fields_out = []
	for f in root.findall(".//Field"):
		item = {
			"id": f.attrib.get("id"),
			"name": f.attrib.get("name"),
			"dataType": f.attrib.get("dataType"),
			"fieldType": f.attrib.get("fieldType"),
		}
		try:
			item["id"] = int(item["id"]) if item["id"] is not None else None
		except:
			pass

		comment = _get_child(f, "Comment")
		if comment is not None and comment.text:
			item["comment"] = _t(comment.text)

		auto = _parse_autoenter(f)
		if auto: item["autoEnter"] = auto

		validation = _parse_validation(f)
		if validation: item["validation"] = validation

		storage = _parse_storage(f)
		if storage: item["storage"] = storage

		field_calc = _parse_field_calc(f)
		if field_calc: item["calculation"] = field_calc

		item = {k: v for k, v in item.items() if v is not None}
		fields_out.append(item)

	return json.dumps(fields_out, indent=4 if pretty else None, ensure_ascii=False)








import json
import xml.etree.ElementTree as ET
from typing import Optional, Dict, Any, List

def fm_scripts_to_json(xml_text: str, pretty: bool = False) -> str:
	"""
	Convert a FileMaker fmxmlsnippet (SCRIPTS) string to JSON.

	Args:
		xml_text: The fmxmlsnippet XML text containing <Script> nodes.
		pretty: If True, return pretty-printed JSON.

	Returns:
		str: JSON array string of script dicts.
	"""
	def _t(v: Optional[str]) -> str:
		return (v or "").strip()

	def _as_bool(v: Optional[str]):
		if v is None:
			return None
		s = str(v).strip().lower()
		if s in ("true", "1", "yes"): return True
		if s in ("false", "0", "no"): return False
		return v

	def _attrs_boolified(elem) -> Dict[str, Any]:
		out: Dict[str, Any] = {}
		for k, v in elem.attrib.items():
			if str(v) in ("True", "False", "true", "false", "0", "1"):
				out[k] = _as_bool(v)
			else:
				out[k] = v
		return out

	def _calc_text(node) -> Optional[str]:
		if node is None:
			return None
		# CDATA arrives as .text
		return _t(node.text)

	def _first(elem, name: str):
		return elem.find(name)

	def _field_ref(node):
		if node is None:
			return None
		return {
			"table": node.attrib.get("table"),
			"id": node.attrib.get("id"),
			"name": node.attrib.get("name"),
		}

	def _layout_ref(node):
		if node is None:
			return None
		return {
			"id": node.attrib.get("id"),
			"name": node.attrib.get("name"),
		}

	def _maybe_num(s: Optional[str]):
		if s is None:
			return None
		try:
			return int(s)
		except:
			try:
				return float(s)
			except:
				return s

	def _grab_calc_container(parent, tag: str):
		"""For blocks like <Value><Calculation>..</Calculation></Value>."""
		node = _first(parent, tag)
		if node is None:
			return None
		calc = _first(node, "Calculation")
		return _calc_text(calc)

	def _parse_query_block(step):
		"""
		Handles Perform Find -> <Query><RequestRow><Criteria><Field .../><Text>...</Text>
		Returns a normalized list of requests.
		"""
		q = _first(step, "Query")
		if q is None:
			return None
		out: List[Dict[str, Any]] = []
		for req in q.findall(".//RequestRow"):
			row: Dict[str, Any] = {"operation": req.attrib.get("operation")}
			crit = _first(req, "Criteria")
			if crit is not None:
				fnode = _first(crit, "Field")
				tnode = _first(crit, "Text")
				row["criteria"] = {
					"field": _field_ref(fnode),
					"text": _t(tnode.text) if tnode is not None else None
				}
			out.append(row)
		return out or None

	def _parse_new_window(step):
		"""
		Extracts common New Window properties (name/height/width/top/left + styles).
		"""
		out: Dict[str, Any] = {}
		out["layoutDestination"] = (_first(step, "LayoutDestination") or {}).attrib.get("value") if _first(step, "LayoutDestination") is not None else None
		out["name"] = _grab_calc_container(step, "Name")
		out["height"] = _maybe_num(_grab_calc_container(step, "Height"))
		out["width"] = _maybe_num(_grab_calc_container(step, "Width"))
		out["distanceFromTop"] = _maybe_num(_grab_calc_container(step, "DistanceFromTop"))
		out["distanceFromLeft"] = _maybe_num(_grab_calc_container(step, "DistanceFromLeft"))
		styles = _first(step, "NewWndStyles")
		if styles is not None:
			out["styles"] = _attrs_boolified(styles)
		# Clean empties
		return {k: v for k, v in out.items() if v not in (None, "", {})} or None

	def _parse_step(step):
		"""
		Normalize a <Step> into:
		{
		"id": 76, "name": "Set Field", "enable": True,
		"calculation": "...",
		"field": {...}, "layout": {...},
		"options": {...}, "query": [...],
		...
		}
		"""
		base = _attrs_boolified(step)
		# Cast id to int if possible
		if "id" in base:
			base["id"] = _maybe_num(base["id"])
		# Common payloads
		calc = _first(step, "Calculation")
		if calc is not None:
			base["calculation"] = _calc_text(calc)

		# Field, Layout references
		fnode = _first(step, "Field")
		if fnode is not None:
			base["field"] = _field_ref(fnode)

		if step.attrib.get("name") in ("Go to Layout",):
			base["layoutDestination"] = (_first(step, "LayoutDestination") or {}).attrib.get("value") if _first(step, "LayoutDestination") is not None else None
			lnode = _first(step, "Layout")
			if lnode is not None:
				base["layout"] = _layout_ref(lnode)

		# Find Matching Records option
		fmr = _first(step, "FindMatchingRecordsByField")
		if fmr is not None:
			base.setdefault("options", {})["findMatchingRecordsByField"] = fmr.attrib.get("value")

		# Show/Hide Toolbars, Scroll Window, Set Error Capture, Commit Records, etc.
		includeEdit = _first(step, "IncludeEditRecordToolbar")
		if includeEdit is not None:
			base.setdefault("options", {})["includeEditRecordToolbar"] = _as_bool(includeEdit.attrib.get("state"))
		lock = _first(step, "Lock")
		if lock is not None:
			base.setdefault("options", {})["lock"] = _as_bool(lock.attrib.get("state"))
		showhide = _first(step, "ShowHide")
		if showhide is not None:
			base.setdefault("options", {})["showHide"] = showhide.attrib.get("value")
		scrollop = _first(step, "ScrollOperation")
		if scrollop is not None:
			base.setdefault("options", {})["scrollOperation"] = scrollop.attrib.get("value")
		setnode = _first(step, "Set")
		if setnode is not None:
			base.setdefault("options", {})["set"] = _as_bool(setnode.attrib.get("state"))
		noint = _first(step, "NoInteract")
		if noint is not None:
			base.setdefault("options", {})["noInteract"] = _as_bool(noint.attrib.get("state"))
		opt = _first(step, "Option")
		if opt is not None:
			base.setdefault("options", {})["option"] = _as_bool(opt.attrib.get("state"))
		ess = _first(step, "ESSForceCommit")
		if ess is not None:
			base.setdefault("options", {})["essForceCommit"] = _as_bool(ess.attrib.get("state"))

		# Set Variable (Name, Value, Repetition)
		name_node = _first(step, "Name")
		if name_node is not None and (name_node.text or "").strip():
			base.setdefault("variable", {})["name"] = _t(name_node.text)
		val_calc = _grab_calc_container(step, "Value")
		if val_calc is not None:
			base.setdefault("variable", {})["value"] = val_calc
		rep_calc = _grab_calc_container(step, "Repetition")
		if rep_calc is not None:
			base.setdefault("variable", {})["repetition"] = _maybe_num(rep_calc)

		# New Window block
		if step.attrib.get("name") == "New Window":
			nw = _parse_new_window(step)
			if nw:
				base["newWindow"] = nw

		# Perform Find query block
		if step.attrib.get("name") == "Perform Find":
			q = _parse_query_block(step)
			if q:
				base["query"] = q
			restore = _first(step, "Restore")
			if restore is not None and "state" in restore.attrib:
				base.setdefault("options", {})["restore"] = _as_bool(restore.attrib.get("state"))

		# Clean empty keys
		base = {k: v for k, v in base.items() if v not in (None, "", {}, [])}
		return base

	# ---- main parse ----
	root = ET.fromstring(xml_text)
	scripts_out: List[Dict[str, Any]] = []
	for s in root.findall(".//Script"):
		sdict: Dict[str, Any] = _attrs_boolified(s)
		# normalize id
		if "id" in sdict:
			sdict["id"] = _maybe_num(sdict["id"])
		# steps
		steps = []
		for st in s.findall("./Step"):
			steps.append(_parse_step(st))
		if steps:
			sdict["steps"] = steps
		sdict = {k: v for k, v in sdict.items() if v not in (None, "", {}, [])}
		scripts_out.append(sdict)

	return json.dumps(scripts_out, indent=4 if pretty else None, ensure_ascii=False)













import json
import xml.etree.ElementTree as ET
from typing import Optional, Dict, Any, List

def fm_layout_to_json(xml_text: str, pretty: bool = False) -> str:
	"""
	Convert a FileMaker fmxmlsnippet (LAYOUT objects) string to JSON suitable
	for HTML generation (absolute positions, ordered top→bottom).

	Output shape:
	{
	"layout": {"bounds": {"top":..,"left":..,"bottom":..,"right":..,"width":..,"height":..}},
	"objects": [
		{
		"type":"Text"|"Field"|"Button"|...,
		"key":"3",
		"rotation":0,
		"zIndex":0,
		"bounds":{"top":..,"left":..,"bottom":..,"right":..,"width":..,"height":..},
		// Text:
		"text":"...", "textRuns":[{"text":"...","bold":True,"italic":False,"size":12,"font":"Verdana"}],
		// Field:
		"field":{"qualified":"Finances::Title","table":"Finances","name":"Title","id":"7"},
		// Button:
		"label":"...", "actions":[{"id":1,"name":"Perform Script","script":{"id":"2","name":"About Scripts..."}, "currentScript":"Pause"}]
		}, ...
	]
	}
	"""
	def _t(s: Optional[str]) -> str:
		return (s or "").strip()

	def _num(v: Optional[str]) -> Optional[float]:
		if v is None: return None
		try: return float(v)
		except: return None

	def _bounds(node) -> Optional[Dict[str, float]]:
		if node is None: return None
		top  = _num(node.attrib.get("top"))
		left = _num(node.attrib.get("left"))
		bot  = _num(node.attrib.get("bottom"))
		right= _num(node.attrib.get("right"))
		if None in (top,left,bot,right): return None
		return {
			"top": top, "left": left, "bottom": bot, "right": right,
			"width": max(0.0, right - left), "height": max(0.0, bot - top)
		}

	def _layout_bounds(layout_node) -> Optional[Dict[str, float]]:
		if layout_node is None: return None
		top   = _num(layout_node.attrib.get("enclosingRectTop"))
		left  = _num(layout_node.attrib.get("enclosingRectLeft"))
		bot   = _num(layout_node.attrib.get("enclosingRectBottom"))
		right = _num(layout_node.attrib.get("enclosingRectRight"))
		if None in (top,left,bot,right): return None
		return {
			"top": top, "left": left, "bottom": bot, "right": right,
			"width": max(0.0, right - left), "height": max(0.0, bot - top)
		}

	def _text_runs(text_obj) -> (str, List[Dict[str, Any]]):
		"""
		Extract styled runs from <CharacterStyleVector><Style><Data>...</Data>...
		Falls back to empty if not present.
		"""
		runs = []
		plain = []
		csv = text_obj.find("./CharacterStyleVector")
		if csv is not None:
			for st in csv.findall("./Style"):
				data = _t((st.findtext("Data") or ""))
				plain.append(data)
				cs = st.find("CharacterStyle")
				run = {"text": data}
				if cs is not None:
					# Basic style hints only (concise)
					font = cs.find("Font-family")
					size = cs.findtext("Font-size")
					face = cs.findtext("Face")
					run["font"] = font.text if font is not None else None
					run["size"] = float(size) if size else None
					# FileMaker face codes: bitwise; surface the common ones
					try:
						face_i = int(face) if face is not None else 0
					except:
						face_i = 0
					run["bold"] = bool(face_i & 0x1100) or "Bold" in (font.attrib.get("postScript","") if font is not None else "")
					run["italic"] = bool(face_i & 0x2200)
				runs.append({k: v for k, v in run.items() if v not in (None, "")})
		return ("".join(plain), runs)

	def _field_info(obj_node) -> Optional[Dict[str, Any]]:
		# Prefer DDRInfo if present; else <FieldObj><Name>qualified</Name>
		ddr = obj_node.find(".//DDRInfo/Field")
		if ddr is not None:
			table = ddr.attrib.get("table")
			name  = ddr.attrib.get("name")
			fid   = ddr.attrib.get("id")
			return {"qualified": f"{table}::{name}" if table and name else None,
					"table": table, "name": name, "id": fid}
		qualified = obj_node.findtext(".//FieldObj/Name")
		if qualified:
			if "::" in qualified:
				table, name = qualified.split("::", 1)
			else:
				table, name = None, qualified
			return {"qualified": qualified, "table": table, "name": name}
		return None

	def _button_actions(obj_node) -> List[Dict[str, Any]]:
		acts = []
		for st in obj_node.findall(".//ButtonObj/Step"):
			entry: Dict[str, Any] = {}
			# basic step attributes
			try: entry["id"] = int(st.attrib.get("id"))
			except: entry["id"] = st.attrib.get("id")
			entry["name"] = st.attrib.get("name")
			cur = st.find("CurrentScript")
			if cur is not None and "value" in cur.attrib:
				entry["currentScript"] = cur.attrib["value"]
			scr = st.find("Script")
			if scr is not None:
				entry["script"] = {"id": scr.attrib.get("id"), "name": scr.attrib.get("name")}
			acts.append({k: v for k, v in entry.items() if v not in (None, "", {})})
		return acts

	# ---------- parse ----------
	root = ET.fromstring(xml_text)
	layout_node = root.find(".//Layout")
	out: Dict[str, Any] = {"layout": {"bounds": _layout_bounds(layout_node)} if layout_node is not None else {}}
	objects: List[Dict[str, Any]] = []

	if layout_node is None:
		return json.dumps({"layout": {}, "objects": []}, indent=4 if pretty else None, ensure_ascii=False)

	for z, obj in enumerate(layout_node.findall("./Object")):
		item: Dict[str, Any] = {
			"type": obj.attrib.get("type"),
			"key": obj.attrib.get("key"),
			"rotation": int(obj.attrib.get("rotation", "0")),
			"zIndex": z
		}
		b = _bounds(obj.find("./Bounds"))
		if b: item["bounds"] = b

		# TEXT & BUTTON labels share <TextObj> with runs
		text_obj = obj.find("./TextObj")
		if text_obj is not None:
			plain, runs = _text_runs(text_obj)
			if plain: item["text"] = plain
			if runs: item["textRuns"] = runs

		# FIELD specifics
		if obj.attrib.get("type") == "Field":
			info = _field_info(obj)
			if info: item["field"] = info

		# BUTTON specifics
		if obj.attrib.get("type") == "Button":
			if "text" in item: item["label"] = item["text"]
			acts = _button_actions(obj)
			if acts: item["actions"] = acts

		# keep concise: omit giant CSS blobs, but keep theme name if present
		theme = obj.findtext(".//Styles/ThemeName")
		if theme: item["theme"] = theme

		objects.append({k: v for k, v in item.items() if v not in (None, "", {}, [])})

	out["objects"] = objects
	return json.dumps(out, indent=4 if pretty else None, ensure_ascii=False)
















import json
from typing import Any, Dict, List, Tuple, Union, Optional
import math

def layout_json_to_responsive_html(layout_json: Union[str, Dict[str, Any]],
								min_col_width: int = 220) -> Tuple[str, str, Dict[str, Any]]:
	"""
	Convert fm_layout_to_json output (dict or JSON string) into responsive HTML+CSS.

	Strategy (concise but effective):
	1) Normalize elements with (top,left,bottom,right,width,height).
	2) Cluster into vertical "rows" by top proximity; within each row, order by left.
	3) Merge rows into vertical "sections" when their horizontal spans significantly overlap
		(keeps related content together).
	4) For each section:
		- If it contains rows that visually produce multiple columns, render as CSS Grid
		with auto-fit/minmax(min_col_width, 1fr) so it collapses on small screens.
		- Otherwise render as simple stacked blocks.
	5) Derive gutters from median horizontal/vertical gaps to preserve spacing feel.

	Returns:
	(html, css, debug) where:
		html: full HTML string (section wrappers + items)
		css:  accompanying CSS string (scoped classes)
		debug: structure explaining sections/rows/items mapping

	Notes:
	• No external dependencies.
	• You can tweak min_col_width to control grid wrap behavior.
	"""

	# ---------- helpers ----------
	def _ensure_dict(d):
		return json.loads(d) if isinstance(d, str) else d

	def median(vals: List[float], default: float) -> float:
		arr = sorted([v for v in vals if v is not None])
		if not arr:
			return default
		n = len(arr)
		return arr[n//2] if n % 2 else 0.5*(arr[n//2-1] + arr[n//2])

	def horiz_overlap(a: Tuple[float,float], b: Tuple[float,float]) -> float:
		"""Return overlap width between [a0,a1] and [b0,b1]."""
		return max(0.0, min(a[1], b[1]) - max(a[0], b[0]))

	def to_px(v: float) -> str:
		return f"{v:.0f}px"

	def clamp(v, lo, hi):
		return max(lo, min(hi, v))

	def text_of(obj: Dict[str, Any]) -> str:
		if obj.get("type") == "Button":
			return obj.get("label") or obj.get("text") or ""
		if obj.get("type") == "Text":
			return obj.get("text") or ""
		if obj.get("type") == "Field":
			# Use field name as label if we don’t have explicit text nearby.
			fld = obj.get("field") or {}
			return fld.get("name") or fld.get("qualified") or ""
		return obj.get("text") or ""

	# ---------- normalize input ----------
	data = _ensure_dict(layout_json)
	objs: List[Dict[str, Any]] = list(data.get("objects", []))

	# filter out items that have no bounds (rare)
	objs = [o for o in objs if isinstance(o.get("bounds"), dict)]

	# ---------- basic metrics ----------
	heights = [o["bounds"]["height"] for o in objs]
	widths  = [o["bounds"]["width"] for o in objs]
	tops    = [o["bounds"]["top"] for o in objs]
	lefts   = [o["bounds"]["left"] for o in objs]

	avg_h   = median(heights, 24.0)
	avg_w   = median(widths,  160.0)
	row_tol = max(8.0, 0.6 * avg_h)  # row clustering tolerance by top proximity

	# Row clustering by "top"
	sorted_objs = sorted(objs, key=lambda o: (o["bounds"]["top"], o["bounds"]["left"]))
	rows: List[List[Dict[str, Any]]] = []
	for o in sorted_objs:
		placed = False
		for r in rows:
			# Compare against row's representative top (use median of row tops)
			row_tops = [x["bounds"]["top"] for x in r]
			row_top_ref = median(row_tops, r[0]["bounds"]["top"])
			if abs(o["bounds"]["top"] - row_top_ref) <= row_tol:
				r.append(o); placed = True; break
		if not placed:
			rows.append([o])

	# sort each row by left
	for r in rows:
		r.sort(key=lambda o: o["bounds"]["left"])

	# compute gutters
	h_gaps = []
	for r in rows:
		for a, b in zip(r, r[1:]):
			h_gaps.append(b["bounds"]["left"] - a["bounds"]["right"])
	v_gaps = []
	for a, b in zip(rows, rows[1:]):
		# gap between closest edges vertically
		a_bot = max(x["bounds"]["bottom"] for x in a)
		b_top = min(x["bounds"]["top"] for x in b)
		v_gaps.append(b_top - a_bot)

	base_h_gutter = clamp(median(h_gaps, 16.0), 8.0, 28.0)
	base_v_gutter = clamp(median(v_gaps, 14.0), 6.0, 28.0)

	# ---------- merge rows into vertical sections ----------
	# If rows have strong horizontal overlap (width overlap >= 40% of min span),
	# treat them as belonging to the same section; otherwise start a new one.
	sections: List[List[List[Dict[str, Any]]]] = []
	for r in rows:
		r_left  = min(x["bounds"]["left"] for x in r)
		r_right = max(x["bounds"]["right"] for x in r)
		r_span  = (r_left, r_right)
		if not sections:
			sections.append([r]); continue
		# Compare to last section's span
		last = sections[-1]
		last_left  = min(min(x["bounds"]["left"] for x in row) for row in last)
		last_right = max(max(x["bounds"]["right"] for x in row) for row in last)
		last_span  = (last_left, last_right)
		overlap = horiz_overlap(r_span, last_span)
		min_span = min(r_right - r_left, last_right - last_left)
		if min_span <= 0:
			sections.append([r]); continue
		if (overlap / max(1.0, min_span)) >= 0.40:
			last.append(r)
		else:
			sections.append([r])

	# ---------- detect multi-column vs stacked in each section ----------
	# A section is "multi-column" if, within the section, there exist rows
	# that align as multiple side-by-side blocks with consistent gaps.
	# We approximate: if any row has 2+ items and avg gap >= 0.5*base_h_gutter.
	def is_multi_column(section_rows: List[List[Dict[str, Any]]]) -> bool:
		for r in section_rows:
			if len(r) >= 2:
				gaps = [r[i+1]["bounds"]["left"] - r[i]["bounds"]["right"] for i in range(len(r)-1)]
				if gaps and median(gaps, base_h_gutter) >= 0.5 * base_h_gutter:
					return True
		return False

	# ---------- HTML emitters ----------
	# Map objects to HTML fragments (minimal but semantically useful).
	def html_for_obj(o: Dict[str, Any]) -> str:
		t = o.get("type")
		txt = text_of(o)
		if t == "Text":
			return f'<div class="fmx-text" data-key="{o.get("key","")}">{escape_html(txt)}</div>'
		if t == "Field":
			fld = o.get("field") or {}
			label = escape_html(fld.get("name") or fld.get("qualified") or "")
			name_attr = escape_attr((fld.get("qualified") or fld.get("name") or "field").lower().replace(" ", "_"))
			return (
				'<label class="fmx-field" data-key="{key}">'
				'<span class="fmx-label">{label}</span>'
				'<input class="fmx-input" name="{name}" />'
				'</label>'
			).format(
				key=escape_attr(o.get("key","")),
				label=label,
				name=name_attr
			)
		if t == "Button":
			return f'<button class="fmx-button" data-key="{o.get("key","")}">{escape_html(txt) or "Button"}</button>'
		# Fallback
		return f'<div class="fmx-obj" data-key="{o.get("key","")}">{escape_html(txt)}</div>'

	def escape_html(s: Optional[str]) -> str:
		if s is None: return ""
		return (s.replace("&","&amp;")
				.replace("<","&lt;")
				.replace(">","&gt;"))

	def escape_attr(s: Optional[str]) -> str:
		return escape_html(s or "")

	# ---------- Build HTML ----------
	html_parts: List[str] = []
	debug: Dict[str, Any] = {"sections": []}

	for si, section_rows in enumerate(sections):
		multi = is_multi_column(section_rows)
		# flatten rows -> items (keep reading order)
		items = [o for r in section_rows for o in r]

		if multi:
			# Grid section: auto-fit columns, keep natural reading order
			html_parts.append(f'<section class="fmx-section fmx-grid" data-sec="{si}">')
			for o in items:
				html_parts.append(f'  <div class="fmx-cell">{html_for_obj(o)}</div>')
			html_parts.append('</section>')
		else:
			# Stacked section: preserve row boundaries
			html_parts.append(f'<section class="fmx-section fmx-stack" data-sec="{si}">')
			for ri, r in enumerate(section_rows):
				html_parts.append(f'  <div class="fmx-row" data-row="{ri}">')
				for o in r:
					html_parts.append(f'    <div class="fmx-cell">{html_for_obj(o)}</div>')
				html_parts.append('  </div>')
			html_parts.append('</section>')

		# debug block
		debug["sections"].append({
			"index": si,
			"multiColumn": multi,
			"rowCount": len(section_rows),
			"itemCount": len(items),
			"rows": [
				[{"key": obj.get("key"),
				"type": obj.get("type"),
				"bounds": obj.get("bounds")} for obj in r]
				for r in section_rows
			]
		})

	# ---------- CSS ----------
	# Scoped, minimal design system. Uses grid for multi-column sections,
	# and simple flowing rows for stacked sections. Spacing derived from layout.
	css = f"""
/* ===== FileMaker → Responsive layout (auto-generated) ===== */
.fmx-root {{
  --fmx-gutter-x: {int(base_h_gutter)}px;
  --fmx-gutter-y: {int(base_v_gutter)}px;
  --fmx-min-col: {int(min_col_width)}px;
  box-sizing: border-box;
  padding: var(--fmx-gutter-y) var(--fmx-gutter-x);
  display: block;
  max-width: min(1100px, 95vw);
  margin: 0 auto;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, Inter, Arial, sans-serif;
  line-height: 1.35;
}}

.fmx-section {{
  margin-bottom: calc(var(--fmx-gutter-y) * 1.25);
}}

.fmx-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(var(--fmx-min-col), 1fr));
  gap: var(--fmx-gutter-y) var(--fmx-gutter-x);
}}

.fmx-stack .fmx-row {{
  display: flex;
  flex-wrap: wrap;
  gap: var(--fmx-gutter-y) var(--fmx-gutter-x);
  margin-bottom: calc(var(--fmx-gutter-y) * 0.5);
}}

.fmx-cell {{
  min-width: min(100%, var(--fmx-min-col));
  flex: 1 1 var(--fmx-min-col);
}}

.fmx-text {{
  white-space: normal;
}}

.fmx-field {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.33rem;
  width: 100%;
}}

.fmx-label {{
  font-size: 0.9rem;
  color: #333;
}}

.fmx-input {{
  width: 100%;
  padding: 0.55rem 0.6rem;
  border: 1px solid #c6c6c6;
  border-radius: 6px;
  outline: none;
}

.fmx-input:focus {{
  border-color: #333;
  box-shadow: 0 0 0 2px rgba(0, 110, 255, 0.18);
}}

.fmx-button {{
  display: inline-block;
  width: 100%;
  padding: 0.6rem 0.8rem;
  border-radius: 6px;
  border: 1px solid #b4b4b4;
  background: linear-gradient(#fff, #f1f1f1);
  cursor: pointer;
  text-align: center;
}}

.fmx-button:hover {{
  filter: brightness(0.98);
}}

@media (max-width: 520px) {{
  .fmx-root {{
	--fmx-min-col: {int(max(160, min_col_width//1.5))}px;
  }}
}}
""".strip()

	# Wrap the sections in a root container
	html = '<div class="fmx-root">\n' + "\n".join(html_parts) + "\n</div>"

	return html, css, debug








'''



'''
















def action():
	_.isDataClip(__.appReg)
	xml = '\n'.join( _.isData(2) )

	if _.switches.isActive('Fields'):
		json_text = fm_fields_to_json(xml, pretty=True)
		_.pr(json_text)

	if _.switches.isActive('Scripts'):
		json_text = fm_scripts_to_json(xml, pretty=True)
		_.pr(json_text)

	if _.switches.isActive('Layouts'):
		if not _.switches.values('Layouts'):
			json_text = fm_layout_to_json(xml, pretty=True)
			_.pr(json_text)
			return
		else:
			json_text = fm_layout_to_json(xml, pretty=False)

		html, css, debug = layout_json_to_responsive_html(json_text)

		# If you want a single HTML blob you can drop into a page:
		full = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<style>{css}</style>
</head>
<body>
{html}
</body>
</html>"""


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)