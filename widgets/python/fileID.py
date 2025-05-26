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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','file.txt',  isPipe='name', description='Files' )
	_.switches.register( 'Password', '-password', 'asdf   OR   abc 123' )
	_.switches.register( 'Setting', '-setting', '128, 64, 32, 16, 8, 4' )
	_.switches.register( 'Probability_of_false_positive', '-false' )
	_.switches.register( 'Time', '-time' )
	_.switches.register( 'Resolve', '-resolve' )
 

_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'textsum.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Homemade checksum for text ',
	'categories': [
						'checksum',
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
						'p textsum -f ipsum.txt -setting 16',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START




import _rightThumb._nID as _nID
import _rightThumb._dir as _dir




def action():

	if _.switches.isActive('Resolve'):
		if _.switches.isActive('Password'):
			_nID.mini.password( _.switches.value('Password') )
		_nID.mini.gen(123)
		_.colorThis( _nID.mini.resolve( _.switches.value('Resolve') ) )
		return None

	global data

	if  _.switches.isActive('Probability_of_false_positive'):
		_.pr()
		_.colorThis( ' Probability of false positive ', 'green' )

		permutations = {
							'128': '10,573,313,306,183,500,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000',
							'64': '21,147,822,030,980,700,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000',
							'32': '57,407,133,808,466,100,000,000,000,000,000,000,000,000,000,000,000,000',
							'16': '4,243,193,364,951,970,000,000,000,000',
							'8': '4,243,193,364,951,970,000,000,000,000',
							'4': '12,524,520',
							'2': '3,660',
		}


		# https://stattrek.com/online-calculator/combinations-permutations.aspx

		_.pr()

		for key in permutations.keys():
			_.pr( '\t', _.colorThis( key, 'yellow', p=0 ), '\t', _.colorThis( permutations[key], 'red', p=0 ) )

		_.pr()
		sys.exit()

	settings = '16'
	password = None

	if _.switches.isActive('Setting') and len(  _.switches.value('Setting')  ):
		settings = _.switches.value('Setting')

	if _.switches.isActive('Password') and len(  _.switches.value('Password')  ):
		password = _.switches.values('Password')

	log = _.getTableDB( 'fileID_efficiency.index' )
	if not len( list(log.keys()) ):
		s = [ 128, 64, 32, 16, 8, 4, 2 ]
		for x in s:
			log[ str(x) ] = []
	_fileID = _nID.checksum( settings, password )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,path in enumerate( _.appData[__.appReg]['pipe'] ):
			# _.pr()
			record = _dir.fileInfo( path )
			start = time.time()
			# _.pr( data )
			# sys.exit()
			# checksum = _fileID.run( path )
			# _.pr(path)
			checksum = _fileID.file( path )
			resolved = _nID.mini.resolve(checksum)
			_.pr(checksum)
			log[settings].append({ 
										'epoch': time.time(),
										'checksum': checksum,
										'time': time.time()-start,
										'resolved': resolved,
										'settings': settings,
										'password': password,
										'record': record
			})

			if _.switches.isActive('Time'):
				_.pr(time.time()-start)
				_.pr()
			_.saveTableDB( log, 'fileID_efficiency.index' )


		# _.pr()
		# _.pr( len(checksum) )






data = ''



########################################################################################
if __name__ == '__main__':
	action()






