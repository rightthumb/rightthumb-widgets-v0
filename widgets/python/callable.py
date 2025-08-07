import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Callable', '--c,-fn,-class,-callable' )
	_.switches.register( 'First', '-first,-1' )
	# _.switches.register( 'ListKeys', '-k,-keys' )



_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
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



import ast
import textwrap

def py_extract_top_level_callables(source_code: str) -> dict:
	"""
	Parses and executes the Python source code to extract top-level classes and functions.
	Returns a dictionary with:
		{
			'def': { 'function_name': 'source code' },
			'class': { 'ClassName': 'source code' }
		}

	:param source_code: Python source code as a string.
	:return: Dict with 'def' and 'class' keys mapping names to their source code.
	"""
	tree = ast.parse(source_code)
	lines = source_code.splitlines()
	result = {'def': {}, 'class': {}}

	for node in tree.body:
		if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
			name = node.name
			start = node.lineno - 1
			end = getattr(node, 'end_lineno', None)

			if end is None:
				# crude fallback for older Python versions
				end = start + 1
				while end < len(lines) and lines[end].startswith((' ', '\t')):
					end += 1

			raw_source = '\n'.join(lines[start:end])
			clean_source = textwrap.dedent(raw_source)

			if isinstance(node, ast.FunctionDef):
				result['def'][name] = clean_source
			elif isinstance(node, ast.ClassDef):
				result['class'][name] = clean_source

	return result











