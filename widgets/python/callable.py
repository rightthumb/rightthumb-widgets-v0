import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Callable', '--c,-fn,-class,-callable' )
	_.switches.register( 'First', '-first,-1' )
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



# import ast
# import textwrap

# def py_extract_top_level_callables(source_code: str) -> dict:
# 	"""
# 	Parses and executes the Python source code to extract top-level classes and functions.
# 	Returns a dictionary with:
# 		{
# 			'def': { 'function_name': 'source code' },
# 			'class': { 'ClassName': 'source code' }
# 		}

# 	:param source_code: Python source code as a string.
# 	:return: Dict with 'def' and 'class' keys mapping names to their source code.
# 	"""
# 	tree = ast.parse(source_code)
# 	lines = source_code.splitlines()
# 	result = {'def': {}, 'class': {}}

# 	for node in tree.body:
# 		if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
# 			name = node.name
# 			start = node.lineno - 1
# 			end = getattr(node, 'end_lineno', None)

# 			if end is None:
# 				# crude fallback for older Python versions
# 				end = start + 1
# 				while end < len(lines) and lines[end].startswith((' ', '\t')):
# 					end += 1

# 			raw_source = '\n'.join(lines[start:end])
# 			clean_source = textwrap.dedent(raw_source)

# 			if isinstance(node, ast.FunctionDef):
# 				result['def'][name] = clean_source
# 			elif isinstance(node, ast.ClassDef):
# 				result['class'][name] = clean_source

# 	return result











# def js_extract_namespaced_assignments(code: str) -> dict:
# 	"""
# 	Extract namespaced assignments from JavaScript code (e.g., _.note.manager.action = ...).
# 	Automatically handles '??', '?.', and deeply nested object literals.

# 	Returns:
# 		dict: { '_.note.manager.action': 'assigned code as string' }
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
# 		while node.type == 'MemberExpression':
# 			prop = node.property
# 			name = None
# 			if hasattr(prop, 'name'):
# 				name = prop.name
# 			elif hasattr(prop, 'value'):
# 				name = str(prop.value)
# 			parts.insert(0, name if name is not None else '[unknown]')
# 			node = node.object
# 		if node.type == 'Identifier':
# 			parts.insert(0, node.name)
# 		elif hasattr(node, 'name') and node.name:
# 			parts.insert(0, node.name)
# 		else:
# 			parts.insert(0, '[root]')
# 		return '.'.join(str(p) for p in parts if p)

# 	def walk(node):
# 		if isinstance(node, list):
# 			for item in node:
# 				walk(item)
# 		elif hasattr(node, 'type'):
# 			if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
# 				walk(node.expression)

# 			elif node.type == 'AssignmentExpression':
# 				left = node.left
# 				right = node.right
# 				if left.type == 'MemberExpression' and hasattr(right, 'range'):
# 					try:
# 						full_path = extract_full_path(left)
# 						start, end = right.range
# 						assignments[full_path] = code[start:end]
# 					except Exception as e:
# 						print(f"[extract] skipping invalid path: {e}")

# 			elif node.type == 'VariableDeclaration':
# 				for decl in node.declarations:
# 					if decl.init and decl.init.type == 'ObjectExpression':
# 						walk_object(decl.id.name, decl.init)

# 			for key in dir(node):
# 				if key.startswith('_') or key in ('type', 'range', 'loc'):
# 					continue
# 				value = getattr(node, key)
# 				if isinstance(value, (list, esprima.nodes.Node)):
# 					walk(value)

# 	def walk_object(base: str, obj_node):
# 		for prop in obj_node.properties:
# 			if prop.key.type == 'Identifier':
# 				prop_name = prop.key.name
# 			elif prop.key.type == 'Literal':
# 				prop_name = str(prop.key.value)
# 			else:
# 				prop_name = '[unknown]'
# 			full_path = f"{base}.{prop_name}"
# 			if hasattr(prop.value, 'range'):
# 				start, end = prop.value.range
# 				assignments[full_path] = code[start:end]
# 			if prop.value.type == 'ObjectExpression':
# 				walk_object(full_path, prop.value)

# 	# === Begin Execution ===
# 	code = sanitize_js(code)
# 	try:
# 		tree = esprima.parseScript(code, {'range': True})
# 	except Exception as e:
# 		print(f"[js_extract_namespaced_assignments] Parse error: {e}")
# 		return {}

