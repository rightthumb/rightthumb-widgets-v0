import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Bullets', '-b,-bullets' )
	_.switches.register( 'Numbers', '-n,-num,-number,-numbers' )
	_.switches.register( 'ChildrenRecursive', '-r-cr,-child,-children,-recursive' )
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


def convert_markdown(file_path, to_format="bullets", include_children=False):
	"""
	Convert Markdown bullets to numbers or numbers to bullets.
	
	Parameters:
	- file_path (str): Path to the Markdown file.
	- to_format (str): "bullets" to convert to bullets, "numbers" to convert to numbers.
	- include_children (bool): Whether to include nested lists in the conversion.
	
	Returns:
	- None: Writes the converted content back to the file.
	"""
	import re

	def is_top_level(line):
		"""Check if a line is top-level (no leading spaces or tabs)."""
		return not line.startswith("  ") and not line.startswith("\t")

	# Read the file content
	with open(file_path, 'r') as file:
		lines = file.readlines()

	converted_lines = []
	number = 1  # Start numbering from 1
	child_number = 1  # Start numbering for children if included

	for line in lines:
		stripped = line.lstrip()

		# Check if the line is top-level
		if is_top_level(line):
			# Convert top-level numbers to bullets
			if to_format == "bullets" and re.match(r'^\d+\.', stripped):
				converted_lines.append(f"- {stripped.split(maxsplit=1)[-1]}")

			# Convert top-level bullets to numbers
			elif to_format == "numbers" and stripped.startswith("- "):
				converted_lines.append(f"{number}. {stripped[2:]}")
				number += 1
			else:
				converted_lines.append(line)

		# Check nested children only if include_children is True
		elif include_children:
			# Convert nested numbers to bullets
			if to_format == "bullets" and re.match(r'^\d+\.', stripped):
				converted_lines.append(f"  - {stripped.split(maxsplit=1)[-1]}")
			
			# Convert nested bullets to numbers
			elif to_format == "numbers" and stripped.startswith("- "):
				converted_lines.append(f"  {child_number}. {stripped[2:]}")
				child_number += 1
			else:
				converted_lines.append(line)
		else:
			# Keep lines as is if they are children and include_children is False
			converted_lines.append(line)

	# Write the converted content back to the file
	with open(file_path, 'w') as file:
		file.writelines(converted_lines)

	print(f"Conversion to '{to_format}' format completed for file: {file_path}")


def action():
	do = 'bullets'
	if _.switches.isActive('Bullets'):
		do = 'bullets'
	if _.switches.isActive('Numbers'):
		do = 'numbers'
	if _.switches.isActive('Files'):
		for f in _.isData(r=1):
			convert_markdown(f, do, _.switches.isActive('ChildrenRecursive'))
			
				

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);