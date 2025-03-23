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
	tabGroup = 0
	tabGroup += 1
	# , group=[tabGroup,'Scan What (default current folder)'] )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','(optional) file.txt', isPipe='glob', description='Files', group=[tabGroup,'Scan What',0,'(defaults to current folder)'] )
	_.switches.register( 'Files', '-f,-fi,-file,-files','(optional) file.txt', isPipe='glob', description='Files', group=[tabGroup,'Scan What', 0,'(defaults to current folder)'] )
	_.switches.register('Folder', '-fo,-folder', group=[tabGroup,'Scan What',0,'(defaults to current folder)'] )

	_.switches.register('Recursive', '-r,-recursive', group=[tabGroup,'Scan Settings'] )
	_.switches.register('Duplicate', '-dup,-duplicates', 'bytes,epoch,filename OR (c,m,b,f,n) DAY', group=[tabGroup,'Scan Settings'] )
	_.switches.register('Ago', '-ago','1m c, 1y, 1d a', group=[tabGroup,'Refine Search'] )
	# _.switches.register('Ago_by_Created', '-cago', group=[tabGroup,'Scan Settings'] ) 
	_.switches.register('Ago-Create-Date', '-cd', group=[tabGroup,'Refine Search'] )
	_.switches.register('Text', '-t,-text,-txt', group=[tabGroup,'Refine Search'] )
	_.switches.register('Binary', '-bin', group=[tabGroup,'Refine Search'] )
	_.switches.register('Size', '-size',' g 10mb, L 2kb ', group=[tabGroup,'Refine Search'] )
	# , group=[tabGroup,'Scan Settings'] )
	_.switches.register('FolderRefine', '-fr', group=[tabGroup,'Refine Search'] )
	_.switches.register('PlusFile', '-pf,-pn,-plusfile', group=[tabGroup,'Refine Search'] )




	tabGroup += 1
	# , group=[tabGroup,'Destination'] )
	_.switches.register('Database', '-db,-database', group=[tabGroup,'Destination'] )
	_.switches.register('Cache', '-cache', group=[tabGroup,'Destination'] )
	_.switches.register('Save', '-save', group=[tabGroup,'Destination'] )
	

	tabGroup += 1
	_.switches.register('PrintBytes', '-bytes', group=[tabGroup,'Output'] )
	_.switches.register('Disable-Intelligence', '-showall', group=[tabGroup,'Output'] )
	_.switches.register('Count', '-c,-count,--c', group=[tabGroup,'Output'] )
	_.switches.register('Totals', '-total,-totals', group=[tabGroup,'Output'] )
	_.switches.register('JSON', '-json', group=[tabGroup,'Output'] )
	_.switches.register('YAML', '-yml,-yaml', group=[tabGroup,'Output'] )
	_.switches.register('Time', '-time', group=[tabGroup,'Output'] )
	_.switches.register('Clean', '--c', group=[tabGroup,'Output'] )
	_.switches.register('CacheInfo', '-info', group=[tabGroup,'Output'] )
	_.switches.register('NoMeta', '-nm,-nometa', group=[tabGroup,'Output'] )
	
	

	tabGroup += 1
	# , group=[tabGroup,'Fields'] )
	_.switches.register('Hash', '-hash', 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256', group=[tabGroup,'Fields'] )
	_.switches.register('mimeType', '-m,-mime', group=[tabGroup,'Fields'] )
	_.switches.register('MovieTitle', '-movietitle', group=[tabGroup,'Fields'] )
	_.switches.register('NameLength', '-nl,-namelength', '4 OR 4 L OR 3 g', group=[tabGroup,'Fields'] )
	_.switches.register('ExtLength', '-el,-extlength', '4 OR 4 L OR 3 g', group=[tabGroup,'Fields'] )
	_.switches.register('SuperDate', '-sdate,-superdate','older OR newer', group=[tabGroup,'Fields'] )
	
	_.switches.register('Not', '-not,-invert', group=[tabGroup,'Fields'] )
	_.switches.register('Extensions', '-ext', 'db image graphic video app audio doc script archive', group=[tabGroup,'Fields'] )
	_.switches.register('Header', '-h,-header','5', group=[tabGroup,'Fields'] )
	_.switches.register('Group>=', '++g', '2' , group=[tabGroup,'Fields'] )
	_.switches.register('Group<=', '--g', '2' , group=[tabGroup,'Fields'] )

	# _.switches.register('WOYCreatedDate', '-cwoy')



	# Recursive Extensions Files Folder Text Binary Size Ago Save 
	# Cache FolderRefine Duplicate Hash mimeType MovieTitle

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ls.py',
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
						'p ls ',
						'p ls -ago 1d ',
						'',
						'p ls -folder %pyFolder% -r -save %i%\\py.cache',
						'',
						'p ls -cache %i%\\py.cache -ago 1d',
						'',
						'p ls -r -c ext size name md cd -g ext -s ext md',
						'',
						'p ls -ext image',
						'',
						'',
						'b pys',
						'p ls -duplicates epoch -r + dir -g | p resolveIDs -replace',
						'',
						'p ls -cache %mData% -movietitle -save %mData%',
						'',
						'p ls -movietitle -c n tf -table header;left --c | p cmd2table -make rename \'{name}\' \'{file}\' -settings quote',
						'',
						'',
						'p ls -ago 2d -invert',
						'',
						'',
						'ls.p ago -ago 1m',
						'ls.p -ago 1m',
						'ls.d',
						'',
						'p ls -s md -aggregate "  isDate(me); bog?woy?week-totals=add(bytes); format( week-totals, ?size );"',
						'p ls -s md -aggregate "  isDate(me); bog?month?month-totals=add(bytes); format( month-totals, ?size );"',
						'',
						'',
						'b txt',
						'p ls -s md -aggregate "  isDate(ce); bog?woy?week-totals=add(bytes); format( week-totals, ?size );" -c week-totals | p line --c',
						'',
						'',
						'p size -print',
						'p size -print g',
						'p size -print g f',
						'',
						'p ls -c g s n -s g -g g',
						'',
	],
	'columns': [
						{ 'name': 'group', 'abbreviation': 'g', 'sort': 'bytes' },
						{ 'name': 'path', 'abbreviation': 'p', 'sort': '' },
						{ 'name': 'name', 'abbreviation': 'n', 'sort': 'path' },
						{ 'name': 'folder', 'abbreviation': 'f', 'sort': 'path' },
						{ 'name': 'relative', 'abbreviation': 'r', 'sort': 'path' },
						{ 'name': 'parent', 'abbreviation': 'pa,par,rent', 'sort': 'path' },
						{ 'name': 'bytes', 'abbreviation': 'b', 'sort': '' },
						{ 'name': 'size', 'abbreviation': 's', 'sort': 'bytes' },
						{ 'name': 'size', 'abbreviation': 'size', 'sort': 'bytes' },
						{ 'name': 'md5', 'abbreviation': '5', 'sort': '' },
						{ 'name': 'ext', 'abbreviation': 'e', 'sort': '' },
						{ 'name': 'year', 'abbreviation': 'y', 'sort': 'date_modified_raw' },
						{ 'name': 'date_modified', 'abbreviation': 'm,md,dm', 'sort': 'date_modified_raw' },
						{ 'name': 'date_created', 'abbreviation': 'c,cd,dc', 'sort': 'date_created_raw' },
						{ 'name': 'friendly_month', 'abbreviation': 'm', 'sort': 'date_modified_raw' },
						{ 'name': 'friendly_week', 'abbreviation': 'w', 'sort': 'date_modified_raw' },
						{ 'name': 'week_of_year', 'abbreviation': 'woy', 'sort': 'date_modified_raw' },
						{ 'name': 'ago', 'abbreviation': 'ago', 'sort': 'date_modified_raw' },
						{ 'name': 'day_of_the_week', 'abbreviation': 'dow', 'sort': 'date_modified_raw' },
						{ 'name': 'date_accessed', 'abbreviation': 'a,ad,da', 'sort': '' },
						{ 'name': 'movie', 'abbreviation': 'mv,mt', 'sort': '' },
						{ 'name': 'title', 'abbreviation': 't,mvt', 'sort': '' },
						{ 'name': 'file', 'abbreviation': 'tf', 'sort': '' },
						{ 'name': 'sdate', 'abbreviation': 'sdate', 'sort': 'sdate_raw' },
						{ 'name': 'dps', 'abbreviation': 'sdate', 'sort': 'sdate_raw' },
						{ 'name': 'header', 'abbreviation': 'h' },
						# { 'name': 'hash', 'abbreviation': '?', 'sort': '' },
					
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

def save_trigger(data):
	if not '.' in data:
		return data+'.ls'




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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.bAlias )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Size', unFormatSize )
	# _.switches.trigger( 'Save', save_trigger )
	
	
	
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