# 	assignments = {}
# 	walk(tree.body)
# 	return assignments










# def extract_javascript(code):
# 	code = strip_html_comments(code)
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
# 			js_code += line + '\r\n'  # Preserve original formatting

# 	return js_code




# import re

# def strip_php_blocks(code: str) -> str:
# 	"""
# 	Replace all PHP code blocks like <?php ... ?> or <? ... ?> with empty single quotes ''.
# 	Useful for sanitizing JavaScript embedded in PHP files.

# 	:param code: The full JavaScript (or HTML) code string
# 	:return: Cleaned code with PHP blocks removed
# 	"""
# 	return re.sub(r'<\?(php)?[\s\S]*?\?>', "''", code, flags=re.IGNORECASE)



# import re

# def strip_html_comments(html: str) -> str:
# 	"""
# 	Removes all HTML comments from the input string.

# 	Args:
# 		html (str): The HTML content as a string.

# 	Returns:
# 		str: The HTML string with comments removed.
# 	"""
# 	return re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)


# def js_clean(code):
# 	code = code.replace("''''", "''")
# 	code = code.replace('?.(','(')
# 	code = code.replace('?.[','[')
# 	# code = code.replace('','')
# 	data = []
# 	lines = code.splitlines()
# 	for line in lines:
# 		cl = line.strip()
# 		if cl == "''": continue
# 		if cl.lower().startswith('<'): continue
# 		data.append(line)
# 	return '\n'.join(data)



# from bs4 import BeautifulSoup

# def extract_javascript_from_html(html: str) -> str:
#     """
#     Extract all JavaScript code from an HTML string, including:
#     - <script> tag content
#     - Inline event handler attributes (e.g., onclick, onload)

#     Returns:
#         str: Combined JavaScript code separated by multiple newlines.
#     """
#     soup = BeautifulSoup(html, "html.parser")
#     js_blocks = []

#     # Extract from <script> tags
#     for script in soup.find_all("script"):
#         if script.string:
#             js_blocks.append(script.string.strip())

#     # Extract from inline JS attributes
#     for tag in soup.find_all(True):
#         for attr, value in tag.attrs.items():
#             if attr.startswith("on") and isinstance(value, str):
#                 js_blocks.append(value.strip())

#     return "\n\n\n".join(js_blocks)



# def extract_javascript_from_html2(html: str) -> str:
#     """
#     Extract all JavaScript code from an HTML string, including:
#     - <script> tag content
#     - Inline event handler attributes (e.g., onclick, onload)

#     Returns:
#         str: Combined JavaScript code separated by multiple newlines.
#     """
#     soup = BeautifulSoup(html, "html.parser")
#     js_blocks = []

#     # Extract from <script> tags
#     for script in soup.find_all("script"):
#         if script.string:
#             js_blocks.append(script.string.strip())

#     # Extract from inline JS attributes
#     for tag in soup.find_all(True):
#         for attr, value in tag.attrs.items():
#             if attr.startswith("on") and isinstance(value, str):
#                 js_blocks.append(value.strip())

#     return js_blocks





# from bs4 import BeautifulSoup

# def extract_javascript_from_html3(html: str) -> str:
#     """
#     Extract only JavaScript from <script> tags in the HTML.
#     Inline JS (like onclick attributes) will be ignored.

#     Returns:
#         str: All JS code from <script> tags, separated by newlines.
#     """
#     soup = BeautifulSoup(html, "html.parser")
#     js_blocks = []

#     for script in soup.find_all("script"):
#         if script.string:
#             js_blocks.append(script.string.strip())

#     return "\n\n\n".join(js_blocks)






# import os, sys

# def getData():
# 	global Language
# 	lan = 'py'
# 	relevant = 'error'
# 	callable = _.switches.value('Callable')
	
# 	Lan = {
# 		'py': 'python',
# 		'js': 'javascript',
# 		'php': 'php',
# 		'htm': 'html',
# 		'html': 'html',
# 	}

# 	for path in _.isData(2):
# 		if path.endswith('.js'): lan = 'js'
# 		data = _.getText(path,raw=True)
# 		items_to_check = ['php','htm','html']
# 		root, ext = os.path.splitext(path)
# 		ext = ext.replace('.', '').lower()
# 		if ext in Lan:
# 			Language = Lan[ext]
# 		else:
# 			Language = None


