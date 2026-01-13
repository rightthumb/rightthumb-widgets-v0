import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Module','-m,-i,-module,-import','shutil, _construct')
	_.switches.register( 'Show-Only','-o,-only,-show','c, s, Callable, Strings')
	_.switches.register( 'List-Framework-Modules','-l,-list')

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'Import-Module-Functions.py',
	'description': 'Loads python module or framework module, then prints a searchable table of namespace and values (framework variable lookup) or Callable arguments with required and data types',
	'categories': [
						'module',
						'research',
						'programming research',
				],
	'examples': [
						_.hp('accepts python modules   OR   framework module both in python folder   OR   in _rightThumb master import folder'),
						_.hp('p Import-Module-Functions -i shutil'),
						_.hp('p Import-Module-Functions -i shutil + copy2'),
						_.hp('alias to if. in both windows and linux'),
						_.hp('if. inspect'),
						_.hp('if. importlib'),
						_.hp('if. importlib + import_module'),
						_.hp('if. importlib + __file__'),
						_.hp(''),
						_.hp('if. ssl -o c'),
						_.hp('if. ssl + '),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': ['if.'],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import re

def clean_string(text,clip=0):
	if not isinstance(text, str):
		return text

	# Remove non-printable characters
	text = ''.join(ch for ch in text if ch.isprintable())

	# Replace tabs, newlines, and carriage returns with a space
	text = re.sub(r'[\t\n\r]', ' ', text)

	# Escape special characters (optional, based on need)
	text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")

	# Strip leading/trailing whitespace
	text = text.strip()
	if clip:
		text = text[:clip] + "..." if len(text) > clip else text
	return text




import importlib
import inspect


def get_function_args(module, function_name):
	try:
		func = getattr(module, function_name)

		# Handle classes and recursively get their methods
		if inspect.isclass(func):
			methods = inspect.getmembers(func, predicate=inspect.isfunction)
			class_report = []
			for method_name, method in methods:
				signature = inspect.signature(method)
				args = [
					f"{param.name}|{'r' if param.default == inspect.Parameter.empty else param.default.__class__.__name__}"
					for param in signature.parameters.values()
				]
				class_report.append(f"  {method_name}({', '.join(args).replace('|NoneType', '|n')})")
			return "\n".join(class_report)

		# Skip submodules to avoid nested imports
		if inspect.ismodule(func):
			return "Submodule"

		# Handle functions and methods
		if callable(func):
			signature = inspect.signature(func)
			args = [
				f"{param.name}|{'r' if param.default == inspect.Parameter.empty else param.default.__class__.__name__}"
				for param in signature.parameters.values()
			]
			return ', '.join(args).replace('|NoneType', '|n')

		# Handle variables and attributes with their types
		if not callable(func):
			return f"{type(func).__name__}"

	except Exception as e:
		return "Error"


def moduleProfile(mod):
	global fw
	if mod.startswith('_') and not '_rightThumb.' in mod:
		mod = '_rightThumb.' + mod

	# Import the module
	module = importlib.import_module(mod)

	table = []
	for x in dir(module):
		yy = mod + '.' + x
		yyy = yy

		# Replace keys in the namespace if they exist in WidgetsFW
		for k in _.WidgetsFW.keys():
			yyy = yyy.replace(k, _.WidgetsFW[k])
		yyy = yyy.replace('-', '_')
		y = 'module.' + x

		try:
			z = eval(y)
			xx = x

			# Determine the type of the item
			if inspect.isclass(z):
				iAm = "Class"
				z = get_function_args(module, x)
			elif callable(z):
				iAm = "Function"
				z = get_function_args(module, x)
			elif isinstance(z, dict):
				iAm = "Dict"
				z = f"Keys: {', '.join(z.keys())}"
			elif hasattr(z, '__dict__'):
				iAm = "Object with Keys"
				z = f"Keys: {', '.join(z.__dict__.keys())}"
			elif isinstance(z, (str, int, float, bool)):
				iAm = "Attribute"
				z = str(z)
			else:
				iAm = "Unknown"

			# Apply string cleaning if it's an attribute
			if isinstance(z, str):
				z_cleaned = clean_string(z, clip=100)
			else:
				z_cleaned = z

			if _.showLine(xx):
				table.append({'type': iAm, 'ns': yyy, 'val': z_cleaned})

		except Exception as e:
			pass
			if _.showLine(xx):
				
				table.append({'type': 'Error', 'ns': yy, 'val': ''})
			# _.pr('Error:', yy, str(e))

	# Sort and display the table
	table = _.sort(table, 'type,ns')
	_.switches.fieldSet( 'GroupBy', 'active', True )
	_.switches.fieldSet( 'GroupBy', 'value', 'Type' )
	_.switches.fieldSet( 'GroupBy', 'values', ['Type'] )
	if _.switches.isActive('Show-Only'):
		show = _.switches.value('Show-Only').lower()
		if 's' in show:
			show = ['String', 'Attribute', 'Dict', 'Object with Keys', 'Keys']
		else:
			show = ['Callable', 'Function', 'Class']
		newTable = [row for row in table if row['type'] in show]
		
		table = newTable
	_.pt(table, l=1)
	_.pr()
	_.pr('|r = required', c='cyan')
	_.pr('|n = NoneType', c='cyan')
	_.pr()





def action():


	if _.switches.isActive('List-Framework-Modules'):
		if _.switches.value('List-Framework-Modules'):
			fw = _.WidgetsFW
		else:
			fw = _.WidgetsFW_Clean

		for module in fw.keys():
			# module = module.replace('_rightThumb.','')
			if _.showLine(module):
				_.pr(module)
		return


	if _.switches.isActive('Module'):
		mod = _.switches.value('Module')
		mod = mod.strip()
		if not mod:
			_.help()
		moduleProfile(mod)
	else:
		_.e('No module specified')
		# varDir()


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);