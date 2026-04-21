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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('First', '-first','20')
	_.switches.register('Last', '-last','20')
	_.switches.register('Label', '-label','20')

	



_.appInfo[focus()] = {
	'file': 'logView.py',
	'description': 'View log files',
	'categories': [
						'management',
						'maintanance',
						'log',
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

_.appInfo[focus()]['prerequisite'].append('p logConfig -i indexTable_drives-{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}.json -l drive log')


_.appInfo[focus()]['examples'].append('p logView -i indexTable_drives-{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}.json')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p logView -label txtScheduler -long -last 20')
_.appInfo[focus()]['examples'].append('p logView -label txtS -long -first 20')

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
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )

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
# os.system('"' + do + '"')

########################################################################################
# START

def getLogText( data ):
	global record
	for attribute in record['data']['logfields']['attribute']:
		if attribute['id'] == data:
			# _.pr(attribute['text'])
			return attribute['text']

def getDelete( data ):
	global record
	for attribute in record['data']['logfields']['attribute']:
		if attribute['id'] == data:
			return attribute['delete']

def process( data ):
	global groups
	global fields
	for d in data:
		if not getDelete( d['id'] ):
			fields.append( getLogText( d['id'] ) )

		try:
			d['children']
			groups.append( getLogText( d['id'] ) )
			process( d['children'] )
		except Exception as e:
			pass

def flatten( data ):
	result = ''
	for d in data:
		result += d + ','
	result = _str.replaceDuplicate( result, ',' )
	result = _str.cleanBE( result, ',' )
	return result

def flattenSort():
	global record
	result = ''
	ids = []
	for attribute in record['data']['sortby']['attribute']:
		if not attribute['id'] in ids:
			ids.append( attribute['id'] )
			if not attribute['delete']:
				if attribute['direction'] == 'desc':
					result += 'd.' + attribute['text'] + ','
				else:
					result += attribute['text'] + ','
	result = _str.replaceDuplicate( result, ',' )
	result = _str.cleanBE( result, ',' )
	return result



def action():
	global groups
	global record
	global fields
	theLog = _.getTable('logConfig.json')

	shouldRun = False
	record = False

	if _.switches.isActive('Label'):
		for row in theLog:
			if _.switches.value('Label').lower() in row['label'].lower():
				record = row


	if _.switches.isActive('Input'):
		for row in theLog:
			if _.switches.value('Input').lower() == row['file'].lower():
				record = row




	if type( record ) == bool:
		_.pr()
		_.pr('log not configured')
		_.pr()
		_.pr(' Run:')
		_.pr( '\tp logConfig -i', _.switches.value('Input') )
		sys.exit()
	else:
		shouldRun = True


		# delete
		# id
		# text

		# _.pr( record['data']['logfields']['attribute'] )
	if shouldRun:
		# _.printVar(record)
		# sys.exit()
		process( record['data']['logfields']['dataTable'] )
		# _.pr( 'groups:', flatten( groups ) )
		# _.pr( 'fields:', flatten( fields ) )
		# _.pr( 'flattenSort:', flattenSort() )

		if len( groups ) > 0:
			_.switches.fieldSet( 'GroupBy','active', True )
			_.switches.fieldSet( 'GroupBy','value', flatten( groups ) )

		log = _.getTable( record['file'] )
		if len(log) == 0:
			log = _.getTable2( record['path'] )

		if len( record['data']['sortby']['attribute'] ):
			log = _.tables.returnSorted( 'log', flattenSort(), log )


		if _.switches.isActive( 'First' ):
			get = int( _.switches.value( 'First' ) )
			newLog = []
			for i,row in enumerate(log):
				if (i+1) <= get:
					newLog.append( row )
			log = newLog


		if _.switches.isActive( 'Last' ):
			get = int( _.switches.value( 'Last' ) )
			newLog = []
			log.reverse()
			for i,row in enumerate(log):
				if (i+1) <= get:
					newLog.append( row )
			log = newLog
			log.reverse()


		_.pr()
		_.tables.register('logs',log)
		for row in record['data']['logfields']['attribute']:
			try:
				trigger = row['trigger']
			except Exception as e:
				trigger = False
			if not type(trigger) == bool:
				# if trigger == 'epoch':
					# _.pr( trigger, row['text'],flatten( fields ) )
				_.tables.fieldProfileSet( 'logs', row['text'], 'trigger', eval(trigger) )
		# sys.exit()
		# _.tables.fieldProfileSet('logs','timestamp','trigger',_.float2Date)
		# _.tables.fieldProfileSet( 'logs', 'timestamp', 'trigger', _.float2Date )
		_.tables.print('logs', flatten( fields ) )

groups = []
fields = []

# logView
########################################################################################
if __name__ == '__main__':
	action()