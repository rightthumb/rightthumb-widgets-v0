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
	pass



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'acquire_lunar_calendar.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Extract lunar calendar from online resources',
	'categories': [
						'scrape',
						'lunar',
						'front end',
						'frontend',
						'calendar',
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
						'p acquire_lunar_calendar',
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

_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )

def processYear( year ):
	global code
	global data
	url = 'https://lunaf.com/lunar-calendar/'+str(year)+'/'

	_.colorThis( [  '\n\n', year,'\t', url, '\n\n'  ], 'green' )


	error = False
	payload = []
	_browser.imp.project.open( url )
	_browser.imp.project.wait()
	_browser.imp.project.jqueryInject()
	_browser.imp.project.inject( code )
	# _browser.imp.project.wait()
	payload = _browser.imp.project.injectReturn( 'return window.hackData.process();' )
	_.printVarSimple( payload )

	# try:
	#     _browser.imp.project.open( url )
	#     _browser.imp.project.wait()
	#     _browser.imp.project.jqueryInject()
	#     _browser.imp.project.inject( code )
	# except Exception as e:
	#     error = True
	# payload = []
	# try:
	#     payload = _browser.imp.project.injectReturn( 'window.hackData.process();' )
	# except Exception as e:
	#     error = True
		

	if type(payload) == list:
		data[year] = []
		if not len(payload):
			_.pr('Blank')
			error = True
		for x in payload:
			data[year].append(x)

	if error:
		_.colorThis( [ 'Error: Bad Year,', year ], 'red' )
	_.saveTableDB( data, 'lunar_calendar.json' )

def action():
	global data
	load()
	year = 2000
	yearMax = 2003
	yearMax = 2040

	while not year == yearMax:
		year+=1
		processYear( year )
	



	_browser.imp.project.close()
	# _.printVarSimple( data )


def load():
	global code
	code = _.getText( _v.myAppsJs + _v.slash+'acquire_lunar_calendar.js', raw=True )
	# _.pr(code)


code = ''
data = {}



########################################################################################
if __name__ == '__main__':
	action()







