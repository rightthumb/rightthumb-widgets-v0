import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Input', '-i' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'addComma.py',
	'description': 'Used in shell scripts, batch files, etc to format numbers',
	'categories': [
						'Script Helper',
						'Batch Files',
						'Shell Scripts',
						'.sh',
						'.bat',
				],
	'examples': [
						_.hp('p addComma -i 1000000'),
						_.hp('     1,000,000'),
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

def action():
	if _.switches.isActive('Input'):
		_.pr(_.addComma(_.switches.value('Input')))
		return None
	for line in _.pp():
		_.pr(_.addComma(line))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);