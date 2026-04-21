import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Folder', '-f', '_docs_' )
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
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import os
def delete_empty_folders(directory):
	"""
	Recursively deletes empty folders starting from the specified directory.
	"""
	for root, dirs, files in os.walk(directory, topdown=False):  # Traverse the tree from bottom up
		for dir in dirs:
			dir_path = os.path.join(root, dir)
			# If the directory is empty, remove it
			if not os.listdir(dir_path):
				try:
					os.rmdir(dir_path)
					print(f"Deleted empty folder: {dir_path}")
				except:
					print(f"Unable to delete folder: {dir_path}")

def action():
	if _.switches.isActive('Folder'):
		folder = _.switches.values('Folder')[0]
	else:
		folder = os.getcwd()
	delete_empty_folders(folder)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);