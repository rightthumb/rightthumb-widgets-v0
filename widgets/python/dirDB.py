#!/usr/bin/python3
import os
import sys
import time
from datetime import datetime as dt, timedelta
import datetime
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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._md5 as _md5
##################################################
import sqlite3
import hashlib
##################################################

def appSwitches():
	_.switches.register('Database', '-db,-database','%i%\\C_Drive.db')
	_.switches.register('Duplicates', '-dup,-duplicate,-duplicates')
	_.switches.register('NoCount', '--c,--count')
	_.switches.register('MD5', '-md5')
	_.switches.register('EXT', '-ext', 'mp4')
	_.switches.register('Size', '-size')
	_.switches.register('Text', '-text')
	_.switches.register('Folder', '-folder')
	_.switches.register('DateUnix', '-dateunix','1183330364 1193957564')
	_.switches.register('Ago', '-ago')
	_.switches.register('Date', '-date')
	_.switches.register('JustCount', '-jc')
	_.switches.register('ExtReport', '-report','c d all allx')
	_.switches.register('BackupDrive', '-bk,-backup')
	_.switches.register('Save', '-save')
	_.switches.register('NoPrint', '-noprint')
	_.switches.register('Min', '-min')
	_.switches.register('Clean', '-clean')
	_.switches.register('Test', '-test')
	_.switches.register('Prefix', '-prefix', 'ADD THIS LATER')

	



_.appInfo[focus()] = {
	'file': 'dirDB.py',
	'description': 'Queries file dir databases',
	'categories': [
						'dir',
						'file',
						'query',
						'database',
						'db',
						'research',
				],
	'relatedapps': [
						'p dirDB + netflix --c | p filePathPatterns -r',
	],
	'prerequisite': [],
	'examples': [
						'p dirDB + *.iso - windows dvd',
						'',
	],
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
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirDB -dup  -db i D_Drive.db -size 50mb')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dirDB -db C_Drive.db -dup -min 50mb')
_.appInfo[focus()]['examples'].append('')
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



def dbPathTrigger(data):
	if data.lower() == 'i':
		data = _v.myIndexes
	return data



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
	_.switches.trigger('Database',dbPathTrigger)
	
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
	elif size > 1073741824 and size < 1099511627776	:
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	# 	result = ''
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
	# print(dT)
	# print(dT)
	# print(dT)
	d = dT.split('-')
	result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# print(start_date)
	return result
def epoch(string,end=False):
	string = str(string)
	if '.' in string:
		d = string.split('.')
	elif '/' in string:
		d = string.split('/')
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
	# print(d)
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

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			(result).encode('utf8')
		except Exception as e:
			result = result.encode('utf-8')
	return result

def repairEncoding( result ):
	result = formatData( result )
	return result
	result = str(result,'iso-8859-1')