if _.switches.isActive('Column') and len(_.switches.value('Column')) and 'header' in _.switches.values('Column'):
	if not _.switches.isActive('Header'): 
		_.switches.fieldSet( 'Header', 'active', True )

import _rightThumb._dir as _dir
if _.switches.isActive('Header'):
	if not len(_.switches.value('Header')):
		_dir.header = 5
	else:
		if _.switches.value('Header') == 'all':
			_.switches.fieldSet( 'Long', 'active', True )
			_dir.header = True
		else:
			_dir.header = int(_.switches.value('Header'))



if _.switches.isActive('Ago_by_Created'):
	_dir.dateCalcByModified = False
	if not _.switches.isActive('Sort') and not _.switches.isActive('GroupBy'):
		_.switches.fieldSet( 'Sort', 'active', True )
		_.switches.fieldSet( 'Sort', 'value', 'date_created_raw,ago' )
		_.switches.fieldSet( 'Sort', 'values', ['date_created_raw','ago'] )
		_.switches.fieldSet( 'GroupBy', 'active', True )
		_.switches.fieldSet( 'GroupBy', 'value', 'ago' )
		_.switches.fieldSet( 'GroupBy', 'values', ['ago'] )

	# if not _.switches.isActive('GroupBy'):
		# _.switches.fieldSet( 'Sort', 'active', True )
		# WEEK OF YEAR
	#   date_modified_raw

	# _.pr('cwoy ')

