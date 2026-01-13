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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._encryptString as _blowfish
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Folder', '-folder','D:\Picture_Project')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'exif.py',
	'description': 'Acquire exif data',
	'categories': [
						'exif',
						'file'
						'meta'
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
						'type %tmpf0% | p exif -folder D:\Picture_Project',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# os.system('"' + do + '"')
########################################################################################
# START

def exif( doThis, qID=False ):
	global isSingle
	try:
		if isSingle:
			doThis += '>' + _v.json_temp
			os.system('"' + doThis + '"')
			var = _.getTable2( _v.json_temp )
			_.printVar( var )
		else:
			os.system('"' + doThis + '"')
	except Exception as e:
		pass
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( 'obj' ) )


def complete():
	_.pr()
	_.pr()
	_.pr( 'Done' )


def action():
	global isSingle
	if _.switches.isActive( 'Folder' ):
		_.threads.add( 'acquire_exif', trigger=complete, loaded=False )
		_.threads.report = True
		_.threads.auditPrint = True
		_.threads.maxThreadsSafe = 50

	do = 'exiftool "THEFILE" -json > MOD_BYTES.json'
	# do = 'exiftool "THEFILE" -json '
	pass
	# load()
	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	if _.switches.isActive('Input'):
	#     _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.setPipeData( _.switches.values('Input') , focus() )
			# _.appData[__.appReg]['pipe'] = []
			# for row in _.switches.value('Input').split( ',' ):
			#     _.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		
		if not _.switches.isActive( 'Folder' ):
			do = 'exiftool "THEFILE" -json'

		if _.switches.isActive('Input'):
			if len( _.appData[__.appReg]['pipe'] ) == 1:
				isSingle = True

		

		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			# _.pr( row )
			if not os.path.isfile( row ):
				if _.switches.isActive('Input'):
					_.pr( 'File does not exist' )
					sys.exit()
			else:
				info = _dir.fileInfo( row )
				# _.pr( _.printVar( info ) )
				
				# try:
				# except Exception as e:
				#     pass
				doThis = do.replace( 'THEFILE', row )
				if _.switches.isActive( 'Folder' ):
					doThis = doThis.replace( 'MOD_BYTES', _.switches.value( 'Folder' ) +_v.slash+ str(info['date_modified_raw'])+'_'+str(info['bytes']) )
				else:
					doThis = doThis.replace( 'MOD_BYTES', str(info['date_modified_raw'])+'_'+str(info['bytes']) )
				# _.pr( doThis )
				if not _.switches.isActive( 'Folder' ):
					exif( doThis )
				else:
					_.threads.add( 'acquire_exif', exif, [ doThis ] )


isSingle = False
# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()