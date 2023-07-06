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

import os
import sys
import time
# import platform
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
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'this_distro.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'register distro',
	'categories': [
						'register',
						'distro',
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
						'p this_distro ',
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
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



def action():
	if _.isWin:
		do = "systeminfo | p line --c + \"OS Name\" -p ;. 1 | p line --c > " + _v.tmpf
		os.system('"' + do + '"')
		thisDistro = _.getText( _v.tmpf, raw=True, clean=2 )
		_.saveText( thisDistro, _v.configFile('.distro') )
		_.pr( thisDistro )
		

	elif not _.isWin:
		import csv
		RELEASE_DATA = {}
		if os.path.isfile('/etc/os-release') and os.path.isfile('/etc/debian_version'):
			with open('/etc/os-release') as f:
				reader = csv.reader(f, delimiter="=")
				for row in reader:
					if row:
						RELEASE_DATA[row[0]] = row[1]
			thisDistro = RELEASE_DATA["NAME"]
			if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
				with open('/etc/debian_version') as f:
					DEBIAN_VERSION = f.readline().strip()
				major_version = DEBIAN_VERSION.split(".")[0]
				version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
				if version_split[0] == major_version:
					# Just major version shown, replace it with the full version
					RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])
				thisDistro = "{} {}".format(RELEASE_DATA["NAME"], RELEASE_DATA["VERSION"])
		elif os.path.isfile('/proc/version'):
			thisDistro = _.getText( '/proc/version', raw=True, clean=2 )
		_.saveText( thisDistro, _v.configFile('.distro') )
		_.pr(thisDistro)




########################################################################################
if __name__ == '__main__':
	action()







