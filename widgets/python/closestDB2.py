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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data', description='Files' )
	_.switches.register( 'AutoDelim', '-autodelim', ';' )
	_.switches.register( 'ClearCache', '-clear,-del,-clearcache' )
	_.switches.register( 'Max', '-max', '10' )
	_.switches.register( 'All', '-all' )

_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'closestDB.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Find strings that are closest to each other.',
	'categories': [
						'javascript',
						'find',
						'db',
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
						'type dx.all-20.2.5-clean.js | p closestDB + dataType format',
						'',
						'type dx.all-20.2.5-clean-mod.js | p closestDB + "g =" "m =" "v =" "_ =" -strictcase -max 6 -all',
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
www = {}
good = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_'
def prep(x):
	global www
	www['x'] = x
	_.pr( str(www) )
	x = x.replace( '"', '\\"' )
	return x

def clean(x):
	x = _str.cleanBE(x,' ')
	x = _str.cleanBE(x,'\t')
	x = x.replace( '\r', '' )
	x = x.replace( '\n', '' )
	for z in _.switches.values('Plus'):
		for y in _.caseUnspecific(x,z):
			x = x.replace(y, _.colorThis( y, 'green', p=0 ))

	return x

def action():

	if _.switches.isActive('AutoDelim'):
		if len( _.switches.value('AutoDelim') ):
			delim = _.switches.value('AutoDelim')
		else:
			delim = ';'
	else:
		delim = None

	_.switches.fieldSet( 'PlusOr', 'active', True )
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
			if _.switches.isActive('AutoDelim'):
				newRow = ''
				for xyz in rec[1]:
					if xyz in good:
						newRow += xyz
					else:
						newRow += delim
				newRow += delim
				row = newRow
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			cursor.execute( "INSERT INTO file VALUES (?, ?)", (i,row) )
		conn.commit()
	else:
		conn = sqlite3.connect(db)
		cursor = conn.cursor()

	table = []
	for x in _.switches.values('Plus'):
		if _.switches.isActive('AutoDelim'):
			x += delim
		sql = """ SELECT * FROM file WHERE row like "%"""+x+"""%" """
		if not _.switches.isActive('StrictCase'):
			sql += ' COLLATE NOCASE'
		cursor.execute(sql)
		results = cursor.fetchall()
		for rec in results:
			rowX = rec[1]
			if _.switches.isActive('AutoDelim'):
				newRow = ''
				for xyz in rec[1]:
					if xyz in good:
						newRow += xyz
					else:
						newRow += delim
				newRow += delim
				rowX = newRow

			if _.showLine( rowX, end=delim ):
				if not rec[0] in table:
					table.append( rec[0] )
	conn.close()

	table.sort()
	last = ''
	dex = {}
	windex = {}
	default = 999999999999999999999999999999
	diff = default
	for i in table:
		row = _.isData(c=0)[i]

		cnt = 0
		for x in _.switches.values('Plus'):
			if x.lower() in row.lower():
				cnt+=1
		if cnt == len(_.switches.values('Plus')):
			single = True
		else:
			single = False

		for x in _.switches.values('Plus'):
			if _.switches.isActive('AutoDelim'):
				x += delim
			if x.lower() in row.lower():
				if not x == last:
					li = -1
					if single:
						dx = 0
						li = i
					else:
						try:
							li = windex[last]
						except Exception as e:
							li = -1
						if not li == -1:
							dx = i - li
					# _.colorThis(li)
					if not li == -1:
						if dx < diff:
							diff = dx
						if not dx in dex:
							dex[dx] = {}

						dex[ dx ][ li ] = i
				last = x
				windex[x] = i


	_.pr( '                                                        ', end='\r' )
	if diff == default:
		_.colorThis( 'not found', 'red' )
	else:
		if _.switches.isActive('Max'):
			m = int( _.switches.value('Max') )
		else:
			m = 10
		tbl = []
		# for s in slots:
		#     if not slots[s] == default:
		#         if slots[s] <= m:
		#             tbl.append(slots[s])
		for t in dex:
			if t <= m:
				tbl.append(t)
		tbl.sort()
		cnt = 0
		for t in tbl:
			label_printed = False

			
			for d in dex[t]:
				shouldInclude = True
				if _.switches.isActive('All'):
					fnd_cnt = 0
					x = d

					while not x == dex[t][d]+1:

						row = _.isData(pipeClean=False)[x]
						if _.switches.isActive('AutoDelim'):
							newRow = ''
							for xyz in rec[1]:
								if xyz in good:
									newRow += xyz
								else:
									newRow += delim
							newRow += delim
							row = newRow

						for yx in _.switches.values('Plus'):
							if _.switches.isActive('AutoDelim'):
								yx += delim
							yyx = yx
							if not _.switches.isActive('StrictCase'):
								yyx = yyx.lower()
								row = row.lower()
							if yyx in row:
								fnd_cnt += 1


						x+=1
					if not fnd_cnt >= len(  _.switches.values('Plus')  ):
						shouldInclude = False


				if shouldInclude:
					if not label_printed:
						_.colorThis( t, 'blue' )
						label_printed = True
					_.colorThis( [ '\t', d, dex[t][d] ], 'cyan' )
					cnt+=1
					if not _.switches.isActive('Clean'):
						if d == dex[t][d]:
							_.pr( '\t\t', clean( _.isData(pipeClean=False)[d] ) )
						else:
							x = d
							while not x == dex[t][d]+1:
								_.pr( '\t\t', clean( _.isData(pipeClean=False)[x] ) )
								x+=1
		_.colorThis( [ '\n','',  cnt ], 'yellow' )



########################################################################################
if __name__ == '__main__':
	action()







