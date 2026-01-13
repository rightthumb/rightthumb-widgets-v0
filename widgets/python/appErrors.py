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

# import os
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

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Fields', '-f,-fields')
	



_.appInfo[focus()] = {
	'file': 'appErrors.py',
	'description': 'Search app documentation ',
	'categories': [
						'audit',
						'documentation',
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
						'p appErrors + ',
						''
	],
	'columns': [
					{'name': 'file', 'abbreviation': 'f'},
					{'name': 'description', 'abbreviation': 'd'},
					{'name': 'categories', 'abbreviation': 'cat'},
					{'name': 'aliases', 'abbreviation': 'a'},
					{'name': 'relatedapps', 'abbreviation': 'ra'},
					{'name': 'base_version', 'abbreviation': 'bv'},
					{'name': 'app_version', 'abbreviation': 'av'},
					{'name': 'prerequisite', 'abbreviation': 'pre'},
					{'name': 'examples', 'abbreviation': 'x'},
					{'name': 'columns', 'abbreviation': 'c'},
					{'name': 'error', 'abbreviation': 'e'},
					{'name': 'errors;field', 'abbreviation': 'ef'},
					{'name': 'errors;error', 'abbreviation': 'ee'},
					{'name': 'errors;affect', 'abbreviation': 'ea'},

					{'name': 'file_profile;imports;app', 'abbreviation': 'ia'},
					{'name': 'file_profile;imports;examples', 'abbreviation': 'ie'},
					{'name': 'file_profile;imports;raw', 'abbreviation': 'ir'},
					{'name': 'file_profile;imports;instantiated', 'abbreviation': 'ii'},
					{'name': 'file_profile;imports;myapp', 'abbreviation': 'myapp'},
					{'name': 'file_profile;imports;myimport', 'abbreviation': 'myimport'},
					{'name': 'file_profile;imports;from', 'abbreviation': 'ifrom'},
					{'name': 'file_profile;imports;namespace', 'abbreviation': 'ins'},
	],
	'aliases': [
					'error',
					'errors',
	]}







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
	_.switches.trigger('Fields',_.formatColumns)
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
########################################################################################
# START

def searchRegistration():
	global data

	if not _.switches.isActive( 'Fields' ):
		for i,record in enumerate(data):
			if _.showLine( record['description'] ):
				IDs.append( i )
			elif _.showLine( record['file'] ):
				IDs.append( i )
			elif _.showLine( record['live_file'] ):
				IDs.append( i )
			elif _.showLine( record['aliases'] ):
				IDs.append( i )
			else:
				for row in record['categories']:
					if _.showLine( row ):
						IDs.append( i )
	else:
		pass

def action():
	load()
	if _.switches.isActive('Input'):
	#     _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			for row in _.switches.value('Input').split( ',' ):
				_.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		_.pr( _.printVar(_.appData) )
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			pass
			



def load():
	global data
	data = _.getTableDB( 'appRegistration.json' )
data = []
########################################################################################
if __name__ == '__main__':
	action()



# base_version
# app_version
# file
# description
# categories
# relatedapps
# prerequisite
# examples
# columns
# live_file
# live_app
# error
# errors
#     field
#     error
#     affect
# aliases
# file_profile
# imports
#     app
#     examples
#     raw
#     instantiated
#     myapp
#     myimport
#     from
#     namespace