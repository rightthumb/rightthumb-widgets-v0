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
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import sqlite3


import sys
import hashlib

import os


_.switches.register('Database', '-db,-database','%i%/C_Drive.db')
_.switches.register('MD5', '-md5')

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'dirDBMD5.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p dirDBMD5 -database defaultDir.db')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirDBMD5 -db %i%/C_Drive.db -c name')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p dirdbmd5 -db test_MD5.db')
_.appInfo['examples'].append('')









_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo['columns'].append({'name': 'path', 'abbreviation': 'p'})
_.appInfo['columns'].append({'name': 'folder', 'abbreviation': 'f'})
_.appInfo['columns'].append({'name': 'bytes', 'abbreviation': 'b'})

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
	size = int(size)
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


def action():
	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"

		# print(databaseFile)
		# print(databaseFile)
		conn = sqlite3.connect(databaseFile)
		c = conn.cursor()
		# sql = "SELECT bytes,path FROM files WHERE path like '%0%'"
		sql = "SELECT * FROM md5  ORDER BY bytes"
		# sql = "SELECT bytes,path FROM files WHERE bytes < 101 and bytes > 49  ORDER BY bytes"
		# sql = "SELECT bytes,path FROM files WHERE bytes < 10000000 and bytes > 200  ORDER BY bytes"
		# sql = "SELECT bytes,path FROM files WHERE bytes > 100000000"
		c.execute(sql)
		# c.execute('SELECT * FROM {tn} WHERE {cn} = {st}'.\
		#         format(tn='files', cn='path', st='s'))
		all_rows = c.fetchall()
		# print('1):', all_rows)
		names = action2()
		# print(len(all_rows))
		rows = []
		print(len(all_rows))
		sys.exit()
		for f in all_rows:
			# print(f)
			# print(_.switches.value('Column'))

			row = {}
			for i,n in enumerate(names):
				row[n] = f[i]
			if _.switches.isActive('Column'):
				line = ''
				col = _.switches.value('Column')
				for c in col.split(','):
					line += str(row[c]) + str('\t')
				print(line)
			else:
				rows.append({'md5': row['md5'], 'bytes': formatSize(row['bytes']), 'name': row['name'], })
				# print(row['md5'],formatSize(row['bytes']),'\t',row['name'])

		if not _.switches.isActive('Column'):
			_.tables.register('Auto',rows)
			_.tables.print('Auto','md5,bytes,name')

			# if _.switches.value('Column') == 'name' or _.switches.value('Column') == 'n':
			#     print(f[1])
			# else:
			#     print(formatSize(f[0]),'\t',f[1])

def action2():
	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"
	connection = sqlite3.connect(databaseFile)
	connection.row_factory = sqlite3.Row
	cursor = connection.execute('select * from md5')
	row = cursor.fetchone()
	names = row.keys()
	# print(names)

	# for n in names:
		# print(n)
	
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
########################################################################################
if __name__ == '__main__':
	action()
	# print(action2())