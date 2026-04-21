import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
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




import sys
import os

def wait_for_keypress_or_q():
	if os.name == 'nt':
		import msvcrt
		key = msvcrt.getch()
		if key in [b'q', b'Q']:
			print("\n[Exit] User pressed 'q'")
			sys.exit(0)
	else:
		import tty
		import termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setcbreak(fd)
			key = os.read(fd, 1)
			if key in [b'q', b'Q']:
				print("\n[Exit] User pressed 'q'")
				sys.exit(0)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def action():
	cnt = 0
	try:
		print('Press any key to continue, or "q" to quit.')
		
		for line in _.isData(2):
			if _.showLine(line):
				if cnt > 0:
					wait_for_keypress_or_q()
					if _.isWin:
						os.system('cls')
					else:
						os.system('clear')
				cnt += 1
			_.pr(line)
	except KeyboardInterrupt:
		print("\n[Exit] Interrupted with Ctrl+C")
		sys.exit(0)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)