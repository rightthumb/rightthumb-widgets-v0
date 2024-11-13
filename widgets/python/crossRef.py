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
	_.switches.register('Input', '-i,-f,-file','one.csv two.csv')
	_.switches.register('FileOne', '-1,-one','%tmpf1%')
	_.switches.register('FileTwo', '-2,-two','%tmpf2%')
	_.switches.register('NoCount', '-nocount')
	_.switches.register('Report', '-report','1')
	_.switches.register('NoCount', '--c')



_.appInfo[focus()] = {
	'file': 'crossRef.py',
	'description': 'Cross reference 2 lists',
	'categories': [
						'lists',
						'data',
						'research',
						'xref',
						'cross reference',
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

_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2%')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -nocount')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -nocount -report 1')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -report 2')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -report')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -nocount --c')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p crossRef -1 %tmpf1% -2 %tmpf2% -nocount --c -report 1')

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

def action():
	if _.switches.isActive('Input'):
		one = _.switches.value('Input').split(',')[0]
		two = _.switches.value('Input').split(',')[1]
	elif _.switches.isActive('FileOne') and _.switches.isActive('FileTwo'):
		one = _.switches.value('FileOne')
		two = _.switches.value('FileTwo')
	else:
		_.pr('Error 0')
		sys.exit()
	try:
		fileOne = _.getText( one )
		fileTwo = _.getText( two )
	except Exception as e:
		_.pr('Error 1')
		sys.exit()

	listOne = []
	listTwo = []
	rawOne = []
	rawTwo = []

	for row in fileOne:
		row = row.replace( '\n', '' )
		if len( row ) > 1 and not row in rawOne:
			listOne.append( { 'row': row, 'found': False } )
			rawOne.append( row )

	for row in fileTwo:
		row = row.replace( '\n', '' )
		if len( row ) > 1 and not row in rawTwo:
			listTwo.append( { 'row': row, 'found': False } )
			rawTwo.append( row )

	for r1i, row1 in enumerate(listOne):
		found = False
		for r2i, row2 in enumerate(listTwo):
			if row1['row'] == row2['row']:
				found = True
				listTwo[r2i]['found'] = True
		listOne[r1i]['found'] = found

	fileOneFalseCount = 0
	fileOneTrueCount = 0
	fileOneFalseList = []
	for i, row in enumerate(listOne):
		if not row['found']:
			fileOneFalseCount += 1
			fileOneFalseList.append( row['row'] )
		else:
			fileOneTrueCount += 1
	fileTwoFalseCount = 0
	fileTwoTrueCount = 0
	fileTwoFalseList = []
	for i, row in enumerate(listTwo):
		if not row['found']:
			fileTwoFalseCount += 1
			fileTwoFalseList.append( row['row'] )
		else:
			fileTwoTrueCount += 1


	if not fileOneFalseCount and not fileTwoFalseCount:
		_.pr( 'Lists are a match' )
	else:
		if not fileOneFalseCount:
			_.pr( 'All items in one are in two' )
		else:
			if not _.switches.isActive('Report') or '1' in _.switches.value('Report') or 'one' in _.switches.value('Report').lower():
				if not _.switches.isActive('Report'):
					_.pr( 'Items in list 1 that are missing in list 2:' )
					_.pr()
				for i, row in enumerate(fileOneFalseList):
					if _.switches.isActive('NoCount'):
						_.pr( row )
					else:
						_.pr( i+1, row )
				if not _.switches.isActive('Report'):
					_.pr()
					_.pr()
					_.pr()
		if not fileTwoFalseCount:
			_.pr( 'All items in two are in one' )
		else:
			if not _.switches.isActive('Report') or '2' in _.switches.value('Report') or 'two' in _.switches.value('Report').lower():
				if not _.switches.isActive('Report'):
					_.pr( 'Items in list 2 that are missing in list 1:' )
					_.pr()
				for i, row in enumerate(fileTwoFalseList):
					if _.switches.isActive('NoCount'):
						_.pr( row )
					else:
						_.pr( i+1, row )
		if not _.switches.isActive('NoCount'):
			_.pr()
			_.pr( 'One:' )
			_.pr( '\tTotal:\t', fileOneTrueCount+fileOneFalseCount )
			# _.pr( '\tTrue:\t', fileOneTrueCount )
			_.pr( '\tFalse:\t', fileOneFalseCount )
			_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileOneTrueCount+fileOneFalseCount, fileOneTrueCount))+'%' )
			_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileOneTrueCount+fileOneFalseCount, fileOneFalseCount))+'%' )
			_.pr()
			_.pr( 'Two:' )
			_.pr( '\tTotal:\t', fileTwoTrueCount+fileTwoFalseCount )
			# _.pr( '\tTrue:\t', fileTwoTrueCount )
			_.pr( '\tFalse:\t', fileTwoFalseCount )
			_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount, fileTwoTrueCount))+'%' )
			_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount, fileTwoFalseCount))+'%' )

			_.pr()
			_.pr( 'Totals:' )
			_.pr( '\tRows:\t', fileTwoTrueCount+fileTwoFalseCount+fileOneTrueCount+fileOneFalseCount )
			_.pr()
			_.pr( '\tUnique:\t', fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount )
			_.pr( '\tTrue:\t', fileOneTrueCount )
			_.pr( '\tFalse:\t', fileTwoFalseCount+fileOneFalseCount )
			_.pr( '\t% T:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount, fileTwoTrueCount))+'%' )
			_.pr( '\t% F:\t', str(_.percentageDiffIntAuto( fileTwoTrueCount+fileTwoFalseCount+fileOneFalseCount, fileTwoFalseCount+fileOneFalseCount))+'%' )
# crossRef
########################################################################################
if __name__ == '__main__':
	action()






