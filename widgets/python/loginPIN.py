import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'SaveHash', '-save', isRequired=False )
	_.switches.register( 'SecureDeleteHash', '-del,-delete,-secure-delete', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'loginPIN.py',
	'description': 'Login PIN',
	'categories': [
						'login',
						'pin',
				],
	'examples': [
						_.hp('p loginPIN'),
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
	try:
		pin = _v.vaultPinLogin()
		_.saveText(pin, _v.pinTemp)
	except KeyboardInterrupt:
		print('\n[Ctrl+C detected] Exiting...')
		_.isExit(__file__)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);