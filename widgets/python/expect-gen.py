#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Continue', '-y' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Sudo', '-sudo' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'expect-gen.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate expect command to auto login',
	'categories': [
						'bash',
						'expect',
						'gen',
						'login',
						'auto',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


app = {}

app['A']="""#!/usr/bin/expect -f
set PW [lindex $argv 0]
spawn REPLACE_COMMAND
REPLACE_PROMPTS
interact"""


app['P']="""#!/usr/bin/expect -f
set PW [lindex $argv 0]
spawn REPLACE_COMMAND
expect "assword:"
send "$PW\\n"
interact"""

app['PC']="""#!/usr/bin/expect -f
set PW [lindex $argv 0]
spawn REPLACE_COMMAND
expect "ontinue"
send "yes\\n"
expect "assword:"
send "$PW\\n"
interact"""

app['C']="""#!/usr/bin/expect -f
set PW [lindex $argv 0]
spawn REPLACE_COMMAND
expect "ontinue"
send "yes\\n"
expect "assword:"
send "$PW\\n"
interact"""

def action(p=False,c=False):
	global app
	if _.switches.isActive('Password'):
		p = True
	if _.switches.isActive('Continue'):
		c = True

	if p and not c:
		appy = app['P']
	if p and c:
		appy = app['PC']
	if not p and c:
		appy = app['C']

	where = _v.rtstmp +os.sep+ 'temp.exp'
	_v.mkdir( __.path( where, pop=True ) )
	theCMD = ' '.join( _.isData(r=1) )
	theCMD = _str.cleanBE( theCMD, ' ' )
	if 's.c.s.dl' in theCMD:
		theCMD = 'sudo '+ _v.techDrive+'/tech/programs/bash/nav/p.sh cloud -sync -download'
	elif 's.c.s' in theCMD:
		theCMD = 'sudo '+ _v.techDrive+'/tech/programs/bash/nav/p.sh cloud -sync'
	if 'c.s.dl' in theCMD:
		theCMD = _v.techDrive+'/tech/programs/bash/nav/p.sh cloud -sync -download'
	elif 'c.s' in theCMD:
		theCMD = _v.techDrive+'/tech/programs/bash/nav/p.sh cloud -sync '
	if theCMD.startswith('p '):
		theCMD = theCMD[1:] + _v.techDrive+'/tech/programs/bash/nav/p.sh '
	elif theCMD.startswith('s.p '):
		theCMD = 'sudo '+ theCMD[3:] + _v.techDrive+'/tech/programs/bash/nav/p.sh '
	appy = appy.replace( 'REPLACE_COMMAND', theCMD )
	# appy = appy.replace( 'REPLACE_PROMPTS', subby )
	_.saveText(appy, where)
	_.chmod(where)
	if _.switches.isActive('Sudo'):
		_.pr( 'sudo', where )
	else:
		_.pr( where )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







