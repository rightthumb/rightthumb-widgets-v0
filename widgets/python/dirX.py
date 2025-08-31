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
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass

	_.switches.register('Database', '-db,-database')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register('Folder', '-folder')

	_.switches.register('Count', '-c,-count,--c')
	# _.switches.register('Path', '-p,-path,-folder')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('JSON', '-json')
	_.switches.register('Ago', '-ago')
	_.switches.register('Time', '-time')
	_.switches.register('Clean', '--c')
	_.switches.register('CacheInfo', '-info')
	_.switches.register('Cache', '-cache')
	_.switches.register('Save', '-save')
	_.switches.register('Extensions', '-ext', 'image, video, audio')
	_.switches.register('Totals', '-total,-totals')
	_.switches.register('FolderRefine', '-fr')


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'dirX.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Display information about files in a folder and subfolders',
	'categories': [
						'dir',
						'file',
						'folder',
						'db',
						'file database',
						'json',
						'report',
						'file report',
						'tool',
						'tools',
						'files',
						'folders',
						'meta',
						'meta data',
						'meta report',
						'meta data report',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p dirX ',
						'p dirX -ago 1d ',
						'',
						'p dirX -folder %pyFolder% -r -save %i%\\py.cache',
						'',
						'p dirX -cache %i%\\py.cache -ago 1d',
						'',
						'p dirX -r -c ext size name md cd -g ext -s ext md',
						'',
						'p dirx -ext image',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n', 'sort': '' },
						{ 'name': 'path', 'abbreviation': 'p', 'sort': '' },
						{ 'name': 'name', 'abbreviation': 'n', 'sort': '' },
						{ 'name': 'folder', 'abbreviation': 'f', 'sort': '' },
						{ 'name': 'bytes', 'abbreviation': 'b', 'sort': '' },
						{ 'name': 'size', 'abbreviation': 's', 'sort': 'bytes' },
						{ 'name': 'md5', 'abbreviation': '5', 'sort': '' },
						{ 'name': 'ext', 'abbreviation': 'e', 'sort': '' },
						{ 'name': 'year', 'abbreviation': 'y', 'sort': 'date_modified_raw' },
						{ 'name': 'date_modified', 'abbreviation': 'md,dm', 'sort': 'date_modified_raw' },
						{ 'name': 'date_created', 'abbreviation': 'cd,dc', 'sort': 'date_created_raw' },
						{ 'name': 'friendly_month', 'abbreviation': 'm', 'sort': 'date_modified_raw' },
						{ 'name': 'friendly_week', 'abbreviation': 'w', 'sort': 'date_modified_raw' },
						{ 'name': 'week_of_year', 'abbreviation': 'woy', 'sort': 'date_modified_raw' },
						{ 'name': 'day_of_the_week', 'abbreviation': 'dow', 'sort': 'date_modified_raw' },
						{ 'name': 'date_accessed', 'abbreviation': 'a,ad,da', 'sort': '' },
					
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


def unFormatSize(size):
	if len(size) == 1 and size in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
		return size.lower()
	hasNumber = False
	for x in size:
		if x in '0123456789':
			hasNumber = True
	if not hasNumber:
		return size.lower()
	if ',' in size:
		return size

	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776    
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = int(float(size))
	result = round(size * factor,0)
	return result

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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	# _.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Size', unFormatSize )
	
	
	
	_.defaultScriptTriggers()
	# _.autoAbbreviations()
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
# START


import _rightThumb._dir as _dir



def isText(file):
	global _mime
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result

def getFolder(folder):
	global i
	global iS
	global folderCount
	global fileCount
	folderCount += 1

	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:

		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		if _.switches.isActive('Files'):
			dirList = _.switches.values('Files')
			# _.pr( dirList )
		for item in dirList:
			if not _.switches.isActive('Files'):
				path = folder + _v.slash + item
				path = path.replace(_v.slash+_v.slash,_v.slash)
			else:
				path = item
			if os.path.isfile(path):
				fileCount += 1
				if _.showLine(path):
					shouldPrint = True



					if shouldPrint:
						addFile( path )

			if os.path.isdir(path) and _.switches.isActive('Recursive'):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):

					shouldRun = True
					if _.switches.isActive('FolderRefine'):
						if not _.showLine(newFolder):
							shouldRun = False
					if shouldRun:

						try:
							getFolder(newFolder)
						except Exception as e:
							pass
				else:
					_.pr('error')



