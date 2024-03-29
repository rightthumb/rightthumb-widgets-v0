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

##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
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

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################
from shutil import copyfile
##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Before', '-b,-before')
	_.switches.register('After', '-a,-after')
	_.switches.register('Insert', '-insert')
	_.switches.register('InsertFile', '-insertfile')

	


_.appInfo[focus()] = {
	'file': 'insertText.py',
	'description': 'Insert text into a file or set of files',
	'categories': [
						'file manipulation',
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

# epy replaceText
# epy insertText
# epy changeTextEnd
# epy moveText
# epy replaceFunction



_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p replaceText ?')
_.appInfo[focus()]['relatedapps'].append('p insertText ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p changeTextEnd ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p moveText ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p replaceFunction ?')


_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p insertText -i base + pyperclip -insert test -after')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p insertText -i %tmpf1% + xxx -insert yyy -before')
_.appInfo[focus()]['examples'].append('p insertText -i %tmpf1% + xxx -a - xxxy -insertfile %tmpf9%')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p insertText -i D:\\tech\\programs\\python\\src\\windows\\_rightThumb\\_auditCodeBase\\config.py -insert "\'rules\': []," + "\'nest\'" -before')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p insertText -i auditCodeBase.json -insert ";\'rules;\': []," + ";\'nest;\'" -before')
_.appInfo[focus()]['examples'].append('p insertText -i auditCodeBase.json -insert ";\'escape;\': []," + ";\'set;\'" -after')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()

	_.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

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



########################################################################################
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
# _.switches.fieldSet( 'Input', 'active', True )
# _.switches.fieldSet( 'Input', 'value', 'one' )
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
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:
# os.system('"' + do + '"')

########################################################################################
# NEW database stuff

# def testTrigger( data ):
#     return data * 5

# def dateScramble( data ):
#     d = _.date2epoch( data )
#     if len( str(data) ) > 0:
#         _.pr( data, d )
#     return _.resolveEpochTest( d, falseBlank=True )

	# data = [
	#             {
	#                         'first': 'Scott',
	#                         'last': 'Reph',
	#                         'test': 3,
	#             },
	#             {
	#                         'first': 'Alpha',
	#                         'last': 'Reph',
	#                         'test': 7,
	#             },
	# ]
	# fieldConfig = [{
	#             'table': 'test_table',
	#             'name': 'test',
	#             'trigger': testTrigger,
	#     },{
	#             'table': 'test_table',
	#             'name': 'date_modified',
	#             'trigger': dateScramble,
	#     }]

	# testSet = 0
	# if testSet == 1:
	#     __.databases.register(
	#                             name='test',
	#                             table='test_table',
	#                             file='__first_test.db',
	#                             records=data,
	#                             delete=True,
	#                             fields=fieldConfig,
	#                             # printFileActivity=True,
	#     )
	# elif testSet == 0:
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test.db',
	#     )
	# elif testSet == 2:
	#     testSet = 1
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test____X.db',
	#                             fields=fieldConfig,
	#     )
	# elif testSet == 3:
	#     testSet = 1
	#     __.databases.register(
	#                             name='test',
	#                             file='__first_test____X.db',
	#                             delete=True,
	#     )



	# if testSet == 1:
	#     records = []

	#     records.append({
	#                                     'first': 'Jessica',
	#                                     'last': 'Reph',
	#                                     'test': 55,
	#     })

	#     records.append({
	#                                     'first': 'Nana',
	#                                     'last': 'Reph',
	#                                     'test': 100,
	#     })

	#     __.databases.insertRecords( name='test', table='test_table', records=records )


	#     __.databases.update(
	#                             name='test',
	#                             info={
	#                                     'table': 'test_table',
	#                                     'record': {
	#                                                     'first': 'Sam',
	#                                                     'last': 'Test',
	#                                                     'test': 99,
	#                                     },
	#                                     'update': 'id=1',
	#                             }
	#     )



	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'custom': 'select * from test_table',
	#                                 'force': True,
	#                         }
	# )

	###################
	# __.databases.trigger(
	#                         name='test',
	#                         table='test_table',
	#                         field='test',
	#                         trigger=testTrigger,
	# )

	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'type': 'text',
	#                                 'field': 'first',
	#                                 'search': 'Scott',
	#                                 'custom': False,
	#                                 'force': False,

	#                         }
	# )

	# results = __.databases.search(
	#                         name='test',
	#                         info={
	#                                 'table': 'test_table',
	#                                 'custom': 'test<10 and test>5',
	#                                 'force': False,
	#                         }
	# )
	###################

	# try:
	#     _.pr()

	#     fieldList = ','.join(__.databases.getFields( 'test', 'test_table', exclude='' ))
	#     _.tables.register('results_table',results)
	#     _.tables.print('results_table',fieldList)
	# except Exception as e:
	#     pass


########################################################################################
# START

fileBackup = _.regImp( __.appReg, 'fileBackup' )

# fileBackup.switch( 'Silent' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )

insertText = ''
def action():
	global insertText

	# _.pr( _.switches.value('Input') )

	if _.switches.isActive('InsertFile'):
		if not os.path.isfile( _.switches.value('InsertFile') ):
			_.pr( 'Error: InsertFile' )
			sys.exit()
		else:
			insertText = _.getText( _.switches.value('InsertFile'), True )
			insertText = insertText.replace( '\n', '' )

	if _.switches.isActive('Insert'):
		
		insertText = _.ci(_.switches.value('Insert'))
		insertText = _str.cleanBE( insertText, ' ' )

	if len(_.switches.value('Plus'))<3:
		_.pr( 'Error: Plus' )
		sys.exit()

	if not type( _.appData[__.appReg]['pipe'] ) == bool or _.switches.isActive('Input') and os.path.isfile( _.switches.value('Input') ):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			_.appData[__.appReg]['pipe'].append( _.switches.value('Input') )
		
		files = _.appData[__.appReg]['pipe']
		for filename in files:
			if os.path.isfile( filename ):
				processFile(filename)



def getTabs( line ):
	pre = ''
	for ch in str(line):
		if ch == ' ' or ch == '\t':
			pre += ch
		else:
			return pre
	return pre

def processFile( filename ):
	global insertText

	_.pr()
	_.pr('processing:', filename)
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre insertText' )
	recoveryFile = fileBackup.do( 'action' )

	file = _.getText( filename )

	newFile = []
	rows = []
	for i,line in enumerate(file):
		line = line.replace( '\n', '' )
		found = False
		if _.showLine(line):
			found = True

			if _.switches.isActive('Before'):
				newFile.append( str(getTabs(line)) + str(insertText) )
				newFile.append( line )
			if _.switches.isActive('After'):
				newFile.append( line )
				newFile.append( str(getTabs(line)) + str(insertText) )

		if not found:
			newFile.append( line )

	_.saveText( newFile, filename )

	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'insertText' )
	recoveryFile = fileBackup.do( 'action' )


	if _.switches.isActive('Input'):

		keep=input('Keep changes? ')
		if 'n' in keep.lower():
			try:
				copyfile(recoveryFile, filename)
				_.pr( 'Undo successful' )
			except Exception as e:
				_.pr( 'Undo fail' )



########################################################################################
if __name__ == '__main__':
	action()