def movieTitle(pipeData):
	theResult = pipeData
	def clean( p ):
		p = p.replace('\n','')
		p = p.replace('\r','')
		p = p.replace('\t','')
		p = _str.replaceDuplicate(p,' ')
		p = _str.cleanBE(p,' ')
		# dots = p.split('.')
		# _.pr(dots[len(dots)-1])
		# p.replace(dots[len(dots)-1],'')
		line = ''
		i=0
		for t in p.split('.'):
			i+=1
			if not i == len(p.split('.')):
				line += t + ' '
		p = line
		p = _str.replaceAll(p,'_',' ')
		# p = _str.totalStrip7(p)
		p = p.replace('_',' ')
		p = p.replace('.',' ')
		# p = line
		line = p.split('(')[0]
		line = _str.cleanBE(line,' ')
		if len(line) == 0:
			try:
				line = p.split(')')[1]
			except Exception as e:
				pass
		line = _str.cleanBE(line,' ')
		line = line.split('.')[0].split('HD-TS')[0].split('x264')[0].split('1080P')[0].split('1080p')[0].split('720p')[0].split('HDRip')[0].split('HDCLUB')[0].split('BluRay')[0].split('BluRay')[0].split('_track')[0].split(' HDTV')[0].split(' MULTI ')[0].split( '2160P' )[0].split( '2160p' )[0].split( '512Kb' )[0]
		line = line.lower()
		line = line.title()
		line = _str.cleanBE(line,' ')
		if '(' in p:
			line += ' ' + p.split('(')[1].split(')')[0]
		# _.pr(line.encode('ascii'))
		y = False
		for l in line.split(' '):
			if len(l) == 4:
				try:
					test0 = int(l)
					test1 = str(test0)
				except Exception as e:
					test1 = ''
				if len(test1) == 4:
					year = l
					y = True
		if y:
			line = line.replace(year,'')
			# line = line + ' ' + year
			line = year + ' ' + line
		line = _str.replaceDuplicate(line,' ')
		# line = line.replace('WwW SeeHD PL','').replace('WwW SeeHD','').replace('NEW','').replace('new','').replace('New','').replace('WEB-DL','').replace('WEB-DLRip','').replace('46Gb','').replace('Rip 1  Line MegaPeer','')
		# line = line.replace('P TS','')
		line = removeStuff(line)
		line = _str.charFix( line )
		line = _str.replaceDuplicate(line,' ')
		line = _str.cleanBE(line,' ')
		return line
	pass

	def removeStuff( line ):
		stuff = [
					'WwW SeeHD PL',
					'WwW SeeHD',
					'NEW',
					'new',
					'New',
					'WEB-DL',
					'WEB-DLRip',
					'46Gb',
					'Rip 1  Line MegaPeer',
					'P TS',
					'E:\\MOVIES'+_v.slash,
					'dvdrip',
					'xvid',
					'kinokopilka',
					' www ',
					' dvdrip ',
					' Hmark ',
					' Dvdrip ',
					'Xvid',
					'Bgaudio',
					'Siso',
					'-',
					'"',
					'Dvdrip',
					'Brrip',
					'Youtube',
					'youtube',
				]
		for s in stuff:
			line = line.replace(s,' ')
		return line
	def cleanUpMovie(title):
		title = _str.replaceDuplicate( title, ' ' )
		title = _str.cleanBE( title, ' ' )
		title = _str.cleanBE( title, ',' )
		title = _str.cleanBE( title, ' ' )
		return title
	def yearCheckRecordFix( record ):
		if type(record) == str:
			if '.' in record:
				temp = record.split('.')
				temp.pop()
				record = '.'.join(temp)
			newRecord = ''
			year = ''
			last = 'T'
			for x in record:
				if x in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-:':
					if not x in '0123456789':
						if not len(year) == 4:
							year = ''
					elif  x in '0123456789':
						year+=x
					newRecord += x
			newRecord = newRecord.replace(year,'')
			return year, cleanUpMovie(newRecord)

			# _.pr( record )
		if not type(record) == tuple:
			return record
		elif type(record) == tuple:
			if record[0][0] in '0123456789' and record[0][1] in '0123456789' and record[0][2] in '0123456789' and record[0][3] in '0123456789':
				year = record[0][0]+record[0][1]+record[0][2]+record[0][3]
				movie = cleanUpMovie(record[0][4:])

				return year,movie

			else:
				year, movie = movieTitle( record[2] )
				if not len(year) == 4:
					return '', record[0]
				return year, movie


	pass
	theTitle = ''
	result = []
	dataType = 'filename'
	for p in pipeData:
		# _.pr( ( p ) )
		# sys.exit()
		if type( p ) == dict:
			dataType = 'dict'
			f = p['folder'].lower().split(_v.slash)
			folder = f[ len(f)-1 ]

			if folder == 'samples' or folder == 'extras':
				folder = f[ len(f)-2 ]
			elif folder == 'mobile movies':
				folder = ''

			line = clean( folder + ' ' + p['name'] )
		else:
			line = clean( p )
		# _.pr( line )
		if len(line) > 0 and not 'sample' in line:
			if dataType == 'filename':
				result.append(line)
			else:
				result.append( { 'title': line, 'folder': p['folder'], 'file': p['name'], 'mod': p['date_modified_raw'], 'bytes': p['bytes'] } )
	if dataType == 'filename':
		for res in  set(result):
			if _.switches.isActive('JustVar'):
				theTitle = res.title()
			else:
				theResult = res.title()
	else:
		for res in  (result):
			if _.switches.isActive('JustVar'):
				theTitle = { 'title': res['title'].title(), 'folder': res['folder'], 'file': res['file'], 'mod': res['mod'], 'bytes': res['bytes'] }
			else:
				theResult = res['title'].title()+',', res['folder']+',', res['file']
				
	if 'sample' in theTitle.lower():
		theTitle = 'sample'
	pass
	if theResult == '':
		theResult = theTitle


	return yearCheckRecordFix( theResult )



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

	if not os.path.isdir(folder): return None

	if not _.v.do_not_hide__pycache:
		if '__pycache__' in folder.split(os.sep)[-1]: return None

	if _.switches.isActive('Minus'):
		if not _.showLine(folder):
			return None

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
				if _.switches.isActive('PlusFile'):
					sL = _.showLine(item)
				else:
					sL = _.showLine(path)
				sL = True
				if _.switches.isActive('NameLength'): # ExtLength
					sL = True
				if _.switches.isActive('ExtLength'): # ExtLength
					sL = True
				if sL:
					shouldPrint = True



					if shouldPrint:
						addFile( path )

			if os.path.isdir(path) and _.switches.isActive('Recursive'):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):

					shouldRun = True
					if _.switches.isActive('FolderRefine'):
						sL = _.showLine(newFolder)
						if _.switches.isActive('NameLength'): # ExtLength
							sL = True
						if _.switches.isActive('ExtLength'): # ExtLength
							sL = True
						if not sL:
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
		sL = _.showLine(path)
		if _.switches.isActive('NameLength'): # ExtLength
			sL = True
		if _.switches.isActive('ExtLength'): # ExtLength
			sL = True
		if sL:
			shouldPrint = True



			if shouldPrint:
				shouldPrint = False
				addFile( path )



