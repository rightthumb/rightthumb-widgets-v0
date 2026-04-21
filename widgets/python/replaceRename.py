import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Replace', '-r,-replace' )
	_.switches.register( 'With', '-w,-with' )
	_.switches.register( 'Yes, Rename', '-y,-yes', 'Otherwise Just Prints' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'replaceRename.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('>> Alias: `rr.` <<'),
						_.hp(''),
						_.hp('p replaceRename -r 2019 -w 2020 -f *.txt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import os

def matchReplace(file):
	try:
		for i, r in enumerate(_.switches.values('Replace')):
			w = _.switches.values('With')[i]
			file = file.replace(r,w)
	except:
		_.e('Error: Replace and With must be the same length')
	return file

def action():
	# _.switches.fieldSet('Plus','active',True)
	# _.switches.fieldSet('Plus','value',_.switches.value('Replace'))
	# _.switches.fieldSet('Plus','values',_.switches.values('Replace'))
	

# p file + JsonDatabase_roles .json --c

	table = []
	if _.switches.isActive('Yes, Rename'):
		key = 'New'
	else:
		key = 'Suggested'
	for file in _.isData():
		if os.path.isfile(file):
			if _.showLine(file): continue
			print(file)
			# if _.showLine(file,_.switches.value('Replace')):
			# 	new = matchReplace(file)
			# 	table.append({'Current':file, key:new})
			# 	if _.switches.isActive('Yes, Rename'):
			# 		os.rename(file,new)
	_.pt(table)


				

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)