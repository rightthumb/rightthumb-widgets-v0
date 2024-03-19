import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Type', '-i,-w,-type,-write' )
	_.switches.register( 'Template', '-t,-tmp,-temp,-template' )
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

def typewriter(data):
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
	global template
	global parts
	keyboard.press(Key.alt)
	keyboard.press(Key.tab)
	# time.sleep(.001 )
	keyboard.release(Key.alt)
	keyboard.release(Key.tab)
	time.sleep(.5)
	if _.switches.isActive('Template'):

		for item in _.switches.values('Template'):
			if item in template:
				typewriter(template[item])
			if item in parts:

				for it in parts[item]:
					print(type(it))
					if type(it) == int:
						time.sleep(it)
					else:
						typewriter(it)
						typewriter('\n')
			
	text = ' '.join(_.switches.values('Type'))
	text = text.replace('\r','')
	for r in replace:
		text = text.replace(r,replace[r])
	type(text)
_keychain = _.regImp( __.appReg, 'keychain' )
__.keychain_copy=False
template = {}
template['fi']='''
for path in _.fi():
	_.pr(path)
'''.strip()

# \\

template['btn']='''
@echo off
call D:\\.rightthumb-widgets\\widgets\\batch\\c-mini.bat
call p typewriter -t fi
@REM call p typewriter -type echo test
'''.strip()

template['mklink']='''
mklink /D d s
'''.strip()

template['url']='''
https://s2.webigami.com/c/htmlos/.52834/postdata/sysint/Qqqjc1b9XWtmsKo-ih91IBVTuG7SF0ljWzxkIwKEG88vTff7sVWYiccSIdspI.html
'''.strip()

# \\

parts={}
parts['in.'] = [
	'curl -s "https://sds.sh/a/repo/?api=09c771b8&fi=vps-bashrc_extended.sh" > /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh; chmod +x /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh;',
]
parts['.git.'] = [
	'cd /opt',
	1,
	'rm -rf /opt/rightthumb-widgets-v0',
	1,
	'git clone https://github.com/rightthumb/rightthumb-widgets-v0',
	6,
	'curl -s "https://sds.sh/a/repo/?api=09c771b8&fi=vps-bashrc_extended.sh" > /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh',
	2,
	'chmod -R 777 /opt/rightthumb-widgets-v0',
	1,
	'load',
	3,
	'vps.y.d',
	3,
	_keychain.imp.key('root')

]

parts['vps-bashrc_extended']=[
	'copy /y D:\\.rightthumb-widgets\\widgets\\bash\\vps-bashrc_extended.sh D:\\websites\\domains\\sds.sh\\public_html\\a\\repo\\_files_\\',
	1,
	'u. D:\\websites\\domains\\sds.sh\\public_html\\a\\repo\\_files_\\vps-bashrc_extended.sh'
]

parts['vps-bashrc_extended.vps']=[
	'curl -sL "https://sds.sh/a/repo/?api=09c771b8&fi=vps-bashrc_extended.sh" > /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh; /usr/bin/python3 /opt/rightthumb-widgets-v0/widgets/python/shClean.py -f /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh; chmod +x /opt/rightthumb-widgets-v0/widgets/bash/vps-bashrc_extended.sh;',
	1,
]

import time


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);