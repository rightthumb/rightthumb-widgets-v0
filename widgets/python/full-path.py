import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Script-Save', '-script', '$stmp/full-path.tmp' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
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

from os import sep

def action():
	if not _.switches.isActive('Files'): _.e('No files specified')
	save = None
	if _.switches.isActive('Script-Save'):
		save = _v.stmp + sep + 'full-path.tmp'
	if _.switches.isActive('Save'):
		save = _.switches.value('Save')
	path = _.switches.values('Files')[0]
	path = __.path(path)
	if not _.switches.isActive('Script-Save'):
		_.pr(path,c='cyan')
	if save:
		_.saveText(path,save)
		_.pr(save,c='cyan')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);