# 		analyze = True
# 		if analyze:
# 			CODE = _.CodeColor()
# 			info = CODE.analyze(data, language=Language)
# 			# _.pv(info)
# 		EXT = [ext]
# 		if any(item in EXT for item in items_to_check):
# 			# data = extract_javascript(data)
# 			data = extract_javascript_from_html3(data)
# 			# testing = extract_javascript_from_html2(data); _.pv(testing); sys.exit(0)
# 			if ext in ['php']:
# 				data = strip_php_blocks(data)
# 			data = data.replace('\r','')
# 			data = data.replace('\n\n','\n')
# 			# data = data.split('//eof')[0]
# 			lan = 'js'
# 		if lan == 'js':
# 			data = js_clean(data)


# 			Save_Quit = 0

# 			if Save_Quit:
# 				_.saveText(data,'__temp.js')
# 				# print(data)
# 				sys.exit(0)
		

# 		# print(data)
# 		if lan == 'py':
# 			def_class = py_extract_top_level_callables(data)
# 			callables = {}
# 			for item in def_class['def']:
# 				callables[item] = def_class['def'][item]
# 			for item in def_class['class']:
# 				callables[item] = def_class['class'][item]
# 		elif lan == 'js':
# 			callables = js_extract_namespaced_assignments(data)
# 		if not callable:
# 			relevant = callables
# 		else:
# 			if callable in callables:
# 				if lan == 'py' and len(_.switches.values('Callable')) > 2:
# 					a = _.switches.values('Callable')[0].lower()
# 					b = _.switches.values('Callable')[1]
# 					if 'c' in a:
# 						relevant = def_class['class'].get(b, '<error>')
# 					elif 'd' in a:
# 						relevant = def_class['def'].get(b, '<error>')
# 					else:
# 						relevant = callables.get(b, '<error>')
# 				else:
# 					relevant = callables.get(callable, '<error>')

# 	if type(relevant) == dict and callable in relevant:
# 		relevant = relevant[callable]
	

# 	return relevant, callables
# Language = 'python'

# import sys

# sample_python = """
# class Threads:
#     openCnt = 0
#     closedCnt = 0

#     def __init__(self, name=None, func=None, **kwargs):
#         self.name = name
#         self.func = func
#         self.kwargs = kwargs

#     def start(self):
#         print(f"Starting thread: {self.name}")

# if __name__ == "__main__":
#     t = Threads(name="Worker1")
#     t.start()
# """
# sample_js = """
# class Threads {
#     constructor(name, func) {
#         this.name = name;
#         this.func = func;
#     }

#     start() {
#         console.log(`Starting thread: ${this.name}`);
#     }
# }

# const t = new Threads("Worker1", () => console.log("Running..."));
# t.start();
# """

# # You liked the following styles:
# liked='''
# arduino
# autumn
# coffee
# default
# emacs
# friendly
# github-dark
# gruvbox-dark
# lightbulb
# manni
# material
# monokai
# one-dark
# paraiso-dark
# solarized-dark
# '''.strip().split('\n')

# def action():
# 	if _.switches.isActive('ColorSamples'):
# 		styles = ["abap", "algol", "algol_nu", "arduino", "autumn", "bw", "borland", "coffee", "colorful", "default", "dracula", "emacs", "friendly_grayscale", "friendly", "fruity", "github-dark", "gruvbox-dark", "gruvbox-light", "igor", "inkpot", "lightbulb", "lilypond", "lovelace", "manni", "material", "monokai", "murphy", "native", "nord-darker", "nord", "one-dark", "paraiso-dark", "paraiso-light", "pastie", "perldoc", "rainbow_dash", "rrt", "sas", "solarized-dark", "solarized-light", "staroffice", "stata-dark", "stata-light", "tango", "trac", "vim", "vs", "xcode", "zenburn"]
# 		styles = liked
# 		like = []
# 		for style in styles:
# 			codeColor = _.CodeColor(style)
# 			print(codeColor.color(sample_python,'python'))
# 			print(codeColor.color(sample_js,'javascript'))
# 			_.pr()
# 			_.pr(style,c='green')
# 			_.pr()
# 			_.pr(line=1)
# 			ask = input(': ')
# 			if ask.lower() in ['y','yes']:
# 				like.append(style)
# 		_.pr()
# 		_.pr('You liked the following styles:')
# 		for item in like:
# 			_.pr(item)
# 		_.pr()

# 		return
# 	global Language
# 	valid = True
# 	if not _.switches.isActive('Callable'):
# 		valid = False