def addFile( path, hasData=False ):

	if not _.v.do_not_hide__pycache and path.endswith('.pyc'): return None

	global data
	global i
	global omit
	global extensionList
	global meta
	record = None
	shouldAdd = False
	shouldPrint_2 = True

	if hasData:
		record = path
	else:
		record = _dir.fileInfo( path, sdate=__.sdate, meta=meta )
		# record['modified'] = _.friendlyDate( record['me'] )
	if type(record) == bool:
		error = ''
		try:
			_dir.fileInfo(path,err=True)
		except Exception as e:
			error = e
		_.pr( 'Error:', os.path.isfile(path),path, error, '\n________________________\n' )

		return None
	
	if _.switches.isActive('PlusFile'):
		sL = _.showLine( record['name'] )
	else:
		sL = _.showLine( record['path'] )


	if _.switches.isActive('NameLength'): # ExtLength
		sL = True
	if _.switches.isActive('ExtLength'): # ExtLength
		sL = True
	if not sL:
		return None

	if record['name'].lower() in omit:
		return None

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
			#   found = True


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
				if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(record['path']) == True :
					# _.pr(isText(record['path']))
					i = i + 1
					shouldPrint = True
				elif not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
					i = i + 1
					shouldPrint = True
				elif not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(record['path']) == True:
					i = i + 1
					shouldPrint = True
				elif not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
					i = i + 1
					shouldPrint = True



	shouldAdd = shouldPrint
	if shouldAdd:
		if _.switches.isActive('Ago'):

			shouldAdd = False
			run = 'default'

			if len( _.switches.values('Ago') ) > 2:
				if 'a' in _.switches.values('Ago')[2]:
					run = 'a'
				elif 'cd' in _.switches.values('Ago')[2]:
					run = 'cd'
				elif 'md' in _.switches.values('Ago')[2]:
					run = 'md'
				elif _.switches.isActive('Ago-Create-Date'):
					run = 'cd'
				elif 'resent' in _.switches.values('Ago')[2]:
					run = 'resent'
				elif 'm' in _.switches.values('Ago')[2]:
					run = 'md'


			elif len( _.switches.values('Ago') ) == 2 and type(_.switches.values('Ago')[1]) == str:
				# _.pr('asdf')
				if 'a' in _.switches.values('Ago')[1]:
					run = 'a'
				elif 'cd' in _.switches.values('Ago')[1]:
					run = 'cd'
				elif 'md' in _.switches.values('Ago')[1]:
					run = 'md'
				elif _.switches.isActive('Ago-Create-Date'):
					run = 'cd'
				elif 'resent' in _.switches.values('Ago')[1]:
					run = 'resent'
				elif 'm' in _.switches.values('Ago')[1]:
					run = 'md'

			# print(len( _.switches.values('Ago') ))
			# print(_.switches.values('Ago'))
			# print(run)
			# print(run)
			# print(run)
			# _.e(1)
			# _.pr(  len( _.switches.values('Ago') )  )
			# _.pr(  ( _.switches.values('Ago') )  )
			# sys.exit()
			# accessed_raw

			agoRange = False
			if len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == float:
				agoRange = True

			# _.pr(  'agoRange', agoRange  )

			if not agoRange:
				if run == 'default':
					# _.pr(record['date_modified_raw'])
					# _.pr(_.switches.values('Ago'))
					if record['date_modified_raw'] > _.switches.values('Ago')[0]:
						shouldAdd = True
				elif run == 'resent':
					if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0] or record['accessed_raw'] > _.switches.values('Ago')[0]:
						shouldAdd = True
				elif run == 'a':
					if record['accessed_raw'] > _.switches.values('Ago')[0]:
						# _.pr( _.friendlyDate(_.switches.values('Ago')[0]), _.switches.values('Ago')[0], record['accessed_raw'], _.friendlyDate(record['accessed_raw']) )
						shouldAdd = True
				elif run == 'cd':
					# _.e()
					if record['date_created_raw'] > _.switches.values('Ago')[0]:
						shouldAdd = True
				elif run == 'md':
					if record['date_modified_raw'] > _.switches.values('Ago')[0]:
						shouldAdd = True
			elif agoRange:
				if run == 'default':
					# _.pr(record['date_modified_raw'])
					# _.pr(_.switches.values('Ago'))
					if record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0]:
						if record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1]:
							shouldAdd = True
				elif run == 'resent':
					if record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0] or record['accessed_raw'] < _.switches.values('Ago')[0]:
						if record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1] or record['accessed_raw'] > _.switches.values('Ago')[1]:
							shouldAdd = True
				elif run == 'a':
					if record['accessed_raw'] < _.switches.values('Ago')[0]:
						if record['accessed_raw'] > _.switches.values('Ago')[1]:
							shouldAdd = True
				elif run == 'cd':
					# _.e()
					if record['date_created_raw'] < _.switches.values('Ago')[0]:
						if record['date_created_raw'] > _.switches.values('Ago')[1]:
							shouldAdd = True
				elif run == 'md':
					if record['date_modified_raw'] < _.switches.values('Ago')[0]:
						if record['date_modified_raw'] > _.switches.values('Ago')[1]:
							shouldAdd = True


	if _.switches.isActive('Not'):
		if shouldAdd:
			shouldAdd = False
		else:
			shouldAdd = True

	if shouldAdd:
		if not _.v.do_not_hide__pycache and record['path'].endswith('.pyc'): shouldAdd=False

	if shouldAdd:

		if _.switches.isActive('MovieTitle'):
			record['movie'] = ''
			record['title'] = ''
			record['file'] = ''
			found = False
			pathX = record['path'].lower()
			for x in extensionList:
				if pathX.endswith(x):
					found = True
			if found:
				record['movie'] = movieTitle( [record] )
				record['title'] = record['movie'][0]+' '+record['movie'][1]
				record['file'] = record['title']+'.'+record['ext']


		if _.switches.isActive('Database'):
			_dir.fileInfo( path, sql=True, insert=True, sdate=__.sdate, meta=meta )
			# record['modified'] = _.friendlyDate( record['me'] )
		else:
			if not record is None:
				data.append(  record  )
			else:
				data.append(  _dir.fileInfo( path, sdate=__.sdate, meta=meta )  )

