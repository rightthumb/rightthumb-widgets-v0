import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'FullPath', '-f' )
	_.switches.register( 'Missing', '-m' )

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'folderFlag.py',
	'description': 'Pipe a list of files and folders, this will print all and colorize matches',
	'categories': [
						'files',
						'folders',
						'tool',
						'research',
				],
	'examples': [
						_.hp('cat files_folders.txt | p folderFlag'),
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

__.folderFlag = []

import os
def list_files_and_folders(
	colorize=[],
	recursive=False,
	fullpath=False
):
	new = []
	for i,item in enumerate(colorize):
		item = item.replace('"','')
		item = item.replace("'",'')
		item = item.strip()
		if item:
			new.append(item)
	colorize = new
	

	def print_item(item_path):
		if should_colorize(item_path):
			_.pr(item_path, c='yellow')
		else:
			__.folderFlag.append(item_path)
			_.pr(item_path,c='red')

	def should_colorize(item):
		item = item.strip()
		item_abs = os.path.abspath(item)
		if _.switches.isActive('StrictCase'):
			return any(
				os.path.abspath(x) == item_abs or
				os.path.normpath(x) == os.path.normpath(item) or
				os.path.basename(x) == os.path.basename(item)
				for x in colorize
			)
		else:
			return any(
				os.path.abspath(x).lower() == item_abs.lower() or
				os.path.normpath(x).lower() == os.path.normpath(item).lower() or
				os.path.basename(x).lower() == os.path.basename(item).lower()
				for x in colorize
			)

	def handle_directory(path):
		files = []
		folders = []
		entries = os.listdir(path)
		for entry in sorted(entries):
			full_entry = os.path.join(path, entry)
			if os.path.isfile(full_entry):
				files.append(full_entry)
			elif os.path.isdir(full_entry):
				folders.append(full_entry)
		for f in files:
			display = f if fullpath else os.path.relpath(f)
			print_item(display)
		_.pr(line=1, c='cyan')
		for d in folders:
			display = d if fullpath else os.path.relpath(d)
			print_item(display)
	if recursive:
		for root, dirs, files in os.walk('.'):
			for name in sorted(files):
				path = os.path.join(root, name)
				display = os.path.abspath(path) if fullpath else os.path.relpath(path)
				print_item(display)
			for name in sorted(dirs):
				path = os.path.join(root, name)
				display = os.path.abspath(path) if fullpath else os.path.relpath(path)
				print_item(display)
	else:
		handle_directory('.')
		
def action():
	items = []
	for line in _.isData():
		line = line.strip()
		items.append(line)

	list_files_and_folders(items, _.switches.isActive('Recursive'), _.switches.isActive('FullPath'))
	if _.switches.isActive('Missing'):
		_.pr(line=True,c='purple')
		for item in _.isData():
			if item.strip().lower() not in __.folderFlag:
				_.pr(item, c='purple')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)