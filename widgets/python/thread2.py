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
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'thread2.py',
	'description': 'Changes the world',
	'categories': [
						'research',
						'text manipulation',
				],
	'instance': '',
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

_.appInfo[focus()]['examples'].append('p thread2 -file file.txt')

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
from threading import Timer
def threadAdd(duplicate,time,func,arg):
	thread = Timer(int(time), func, arg)
	thread.start()

def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate

def getFileInfo(path):
	# global data
	# 
	# __.queue[path]
	modified = formatDate(os.path.getctime(os.path.abspath(path)))
	created = formatDate(os.path.getmtime(os.path.abspath(path)))
	# data.append({ 'path': path, 'modified': modified, 'created': created })
	_.pr( created, modified, path)

def test(data):
	_.pr(type(data),str(data))

def test2(data,two):
	_.pr(type(data),str(data))
	_.pr(type(two),str(two))

def test3(*args):
	for i,a in enumerate(args):
		_.pr(i,a)
	_.pr()

def getFileInfo4( path, qID=0 ):
	_.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );
	# _.pr(path)
	global data
	try:
		data[0]
	except Exception as e:
		data = []


	aPath = os.path.abspath(path)
	name = Path(path).name
	_.appData[focus()]['audit'].append( { 'start': True, 'note': 'getctime, getmtime', 'entire': False, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );
	createdRaw = os.path.getctime(aPath)
	modifiedRaw = os.path.getmtime(aPath)
	_.appData[focus()]['audit'].append( { 'start': False, 'note': 'getctime, getmtime', 'entire': False, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );
	obj = {
				'file': name,
				'path': aPath,
				'createdRaw': createdRaw,
				'modifiedRaw': modifiedRaw,
				'created': formatDate(createdRaw),
				'modified': formatDate(modifiedRaw),
	}

	data.append(obj)
	queueClose( qID, sys.getsizeof(obj) )
	_.appData[focus()]['audit'].append( { 'start': False, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );


def threadAdd2( qID, func, arg, isLoop=False ):
	__.queueID += 1
	argN = arg
	queueCount = __.queueCount

	# if __.queueCount < __.queueMax:
	waitFor = .0001
	queueOpen( qID, func, arg, waitFor, queueCount)
	argN.append(qID)
	thread = Timer(waitFor, func, argN)
	thread.start()

def queueOpen( qID, func, arg, waitFor, queueCount ):
	__.queue.append( { 'id': qID, 'func': func.__name__, 'arg': arg, 'start': time.time(), 'end': 0, 'runtime': 0, 'mem': 0, 'wait': waitFor, 'qcount': queueCount } )

def queueClose( qID, mem=0 ):
	pass

def queueMonitor():
	__.queueMonitorCount += 1
	# _.pr('queueMonitor')
	total = 0
	q = __.queue
	if len(q) > 0:
		for i,qu in enumerate(q):
			if qu['end'] == 0:
				total += 1
		__.queueCount =  total
	if not __.queueLoaded or not __.queueLoaded:
		thread = Timer(.0001, queueMonitor)
		thread.start()
	else:
		if len(q) == 0:
			thread = Timer(.0001, queueMonitor)
			thread.start()
		elif total > 0:
			thread = Timer(.0001, queueMonitor)
			thread.start()

		else:
			if not type(__.queueCompleteFunc) == str:
				_.pr('qm',__.queueMonitorCount)
				Timer(.01, __.queueCompleteFunc).start()



def action():
	_.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	_.appInfo[focus()]['instance'] = _.genUUID()
	queueMonitor()
	__.queueCompleteFunc = complete
	folder = os.getcwd()
	dirList = os.listdir(folder)

	if not type(_.appData[__.appReg]['pipe']) == str:
		dirList = _.appData[__.appReg]['pipe']
		_.pr('pipe')
	else:
		_.pr('no pipe')
	i = 0
	for item in dirList:
		item = item.replace('\n','')
		path = folder + _v.slash + item
		if os.path.isfile(item) == True:
			# _.pr(item)
			# threadAdd(False,1.0, test, ({'name': item}))    # fail
			# threadAdd(False,1.0, test, (('test')))        # fail
			# threadAdd(False,1.0, test, ('test'))            # fail

			# threadAdd(False,1.0, test, ['test'])            # WORKS
			# threadAdd(False,1.0, test3, ('test','two'))    # WORKS
			# threadAdd(False,1.0, test, [{'name': item}])    # WORKS
			# threadAdd(False,1.0, test2, ['test','two'])    # WORKS
			# threadAdd(False,1.0, test3, ['test','two'])    # WORKS
			i+=1
			threadAdd2(__.queueID,getFileInfo4, [item])    # WORKS
	_.pr('size',i)
	__.queueLoaded = True

def complete():
	global data
	# for d in data:
		# _.pr(d)
	_.pr('data:',len(data))
	# _.saveTable(__.queue,                   'app_audit_log_'+str(time.time())+'__'+_.appInfo[focus()]['file']+'____'+_.appInfo[focus()]['instance']+'.json')
	# _.saveTable(,'app_audit_log_'+str(time.time())+'__'+_.appInfo[focus()]['file']+'__actions__'++'.json')
	_.saveLog('queue')
	_.saveLog('audit')



# _.appQueueDefault = {
#     'queueID': 1,
#     'queue': [],
#     'queueCount': 0,
#     'queueLoaded': False,
#     'queueCompleteFunc': '',
#     'queueMax': 20,
#     'queueMonitorCount': 0,
#     }

__.queueID = 1
__.queue = []
__.queueCount = 0
__.queueLoaded = False
__.queueCompleteFunc = ''
__.queueMax = 5
__.queueMonitorCount = 0




# _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );
########################################################################################
if __name__ == '__main__':
	action()






