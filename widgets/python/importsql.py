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
# import sys
# import simplejson as json
# import shutil

import sqlite3


import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

if __name__ == '__main__':

	_.switches.register('Database', '-db,-database','%i%/C_Drive.db')
	_.switches.register('File', '-file,-sql','%i%/dump.sql')

	_.appInfo=    {
		'file': 'importsql.py',
		'description': 'Changes the world',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p importsql -sql dump.sql -db dump.db')

	# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


	_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
theSQL = []
def action():
	global theSQL
	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
		else:
			databaseFile = "defaultDir.db"

		if len(_.switches.value('File')) > 1:
			sqlFile = _.switches.value('File')
		else:
			sqlFile = "dump.sql"
		databaseFile = _v.myDatabases + _v.slash + databaseFile
		if os.path.isfile(databaseFile):
			print('')
			question = input('Delete database: ' + databaseFile + '? (y): ')
			if 'y' in  question.lower() or len(question) == 0:
				os.system('del /Q "' + databaseFile + '"')
		if os.path.isfile(databaseFile):
			print('Operation aborted')
		else:
			con = sqlite3.connect(databaseFile)
			cur = con.cursor()
			if len(theSQL) == 0:
				f = open(sqlFile,'r')
				# line = f.read()
				lines = f.readlines()
			else:
				lines = theSQL
			for l in lines:
				l = l.replace('\n','')
				cur.execute(l)
			print()
			if not os.path.isfile(databaseFile):
				print('Database creation failure')
			else:
				print('Database created')
				print('Example:')
				


########################################################################################
if __name__ == '__main__':
	action()