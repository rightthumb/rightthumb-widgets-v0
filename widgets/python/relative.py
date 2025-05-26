import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','Show Only Files' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Clean', '--c' )
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

def action():
	folder = os.getcwd()+os.sep
	folderSelf = os.getcwd()
	paths = []
	for item in _.isData(r=0):
		if not _.showLine(item): continue
		# relative = item.lstrip(folder)
		relative = item.replace(folder,'')
		if _.switches.isActive('Files'):
			if not os.path.isfile(relative): continue
		if not os.path.exists(relative): continue
		if relative == folderSelf: relative = '.'+os.sep
		if relative:paths.append(relative)
	paths.sort()
	for path in paths:
		_.showLine(path,c=1)
		_.pr(_.sl)
	if not _.switches.isActive('Clean'):
		_.pr()
		_.pr('',len(paths),c='yellow')
		_.pr()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)