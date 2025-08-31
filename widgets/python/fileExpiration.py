import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )
	_.switches.register( 'Expiration', '-e,-x,-ex,-expire,-m,-min,-minutes,-expiration' )
	_.switches.register( 'Clear', '-clear' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'fileExpiration.py',
	'description': 'Clear a file if it is expired',
	'categories': [
						'file',
						'Expiration',
				],
	'examples': [
						_.hp('p fileExpiration -f file.txt -e 5'),
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

import os
import time

def process(path, min, clear):
	path = __.path(path)
	try:
		# Get the current time in seconds
		current_time = time.time()
		
		# Get the last modification time of the file
		mod_time = os.path.getmtime(path)
		
		# Calculate the age of the file in minutes
		age_minutes = (current_time - mod_time) / 60
		
		# If the file is older than 'min' minutes, clear its contents
		if age_minutes > min:
			print(f"Expired")
			if clear:
				open(path, 'w').close() # This opens the file in write mode and immediately closes it, clearing its contents.
				print(f"Cleared")
		else:
			print(f"Valid")
	except FileNotFoundError:
		print(f"File '{path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")


def action():
	if _.switches.isActive('Expiration'):
		expiration = int(_.switches.value('Expiration'))
	else:
		expiration = 30
	for path in _.switches.values('Files'):
		process(path, expiration, _.switches.isActive('Clear'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);