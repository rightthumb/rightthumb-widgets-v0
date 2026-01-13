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
from datetime import datetime as dt, timedelta
import datetime

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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
import sqlite3
import hashlib

##################################################


def appSwitches():
	_.switches.register('NoCount', '--c,--count')
	_.switches.register('Database', '-db,-database','%i%/C_Drive.db')
	_.switches.register('MD5', '-md5')
	_.switches.register('Size', '-size')
	_.switches.register('Text', '-text')
	_.switches.register('Folder', '-folder')
	_.switches.register('DateUnix', '-dateunix','1183330364 1193957564')
	_.switches.register('Ago', '-ago')
	_.switches.register('Date', '-date')
	



_.appInfo[focus()] = {
	'file': 'dirDB.py',
	'description': 'Queries file dir databases',
	'categories': [
						'dir',
						'file',
						'query',
						'database',
						'research',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}


_.appInfo[focus()]['examples'].append('p dirDB -database defaultDir.db')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirDB -db %i%\\C_Drive.db -c name')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirDB -db %i%\\C_Drive.db -c name | p dir -c s p -s bytes')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb -db C_Drive.db -c n | p dir -s s -c s p')
_.appInfo[focus()]['examples'].append('p dirdb -db D_Drive.db -c n | p dir -s s -c s p')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb -db D_Drive.db -size g 2gb')
_.appInfo[focus()]['examples'].append('p dirdb -db D_Drive.db -size b 1gb 3gb')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb -db C_Drive.db -c p  + *.pdf')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018.')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018. --c | p line --c -p \\ ee -u | p line --c -make "p dirdb -folder ;\'{};\' + *.txt --c " | p execute | p line --c - "p dirdb"')
_.appInfo[focus()]['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018. --c |p line --c -p \\ ee -u |p line --c -make "p dirdb -folder ;\'{};\' + *.txt --c " |p execute |p line --c - "p dirdb" |p f + com gen -jn')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb + \\201 | p line --c -p \\ ;mdt | p sortMDT -r')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb -db %i%\\C_Drive.db -c s p -size g 100mb')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirdb -db %i%\\C_Drive.db -c s p -s d.bytes -size g 100mb ')
_.appInfo[focus()]['examples'].append('')



_.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo[focus()]['columns'].append({'name': 'name_', 'abbreviation': 'n_'})
_.appInfo[focus()]['columns'].append({'name': 'path', 'abbreviation': 'p'})
_.appInfo[focus()]['columns'].append({'name': 'folder', 'abbreviation': 'f'})
_.appInfo[focus()]['columns'].append({'name': 'friendly_month', 'abbreviation': 'fm'})
_.appInfo[focus()]['columns'].append({'name': 'friendly_week', 'abbreviation': 'fw'})
_.appInfo[focus()]['columns'].append({'name': 'month', 'abbreviation': 'm'})
_.appInfo[focus()]['columns'].append({'name': 'attrib', 'abbreviation': 'a'})
_.appInfo[focus()]['columns'].append({'name': 'bytes', 'abbreviation': 'b'})
_.appInfo[focus()]['columns'].append({'name': 'ext', 'abbreviation': 'e'})
_.appInfo[focus()]['columns'].append({'name': 'type', 'abbreviation': 't'})
_.appInfo[focus()]['columns'].append({'name': 'size', 'abbreviation': 's'})
_.appInfo[focus()]['columns'].append({'name': 'week_of_year_', 'abbreviation': 'w2,woy2'})
_.appInfo[focus()]['columns'].append({'name': 'week_of_year', 'abbreviation': 'woy,w'})
_.appInfo[focus()]['columns'].append({'name': 'day_of_the_week', 'abbreviation': 'd,dotw,dow'})
_.appInfo[focus()]['columns'].append({'name': 'date_modified', 'abbreviation': 'mdate,datem,dm,md'})
_.appInfo[focus()]['columns'].append({'name': 'date_created', 'abbreviation': 'cdate,datec,dc,cd'})

_.appInfo[focus()]['columns'].append({'name': 'date_modified_raw', 'abbreviation': 'dmr,mdr'})
_.appInfo[focus()]['columns'].append({'name': 'date_created_raw', 'abbreviation': 'dcr,cdr'})

_.appInfo[focus()]['columns'].append({'name': 'md5', 'abbreviation': 'md5'})




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
########################################################################################
# START

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()


def formatSize(size):
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776    :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#     result = ''
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776    
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	result = round(size * factor,0)
	return result

