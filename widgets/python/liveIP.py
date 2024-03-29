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
	_.switches.register( 'History', '-h,-history' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ip.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'View current ipv4 address and history',
	'categories': [
						'tool',
						'ipv4',
						'log',
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
						'p ip -history',
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
	_v.ipGet( force=True )
	_.colorThis(  ['IP:',_v.ip], 'green'  )
	if not _v.ip_old == _v.ip:
		_.colorThis(  ['previous:',_v.ip_old], 'red'  )


	if _.switches.isActive('History'):

		_.switches.fieldSet( 'GroupBy', 'active', True )
		_.switches.fieldSet( 'GroupBy', 'value', 'woy,ip' )
		_.switches.fieldSet( 'GroupBy', 'values', ['woy','ip'] )

		_.switches.fieldSet( 'Sort', 'active', True )
		_.switches.fieldSet( 'Sort', 'value', 'woy,ip,epoch' )
		_.switches.fieldSet( 'Sort', 'values', ['woy','ip','epoch'] )

		cache = _.getTable2(_v.config('.ip.hash'))
		records = []
		for ip in cache:
			for t in cache[ip]:
				records.append({   'epoch': float(t),   'ip': ip,   'woy':  str(_dir.getYearFromEpoch( float(t) )) +'.'+ str(_dir.getWOYFromEpoch(  float(t)  ))   })
		history = _.tables.returnSorted( 'data', 'd.epoch',records )
		history.reverse()
		last = history[0]['epoch']
		for i,record in enumerate(history):
			history[i]['duration_min'] = round( abs(last - record['epoch']) / 60 , 2 )
			last = history[i]['epoch']


		_.tables.fieldProfileSet( 'data', 'epoch', 'trigger', _.friendlyDate )
		_.tables.print( 'data', 'woy,ip,epoch,duration_min' )
		# _.printVarSimple( cache )

import _rightThumb._dir as _dir


########################################################################################
if __name__ == '__main__':
	action()






