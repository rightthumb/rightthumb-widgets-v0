#!/usr/bin/python3
# import os
import sys
import time
# import simplejson as json
# from threading import Timer


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
	'file': 'diff.py',
	'description': 'Percentage difference between 2 numbers',
	'categories': [
						'quick',
						'percent',
						'difference',
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

_.appInfo[focus()]['examples'].append('p diff -i 45 60')

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



########################################################################



def getFileInfo5( path ):
	__.queueLastActivity = time.time()
	global data

	try:
		data[0]
	except Exception as e:
		data = []

	obj = _dir.fileInfo( path )

	if not type(obj) == bool:
		data.append( obj )
	

def processFolder(dirList, qID):
	__.queueLastActivity = time.time()
	global data

	for item in dirList:
		item = item.replace('\n','')
		path = os.path.abspath(item)
		if os.path.isdir(item):
			_.threads.add( 'process_folder', processFolder, [ path ] )
		if os.path.isfile( path ):
			getFileInfo5( path )
	
	_.threads.spent( qID, sys.getsizeof( 'obj') )

########################

	# _.threads.add( 'process_folder', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
	# # _.threads.maxThreads = 100
	# _.threads.maxThreadsSafe = 600
	# _.threads.report = True
	# _.threads.maxThreadsAuto = True
	# _.threads.autoLoaded = True
	# _.threads.autoLoadedAfter = 30







# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );





	# _.saveLog('queue')
	# _.saveLog('audit')

########################################################################







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

# books = _.getText(_v.myTables + '\\bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START
def percentageDiffInt(smaller, bigger):
	result = round(( (smaller) / (bigger) )*100,2)
	if result == int(result):
		result = int(result)
	return result

def percentageInt(percent, whole):
	result = round(( (percent) * (whole) ) / 100.0,2)
	if result == int(result):
		result = int(result)
	return result

def action():
	if not _.switches.isActive('Input'):
		print()
		_.colorThis(  [ 'Error' ], 'red'  )
		_.colorThis(  [ '\t', 'p diff -i 45 60' ], 'yellow'  )
	if _.switches.isActive('Input'):
		nv = _.switches.value('Input').split(',')

		try:
			pass
			nv[0] = int(nv[0])
			nv[1] = int(nv[1])

				
			if nv[0] < nv[1]:
				n0 = nv[0]
				n1 = nv[1]
			else:
				n0 = nv[1]
				n1 = nv[0]


			print()
			print( 'difference' )
			print()
			print( '\t  ', str(_.pDiff(n0, n1, 'l')) + ' %' )
			print( '\t  ', str(_.pDiff(n0,n1, 'g')) + ' %' )
			print()
			_.colorThis( [ '', n1-n0 ], 'yellow' )
			print()
			
			
		except Exception as e:
			print()
			_.colorThis(  [ 'Error' ], 'red'  )
			_.colorThis(  [ '\t', 'p diff -i 45 60' ], 'yellow'  )




########################################################################################
if __name__ == '__main__':
	action()


