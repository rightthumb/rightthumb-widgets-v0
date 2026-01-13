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
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	pass
	_.switches.register('Recursion', '-r,-recursion,-recursive')
	_.switches.register('Stats', '-stats,-stat')
	_.switches.register('Save', '-save','%mData%')
	_.switches.register('SkipIsFile', '-skip')
	_.switches.register('Prefix', '-prefix')
	_.switches.register('MD5', '-md5')
	_.switches.register('Dump', '-dmp,-dump')
	_.switches.register('NoDirPass', '-no,-nopass')
	_.switches.register('PrintVar', '-printvar,-var')
	_.switches.register('Exif', '-exif')
	_.switches.register('SkipAgeCheck', '-skipcheck,-force,-update')
	_.switches.register('Pass', '-pass')
	



_.appInfo[focus()] = {
	'file': 'dir3.py',
	'description': 'Creates dir offline.dirCache executes dir0 by default',
	'categories': [
						'dir',
						'cache',
						'dirCache',
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

_.appInfo[focus()]['examples'].append('p dir3')
_.appInfo[focus()]['examples'].append('dir /s/b /a:a | p dir3')
_.appInfo[focus()]['examples'].append('p dir3 -r -dump -stats')

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
	# _.switches.trigger('PrintVar',_.myFileLocations)
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
	# setPipeData( sys.stdin.readlines() )
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
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

# books = _.getText(_v.myTables + _v.slash+'bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START
def xRefDataArchive( path ):
	global dataArchive
	result = True
	shouldRun = False

	if len( dataArchive ):
		try:
			dataArchive[0]['md5']
			shouldRun = True
		except Exception as e:
			pass
	if shouldRun:
		for data in dataArchive:
			if path.lower() == data['path'].lower() and len( data['md5'] ) > 2:
				return [ data['date_modified_raw'], data['md5'] ]

	return result
			


def getFileInfo( path, qID=False ):
	global data
	global md5
	global exif

	if _.switches.isActive('Dump'):
		sql=True
	else:
		sql=False

	__.queueLastActivity = time.time()
	if md5:
		md5Data = xRefDataArchive( path )
	else:
		md5Data = False

	# _.pr( md5Data )
	try:
		obj = _dir.fileInfo( path, sql, md5Data, exif=exif )
	except Exception as e:
		obj =False
	# _.printVar( obj )
	# sys.exit()
	# _.pr( obj )
	# sys.exit()
	if not type(obj) == bool:
		if _.switches.isActive('Dump'):
			__.projectData[focus()]['folder'][   __.pdID[focus()]['folder']  ]['data'].append( obj )
		else:
			data.append(obj)
			# _.printVar( obj )
			# sys.exit()
	
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( obj) )

def processFolder(folder, qID):
	__.queueLastActivity = time.time()
	__.threadActivity[qID]['activity'] = time.time()
	try:
		dirList = os.listdir(folder)
		for item in dirList:
			if not item == __.cacheFile:
				path = folder + _v.slash + item
				item = item.replace('\n','')

				if _.switches.isActive('Recursion'):
					if os.path.isdir(path):
						_.threads.add( 'folder', processFolder, [ path ], pID=qID )

				if os.path.isfile( path ):
					try:
						if _.switches.isActive('Recursion'):
							# getFileInfo( path )
							_.threads.add( 'folder', getFileInfo, [ path ], pID=qID )
						else:
							_.threads.add( 'folder', getFileInfo, [ path ], pID=qID )
					except Exception as e:
						__.threadActivity[qID]['error'] = True
						__.threadActivity[qID]['log'].append({'folder': folder})
	except Exception as e:
		__.threadActivity[qID]['error'] = True
		__.threadActivity[qID]['log'].append({'folder': folder})

	_.threads.spent( qID, sys.getsizeof( 'obj') )
	__.queueLastActivity = time.time()
	__.threadActivity[qID]['activity'] = time.time()

# from threading import Timer

def action():
	global md5
	global exif



	if _.switches.isActive('PrintVar'):
		# _.pr( _.switches.value('PrintVar') )

		for file in _.switches.values('PrintVar'):
			_.pr( '______________________________________________' )
			info = _dir.fileInfo( _.ci(file), md5=True, exif=True )
			_.printVar( info )
			d = _.dateDiffX( info['date_modified_raw'], time.time() )
			_.pr( 'Days:', d )
			_.pr( 'Weeks:', round(d/7,1) )
			_.pr( 'Months:', round(d/30,1) )
			y = round(d/365,1)
			if y < 1:
				_.pr( 'Years:', _.percentageDiffInt( y, 1 ), '%' )
			else:
				_.pr( 'Years:', y )
			# _.pr( _.dateDiff( info['date_modified_raw'], time.time() ) )

		sys.exit()


	if not _.switches.isActive( 'SkipAgeCheck' ):
		if os.path.isfile( __.cacheFile ):
			age = int(_dir.fileAge( __.cacheFile ))
			# _.pr( age, age/60 )
			# sys.exit()
			if ( age/60 ) < __.ageCheck:
				# _.pr( 'Skipped' )
				import dir0
				if _.switches.isActive('NoColor'):
					dir0.updateSwitchField('NoColor','active',True)
				return True

	if _.switches.isActive('Dump'):
		isDatabase = True
	else:
		isDatabase = False
	if not exif:
		_.threads.add( 'folder', trigger=complete, loaded=False, database=isDatabase ) # kwargs 
		_.threads.maxThreadsSafe = 225
		_.threads.autoLoadedAfter = .5
		_.threads.scheduleLoop = .01
		_.threads.auditLoop = .1
		_.threads.projectDataMaxLen = 500

	# Timer( .1, _.loadingGraphic ).start()

	if _.switches.isActive('Prefix'):
		if not exif:
			_.threads.prefix = _.switches.value('Prefix')


	if not type( _.appData[__.appReg]['pipe'] ) == str:
		# os.system('cls')
		# _.pr()
		if not exif:
			_.threads.report = False
			_.threads.auditPrint = False
		if _.switches.isActive('SkipIsFile'):
			info = _.appData[__.appReg]['pipe']
		else:
			info = []
			for row in _.appData[__.appReg]['pipe']:
				row = row.replace( '\n', '' )
				if os.path.isfile( row ):
					info.append( row )
		if not exif:
			_.threads.statusTotal = len( info )

		for row in info:
			row = row.replace( '\n', '' )
			if not exif:
				_.threads.add( 'folder', getFileInfo, [ row ] )
			else:
				getFileInfo( row )

	else:
		if not exif:
			if _.switches.isActive('Stats'):
				_.threads.report = True
				_.threads.auditPrint = True
			else:
				_.threads.report = False
				_.threads.auditPrint = False

			folder = os.getcwd()
			_.threads.add( 'folder', processFolder, [ folder ] )


def complete():
	global data
	# Timer( .1, _.loadingGraphicEnd ).start()
	
	if not _.switches.isActive('Dump'):
		if _.switches.isActive('Save'):
			_.saveTable2( data, _.switches.value('Save'), printThis=False )
		else:
			_.saveTable2( data, __.cacheFile, printThis=False )
			# _.pr(' p dir -cache offline.dirCache')
		if not _.switches.isActive('NoDirPass'):
			import dir0
		if _.switches.isActive('Save'):
			pass
			# _.pr( 'Saved:', _.switches.value('Save') )
		else:
			pass
			# _.pr( 'Saved:', __.cacheFile )

# ****************************************************
__.ageCheck = 20
# ****************************************************


# __.cacheFile = 'offline.dirCache'
__.cacheFile = 'ol.c'

data = []
exif = 0
if _.switches.isActive('Exif'):
	exif = 1
	if '2' in _.switches.value('Exif'):
		exif = 2
	if '1' in _.switches.value('Exif'):
		exif = 1

if _.switches.isActive('MD5'):
	md5 = True
	shouldGetData = False
	dataArchiveFile = __.cacheFile
	dataArchive = []
	if _.switches.isActive('Save'):
		if os.path.isfile( _.switches.value('Save') ):
			dataArchiveFile = _.switches.value('Save')
			shouldGetData = True
	else:
		if os.path.isfile( __.cacheFile ):
			shouldGetData = True
	if shouldGetData:
		dataArchive = _.getTable2( dataArchiveFile )
	# _.pr(dataArchiveFile)
	# _.pr(dataArchive)
else:
	md5 = False




########################################################################################
if __name__ == '__main__':
	action()