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
# import simplejson as json
# import shutil

from datetime import datetime as dt, timedelta
import datetime

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import sqlite3


import sys
import hashlib

_.switches.register('NoCount', '--c,--count')
_.switches.register('Database', '-db,-database','%i%/C_Drive.db')
_.switches.register('MD5', '-md5')
_.switches.register('Size', '-size')
_.switches.register('Text', '-text')
_.switches.register('Folder', '-folder')
_.switches.register('DateUnix', '-dateunix','1183330364 1193957564')
_.switches.register('Ago', '-ago')
_.switches.register('Date', '-date')

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'dirDB.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p dirDB -database defaultDir.db')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirDB -db %i%\\C_Drive.db -c name')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirDB -db %i%\\C_Drive.db -c name | p dir -c s p -s bytes')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb -db C_Drive.db -c n | p dir -s s -c s p')
_.appInfo['examples'].append('p dirdb -db D_Drive.db -c n | p dir -s s -c s p')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb -db D_Drive.db -size g 2gb')
_.appInfo['examples'].append('p dirdb -db D_Drive.db -size b 1gb 3gb')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb -db C_Drive.db -c p  + *.pdf')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018.')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018. --c | p line --c -p \\ ee -u | p line --c -make "p dirdb -folder ;\'{};\' + *.txt --c " | p execute | p line --c - "p dirdb"')
_.appInfo['examples'].append('p dirdb + *.pdf resume scott reph - bookmarks 2018. --c |p line --c -p \\ ee -u |p line --c -make "p dirdb -folder ;\'{};\' + *.txt --c " |p execute |p line --c - "p dirdb" |p f + com gen -jn')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb + \\201 | p line --c -p \\ ;mdt | p sortMDT -r')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdb -db %i%\\C_Drive.db -c s p -size g 100mb')
_.appInfo['examples'].append('')






_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo['columns'].append({'name': 'name_', 'abbreviation': 'n_'})
_.appInfo['columns'].append({'name': 'path', 'abbreviation': 'p'})
_.appInfo['columns'].append({'name': 'folder', 'abbreviation': 'f'})
_.appInfo['columns'].append({'name': 'friendly_month', 'abbreviation': 'fm'})
_.appInfo['columns'].append({'name': 'friendly_week', 'abbreviation': 'fw'})
_.appInfo['columns'].append({'name': 'month', 'abbreviation': 'm'})
_.appInfo['columns'].append({'name': 'attrib', 'abbreviation': 'a'})
_.appInfo['columns'].append({'name': 'bytes', 'abbreviation': 'b'})
_.appInfo['columns'].append({'name': 'ext', 'abbreviation': 'e'})
_.appInfo['columns'].append({'name': 'type', 'abbreviation': 't'})
_.appInfo['columns'].append({'name': 'size', 'abbreviation': 's'})
_.appInfo['columns'].append({'name': 'week_of_year_', 'abbreviation': 'w2,woy2'})
_.appInfo['columns'].append({'name': 'week_of_year', 'abbreviation': 'woy,w'})
_.appInfo['columns'].append({'name': 'day_of_the_week', 'abbreviation': 'd,dotw,dow'})
_.appInfo['columns'].append({'name': 'date_modified', 'abbreviation': 'mdate,datem,dm,md'})
_.appInfo['columns'].append({'name': 'date_created', 'abbreviation': 'cdate,datec,dc,cd'})

_.appInfo['columns'].append({'name': 'date_modified_raw', 'abbreviation': 'dmr,mdr'})
_.appInfo['columns'].append({'name': 'date_created_raw', 'abbreviation': 'dcr,cdr'})

_.appInfo['columns'].append({'name': 'md5', 'abbreviation': 'md5'})

# stat
# typesort

def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Column',formatColumns)



_.switches.process()


# timestamp 
# echo %now% > %tmpf2%
# type %tmpf1% | p line -make " md5.py ;'{};' >> ;'%tmpf2%;'" | p execute
# timestamp
# echo %now% >> %tmpf2%
# done




# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
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
		print()
		print('Total:')
		print('\tFiles:\t',totalCount)
		print('\tSize:\t',formatSize(totalSize))
def do(databaseFile):
	# print(databaseFile)
	global totalSize
	global totalCount
	# print(databaseFile)
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
			print(sql)
		else:
			print('Error:')
			print('\tExpected:')
			print('\t\tp dirdb -db D_Drive.db -size g 2gb')
			print('\t\tp dirdb -db D_Drive.db -size b 1gb 3gb')
			sys.exit()
	elif not  _.switches.isActive('Folder'):
		sql = "SELECT * FROM files WHERE bytes > 100000000 ORDER BY bytes"
	if _.switches.isActive('Folder'):
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
		sql = "SELECT * FROM files WHERE date_modified_raw > " + str(timeAgo()) + " ORDER BY bytes"

		# d = epoch()
		# print(d)
		# sys.exit()

	# sql = "SELECT bytes,path FROM files WHERE bytes > 100000000"
	# if  _.switches.isActive('Folder'):
		# print(sql)
	c.execute(sql)
	# c.execute('SELECT * FROM {tn} WHERE {cn} = {st}'.\
	#         format(tn='files', cn='path', st='s'))
	all_rows = c.fetchall()
	# print('1):', all_rows)
	names = action2(databaseFile)
	# print(names)
	for f in all_rows:
		# print(_.switches.value('Column'))

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
			# if not '$Recycle.Bin' in row['path']:
			totalCount += 1
			totalSize += row['bytes']
			# if not _.switches.isActive('Folder'):
			print(line)
		else:
			if _.showLine(row['path']) and os.path.isfile(row['path']):
				# if not '$Recycle.Bin' in row['path']:
				totalCount += 1
				totalSize += row['bytes']
				fS = formatSize(row['bytes'])
				while len(fS) < 10:
					fS += ' '
				# if not _.switches.isActive('Folder'):
				print(fS,'',row['path'])



def action2(databaseFile):
	connection = sqlite3.connect(databaseFile)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute('select * from files')
	row = cursor.fetchone()
	names = row.keys()
	# print(names)

	# for n in names:
	#     print(n)
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
	# print(dbs)
	_.switches.fieldSet('Database','active',True)
	_.switches.fieldSet('Database','value',dbs)

if not _.switches.isActive('Column'):
	_.switches.fieldSet('Column','active',True)
	_.switches.fieldSet('Column','value','path')

########################################################################################
if __name__ == '__main__':
	action()