# print(list(os.get_terminal_size())[0])
# sys.exit()

def relative_folder(path):
	return path.replace(os.getcwd()+os.sep,'')


def action():
	global i
	global fileCount
	global folderCount
	global _mime
	global meta
	if _.switches.isActive('Files') and (_.switches.isActive('JSON') or _.switches.isActive('YAML')):
		__.dir.print=True
		if _.switches.isActive('JSON') and len(_.switches.value('JSON')):
			__.dir.print=False
		if _.switches.isActive('YAML') and len(_.switches.value('YAML')):
			__.dir.print=False

		records = []
		for file in _.switches.values('Files'):
			records.append( _dir.fileInfoAction( file, sdate=__.sdate, meta=meta ) )
		if len(records) ==1: records=records[0]
		if _.switches.isActive('JSON'):
			_.pv( records )
		elif _.switches.isActive('YAML'):
			print(_.toYML(records))

		sys.exit()
	_.v.do_not_hide__pycache = _.switches.isActive('Disable-Intelligence')
	try:
		if 165 < list(os.get_terminal_size())[0] and not _.switches.isActive('Long'): _.switches.fieldSet( 'Long', 'active', True )
	except Exception as e: _.switches.fieldSet( 'Long', 'active', True )
	global data
	# _.pr('_.isData()',_.isData())
	# focus()
	# _.pr('ce797caa1c16', _.switches.values('Files') )
	if _.isData():
		data=[]
		for path in _.isData():
			path=path.strip()
			path=path.replace('"','')
			if os.path.isfile(path):
				path=__.path(path)
				# _.pr(path)
				addFile(path)
		pass
		if _.switches.isActive('Totals'):
			total=0
			for rec in data:
				total+=rec['bytes']
			_.cp( _.formatSize(total), 'green' )
			if _.switches.isActive('PrintBytes'): _.cp( ['bytes:',totalBytes], 'cyan' )
			return None
		elif not _.switches.isActive('Totals'):
			
			_.tables.register( 'data', data, w=1 )
			_.tables.fieldProfileSet( 'data', 'folder', 'trigger', relative_folder )
			# _.tables.fieldProfileSet( 'data', 'week_of_year', 'trigger', _.woyTrigger )
			_.tables.fieldProfileSet( 'data', 'meta.epoch.me', 'trigger', _.friendlyDate )
			_.tables.fieldProfileSet( 'data', 'meta.epoch.ae', 'trigger', _.friendlyDate )
			_.tables.fieldProfileSet( 'data', 'meta.epoch.ce', 'trigger', _.friendlyDate )
			if _.switches.isActive('mimeType'):
				theColumns = 'mime,ext,ago,name,size,date_modified,date_created,date_accessed'
			else:
				theColumns = 'ext,ago,name,size,date_modified,date_created,date_accessed'
			if 0:
				theColumns = theColumns.replace( ',date_accessed', '' )

			theColumns = theColumns.replace( ',date_accessed', '' )
			_.tables.print( 'data', _.responsiveColumns( data, theColumns, focus() ) )
			return None

	# _.switches.fieldSet( 'NoTableLines', 'active', True )
	if _.switches.isActive('Group>='):
		g = _.switches.values('Group>=')[0]
		try:
			s = str(_.size_group_size(g))
			_.switches.fieldSet( 'Size', 'active', True )
			_.switches.fieldSet( 'Size', 'value', 'g,'+s )
			_.switches.fieldSet( 'Size', 'values', ['g',s] )
		except Exception as e:
			pass

	if _.switches.isActive('Group<='):
		g = _.switches.values('Group<=')[0]
		s = str(_.size_group_size(g))
		# _.pr( g,s )
		_.switches.fieldSet( 'Size', 'active', True )
		_.switches.fieldSet( 'Size', 'value', 'l,'+s )
		_.switches.fieldSet( 'Size', 'values', ['l',s] )



	isLegacy = False
	# load()
	start = time.time()


	if _.switches.isActive('Text') or _.switches.isActive('Binary'):
		import _rightThumb._mimetype as _mime



	if _.switches.isActive('Extensions') or _.switches.isActive('MovieTitle'):
		if _.switches.isActive('MovieTitle'):
			_.switches.fieldSet( 'Extensions', 'values', ['video'] )
		extensionsDatabank()


	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		_.switches.fieldSet( 'Files', 'active', True )
		_.switches.fieldSet( 'Files', 'values', _.appData[__.appReg]['pipe'] )
		_.switches.fieldSet( 'Files', 'value', ','.join(_.appData[__.appReg]['pipe']) )
		# _.pr( _.switches.values('Files') )


	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
		if not len(db):
			db = '_DIR_' + _.fileDate( time.time() ) + '_.db'
		_dir.sqlCreateTable( db , delete=True )



	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#   _.pipeCleaner(0)
	#   # _.printVar( _.appData )
	#   for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
	#       _.pr( row )
	#       process( row )



	else:
		if _.switches.isActive('Folder'):
			folders = _.switches.values('Folder')
		else: 
			folders = [os.getcwd()]
		if not folders:
			if len(_.switches.value('Folder')):
				folders.append(_.switches.value('Folder'))
			else:
				_.e( 'no folder selected' )
		#   folders.append(os.getcwd())
		# _.pr(folders)
		# sys.exit()
		for folder in folders:
			# _.pr(folder)
			# sys.exit()
			if _.switches.isActive('Cache') or ( _.switches.isActive('LoadEpoch') and not __.payloadCache is None ):
				_.switches.fieldSet( 'Cache', 'active', True )
				if _.switches.isActive('LoadEpoch'):
					dataCache = __.payloadCache
				else:
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
				#   'folder': folder,
				#   'folders': folderCount,
				#   'files': fileCount,
				#   'data': data,
				# }

				for x in dataCacheX:
					# _.pr(x)
					addFile( x, hasData=True )
			else:
				getFolder(folder)

	# if _.switches.isActive('Sort'): data = _.tables.returnSorted( 'data', _.switches.value('Sort'), data );

	if _.switches.isActive('Database'):
		_dir.commit()
		_.colorThis( [ '\nDatabase Created' ], 'green' )
		_.colorThis( [ '\t', db ], 'yellow' )
		end = time.time()
	else:
		end = time.time()
		# if _.switches.isActive('Ago'):
		#   newData = []
		#   ago = _.switches.value('Ago')
		#   for record in data:
		#       if record['date_modified_raw'] < ago:
		#           newData.append( record )
		#   data = newData

		if _.switches.isActive('JSON'):
			# for x in data[0].keys():
			#   _.pr(x)
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
																'app': 'ls',
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



			if _.switches.isActive('mimeType'):
				for i,record in enumerate(data):
					data[i]['mime'] = _mime.what( record['path'] )

			if _.switches.isActive('Hash'):
				import _rightThumb._md5 as _hash
				hashes = 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256'

				for i,record in enumerate(data):

					for h in hashes.split(' '):
						if h in _.switches.values('Hash'):
							data[i][h] = _hash.file( record['path'], h=h )
			# Cache FolderRefine Duplicate Hash mimeType MovieTitle
			saveFile = {
								'argv': sys.argv,
								# 'switches': {
								#     'active': [],
								#     'isActive': {},
								#     'values': {},
								# },
								'folder': folder,
								'folders': folderCount,
								'files': fileCount,
								'data': data,
								'isLegacy': False,
			}
			
			# saveFile['switches'] = _.switches.records('dic_a-v')

			_.payloadCache( saveFile )
			

			if _.switches.isActive('Save'):
				# _.pr(saveFile)
				# _.pr(_.switches.values('Save')[0])
				_.pr( 'Saved:', _.switches.values('Save')[0] )
				_.saveTable2( saveFile, _.switches.values('Save')[0] )

			elif not _.switches.isActive('Save'):



				if _.switches.isActive('Duplicate'):
					if _.switches.value('Duplicate') == '':
						keyType = 'bytes,epoch'
					else:
						keyType = _.switches.value('Duplicate').lower()


					table = {}
					duplicates = []
					delim = '*'
					for i,record in enumerate(data):

						key = ''
						if 'created' in keyType or ( 'c' in keyType and not 'epoch' in keyType ) or keyType.count('c') > 1:
							if 'day' in keyType:
								key += record['date_created'].split(' ')[0]
							else:
								key += record['date_created']
							# date_created date_created_raw
						if 'bytes' in keyType or 'b' in keyType:
							key += str(record['bytes'])
						key += delim
						if 'epoch' in keyType or ( 'm' in keyType and not 'name' in keyType ) or keyType.count('m') > 1:
							if 'day' in keyType:
								key += record['date_modified'].split(' ')[0]
							else:
								key += str(record['date_modified_raw'])
						key += delim
						if 'f' in keyType or 'n' in keyType:
							# _.printTest(record)
							key += str(record['name'])
						if 'test0' in keyType:
							_.pr(key)
						if key in table:
							table[key].append(i)
							if not key in duplicates:
								duplicates.append(key)
						else:
							table[key] = []
							table[key].append(i)

					pass
					if _.switches.isActive( 'GroupBy' ):
						keyType+='test11'
					for key in duplicates:
						_.pr()
						if 'test1' in keyType:
							keyP = key
							if 'test11' in keyType:
								keyP = keyP.replace( '*', '' )
							_.pr(keyP)
							_.pr()
						for i in table[key]:
							# _.pr(i)
							day = ''
							if 'test1' in keyType:
								day = '\t'
							# day = data[i]['date_modified_raw']
							# day = data[i]['date_modified'].split(' ')[0]
							if 'day' in keyType:
								if 'created' in keyType or ( 'c' in keyType and not 'epoch' in keyType ) or keyType.count('c') > 1:
									day += data[i]['date_created'].split(' ')[0]
								if 'epoch' in keyType or ( 'm' in keyType and not 'name' in keyType ) or keyType.count('m') > 1:
									if not day == data[i]['date_modified'].split(' ')[0]:
										if not day == '':
											day += ' '
										day += data[i]['date_modified'].split(' ')[0]
								_.pr( day, data[i]['path'] )
							else:
								_.pr( day+data[i]['path'] )



					return None

				# if len(data) == 1:
					# _.printVarSimple( data )

				# _.switches.fieldSet( 'Long', 'active', True )

				# if _.switches.isActive('Sort'): data = _.tables.returnSorted( 'data', _.switches.value('Sort'), data );

				if _.switches.isActive('NameLength'): # ExtLength
					if len(_.switches.value('NameLength')):
						ln = len(_.switches.values('NameLength'))
						length = int( _.switches.values('NameLength')[0] )
						op = '=='
						if ln > 1:
							if 'g' in _.switches.values('NameLength')[1].lower():
								op = '>='
							elif 'l' in _.switches.values('NameLength')[1].lower():
								op = '<='
						nw = []
						for record in data:
							# if True:
							if _.showLine(record['name']):
								if len(record['ext']):
									nN = record['name'][0:len(record['name'])-len(record['ext'])-1]
									fL = len(nN)
									# _.pr( nN, record['name'], record['ext'], length, op, fL )
									# _.pr( length, op, fL )
									shouldAdd = False
									if op == '==':
										if fL == length:
											shouldAdd = True
									elif op == '>=':
										if fL >= length:
											shouldAdd = True
									elif op == '<=':
										if fL <= length:
											shouldAdd = True
									if shouldAdd:
										# _.pr( nN, record['name'], record['ext'], length, op, fL )
										record['length'] = fL
										nw.append(record)

						data = nw

				# ExtLength
				if _.switches.isActive('ExtLength'):
					if len(_.switches.value('ExtLength')):
						ln = len(_.switches.values('ExtLength'))
						length = int( _.switches.values('ExtLength')[0] )
						op = '=='
						if ln > 1:
							if 'g' in _.switches.values('ExtLength')[1].lower():
								op = '>='
							elif 'l' in _.switches.values('ExtLength')[1].lower():
								op = '<='
						nw = []
						for record in data:
							if _.showLine(record['ext']):
								nN = record['ext']
								fL = len(nN)
								# _.pr( nN, record['name'], record['ext'], length, op, fL )
								# _.pr( length, op, fL )
								shouldAdd = False
								if op == '==':
									if fL == length:
										shouldAdd = True
								elif op == '>=':
									if fL >= length:
										shouldAdd = True
								elif op == '<=':
									if fL <= length:
										shouldAdd = True
								if shouldAdd:
									# _.pr( nN, record['name'], record['ext'], length, op, fL )
									record['length'] = fL
									nw.append(record)

						data = nw


				_.tables.register( 'data', data, w=1 )
				_.tables.fieldProfileSet( 'data', 'folder', 'trigger', relative_folder )
				# _.tables.fieldProfileSet( 'data', 'week_of_year', 'trigger', _.woyTrigger )
				_.tables.fieldProfileSet( 'data', 'meta.epoch.me', 'trigger', _.friendlyDate )
				_.tables.fieldProfileSet( 'data', 'meta.epoch.ae', 'trigger', _.friendlyDate )
				_.tables.fieldProfileSet( 'data', 'meta.epoch.ce', 'trigger', _.friendlyDate )
				# _.pr('here')
				# _.tables.fieldProfileSet( 'data', 'week_of_year', 'trigger', _.woyTrigger )
				# _.tables.fieldProfileSet( 'data', '_header_', 'alignment', 'left' )
				# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
				# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')

				if not _.switches.isActive('Sort') and not _.switches.isActive('GroupBy') and not _.switches.isActive('Column'):
					if not _.switches.isActive('Files'):
						_.switches.fieldSet( 'GroupBy', 'active', True )
						if _.switches.isActive('mimeType'):
							_.switches.fieldSet( 'GroupBy', 'value', 'mime,ext,ago' )
							_.switches.fieldSet( 'GroupBy', 'values', ['mime','ext','ago'] )
						else:
							_.switches.fieldSet( 'GroupBy', 'value', 'ext,ago' )
							_.switches.fieldSet( 'GroupBy', 'values', ['ext','ago'] )


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
							if not _.switches.isActive('Sort'):
								_.switches.fieldSet( 'Sort', 'active', True )
								_.switches.fieldSet( 'Sort', 'value', _.switches.value('Column') )
								_.switches.fieldSet( 'Sort', 'values', _.switches.values('Column') )
							if not _.switches.isActive('Totals'):
								_.tables.print( 'data', ','.join( _.switches.values('Column') ) )

						else:
							_.switches.fieldSet( 'Sort', 'active', True )
							_.switches.fieldSet( 'Sort', 'value', _.switches.value('Column') )
							_.switches.fieldSet( 'Sort', 'values', _.switches.values('Column') )
							if not _.switches.isActive('Totals'):
								_.tables.print( 'data', ','.join( _.switches.values('Column') ) )


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
							if len(data) and not 'date_accessed' in list(data[0].keys()):
								theColumns = theColumns.replace( ',date_accessed', '' )
							

							theColumns = theColumns.replace( ',date_accessed', '' )
							_.tables.print( 'data', _.unixAutoColumns( data, theColumns, focus() ) )

					else:
						if not _.switches.isActive('Totals'):
							if _.switches.isActive('mimeType'):
								theColumns = 'mime,ext,ago,name,size,date_modified,date_created,date_accessed'
							else:
								theColumns = 'ext,ago,name,size,date_modified,date_created,date_accessed'
							if isLegacy:
								theColumns = theColumns.replace( ',date_accessed', '' )

							theColumns = theColumns.replace( ',date_accessed', '' )
							_.tables.print( 'data', _.unixAutoColumns( data, theColumns, focus() ) )
							
					pass

				pass
			if not _.switches.isActive('Clean'):
				_.pr()

				
				totalBytes = 0

				for record in data:
					try:
						totalBytes += record['bytes']
					except Exception as e:
						pass

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
				if _.switches.isActive('PrintBytes'): _.cp( ['bytes:',totalBytes], 'cyan' )
				endPrint = time.time()
				if _.switches.isActive('Time'):
					_.colorThis( [ 'App Time:', round( end-start, 3 ) ], 'yellow' )
					_.colorThis( [ 'Print Time:', round( endPrint-end, 3 ) ], 'yellow' )
					_.colorThis( [ 'Total Time:', round( endPrint-start, 3 ) ], 'yellow' )


# EXT                  WEEK OF YEAR    DATE MODIFIED          NAME                                                     SIZE


# _.printVar( _dir.fileInfo( path ) )

# def load():
#   global data
#   data = _.getTable( 'table' )

# test
# test
# test
# test
# test
# test

__.sdate = None
if _.switches.isActive('SuperDate'):
	__.sdate = _.switches.values('SuperDate')[0]


def extensionsDatabank():
	global extensionList
	extensionList = []
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )

	for index in _.switches.values('Extensions'):
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )
	# _.pr( extensionList )
	# sys.exit()



	# _.pr('done')
	# _.printVarSimple(woy_hash_table)

# datetime.datetime.fromtimestamp(epoch).strftime('%c')

if _.switches.isActive('mimeType'):
	import _rightThumb._mimetype as _mime

meta = True
if _.switches.isActive('NoMeta'):
	meta = False

omit = [ 'desktop.ini' ]
extensionList = []
folderCount = 0
fileCount = 0
data = []
i=0

woy_hash_table = {}
# gen_WOY_hash_table()
# sys.exit()
# saveFile

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)
	# _.pr(_v.appLogs())