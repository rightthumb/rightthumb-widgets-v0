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
import sys
import time
# import simplejson as json
# from threading import Timer

import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
from datetime import datetime as dt, timedelta
import datetime
from datetime import date
from dateutil import rrule

import time

from pathlib import Path
import sqlite3

##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'threadBase.py',
	'description': 'Changes the world',
	'categories': [
						'research',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}
	
_.appInfo[focus()]['examples'].append('p threadBase -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	pipeCleaner()



# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + _v.slash+'bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START


def getFileInfo6( path, sql=True, qID=False ):
	__.queueLastActivity = time.time()

	obj = _dir.fileInfo( path, sql )

	if not type(obj) == bool:

		__.projectData[focus()]['folder'][   __.pdID[focus()]['folder']  ]['data'].append( obj )
		# __.projectData[focus()][__.pdID[focus()]].append( obj )
	
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( obj) )


def getFileInfo7( path, sql=True, qID=False ):
	__.queueLastActivity = time.time()

	obj = _dir.fileInfo( path, sql )
	if not type(obj) == bool:
		obj1 = _dir.fileInfo( path )

		if obj1['ext'].lower() == 'exe':
			__.projectData[focus()]['exe'][   __.pdID[focus()]['exe']  ]['data'].append( obj )
		else:
			__.projectData[focus()]['folder'][   __.pdID[focus()]['folder']  ]['data'].append( obj )



		# __.projectData[focus()][__.pdID[focus()]].append( obj )
	
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( obj) )





def processFolder(folder, qID):
	__.queueLastActivity = time.time()
	__.threadActivity[qID]['activity'] = time.time()
	try:
		dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			item = item.replace('\n','')

			if os.path.isdir(path):
				_.threads.add( 'folder', processFolder, [ path ], pID=qID )

			if os.path.isfile( path ):
				try:
					getFileInfo6( path, True )
				except Exception as e:
					__.threadActivity[qID]['error'] = True
					__.threadActivity[qID]['log'].append({'folder': folder})
				# getFileInfo6( path, True )
				# getFileInfo7( path )
	except Exception as e:
		__.threadActivity[qID]['error'] = True
		__.threadActivity[qID]['log'].append({'folder': folder})

	_.threads.spent( qID, sys.getsizeof( 'obj') )
	__.queueLastActivity = time.time()
	__.threadActivity[qID]['activity'] = time.time()


		


	# data=[]
	# data.append({'name': 'Scott'})
	# theID = _.threads.spent( qID, sys.getsizeof( 'obj') )    
	# _.threads.listen( theID, test )
	# _.threads.spent( qID, sys.getsizeof( 'obj'), trigger=test )
	# _.threads.spent( qID, sys.getsizeof( 'obj'), trigger=test, data=data )
	# _.threads.spent( qID, sys.getsizeof( 'obj'), trigger=test,  triggerArg=['hello'] )
	# _.threads.spent( qID, sys.getsizeof( 'obj'), trigger=test, triggerArg=[{'name': 'Scott'}], kwargs=True )
	# _.threads.spent( qID, sys.getsizeof( 'obj'), trigger=test, data=data, triggerArg=[{'name': 'Scott'}], kwargs=True )



def test(data=False,name=False):
	_.pr(data)
	_.pr(name)



# def action5():
def action():
	# _.pr( __.structure() )
	# sys.exit()
	db = 'Apps_Folder.db'
	_dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
	_.threads.add( 'folder', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False, database=db ) # kwargs 
	_.threads.maxThreads = 350
	_.threads.maxThreadsSafe = 350
	_.threads.report = True
	_.threads.autoLoaded = True
	_.threads.autoLoadedAfter = 2
	_.threads.auditPrint = True
	_.threads.scheduleLoop = .01
	_.threads.auditLoop = .5
	folder = os.getcwd()
	_.threads.add( 'folder', processFolder, [ folder ] )



def action4():
# def action():
	
	db = 'Apps_Folder_exe.db'
	_dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
	_.threads.add( 'exe', loaded=False, database=db ) # kwargs 
	# _.threads.maxThreadsSafe = 250
	_.threads.report = True
	_.threads.autoLoaded = True
	_.threads.autoLoadedAfter = 2
	_.threads.auditPrint = True


	db = 'Apps_Folder.db'
	_dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
	_.threads.add( 'folder', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False, database=db ) # kwargs 
	_.threads.maxThreads = 350
	_.threads.maxThreadsSafe = 350
	_.threads.report = True
	_.threads.autoLoaded = True
	_.threads.autoLoadedAfter = 2
	_.threads.auditPrint = True


	folder = os.getcwd()
	# _.threads.add( 'folder', processFolder, [{'folder':folder}], kwargs=True )
	_.threads.add( 'folder', processFolder, [ folder ] )




def action3():

	folder = os.getcwd()
	dirList = os.listdir(folder)

	if not type(_.appData[__.appReg]['pipe']) == str:
		dirList = _.appData[__.appReg]['pipe']
		_.pr('pipe')
	else:
		_.pr('no pipe')
	
	# _.threads.add( 'test', trigger=complete, triggerArg=({'two', 'hi'}), loaded=False )
	# _.threads.add( 'test', trigger=complete, triggerArg=(('one'),('two')), loaded=False )
	# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
	# _.threads.add( 'test', trigger=complete, triggerArg=[{'one': 'hello', 'two': 'hi'}], loaded=False ) # sends as a dictionary
	_.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
	# _.threads.maxThreads = 100
	_.threads.maxThreadsSafe = 250
	_.threads.report = True
	_.threads.projectDataMaxLen = 2000
	# _.threads.maxThreadsAuto = True

	i = 0
	for item in dirList:
		item = item.replace('\n','')
		path = folder + _v.slash + item
		if os.path.isfile(item):
			i+=1
			_.threads.add( 'test', getFileInfo6, [item,False] ) # this spends the threads

			# _.pr(item)
			# _.threads.add( 'test', testThis, [item] ) # this spends the threads
			# _.threads.add( 'test', testFunction, [item] ,loaded=False )
			# _.threads.add( 'test', testFunction, [[item]], addID=False ,loaded=False )
			# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )

	_.threads.loaded()



	_.pr('size',i)






