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
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._md5 as _md5
import _rightThumb._mimetype as _mime
##################################################
import sqlite3
try:
	import _rightThumb._beep as _beep
except Exception as e:
	_beep=None
##################################################

def appSwitches():
	_.switches.register('Database', '-db,-database')
	_.switches.register('MD5', '-md5')
	_.switches.register('Mimetype', '-m,-mime,-mimetype')
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Path', '-p,-path,-f,-fo,-folder,-i')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('Print', '-print')
	_.switches.register('Commit-Per', '-commit','46,285')
	_.switches.register('Header', '-h,-header', '5 OR all')
	# _.switches.register('Data', '-data', '')
	



_.appInfo[focus()] = {
	'file': 'indexDB.py',
	'description': 'Lists files',
	'categories': [
						'dir',
						'recursive',
						'files',
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
						'p indexDB --c ',
						'p indexDB -text ',
						'',
						'p indexDB -size g 2mb',
						'p indexDB -size L 2mb',
						'p indexDB -size g 2mb --c -folder D:\\techApps\\Python\\Python36-32'+_v.slash,
						'',
						'p indexDB -folder C:\\ -db %myIndexes%\\C_Drive.db',
						'p indexDB -folder D:\\ -db %myIndexes%\\D_Drive.db',
						'p indexDB -folder C:\\ -db %myIndexes%\\C_Drive.db -md5 -mimetype',
						'p indexDB -folder D:\\ -db %myIndexes%\\D_Drive.db -md5 -mimetype',
						'p indexDB -folder %theUSB%:\\ -db %myIndexes%\\3T_Drive.db',
						'',
						'p indexDB -folder C:\\ -db %i%\\C_Drive.db',
						'p indexDB -folder D:\\ -db %i%\\D_Drive.db',
						'',
						'p indexDB -folder C:\\ -db %i%\\C_Drive.db |  p did -beep',
						'p indexDB -folder D:\\ -db %i%\\D_Drive.db |  p did -beep',
						'',
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



def formatSize(size):
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776    :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#     result = ''
	return result

def unFormatSize(size):
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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.switches.trigger( 'Size' , unFormatSize )
	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# START

########################################################################################
def is_text(filename):
	try:
		with open(filename, 'tr') as check_file:
			check_file.read()
		return True
	except:
		return False

# function to get file content
def get_content(filename):
	try:
		with open(filename, 'r') as read_file:
			return read_file.read()
	except:
		return ""

########################################################################################


def isText(file):
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
	if _.switches.isActive('Print'):
		_.colorThis( [ folder ], 'cyan' )
	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path):

				if _.showLine(path):

					# if _.switches.isActive('Print'):
					#     _.pr( path )

					shouldPrint = False

					if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
						i = i + 1
						# _.pr(0,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					else:
						if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
							i = i + 1
							# _.pr(1,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
							i = i + 1
							# _.pr(2,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
							i = i + 1
							# _.pr(3,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True
						if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
							i = i + 1
							# _.pr(4,whatIsIt(path),path)
							# _.pr(path)
							shouldPrint = True



					if _.switches.isActive('Size'):
						shouldPrint = False
						shouldPrint_2 = False
						stat = os.stat(path)
						size = stat.st_size
						if 'l' in _.switches.values('Size')[0]:
							if size < _.switches.values('Size')[1]:
								shouldPrint_2 = True
						if 'g' in _.switches.values('Size')[0]:
							if size > _.switches.values('Size')[1]:
								shouldPrint_2 = True

						if shouldPrint_2:
							shouldPrint = False

							if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
								i = i + 1
								shouldPrint = True
							else:
								if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
									i = i + 1
									shouldPrint = True
								if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
									i = i + 1
									shouldPrint = True



								# _.pr( formatedSize, '\t', path )



					if shouldPrint:
						global checkMD5
						global mimetype
						global conn
						global cursor
						global fileContents
						
						sql = _dir.fileInfo( path, sql=True, md5=checkMD5, db_connection=conn, db_cursor=cursor, count=i, mime=mimetype )
						# sql = _dir.fileInfo( path, sql=True, md5=checkMD5, db_connection=conn, db_cursor=cursor, count=i, mime=mimetype, data=fileContents )
						# saveRecord(sql)
						# if not _.switches.isActive('Plus'):
						#     _.colorThis( path, 'cyan' )
						# else:
						#     _.pr( _.colorPlus( path, 'cyan' ) )

			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					try:
						getFolder(newFolder)
					except Exception as e:
						pass
				else:
					_.pr('error')



def action():
	if _.switches.isActive('Path') == False:
		folder = os.getcwd()
	else:
		folder = _.switches.values('Path')[0]
	if not _.switches.isActive('Database'):
		idFi = folder + os.sep + 'drive.id.sys'
		if os.path.isfile( idFi ):
			ID = _.getText(idFi,raw=True).strip()
			db = _.getTable('indexTable_drives-{8A92E16E-EA69-35DF-699C-907ED1D1376D}.json')
			for rec in db:
				if rec['id'] == ID:
					name = rec['name'].replace(' ','_')+'.db'
		else:
			name = input( 'Database Name: ' )
			name = name.replace(' ','_')+'.db'
		fo=_v.rt+os.sep+'indexes'+os.sep+name
		_.switches.fieldSet( 'Database', 'active', True )
		_.switches.fieldSet( 'Database', 'value', fo )
		_.switches.fieldSet( 'Database', 'values', [ fo ] )

	global fileContents
	global conn
	global cursor
	fileContents = _.switches.isActive('Data')
	epoch = time.time()

	if _.switches.isActive('Database'):
		databaseFile = _.switches.values('Database')[0]
	else:
		databaseFile = 'index_'+_.miniUUID()+'.db'

	if not '.db' in databaseFile:
		databaseFile += '.db'

	_.colorThis( [ '\nDatabase:', databaseFile ], 'cyan' )

	if os.path.isfile( databaseFile ):
		_.pr()
		_.pr( '___________________________________________' )
		_nd = _.regImp( __.appReg, 'fileNameDate' )
		_nd.pipe( [databaseFile] )
		_nd.do( 'action' )
		_.pr( '___________________________________________' )


		try: os.unlink(databaseFile)
		except: pass
	# sys.exit()
	# _.pr( databaseFile )
	# sys.exit()
	conn, cursor = _dir.sqlCreateTable( databaseFile )
	# conn = sqlite3.connect(databaseFile)
	# cursor = conn.cursor()
	# cursor.execute("""CREATE TABLE files (path text, name_ text, name text, folder text, stat text, attrib text, bytes int, size text, date_created_raw int, date_modified_raw int, date_created text, date_modified text, type text, typesort text, ext text, week_of_year text, week_of_year_ text, day_of_the_week text, month text, friendly_week text, friendly_month text)""")



	_.fields.register( 'files', 'name', '1000.43 KB' )
	global i
	global iS
	# load()

	
	# _.pr( folder )
	# sys.exit()
	_.pr()
	_.pr()
	_.colorThis( [ 'indexing:', folder ], 'green' )
	_.pr()
	_.pr()

	getFolder(folder)
	# if _.switches.isActive('Count') == False:
	#     if _.switches.isActive('Size'):
	#         _.colorThis( [  '\n', iS, 'of', i, '\n'  ], 'yellow' )
	#     else:
	#         _.colorThis( [  '\n{}\n'.format(i)  ], 'yellow' )
	#     # _.pr('\n{}\n'.format(i))
	# _.saveTable( _dir.timeAudit, '_dir.timeAudit.json', p=0 )
	if _.switches.isActive('Count') == False:
		_.colorThis( [ 'Created database of meta data for', _.addComma(i), 'files in ', round(time.time()-epoch,2), 'seconds,', round(  (time.time()-epoch)/60 ,1), 'minutes' ], 'yellow' )

	conn.commit()
	global _beep
	if not _beep is None:
		_beep.mission_impossible()

	
i = 0
iS = 0
# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []


import _rightThumb._dir as _dir

if _.switches.isActive('Header'):
	if not len(_.switches.value('Header')):
		_dir.header = 5
	else:
		if _.switches.value('Header') == 'all':
			_dir.header = True
		else:
			_dir.header = int(_.switches.value('Header'))



_dir.timeAudit = _.getTable( '_dir.timeAudit.json' )
_dir.timeAuditCollect = False
_dir.commitPer = 46285
if _.switches.isActive('Commit-Per'):
	_dir.commitPer = int(  _.switches.value('Commit-Per').replace( ',', '' )  )
checkMD5 = _.switches.isActive('MD5')
mimetype = _.switches.isActive('Mimetype')
########################################################################################
if __name__ == '__main__':
	action()



# fileAge
# acquireExif
# getTable2
# epoch
# getSize
# sqlCreateTable
# fileInfo
# fileInfoAction
# formatDate
# formatDateYear
# formatDateDay
# formatDateMonth
# friendlyMonthNew
# friendlyWeekNew
# getYearFromEpoch
# getWOYFromEpoch
# getDOWromEpoch
# getDOWromEpochText
# dowConvert
# formatSize
# unFormatSize
# fileNameLength
# attrib
# getAttribs
# getExtension