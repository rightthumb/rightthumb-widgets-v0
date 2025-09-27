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
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'fileHeader_char_builder.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'List characters in file headers',
	'categories': [
						'header characters',
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
						'p fileHeader_char_builder',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
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
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

def asciiHeader( header, p=1 ):
	try:
		return asciiHeaderRun( header, p )
	except Exception as e:
		return header

hex_header_chars = None
def asciiHeaderRun( header, p=1 ):
	global hex_header_chars
	if hex_header_chars is None:
		hex_header_chars = _.getTableDB( 'hex_header_chars.json' )
	hexHeader = []
	txtHeader = []
	for hx in header.split(' '):
		x = ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])
		if x in _str.visibleChar or x in hex_header_chars:
			txtHeader.append( x )
			hexHeader.append( hx )
		else:
			break
	if len( hexHeader ):
		if p:
			return _.colorThis( 'ASCII: ', 'cyan', p=0 ) + _.colorThis( ''.join(txtHeader), 'green', p=0 ) + '\t' +  _.colorThis( 'HEX: ', 'cyan', p=0 ) + _.colorThis( ' '.join(hexHeader), 'yellow', p=0 )
		else:
			return { 'ascii': ''.join(txtHeader), 'hex': ' '.join(hexHeader) }
	else:
		return header

def action():
	load()
	global table
	global data
	global hex_header_chars
	total = { 'good': 0, 'bad': 0 }
	for record in table:
		if record['src'] == 'filesignatures.net':

			hx = record['signature'].replace(' ','')

			try:
				header = ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])
				# _.pr(header)
				for x in header:
					if not x in data:
						data.append(x)
				_.colorThis( record['signature'], 'green' )

				total['good'] += 1
			except Exception as e:
				total['bad'] += 1
				# _.colorThis( record['signature'], 'red' )
				pass

	_.pr()
	_.pr(total)
	_.pr()
	_.pr(data)

	_.saveTableDB( data, 'hex_header_chars.json' )
	_.colorThis( 'saved: hex_header_chars.json', 'green' )

	# pause=input( '  paused hit enter  ' )

	_.pr( 'Testing...' )
	_.pr()
	_.pr()
	_.pr()

	

	for record in table:
		if record['src'] == 'filesignatures.net':
			if not 'sign' in record['signature'].lower():
				hx = asciiHeader( record['signature'] )
				_.pr( hx )





def load():
	global table
	global data
	global hex_header_chars
	table = _.getTableDB( 'hex_headers.json' )

	data = []


########################################################################################
if __name__ == '__main__':
	action()