def action():


	if _.switches.isActive('Duplicates') and not len(_.switches.value('Duplicates')):
		saveData = []
		saveDataSet = []
		includeName = False
		if 'n' in _.switches.value('Duplicates').lower() :
			includeName = True

		spent = []
		totalSave = 0


		db = _v.slash.join( _.switches.values('Database') )
		
		names = action2( db )
		sizePre = 0
		sizeMax = 0
		if _.switches.isActive('Size'):
			sizePre = _.switches.values('Size')[0]
			if len(_.switches.values('Size')) > 1:
				sizeMax = unFormatSize(_.switches.values('Size')[1])
		size = unFormatSize(sizePre)
		if sizeMax:
			sql = """
						SELECT *
						FROM files
						WHERE bytes > """+str(size)+""" and bytes < """+str(sizeMax)+"""
						GROUP BY bytes, date_modified_raw
						HAVING count(*) > 1
						ORDER BY bytes Desc
			"""
		else:
			sql = """
						SELECT *
						FROM files
						WHERE bytes > """+str(size)+"""
						GROUP BY bytes, date_modified_raw
						HAVING count(*) > 1
						ORDER BY bytes Desc
			"""
		if includeName:
			if sizeMax:
				sql = """
							SELECT *
							FROM files
							WHERE bytes > """+str(size)+""" and bytes < """+str(sizeMax)+"""
							GROUP BY bytes, date_modified_raw, name
							HAVING count(*) > 1
							ORDER BY bytes Desc
				"""
			else:
				sql = """
							SELECT *
							FROM files
							WHERE bytes > """+str(size)+"""
							GROUP BY bytes, date_modified_raw, name
							HAVING count(*) > 1
							ORDER BY bytes Desc
				"""

		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute(sql)
		records = c.fetchall()

		conn2 = sqlite3.connect(db)
		test = conn2.cursor()



		c.execute(sql)
		all_done = False
		for f in records:
			if all_done:
				break
			row = {}
			duplicates = []
			for i,n in enumerate(names):
				row[n] = f[i]

			# _.printTest( row, x=0 )


			mod = str(row['date_modified_raw'])
			if not '.'  in mod:
				mod = mod+'.0'
			sql = """
						SELECT *
						FROM files
						WHERE bytes = """+str(row['bytes'])+""" AND date_modified_raw = """+str(mod)+"""   
			"""
			if includeName:
				sql = """
							SELECT *
							FROM files
							WHERE bytes = """+str(row['bytes'])+""" AND date_modified_raw = """+str(mod)+"""  AND name = '"""+str(row['name'])+"""'  
				"""

			# print( sql )
			try:
				test.execute(sql)
			except Exception as e:
				pass
			else:

				for rec in test.fetchall():
					record = {}
					for ii,nn in enumerate(names):
						record[nn] = rec[ii]

					# print( record )
					if not record['path'] in spent:
						spent.append( record['path'] )
						duplicates.append( record )
						


				pass
				if len( duplicates ) > 1:
					subTotal = 0

					if _.switches.isActive('Save'):
						saveData.append('\n\n\n')
						saveDataSetGroup = []

					shouldInclude = True
					if _.switches.isActive('Plus'):
						shouldInclude = False
						for di,dupRec in enumerate(duplicates):
							if _.showLine( dupRec['path'] ):
								shouldInclude = True

					if shouldInclude:
						if _.switches.isActive('Min'):
							subTest = 0
							for di,dupRec in enumerate(duplicates):
								if di:
									subTest += int(dupRec['bytes'])
							if subTest < unFormatSize( _.switches.values('Min')[0] ):
								# print(  unFormatSize( _.switches.values('Min')[0] )  )
								shouldInclude = False
								all_done = True
					if shouldInclude:
						cnt = 0
						for di,dupRec in enumerate(duplicates):
							if not os.path.isfile( dupRec['path'] ):
								shouldInclude = False
								removeFile( dupRec['path'], c )
							else:
								cnt+=1
						if cnt > 1:
							shouldInclude = True

					if shouldInclude:
						print()
						print()
						print()
						for di,dupRec in enumerate(duplicates):
							# print( row['size'] )
							if os.path.isfile( dupRec['path'] ):
								if _.switches.isActive('Save'):
									saveData.append( dupRec['path'] )
									saveDataSetGroup.append( dupRec['path'] )

								if not row['name'].lower() == dupRec['name'].lower():
									try:
										_.colorThis( dupRec['path'], 'red' )
									except Exception as e:
										_.colorThis(   repairEncoding(dupRec['path'])  , 'red' )
										
								else:
									try:
										print( dupRec['path'] )
									except Exception as e:
										print(  repairEncoding(dupRec['path'])  )
								if di:
									totalSave += int(dupRec['bytes'])
									subTotal += int(dupRec['bytes'])


								if _.switches.isActive('Save'):
									saveDataSet.append({ 'files': saveDataSetGroup, 'bytes': subTotal, 'size': formatSize(subTotal) })

						if not _.switches.isActive('NoCount'):
							if 'GB' in formatSize(subTotal):
								col = 'red'
							else:
								col = 'green'

							_.colorThis( [' group -1:', formatSize(subTotal)], col )
							_.colorThis( ['sub-total:', formatSize(totalSave)], 'yellow' )


		print()
		print()
		print()
		if _.switches.isActive('Save'):
			saveData.append( '\n\n\n' )
			saveData.append( 'Total: ' + formatSize(totalSave) )
			_.saveText( saveData, _.switches.values('Save')[0] )
			# _.saveText( saveData, _.switches.values('Save')[0].split('.')[0]+'-print.'+_.switches.values('Save')[0].split('.')[1] )
			_.saveText( saveDataSet, _.switches.values('Save')[0].split('.')[0]+'-set.'+_.switches.values('Save')[0].split('.')[1] )
		_.colorThis( [  'Total',  formatSize(totalSave) ], 'red' )
		sys.exit()


	elif _.switches.isActive('Duplicates') and len(_.switches.value('Duplicates')):



		saveData = []
		includeName = False
		if 'n' in _.switches.value('Duplicates').lower() :
			includeName = True

		spent = []
		totalSave = 0


		db = _v.slash.join( _.switches.values('Database') )
		
		names = action2( db )
		sizePre = 0
		sizeMax = 0
		if _.switches.isActive('Size'):
			sizePre = _.switches.values('Size')[0]
			if len(_.switches.values('Size')) > 1:
				sizeMax = unFormatSize(_.switches.values('Size')[1])
		size = unFormatSize(sizePre)
		if sizeMax:
			sql = """
						SELECT *
						FROM files a, (SELECT bytes, date_modified_raw
						FROM files
						WHERE bytes > """+str(size)+""" and bytes < """+str(sizeMax)+"""
						GROUP BY bytes, date_modified_raw
						HAVING count(*) > 1
						ORDER BY bytes Desc) b
						WHERE a.bytes = b.bytes AND a.date_modified_raw = b.date_modified_raw
						ORDER BY bytes Desc
			"""
		else:
			sql = """

						SELECT *
						FROM files a, (SELECT bytes, date_modified_raw
						FROM files
						WHERE bytes > """+str(size)+"""
						GROUP BY bytes, date_modified_raw
						HAVING count(*) > 1
						ORDER BY bytes Desc) b
						WHERE a.bytes = b.bytes AND a.date_modified_raw = b.date_modified_raw
						ORDER BY bytes Desc



			"""
		if includeName:
			if sizeMax:
				sql = """
							SELECT *
							FROM files a, (SELECT bytes, date_modified_raw
							FROM files
							WHERE bytes > """+str(size)+""" and bytes < """+str(sizeMax)+"""
							GROUP BY bytes, date_modified_raw, name
							HAVING count(*) > 1
							ORDER BY bytes Desc) b
							WHERE a.bytes = b.bytes AND a.date_modified_raw = b.date_modified_raw
							ORDER BY bytes Desc
				"""
			else:
				sql = """
							SELECT *
							FROM files a, (SELECT bytes, date_modified_raw
							FROM files
							WHERE bytes > """+str(size)+"""
							GROUP BY bytes, date_modified_raw, name
							HAVING count(*) > 1
							ORDER BY bytes Desc) b
							WHERE a.bytes = b.bytes AND a.date_modified_raw = b.date_modified_raw
							ORDER BY bytes Desc
				"""

		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute(sql)
		records = c.fetchall()

		conn2 = sqlite3.connect(db)
		test = conn2.cursor()



		c.execute(sql)
		duplicates = {}

		_.fields.register( 'bytes', 'val', 7, m=20 )
		test = _.fields.padZeros( 'bytes', 'val', 5 )

		# theKeySort = []
		# spentKeys = []
		for f in records:
			row = {}
			for i,n in enumerate(names):
				row[n] = f[i]

			key = str(row['bytes'])+'_'+str(row['date_modified_raw'])
			# if not key in spentKeys:
			# 	spentKeys.append(key)
			# 	# theKeySort.append({  'key': key, 'orderby':   _.fields.padZeros( 'bytes', 'val', row['bytes'] )  })
			# 	theKeySort.append({  'key': key, 'orderby':   row['bytes']  })

			try:
				duplicates[ key ].append( row )
			except Exception as e:
				duplicates[ key ] = []
				duplicates[ key ].append( row )


		if len( records ) > 1:
			# from operator import itemgetter
			# keyManage = sorted(theKeySort, key=itemgetter('orderby'))
			# keyManage = _.tables.returnSorted( 'data', 'd.orderby', theKeySort )
			noPrint = _.switches.isActive('NoPrint')
			isSave = _.switches.isActive('Save')
			
			for key in duplicates.keys():
				if isSave: saveData.append('\n\n\n');
				if not noPrint:
					print()
					print()
					print()
				for di,dupRec in enumerate(duplicates[key]):
					if _.switches.isActive('Save'):
						saveData.append( dupRec['path'] )
					if not noPrint:
						print( dupRec['size'], dupRec['path'] )
						# print( dupRec['path'] )

					if di:
						totalSave += int(dupRec['bytes'])



		print()
		print()
		print()
		if _.switches.isActive('Save'):
			saveData.append( '\n\n\n' )
			saveData.append( 'Total: ' + formatSize(totalSave) )
			_.saveText( saveData, _.switches.values('Save')[0] )
		_.colorThis( [  'Total',  formatSize(totalSave) ], 'red' )
		sys.exit()



	global totalSize
	global totalCount
	totalSize = 0
	totalCount = 0

	if _.switches.isActive('ExtReport'):
		dbsX = _.switches.value('Database')
		dbs = dbsX.split(',')
		IDs = []
		if 'c' in _.switches.value('ExtReport').lower():
			IDs.append(0)
		elif 'd' in _.switches.value('ExtReport').lower():
			IDs.append(1)
		else:
			IDs.append(0)
			IDs.append(1)

		restrictSize = True
		restrictChar = True
		if 'all' in _.switches.value('ExtReport').lower():
			restrictSize = False
		if 'x' in _.switches.value('ExtReport').lower():
			restrictSize = False
			restrictChar = False
		# print(  )
		# print( dbs )
		# dbs = 'D:\\tech\\hosts\\MSI\\indexes\\D_Drive.db'
		# sys.exit()
		sql = "SELECT ext FROM files GROUP BY ext"
		data = []
		for i,db in enumerate(dbs):
			if i in IDs:
				# print( db )
				# sys.exit()
				run = True
				if run:
					conn = sqlite3.connect(db)
					c = conn.cursor()
					c.execute(sql)
					records = c.fetchall()
					# names = action2(databaseFile)
					for record in records:
						shouldAdd = True
						if restrictChar:
							if not record[0].isalnum():
								shouldAdd = False
						if restrictSize:
							if  ( len( record[0] ) == 3 or len( record[0] ) == 4 ):
								pass
							else:
								shouldAdd = False


						if shouldAdd:
							data.append( record[0] )
		dataX = []
		for row in set(data):
			dataX.append({ 'row': row })
		for row in _.tables.returnSorted( 'data', 'a.row', dataX ):
			print( row['row'].lower() )
		sys.exit()

	elif _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"
		for dbFile in databaseFile.split(','):
			if os.path.isfile(dbFile):
				try:
					do(dbFile)
				except Exception as e:
					pass
	if not _.switches.isActive('NoCount'):
		print()
		print('Total:')
		print('\tFiles:\t', _.addComma(totalCount) )
		print('\tSize:\t', formatSize(totalSize)  )