def timeAgo():
	do = _.switches.value('Ago')
	do = do.lower()
	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1
	if 'y' in do:
		start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
	if 'm' in do:
		start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
	if 'w' in do:
		start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
	if 'd' in do:
		start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
	dT = str(start_date)
	# _.pr(dT)
	# _.pr(dT)
	# _.pr(dT)
	d = dT.split('-')
	result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# _.pr(start_date)
	return result
def epoch(string,end=False):
	string = str(string)
	if '.' in string:
		d = string.split('.')
	elif _v.slash in string:
		d = string.split(_v.slash)
	elif '-' in string:
		d = string.split('-')
	elif len(string) == 6:
		t = string[:4] + '-' + string[-2:]
		d = t.split('-')
	elif len(string) == 8:
		x = string[-4:]
		t = string[:4] + '-' + x[:2] + '-' + x[-2:]
		d = t.split('-')

	if not len(d) == 3:
		day = 1
	else:
		day = d[2]
	# _.pr(d)
	# sys.exit()
	if end:
		y = int(d[0])
		m = int(d[1])
		if m == 12:
			y += 1
			m = 1
		else:
			m += 1
		start_date = datetime.datetime(y,m,1,0,0) + datetime.timedelta(-1)
		result = start_date.timestamp()
	else:
		result = datetime.datetime(int(d[0]),int(d[1]),int(day),0,0).timestamp()
	# result = d
	return result
def isNu(string):
	result = True
	for s in string:
		try:
			int(s)
		except Exception as e:
			result = False
	return result

def action():
	global totalSize
	global totalCount
	totalSize = 0
	totalCount = 0

	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"
		for dbFile in databaseFile.split(','):
			do(dbFile)
	if not _.switches.isActive('NoCount'):
		_.pr()
		_.pr('Total:')
		_.pr('\tFiles:\t',totalCount)
		_.pr('\tSize:\t',formatSize(totalSize))
