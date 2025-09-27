import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Save', '-save,-f', 'to.txt || aliasName' )
	_.switches.register( 'Move', '-move,-m', 'from.txt || aliasName' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'pSave.py',
	'description': 'Pipe Save',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('pa | p pSave -file file.txt'),
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

import sys

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	if '-move' in sys.argv or '-m' in sys.argv:
		_.aliasesDefault = 'fo'
		_.switches.trigger( 'Save', _.aliases )
	else:
		_.switches.trigger( 'Save', _.aliasesFi )
	_.switches.trigger( 'Move', _.isFileAdvanced )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def action():

	if _.switches.isActive('Move'):
		for file in _.switches.values('Move'):
			_.pr(file,c='yellow')
			to = _.switches.value('Save')
			import shutil
			shutil.move(file,to)
			_.pr('Moved:\n\t',file,'\nTo:\n\t',to, c='green')
		return
		

	_.isDataClip(__.appReg)
	data = '\n'.join(_.isData(2))
	data = data.replace('\r','')
	data = data.replace('\n\n','\n')
	if _.switches.isActive('Save') and _.isData(2):
		_.saveText(data, _.switches.value('Save'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)