def do(databaseFile):
	# print(databaseFile)
	global totalSize
	global totalCount
	thisRan = []
	# print(databaseFile)
	# print('"'+databaseFile+'"')
	conn = sqlite3.connect(databaseFile)
	c = conn.cursor()
	# sql = "SELECT bytes,path FROM files WHERE path like '%0%'"
	# sql = "SELECT * FROM files WHERE bytes < 101 and bytes > 49  ORDER BY bytes"
	# sql = "SELECT bytes,path FROM files WHERE bytes < 101 and bytes > 49  ORDER BY bytes"
	# sql = "SELECT bytes,path FROM files WHERE bytes < 10000000 and bytes > 200  ORDER BY bytes"
	if _.switches.isActive('Plus') and not _.switches.isActive('Folder'):
		pv = _.switches.value('Plus')
		pvX = []
		for tP in _.switches.values('Plus'):
			if tP.startswith( '*.' ):
				pvX.append( tP )

		for tP in _.switches.values('Plus'):
			if not tP.startswith( '*.' ):
				if not tP in pvX:
					pvX.append( tP )

		_.switches.fieldSet('Text','active',True)
		_.switches.fieldSet('Text','value',pv.split(',')[0])
		# _.switches.fieldSet('Text','value',pvX[0])
	if _.switches.isActive('Text') and not  _.switches.isActive('Folder') and not _.switches.isActive('Size'):
		thisRan.append( 10100 )
		tv = _.switches.value('Text')
		# print( 'tv:',tv )
		if tv.startswith('*.'):
			tv = tv.replace('*.','').lower()
			sql = "SELECT * FROM files WHERE lower(ext) = '" + tv + "' ORDER BY bytes"
		elif tv.startswith('*'):
			tv = tv.replace('*','')
			sql = "SELECT * FROM files WHERE path like '%" + tv + "' ORDER BY bytes"
		elif tv.endswith('*'):
			tv = tv.replace('*','')
			sql = "SELECT * FROM files WHERE path like '" + tv + "%' ORDER BY bytes"
		else:
			sql = "SELECT * FROM files WHERE path like '%" + tv + "%' ORDER BY bytes"


	elif _.switches.isActive('Size') and not  _.switches.isActive('Folder'):
		thisRan.append( 10200 )
		s = _.switches.value('Size')
		sA = s.split(',')
		# print( unFormatSize(sA[1]) )
		# sys.exit()
		if sA[0].lower() == 'g':
			sql = "SELECT * FROM files WHERE bytes > " + str(unFormatSize(sA[1])) + " ORDER BY bytes"
		elif sA[0].lower() == 'l':
			sql = "SELECT * FROM files WHERE bytes < " + str(unFormatSize(sA[1])) + " ORDER BY bytes"
		elif sA[0].lower() == 'b' and len(sA) == 3:
			sql = "SELECT * FROM files WHERE bytes > " + str(unFormatSize(sA[1])) + " and bytes < " + str(unFormatSize(sA[2])) + " ORDER BY bytes"
			# print(sql)
		else:
			print('Error:')
			print('\tExpected:')
			print('\t\tp dirdb -db D_Drive.db -size g 2gb')
			print('\t\tp dirdb -db D_Drive.db -size b 1gb 3gb')
			sys.exit()
	elif not  _.switches.isActive('Folder'):
		thisRan.append(10300)
		sql = "SELECT * FROM files WHERE bytes > 100000000 ORDER BY bytes"
	if _.switches.isActive('Folder'):
		thisRan.append(10400)
		# print(_.switches.value('Folder'))
		sql = "SELECT * FROM files WHERE folder like '" + _.switches.value('Folder') + "' ORDER BY bytes"
	if _.switches.isActive('DateUnix'):
		s = _.switches.value('DateUnix')
		sA = s.split(',')
		sql = "SELECT * FROM files WHERE date_modified_raw > " + str(sA[0]) + " and date_modified_raw < " + str(sA[1]) + " ORDER BY bytes"
	if _.switches.isActive('Date'):
		sDate = _.switches.value('Date')
		sD = sDate.split(',')
		# print(sD[0])
		# print(isNu(sD[0]))
		# print(len(sD))
		if isNu(sD[0]) and len(sD) == 2:
			sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[0])) + " and date_modified_raw < " + str(epoch(sD[1],True)) + " ORDER BY bytes"
		elif len(sD) == 3:
			sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[1])) + " and date_modified_raw < " + str(epoch(sD[2],True)) + " ORDER BY bytes"
			# print(sql)
		elif len(sD) == 2:
			if sD[0] == 'before':
				sql = "SELECT * FROM files WHERE date_modified_raw < " + str(epoch(sD[1])) + " ORDER BY bytes"
			elif sD[0] == 'after':
				sql = "SELECT * FROM files WHERE date_modified_raw > " + str(epoch(sD[1])) + " ORDER BY bytes"
			else:
				print('before after between')
				sys.exit()
	if _.switches.isActive('Ago'):

		# print(timeAgo())
		# sys.exit()
		if not len( _.switches.values('Ago') ) > 1:
			sql = "SELECT * FROM files WHERE date_modified_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
		else:
			if False:
				pass
				
			elif _.switches.values('Ago')[1] == 'ad':
				sql = "SELECT * FROM files WHERE accessed_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
			elif _.switches.values('Ago')[1] == 'md':
				sql = "SELECT * FROM files WHERE date_modified_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
			elif _.switches.values('Ago')[1] == 'cd':
				sql = "SELECT * FROM files WHERE date_created_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
			
			elif _.switches.values('Ago')[1] == 'a':
				sql = "SELECT * FROM files WHERE accessed_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
			elif _.switches.values('Ago')[1] == 'm':
				sql = "SELECT * FROM files WHERE date_modified_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"
			elif _.switches.values('Ago')[1] == 'c':
				sql = "SELECT * FROM files WHERE date_created_raw > " + str(_.switches.values('Ago')[0]) + " ORDER BY bytes"



		# d = epoch()
		# print(d)
		# sys.exit()

	# sql = "SELECT bytes,path FROM files WHERE bytes > 100000000"
	# if  _.switches.isActive('Folder'):
		# print(sql)



	
	if _.switches.isActive('EXT'):
		# print( 'here' )
		sql = "SELECT * FROM files WHERE ext = '" + _.switches.value('EXT').lower() + "' AND path like '%" + _.switches.values('Plus')[0] + "%' ORDER BY bytes"
		print( sql )


	# print( 'here2' )
	# print( sql )
	# sys.exit()
	if _.switches.isActive('Test'):
		print()
		print( 'thisRan:', thisRan )
		print()
		print(sql)
		sys.exit()
	c.execute(sql)
	# c.execute('SELECT * FROM {tn} WHERE {cn} = {st}'.\
	#         format(tn='files', cn='path', st='s'))
	all_rows = c.fetchall()
	# print('1):', all_rows)
	names = action2(databaseFile)
	# print(names)
	global columnDefault
	global network_replace

	netReplaceI = None
	for nrXi, nrX in enumerate(network_replace):
		if nrX['file'].lower() in databaseFile.lower():
			netReplaceI = nrXi

	data = []
	for f in all_rows:
		# print(_.switches.value('Column'))

		row = {}
		for i,n in enumerate(names):
			row[n] = f[i]
		# print(row['path'])
		if _.switches.isActive('Column'):
			line = ''
			col = _.switches.value('Column')
			for ii,tc in enumerate(col.split(',')):
				i = ii + 1
				if tc == 'md5':
					try:
						line += str(md5(row['path']))
						if not len(col.split(',')) == i:
							line += str('\t')
					except Exception as e:
						line += '* MD5 Error *'
						if not len(col.split(',')) == i:
							line += str('\t')
					
				else:
					line += str(row[tc])
					if not len(col.split(',')) == i:
						line += str('\t')
		# if _.showLine(line) and os.path.isfile(row['path']):
		includeResult = False
		if _.showLine(row['path']):
			includeResult = True
			if not os.path.isfile( row['path'] ):
				includeResult = False
				removeFile( row['path'], c )
		if includeResult:

			data.append( row )
			# if not '$Recycle.Bin' in row['path']:
			totalCount += 1
			totalSize += row['bytes']
			# if not _.switches.isActive('Folder'):
			if columnDefault:
				if not _.switches.isActive( 'JustCount' ):
					if not netReplaceI is None:
						line = line.replace( network_replace[netReplaceI]['replace'], network_replace[netReplaceI]['with'] )
						line = line.replace( network_replace[netReplaceI]['replace'].lower(), network_replace[netReplaceI]['with'] )
						line = line.replace( network_replace[netReplaceI]['replace'].upper(), network_replace[netReplaceI]['with'] )
					try:
						print(line)
					except Exception as e:
						pass
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
					if not _.switches.isActive( 'JustCount' ):
						print(fS,'',row['path'])

	if not columnDefault:
		print()
		if not _.switches.isActive('JustCount'):
			_.switches.fieldSet('Long','active',True)
			_.tables.register( 'data', data )
			_.tables.print( 'data', _.switches.value('Column') )


