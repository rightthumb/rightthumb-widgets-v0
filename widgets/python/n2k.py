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
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
	# folderReport = _filePathPatterns.action()
# txtBackup = _.regImp( __.appReg, 'txtBackup' )
#     txtBackup.switch( 'Input', filename )
#     txtBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = txtBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3
import math

##################################################


def appSwitches():
	pass
	_.switches.register( 'Stats', '-stats' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'N2K.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Solves N2K math problems',
	'categories': [
						'beth',
						'edu',
						'education',
						'nephews',
				],
	'relatedapps': [
						'pp closestNumber',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p N2K',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],

	}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
				'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
				'table': {'sent': [], 'received': [] }, 
	},
	}

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
	_.defaultScriptTriggers()
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START


def upDown(myList, myNumber):
	if myNumber in myList:
		return myNumber
	# try:
	# except Exception as e:
	#     _.pr( myNumber )
	#     _.pr( myList )
	#     sys.exit()

	myList = list(myList)
	myList.append( myNumber )
	myList.sort()
	i = myList.index( myNumber )
	if i == 0:
		return myList[i]
	if i == len( myList )-1:
		return myList[i]
	x = myNumber - myList[i-1]
	y = myList[i+1] - myNumber
	if x > y:
		return myList[i+1]
	if x < y:
		return myList[i-1]
	result = []
	result.append( myList[i-1] )
	result.append( myList[i+1] )
	
	return result[0]
	# return _.shuffle( result )[0]
	

def testItem( num ):
	global numberList
	global powerTable
	n = upDown( numberList, num )
	# _.pr( 'testItem:', num, n )
	return n


def listOptions( num ):

	small = int(num*.25)
	large = int(num*.75)

	small = 1
	large = num

	x = small

	
	options = []
	while not x == large:
		ti = testItem( x )
		# _.pr( 'listOptions:', x, ti, num )
		if ti:
			if not ti in options:
				options.append( ti )
		# try:

		# except Exception as e:
		#     pass
		
		x+=1

	ti = testItem( num )
	if ti:
		if not ti in options:
			options.append( ti )


	newOptions = []
	for x in options:
		if x <= num:
			newOptions.append( x )

	# _.pr( 'options:', num, newOptions )

	return options

def test( num, total, path ):
	global numberList
	global powerTable
	# _.pr()


	if not total:
		return path

	lo = listOptions( total )
	newLo = []
	for x in lo:
		if x <= total:
			newLo.append( x )

	myLo = max(newLo)
	t = total-myLo
	# _.pr( '\n TEST:', num, total, newLo, myLo, t )
	path.append( myLo )

	if t < 1:
		return path
	else:
		return test( num, t, path )


def testOLD( num, total, path ):
	global numberList
	global powerTable
	# _.pr()



	lo = listOptions( total )
	isDone = False
	for x in lo:

		t = total-x
		if not t or t < 10:
			if t < 10:
				isDone = True
				path.append( t )
				t = total-t
				# _.pr( t, path )
				return path
			else:
				isDone = True
				path.append( x )
				# _.pr( t, path )
				return path

	nextFound = False
	loops = 0
	while not nextFound and loops < 99:
		loops+=1
		if len( lo ):
			n = _.shuffle( lo )[0]
		else:
			return None
			
			# _.pr( 'Error:  n' )
			# sys.exit()
		if not n in path:
			nextFound = True
	if loops == 99:
		n = min( lo )

	if not isDone:
		t = total-n
		path.append( n )
		if t > 0:
			test( num, t, path )
	# else:
	# tx = total-n
	# if tx > 0:
	#     path.append( tx )
	subT = num
	for x in path:
		subT -= x


	if not subT == 0:
		test( num, subT, path )

	else:
		return path



	


	# total = 0
	# while not total == num:
	#     pass

def findValues( num ):
	global numberList
	global powerTable
	

	
	loop = 0
	result = None
	while result is None:
		loop += 1
		if loop > 20:
			# _.pr( 'Skipping' )
			return None
		result = test( num, num, [] )
		if not result is None:
			if not sum(result) == num:
				result = None


		try:
			for x in result:
				record = powerTable[ x ]
		except Exception as e:
			result = None

	return result

		

def findShortest( num ):
	global omit
	# _.pr( 'Finding:', num )

	records = []
	spent = []

	loop = 0

	while loop < 1:
		loop += 1
		thisResult = findValues( num )
		if thisResult is None:
			omit.append( num )
			return None

		# _.pr( thisResult )
		string = str(thisResult)
		if not string in spent:
			spent.append( string )
			records.append({ 'length': len(thisResult), 'data': thisResult })

	shortest = _.tables.returnSorted( 'data', 'a.length', records )
	return shortest[0]['data']