def process( path ):
	global data
	global fileCount
	global i
	if os.path.isfile(path):
		fileCount += 1
		if _.showLine(path):
			shouldPrint = True



			if shouldPrint:
				shouldPrint = False
				addFile( path )



def addFile( path, hasData=False ):
	global data
	global i
	global extensionList
	record = None
	shouldAdd = False
	shouldPrint_2 = True

	if hasData:
		record = path
	else:
		record = _dir.fileInfo( path )

	if _.switches.isActive('Size'):
		shouldPrint = False
		shouldPrint_2 = False
		# stat = os.stat(path)
		# size = stat.st_size
		size = record['bytes']
		# _.pr( _.switches.values('Size') )
		# sys.exit()
		if 'l' in _.switches.values('Size')[0]:
			if size < _.switches.values('Size')[1]:
				shouldPrint_2 = True
		if 'g' in _.switches.values('Size')[0]:
			if size > _.switches.values('Size')[1]:
				shouldPrint_2 = True

	if shouldPrint_2:
		shouldPrint = False


		if _.switches.isActive('Extensions'):
			
			found = False
			# if '.'+record['ext'].lower() in extensionList:
			#     found = True


			pathX = record['path'].lower()
			for x in extensionList:
				if pathX.endswith(x):
					found = True
			if found:
				i = i + 1
				shouldPrint = True


		
		else:



			if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
				i = i + 1
				shouldPrint = True
			else:
				if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(record['path']):
					i = i + 1
					shouldPrint = True
				if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
					i = i + 1
					shouldPrint = True
				if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(record['path']):
					i = i + 1
					shouldPrint = True
				if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
					i = i + 1
					shouldPrint = True
















	shouldAdd = shouldPrint
	if shouldAdd:
		if _.switches.isActive('Ago'):

			shouldAdd = False
			run = 'default'
			if len( _.switches.values('Ago') ) > 1:
				if 'a' in _.switches.values('Ago')[1]:
					run = 'a'
				elif 'md' in _.switches.values('Ago')[1]:
					run = 'md'
				elif 'cd' in _.switches.values('Ago')[1]:
					run = 'cd'
				elif 'resent' in _.switches.values('Ago')[1]:
					run = 'resent'

			# _.pr(  len( _.switches.values('Ago') )  )
			# _.pr(  ( _.switches.values('Ago') )  )
			# sys.exit()
			# accessed_raw


			if run == 'default':
				# _.pr(record['date_modified_raw'])
				# _.pr(_.switches.values('Ago'))
				if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0]:
					shouldAdd = True
			elif run == 'resent':
				if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0] or record['accessed_raw'] > _.switches.values('Ago')[0]:
					shouldAdd = True
			elif run == 'a':
				if record['accessed_raw'] > _.switches.values('Ago')[0]:
					# _.pr( _.friendlyDate(_.switches.values('Ago')[0]), _.switches.values('Ago')[0], record['accessed_raw'], _.friendlyDate(record['accessed_raw']) )
					shouldAdd = True
			elif run == 'cd':
				if record['date_created_raw'] > _.switches.values('Ago')[0]:
					shouldAdd = True
			elif run == 'md':
				if record['date_modified_raw'] > _.switches.values('Ago')[0]:
					shouldAdd = True



	if shouldAdd:
		if _.switches.isActive('Database'):
			_dir.fileInfo( path, sql=True, insert=True )
		else:
			if not record is None:
				data.append(  record  )
			else:
				data.append(  _dir.fileInfo( path )  )

