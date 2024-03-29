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
import time
# import simplejson as json
from threading import Timer


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
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################

def appSwitches():
	_.switches.register('Project', '-p,-project')

	_.switches.register('Input', '-i,-cmd','dir /s/b /a:a')

	_.switches.register('Pipe', '-pipe')

	_.switches.register('Prefix', '-prefix')


	
def addSuffixToProject(text):
	if not type( text ) == str:
		_.pr('Project switch error')
		sys.exit()
	return text + '_executeEstimate'



_.appInfo[focus()] = {
	'file': 'executeEstimate.py',
	'description': 'Executes stuff and estemates percentage complete based on time',
	'categories': [
						'execute',
						'timer',
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

_.appInfo[focus()]['examples'].append('p executeEstimate ')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})




focus()


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
	_.switches.trigger( 'Project', addSuffixToProject )
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
		for pd in data:
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




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################

# def processFolder(folder, qID):
# __.queueLastActivity = time.time()
# __.projectData[focus()][__.pdID[focus()]].append( obj )
# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )
# _.threads.add( 'process_folder', processFolder, [ path ] )
# _.threads.spent( qID, sys.getsizeof( 'obj') )
					################
# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
# _.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
# _.threads.maxThreadsSafe = 250
# _.threads.report = True
# _.threads.projectDataFileSQL = db
# _.threads.auditPrint = False

##################

# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );

# _dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
# obj = _dir.fileInfo( path, sql=True )
# _.pr(   _dir.fileInfo( _.switches.value('Input') )['size']   )

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
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def execute():
	global done
	global projectTimer
	focus()
	executeThis = _.switches.value('Input')
	do = executeThis + '> ' + _v.tmpf
	os.system('"' + do + '"')
	done = True
	if _.switches.isActive('Pipe'):
		results = _.getText( _v.tmpf )
		for row in results:
			row = row.replace( '\n', '' )
			_.pr(row)

	projectTimer.imp.focus(focus())
	_.switches.fieldSet( 'Note', 'active', True )
	_.switches.fieldSet( 'Note', 'value', executeThis )


	_.switches.fieldSet( 'Start', 'active', False )
	_.switches.fieldSet( 'End', 'active', True )

	projectTimer.imp.action()
	focus()

def estimate():
	global startTime
	global done
	global estimatedTotal
	
	if done:
		_.pr( '                                                                       ', end='\r', flush=True )
		# if _.switches.isActive('Prefix'):
		#     _.pr( ' ' + _.switches.value('Prefix') + ':', '100%', end='\r', flush=True )
		# else:
		#     _.pr( ' ' + '100%', end='\r', flush=True )

	else:

		if estimatedTotal == 0:
			if _.switches.isActive('Prefix'):
				_.pr(' ' + _.switches.value('Prefix') )

		else:
			pDone = str(int(_.percentageDiffInt( time.time()-startTime , estimatedTotal )))
			if _.switches.isActive('Prefix'):
				_.pr(' ' + _.switches.value('Prefix') + ':', pDone + '%', end='\r', flush=True)
			else:
				_.pr(' ' + pDone + '%', end='\r', flush=True)
			Timer( .1, estimate ).start()

def action():
	global estimatedTotal
	global projectTimer

	if _.switches.isActive('Project') and _.switches.isActive('Input'):
		logFile = _.getTable('projectTimer.json')

		focus()
		project = _.switches.value('Project')
		executeThis = _.switches.value('Input')



		records = []
		for row in logFile:
			if row['project'] == project and row['note'] == executeThis:
				records.append( row['total'] )

		if len(records) > 0:
			estimatedTotal = sum( records ) / len( records )


		projectTimer = _.regImp( focus(), 'projectTimer' )

		projectTimer.imp.focus(focus())

		_.switches.fieldSet( 'Project', 'active', True )
		_.switches.fieldSet( 'Project', 'value', project )

		_.switches.fieldSet( 'Start', 'active', True )

		projectTimer.imp.action()
		focus()
		Timer( .1, estimate ).start()
		Timer( .1, execute ).start()







done = False
estimatedTotal = 0
startTime = time.time()
# executeEstimate
########################################################################################
if __name__ == '__main__':
	action()