def action2(databaseFile):
	connection = sqlite3.connect(databaseFile)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute('select * from files')
	row = cursor.fetchone()
	names = row.keys()
	# print(names)

	# for n in names:
	# 	print(n)
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
	if os.path.isfile(_v.myIndexes + _v.slash + 'D_Drive.db'):
		dbs = _v.myIndexes + _v.slash + 'C_Drive.db,' + _v.myIndexes + _v.slash + 'D_Drive.db'
	else:
		dbs = _v.myIndexes + _v.slash + 'C_Drive.db'
	# print(dbs)
	_.switches.fieldSet('Database','active',True)
	_.switches.fieldSet('Database','value',dbs)
	_.switches.fieldSet('Database','values',dbs.split(','))

if _.switches.isActive('BackupDrive'):
	dbs = _v.myIndexes + _v.slash + '3T_Drive.db'
	_.switches.fieldSet('Database','active',True)
	_.switches.fieldSet('Database','value',dbs)

columnDefault = False
if not _.switches.isActive('Column'):
	columnDefault = True
	_.switches.fieldSet('Column','active',True)
	_.switches.fieldSet('Column','value','path')

network_replace =   [{
                        'file': 'TBCN_shared.db',
                        'replace': 'Y:'+_v.slash,
                        'with': '\\\\tbcnad\\shared'+_v.slash,
                    },
                    {
                        'file': 'TBCN_Users.db',
                        'replace': 'X:'+_v.slash,
                        'with': '\\\\tbcnad\\Users'+_v.slash,
                    },
                    {
                        'file': 'TBCN_E.D.Files.db',
                        'replace': 'W:'+_v.slash,
                        'with': '\\\\tbcnad\\E.D. Files'+_v.slash,
                    },
                    {
                        'file': 'TBCN_erica.db',
                        'replace': 'V:'+_v.slash,
                        'with': '\\\\tbcnad\\erica'+_v.slash,
                    },
                    {
                        'file': 'TBCN_Facil.db',
                        'replace': 'U:'+_v.slash,
                        'with': '\\\\tbcnad\\Facil'+_v.slash,
                    },
                    {
                        'file': 'TBCN_Finance.db',
                        'replace': 'T:'+_v.slash,
                        'with': '\\\\tbcnad\\Finance'+_v.slash,
                    },
                    {
                        'file': 'TBCN_MasterControle.db',
                        'replace': 'S:'+_v.slash,
                        'with': '\\\\tbcnad\\MasterControle'+_v.slash,
                    },
                    {
                        'file': 'TBCN_MasterControle2.db',
                        'replace': 'S:'+_v.slash,
                        'with': '\\\\tbcnad\\MasterControle2'+_v.slash,
                    },]

def  removeFile( path, cursr ):
	# sql = "SELECT * FROM files WHERE path like '%" + tv + "%' ORDER BY bytes"
	sql = "   DELETE FROM files WHERE path = '"+path+"';   "
	if _.switches.isActive('Clean'):
		cursr.execute(sql)


########################################################################################
if __name__ == '__main__':
	action()



