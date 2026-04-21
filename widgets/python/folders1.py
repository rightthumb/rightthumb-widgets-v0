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
# import sqlite3

import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext



import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

if __name__ == '__main__':
	_.switches.register('NoCount', '--c,--count')
	_.switches.register('JustCount', '-jc,++c,++count')
	_.switches.register('FileCount', '-f')
	_.switches.register('CleanBlank', '-clean')
	_.switches.register('Raw', '-raw')
	_.switches.register('Folder', '-folder')
	_.switches.register('MaxDepth', '-depth')

	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=    {
		'file': 'folders.py',
		'description': 'Lists folders, file count, clear empty',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p folders ')

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
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
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
i = 0
folderList = []
def getFolder(folder):
	global i
	global folderList
	global baseDepth

	if _.switches.isActive('MaxDepth'):
		if len(_.switches.value('MaxDepth')):
			maxDepth = int(_.switches.value('MaxDepth'))
		else:
			maxDepth = 4
		if len( folder.split(_v.slash) ) - baseDepth >= maxDepth:
			return None


	try:
		dirList = os.listdir(folder)
		action = True
	except Exception as e:
		action = False
	if action:
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace( _v.slash+_v.slash, _v.slash )
			# if os.path.isfile(item) == True:
			if os.path.isdir(path) == True:
				i = i + 1
				# print(path)
				if _.switches.isActive('Raw'):
					print(path)
				else:
					folderList.append(path)
				newFolder = folder + _v.slash + item
				try:
					getFolder(newFolder)
				except Exception as e:
					pass
iF = 0
def fileCount(folder):
	global iF
	i = 0
	# print()
	# print()
	# print(folder)
	# print(dirList)
	try:
		dirList = os.listdir(folder)
		action = True
	except Exception as e:
		action = False
	if action:
		for item in dirList:
			path = folder + _v.slash + item
			# if os.path.isfile(path):
			i += 1
	iF += i
	return i




baseDepth = 0
def action():
	global i
	global iF
	global folderList
	global omit
	global baseDepth

	_.switches.fieldSet('Long','active',True)
	if not _.switches.isActive('Sort'):
		_.switches.fieldSet('Sort','active',True)
		_.switches.fieldSet('Sort','value','a.count')
		# _.switches.fieldSet('Sort','value','d.count')


	folder = os.getcwd()
	if _.switches.isActive('Folder'):
		folder = _.switches.value('Folder')

	baseDepth = len( folder.split(_v.slash) )



	getFolder(folder)

	data = []
	clean = True
	cnt = 0
	for folder in folderList:
		if not _.switches.isActive('JustCount') and not _.switches.isActive('FileCount'):
			if _.showLine( folder ):
				cnt+=1
				print(folder)
		elif _.switches.isActive('FileCount'):
			count = fileCount(folder)
			if count == 0:
				clean = False
			data.append({'count': count, 'folder': folder})




	if len(data) > 0:
		print()
		_.tables.register('folders',data)
		_.tables.fieldProfileSet('folders','count','alignment','center')
		_.tables.print('folders','count,folder')
		if not _.switches.isActive('NoCount'):
			print()
			print()
			_.tables.register('count',[{'folders': i, 'files': iF}])
			_.tables.fieldProfileSet('count','folders,files','alignment','center')
			_.tables.print('count','folders,files')
			# print('\n{}\tFolders\n{}\tFiles\n'.format(i,iF))
		if _.switches.isActive('CleanBlank'):
			print()
			if clean:
				print('folders clean')
			else:
				print('Confirm delete:')
				for d in data:
					if d['count'] == 0:
						print('\t',d['folder'])
				confirm = input('Confirm: ')
				print()
				if not 'n' in confirm.lower():
					for d in data:
						if d['count'] == 0:
							for o in omit:
								skip = False
								if o in d['folder']:
									skip = True
							if skip:
								print('Skipped:', d['folder'])
							else:
								do = 'rmdir /Q "' + d['folder'] + '"'
								print(do)
								os.system('"' + do + '"')
				print()
				if not 'n' in confirm.lower():
					print('folders cleaned')
				else:
					print('canceled')
	else:
		if not _.switches.isActive('NoCount'):
			if cnt:
				print('\n{}\n'.format(cnt))
			else:
				print('\n{}\n'.format(i))

omitList = 'GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}'
omit = omitList.split(',')

########################################################################################
if __name__ == '__main__':
	action()