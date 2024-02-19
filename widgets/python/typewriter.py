import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Type', '-i,-t,-w,-type,-write' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'typewriter.py',
	'description': 'Type / Keypress',
	'categories': [
						'typing',
						'type',
						'keypress',
						'keydown',
				],
	'examples': [
						_.hp('p typewriter -t type this'),
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

from pynput.keyboard import Key, KeyCode, Controller
keyboard = Controller()

def type(data):
	global keyboard
	for t in data:
		if t == '\n':
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
		elif t == '\t':
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
		elif t == '\r':
			keyboard.press(Key.esc)
			keyboard.release(Key.esc)
		else:
			keyboard.press(t)
			keyboard.release(t)
replace = {
	'\\n': '\n', 
	'\\t': '\t', 
	'\\e': '\r', 
}

def action():
	global keyboard
	global replace
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)
	i=0
	keyboard.release(Key.alt)
	keyboard.release(Key.tab)
	time.sleep(.5)
	text = ' '.join(_.switches.values('Type'))
	text = text.replace('\r','')
	for r in replace:
		text = text.replace(r,replace[r])
	type(text)


import time

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);