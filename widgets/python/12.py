import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
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


import os
one_text = _.getText(_v.stmp + os.sep + 'hotkeys-save_clip_1')
two_text = _.getText(_v.stmp + os.sep + 'hotkeys-save_clip_2')
one = [line.strip() for line in one_text if line.strip()]
two = [line.strip() for line in two_text if line.strip()]
set_one = set(one)
set_two = set(two)
common = sorted(set_one & set_two)
only_in_one = sorted(set_one - set_two)
only_in_two = sorted(set_two - set_one)
print('✅ In both:')
for item in common:
	print('   ', item)
print('\n❌ Only in first:')
for item in only_in_one:
	print('   ', item)
print('\n❌ Only in second:')
for item in only_in_two:
	print('   ', item)

########################################################################################
def action():
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)