import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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

import time
import threading
import keyboard
import platform

# Function to play a low beep sound
def play_beep(x=400):
	if platform.system() == "Windows":
		import winsound
		winsound.Beep(x, 300)  # 400 Hz, 300 ms
	else:
		import os
		os.system("play -nq -t alsa synth 0.3 sine 400")  # Linux/macOS

# Function to lock Left Ctrl for 3 seconds
def lock_ctrl():
	keyboard.press("ctrl")
	time.sleep(3)
	keyboard.release("ctrl")
	play_beep(450)

# Main loop to detect Shift key being held
def monitor_shift(threshold_ms=500):
	while True:
		if keyboard.is_pressed("ctrl+z"):
			print("Exiting...")
			break
		
		keyboard.wait("shift")
		start_time = time.time()
		while keyboard.is_pressed("shift"):
			if (time.time() - start_time) * 1000 >= threshold_ms:
				play_beep()
				threading.Thread(target=lock_ctrl).start()
				time.sleep(1)  # Prevent rapid re-triggering
				break


def action():
	monitor_shift(500)
	

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)