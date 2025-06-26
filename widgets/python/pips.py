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
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
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
_file_folder = _.regImp( __.appReg, 'file_folder' )

##################################################

import shutil
# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register('Input', '-i,-input','install selenium, install --upgrade pip')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'pips.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT'
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
						'p pips -i install selenium',
						'',
						'type module_list.txt | p pips -i install --upgrade pip',
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


def pipAction( pip, what ):
	do = pip + ' ' + what
	os.system('"' + do + '"')

def pipProcess( what ):
	runFix = False
	if runFix:
		pipFolder = _v.appsFolder+_v.slash+'Python\\Python36-32\\Lib\\site-packages'
		_file_folder.switch( 'Folder', 'pipFolder' )
		shouldRun = False


	pipList = _.getText( _v.pips, raw=True, clean=True ).split('\n')
	# sys.exit()
	for i,row in enumerate( pipList ):
		if runFix and i > 0:
			_file_folder.switch( 'Compair,Clean' )
		_.pr()
		_.pr( '____________________________________ PIP ____________________________________' )
		pipAction( row, what )

		if runFix and i == 0:
			_file_folder.switch( 'Save,Clean' )
	

def action():
	# for row in help("modules"):
	#     _.pr( row )
	# sys.exit()

	if type( _.appData[__.appReg]['pipe'] ) == bool and _.switches.isActive( 'Input' ):
		v = _.switches.value( 'Input' ).replace( ',', ' ' )
		pipProcess( _.ci(v) )
		sys.exit()

	# load()
	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	# if _.switches.isActive('Input'):
	#     if os.path.isfile(path):
	#         _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
	#     else:
	#         if type( _.appData[__.appReg]['pipe'] ) == bool:
	#             _.appData[__.appReg]['pipe'] = []
	#             for row in _.switches.value('Input').split( ',' ):
	#                 _.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if _.switches.isActive( 'Input' ) and 'up' in _.switches.value( 'Input' ).lower():
				pipProcess( 'install --upgrade ' + row )
			else:
				pipProcess( 'install ' + row )



# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()






