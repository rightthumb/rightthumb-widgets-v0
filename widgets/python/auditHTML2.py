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
# import sqlite3
import time
import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext

from lxml import html
import requests
import cssselect

from bs4 import BeautifulSoup

# import _rightThumb._md5 as _md5
import _rightThumb._dir as _dir
import _rightThumb._mimetype as _mime

_.switches.register('Input', '-i,-f,-file','file.htm, https://lxml.de/tutorial.html')
_.switches.register('Folder', '-folder')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__] = {
	'file': 'auditHTML.py',
	'description': 'Report on html stuff',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['examples'].append('p auditHTML -i Pinterest_Page_Cache_ID-461548661794872237.html')
_.appInfo[__name__]['examples'].append('p auditHTML -i Pinterest_Page_Cache_ID-461548661804503455.html')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditHTML -folder + *.html')
_.appInfo[__name__]['examples'].append('')

# _.appInfo[__name__]['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         hasPre = False
#         if '.' in c or ':' in c:
#             hasPre = True
#             c = c.replace(':','.')
#             preDataR = c.split('.')
#             preData = preDataR[0]
#             c = preDataR[1]

#         for col in _.appInfo[__name__]['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         if hasPre:
#             c = preData + '.' + c
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
# _.switches.trigger('Sort',formatColumns)
# _.switches.trigger('GroupBy',formatColumns)

if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f


def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# __.pipeData = list(data)
	# _.appData[focus()]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[focus()]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[focus()]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




# _.appData[focus()]['pipe'] = ''
# if not sys.stdin.isatty():
#     _.appData[focus()]['pipe'] = sys.stdin.readlines()
#     pipeCleaner()














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
#         print('This is a switch')




#     if _.switches.isActive('Output') == True:


#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)



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

# if _.switches.isActive('Move'):
	# shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))


########################################



#     json = _.getTable('base64Key.json')
#    books = _.getText(_v.myTables + _v.slash+'bible_books.csv')

# _mime.isText(file)
# _mime.isBinary(file)


# _.saveTable(jsonFile,'file.json')
# _.saveText(convertedFile,_.ci(_.switches.value('Output')))
# _.saveText(convertedFile,'file.txt')
# _.showLine(item)
########################################################################################


def extractID(text):
	global removeThis
	text = str(text)
	text = text.replace('\n','')
	text = text.replace('\r','')
	text = text.replace(' ','')
	before = len(text)
	for rt in removeThis:
		text = text.replace(rt,'')
	after = len(text)
	if before == after:
		text = ''
	return text
def getPage(url):
	global thisWebPage
	if type(thisWebPage) == bool:
		f = open(url, 'r', encoding='UTF-8')
		file = f.read()
		file = file.encode('latin-1','ignore')
		file = file.decode('utf-8','ignore')
		thisWebPage = BeautifulSoup(file,"html.parser")
	return thisWebPage
def getLocal(url):
	print('Not Configured')
	sys.exit()

def getPageTitle(url):
	thisWebPage = getPage(url)
	return thisWebPage.title.string

def getPageStructure(url,report):
	global projectReport
	projectReport = []
	thisWebPage = getPage(url)
	first_child = thisWebPage.find("body")
	for i,ch in enumerate(first_child.children):
		data = { 'data': [], 'el': [], 'ids': [], 'timestart': time.time()}
		thinkOfTheChildren(ch,data)
	report['structure'] = projectReport
	return report

def thinkOfTheChildren(obj,report,path='-'):
	global projectReport
	try:
		path += ':' + obj.name
	except Exception as e:
		path += ':-'
	try:
		ids = str(obj.get('id'))
		if not ids == 'None':
			report['ids'].append()
	except Exception as e:
		pass
	try:
		# path += ':[' + obj.name + ':' + obj.get('id') + '(' + obj.get('class') + ')]'
		path += '[' + obj.get('id') + ']'
	except Exception as e:
		pass
	# try:
	#     if len(str(obj)) > 2:
	#         report['el'].append({'path': path,'obj': str(obj)})
	# except Exception as e:
	#     pass
	try:
		# path += ':[' + obj.name + ':' + obj.get('id') + '(' + obj.get('class') + ')]'
		# path += '(' + obj.get('class') + ')'
		try:
			report['data'].append({'path': path,'attrib': dict(obj.attrs.values())})
		except Exception as e:
			try:
				report['data'].append({'path': path,'attrib': list(obj.attrs.values())})
			except Exception as e:
				pass
	except Exception as e:
		pass
	try:
		test = 1
		for ch in obj.children:
			thinkOfTheChildren(ch,report,path)
	except Exception as e:
		test = 0
	if not test:
		report['el'].append({'path': path,'obj': obj})
		report['timeend'] = time.time()
		projectReport.append(report)
		# print(path,obj)



# def checkComplete(pinID):
#     global projectReport
#     result = True
#     for pr in projectReport:
#         if pr['pinID'] == pinID:
#             result = False
#     return result





def saveResults(data):
	print()
	if type(data) == dict:
		report.append(data)
		print(report)
		_.saveTable(report,'auditHTML.json')
	else:
		print('Not Saved')

def action():
	global thisWebPage
	global projectReport
	global completedIDs
	# global projectReport
	if _.switches.isActive('Input'):
		url = _.switches.value('Input')
		if 'http' in url:
			saveResults(getRemote(url))
		else:
			pageTitle = getPageTitle(url)
			print('title:',pageTitle)
			pinID = extractID(url)
			report = {'pinID': pinID, 'title': pageTitle, 'structure': [], 'timestart': time.time()}
			pageStructure = getPageStructure(url,report)
			_.saveTable(pageStructure,'auditHTML.json')
			# saveResults()


	if _.switches.isActive('Folder'):
		folder = os.getcwd()
		dirList = os.listdir(folder)
		i = 0

		for tdi,td in enumerate(dirList):
			td = td.replace('\n','')
			if _.showLine(td):
				pinID = extractID(td)

				# if checkComplete(pinID):
				if not pinID in completedIDs:
					projectReport = []
					try:
						print()
						print(_dir.formatSize(_dir.getSize(td)),pinID)
						pageTitle = getPageTitle(td)
						# print('title:',pageTitle)
						report = {'pinID': pinID, 'title': pageTitle, 'structure': [], 'timestart': time.time()}

						getPageStructure(td,report)
						
					except Exception as e:
						pass
					thisWebPage = True
					dataPath = 'D:\\Pinterest_Cache_Report\\Pinterest_Page_Cache_Report_ID-THEID.json'
					jsonFile = dataPath.replace('THEID',pinID)
					if len(projectReport) > 0:
						print('memory:',sys.getsizeof(projectReport))
						# print(projectReport)
						_.saveTable3(projectReport,jsonFile    )
						projectReport = []


		# for item in dirList:
		#     path = folder + _v.slash + item
		#     if os.path.isfile(item):
		#     # if os.path.isdir(item) == True:
		#         if _mime.isText(item) and _.showLine(item):
		#             saveResults(getLocal(item))
					
		#             i = i + 1
# saveResults(getLocal(item))
if __name__ == '__main__':
	projectReport = []
	removeThis = []
	removeThis.append('Pinterest_Page_Cache_ID-')
	removeThis.append('.html')
	removeThis.append('.json')
	removeThis.append('Pinterest_Pin_Data_ID-')
	removeThis.append('Pinterest_Page_Cache_Report_ID-')
	removeThis.append('Pinterest_Cache_Report')
	removeThis.append(_v.slash)
	removeThis.append('D:')
	completedIDs = []
	completedIDs.append('461548661795334760')
	if os.path.isdir('D:\\Pinterest_Cache_Report'):
		dirList = os.listdir('D:\\Pinterest_Cache_Report')
		for item in dirList:
			completedIDs.append(extractID(item))

	print('completedIDs:', len(completedIDs))

# auditHTML
thisWebPage = True
# projectReport = _.getTable('auditHTML.json')
########################################################################################
if __name__ == '__main__':
	action()