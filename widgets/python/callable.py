import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
    _.switches.register( 'Callable', '--c,-fn,-class,-callable' )
    _.switches.register( 'First', '-first,-1,-one,-o' )
    _.switches.register( 'ColorSamples', '-sample' )
    _.switches.register( 'RefreshCache', '-r,-refresh' )
    _.switches.register( 'Save', '-save', 'file.ext' )
    # _.switches.register( 'ListKeys', '-k,-keys' )



_._default_settings_()

_.appInfo[focus()] = {
    'file': 'callable.py',
    'description': 'Function and class tool for JavaScript and Python.',
    'categories': [
                        'function',
                        'class',
                        'code',
                        'python',
                        'javascript',
                        'js',
                        'py',
                ],
    'examples': [
                        _.hp('p callable -f callable.py'),
                        _.hp('p callable -f base --c Switches | p inFunc'),
                        _.hp('p callable -f base --c Switches + def'),
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
    _.switches.trigger( 'Save', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start





# -*- coding: utf-8 -*-
import os
import sys
import re
import ast
import textwrap
from typing import Dict, Tuple, Optional

# ---------------------------
# Optional deps with graceful fallbacks
# ---------------------------
try:
    import esprima  # for JS parsing
except Exception:
    esprima = None

try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None


# ---------------------------
# Shims for your framework if not present
# ---------------------------
class _ShimV:
    slash = os.sep
    tt = os.path.join(os.path.expanduser('~'), '.callable_cache')

    @staticmethod
    def mkdir(path):
        os.makedirs(path, exist_ok=True)

class _Shim_:
    class Switches:
        def isActive(self, name): return False
        def value(self, name): return ''
        def values(self, name): return []
    switches = Switches()

    @staticmethod
    def getText(path, raw=False):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()

    @staticmethod
    def saveText(text, path):
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

    @staticmethod
    def saveTable(obj, path, p=0):
        import json
        _Shim_.saveText(json.dumps(obj, ensure_ascii=False, indent=2), path + '.json')

    @staticmethod
    def getTable(path):
        import json
        with open(path + '.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def md(path, val=None):
        # store/load a small stamp file; if val provided, write, else read
        stamp = path + '.mdstamp'
        if val is None:
            try:
                with open(stamp, 'r', encoding='utf-8') as f:
                    return f.read().strip()
            except Exception:
                return ''
        else:
            with open(stamp, 'w', encoding='utf-8') as f:
                f.write(val)
            return val

    @staticmethod
    def md5_string(s):
        import hashlib
        return hashlib.md5(s.encode('utf-8', errors='ignore')).hexdigest()

    @staticmethod
    def e(*args): print(*args, file=sys.stderr)
    @staticmethod
    def pr(*args, **kwargs): print(*args)
    @staticmethod
    def showLine(line): return True

    class CodeColor:
        def __init__(self, style=None): pass
        def color(self, text, language='python'): return text

    class RegID:
        @staticmethod
        def add(a,b,c): pass

# adopt user env if available
_ = globals().get('_', _Shim_)
_v = globals().get('_v', _ShimV)


class CallableExtractor:
    def __init__(self):
        self.Language = 'python'
        self.liked_styles = [
            'arduino','autumn','coffee','default','emacs','friendly',
            'github-dark','gruvbox-dark','lightbulb','manni','material',
            'monokai','one-dark','paraiso-dark','solarized-dark'
        ]

    # ---------------------------
    # Utilities
    # ---------------------------
    # @staticmethod
    # def strip_html_comments(html: str) -> str:
    # 	return re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # @staticmethod
    # def strip_php_blocks(code: str) -> str:
    # 	return re.sub(r'<\?(php)?[\s\S]*?\?>', "''", code, flags=re.IGNORECASE)

    # @staticmethod
    # def js_clean(code: str) -> str:
    # 	code = code.replace("''''", "''")
    # 	code = code.replace('?.(', '(').replace('?.[', '[')
    # 	data = []
    # 	for line in code.splitlines():
    # 		cl = line.strip().lower()
    # 		if cl == "''": continue
    # 		if cl.startswith('<'): continue
    # 		data.append(line)
    # 	return '\n'.join(data)

    # @staticmethod
    # def _language_from_ext(path: str) -> Optional[str]:
    # 	EXT_TO_LANG = {

    # 		# Python
    # 		'py': 'python',

    # 		# JavaScript / TypeScript
    # 		'js': 'javascript',
    # 		'mjs': 'javascript',
    # 		'cjs': 'javascript',
    # 		'ts': 'typescript',
    # 		'tsx': 'typescript',

    # 		# PHP / Web
    # 		'php': 'php',
    # 		'html': 'html',
    # 		'htm': 'html',
    # 		'vue': 'html',        # script blocks
    # 		'svelte': 'html',

    # 		# Shell
    # 		'sh': 'shell',
    # 		'bash': 'shell',
    # 		'zsh': 'shell',

    # 		# Go
    # 		'go': 'go',

    # 		# Rust
    # 		'rs': 'rust',

    # 		# C / C++
    # 		'c': 'c',
    # 		'h': 'c',
    # 		'cpp': 'cpp',
    # 		'cc': 'cpp',
    # 		'cxx': 'cpp',
    # 		'hpp': 'cpp',

    # 		# Java / C#
    # 		'java': 'java',
    # 		'cs': 'csharp',

    # 		# Misc
    # 		'lua': 'lua',
    # 		'rb': 'ruby',
    # 	}

    # 	ext = os.path.splitext(path)[1].lower().lstrip('.')
    # 	return EXT_TO_LANG.get(ext)


    # ---------------------------
    # HTML/JS extractors
    # ---------------------------
    # def extract_javascript(self, code: str) -> str:
    # 	lines = code.splitlines()
    # 	inside_script = False
    # 	js_code = ''
    # 	for line in lines:
    # 		stripped = line.strip().lower()
    # 		if not inside_script and stripped.startswith('<script'):
    # 			inside_script = True
    # 			continue
    # 		if inside_script:
    # 			if stripped.startswith('</script'):
    # 				inside_script = False
    # 				continue
    # 			js_code += line + '\r\n'
    # 	return js_code

    # def extract_javascript_from_html(self, html: str) -> str:
    # 	if not BeautifulSoup:
    # 		return self.extract_javascript(html)
    # 	soup = BeautifulSoup(html, "html.parser")
    # 	js_blocks = []
    # 	for script in soup.find_all("script"):
    # 		if script.string:
    # 			js_blocks.append(script.string.strip())
    # 	# inline handlers
    # 	for tag in soup.find_all(True):
    # 		for attr, value in tag.attrs.items():
    # 			if attr.startswith("on") and isinstance(value, str):
    # 				js_blocks.append(value.strip())
    # 	return "\n\n\n".join(js_blocks)

    # def extract_javascript_from_html_scripts_only(self, html: str) -> str:
    # 	if not BeautifulSoup:
    # 		return self.extract_javascript(html)
    # 	soup = BeautifulSoup(html, "html.parser")
    # 	js_blocks = []
    # 	for script in soup.find_all("script"):
    # 		if script.string:
    # 			js_blocks.append(script.string.strip())
    # 	return "\n\n\n".join(js_blocks)

    # ---------------------------
    # JS namespaced assignments
    # ---------------------------
    # def js_extract_namespaced_assignments(self, code: str) -> dict:
    # 	"""
    # 	Extract namespaced assignments from JavaScript code (e.g., _.note.manager.action = ..., or
    # 	_.note.manager = { init(){}, project:{ select(){} } } ), expanding nested properties.

    # 	Returns:
    # 		dict: { '_.note.manager.action': 'function or value source', ... }
    # 	"""
    # 	import esprima

    # 	def sanitize_js(js_code: str) -> str:
    # 		return (
    # 			js_code
    # 			.replace('??', '||')  # nullish coalescing -> OR
    # 			.replace('?.', '.')   # optional chaining -> normal dot
    # 		)

    # 	def extract_full_path(node):
    # 		parts = []
    # 		while getattr(node, 'type', None) == 'MemberExpression':
    # 			prop = node.property
    # 			if hasattr(prop, 'name') and prop.name is not None:
    # 				name = prop.name
    # 			elif hasattr(prop, 'value'):
    # 				name = str(prop.value)
    # 			else:
    # 				name = '[unknown]'
    # 			parts.insert(0, name)
    # 			node = node.object
    # 		if getattr(node, 'type', None) == 'Identifier':
    # 			parts.insert(0, node.name)
    # 		elif hasattr(node, 'name') and node.name:
    # 			parts.insert(0, node.name)
    # 		else:
    # 			parts.insert(0, '[root]')
    # 		return '.'.join(p for p in parts if p)

    # 	code = sanitize_js(code)
    # 	try:
    # 		tree = esprima.parseScript(code, {'range': True})
    # 	except Exception as e:
    # 		print(f"[js_extract_namespaced_assignments] Parse error: {e}")
    # 		return {}

    # 	assignments = {}

    # 	def add_slice(path, node):
    # 		if hasattr(node, 'range') and node.range:
    # 			start, end = node.range
    # 			assignments[path] = code[start:end]

    # 	def walk_object(base: str, obj_node):
    # 		# Expand object literal: base.prop -> value (recursively)
    # 		for prop in obj_node.properties:
    # 			# Determine property name
    # 			if prop.key.type == 'Identifier':
    # 				prop_name = prop.key.name
    # 			elif prop.key.type == 'Literal':
    # 				prop_name = str(prop.key.value)
    # 			else:
    # 				prop_name = '[unknown]'
    # 			full_path = f"{base}.{prop_name}"

    # 			val = prop.value
    # 			# Grab the exact source for this property value
    # 			add_slice(full_path, val)

    # 			# Recurse if nested object
    # 			if getattr(val, 'type', None) == 'ObjectExpression':
    # 				walk_object(full_path, val)

    # 	def walk(node):
    # 		if isinstance(node, list):
    # 			for item in node:
    # 				walk(item)
    # 			return

    # 		if not hasattr(node, 'type'):
    # 			return

    # 		# Top-level statements
    # 		if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
    # 			walk(node.expression)

    # 		elif node.type == 'AssignmentExpression':
    # 			left = node.left
    # 			right = node.right
    # 			if getattr(left, 'type', None) == 'MemberExpression':
    # 				# Always record the RHS slice for the whole assignment
    # 				full_path = extract_full_path(left)
    # 				add_slice(full_path, right)

    # 				# NEW: if assigning an object literal, expand its nested properties
    # 				if getattr(right, 'type', None) == 'ObjectExpression':
    # 					walk_object(full_path, right)

    # 		elif node.type == 'VariableDeclaration':
    # 			# Handle `const foo = { ... }` then foo.bar...
    # 			for decl in node.declarations or []:
    # 				if decl.init and decl.init.type == 'ObjectExpression' and decl.id.type == 'Identifier':
    # 					base = decl.id.name
    # 					# Record the top-level object literal itself
    # 					add_slice(base, decl.init)
    # 					walk_object(base, decl.init)

    # 		# Continue walking child nodes
    # 		for key in dir(node):
    # 			if key.startswith('_') or key in ('type', 'range', 'loc'):
    # 				continue
    # 			value = getattr(node, key)
    # 			if isinstance(value, list) or (hasattr(value, 'type') and value.type):
    # 				walk(value)

    # 	walk(tree.body)
    # 	return assignments



    def js_extract_namespaced_assignments2(self, code: str) -> dict:
        if not esprima:
            return {}  # no parser available
        def sanitize_js(js_code: str) -> str:
            return js_code.replace('??', '||').replace('?.', '.')
        code = sanitize_js(code)
        try:
            tree = esprima.parseScript(code, {'range': True})
        except Exception:
            return {}

        assignments = {}

        def extract_full_path(node):
            parts = []
            while getattr(node, 'type', None) == 'MemberExpression':
                prop = node.property
                name = getattr(prop, 'name', None)
                if name is None and hasattr(prop, 'value'):
                    name = str(prop.value)
                parts.insert(0, name if name is not None else '[unknown]')
                node = node.object
            if getattr(node, 'type', None) == 'Identifier':
                parts.insert(0, node.name)
            elif hasattr(node, 'name') and node.name:
                parts.insert(0, node.name)
            else:
                parts.insert(0, '[root]')
            return '.'.join(p for p in parts if p)

        def walk(node):
            if isinstance(node, list):
                for item in node:
                    walk(item)
                return
            if not hasattr(node, 'type'): return

            if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
                walk(node.expression)

            elif node.type == 'AssignmentExpression':
                left = node.left
                right = node.right
                if getattr(left, 'type', '') == 'MemberExpression' and hasattr(right, 'range'):
                    full_path = extract_full_path(left)
                    start, end = right.range
                    assignments[full_path] = code[start:end]

            elif node.type == 'VariableDeclaration':
                for decl in node.declarations:
                    if decl.init and decl.init.type == 'ObjectExpression':
                        walk_object(decl.id.name, decl.init)

            for key in dir(node):
                if key.startswith('_') or key in ('type', 'range', 'loc'): continue
                value = getattr(node, key)
                if isinstance(value, (list,)) or (hasattr(value, 'type') and value.type):
                    walk(value)

        def walk_object(base: str, obj_node):
            for prop in obj_node.properties:
                if prop.key.type == 'Identifier':
                    prop_name = prop.key.name
                elif prop.key.type == 'Literal':
                    prop_name = str(prop.key.value)
                else:
                    prop_name = '[unknown]'
                full_path = f"{base}.{prop_name}"
                if hasattr(prop.value, 'range'):
                    start, end = prop.value.range
                    assignments[full_path] = code[start:end]
                if prop.value.type == 'ObjectExpression':
                    walk_object(full_path, prop.value)

        walk(tree.body)
        return assignments

    # ---------------------------
    # Python extractor
    # ---------------------------
    def py_extract_top_level_callables(self, source_code: str) -> dict:
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        result = {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}

        def slice_by_lines(start_lineno: int, end_lineno: Optional[int]) -> str:
            start = start_lineno - 1
            if end_lineno is None:
                end = start + 1
                while end < len(lines) and (lines[end].startswith((' ', '\t')) or not lines[end].strip()):
                    end += 1
            else:
                end = end_lineno
            raw = '\n'.join(lines[start:end])
            return textwrap.dedent(raw)

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                name = node.name
                code = slice_by_lines(node.lineno, getattr(node, 'end_lineno', None))
                result['def'][name] = code
                result['flat'][name] = code

            elif isinstance(node, ast.ClassDef):
                cname = node.name
                class_code = slice_by_lines(node.lineno, getattr(node, 'end_lineno', None))
                result['class'][cname] = class_code
                result['flat'][cname] = class_code

                for sub in node.body:
                    if isinstance(sub, ast.FunctionDef):
                        mname = sub.name
                        mcode = slice_by_lines(sub.lineno, getattr(sub, 'end_lineno', None))
                        for key in (f'{cname}.{mname}', f'{cname}::{mname}'):
                            result['class_methods'][key] = mcode
                            result['flat'][key] = mcode
        return result

    # ---------------------------
    # PHP extractor (lightweight)
    # ---------------------------
    _PHP_IDENT = re.compile(r'[A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*', re.UNICODE)

    # def _php_segments_only(self, code: str) -> str:
    # 	out, i, n = [], 0, len(code)
    # 	while i < n:
    # 		start = code.find('<?', i)
    # 		if start < 0:
    # 			if not out and i == 0 and code.strip():
    # 				return code  # pure PHP file
    # 			break
    # 		endtag = code.find('?>', start)
    # 		segment = code[start+2:] if endtag < 0 else code[start+2:endtag]
    # 		if segment.lstrip().startswith('php'):
    # 			segment = segment.lstrip()[3:]
    # 		out.append(segment)
    # 		i = n if endtag < 0 else endtag + 2
    # 	return '\n'.join(out) if out else ''


    # def php_extract_callables(self, source: str) -> dict:
    # 	import sys, re

    # 	def log(msg):
    # 		pass
    # 		# print(f"[php_extract] {msg}", file=sys.stderr)

    # 	code = self._php_segments_only(source)
    # 	result = {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}
    # 	if not code.strip():
    # 		log("no code after _php_segments_only")
    # 		return result

    # 	log(f"code length={len(code)}")

    # 	# ---------------------------
    # 	# Build a MASKED copy with SAME LENGTH as code:
    # 	# replace contents of strings/comments with spaces so { } in them don't affect scans,
    # 	# but all positions still match the original 'code'.
    # 	# ---------------------------
    # 	n = len(code)
    # 	i = 0
    # 	out = []
    # 	while i < n:
    # 		ch = code[i]

    # 		# line comment //... or #
    # 		if code.startswith('//', i) or (ch == '#' and (i == 0 or code[i-1] != '$')):
    # 			j = code.find('\n', i)
    # 			if j == -1:
    # 				out.append(' ' * (n - i))
    # 				i = n
    # 				break
    # 			out.append(' ' * (j - i))
    # 			out.append('\n')
    # 			i = j + 1
    # 			continue

    # 		# block comment /* ... */
    # 		if code.startswith('/*', i):
    # 			j = code.find('*/', i + 2)
    # 			if j == -1:
    # 				out.append(' ' * (n - i))
    # 				i = n
    # 				break
    # 			out.append(' ' * (j + 2 - i))
    # 			i = j + 2
    # 			continue

    # 		# single or double quoted strings
    # 		if ch in ("'", '"'):
    # 			q = ch
    # 			j = i + 1
    # 			while j < n:
    # 				if code[j] == '\\':
    # 					j += 2
    # 					continue
    # 				if code[j] == q:
    # 					j += 1
    # 					break
    # 				j += 1
    # 			# keep quotes, space out inside
    # 			out.append(q)
    # 			inner_len = max(0, (j - i - 2))
    # 			if inner_len:
    # 				out.append(' ' * inner_len)
    # 			out.append(q if j <= n else '')
    # 			i = j
    # 			continue

    # 		# default: copy char
    # 		out.append(ch)
    # 		i += 1

    # 	masked = ''.join(out)
    # 	log(f"masked length={len(masked)}")

    # 	# Helper: safe brace walk on MASKED (returns end index or EOF)
    # 	def find_matching_brace(start_idx: int) -> int:
    # 		depth = 1
    # 		j = start_idx + 1
    # 		steps = 0
    # 		MAX_STEPS = 10_000_000  # guard
    # 		while j < len(masked) and depth > 0:
    # 			c = masked[j]
    # 			if c == '{':
    # 				depth += 1
    # 			elif c == '}':
    # 				depth -= 1
    # 			j += 1
    # 			steps += 1
    # 			if steps > MAX_STEPS:
    # 				log(f"brace-walk guard hit at {j}, breaking")
    # 				break
    # 		return min(j, len(masked))

    # 	# ---------------------------
    # 	# 1) Find class/interface/trait/enum blocks on MASKED
    # 	# ---------------------------
    # 	class_pat = re.compile(
    # 		r'\b(class|interface|trait|enum)\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\b[^{;]*\{',
    # 		re.IGNORECASE
    # 	)

    # 	spans = []
    # 	for m in class_pat.finditer(masked):
    # 		kind, cname = m.group(1), m.group(2)
    # 		open_brace_pos = masked.find('{', m.start())
    # 		if open_brace_pos == -1:
    # 			log(f"{kind} {cname}: no opening brace, skipping")
    # 			continue
    # 		end = find_matching_brace(open_brace_pos)
    # 		log(f"found {kind} {cname} at {m.start()}..{end}")
    # 		class_src = code[m.start(): end]  # slice from ORIGINAL using aligned indices
    # 		result['class'][cname] = class_src
    # 		result['flat'][cname] = class_src
    # 		spans.append((cname, m.start(), end))

    # 	# ---------------------------
    # 	# 2) Methods inside each class (search MASKED slice for 'function name(')
    # 	# ---------------------------
    # 	fn_in_class_pat = re.compile(r'\bfunction\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\s*\(')

    # 	for cname, s, e in spans:
    # 		inner_masked = masked[s:e]
    # 		inner_off = s
    # 		log(f"scan methods in {cname}: slice={s}-{e} (len={len(inner_masked)})")
    # 		for fm in fn_in_class_pat.finditer(inner_masked):
    # 			mname = fm.group(1)
    # 			# find body or ';'
    # 			after = inner_masked[fm.end():]
    # 			rel = fm.end()
    # 			ob = after.find('{')
    # 			sc = after.find(';')

    # 			if ob != -1 and (sc == -1 or ob < sc):
    # 				open_pos = inner_off + rel + ob
    # 				end = find_matching_brace(open_pos)
    # 				msrc = code[inner_off + fm.start(): end]
    # 				log(f"method {cname}.{mname}: body {inner_off+fm.start()}..{end} (len={len(msrc)})")
    # 			else:
    # 				semi_pos = masked.find(';', inner_off + fm.start())
    # 				if semi_pos == -1:
    # 					semi_pos = inner_off + fm.start() + len('function ' + mname)
    # 				msrc = code[inner_off + fm.start(): semi_pos + 1]
    # 				log(f"method {cname}.{mname}: signature {inner_off+fm.start()}..{semi_pos+1}")

    # 			for key in (f'{cname}.{mname}', f'{cname}::{mname}'):
    # 				result['class_methods'][key] = msrc
    # 				result['flat'][key] = msrc

    # 	# ---------------------------
    # 	# 3) Top-level functions (MULTILINE on MASKED)
    # 	# ---------------------------
    # 	top_fn_pat = re.compile(
    # 		r'(?m)^\s*\bfunction\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\s*\('
    # 	)
    # 	log("scan top-level functions")
    # 	for fm in top_fn_pat.finditer(masked):
    # 		fname = fm.group(1)
    # 		log(f"found function {fname} at {fm.start()}")
    # 		# find body or ';'
    # 		after = masked[fm.end():]
    # 		rel = fm.end()
    # 		ob = after.find('{')
    # 		sc = after.find(';')

    # 		if ob != -1 and (sc == -1 or ob < sc):
    # 			open_pos = rel + ob
    # 			open_pos_abs = open_pos + 0  # relative to start of masked
    # 			open_pos_abs = fm.end() + ob
    # 			end = find_matching_brace(open_pos_abs)
    # 			msrc = code[fm.start(): end]
    # 			log(f"function {fname}: body {fm.start()}..{end} (len={len(msrc)})")
    # 		else:
    # 			semi_pos = masked.find(';', fm.start())
    # 			if semi_pos == -1:
    # 				semi_pos = fm.start() + len('function ' + fname)
    # 			msrc = code[fm.start(): semi_pos + 1]
    # 			log(f"function {fname}: signature {fm.start()}..{semi_pos+1}")

    # 		result['def'][fname] = msrc
    # 		result['flat'][fname] = msrc

    # 	log("done")
    # 	return result


    def php_extract_callables2(self, source: str) -> dict:
        """
        Returns same shape as Python extractor:
        { 'def': {...}, 'class': {...}, 'class_methods': {...}, 'flat': {...} }
        """
        import re, sys
        print("[php_extract_callables] start", file=sys.stderr)
        code = self._php_segments_only(source)
        result = {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}
        if not code.strip():
            print("[php_extract_callables] no code after _php_segments_only", file=sys.stderr)
            return result

        # Remove comments and strings for structure scanning (keep indexes approximate)
        def strip_comments_strings(s: str) -> str:
            s = re.sub(r'//.*?$|#.*?$', '', s, flags=re.MULTILINE)
            s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
            s = re.sub(r"(?s)'(?:\\.|[^\\'])*'", "''", s)
            s = re.sub(r'(?s)"(?:\\.|[^\\"])*"', '""', s)
            return s

        rough = strip_comments_strings(code)
        print(f"[php_extract_callables] stripped length={len(rough)}", file=sys.stderr)

        # Find class blocks
        class_iter = re.finditer(
            r'\b(class|interface|trait|enum)\s+(' + self._PHP_IDENT.pattern + r')\b[^{;]*\{',
            rough, flags=re.IGNORECASE
        )

        spans = []
        for m in class_iter:
            kind, cname = m.group(1), m.group(2)
            print(f"[php_extract_callables] found {kind} {cname}", file=sys.stderr)
            start = m.end()  # at '{'
            # find matching closing brace by manual walk
            depth = 1
            j = start
            n = len(rough)
            while j < n and depth > 0:
                if rough[j] == '{':
                    depth += 1
                elif rough[j] == '}':
                    depth -= 1
                j += 1
            end = j
            print(f"[php_extract_callables] class {cname} span {start}-{end}", file=sys.stderr)
            class_src = code[m.start(): end]  # slice from original code for exact output
            result['class'][cname] = class_src
            result['flat'][cname] = class_src
            spans.append((cname, start, end))

        # Extract methods inside each class span
        for cname, s, e in spans:
            inner = code[s:e]
            print(f"[php_extract_callables] scanning methods in {cname}, length={len(inner)}", file=sys.stderr)
            for fm in re.finditer(
                r'\bfunction\s+(' + self._PHP_IDENT.pattern + r')\s*\(', inner
            ):
                mname = fm.group(1)
                print(f"[php_extract_callables] found method {cname}.{mname}", file=sys.stderr)
                body_start = fm.end()
                tail = inner[body_start:]
                brace_idx = tail.find('{')
                semi_idx = tail.find(';')
                if brace_idx != -1 and (semi_idx == -1 or brace_idx < semi_idx):
                    off = body_start + brace_idx
                    depth = 1
                    j = off + 1
                    n2 = len(code)
                    while j < n2 and depth > 0:
                        if code[j] == '{':
                            depth += 1
                        elif code[j] == '}':
                            depth -= 1
                        j += 1
                    msrc = code[fm.start()+s: j]
                    print(f"[php_extract_callables] captured body of {cname}.{mname}, len={len(msrc)}", file=sys.stderr)
                else:
                    semi_global = code.find(';', fm.start()+s)
                    if semi_global == -1: semi_global = fm.start()+s+len('function ' + mname)
                    msrc = code[fm.start()+s: semi_global+1]
                    print(f"[php_extract_callables] captured signature of {cname}.{mname}", file=sys.stderr)

                for key in (f'{cname}.{mname}', f'{cname}::{mname}'):
                    result['class_methods'][key] = msrc
                    result['flat'][key] = msrc

        # Top-level functions
        print("[php_extract_callables] scanning top-level functions", file=sys.stderr)
        for fm in re.finditer(
            r'(?m)^\s*(?:#[^\n]*\n|//[^\n]*\n|\s*)*\bfunction\s+(' + self._PHP_IDENT.pattern + r')\s*\(',
            rough
        ):
            fname = fm.group(1)
            print(f"[php_extract_callables] found function {fname}", file=sys.stderr)
            body_start = fm.end()
            tail = rough[body_start:]
            brace_idx = tail.find('{')
            semi_idx = tail.find(';')
            if brace_idx != -1 and (semi_idx == -1 or brace_idx < semi_idx):
                off = body_start + brace_idx
                depth = 1
                j = off + 1
                n2 = len(rough)
                while j < n2 and depth > 0:
                    if rough[j] == '{':
                        depth += 1
                    elif rough[j] == '}':
                        depth -= 1
                    j += 1
                msrc = code[fm.start(): j]
                print(f"[php_extract_callables] captured body of function {fname}, len={len(msrc)}", file=sys.stderr)
            else:
                semi_global = code.find(';', fm.start())
                if semi_global == -1: semi_global = fm.start()+len('function ' + fname)
                msrc = code[fm.start(): semi_global+1]
                print(f"[php_extract_callables] captured signature of function {fname}", file=sys.stderr)

            result['def'][fname] = msrc
            result['flat'][fname] = msrc

        print("[php_extract_callables] done", file=sys.stderr)
        return result


    # ---------------------------
    # Orchestrator
    # ---------------------------
    # def extract_callables(self, data: str, language: Optional[str]) -> Tuple[dict, str]:
    # 	lang = (language or '').lower()

    # 	# import sys; print(language); sys.exit(0)

    # 	if lang == 'javascript':
    # 		data = self.js_clean(data)
    # 		if data:
    # 			return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': self.js_extract_namespaced_assignments(data)}, 'javascript'
    # 		else:
    # 			return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}, 'javascript'


    # 	# Auto-detect minimal: if contains <script> or </script>, treat as HTML
    # 	elif not lang:
    # 		if '<script' in data.lower() and '</script' in data.lower():
    # 			lang = 'html'
    # 		else:
    # 			lang = 'python'  # default

    # 	elif lang in ('htm','html'):
    # 		# Only <script> blocks, then sanitize for PHP if needed
    # 		data = self.extract_javascript_from_html_scripts_only(data)
    # 		data = data.replace('\r','').replace('\n\n','\n')
    # 		lang = 'javascript'  # analyze JS extracted from HTML

    # 	elif lang == 'php':
    # 		# sometimes PHP files embed HTML/JS; we only want PHP segments for callable extraction
    # 		# JS extraction in PHP HTML is separate flow; here we focus on PHP callables
    # 		return self.php_extract_callables(data), 'php'


    # 	# python
    # 	return self.py_extract_top_level_callables(data), 'python'

    # @staticmethod
    # def get_callable(extracted: dict, key: str) -> Optional[str]:
    # 	if not extracted: return None
    # 	# prioritize exact flat match
    # 	if 'flat' in extracted and key in extracted['flat']:
    # 		return extracted['flat'][key]
    # 	# allow ClassName.functionName with either '.' or '::'
    # 	if 'class_methods' in extracted:
    # 		if key in extracted['class_methods']:
    # 			return extracted['class_methods'][key]
    # 		alt = key.replace('::','.') if '::' in key else key.replace('.', '::')
    # 		return extracted['class_methods'].get(alt)
    # 	# fallback to def / class
    # 	if key in extracted.get('def', {}): return extracted['def'][key]
    # 	if key in extracted.get('class', {}): return extracted['class'][key]
    # 	return None

    # ---------------------------
    # High-level: getData() (file-driven)
    def getData(self) -> Tuple[object, dict]:
        global _
        relevant = 'error'
        callable_key = _.switches.value('Callable')
        extracted = {}

        for path in _.isData(2) if hasattr(_, 'isData') else []:
            data = _.getText(path, raw=True)

            # Decide language from extension
            ext = os.path.splitext(path)[1].lower().lstrip('.')
            language = {
                'py': 'python',
                'js': 'javascript',
                'php': 'php',
                'htm': 'html',
                'html': 'html',
            }.get(ext, None)
            # import sys; print(language); sys.exit(0)

            # Extract
            # extracted, detected_language = self.extract_callables(data, language or 'python')
            extracted, detected_language = self.extract_callables(data, language)


            if not callable_key:
                relevant = extracted
            else:
                relevant = self.get_callable(extracted, callable_key) or '<error>'

        return relevant, extracted






    # ---------------------------
    # action() — same flow, with updates
    # ---------------------------
    def action(self):
        global _
        # ColorSamples quick feature preserved
        if _.switches.isActive('ColorSamples'):
            sample_python = "class A:\n    def x(self):\n        pass\n"
            sample_js = "class A { x(){ return 1; } }\n"
            like = []
            for style in self.liked_styles:
                codeColor = _.CodeColor(style)
                print(codeColor.color(sample_python, 'python'))
                print(codeColor.color(sample_js, 'javascript'))
                _.pr()
                _.pr(style, c='green')
                _.pr()
                _.pr(line=1)
                ask = input(': ')
                if ask.lower() in ['y', 'yes']:
                    like.append(style)
            _.pr('\nYou liked:')
            for item in like:
                _.pr(item)
            return

        valid = _.switches.isActive('Callable')

        # ------------- CACHE -------------
        thePath = _v.tt + _v.slash + 'Callable' + _v.slash
        try:
            theFile = _.switches.values('Files')[0]
        except Exception:
            _.e('No input file provided.')
            return

        if not os.path.isfile(theFile):
            _.e('File not found:', theFile)
            return

        _v.mkdir(thePath)
        file_key = _.md5_string(theFile)
        table_path = 'Callable' + _v.slash + file_key  # where _.saveTable/_.getTable read/write
        stamp_path = thePath + file_key                 # where _.md reads/writes the mtime stamp

        # Cache is valid if stored stamp equals current file mtime
        CACHE = False
        try:
            cached_stamp = _.md(stamp_path)         # read stored mtime string
            current_stamp = _.md(theFile)           # read current mtime string
            CACHE = (cached_stamp == current_stamp) and os.path.isfile(table_path + '.json')
        except Exception:
            CACHE = False

        isCACHE = False
        relevant = None
        callables = None

        if not CACHE:
            # fresh parse
            relevant, callables = self.getData()
            _.saveTable(callables, table_path, p=0)

            # write fresh stamp with current file mtime (string your When.parse understands)
            try:
                current_stamp = _.md(theFile)
                _.md(stamp_path, current_stamp)
            except Exception as e:
                _.e('Stamp write error:', e)

        else:
            _v.mkdir(thePath)
            try:
                callables = _.getTable(table_path)
            except Exception:
                callables = None

            if not callables:
                relevant, callables = self.getData()
                _.saveTable(callables, table_path, p=0)
                try:
                    current_stamp = _.md(theFile)
                    _.md(stamp_path, current_stamp)
                except Exception as e:
                    _.e('Stamp write error:', e)
            else:
                isCACHE = _.pr('\n\n  Cache', p=0)

        if relevant is None:
            if not valid:
                relevant = callables
            else:
                relevant = self.get_callable(callables, _.switches.value('Callable'))

        if not relevant:
            _.e('No callable found')
            return

        # Print list if not selecting a specific callable
        if not valid and isinstance(relevant, dict):
            keys = list(relevant.get('flat', {}).keys()) or list(relevant.keys())
            for k in keys:
                _.pr(k)
            return

        # Language selection for colorizer
        if theFile.lower().endswith('.py'):
            self.Language = 'python'
        elif theFile.lower().endswith('.js'):
            self.Language = 'javascript'
        elif theFile.lower().endswith('.php'):
            self.Language = 'php'
        elif theFile.lower().endswith('.html'):
            self.Language = 'html'
        elif theFile.lower().endswith('.css'):
            self.Language = 'css'

        # Save if requested
        if valid and _.switches.isActive('Save'):
            _.saveText(relevant, _.switches.value('Save'))
            return

        # Display with color
        def display():
            codeColor = _.CodeColor()
            text = relevant
            if not _.switches.isActive('NoColor'):
                if self.Language == 'php':
                    lan = 'javascript'
                else:
                    lan = self.Language
                text = codeColor.color(text, lan)
            lines_color = text.splitlines()
            lines_raw = relevant.splitlines()

            firstText = False
            isClass = False
            print('')
            for i, line in enumerate(lines_raw):
                if not firstText and not line.strip():
                    continue
                if _.showLine(line):
                    if line.lstrip().startswith('class '):
                        isClass = True
                    print(lines_color[i] if i < len(lines_color) else line)
                    if line.strip():
                        firstText = True
                    # if isClass and _.switches.isActive('First') and line.strip().startswith(('def ', 'function ')):
                    if _.switches.isActive('First'):
                        return

        if valid and isinstance(relevant, str):
            display()


# ---------------------------
# If you wire this into your CLI, call:
# CallableExtractor().action()
# ---------------------------











#############################################################################################################
# class CallableExtractor:
#     def __init__(self):
#         self.Language = 'python'
#         self.liked_styles = [
#             'arduino','autumn','coffee','default','emacs','friendly',
#             'github-dark','gruvbox-dark','lightbulb','manni','material',
#             'monokai','one-dark','paraiso-dark','solarized-dark'
#         ]

    # ---------------------------
    # Utilities
    # ---------------------------
    @staticmethod
    def strip_html_comments(html: str) -> str:
        return re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    @staticmethod
    def strip_php_blocks(code: str) -> str:
        return re.sub(r'<\?(php)?[\s\S]*?\?>', "''", code, flags=re.IGNORECASE)

    @staticmethod
    def js_clean(code: str) -> str:
        code = code.replace("''''", "''")
        code = code.replace('?.(', '(').replace('?.[', '[')
        data = []
        for line in code.splitlines():
            cl = line.strip().lower()
            if cl == "''":
                continue
            if cl.startswith('<'):
                continue
            data.append(line)
        return '\n'.join(data)

    @staticmethod
    def _language_from_ext(path: str) -> Optional[str]:
        EXT_TO_LANG = {
            # Python
            'py': 'python',

            # JavaScript / TypeScript
            'js': 'javascript',
            'mjs': 'javascript',
            'cjs': 'javascript',
            'ts': 'typescript',
            'tsx': 'typescript',

            # PHP / Web (containers)
            'php': 'php',
            'html': 'html',
            'htm': 'html',
            'vue': 'html',
            'svelte': 'html',

            # Shell
            'sh': 'shell',
            'bash': 'shell',
            'zsh': 'shell',

            # Go
            'go': 'go',

            # Rust
            'rs': 'rust',

            # C / C++
            'c': 'c',
            'h': 'c',
            'cpp': 'cpp',
            'cc': 'cpp',
            'cxx': 'cpp',
            'hpp': 'cpp',

            # Java / C#
            'java': 'java',
            'cs': 'csharp',

            # Misc
            'lua': 'lua',
            'rb': 'ruby',
        }
        ext = os.path.splitext(path)[1].lower().lstrip('.')
        return EXT_TO_LANG.get(ext)

    # ---------------------------
    # HTML/JS extractors
    # ---------------------------
    def extract_javascript(self, code: str) -> str:
        lines = code.splitlines()
        inside_script = False
        js_code = ''
        for line in lines:
            stripped = line.strip().lower()
            if not inside_script and stripped.startswith('<script'):
                inside_script = True
                continue
            if inside_script:
                if stripped.startswith('</script'):
                    inside_script = False
                    continue
                js_code += line + '\r\n'
        return js_code

    def extract_javascript_from_html(self, html: str) -> str:
        if not BeautifulSoup:
            return self.extract_javascript(html)
        soup = BeautifulSoup(html, "html.parser")
        js_blocks = []
        for script in soup.find_all("script"):
            if script.string:
                js_blocks.append(script.string.strip())
        # inline handlers
        for tag in soup.find_all(True):
            for attr, value in tag.attrs.items():
                if attr.startswith("on") and isinstance(value, str):
                    js_blocks.append(value.strip())
        return "\n\n\n".join(js_blocks)

    def extract_javascript_from_html_scripts_only(self, html: str) -> str:
        if not BeautifulSoup:
            return self.extract_javascript(html)
        soup = BeautifulSoup(html, "html.parser")
        js_blocks = []
        for script in soup.find_all("script"):
            if script.string:
                js_blocks.append(script.string.strip())
        return "\n\n\n".join(js_blocks)

    # ---------------------------
    # JS namespaced assignments
    # ---------------------------
    def js_extract_namespaced_assignments(self, code: str) -> dict:
        """
        Extract namespaced assignments from JavaScript code (e.g., _.note.manager.action = ..., or
        _.note.manager = { init(){}, project:{ select(){} } } ), expanding nested properties.

        Returns:
            dict: { '_.note.manager.action': 'function or value source', ... }
        """
        import esprima

        def sanitize_js(js_code: str) -> str:
            return (
                js_code
                .replace('??', '||')  # nullish coalescing -> OR
                .replace('?.', '.')   # optional chaining -> normal dot
            )

        def extract_full_path(node):
            parts = []
            while getattr(node, 'type', None) == 'MemberExpression':
                prop = node.property
                if hasattr(prop, 'name') and prop.name is not None:
                    name = prop.name
                elif hasattr(prop, 'value'):
                    name = str(prop.value)
                else:
                    name = '[unknown]'
                parts.insert(0, name)
                node = node.object
            if getattr(node, 'type', None) == 'Identifier':
                parts.insert(0, node.name)
            elif hasattr(node, 'name') and node.name:
                parts.insert(0, node.name)
            else:
                parts.insert(0, '[root]')
            return '.'.join(p for p in parts if p)

        code = sanitize_js(code)
        try:
            tree = esprima.parseScript(code, {'range': True})
        except Exception:
            return {}

        assignments = {}

        def add_slice(path, node):
            if hasattr(node, 'range') and node.range:
                start, end = node.range
                assignments[path] = code[start:end]

        def walk_object(base: str, obj_node):
            for prop in obj_node.properties:
                if prop.key.type == 'Identifier':
                    prop_name = prop.key.name
                elif prop.key.type == 'Literal':
                    prop_name = str(prop.key.value)
                else:
                    prop_name = '[unknown]'
                full_path = f"{base}.{prop_name}"

                val = prop.value
                add_slice(full_path, val)

                if getattr(val, 'type', None) == 'ObjectExpression':
                    walk_object(full_path, val)

        def walk(node):
            if isinstance(node, list):
                for item in node:
                    walk(item)
                return
            if not hasattr(node, 'type'):
                return

            if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
                walk(node.expression)

            elif node.type == 'AssignmentExpression':
                left = node.left
                right = node.right
                if getattr(left, 'type', None) == 'MemberExpression':
                    full_path = extract_full_path(left)
                    add_slice(full_path, right)
                    if getattr(right, 'type', None) == 'ObjectExpression':
                        walk_object(full_path, right)

            elif node.type == 'VariableDeclaration':
                for decl in node.declarations or []:
                    if decl.init and decl.init.type == 'ObjectExpression' and decl.id.type == 'Identifier':
                        base = decl.id.name
                        add_slice(base, decl.init)
                        walk_object(base, decl.init)

            for key in dir(node):
                if key.startswith('_') or key in ('type', 'range', 'loc'):
                    continue
                value = getattr(node, key)
                if isinstance(value, list) or (hasattr(value, 'type') and value.type):
                    walk(value)

        walk(tree.body)
        return assignments

    # ---------------------------
    # Python extractor
    # ---------------------------
    def py_extract_top_level_callables(self, source_code: str) -> dict:
        tree = ast.parse(source_code)
        lines = source_code.splitlines()
        result = {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}

        def slice_by_lines(start_lineno: int, end_lineno: Optional[int]) -> str:
            start = start_lineno - 1
            if end_lineno is None:
                end = start + 1
                while end < len(lines) and (lines[end].startswith((' ', '\t')) or not lines[end].strip()):
                    end += 1
            else:
                end = end_lineno
            raw = '\n'.join(lines[start:end])
            return textwrap.dedent(raw)

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                name = node.name
                code = slice_by_lines(node.lineno, getattr(node, 'end_lineno', None))
                result['def'][name] = code
                result['flat'][name] = code

            elif isinstance(node, ast.ClassDef):
                cname = node.name
                class_code = slice_by_lines(node.lineno, getattr(node, 'end_lineno', None))
                result['class'][cname] = class_code
                result['flat'][cname] = class_code

                for sub in node.body:
                    if isinstance(sub, ast.FunctionDef):
                        mname = sub.name
                        mcode = slice_by_lines(sub.lineno, getattr(sub, 'end_lineno', None))
                        for key in (f'{cname}.{mname}', f'{cname}::{mname}'):
                            result['class_methods'][key] = mcode
                            result['flat'][key] = mcode
        return result

    # ---------------------------
    # PHP extractor (your existing implementation)
    # ---------------------------
    _PHP_IDENT = re.compile(r'[A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*', re.UNICODE)

    def _php_segments_only(self, code: str) -> str:
        out, i, n = [], 0, len(code)
        while i < n:
            start = code.find('<?', i)
            if start < 0:
                if not out and i == 0 and code.strip():
                    return code  # pure PHP file
                break
            endtag = code.find('?>', start)
            segment = code[start+2:] if endtag < 0 else code[start+2:endtag]
            if segment.lstrip().startswith('php'):
                segment = segment.lstrip()[3:]
            out.append(segment)
            i = n if endtag < 0 else endtag + 2
        return '\n'.join(out) if out else ''

    def php_extract_callables(self, source: str) -> dict:
        # keep your full PHP extractor body here exactly as-is
        # (omitted for brevity in this snippet)
        return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}

    # ---------------------------
    # New language extractors (lightweight)
    # ---------------------------
    def shell_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'(?m)^\s*(?:function\s+)?([a-zA-Z_][\w\-]*)\s*\(\)\s*\{', text):
            name = m.group(1)
            flat[name] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def go_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\bfunc\s+([A-Z_a-z]\w*)\s*\(', text):
            flat[m.group(1)] = ''
        for m in re.finditer(r'\btype\s+([A-Z]\w*)\s+(?:struct|interface)\b', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def rust_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\bfn\s+([a-zA-Z_]\w*)\s*\(', text):
            flat[m.group(1)] = ''
        for m in re.finditer(r'\b(struct|enum|trait)\s+([A-Z]\w*)', text):
            flat[m.group(2)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def java_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\b(class|interface|enum)\s+([A-Z]\w*)\b', text):
            flat[m.group(2)] = ''
        for m in re.finditer(r'\b([A-Za-z_]\w*)\s*\([^;{]*\)\s*\{', text):
            # best-effort: avoids perfect parsing; still useful
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def csharp_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\b(class|interface|enum|struct)\s+([A-Z]\w*)\b', text):
            flat[m.group(2)] = ''
        for m in re.finditer(r'\b([A-Za-z_]\w*)\s*\([^;{]*\)\s*\{', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def cpp_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\b(class|struct|enum)\s+([A-Z_a-z]\w*)\b', text):
            flat[m.group(2)] = ''
        for m in re.finditer(r'\b([A-Z_a-z]\w*)\s*\([^;]*\)\s*(?:const\s*)?\{', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def c_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'\b([A-Z_a-z]\w*)\s*\([^;]*\)\s*\{', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def lua_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'(?m)^\s*function\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s*\(', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    def ruby_extract_callables(self, text: str) -> dict:
        flat = {}
        for m in re.finditer(r'(?m)^\s*def\s+([A-Za-z_]\w*[!?=]?)', text):
            flat[m.group(1)] = ''
        for m in re.finditer(r'(?m)^\s*class\s+([A-Z]\w*)', text):
            flat[m.group(1)] = ''
        return {'def': flat, 'class': {}, 'class_methods': {}, 'flat': flat}

    # ---------------------------
    # Orchestrator (registry-based)
    # ---------------------------
    def _extract_js_flat(self, data: str) -> dict:
        data = self.js_clean(data)
        if not data:
            return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}
        return {
            'def': {},
            'class': {},
            'class_methods': {},
            'flat': self.js_extract_namespaced_assignments(data)
        }

    def extract_callables(self, data: str, language: Optional[str]) -> Tuple[dict, str]:
        lang = (language or '').lower().strip()

        if not lang:
            if '<script' in data.lower() and '</script' in data.lower():
                lang = 'html'
            else:
                lang = 'python'

        # containers: HTML/Vue/Svelte -> JS
        if lang in ('htm', 'html'):
            data = self.extract_javascript_from_html_scripts_only(data)
            data = data.replace('\r', '').replace('\n\n', '\n')
            lang = 'javascript'

        # TS -> JS patterns (for now)
        if lang in ('typescript', 'ts', 'tsx'):
            lang = 'javascript'

        EXTRACTORS = {
            'python': self.py_extract_top_level_callables,
            'php': self.php_extract_callables,
            'javascript': self._extract_js_flat,
            'shell': self.shell_extract_callables,
            'go': self.go_extract_callables,
            'rust': self.rust_extract_callables,
            'java': self.java_extract_callables,
            'csharp': self.csharp_extract_callables,
            'cpp': self.cpp_extract_callables,
            'c': self.c_extract_callables,
            'lua': self.lua_extract_callables,
            'ruby': self.ruby_extract_callables,
        }

        fn = EXTRACTORS.get(lang)
        if not fn:
            # unknown language -> default safe behavior
            return self.py_extract_top_level_callables(data), 'python'

        return fn(data), lang

    @staticmethod
    def get_callable(extracted: dict, key: str) -> Optional[str]:
        if not extracted:
            return None
        if 'flat' in extracted and key in extracted['flat']:
            return extracted['flat'][key]
        if 'class_methods' in extracted:
            if key in extracted['class_methods']:
                return extracted['class_methods'][key]
            alt = key.replace('::', '.') if '::' in key else key.replace('.', '::')
            return extracted['class_methods'].get(alt)
        if key in extracted.get('def', {}):
            return extracted['def'][key]
        if key in extracted.get('class', {}):
            return extracted['class'][key]
        return None

#############################################################################################################
#############################################################################################################
#!/usr/bin/env python3
import sys
import re
from typing import Dict, List


PHP_IDENT = r'[A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*'


def php_segments_only(code: str) -> str:
    out, i, n = [], 0, len(code)
    while i < n:
        start = code.find('<?', i)
        if start < 0:
            if not out and i == 0 and code.strip():
                return code
            break
        end = code.find('?>', start)
        seg = code[start + 2:] if end < 0 else code[start + 2:end]
        if seg.lstrip().startswith('php'):
            seg = seg.lstrip()[3:]
        out.append(seg)
        i = n if end < 0 else end + 2
    return '\n'.join(out)


def mask_comments_and_strings(code: str) -> str:
    # keep length identical
    n = len(code)
    out = []
    i = 0
    while i < n:
        ch = code[i]

        if code.startswith('//', i) or (ch == '#' and (i == 0 or code[i-1] != '$')):
            j = code.find('\n', i)
            if j == -1:
                out.append(' ' * (n - i))
                break
            out.append(' ' * (j - i))
            out.append('\n')
            i = j + 1
            continue

        if code.startswith('/*', i):
            j = code.find('*/', i + 2)
            if j == -1:
                out.append(' ' * (n - i))
                break
            out.append(' ' * (j + 2 - i))
            i = j + 2
            continue

        if ch in ("'", '"'):
            q = ch
            j = i + 1
            while j < n:
                if code[j] == '\\':
                    j += 2
                    continue
                if code[j] == q:
                    j += 1
                    break
                j += 1
            out.append(q)
            out.append(' ' * max(0, j - i - 2))
            out.append(q)
            i = j
            continue

        out.append(ch)
        i += 1

    return ''.join(out)


def find_matching_brace(code: str, start: int) -> int:
    depth = 1
    i = start + 1
    while i < len(code) and depth > 0:
        if code[i] == '{':
            depth += 1
        elif code[i] == '}':
            depth -= 1
        i += 1
    return i


def extract_php_callables(source: str) -> Dict[str, List[str]]:
    code = php_segments_only(source)
    masked = mask_comments_and_strings(code)

    callables = []

    # ---------- classes ----------
    class_pat = re.compile(
        rf'\b(class|interface|trait|enum)\s+({PHP_IDENT})\b[^{{;]*\{{',
        re.I
    )


    class_spans = []

    for m in class_pat.finditer(masked):
        cname = m.group(2)
        callables.append(cname)
        ob = masked.find('{', m.start())
        end = find_matching_brace(masked, ob)
        class_spans.append((cname, m.start(), end))

    # ---------- methods ----------
    method_pat = re.compile(rf'\bfunction\s+({PHP_IDENT})\s*\(')

    for cname, s, e in class_spans:
        block = masked[s:e]
        for m in method_pat.finditer(block):
            mname = m.group(1)
            callables.append(f'{cname}.{mname}')
            callables.append(f'{cname}::{mname}')

    # ---------- top-level functions ----------
    top_fn_pat = re.compile(
        rf'(?m)^\s*\bfunction\s+({PHP_IDENT})\s*\('
    )

    for m in top_fn_pat.finditer(masked):
        fname = m.group(1)
        callables.append(fname)

    return {
        'flat': sorted(set(callables))
    }


def main(path):
    # if len(sys.argv) < 2:
    #     print("usage: php_callables.py file.php", file=sys.stderr)
    #     sys.exit(1)

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        src = f.read()

    data = extract_php_callables(src)
    # _.pv(data)
    for name in data['flat']:
        print(name)
    sys.exit(0)



#############################################################################################################


















































def action():

    if _.switches.value('Files').endswith('.php'):

        main(_.switches.values('Files')[0])
        # sys.exit()


    # create an instance
    ce = CallableExtractor()

    # call the high-level entry point
    ce.action()










########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)