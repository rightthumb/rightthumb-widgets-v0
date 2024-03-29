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
import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


from lxml import html
import requests
import cssselect

from bs4 import BeautifulSoup


# import urllib.parse

# from lxml import etree

# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

_.switches.register('Input', '-i,-f,-file','file.txt')
_.switches.register('Field', '-field','name')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__] = {
	'file': 'pinterestGetPageTitleFromCache.py',
	'description': 'Changes the world',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[__name__] = {
	'var': '',
	'pipe': [],
	}

_.appInfo[__name__]['examples'].append('p pinterestGetPageTitleFromCache -i file.txt ')

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
def path2url(path):
	"""Return file:// URL from a filename."""
	path = os.path.abspath(path)
	# if isinstance(path, unicode):
	#     path = path.encode('utf8')
	return 'file:' + urlparse.pathname2url(path)

def osPath2URI(path):
	osp = os.path.abspath(path)
	result = 'file://' + osp
	result = result.replace(_v.slash,'/')
	# 'file:///C:/fun/filename.txt'
	# 'D:\Pinterest_Cache\Pinterest_Page_Cache_ID-461548661796181065.html'
	# print(path)
	# print(result)
	return result


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

def getLocal(url):
	f = open(url, 'r', encoding='UTF-8')
	file = f.read()
	file = file.encode('latin-1','ignore')
	file = file.decode('utf-8','ignore')
	# # code = etree.parse(os.path.abspath(url))
	code = BeautifulSoup(file,"html.parser")
	return code.title.string
	# print(osPath2URI(url))
	# sys.exit()

	# path = path2url(url)
	# print(path)

	# page = requests.get('https://docs.python-guide.org/scenarios/scrape/')
	# print(type(page))
	# sys.exit()

	# path = osPath2URI(url)
	# print(path)
	# sys.exit()
	# code = requests.get(path)

	# print('len(code)',len(code))
	# # for cl in code:
	# #     print(cl)
	# print(code)
	# sys.exit()
	# processPage((code))
	# page = requests.get(url)

def processPage(code):
	tree = html.fromstring(code)
	pageTitle0 = tree.cssselect('title')
	pageTitle = pageTitle0[0].text_content()
	return pageTitle
def action():
	resultData = []

	if _.switches.isActive('Input'):
		# os.system('cls')
		pinData = _.getTable('pinterestData.json')
		textData = _.getText(_.switches.value('Input'))
		# print('pinData',len(pinData))
		# print('textData',len(textData))
		# sys.exit()
		if len(textData) > 0 and len(pinData) > 0:
			for tdi,td in enumerate(textData):
				td = td.replace('\n','')
				pinID = extractID(td)
				# if len(pinID) > 5 and tdi == 0:
				if len(pinID) > 5:
					found = False
					for pdi,pd in enumerate(pinData):
						# print(pd['pinID'])
						if pd['pinID'] == pinID:
							found = True

							data = {}
							data['pinID'] = pd['pinID']
							htmlTitle = getLocal(td)
							pinData[pdi]['webtitle'] = htmlTitle
							print()
							# print('pinData:',pinData[pdi]['pinID'])
							# print('pinID:\t',pinID)
							print('pin:\t',pd['name'])
							print('page:\t',htmlTitle)
							# try:
							# except Exception as e:
							#     pass


						
		_.saveTable(pinData,'pinterestData.json')
		print('Done and saved')




removeThis = []
removeThis.append('Pinterest_Page_Cache_ID-')
removeThis.append('.html')
removeThis.append('.json')
removeThis.append('Pinterest_Pin_Data_ID-')


# pinterestGetPageTitleFromCache
########################################################################################
if __name__ == '__main__':
	action()





