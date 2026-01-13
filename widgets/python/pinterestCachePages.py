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

import time


# import urllib2
# import urllib.request as urllib2


# import nltk   
# from urllib import urlopen


# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# _.switches.register('Input', '-i,-f,-file','file.txt')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__] = {
	'file': 'pinterestCachePages.py',
	'description': 'Cache page specified in a pin',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['prerequisite'].append('** this app never worked **')

_.appInfo[__name__]['examples'].append('p pinterestCachePages')

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
	# _.appData[__name__]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__name__]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__name__]['pipe'].append(pd)




# pipeData = ''
# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


# _.appData[__name__]['pipe'] = ''
# if not sys.stdin.isatty():
#     _.appData[__name__]['pipe'] = []
#     for pd in sys.stdin.readlines():
#         pd = pd.replace('\n','')
#         if not pd == '':
#             _.appData[__name__]['pipe'].append(pd)
#     try:
#         if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
#             _.appData[__name__]['pipe'][0] = _.appData[__name__]['pipe'][0][1:]
#     except Exception as e:
#         pass
# _.appData[thisApp.focus()]['pipe'] = list(data)















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
# def codeTest(pinID,dataIn,whichTest):
#     dataPath = 'D:\\Pinterest_Cache\\Pinterest_Page_Cache_ID-THEID.html'
#     cachePath = dataPath.replace('THEID',pinID)
#     # _.saveText([str(dataIn)],dataPath.replace('THEID',pinID))
#     try:
#         test = True
#         _.saveText([str(dataIn)],cachePath)
#     except Exception as e:
#         test = False
#     if test:
#         # pause = input(whichTest + ' ' + str(test) + '? ')
#         print(whichTest)
#         time.sleep(5)

def cachePage(pinID,url):
	# dataPath = 'D:\\Pinterest_Cache\\Pinterest_Page_Cache_ID-THEID.json'
	dataPath = 'D:\\Pinterest_Cache\\Pinterest_Page_Cache_ID-THEID.html'
	cachePath = dataPath.replace('THEID',pinID)
	if not os.path.isfile(cachePath):
		try:
			page = requests.get(url, timeout=10)
			code = page.content.decode("utf-8")
			_.saveText([str(code)],cachePath)
		except Exception as e:
			pass





def action():
	os.system('cls')

	# print('this app never worked')
	# sys.exit()
	pinData = _.getTable('pinterestData.json')
	for i,pd in enumerate(pinData):
		# if i == 5:
		# if '461548661794872237' in pd['pinID']:
		if True:
			try:
				if 'http' in pd['link']:
					# print(pd['link'])
					cachePage(pd['pinID'],pd['link'])
					print(pd['pinID'])
			except Exception as e:
				pass



# pinterestCachePages
########################################################################################
if __name__ == '__main__':
	action()