def action():
	global i
	global data
	global fileCount
	global folderCount
	global _mime

	isLegacy = False
	# load()
	start = time.time()


	if _.switches.isActive('Text') or _.switches.isActive('Binary'):
		import _rightThumb._mimetype as _mime



	if _.switches.isActive('Extensions'):
		extensionsDatabank()


	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		_.switches.fieldSet( 'Files', 'active', True )
		_.switches.fieldSet( 'Files', 'values', _.appData[__.appReg]['pipe'] )
		_.switches.fieldSet( 'Files', 'value', ','.join(_.appData[__.appReg]['pipe']) )
		# _.pr( _.switches.values('Files') )

	if _.switches.isActive('Files') and _.switches.isActive('JSON'):
		records = []
		for file in _.switches.values('Files'):
			records.append( _dir.info( file ) )
		_.printVar( records )
		sys.exit()


	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
		if not len(db):
			db = '_DIR_' + _.fileDate( time.time() ) + '_.db'
		_dir.sqlCreateTable( db , delete=True )



	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner(0)
	#     # _.printVar( _.appData )
	#     for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
	#         _.pr( row )
	#         process( row )



	else:
		if _.switches.isActive('Folder'):
			folder = _.switches.values('Folder')[0]
		else: 
			folder = os.getcwd()
 
		
		if _.switches.isActive('Cache'):
			# switches isActive values
			dataCache = _.getTable2( _.switches.values('Cache')[0] )

			if type( dataCache ) == dict:
				fileCount = dataCache['files']
				folderCount = dataCache['folders']
				dataCacheX = dataCache['data']
				isLegacy = False
			elif type( dataCache ) == list:
				isLegacy = True
				fileCount = len(dataCache)
				folderCount = 0
				folderKeys = {}
				leastFolder = None
				leastFolderC = 999999
				for record in dataCache:
					if record['folder'].count(_v.slash) < leastFolderC:
						leastFolderC = record['folder'].count(_v.slash)
						leastFolder = record['folder']
					try:
						folderKeys[ record['folder'] ] += 1
					except Exception as e:
						folderKeys[ record['folder'] ] = 1
				folderCount = len( list( folderKeys.keys() ) )
				dataCacheX = dataCache





				dataCache = {
								'isLegacy': True,
								'files': fileCount,
								'folders': folderCount,
								'folder': leastFolder,
				}

				folder = leastFolder

			if _.switches.isActive('CacheInfo'):

				if not isLegacy:
					del dataCache['data']
				elif isLegacy:

					if os.path.isdir(leastFolder):
						folderFileCheckCount = 0

						for x in os.listdir(leastFolder):
							if os.path.isfile(x):
								folderFileCheckCount+=1
						pass
						if len(list(folderKeys.keys())) > 1:
							dataCache['Recursive'] = True
						else:
							dataCache['Recursive'] = False

						if dataCache['Recursive']:
							if folderKeys[leastFolder] < folderFileCheckCount:
								dataCache['had_Criteria'] = False
							elif folderKeys[leastFolder] == folderFileCheckCount:
								dataCache['had_Criteria'] = False
							else:
								dataCache['had_Criteria'] = True

						elif not dataCache['Recursive']:
							if fileCount == folderFileCheckCount:
								dataCache['had_Criteria'] = False
							elif fileCount < folderFileCheckCount:
								dataCache['had_Criteria'] = False
							elif fileCount > folderFileCheckCount:
								dataCache['had_Criteria'] = True


						


				_.printVarSimple( dataCache )
				sys.exit()



			# {
			#     'folder': folder,
			#     'folders': folderCount,
			#     'files': fileCount,
			#     'data': data,
			# }

			for x in dataCacheX:
				# _.pr(x)
				addFile( x, hasData=True )
		else:
			getFolder(folder)


	if _.switches.isActive('Database'):
		_dir.commit()
		_.colorThis( [ '\nDatabase Created' ], 'green' )
		_.colorThis( [ '\t', db ], 'yellow' )
		end = time.time()
	else:
		end = time.time()
		# if _.switches.isActive('Ago'):
		#     newData = []
		#     ago = _.switches.value('Ago')
		#     for record in data:
		#         if record['date_modified_raw'] < ago:
		#             newData.append( record )
		#     data = newData

		if _.switches.isActive('JSON'):
			# for x in data[0].keys():
			#     _.pr(x)
			# sys.exit()
			_.printVarSimple( data )
		else:

			pass

			if not i == len(data):
				i = len(data)


			if not i == fileCount:
			# if not len(files) == i:
				# _.pr('HERE')
				_.folderProfileAttribute( folder=folder, info = {
																'app': 'dirX',
																'recursive': _.switches.isActive('Recursive'),
																'factors': {
																				'Text': _.switches.isActive('Text'),
																				'Binary': _.switches.isActive('Binary'),
																				'Extensions': _.switches.isActive('Extensions'),
																				'Type': _.switches.values('Extensions'),

																				'PlusOr': _.switches.isActive('PlusOr'),
																				'PlusClose': _.switches.isActive('PlusClose'),
																				'Ago': _.switches.isActive('Ago'),
																				'Plus': _.switches.isActive('Plus'),
																				'Minus': _.switches.isActive('Minus'),

																				'AgoVals': _.switches.values('Ago'),
																				'PlusVals': _.switches.values('Plus'),
																				'MinusVals': _.switches.values('Minus'),


																},
																'percentage': _.pDiff( fileCount, i, use='less' ),
																'count': i,
																'files': fileCount ,

				} )



			if _.switches.isActive('Save'):

				_.saveTable2( {
								'isLegacy':    False,
								'switches': {
									'isActive': {
										'Recursive': _.switches.isActive('Recursive'),
										'Extensions': _.switches.isActive('Extensions'),
										'Files': _.switches.isActive('Files'),
										'Folder': _.switches.isActive('Folder'),
										'Text': _.switches.isActive('Text'),
										'Binary': _.switches.isActive('Binary'),
										'Size': _.switches.isActive('Size'),
										'Ago': _.switches.isActive('Ago'),
										'Save': _.switches.isActive('Save'),
									},
									'values': {
										'Recursive': _.switches.values('Recursive'),
										'Extensions': _.switches.values('Extensions'),
										'Files': _.switches.values('Files'),
										'Folder': _.switches.values('Folder'),
										'Text': _.switches.values('Text'),
										'Binary': _.switches.values('Binary'),
										'Size': _.switches.values('Size'),
										'Ago': _.switches.values('Ago'),
										'Save': _.switches.values('Save'),
									},
								},
								'folder': folder,
								'folders': folderCount,
								'files': fileCount,
								'data': data,
				}, _.switches.values('Save')[0] )

			elif not _.switches.isActive('Save'):
				# if len(data) == 1:
					# _.printVarSimple( data )

				# _.switches.fieldSet( 'Long', 'active', True )
				_.tables.register( 'data', data )
				# _.tables.fieldProfileSet( 'data', '_header_', 'alignment', 'left' )
				# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
				# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')

				if not _.switches.isActive('Sort') and not _.switches.isActive('GroupBy') and not _.switches.isActive('Column'):
					if not _.switches.isActive('Files'):
						_.switches.fieldSet( 'GroupBy', 'active', True )
						_.switches.fieldSet( 'GroupBy', 'value', 'ext,week_of_year' )
						_.switches.fieldSet( 'GroupBy', 'values', ['ext','week_of_year'] )


					# _.switches.fieldSet( 'Sort', 'active', True )
					# _.switches.fieldSet( 'Sort', 'value', 'ext' )
					# _.switches.fieldSet( 'Sort', 'value', 'ext,week_of_year' )
					# _.switches.fieldSet( 'Sort', 'values', ['ext','week_of_year'] )

				if not _.switches.isActive('Long') and not _.switches.isActive('Length') and not _.switches.isActive('Short'):
					_.switches.fieldSet( 'Length', 'active', True )
					_.switches.fieldSet( 'Length', 'value', '50' )
					_.switches.fieldSet( 'Length', 'values', ['50'] )


				if _.switches.isActive('Column'):
					if len( _.switches.values('Column') ) > 1:
						if not _.switches.isActive('Totals'):
							_.tables.print( 'data', ','.join(_.switches.values('Column')) )
					else:
						# if not _.switches.isActive('Files') and not _.switches.isActive('Recursive'):
						if not _.switches.isActive('Files'):
							_.switches.fieldSet( 'Long', 'active', True )
							_.switches.fieldSet( 'GroupBy', 'active', False )
							_.switches.fieldSet( 'GroupBy', 'value', '' )
							_.switches.fieldSet( 'Sort', 'active', True )
							_.switches.fieldSet( 'Sort', 'value', _.switches.value('Column') )
							_.switches.fieldSet( 'Sort', 'values', _.switches.values('Column') )
							if not _.switches.isActive('Totals'):
								_.tables.print( 'data', ','.join( _.switches.values('Column') ), pc=False )



				elif not _.switches.isActive('Column'):
					
					if _.switches.isActive('Files') or _.switches.isActive('Recursive') or _.switches.isActive('Cache'):
						_.switches.fieldSet( 'GroupBy', 'active', True )
						GroupBy = ['folder']
						_.switches.fieldSet( 'GroupBy', 'value', ','.join(GroupBy) )
						_.switches.fieldSet( 'GroupBy', 'values', GroupBy )
						_.switches.fieldSet( 'Sort', 'active', True )
						# _.switches.fieldSet( 'Sort', 'value', 'folder,d.bytes' )
						_.switches.fieldSet( 'Sort', 'value', 'folder,d.date_modified_raw' )
						if not _.switches.isActive('Totals'):
							theColumns = 'folder,size,name,date_modified,date_created,date_accessed'
							if isLegacy:
								theColumns = theColumns.replace( ',date_accessed', '' )
							_.tables.print( 'data', _.unixAutoColumns( data, theColumns, focus() ) )
					else:
						if not _.switches.isActive('Totals'):
							theColumns = 'ext,week_of_year,name,size,date_modified,date_created,date_accessed'
							if isLegacy:
								theColumns = theColumns.replace( ',date_accessed', '' )
							_.tables.print( 'data', _.unixAutoColumns( data, theColumns, focus() ) )
					pass

				pass
			if not _.switches.isActive('Clean'):
				_.pr()

				
				totalBytes = 0

				for record in data:
					totalBytes += record['bytes']

				if i == fileCount:
					# _.colorThis(  [  '\t', i, 'files' , _.formatSize( totalBytes ), 'in', folderCount, 'folders' ], 'green'  )
					txt = '\t '
					txt += _.colorThis(  [  _.addComma(i), 'files '  ], 'yellow', p=0 )
					txt += _.colorThis(  [  _.formatSize( totalBytes ) ], 'green', p=0 )
					txt += ' in '
					txt += _.colorThis(  [  _.addComma(folderCount) + ' folders' ], 'blue', p=0 )
					_.pr( txt )
				else:
					txt = '\t ' + _.addComma(fileCount) + ' total files '
					txt += _.colorThis(  [  _.addComma(i), 'selected '  ], 'yellow', p=0 )
					txt += _.colorThis(  [  _.formatSize( totalBytes ) ], 'green', p=0 )
					txt += ' in '
					txt += _.colorThis(  [  _.addComma(folderCount) + ' folders' ], 'blue', p=0 )
					_.pr( txt )
				_.pr()
				endPrint = time.time()
				if _.switches.isActive('Time'):
					_.colorThis( [ 'App Time:', round( end-start, 3 ) ], 'yellow' )
					_.colorThis( [ 'Print Time:', round( endPrint-end, 3 ) ], 'yellow' )
					_.colorThis( [ 'Total Time:', round( endPrint-start, 3 ) ], 'yellow' )


# EXT                  WEEK OF YEAR    DATE MODIFIED          NAME                                                     SIZE


# _.printVar( _dir.fileInfo( path ) )

# def load():
#     global data
#     data = _.getTable( 'table' )


def extensionsDatabank():
	global extensionList
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )
	_db.switch( 'Plus', _.switches.values('Extensions') )
	extensionList = _db.do( 'action' )
	for i,x in enumerate(extensionList):
		extensionList[i] = x.lower()
	# _.pr( extensionList )
	# sys.exit()



extensionList = []
folderCount = 0
fileCount = 0
data = []
i=0
########################################################################################
if __name__ == '__main__':
	action()







