#!/usr/bin/python3
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
	_.switches.register( 'DB', '-db', isRequired=True )
	_.switches.register( 'SQL', '-sql' )
	_.switches.register( 'Subject', '-subject' )
	_.switches.register( 'Fields', '-fields' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'query.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Query SQLite database files',
	'categories': [
						'SQLite',
						'query',
						'sql',
						'db',
						'.db',
						'database',
						'tool',
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
						'p query -db D_Drive.db -sql "select count(path) as cnt, date_modified, folder from files where date_modified_raw > 1548486000 and path like \';p\\tech\\;p\' group by folder order by date_modified_raw desc" ',
						'',
						'p query -db D_Drive.db -sql "select count(path) as cnt, date_modified, folder from files where date_modified_raw > 1580108400 group by folder order by date_modified_raw desc" -subject 2 - tech xampp "Program Files"',
						'',
						'p query -db D_Drive.db -sql "select count(path) as cnt, date_modified, folder from files where date_modified_raw > 1580108400 group by folder order by date_modified_raw desc" -subject 2 - tech xampp "Program Files"  -fields cnt epoch folder -long',
						'',
						'p query -db C_Drive.db -sql " SELECT sql FROM sqlite_master WHERE name=\'files\' "',
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

import sqlite3

def action():
	if not _.switches.isActive('SQL'):
		sql = 'SELECT sql FROM sqlite_master WHERE name="files"'
	else:
		sql = ' '.join( _.switches.values('SQL') ).replace("'",'"').replace( ';p', '%' )
	# print( sql )
	# print()
	# print()
	cnt = 0
	t = None
	for db in _.switches.values('DB'):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute(sql)
		records = c.fetchall()
		table = []
		for record in records:
			if sql == 'SELECT sql FROM sqlite_master WHERE name="files"':
				data = record[0]
				data = data.replace( '(', '(\n\t ' )
				data = data.replace( ')', '\n)' )
				data = data.replace( ',', ',\n\t' )
				print(data)

			else:
				if not _.switches.isActive('Plus') and not _.switches.isActive('Minus'):
					cnt+=1
					t='a'

					if _.switches.isActive('Fields'):
						rec = {}
						for ei, f in enumerate(_.switches.values('Fields')):
							rec[f] = record[ei]
						table.append(rec)
					else:
						print( record )

				elif _.switches.isActive('Subject'):
					i = int( _.switches.value('Subject') )
					if _.showLine( record[i] ):
						cnt+=1
						t='b'
						if _.switches.isActive('Fields'):
							rec = {}
							for ei, f in enumerate(_.switches.values('Fields')):
								rec[f] = record[ei]
							table.append(rec)
						else:
							print( record )
				else:
					if _.showLine( str(record) ):
						cnt+=1
						t='c'
						if _.switches.isActive('Fields'):
							rec = {}
							for ei, f in enumerate(_.switches.values('Fields')):
								rec[f] = record[ei]
							table.append(rec)
						else:
							print( record )
		if len(table):
			_.tables.register( 'data', table )
			_.tables.print( 'data', ','.join( _.switches.values('Fields') ) )
	print()
	_.colorThis( ['',cnt], 'yellow' )


########################################################################################
if __name__ == '__main__':
	action()



