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
import platform
# import simplejson as json
# import shutil
# import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

if __name__ == '__main__':
	_.switches.register('App', '-app','har')
	_.switches.register('Edit', '-edit')
	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=    {
		'file': 'dba.py',
		'description': 'Auto database app',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p dba -app har')
	_.appInfo['examples'].append('')
	_.appInfo['examples'].append('Related:')
	_.appInfo['examples'].append('\t' + 'p json2db -build -app -i sample.json')
	_.appInfo['examples'].append('\t' + 'p databaseInfo -i har.db')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
if __name__ == '__main__':
	_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


# if _.switches.isActive('_File_'):
#     _.tables.register('toCheck') # table, rows = []
#     _.switches.fieldSet('_File_','active',True)
#     _.switches.fieldSet('_File_','value','toCheck.json')
#     _.tables.get('toCheck',_.switches.value('_File_'))
#     _.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
#     _.tables.sort('toCheck', 'name')

#     _.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
#     _.tables.view('test_table','sample') # table, view

#     _.switches.fieldGet('Column','pos')
#     if _.switches.exists('Column2'):
#         print('This is a valid switch')




#     if _.switches.isActive('Output') == True:
#         _.saveTable2(jsonFile,_.switches.value('Output'))
#         # _.saveText(convertedFile,_.ci(_.switches.value('Output')))

#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('App')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('App')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')

#    books = _.getText(_v.myTables + _v.slash+'bible_books.csv')

########################################################################################
# class TheChildItems:

#     def __init__(self, name, switch):
#         self.name = name
#         self.active = False
#         self.value = None

#     def trigger(self,script):
#         self.script_trigger = script

#     def changeStatus(self,newStatus):
#         self.active = newStatus
# class TheParentItems:

#     def __init__(self):
#         self.childItemRows = []

#     def register(self, name):
#         self.childItemRows.append(TheChildItems(name))
#     def print(self):
#         childItems = []
#         for ci in self.childItemRows:
#             childItems.append({'name':ci.name})
#         _.tables.register('childClassItems',childItems)
#         # tables.trigger('switches','switch,name',test,True)
#         _.tables.print('childClassItems','name')
#     def printStatus(self):
#         childItems = []
#         for ci in self.childItemRows:
#             if ci.active:
#                 active = 'True'
#             else:
#                 active = 'False'
#             value = ci.value
#             if ci.value == True:
#                 value = 'True'
#             elif ci.value == False:
#                 value = 'False'

#             childItems.append({'name':ci.name ,'active':active,'value': value})
#         _.tables.register('childClassItems',childItems)
#         _.tables.print('childClassItems','name,active,value')
#     def status(self,name,newStatus):
#         for i,ci in enumerate(self.childItemRows):
#             if ci.name == name:
#                 self.childItemRows[i].changeStatus(newStatus)
########################################################################################
def isApp(app):
	global dbF
	global jsonF
	appDB = _v.myDatabases + _v.slash + app + dbF
	appJSON = _v.myDatabases + _v.slash + app + jsonF
	if os.path.isfile(appDB):
		result = True
	else:
		result = False
	return result
def findApp(app):
	global dbF
	global jsonF
	result = ''
	app2 = app.lower()
	if not isApp(app2):
		print('findApp:',app)
		print()
		dirList = os.listdir(_v.myDatabases)
		records = []
		for aFile in dirList:
			aFileLo = aFile.lower()
			if dbF in aFileLo and app in aFileLo:
				file = aFile.replace(dbF,'').replace(jsonF,'').replace('.db','')
				if os.path.isfile(_v.myDatabases + _v.slash + file + dbF) and not file in records:
					print('\t',len(records),file)
					records.append(file)
		print()
		if len(records) == 0:
			print('No app')
			sys.exit()
		elif len(records) > 1:
			select = input('Select:\t')
			try:
				result = records[int(select)]
			except Exception as e:
				print('No app')
				sys.exit()
		elif len(records) == 1:
			result = records[0]
	else:
		result = app
	return result
def openConfig():
	if _.switches.isActive('App'):
		app = _.switches.value('App')
		if _v.slash in app:
			a = app.split(_v.slash)
			app = a[len(a)-1]
		app = app.replace('.json','')
		database = _.Database(app)
		appPyRaw = database.appPyRaw
		appPy = database.appPy
		do = 'start "edit" ' + _v.notepad() + ' "' + database.appPy + '"'
		print(do)
		os.system('"' + do + '"')
		if platform.system() == 'Windows':
			do = 'cls'
		else:
			do = 'clear'
		os.system('"' + do + '"')
		print('')
		meta = database.metaPrint()
	sys.exit()
def action():
	global dbF
	global jsonF
	if _.switches.isActive('App'):
		app = _.switches.value('App')
		if _v.slash in app:
			a = app.split(_v.slash)
			app = a[len(a)-1]
		app = app.replace('.json','')
		

		app = app.replace(dbF,'').replace(jsonF,'')
		app = findApp(app)
		print('App:',app)
		print()

		database = _.Database(app)
		appPyRaw = database.appPyRaw
		appPy = database.appPy

		if not os.path.isfile(database.appPy):
			from shutil import copyfile
			copyfile(database.appPyDefault, database.appPy)
		
			do = 'start "edit" ' + _v.notepad() + ' "' + database.appPy + '"'
			os.system('"' + do + '"')
			if platform.system() == 'Windows':
				do = 'cls'
			else:
				do = 'clear'
			os.system('"' + do + '"')
			print('')
			meta = database.metaPrint()
			sys.exit()


		if _.switches.isActive('Edit'):
			do = 'start "edit" ' + _v.notepad() + ' "' + database.appPy + '"'
			os.system('"' + do + '"')
			if platform.system() == 'Windows':
				do = 'cls'
			else:
				do = 'clear'
			os.system('"' + do + '"')
			print('')
			meta = database.metaPrint()
			sys.exit()


		sys.path.insert(0, _v.myDatabases)
		theApp = __import__(appPyRaw)

		sqlBuilder = theApp.sql
		try:
			if _.switches.isActive('Plus'):
				sqlBuilder['action'][0]['search'] = _.switches.value('Plus')
		except Exception as e:
			pass
		sql = database.queryBuilder(sqlBuilder)
		print(sql)
		print()
		print()
		data = database.executeSQL(sql)
		print()
		




dbF = '_Generated_App_Database.db'
jsonF = '_Generated_App_Database_Config.json'
########################################################################################
if __name__ == '__main__':
	try:
		action()
	except Exception as e:
		openConfig()