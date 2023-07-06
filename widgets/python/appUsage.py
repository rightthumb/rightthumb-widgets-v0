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
	_.switches.register( 'Specify_SRCs', '-src', 'MSI  OR  VULCAN MSI' )
	_.switches.register( 'ShowAll', '-all' )
	_.switches.register( 'Save', '-save' )



_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'appUsage.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'report on python app usage from history',
	'categories': [
						'usage report',
						'usage',
						'report',
						'python',
						'apps',
						'history',
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
						'p appUsage',
						'',
						'p appUsage -src MSI',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


def ticketsFix():
	if _.switches.isActive('Specify_SRCs'):
		SRCs = []
		for x in _.switches.values('Specify_SRCs'):
			SRCs.append(  _v.myTickets.replace( _v.computername2, x )  )
		return SRCs
	else:
		return [_v.myTickets]

def action():
	_.updateLine( '                                                                           ' )
	_.updateLine( 'Processing...' )
	_.switches.fieldSet( 'Long', 'active', True )
	counter = {}
	totalAll = 0
	python = []
	for file in os.listdir(  _v.python['src']['windows']  ):
		file = file.replace( '.PY', '.py' )
		if file.endswith( '.py' ):
			path = _v.python['src']['windows'] + _v.slash + file
			f = file.replace( '.py', '' )
			thisFile = {
							'app': f,
							'file': file,
							'path': path,
			}
			counter[  thisFile['app']  ] = 0
			# _.pr( thisFile['app'] )
			python.append( thisFile )
	pass
	for ticketSRC in ticketsFix():
		for file in os.listdir(  ticketSRC  ):
			if file.endswith( '.txt' ) and (  file.startswith('open-') or file.startswith('closed-')  ):
				path = ticketSRC + _v.slash + file
				f = file.replace( 'open-', '' )
				f = f.replace( 'closed-', '' )
				f = f.replace( '.txt', '' )
				thisFile = {
								'ticket': f,
								'file': file,
								'path': path,
				}
				# _.pr(thisFile)
				history = _.getText( thisFile['path'], raw=True ).lower()
				for app in python:
					cnt = history.count( ' '+app['app'].lower()+' ' )
					if cnt:
						counter[  app['app']  ] += cnt
						totalAll += cnt

	pass
	result = []
	for key in counter.keys():
		record = { 'app': key, 'total': counter[key], 'percentage': _.pDiff( counter[key], totalAll, 'l' ) }
		# _.updateLine( record )
		if _.switches.isActive('ShowAll'):
			result.append( record )
		else:
			if record['percentage'] :
				result.append( record )
	_.updateLine( '                                                                           ' )
	data = _.tables.returnSorted( 'data', 'd.total', result )
	_.tables.print( 'data', 'app,total,percentage' )
	GRAND_TOTAL = 0
	for rec in result:
		GRAND_TOTAL += rec['total']
	_.pr()
	_.colorThis( [ '', _.addComma(GRAND_TOTAL) ], 'green' )

	if _.switches.isActive('Save'):
		_.saveTableDB(  result, 'appUsage.json'  )


########################################################################################
if __name__ == '__main__':
	action()







