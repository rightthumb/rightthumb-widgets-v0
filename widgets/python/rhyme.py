#!/usr/bin/python3
# import os
# import sys
# import simplejson as json
# import shutil
# import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

if __name__ == '__main__':
	_.switches.register('Input', '-i','dic_adj.json')
	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=	{
		'file': 'rhyme.py',
		'description': 'Changes the world',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p rhyme + *mber *mer -or -i dic_noun.json - _> %tmpf1%')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
# 	result = ''
# 	for c in columns.split(','):
# 		for col in _.appInfo['columns']:
# 			for a in col['abbreviation'].split(','):
# 				if a == c:
# 					c = col['name']
# 		result += c + ','
# 	result = result[:-1]
# 	return result

# _.switches.trigger('Column',formatColumns)
if __name__ == '__main__':
	_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
# 	pipeData = sys.stdin.readlines()
# 	try:
# 		if pipeData[0][0].isalnum() == False:
# 			pipeData[0] = pipeData[0][1:]
# 	except Exception as e:
# 		pass


# if _.switches.isActive('_File_'):
# 	_.tables.register('toCheck') # table, rows = []
# 	_.switches.fieldSet('_File_','active',True)
# 	_.switches.fieldSet('_File_','value','toCheck.json')
# 	_.tables.get('toCheck',_.switches.value('_File_'))
# 	_.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
# 	_.tables.sort('toCheck', 'name')

# 	_.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
# 	_.tables.view('test_table','sample') # table, view

# 	_.switches.fieldGet('Column','pos')
# 	if _.switches.exists('Column2'):
# 		print('This is a valid switch')




# 	if _.switches.isActive('Output') == True:
# 		_.saveTable2(jsonFile,_.switches.value('Output'))
# 		# _.saveText(convertedFile,_.ci(_.switches.value('Output')))

# 	if _.switches.isActive('Move') == True:
# 	        shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
# 	# if _.showLine(string):
# 		# print(line)

# 	json = _.getTable('base64Key.json')

#	books = _.getText(_v.myTables + '\\bible_books.csv')

########################################################################################
# class TheChildItems:

# 	def __init__(self, name, switch):
# 		self.name = name
# 		self.active = False
# 		self.value = None

# 	def trigger(self,script):
# 		self.script_trigger = script

# 	def changeStatus(self,newStatus):
# 		self.active = newStatus
# class TheParentItems:

# 	def __init__(self):
# 		self.childItemRows = []

# 	def register(self, name):
# 		self.childItemRows.append(TheChildItems(name))
# 	def print(self):
# 		childItems = []
# 		for ci in self.childItemRows:
# 			childItems.append({'name':ci.name})
# 		_.tables.register('childClassItems',childItems)
# 		# tables.trigger('switches','switch,name',test,True)
# 		_.tables.print('childClassItems','name')
# 	def printStatus(self):
# 		childItems = []
# 		for ci in self.childItemRows:
# 			if ci.active:
# 				active = 'True'
# 			else:
# 				active = 'False'
# 			value = ci.value
# 			if ci.value == True:
# 				value = 'True'
# 			elif ci.value == False:
# 				value = 'False'

# 			childItems.append({'name':ci.name ,'active':active,'value': value})
# 		_.tables.register('childClassItems',childItems)
# 		_.tables.print('childClassItems','name,active,value')
# 	def status(self,name,newStatus):
# 		for i,ci in enumerate(self.childItemRows):
# 			if ci.name == name:
# 				self.childItemRows[i].changeStatus(newStatus)
########################################################################################
def action():
	json = _.getTable(_.switches.value('Input'))

	for k in json.keys():
		if _.showLine(k):
			print(k.replace('_',' '))



########################################################################################
if __name__ == '__main__':
	action()