def action2():
# def action():
	global cursor
	global conn
	

	if not type(_.appData[__.appReg]['pipe']) == str:
		dirList = _.appData[__.appReg]['pipe']
		_.pr('pipe')
	else:
		_.pr('no pipe')
	
	db = 'Apps_Folder.db'

	_dir.sqlCreateTable( db, deleteDBFirst=True, close=True )

	_.threads.add( 'folder', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
	# _.threads.maxThreads = 100
	_.threads.maxThreadsSafe = 250
	_.threads.report = True
	# _.threads.maxThreadsAuto = True
	_.threads.autoLoaded = True
	_.threads.autoLoadedAfter = 2
	_.threads.auditPrint = True
	_.threads.projectDataFileSQL = db
	folder = os.getcwd()
	# _.threads.add( 'folder', processFolder, [{'folder':folder}], kwargs=True )
	_.threads.add( 'folder', processFolder, [ folder ] )













def action1():
	global cursor
	global conn
	folder = os.getcwd()
	_.pr(folder)
	dirList = os.listdir(folder)

	if not type(_.appData[__.appReg]['pipe']) == str:
		dirList = _.appData[__.appReg]['pipe']
		_.pr('pipe')
	else:
		_.pr('no pipe')
	
	databaseFile = 'Apps_Folder.db'

	try:
		os.unlink(databaseFile)
	except Exception as e:
		pass
	conn = sqlite3.connect(databaseFile)
	cursor = conn.cursor()         
	cursor.execute("""CREATE TABLE files (path text, name_ text, name text, folder text, stat text, attrib text, bytes int, size text, date_created_raw int, date_modified_raw int, date_created text, date_modified text, type text, typesort text, ext text, week_of_year text, week_of_year_ text, day_of_the_week text, month text, friendly_week text, friendly_month text)""")


	_.threads.add( 'folder', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
	# _.threads.maxThreads = 100
	_.threads.maxThreadsSafe = 250
	_.threads.report = True
	_.threads.maxThreadsAuto = True
	_.threads.autoLoaded = True
	_.threads.autoLoadedAfter = 2
	# _.pr(dirList)
	for item in dirList:
		item = item.replace('\n','')
		# path = os.path.abspath(item)
		if os.path.isdir(item):
			# if folder in path:
			_.threads.add( 'folder', processFolder, [ item ] )
		if os.path.isfile( item ):
			# if folder in path:
			getFileInfo6( item )
			pass















def action0():

	folder = os.getcwd()
	dirList = os.listdir(folder)

	if not type(_.appData[__.appReg]['pipe']) == str:
		dirList = _.appData[__.appReg]['pipe']
		_.pr('pipe')
	else:
		_.pr('no pipe')
	
	# _.threads.add( 'test', trigger=complete, triggerArg=({'two', 'hi'}), loaded=False )
	# _.threads.add( 'test', trigger=complete, triggerArg=(('one'),('two')), loaded=False )
	# _.threads.add( 'test', trigger=complete, triggerArg=[{'one': 'hello', 'two': 'hi'}], loaded=False ) # sends as a dictionary
	# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
	_.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
	_.threads.maxThreadsSafe = 250
	_.threads.report = True
	_.threads.maxThreadsAuto = True

	i = 0
	for item in dirList:
		item = item.replace('\n','')
		path = folder + _v.slash + item
		if os.path.isfile(item):
			i+=1
			# _.pr(item)
			# _.threads.add( 'test', testThis, [item] ) # this spends the threads
			_.threads.add( 'test', getFileInfo6, [item,False] ) # this spends the threads
			# _.threads.add( 'test', testFunction, [item] ,loaded=False )
			# _.threads.add( 'test', testFunction, [[item]], addID=False ,loaded=False )
			# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )

	_.threads.loaded()



	_.pr('size',i)

def testThis(*args):
	_.pr(args)
	# _.pr()
	# _.pr(args[len(args)-1])
	_.threads.spent( args[len(args)-1], sys.getsizeof( 'obj') )
	# _.threads.spent( 1, sys.getsizeof( 'obj') )

def testFunctionKwargsHack(data,qID):
	_.pr(data,qID)
	data['qID']=qID
	testFunction(**data)


def testFunction( one=False, two=False, qID=False):
	_.pr(one,two,qID)
	
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof(obj) )


def complete(one=False,two=False):

	_.pr()
	_.pr()
	_.pr()
	_.pr('_______________________________')
	_.pr('Done')
	_.pr()
	_.pr()
	_.pr()
	global data
	try:
		data[0]
	except Exception as e:
		data = []
	# # for d in data:
	#     # _.pr(d)
	# _.pr('data:',len(data))
	# _.pr()
	# try:
	#     _.pr(one,two)
	# except Exception as e:
	#     try:
	#         _.pr('kwargs:',kwargs)
	#     except Exception as e:
	#         _.pr('Error: arg')


	# _.saveTable(data,'Apps.dirCache.json')
	# _.saveLog('queue')
	# for d in data:
	#     _.pr(d)


	# _.saveLog('queue')
	# _.saveLog('audit')



########################################################################################
if __name__ == '__main__':
	action()