# 	# CACHE-START


# 	thePath = _v.tt+_v.slash+'Callable'+_v.slash
# 	theFile = _.switches.values('Files')[0]
# 	theCache = thePath+_.md5_string(theFile)
# 	if not os.path.isfile(theFile):
# 		_.e('File not found')
# 		return
	
# 	_.RegID.add(_.md5_string(theFile), theFile, 'Callable')


# 	CACHE = True
# 	CACHE_AUTO = True
# 	if not os.path.isfile(theCache):
# 		CACHE = False
	
# 	if CACHE:
# 		if CACHE_AUTO:
# 			if not _.md(theFile) == _.md(theCache):
# 				CACHE = False
# 				# _.e('Cache miss')




# 	isCACHE = False
# 	relevant = None
# 	callables = None
# 	if not CACHE:
# 		relevant, callables = getData()
# 		_.saveTable(callables,'Callable'+_v.slash+ _.md5_string(theFile) , p=0)
# 		_.md(thePath+_.md5_string(theFile), _.md(theFile) )


# 	elif CACHE:
# 		relevant = None
# 		_v.mkdir(thePath)
# 		try:
# 			callables = _.getTable('Callable'+_v.slash+ _.md5_string(theFile) )
# 		except: pass

# 		if not callables:
# 			relevant, callables = getData()
# 			_.saveTable(callables,'Callable'+_v.slash+ _.md5_string(theFile) , p=0)
# 			_.md(thePath+_.md5_string(theFile), _.md(theFile) )
# 		else:
# 			isCACHE = _.pr('\n\n  Cache',h=_.P('cyberpunk','p'), p=0)

# 	if relevant is None:
# 		if not valid:
# 			relevant = callables
# 		else:
# 			relevant = callables[_.switches.value('Callable')]


# 	# CACHE-END














# 	# try:
# 	# 	relevant = getData()
# 	# except Exception as ee:
# 	# 	_.e(f"Error occurred: {ee}")
# 	pass
# 	# print(relevant)
# 	if not relevant:
# 		_.e('No callable found')

# 	if not valid:
# 		for k in relevant:
# 			_.pr(k)


# 	if theFile.lower().endswith('.py'):
# 		Language = 'python'
# 	elif theFile.lower().endswith('.js'):
# 		Language = 'javascript'
# 	elif theFile.lower().endswith('.html'):
# 		Language = 'html'
# 	elif theFile.lower().endswith('.css'):
# 		Language = 'css'

# 	if valid:
# 		if _.switches.isActive('Save'):
# 			_.saveText(relevant,_.switches.value('Save'))
# 			return
# 		# print(Language); return
# 		def display():
# 			global Language
# 			firstText = False
# 			print('')

# 			# colorized = _.printVarColor( relevant )

# 			codeColor = _.CodeColor()
# 			# language = codeColor.detect_language(relevant)
# 			# language = 'python'
# 			# _.pr(relevant['_.AppWeaver.code.html.field']); return
# 			# _.pv( list(relevant.keys()) ); return
# 			# _.pv(relevant); return
# 			# _.pr(relevant); return
# 			# print(Language)
# 			# print(colorized)
# 			# return
# 			if _.switches.isActive('NoColor'):
# 				colorized = relevant
# 			else:
# 				colorized = codeColor.color(relevant,Language)
# 			colorLines = colorized.splitlines()
# 			isClass = False
# 			for i, line in enumerate(relevant.splitlines()):
# 				if not firstText and not line.strip():
# 					continue
				
				
# 				if _.showLine(line):
# 					if line.startswith('class '):
# 						isClass = True
				
# 					# _.pr(line)
# 					if not firstText:
# 						# _.printVarSimpleFake3( line )
# 						# print(colorized.color(line,language))
# 						print(colorLines[i])
# 					else:
# 						if isClass and _.switches.isActive('First') and line.strip().startswith('def '):
# 							print(colorLines[i])
# 							# print(colorized.color(line,language))
# 							# _.printVarSimpleFake3( line )
# 							return

# 						print(colorLines[i])
# 						# _.pr(line,h='dark_orange')

# 				firstText = True

