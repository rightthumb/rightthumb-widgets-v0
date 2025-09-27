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
	_.switches.register( 'NoLine', '-noline' )
	_.switches.register( 'AutoDelim', '-autodelim', ';' )
	_.switches.register( 'ClearCache', '-clear,-del,-clearcache' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'lineDB.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Convert file to database then query. Great for LARGE text files :)',
	'categories': [
						'pipe',
						'file',
						'tool',
						'query file',
						'file 2 database',
						'convert',
						'FAST',
						'efficient',
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
						'type dx.all-20.2.5-clean.js | p lineDB + "new t" -autodelim -strictcase',
						'',
						'calculate instantiated objects',
						'\ttype dx.all-20.2.5-clean.js | p lineDB + "new " | p line -p "new " 1 | p finagle_delim | p line -p ; 0 | sort | p countEach',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START

import _rightThumb._md5 as _md5
import sqlite3


def action():
	# _.pr(_.switches.values('Plus'))
	# sys.exit()
	good = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_'
	delim = None

	_.pr( 'Processing...', end='\r' )
	md5 = _md5.md5(  '\n'.join(  _.isData(r=1,c=0)  )  )




	db = _v.myTemp+_v.slash+'closestDB-'+md5+'.db'
	if _.switches.isActive('ClearCache'):
		if os.path.isfile(db):
			try:
				os.unlink(db)
			except Exception as e:
				pass
	


	if not os.path.isfile(db):
		conn = sqlite3.connect(db)
		cursor = conn.cursor()
		sql =  'CREATE TABLE file (i int, row text)'
		cursor.execute( sql )
		for i,row in enumerate(_.isData(r=1,c=0)):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			cursor.execute( "INSERT INTO file VALUES (?, ?)", (i,row) )
		conn.commit()
	else:
		conn = sqlite3.connect(db)
		cursor = conn.cursor()

	_.nc.child( 'cnt' )
	_.nc.cnt.search = 0
	_.nc.cnt.total = len(_.isData(c=0))
	table = []
	spent = []
	_.pr( '                                                                               ', end='\r' )
	if _.switches.isActive('PlusOr'):
		for x in _.switches.values('Plus'):
			sql = """ SELECT * FROM file WHERE row LIKE "%"""+x+"""%" """
			cursor.execute(sql)
			results = cursor.fetchall()
			rowX = rec[1]
			for rec in results:
				if _.switches.isActive('AutoDelim'):
					delim = ';'
					
					# if len( _.switches.value('AutoDelim') ):
					#     delim = _.switches.value('AutoDelim')
					newRow = ''
					for xyz in rec[1]:
						if xyz in good:
							newRow += xyz
						else:
							newRow += delim
					newRow += delim
					rowX = newRow

				if _.showLine( rowX, end=delim ):
					if not rec[0] in spent:
						spent.append(rec[0])
						_.nc.cnt.search += 1
						x=rec[1]
						for z in _.switches.values('Plus'):
							for y in _.caseUnspecific(x,z):
								x = x.replace(y, _.colorThis( y, 'green', p=0 ))
						_.pr(rec[0],x)
						# _.pr(rowX)

	else:
		

		xx = []
		for x in _.switches.values('Plus'):
			xx.append('row LIKE "%'+x+'%"')

		
		sql = 'SELECT * FROM file WHERE ' + ' AND '.join( xx )
		if not _.switches.isActive('StrictCase'):
			sql += ' COLLATE NOCASE'
		cursor.execute(sql)
		results = cursor.fetchall()
		for rec in results:
			rowX = rec[1]
			if _.switches.isActive('AutoDelim'):
				delim = ';'
				if len( _.switches.value('AutoDelim') ):
					delim = _.switches.value('AutoDelim')
				newRow = ''
				for xyz in rec[1]:
					if xyz in good:
						newRow += xyz
					else:
						newRow += delim
				newRow += delim
				rowX = newRow

			# _.pr(_.switches.values('Plus'))
			# _.pr(_.switches.values('Plus'))
			if _.showLine( rowX, end=delim ):
				_.nc.cnt.search += 1
				x=rec[1]
				# _.pr(_.switches.values('Plus'))
				# sys.exit()
				for z in _.switches.values('Plus'):
					# _.pr( z )
					for y in _.caseUnspecific(x,z):
						x = x.replace(y, _.colorThis( y, 'green', p=0 ))
				if _.switches.isActive('NoLine'):
					_.pr(x)
				else:
					_.pr(rec[0],x)
					# _.pr(rowX)

	_.colorThis( [ '', _.addComma(_.nc.cnt.search), 'of', _.addComma(_.nc.cnt.total) ], 'yellow' )


	conn.close()



########################################################################################
if __name__ == '__main__':
	action()