def do(databaseFile):
	# _.pr(databaseFile)
	global totalSize
	global totalCount
	# _.pr(databaseFile)
	conn = sqlite3.connect(databaseFile)
	c = conn.cursor()
	# sql = "SELECT bytes,path FROM files WHERE path like '%0%'"
	# sql = "SELECT * FROM files WHERE bytes < 101 and bytes > 49  ORDER BY bytes"
	# sql = "SELECT bytes,path FROM files WHERE bytes < 101 and bytes > 49  ORDER BY bytes"
	# sql = "SELECT bytes,path FROM files WHERE bytes < 10000000 and bytes > 200  ORDER BY bytes"
	if _.switches.isActive('Plus') and not _.switches.isActive('Folder'):
		pv = _.switches.value('Plus')
		_.switches.fieldSet('Text','active',True)
		_.switches.fieldSet('Text','value',pv.split(',')[0])
	if _.switches.isActive('Text') and not  _.switches.isActive('Folder'):
		tv = _.switches.value('Text')
		if tv.startswith('*.'):
			tv = tv.replace('*.','')
			sql = "SELECT * FROM files WHERE ext = '" + tv + "' ORDER BY bytes"
		elif tv.startswith('*'):
			tv = tv.replace('*','')
			sql = "SELECT * FROM files WHERE path like '%" + tv + "' ORDER BY bytes"
		elif tv.endswith('*'):
			tv = tv.replace('*','')
			sql = "SELECT * FROM files WHERE path like '" + tv + "%' ORDER BY bytes"
		else:
			sql = "SELECT * FROM files WHERE path like '%" + tv + "%' ORDER BY bytes"

	elif _.switches.isActive('Size') and not  _.switches.isActive('Folder'):
		s = _.switches.value('Size')
		sA = s.split(',')
		if sA[0].lower() == 'g':
			sql = "SELECT * FROM files WHERE bytes > " + str(unFormatSize(sA[1])) + " ORDER BY bytes"
		elif sA[0].lower() == 'l':
			sql = "SELECT * FROM files WHERE bytes < " + str(unFormatSize(sA[1])) + " ORDER BY bytes"
		elif sA[0].lower() == 'b' and len(sA) == 3:
			sql = "SELECT * FROM files WHERE bytes > " + str(unFormatSize(sA[1])) + " and bytes < " + str(unFormatSize(sA[2])) + " ORDER BY bytes"
			_.pr(sql)
		else:
			_.pr('Error:')
			_.pr('\tExpected:')
			_.pr('\t\tp dirdb -db D_Drive.db -size g 2gb')
			_.pr('\t\tp dirdb -db D_Drive.db -size b 1gb 3gb')
			sys.exit()
	elif not  _.switches.isActive('Folder'):
		sql = "SELECT * FROM files WHERE bytes > 100000000 ORDER BY bytes"
	if _.switches.isActive('Folder'):
		# _.pr(_.switches.value('Folder'))
		sql = "SELECT * FROM files WHERE folder like '" + _.switches.value('Folder') + "' ORDER BY bytes"
	if _.switches.isActive('DateUnix'):
		s = _.switches.value('DateUnix')
		sA = s.split(',')
		sql = "SELECT * FROM files WHERE date_modified_raw > " + str(sA[0]) + " and date_modified_raw < " + str(sA[1]) + " ORDER BY bytes"
	if _.switches.isActive('Date'):
		sDate = _.switches.value('Date')
		sD = sDate.split(',')
		# _.pr(sD[0])
		# _.pr(isNu(sD[0]))
		# _.pr(len(sD))
		if isNu(sD[0]) and len(sD) == 2:
			sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[0])) + " and date_modified_raw < " + str(epoch(sD[1],True)) + " ORDER BY bytes"
		elif len(sD) == 3:
			sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[1])) + " and date_modified_raw < " + str(epoch(sD[2],True)) + " ORDER BY bytes"
			# _.pr(sql)
		elif len(sD) == 2:
			if sD[0] == 'before':
				sql = "SELECT * FROM files WHERE date_modified_raw < " + str(epoch(sD[1])) + " ORDER BY bytes"
			elif sD[0] == 'after':
				sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[1])) + " ORDER BY bytes"
			else:
				_.pr('before after between')
				sys.exit()
	if _.switches.isActive('Ago'):
		# _.pr(timeAgo())
		# sys.exit()
		sql = "SELECT * FROM files WHERE date_modified_raw > " + str(timeAgo()) + " ORDER BY bytes"

		# d = epoch()
		# _.pr(d)
		# sys.exit()

	# sql = "SELECT bytes,path FROM files WHERE bytes > 100000000"
	# if  _.switches.isActive('Folder'):
		# _.pr(sql)
	c.execute(sql)
	# c.execute('SELECT * FROM {tn} WHERE {cn} = {st}'.\
	#         format(tn='files', cn='path', st='s'))
	all_rows = c.fetchall()
	# _.pr('1):', all_rows)
	names = action2(databaseFile)
	# _.pr(names)
	global columnDefault
	data = []
	for f in all_rows:
		# _.pr(_.switches.value('Column'))

		row = {}
		for i,n in enumerate(names):
			row[n] = f[i]
		if _.switches.isActive('Column'):
			line = ''
			col = _.switches.value('Column')
			for ii,c in enumerate(col.split(',')):
				i = ii + 1
				if c == 'md5':
					try:
						line += str(md5(row['path']))
						if not len(col.split(',')) == i:
							line += str('\t')
					except Exception as e:
						line += '* MD5 Error *'
						if not len(col.split(',')) == i:
							line += str('\t')
					
				else:
					line += str(row[c])
					if not len(col.split(',')) == i:
						line += str('\t')
		if _.showLine(line) and os.path.isfile(row['path']):
			data.append( row )
			# if not '$Recycle.Bin' in row['path']:
			totalCount += 1
			totalSize += row['bytes']
			# if not _.switches.isActive('Folder'):
			if columnDefault:
				_.pr(line)
		else:
			if _.showLine(row['path']) and os.path.isfile(row['path']):
				data.append( row )
				# if not '$Recycle.Bin' in row['path']:
				totalCount += 1
				totalSize += row['bytes']
				fS = formatSize(row['bytes'])
				while len(fS) < 10:
					fS += ' '
				# if not _.switches.isActive('Folder'):
				if columnDefault:
					_.pr(fS,'',row['path'])

	if not columnDefault:
		_.switches.fieldSet('Long','active',True)
		_.tables.register( 'data', data )
		_.tables.print( 'data', _.switches.value('Column') )


def action2(databaseFile):
	connection = sqlite3.connect(databaseFile)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute('select * from files')
	row = cursor.fetchone()
	names = row.keys()
	# _.pr(names)

	# for n in names:
	#     _.pr(n)
	# sys.exit()
	return names


def action3():
	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"
		con = sqlite3.connect(databaseFile)
		with open('dump.sql', 'w') as f:
			for line in con.iterdump():
				f.write('%s\n' % line)


if not _.switches.isActive('Database'):
	dbs = _v.myIndexes + _v.slash+'C_Drive.db,' + _v.myIndexes + _v.slash+'D_Drive.db'
	# _.pr(dbs)
	_.switches.fieldSet('Database','active',True)
	_.switches.fieldSet('Database','value',dbs)


columnDefault = False
if not _.switches.isActive('Column'):
	columnDefault = True
	_.switches.fieldSet('Column','active',True)
	_.switches.fieldSet('Column','value','path')



########################################################################################
if __name__ == '__main__':
	action()