# 				if _.switches.isActive('First') and line.startswith('def '):
# 					return
# 	if valid:
# 		display()

























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
			if cl == "''": continue
			if cl.startswith('<'): continue
			data.append(line)
		return '\n'.join(data)

	@staticmethod
	def _language_from_ext(path: str) -> Optional[str]:
		Lan = {'py':'python','js':'javascript','php':'php','htm':'html','html':'html'}
		ext = os.path.splitext(path)[1].lower().lstrip('.')
		return Lan.get(ext)

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
		except Exception as e:
			print(f"[js_extract_namespaced_assignments] Parse error: {e}")
			return {}

		assignments = {}

		def add_slice(path, node):
			if hasattr(node, 'range') and node.range:
				start, end = node.range
				assignments[path] = code[start:end]

		def walk_object(base: str, obj_node):
			# Expand object literal: base.prop -> value (recursively)
			for prop in obj_node.properties:
				# Determine property name
				if prop.key.type == 'Identifier':
					prop_name = prop.key.name
				elif prop.key.type == 'Literal':
					prop_name = str(prop.key.value)
				else:
					prop_name = '[unknown]'
				full_path = f"{base}.{prop_name}"

				val = prop.value
				# Grab the exact source for this property value
				add_slice(full_path, val)

				# Recurse if nested object
				if getattr(val, 'type', None) == 'ObjectExpression':
					walk_object(full_path, val)

		def walk(node):
			if isinstance(node, list):
				for item in node:
					walk(item)
				return

			if not hasattr(node, 'type'):
				return

			# Top-level statements
			if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
				walk(node.expression)

			elif node.type == 'AssignmentExpression':
				left = node.left
				right = node.right
				if getattr(left, 'type', None) == 'MemberExpression':
					# Always record the RHS slice for the whole assignment
					full_path = extract_full_path(left)
					add_slice(full_path, right)

					# NEW: if assigning an object literal, expand its nested properties
					if getattr(right, 'type', None) == 'ObjectExpression':
						walk_object(full_path, right)

			elif node.type == 'VariableDeclaration':
				# Handle `const foo = { ... }` then foo.bar...
				for decl in node.declarations or []:
					if decl.init and decl.init.type == 'ObjectExpression' and decl.id.type == 'Identifier':
						base = decl.id.name
						# Record the top-level object literal itself
						add_slice(base, decl.init)
						walk_object(base, decl.init)

			# Continue walking child nodes
			for key in dir(node):
				if key.startswith('_') or key in ('type', 'range', 'loc'):
					continue
				value = getattr(node, key)
				if isinstance(value, list) or (hasattr(value, 'type') and value.type):
					walk(value)

		walk(tree.body)
		return assignments



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
		import sys, re

		def log(msg):
			pass
			# print(f"[php_extract] {msg}", file=sys.stderr)

		code = self._php_segments_only(source)
		result = {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}
		if not code.strip():
			log("no code after _php_segments_only")
			return result

		log(f"code length={len(code)}")

		# ---------------------------
		# Build a MASKED copy with SAME LENGTH as code:
		# replace contents of strings/comments with spaces so { } in them don't affect scans,
		# but all positions still match the original 'code'.
		# ---------------------------
		n = len(code)
		i = 0
		out = []
		while i < n:
			ch = code[i]

			# line comment //... or #
			if code.startswith('//', i) or (ch == '#' and (i == 0 or code[i-1] != '$')):
				j = code.find('\n', i)
				if j == -1:
					out.append(' ' * (n - i))
					i = n
					break
				out.append(' ' * (j - i))
				out.append('\n')
				i = j + 1
				continue

			# block comment /* ... */
			if code.startswith('/*', i):
				j = code.find('*/', i + 2)
				if j == -1:
					out.append(' ' * (n - i))
					i = n
					break
				out.append(' ' * (j + 2 - i))
				i = j + 2
				continue

			# single or double quoted strings
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
				# keep quotes, space out inside
				out.append(q)
				inner_len = max(0, (j - i - 2))
				if inner_len:
					out.append(' ' * inner_len)
				out.append(q if j <= n else '')
				i = j
				continue

			# default: copy char
			out.append(ch)
			i += 1

		masked = ''.join(out)
		log(f"masked length={len(masked)}")

		# Helper: safe brace walk on MASKED (returns end index or EOF)
		def find_matching_brace(start_idx: int) -> int:
			depth = 1
			j = start_idx + 1
			steps = 0
			MAX_STEPS = 10_000_000  # guard
			while j < len(masked) and depth > 0:
				c = masked[j]
				if c == '{':
					depth += 1
				elif c == '}':
					depth -= 1
				j += 1
				steps += 1
				if steps > MAX_STEPS:
					log(f"brace-walk guard hit at {j}, breaking")
					break
			return min(j, len(masked))

		# ---------------------------
		# 1) Find class/interface/trait/enum blocks on MASKED
		# ---------------------------
		class_pat = re.compile(
			r'\b(class|interface|trait|enum)\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\b[^{;]*\{',
			re.IGNORECASE
		)

		spans = []
		for m in class_pat.finditer(masked):
			kind, cname = m.group(1), m.group(2)
			open_brace_pos = masked.find('{', m.start())
			if open_brace_pos == -1:
				log(f"{kind} {cname}: no opening brace, skipping")
				continue
			end = find_matching_brace(open_brace_pos)
			log(f"found {kind} {cname} at {m.start()}..{end}")
			class_src = code[m.start(): end]  # slice from ORIGINAL using aligned indices
			result['class'][cname] = class_src
			result['flat'][cname] = class_src
			spans.append((cname, m.start(), end))

		# ---------------------------
		# 2) Methods inside each class (search MASKED slice for 'function name(')
		# ---------------------------
		fn_in_class_pat = re.compile(r'\bfunction\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\s*\(')

		for cname, s, e in spans:
			inner_masked = masked[s:e]
			inner_off = s
			log(f"scan methods in {cname}: slice={s}-{e} (len={len(inner_masked)})")
			for fm in fn_in_class_pat.finditer(inner_masked):
				mname = fm.group(1)
				# find body or ';'
				after = inner_masked[fm.end():]
				rel = fm.end()
				ob = after.find('{')
				sc = after.find(';')

				if ob != -1 and (sc == -1 or ob < sc):
					open_pos = inner_off + rel + ob
					end = find_matching_brace(open_pos)
					msrc = code[inner_off + fm.start(): end]
					log(f"method {cname}.{mname}: body {inner_off+fm.start()}..{end} (len={len(msrc)})")
				else:
					semi_pos = masked.find(';', inner_off + fm.start())
					if semi_pos == -1:
						semi_pos = inner_off + fm.start() + len('function ' + mname)
					msrc = code[inner_off + fm.start(): semi_pos + 1]
					log(f"method {cname}.{mname}: signature {inner_off+fm.start()}..{semi_pos+1}")

				for key in (f'{cname}.{mname}', f'{cname}::{mname}'):
					result['class_methods'][key] = msrc
					result['flat'][key] = msrc

		# ---------------------------
		# 3) Top-level functions (MULTILINE on MASKED)
		# ---------------------------
		top_fn_pat = re.compile(
			r'(?m)^\s*\bfunction\s+([A-Za-z_\x80-\xff][A-Za-z0-9_\x80-\xff]*)\s*\('
		)
		log("scan top-level functions")
		for fm in top_fn_pat.finditer(masked):
			fname = fm.group(1)
			log(f"found function {fname} at {fm.start()}")
			# find body or ';'
			after = masked[fm.end():]
			rel = fm.end()
			ob = after.find('{')
			sc = after.find(';')

			if ob != -1 and (sc == -1 or ob < sc):
				open_pos = rel + ob
				open_pos_abs = open_pos + 0  # relative to start of masked
				open_pos_abs = fm.end() + ob
				end = find_matching_brace(open_pos_abs)
				msrc = code[fm.start(): end]
				log(f"function {fname}: body {fm.start()}..{end} (len={len(msrc)})")
			else:
				semi_pos = masked.find(';', fm.start())
				if semi_pos == -1:
					semi_pos = fm.start() + len('function ' + fname)
				msrc = code[fm.start(): semi_pos + 1]
				log(f"function {fname}: signature {fm.start()}..{semi_pos+1}")

			result['def'][fname] = msrc
			result['flat'][fname] = msrc

		log("done")
		return result


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
	def extract_callables(self, data: str, language: Optional[str]) -> Tuple[dict, str]:
		lang = (language or '').lower()

		# import sys; print(language); sys.exit(0)

		if lang == 'javascript':
			data = self.js_clean(data)
			if data:
				return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': self.js_extract_namespaced_assignments(data)}, 'javascript'
			else:
				return {'def': {}, 'class': {}, 'class_methods': {}, 'flat': {}}, 'javascript'


		# Auto-detect minimal: if contains <script> or </script>, treat as HTML
		elif not lang:
			if '<script' in data.lower() and '</script' in data.lower():
				lang = 'html'
			else:
				lang = 'python'  # default

		elif lang in ('htm','html'):
			# Only <script> blocks, then sanitize for PHP if needed
			data = self.extract_javascript_from_html_scripts_only(data)
			data = data.replace('\r','').replace('\n\n','\n')
			lang = 'javascript'  # analyze JS extracted from HTML

		elif lang == 'php':
			# sometimes PHP files embed HTML/JS; we only want PHP segments for callable extraction
			# JS extraction in PHP HTML is separate flow; here we focus on PHP callables
			return self.php_extract_callables(data), 'php'


		# python
		return self.py_extract_top_level_callables(data), 'python'

	@staticmethod
	def get_callable(extracted: dict, key: str) -> Optional[str]:
		if not extracted: return None
		# prioritize exact flat match
		if 'flat' in extracted and key in extracted['flat']:
			return extracted['flat'][key]
		# allow ClassName.functionName with either '.' or '::'
		if 'class_methods' in extracted:
			if key in extracted['class_methods']:
				return extracted['class_methods'][key]
			alt = key.replace('::','.') if '::' in key else key.replace('.', '::')
			return extracted['class_methods'].get(alt)
		# fallback to def / class
		if key in extracted.get('def', {}): return extracted['def'][key]
		if key in extracted.get('class', {}): return extracted['class'][key]
		return None

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
			extracted, detected_language = self.extract_callables(data, language or 'python')

			if not callable_key:
				relevant = extracted
			else:
				relevant = self.get_callable(extracted, callable_key) or '<error>'

		return relevant, extracted







	# ---------------------------
	# def getData(self) -> Tuple[object, dict]:
	# 	"""
	# 	Returns (relevant, callables)
	# 	- relevant: either dict-of-callables or a single item string when a specific Callable was requested
	# 	- callables: the full extracted structure / map
	# 	"""
	# 	global _
	# 	lan_hint = 'py'
	# 	relevant = 'error'
	# 	callable_key = _.switches.value('Callable')

	# 	for path in _.isData(2) if hasattr(_, 'isData') else []:
	# 		if path.endswith('.js'): lan_hint = 'js'
	# 		data = _.getText(path, raw=True)
	# 		root, ext = os.path.splitext(path)
	# 		ext = ext.replace('.', '').lower()
	# 		language = self._language_from_ext(path)

	# 		# If HTML/PHP, we might want JS for the JS extractor path,
	# 		# but for PHP callables we stay in PHP branch inside extract_callables().
	# 		if ext in ('php', 'htm', 'html'):
	# 			# When you want JUST JavaScript out of HTML/PHP:
	# 			# data_js = self.extract_javascript_from_html_scripts_only(data)
	# 			# if ext == 'php': data_js = self.strip_php_blocks(data_js)
	# 			# data_js = data_js.replace('\r','').replace('\n\n','\n')
	# 			# lan_hint = 'js'
	# 			pass

	# 		extracted, detected_language = self.extract_callables(data, language)
	# 		lan_hint = {'python':'py','javascript':'js','php':'php'}.get(detected_language, lan_hint)

	# 		if not callable_key:
	# 			relevant = extracted
	# 		else:
	# 			# allow advanced handling python (c/d hints) like your original branch
	# 			rel = None
	# 			if detected_language == 'python' and len(_.switches.values('Callable')) > 2:
	# 				a = _.switches.values('Callable')[0].lower()
	# 				b = _.switches.values('Callable')[1]
	# 				if 'c' in a:
	# 					rel = extracted['class'].get(b, '<error>')
	# 				elif 'd' in a:
	# 					rel = extracted['def'].get(b, '<error>')
	# 				else:
	# 					rel = self.get_callable(extracted, b) or '<error>'
	# 			else:
	# 				rel = self.get_callable(extracted, callable_key) or '<error>'
	# 			relevant = rel

	# 	if isinstance(relevant, dict) and callable_key in relevant:
	# 		relevant = relevant[callable_key]
	# 	return relevant, extracted if isinstance(extracted, dict) else {}

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
					firstText = True
					if isClass and _.switches.isActive('First') and line.strip().startswith(('def ', 'function ')):
						return

		if valid and isinstance(relevant, str):
			display()


# ---------------------------
# If you wire this into your CLI, call:
# CallableExtractor().action()
# ---------------------------

def action():

	# create an instance
	ce = CallableExtractor()

	# call the high-level entry point
	ce.action()










########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)