def process( num, qID=False ):
	manual = False
	global numberList
	global resultTable
	global addedList
	addedList[num] = 0
	if manual:
		_.pr()
		_.pr( 'Processing:', num )
	resultTable[num] = findShortest( num )
	if manual:
		_.pr( resultTable[num] )
	if resultTable[num] is None:
		while resultTable[num] is None:
			addThis = _.shuffle( numberList )[0]
			if addThis < 400:
				if manual:
					_.pr( 'Adding:',addThis  )
				pass
				resultTable[num] = findShortest( num+addThis )
		addedList[num] = addThis
		if manual:
			_.pr( 'Adding:', addThis, 'worked', resultTable[num] )


	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( str(resultTable[num]) ) )


def action():
	global numberList
	global powerTable
	global dataSet
	global omit
	load()

	# process( 49 )
	# sys.exit()

	threaded = False
	dataSet = [27,30,33,36,39,42,44,46,48,50,52,54,60,66,72,78,84,90,95,100,105,110,115,120,128,136,144,152,160,168,175,182,189,196,201,208]
	if threaded:
		_.threads.add( 'NumberKnockout', trigger=complete ) # kwargs 
		_.threads.maxThreadsSafe = 225
		_.threads.autoLoadedAfter = .1
		_.threads.scheduleLoop = .01
		_.threads.auditLoop = .1
		_.threads.projectDataMaxLen = 500
		_.threads.report = False
		_.threads.auditPrint = False
		
		if _.switches.isActive('Stats'):
			_.threads.report = True
			_.threads.auditPrint = True
		else:
			_.threads.report = False
			_.threads.auditPrint = False
		# _.loadingGifX( 'Processing' )



	_.pr( 'N2K:', dataSet )
	
	for num in dataSet:
		if threaded:
			_.threads.add( 'NumberKnockout', process, [num] )
		else:
			# process( num )
			_.pr()
			_.pr('__________________________________________')
			_.colorThis( [ num ], 'cyan' )
			spent = []
			for w in [1,2,3,4,5,6]:
				for ww in [1,2,3,4,5,6]:
					for www in [1,2,3,4,5,6]:
						w3 = [w,ww,www]
						w3.sort()
						w3t = str(w3)
						if not w3t in spent:
							spent.append( w3t )
							nn = num-w
							nn = num-ww
							nn = num-www
							x = test( num, nn, [w,ww,www] )
							# _.pr('_____________________')
							# _.pr()
							# _.colorThis( [ x ], 'green' )
							powerPrint = []
							for y in x:
								try:
									powerPrint.append( str(powerTable[y]['number'])+'^'+str(powerTable[y]['power']) )
									pass
								except Exception as e:
									_.pr( 'Error' )
									# _.pr( y )
									_.printTest( powerTable )
									sys.exit()
								else:
									pass
								finally:
									pass
							_.pr( ', '.join( powerPrint ) )
				



			sys.exit()

	# for record in numberList:
	#     _.pr( record )



def complete():
	__.loadingVar['hasLoaded'] = True
	global completeRan
	if completeRan:
		return None
	completeRan = True

	global numberList
	global powerTable
	global dataSet
	global omit
	global resultTable
	global addedList

	_.pr()
	_.pr()
	_.pr()
	_.pr('_______________________________________')
	_.pr('               Complete')
	_.pr()
	_.pr()

	report = 2

	if report == 1:

		for num in dataSet:
			_.pr()
			rec = resultTable[num]
			if addedList[num]:
				_.pr( 'Number:', num, 'Added:', addedList[num], rec )
			else:
				_.pr( 'Number:', num,  rec )

	if report == 2:

		for num in dataSet:
			_.pr()
			_.pr()
			_.pr()
			rec = resultTable[num]
			_.pr( 'Number:', num )
			
			if addedList[num]:
				_.pr( 'Added:' )
				_.pr( '\t', powerTable[addedList[num]] )
				_.pr( 'New Number:', num+addedList[num] )
				_.pr()
			_.pr( 'Power Table:' )
			for r in rec:
				_.pr( '\t', powerTable[r] )


		# if rec is None:




	# _.pr( 'omit:', len(omit), omit )
	# _.pr( 'Skipped:', len(dataSet)-len(omit), 'of', len(dataSet) )


	# _.pr( 'result:', shortest[0] )
	# _.pr()

	# for x in shortest[0]['data']:
	#     record = powerTable[ x ]
	#     _.pr( record )


def load():
	global numberList
	global powerTable


	powerTable[1] = {'number': 1, 'power': 1, 'equals': 1}
	numberList.append( 1 )

	
	for nx in [2,3,4,5,6,7,8,9]:
		# for px in [0,.25,.5,.75,1,2,3,4,5,6,7,8,9]:
		for px in [1,2,3,4,5,6,7,8,9]:
			record = {}
			record['number'] = nx
			record['power'] = px
			p = math.pow( nx, px )
			pa = int(p)
			if pa:
				if p == pa:
					record['equals'] = pa
				else:
					record['equals'] = p
				powerTable[record['equals']] = record
				numberList.append( record['equals'] )

numberList = []
powerTable = {}
n = 0
omit = []
resultTable = {}
dataSet = []
completeRan = False
addedList = {}
########################################################################################
if __name__ == '__main__':
	action()