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
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'secure_vnc.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'secure vnc, used on phone',
	'categories': [
						'vnc',
						'secure',
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
						'p thisApp -file file.txt',
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
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
########################################################################################
# START

import importlib
ip_app = _v.py + _v.slash + 'ip.py'
# _.pr(  os.path.isfile(ip_app) ,  ip_app )
# ip = importlib.import_module( ip_app )

import importlib.util
spec = importlib.util.spec_from_file_location("module.name", ip_app)
ip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ip)


def secure_vnc():
	global ip
	global octets

	myip = ip.action()
	isLocal = False
	for octet in octets:
		if myip.startswith( octet+'.' ):
			isLocal = True
	if isLocal:
		_.pr( 'local network, safe', myip )
		log.append( 'local network, safe, '+myip )
		_.saveTable( log, 'secure_vnc.json' )
	else:
		log.append( 'NOT local network, unsafe, '+ myip )
		_.saveTable( log, 'secure_vnc.json' )
		_.pr( 'NOT local network, unsafe, FIXING' )
		time.sleep(.5)
		subprocess.call(['sh', '/opt/RightThumb/tech/programs/bash/secure_vnc.sh'])
		# toggle_comment -f /etc/vnc.conf -label vnc
		

def action():
	global log
	try:
		log = _.getTable('secure_vnc.json')
	except Exception as e:
		log = []
	
	log.append( "" )
	log.append( "" )
	log.append( _.friendlyDate(time.time()) )
	
	global isActive
	table_file = _v.myConfig +_v.slash+ '.toggle_comment.hash'
	try:
		table = _.getTable2( table_file )
	except Exception as e:
		table = {}
	if 'vnc' in table:
		key = list(table['vnc'].keys())[0]
		status = table['vnc'][key]
		if int(status) == isActive:
			_.pr( 'public' )
			log.append( 'public' )
			secure_vnc()
		else:
			_.pr( 'private, safe', status )
			log.append( 'private, safe' )
			_.saveTable( log, 'secure_vnc.json' )

import subprocess
log = None
isActive = 1
octets = [ '192', '10' ]
# octets = [ '100', '10' ]

########################################################################################
if __name__ == '__main__':
	action()