def js_extract_namespaced_assignments(code: str) -> dict:
	"""
	Extract namespaced assignments from JavaScript code (e.g., _.note.manager.action = ...).
	Automatically handles '??', '?.', and deeply nested object literals.

	Returns:
		dict: { '_.note.manager.action': 'assigned code as string' }
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
		while node.type == 'MemberExpression':
			prop = node.property
			name = None
			if hasattr(prop, 'name'):
				name = prop.name
			elif hasattr(prop, 'value'):
				name = str(prop.value)
			parts.insert(0, name if name is not None else '[unknown]')
			node = node.object
		if node.type == 'Identifier':
			parts.insert(0, node.name)
		elif hasattr(node, 'name') and node.name:
			parts.insert(0, node.name)
		else:
			parts.insert(0, '[root]')
		return '.'.join(str(p) for p in parts if p)

	def walk(node):
		if isinstance(node, list):
			for item in node:
				walk(item)
		elif hasattr(node, 'type'):
			if node.type == 'ExpressionStatement' and hasattr(node, 'expression'):
				walk(node.expression)

			elif node.type == 'AssignmentExpression':
				left = node.left
				right = node.right
				if left.type == 'MemberExpression' and hasattr(right, 'range'):
					try:
						full_path = extract_full_path(left)
						start, end = right.range
						assignments[full_path] = code[start:end]
					except Exception as e:
						print(f"[extract] skipping invalid path: {e}")

			elif node.type == 'VariableDeclaration':
				for decl in node.declarations:
					if decl.init and decl.init.type == 'ObjectExpression':
						walk_object(decl.id.name, decl.init)

			for key in dir(node):
				if key.startswith('_') or key in ('type', 'range', 'loc'):
					continue
				value = getattr(node, key)
				if isinstance(value, (list, esprima.nodes.Node)):
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

	# === Begin Execution ===
	code = sanitize_js(code)
	try:
		tree = esprima.parseScript(code, {'range': True})
	except Exception as e:
		print(f"[js_extract_namespaced_assignments] Parse error: {e}")
		return {}

	assignments = {}
	walk(tree.body)
	return assignments










def extract_javascript(code):
	code = strip_html_comments(code)
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
			js_code += line + '\r\n'  # Preserve original formatting

	return js_code




import re

def strip_php_blocks(code: str) -> str:
	"""
	Replace all PHP code blocks like <?php ... ?> or <? ... ?> with empty single quotes ''.
	Useful for sanitizing JavaScript embedded in PHP files.

	:param code: The full JavaScript (or HTML) code string
	:return: Cleaned code with PHP blocks removed
	"""
	return re.sub(r'<\?(php)?[\s\S]*?\?>', "''", code, flags=re.IGNORECASE)



import re

def strip_html_comments(html: str) -> str:
	"""
	Removes all HTML comments from the input string.

	Args:
		html (str): The HTML content as a string.

	Returns:
		str: The HTML string with comments removed.
	"""
	return re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)


def js_clean(code):
	code = code.replace("''''", "''")
	code = code.replace('?.(','(')
	code = code.replace('?.[','[')
	# code = code.replace('','')
	data = []
	lines = code.splitlines()
	for line in lines:
		cl = line.strip()
		if cl == "''": continue
		if cl.lower().startswith('<'): continue
		data.append(line)
	return '\n'.join(data)



from bs4 import BeautifulSoup

def extract_javascript_from_html(html: str) -> str:
    """
    Extract all JavaScript code from an HTML string, including:
    - <script> tag content
    - Inline event handler attributes (e.g., onclick, onload)

    Returns:
        str: Combined JavaScript code separated by multiple newlines.
    """
    soup = BeautifulSoup(html, "html.parser")
    js_blocks = []

    # Extract from <script> tags
    for script in soup.find_all("script"):
        if script.string:
            js_blocks.append(script.string.strip())

    # Extract from inline JS attributes
    for tag in soup.find_all(True):
        for attr, value in tag.attrs.items():
            if attr.startswith("on") and isinstance(value, str):
                js_blocks.append(value.strip())

    return "\n\n\n".join(js_blocks)



def extract_javascript_from_html2(html: str) -> str:
    """
    Extract all JavaScript code from an HTML string, including:
    - <script> tag content
    - Inline event handler attributes (e.g., onclick, onload)

    Returns:
        str: Combined JavaScript code separated by multiple newlines.
    """
    soup = BeautifulSoup(html, "html.parser")
    js_blocks = []

    # Extract from <script> tags
    for script in soup.find_all("script"):
        if script.string:
            js_blocks.append(script.string.strip())

    # Extract from inline JS attributes
    for tag in soup.find_all(True):
        for attr, value in tag.attrs.items():
            if attr.startswith("on") and isinstance(value, str):
                js_blocks.append(value.strip())

    return js_blocks





from bs4 import BeautifulSoup

def extract_javascript_from_html3(html: str) -> str:
    """
    Extract only JavaScript from <script> tags in the HTML.
    Inline JS (like onclick attributes) will be ignored.

    Returns:
        str: All JS code from <script> tags, separated by newlines.
    """
    soup = BeautifulSoup(html, "html.parser")
    js_blocks = []

    for script in soup.find_all("script"):
        if script.string:
            js_blocks.append(script.string.strip())

    return "\n\n\n".join(js_blocks)






import os, sys

def getData():
	lan = 'py'
	relevant = 'error'
	callable = _.switches.value('Callable')
	
	for path in _.isData(2):
		if path.endswith('.js'): lan = 'js'
		data = _.getText(path,raw=True)
		items_to_check = ['php','htm','html']
		root, ext = os.path.splitext(path)
		ext = ext.replace('.', '').lower()
		EXT = [ext]
		if any(item in EXT for item in items_to_check):
			# data = extract_javascript(data)
			data = extract_javascript_from_html3(data)
			# testing = extract_javascript_from_html2(data); _.pv(testing); sys.exit(0)
			if ext in ['php']:
				data = strip_php_blocks(data)
			data = data.replace('\r','')
			data = data.replace('\n\n','\n')
			# data = data.split('//eof')[0]
			lan = 'js'
		if lan == 'js':
			data = js_clean(data)


			Save_Quit = 0

			if Save_Quit:
				_.saveText(data,'__temp.js')
				# print(data)
				sys.exit(0)
		

		# print(data)
		if lan == 'py':
			def_class = py_extract_top_level_callables(data)
			callables = {}
			for item in def_class['def']:
				callables[item] = def_class['def'][item]
			for item in def_class['class']:
				callables[item] = def_class['class'][item]
		elif lan == 'js':
			callables = js_extract_namespaced_assignments(data)
		if not callable:
			relevant = callables
		else:
			if callable in callables:
				if lan == 'py' and len(_.switches.values('Callable')) > 2:
					a = _.switches.values('Callable')[0].lower()
					b = _.switches.values('Callable')[1]
					if 'c' in a:
						relevant = def_class['class'].get(b, '<error>')
					elif 'd' in a:
						relevant = def_class['def'].get(b, '<error>')
					else:
						relevant = callables.get(b, '<error>')
				else:
					relevant = callables.get(callable, '<error>')

	return relevant

def action():
	valid = True
	if not _.switches.isActive('Callable'):
		valid = False

	relevant = getData()
	# try:
	# 	relevant = getData()
	# except Exception as ee:
	# 	_.e(f"Error occurred: {ee}")
	pass
	# print(relevant)
	if not relevant:
		_.e('No callable found')

	if not valid:
		for k in relevant:
			_.pr(k)


	if valid:
		firstText = False
		print('')

		colorized = _.printVarColor( relevant.copy() )


		for line in relevant.splitlines():
			if not firstText and not line.strip():
				continue
			
			
			if _.showLine(line):
				# _.pr(line)
				if not firstText:
					_.printVarSimpleFake3( line )
				else:
					_.pr(line,c='cyan')

			firstText = True

			if _.switches.isActive('First'):
				return

		


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)