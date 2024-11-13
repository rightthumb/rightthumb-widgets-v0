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
	_.switches.register( 'Files', '-db,-f,-file,-files','file.db', isPipe='name', description='Files' )
	_.switches.register( 'DB', '-db', 'ip.db' )
	_.switches.register( 'SQL', '-sql', " SELECT * FROM terminal_login " )
	_.switches.register( 'NotRecords', '-nr,-notrecords' )
	_.switches.register( 'Delim', '-delim', ',' )
	_.switches.register( 'TableFields', '-table', 'terminal_login' )
	_.switches.register( 'Clean', '--c' )

	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
__.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'db.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'query database',
	'categories': [
						'db',
						'sql',
						'query',
						'tool',
						'research',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'db.new',
						'db.del',
						'b db.new',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p db -db login.db',
						'',
						'p db -db login.db -sql select ip,date_created from terminal_login --c',
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

def table_fields(databaseFile,table):
	connection = sqlite3.connect(databaseFile)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute('select * from '+table)
	row = cursor.fetchone()
	names = row.keys()
	# _.pr(names)

	# for n in names:
	#     _.pr(n)
	# sys.exit()
	return names

def action():

	sql = "SELECT name FROM sqlite_master WHERE type='table';"
	isDefault = True
	# sql = "SELECT * FROM sqlite_master;"
	if _.switches.isActive('SQL'):
		sql = ' '.join( _.switches.values('SQL') )
		if not _.isWin:
			sql = sql.replace( '\*', '*' )
		# _.pr(sql)
		# sys.exit()
		isDefault = False
	else:
		_.colorThis(  [ 'List of tables:' ], 'yellow'  )

	for i,row in enumerate(_.isData(r=1)):
		if not _.switches.isActive('Clean'):
			_.pr('DB:', row)
		
		if _.switches.isActive('TableFields'):
			for table in _.switches.values('TableFields'):
				_.pr( '\t', table )
				for field in table_fields(  row, table  ):
					_.pr( '\t\t', field )

				
		else:
			conn = sqlite3.connect(row)
			c = conn.cursor()
			c.execute( sql )
			delim = ','
			if _.switches.isActive('Delim'):
				delim = _.switches.values('Delim')[0]

			if not _.switches.isActive('NotRecords'):
				# _.pr('here')
				records = c.fetchall()
				# _.pr(records)
				for record in records:
					# _.pr(record)
					txt = []
					for field in record:
						txt.append(str(field)) 
					if isDefault:
						_.pr( '\t', delim.join(txt) )
						for field in table_fields(  row, delim.join(txt)  ):
							_.pr( '\t\t', field )
					else:
						_.pr( delim.join(txt) )



import sqlite3

########################################################################################
if __name__ == '__main__':
	action()







