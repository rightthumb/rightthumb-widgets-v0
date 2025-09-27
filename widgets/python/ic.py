import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	
	_.switches.register('Folder', '-fo,-folder')
	_.switches.register('Recursive', '-r,-recursive')

	_.switches.register('Path', '-p,-path', 'callables variables all') 

	_.switches.register('Class', '-class')
	_.switches.register('Variable', '-v,-var,-variable')
	_.switches.register('Minimal', '-min,-minimal')
	_.switches.register('Tabs', '-t,-tabs')
	_.switches.register('Spaces', '-sp,-spaces,-print,-printable')
	_.switches.register('PrintClean', '--c')
	_.switches.register('EnforceName', '-n', 'pyColor')

	_.switches.register('SysPath', '-i,-sp,-sys,-imp,-import', 'a/b/dst.py a/c/imp.py')
	# _.switches.register('SysPathSingleLine', '-one')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'ic.py',
	'description': 'Import Callable',
	'categories': [
						'code',
						'python',
						'class',
						'function',
						'include',
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


__.setting('omit-switch-triggers',['Folder'])


_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start



import os

def make_import1(path_consumer: str, path_provider: str):
	"""
	Generate sys.path.append and import statement so that path_consumer
	can import from path_provider.

	Args:
		path_consumer (str): Path to the Python file doing the import
		path_provider (str): Path to the Python file to be imported

	Returns:
		dict: {
			"sys_path": str,   # sys.path.append(...) line
			"import": str      # from ... import ...
		}
	"""
	consumer_dir = os.path.dirname(os.path.abspath(path_consumer))
	provider_dir = os.path.dirname(os.path.abspath(path_provider))
	provider_file = os.path.basename(path_provider)

	# figure relative path jumps
	rel_path = os.path.relpath(provider_dir, consumer_dir)

	# convert rel_path into os.path.join(__file__, '..', ...)
	steps = rel_path.split(os.sep)
	join_expr = ", ".join(["os.path.dirname(__file__)"] + [f"'{s}'" for s in steps])

	sys_path_line = f"sys.path.append(os.path.abspath(os.path.join({join_expr})))"

	# import path: replace / with .
	module_base = os.path.splitext(provider_file)[0]
	import_path = rel_path.replace(os.sep, ".")
	if import_path == ".":
		import_stmt = f"from {module_base} import {module_base}"
	else:
		import_stmt = f"from {module_base} import {module_base}"

	out = [
		'import sys, os',
		sys_path_line,
		import_stmt
	]

	return '\n'.join(out)


import os

def make_import2(path_consumer: str, path_provider: str) -> str:
	"""
	Build sys.path.append(...) (via __file__ + '..' jumps) so that the consumer can import the provider,
	and emit the import statement.

	Args:
		path_consumer: path to the Python file that will do the import
		path_provider: path to the Python file or package (__init__.py) to import

	Returns:
		str: lines to paste at top of the consumer file:
			 - "import sys, os"
			 - sys.path.append(...)
			 - import statement
	"""
	consumer_dir = os.path.dirname(os.path.abspath(path_consumer))
	provider_abs = os.path.abspath(path_provider)
	provider_dir = os.path.dirname(provider_abs)
	provider_filename = os.path.basename(provider_abs)

	# Determine if provider is a package (__init__.py) or a module file
	module_name, ext = os.path.splitext(provider_filename)
	is_package = (module_name == "__init__")

	# Choose the import root = common ancestor between consumer and provider dirs
	import_root = os.path.commonpath([consumer_dir, provider_dir])

	# Build the relative steps from consumer_dir -> import_root for sys.path.append
	rel_to_root = os.path.relpath(import_root, consumer_dir)
	steps = [] if rel_to_root == "." else rel_to_root.split(os.sep)

	join_expr_parts = ["os.path.dirname(__file__)"] + [f"'{s}'" for s in steps]
	join_expr = ", ".join(join_expr_parts) if join_expr_parts else "os.path.dirname(__file__)"
	sys_path_line = f"sys.path.append(os.path.abspath(os.path.join({join_expr})))"

	# Compute dotted package path from import_root -> provider_dir
	rel_pkg_path = os.path.relpath(provider_dir, import_root)
	dotted_pkg = "" if rel_pkg_path in (".", "") else rel_pkg_path.replace(os.sep, ".")

	# Build the import statement
	if is_package:
		# Import the package itself (since provider is __init__.py)
		if dotted_pkg:
			import_stmt = f"import {dotted_pkg}"
		else:
			# Package at import root; importing as top-level name = last folder name
			import_stmt = f"import {os.path.basename(provider_dir)}"
	else:
		# Import from the module file
		if dotted_pkg:
			import_stmt = f"from {dotted_pkg}.{module_name} import {module_name}"
		else:
			import_stmt = f"from {module_name} import {module_name}"

	out = [
		"import sys, os",
		sys_path_line,
		import_stmt
	]
	if not _.switches.isActive('SysPathSingleLine'):
		return "\n".join(out)
	else:
		return "; ".join(out)












import os

def make_import3(path_consumer: str, path_provider: str) -> str:
	"""
	Build sys.path.append(...) so that the consumer can import the provider
	using a direct path (no dotted package names).

	Args:
		path_consumer: path to the Python file that will do the import
		path_provider: path to the Python file or package (__init__.py) to import

	Returns:
		str: lines to paste at top of the consumer file:
			 - "import sys, os"
			 - sys.path.append(...)
			 - import statement (no dots)
	"""
	consumer_dir = os.path.dirname(os.path.abspath(path_consumer))
	provider_abs = os.path.abspath(path_provider)
	provider_dir = os.path.dirname(provider_abs)
	provider_filename = os.path.basename(provider_abs)

	module_name, ext = os.path.splitext(provider_filename)
	is_package = (module_name == "__init__")

	# Build relative path for sys.path.append
	rel_to_provider = os.path.relpath(provider_dir, consumer_dir)
	steps = [] if rel_to_provider == "." else rel_to_provider.split(os.sep)

	join_expr_parts = ["os.path.dirname(__file__)"] + [f"'{s}'" for s in steps]
	join_expr = ", ".join(join_expr_parts)
	sys_path_line = f"sys.path.append(os.path.abspath(os.path.join({join_expr})))"

	# Build import statement (always flat, no dots)
	if is_package:
		import_stmt = f"import {os.path.basename(provider_dir)}"
	else:
		import_stmt = f"from {module_name} import {module_name}"

	out = [
		"import sys, os",
		sys_path_line,
		import_stmt
	]
	return "\n".join(out)





import os
import sys

def make_import(path_consumer: str, path_provider: str) -> str:
	"""
	Build sys.path.append(...) + import statement if both are Python files.
	If either path does not end in .py, just print the relative path and exit.

	Args:
		path_consumer: path to the Python file that will do the import
		path_provider: path to the Python file or package (__init__.py) to import

	Returns:
		str: import boilerplate, or relative path string (if non-.py)
	"""
	consumer_dir = os.path.dirname(os.path.abspath(path_consumer))
	provider_abs = os.path.abspath(path_provider)

	# if either isn't a .py file → just relative path
	if not path_consumer.endswith(".py") or not path_provider.endswith(".py"):
		rel_path = os.path.relpath(provider_abs, consumer_dir)
		print(rel_path)
		sys.exit(0)

	provider_dir = os.path.dirname(provider_abs)
	provider_filename = os.path.basename(provider_abs)

	module_name, ext = os.path.splitext(provider_filename)
	is_package = (module_name == "__init__")

	# Build relative path for sys.path.append
	rel_to_provider = os.path.relpath(provider_dir, consumer_dir)
	steps = [] if rel_to_provider == "." else rel_to_provider.split(os.sep)

	join_expr_parts = ["os.path.dirname(__file__)"] + [f"'{s}'" for s in steps]
	join_expr = ", ".join(join_expr_parts)
	sys_path_line = f"sys.path.append(os.path.abspath(os.path.join({join_expr})))"

	# Build import statement (always flat, no dots)
	if is_package:
		import_stmt = f"import {os.path.basename(provider_dir)}"
	else:
		import_stmt = f"from {module_name} import {module_name}"

	out = [
		"import sys, os",
		sys_path_line,
		import_stmt
	]
	return "\n".join(out)







import re

# from _rightThumb._base3.library.code.classes.PythonCodeColorizer import PythonCodeColorizer





# Spaces
iFn = '''
def iName(*args, **kwargs):
	import importlib.util
	if 'iName' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'iFullPath')
		spec = importlib.util.spec_from_file_location('iName', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['iName'] = module.iName
	return intelligent_code.functions['iName'](*args, **kwargs)
'''.strip().replace('    ', '\t')
iClass = '''
class iName:
	def __new__(cls, *args, **kwargs):
		import importlib.util
		if 'iName' not in intelligent_code.classes:
			import importlib.util
			path = os.path.normpath(_v.w+'iFullPath')
			spec = importlib.util.spec_from_file_location('iName', path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			intelligent_code.classes['iName'] = module.iName
		return intelligent_code.classes['iName'](*args, **kwargs)
'''.strip().replace('    ', '\t')
iVar = '''
def iName():
	import importlib.util, os
	if not hasattr(intelligent_code, "variables"):
		intelligent_code.variables = {}
	if "iName" not in intelligent_code.variables:
		file_path = os.path.normpath(_v.w + "iFullPath")
		module_name = "iName"
		spec = importlib.util.spec_from_file_location(module_name, file_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.variables["iName"] = module.iName
	return intelligent_code.variables["iName"]
'''.strip().replace('    ', '\t')

template = '''

_intelligent_code_ = {
	"functions": {},
	"classes": {},
	"variables": {}
}

def loadFunction( name, path, load=None ):
	global _intelligent_code_
	if not hasattr( _intelligent_code_, "functions" ):
		_intelligent_code_["functions"] = {}
	if name in _intelligent_code_["functions"]:
		return _intelligent_code_["functions"][ name ]
	if name not in _intelligent_code_["functions"]:
		import importlib.util
		path = os.path.normpath( _v.w + path )
		spec = importlib.util.spec_from_file_location( name, path )
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module( module )
		if load is None: load = name
		_intelligent_code_["functions"][ name ] = eval( 'module.' + load )
	return _intelligent_code_["functions"][ name ]

def loadClass( name, path, load=None ):
	global _intelligent_code_
	if not hasattr( _intelligent_code_, "classes" ):
		_intelligent_code_["classes"] = {}
	if name in _intelligent_code_["classes"]:
		return _intelligent_code_["classes"][ name ]
	if name not in _intelligent_code_["classes"]:
		import importlib.util
		path = os.path.normpath( _v.w + path )
		spec = importlib.util.spec_from_file_location( name, path )
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module( module )
		if load is None: load = name
		_intelligent_code_["classes"][ name ] = eval( 'module.'+load )
	return _intelligent_code_["classes"][ name ]

def loadVariable( name, path, load=None ):
	global _intelligent_code_
	if not hasattr( _intelligent_code_, "variables" ):
		_intelligent_code_["variables"] = {}
	if name in _intelligent_code_["variables"]:
		return _intelligent_code_["variables"][ name ]
	if name not in _intelligent_code_["variables"]:
		import importlib.util, os
		file_path = os.path.normpath( _v.w + path )
		module_name = name
		spec = importlib.util.spec_from_file_location( module_name, file_path )
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module( module )
		_intelligent_code_["variables"][ name ] = eval( 'module.'+load )
	return _intelligent_code_["variables"][ name ]
'''.strip().replace('    ', '\t')





minFn = '''
def iName(*args, **kwargs):
	return loadFunction(
		'iName',
		'iFullPath'
	)(*args, **kwargs)
'''.strip().replace('    ', '\t')

minClass = '''
class iName:
	def __new__(cls, *args, **kwargs):
		return loadClass(
			'iName',
			'iFullPath',
		)(*args, **kwargs)
'''.strip().replace('    ', '\t')

minVar = '''
def iName(*args, **kwargs):
	return loadVariable(
		'iName',
		'iFullPath',
	)(*args, **kwargs)
'''.strip().replace('    ', '\t')





minFn = '''
def iName(*args, **kwargs):
	return loadFunction( 'iName', 'iFullPath' )(*args, **kwargs)
'''.strip().replace('    ', '\t')

minClass = '''
class iName:
	def __new__(cls, *args, **kwargs):
		return loadClass( 'iName', 'iFullPath' )(*args, **kwargs)
'''.strip().replace('    ', '\t')

minVar = '''
def iName(*args, **kwargs):
	return loadVariable( 'iName', 'iFullPath' )(*args, **kwargs)
'''.strip().replace('    ', '\t')








if _.switches.isActive('Minimal'):
	iFn = minFn
	iClass = minClass
	iVar = minVar


iFnPath='from iPath import iName'
iFnPath='from iPath import'

iClassPath='from iPath import iName'
iClassPath='from iPath import'

iVarPath='from iPath import iName'
iVarPath='from iPath import'


_copy = _.regImp( __.appReg, '-copy' )

import os
# from _rightThumb._base3.library.classes.index import index as live
def action():
	if _.switches.isActive('SysPath'):
		# _copy.imp.copy(  )
		paths = _.switches.values('SysPath')
		res = make_import(*paths)

		_copy.imp.copy(res)
		return

	# colorizer = PythonCodeColorizer()
	# print(colorizer.colorize(sample_code))
	files = []

	# if _.switches.isActive('Path'):
	# 	if not _.switches.values('Path'):
	# 		_.switches.val('Path','value','m')
	# 		_.switches.val('Path','values',['m'])
	if _.switches.isActive('Files'):
		files = _.switches.values('Files')
	elif _.isData():
		files = _.isData()
	else:
		folder = os.getcwd()
		if _.switches.isActive('Folder'):
			folder = _.switches.value('Folder')
		if not folder: folder = os.getcwd()
		files = _.fo(folder,r=_.switches.isActive('Recursive'))


	global iFn
	global iFnPath
	global iClass
	global iClassPath
	global iVarPath
	isData = []
	for path in files:
		# print(path)
		path = __.path(path)
		# print(path)
		# continue
		if not os.path.isfile(path): continue
		if not _.switches.isActive('Files'):
			if not _.showLine(path): continue
		if '__pycache__' in path: continue
		if os.sep+'backup'+os.sep in path and not 'os' in path and not 'file' in path: continue
		isData.append(path)

	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	# print(isData)
	for path in isData:
		
		path = __.path(path)
		
		if len(isData) > 1:
			if not _.switches.isActive('PrintClean'):
				_.pr()
				_.pr(line=1)
				_.pr(path,c='green')
		# try:



	
		relevant = []
		parts = path.split(os.sep)
		active = False
		for part in parts:
			if part == '_rightThumb' or part == 'library':
				active = True
			if active:
				relevant.append(part)
		iPath = '.'.join(relevant)
		iPath = iPath[0:len(iPath)-len('.py')]
		isClass = False
		
		if 'library.classes' in iPath:
			isClass = True
		# print(relevant)
		# print(relevant)
		iName = relevant[-1].replace('.py','')
		iName = iName[0:len(iPath)-len('.py')]
		oName = iName
		# print(iName)





		# impPath = impPath.replace('library.python.', '')
		# iCode = iCode.replace('iPath',iPath)
		# iCode = iCode.replace('iName',iName)

		# if '.__init__ import  __init__' in impPath:
		# 	impPath = impPath.replace('.__init__ import  __init__', ' as imp')
		# 	impPath = impPath.replace('from ', 'import ')
		# if '.__init__ import __init__' in impPath:
		# 	impPath = impPath.replace('.__init__ import __init__', ' as _')
		# 	impPath = impPath.replace('from ', 'import ')
		
		# if _.switches.isActive('Tabs'):
		# 	iCode = iCode.replace('    ', '\t')
		
		# if _.switches.isActive('Spaces')  or  len(isData) > 1:
		# 	iCode = iCode.replace('\t', '    ')

		if _.switches.isActive('Variable'):
			iCode = iVar
			if _.switches.values('Variable'):
				iName = _.switches.value('Variable')
			iCode = iVar
			impPath = iVarPath.replace('iPath',iPath).replace('iName',iName)
		elif isClass or _.switches.isActive('Class'):
			# print('isClass')
			iCode = iClass
			impPath = iClassPath.replace('iPath',iPath).replace('iName',iName)
		else:
			iCode = iFn
			impPath = iFnPath.replace('iPath',iPath).replace('iName',iName)

		
		# colorized = colorizer.colorize(iCode)
		
		# if _.switches.isActive('Path'):
		if True:
			file = _.getText(path,raw=True)
			file = file.replace('    ','\t')
			objects = []
			basic = []
			classes = []
			functions = []
			All = []
			# print(file)
			for line in file.split('\n'):
				line = line.split('#')[0].rstrip()
				# st = line.strip()
				st = line

				if st.startswith('class '):
					isClass = True
					name = st[6:].split('(')[0].split(':')[0].strip()
					if any(x in _.switches.value('Path') for x in ['c', 'all']) or _.switches.value('Path') == '':
						classes.append(name)
						objects.append(name)
						basic.append(name)
						All.append(name)

				elif st.startswith('def '):
					name = st[4:].split('(')[0].strip()
					# print(name)
					if not _.switches.isActive('Path') or any(x in _.switches.value('Path') for x in ['c', 'all']):
						functions.append(name)
						objects.append(name)
						basic.append(name)
						All.append(name)

				elif '=' in st and not st.startswith('def ') and not st.startswith('class '):
					left = st.split('=')[0].strip()
					if not any(c in left for c in ['[', '(', '{']) and not line.startswith((' ', '\t')):
						if any(x in _.switches.value('Path') for x in ['v', 'all']):
							objects.append(left)
						All.append(left)


			# for line in file.split('\n'):
			# 	line = line.split('#')[0]
			# 	st = line.strip()
			# 	if line.startswith('class '):
			# 		isClass = True
			# 		# print(line)
			# 		if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path') or _.switches.value('Path') == '':
			# 			# print(line)
			# 			objects.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 			basic.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 			All.append(st.split('class ')[1].split('(')[0].split(':')[0].strip())
			# 	elif line.startswith('def '):
			# 		if 'c' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
			# 			objects.append(st.split('def ')[1].split('(')[0].strip())
			# 			basic.append(st.split('def ')[1].split('(')[0].strip())
			# 			All.append(st.split('def ')[1].split('(')[0].strip())
			# 	elif '='  in line  and not st.startswith('def ') and not '[' in line.split('=')[0] and not '(' in line.split('=')[0]:
			# 		if not line.startswith('\t') and not line.startswith(' '):
			# 			if 'v' in _.switches.value('Path') or 'all' in _.switches.value('Path'):
			# 				objects.append(st.split('=')[0].strip())
			# 			# All.append(line)
			# 			All.append(st.split('=')[0].strip())

			if not basic:
				objects = All
				if len(_.switches.value('Path')):
					_.switches.fieldSet('Path','value','all')
			if '.__init__' in impPath:
				impPath = impPath.replace('.__init__', '')
				# impPath = impPath.replace('from ', 'import ')
			if '.__init__ import __init__' in impPath:
				impPath = impPath.replace('.__init__ import __init__', ' as _')
				# impPath = impPath.replace('from ', 'import ')
			# for o in objects: print(o)
			# return None
			# impPath = _.tailpop(impPath,' ')

			# print(objects)
			objs = []
			for o in objects:
				# print(o)
				if _.switches.isActive('Files'):
					if _.showLine(o):
						objs.append(o)
				else:
					objs.append(o)
			objectItems = '  '+', '.join(objs)

			# print(All)

			if len(_.switches.value('Path')):
				# print(impPath)
				if not objects:
					# impPath += '  '+ iName
					objects = '  '+ iName
				else:
					objs = []
					for o in objects:
						if _.switches.isActive('Files'):
							objs.append(o)
						else:
							if _.showLine(o):
								objs.append(o)
					objects = '  '+', '.join(objs)
					# impPath += '  '+', '.join(objs)
			else:
				# print(impPath)
				if not basic:
					# impPath += '  '+ iName
					objects = '  '+ iName
				elif iName in basic:
					# impPath += '  '+ iName
					objects = '  '+ iName
				else:
					# impPath += '  '+ basic[0]
					objects = '  '+ basic[0]
			impPath += objectItems
			impPath = impPath.replace('import  __init__','as ')
			if _.switches.isActive('Path'):
				print(impPath)
				_copy.imp.copy( impPath, p=0 )
		# else:


		
		if True:

			if oName in functions:
				isClass = False

			
			if isClass or _.switches.isActive('Class'):
				iCode = iClass
				iName = classes[0]

			if oName in classes:
				# print('oName in All')
				iName = oName
			elif oName in functions:
				iName = oName
			# print(All)
			# iCode = iCode.replace('iName', 'asdf')
			if _.switches.isActive('EnforceName'):
				iCode = iCode.replace('iName', _.switches.value('EnforceName'))
			else:
				iCode = iCode.replace('iName', iName)

			iCode = iCode.replace('iFullPath', __.wPath(path))

			if _.switches.isActive('Variable'):
				iCode = iVar.replace('iName', _.switches.value('Variable'))
				iCode = iCode.replace('iFullPath', __.wPath(path))


			_.pyColor(iCode)
			# print(iCode)
			_copy.imp.copy( iCode, p=0 )





		# except Exception as e:
		# 	_.e(e,path)
		# if len(isData) > 1:
		# 	_.pr()
		# 	_.pr(line=1)




_copy = _.regImp( __.appReg, '-copy' )


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)