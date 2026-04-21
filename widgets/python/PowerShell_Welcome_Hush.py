import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'On', '-on', 'Enable PowerShell Welcome')
	_.switches.register( 'Off', '-off', 'Disable PowerShell Welcome')
	_.switches.register( 'Status', '-status', 'use with -clean to get single word response: on or off')
	_.switches.register( 'Clean/NoPrint', '-clean,-noPrint,--c')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'PowerShell_Welcome_Hush.py',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#N)--> START
import os
import platform

if platform.system() == "Windows":
	hush_file = os.path.join(os.getenv('USERPROFILE')+os.sep+'.rt', '.hushlogin_ps1')
else:
	hush_file = os.path.join(os.getenv('HOME')+os.sep+'.rt', '.hushlogin_ps1')

# print(f"Hush file path: {hush_file}")

def action():
	global hush_file
	if _.switches.isActive('Clean/NoPrint') and _.switches.isActive('Status'):
		_.switches.fieldSet('Status','value','Single Word Response Activated')
	if not _.switches.isActive('Clean/NoPrint'):
		if _.switches.isActive('Status') and not len(_.switches.value('Status').strip()):
			_.pr()
			_.pr(hush_file,c='yellow')
			_.pr()
	if _.switches.isActive('Status'):
		if _.switches.isActive('Status') and not len(_.switches.value('Status').strip()):
			if os.path.isfile(hush_file):
				_.pr('\tPowerShell Welcome is OFF - hush file exists', c='yellow')
			else:
				_.pr('\tPowerShell Welcome is ON - hush file does not exist',c='yellow')
		elif _.switches.isActive('Status') and len(_.switches.value('Status').strip()):
			if os.path.isfile(hush_file):
				print('off')
			else:
				print('on')
	elif _.switches.isActive('Off'):
		if not os.path.isfile(hush_file):
			with open(hush_file, 'w') as file: file.write('PowerShell Welcome Disabled')
		if not _.switches.isActive('Clean/NoPrint'):
			_.pr('\tPowerShell Welcome is now OFF - hush file exists',c='yellow')
	elif _.switches.isActive('On'):
		if os.path.isfile(hush_file):
			os.remove(hush_file)
		if not _.switches.isActive('Clean/NoPrint'):
			_.pr('\tPowerShell Welcome is now ON - hush file removed', c='yellow')
	

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);