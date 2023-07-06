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
__.isRequired_Pipe = True
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'file_date_from_3T_PowerShell.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Generate powershell script from dates in tech/hosts/MSI/indexes/3T_Drive.db',
	'categories': [
						'tool',
						'create date',
						'date',
						'ps1',
						'ps',
						'PowerShell',
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
						'b py',
						'p files + *.py --c | p file_date_from_3T_PowerShell > %tmpf0%',
						'',
						'b s',
						'p file + *.bat --c | p file_date_from_3T_PowerShell > %tmpf1%',
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
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

def get_name(  path, name  ):
	if name == '__init__.py':
		part = path.split(_v.slash)
		part.reverse()
		part.pop(0)
		return '\\_rightThumb\\'+ part.pop(0) +'\\__init__.py'
	else:
		return '\\'+name

def action():

	db = 'D:\\tech\\hosts\\MSI\\indexes\\3T_Drive.db'
	conn = sqlite3.connect(db)
	c = conn.cursor()

	sql = 'SELECT date_modified_raw FROM files WHERE bytes > 10 AND path LIKE "%xXx" ORDER BY date_modified_raw Asc LIMIT 1'

	for i,row in enumerate(_.isData(r=1)):
		info = _dir.info(row)
		name = get_name(  info['path'], info['name']  )
		c.execute(sql.replace( 'xXx', name ))
		records = c.fetchall()
		if len(records):
			d = _.modify_timestamp( records[0][0] )
			ps = '$(Get-Item "'+info['path']+'").CreationTime=("'+d+'")'
			_.pr( ps )
			




import _rightThumb._dir as _dir
import sqlite3

########################################################################################
if __name__ == '__main__':
	action()






