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
	pass
	### EXAMPLE: START
	_.switches.register( 'Miles', '-miles', '200' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


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

import geopy.distance


def km2US(kilometers):
	# Taking kilometers input from the user
	kilometers = float(kilometers)

	# conversion factor
	conv_fac = 0.621371

	# calculate miles
	miles = kilometers * conv_fac
	# _.pr('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
	return miles

def findDistance2( lon, lat, distance, what='lat' ):
	pass

def findDistance( lon, lat, distance, what='lat' ):

	def testThisFloat( n, ud, test=0 ):
		if 'u' in ud:
			while test < distance:
				coordinates['one'][what] += n
				result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
				test = km2US(result)
				# _.pr( test )

		elif 'd' in ud:
			while test > distance:
				coordinates['one'][what] -= n
				result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
				test = km2US(result)
				# _.pr( test )
		return test


	# coords_1 = (48.671342, -124.701721)
	# coords_2 = (48.671342, -120.3073058)
	coordinates = {
					'one': {
								'lon': lon,
								'lat': lat,
					},
					'two': {
								'lon': lon,
								'lat': lat,
					},
	}
	global direction
	direction = 'down'

	def toggleDirection():
		global direction
		if direction == 'up':
			direction = 'down'
		else:
			direction = 'up'
		return direction

	global by
	by = 100

	def modBy():
		global by
		by = int( str(by).replace( '1', '10' )  )
		return 1/by
	
	ix = 0
	test = 0
	while test < distance:
		ix+=1
		test = testThisFloat( ix, toggleDirection() )

	if test == distance:
		return coordinates['two']
	

	while not test == distance:
		if by == 100000000000000:
			break
		# _.pr()
		# _.pr( str(by), coordinates['two'] )
		test = testThisFloat( modBy(), toggleDirection(), test )

	if test > distance:
		test = testThisFloat( 1/by, 'down', test )
	# _.pr(coordinates['two'])
	return coordinates['one'][what]


	# while test < distance:
	#     coordinates['one'][what] += 1

	#     result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
	#     test = km2US(result)
	#     _.pr( test )


	# if test == distance:
	#     return coordinates['two']

	# _.pr()

	# while test > distance:
	#     coordinates['one'][what] -= .001

	#     result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
	#     test = km2US(result)
	#     _.pr( test )

	# if test == distance:
	#     return coordinates['two']

	# _.pr()

	# while test < distance:
	#     coordinates['one'][what] += .0001

	#     result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
	#     test = km2US(result)
	#     _.pr( test )

	# sys.exit()
	# if test == distance:
	#     return coordinates['two']

	# _.pr()

	# while not test > distance:
	#     coordinates['one'][what] += .00001

	#     result =  geopy.distance.vincenty( (  coordinates['one']['lon'], coordinates['one']['lat']  ) , (  coordinates['two']['lon'], coordinates['two']['lat']  )  ).km
	#     test = km2US(result)
	#     _.pr( test )

	# print

def genLon():
	global base
	global miles
	lon = base['start']['lon']
	lat = base['start']['lat']
	
	# _.pr( lon, lat )
	while lon < base['end']['lon']:
		_.pr()
		genLat( lon, lat )
		lon = findDistance( lon, lat, miles, what='lon' )

def genLat( lon, lat ):
	global data
	global base
	global miles


	while lat < base['end']['lat']:
		lat = findDistance( lon, lat, miles, what='lat' )
		_.pr( lon, lat )
		# sys.exit()
		data.append( (lon,lat) )

def action():
	global data
	load()
	genLon()
	

def load():
	global data
	global miles
	global base
	miles = int( _.switches.value('Miles') )
	base =     {
						'start' : {
							'lon': 25.4492618,
							'lat': -124.701721,
						},
						'end' : {
							'lon': 48.671342,
							'lat': -65.5909714,
						},
	}
	data.append( ( base['start']['lon'], base['start']['lat'] ) )

data = []

########################################################################################
if __name__ == '__main__':
	action()