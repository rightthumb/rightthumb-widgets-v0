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

import sys,time,os
from _rightThumb._hub import _construct as __
from _rightThumb._hub import app
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _func as _
reg = app.space(__name__, __file__)
app.reg = reg
reg.rent = app.register(reg)
app.rent=reg.rent
app.rent=app.rent
app.rent = app.focus(reg.rent)
app.switches()
app.tables()
def app_switches():

	pass

	app.switch.reg('Database', '-db,-database')
	app.switch.reg('Recursive', '-r,-recursive')
	app.switch.reg( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	app.switch.reg('Folder', '-folder')

	app.switch.reg('Count', '-c,-count,--c')
	# app.switch.reg('Path', '-p,-path,-folder')
	app.switch.reg('Text', '-t,-text,-txt')
	app.switch.reg('Binary', '-bin')
	app.switch.reg('Size', '-size',' g 10mb, L 2kb ')
	app.switch.reg('JSON', '-json')
	app.switch.reg('Ago', '-ago','1m cd, 1y, 1d')
	app.switch.reg('Time', '-time')
	app.switch.reg('Clean', '--c')
	app.switch.reg('CacheInfo', '-info')
	app.switch.reg('Cache', '-cache')
	app.switch.reg('Save', '-save')
	app.switch.reg('Totals', '-total,-totals')
	app.switch.reg('FolderRefine', '-fr')
	app.switch.reg('Duplicate', '-dup,-duplicates', 'bytes,epoch,filename OR (c,m,b,f,n) DAY')
	app.switch.reg('Hash', '-hash', 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256')
	app.switch.reg('mimeType', '-m,-mime')
	app.switch.reg('MovieTitle', '-movietitle')
	app.switch.reg('NameLength', '-nl,-namelength', '4 OR 4 L OR 3 g')
	app.switch.reg('ExtLength', '-el,-extlength', '4 OR 4 L OR 3 g')
	app.switch.reg('SuperDate', '-sdate,-superdate','older OR newer')
	app.switch.reg('NoMeta', '-nm,-nometa')
	app.switch.reg('Ago_by_Created', '-cago')
	app.switch.reg('Not', '-not,-invert')
	app.switch.reg('Extensions', '-ext', 'db image graphic video app audio doc script archive')
	app.switch.reg('Header', '-h,-header','5')
	app.switch.reg('PlusFile', '-pf,-pn,-plusfile')
	app.switch.reg('Group>=', '-,++g', '2' )
	app.switch.reg('Group<=', '-,--g', '2' )
	# app.switch.reg('WOYCreatedDate', '-cwoy')

	# Recursive Extensions Files Folder Text Binary Size Ago Save 
	# Cache FolderRefine Duplicate Hash mimeType MovieTitle

app.autoBackupData = True
app.isRequired_Pipe = False
app.isRequired_Pipe_or_File = False
# app.isRequired_or_List = ['Pipe','Files','Plus']

reg.documentation = {
	'file': 'ls.py',
	'liveAppName': app.this_app( __file__ ),
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
						{ 'name': 'name', 'abbreviation': 'n', 'sort': '' },
						{ 'name': 'folder', 'abbreviation': 'f', 'sort': '' },
						{ 'name': 'bytes', 'abbreviation': 'b', 'sort': '' },
						{ 'name': 'size', 'abbreviation': 's', 'sort': 'bytes' },
						{ 'name': 'size', 'abbreviation': 'size', 'sort': 'bytes' },
						{ 'name': 'md5', 'abbreviation': '5', 'sort': '' },
						{ 'name': 'ext', 'abbreviation': 'e', 'sort': '' },
						{ 'name': 'year', 'abbreviation': 'y', 'sort': 'date_modified_raw' },
						{ 'name': 'date_modified', 'abbreviation': 'md,dm', 'sort': 'date_modified_raw' },
						{ 'name': 'date_created', 'abbreviation': 'cd,dc', 'sort': 'date_created_raw' },
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

reg.data = {
	'start': app.start_time,
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

def sw( argvProcessForce=False ):
	global appDBA
	if True:

		if not __name__ == '__main__':
			app.argv_process = argvProcessForce
		else:
			app.argv_process = True

		app.load()
	app.construct_registration( reg.documentation['file'],app.rent )
	app_switches()

	app.myFileLocation_Print = False
	# app.switch.trigger( 'Files', app.myFileLocations )
	app.switch.trigger( 'Folder', app.myFolderLocations )
	# app.switch.trigger( 'URL', app.urlTrigger )
	# app.switch.trigger( 'Size', unFormatSize )
	# # app.switch.trigger( 'Save', save_trigger )
	
	
	
	app.default_script_triggers()
	# app.autoAbbreviations()
	app.switch.process()
if not __name__ == '__main__':
	app.argv_process = False
else:
	app.argv_process = True

sw()
def field_set( switchName, switchField, switchValue, rent=False ):
	if not type( rent ) == bool:
		rent = rent
	app.switch.field_set( switchName, switchField, switchValue, rent )
if __name__ == '__main__':
	if not sys.stdin.isatty():
		app.set_pipe_data( sys.stdin.readlines(), app.rent )
app.post_load( __file__ )

########################################################################################
# START
if app.switch.isActive('Column') and len(app.switch.value('Column')) and 'header' in app.switch.values('Column'):
	if not app.switch.isActive('Header'): 
		app.switch.field_set( 'Header', 'active', True )

import _rightThumb._dir as _dir
if app.switch.isActive('Header'):
	if not len(app.switch.value('Header')):
		_dir.header = 5
	else:
		if app.switch.value('Header') == 'all':
			app.switch.field_set( 'Long', 'active', True )
			_dir.header = True
		else:
			_dir.header = int(app.switch.value('Header'))

if app.switch.isActive('Ago_by_Created'):
	_dir.dateCalcByModified = False
	if not app.switch.isActive('Sort') and not app.switch.isActive('GroupBy'):
		app.switch.field_set( 'Sort', 'active', True )
		app.switch.field_set( 'Sort', 'value', 'date_created_raw' )
		app.switch.field_set( 'Sort', 'values', ['date_created_raw'] )
		app.switch.field_set( 'GroupBy', 'active', True )
		app.switch.field_set( 'GroupBy', 'value', 'ago' )
		app.switch.field_set( 'GroupBy', 'values', ['ago'] )

	# if not app.switch.isActive('GroupBy'):
		# app.switch.field_set( 'Sort', 'active', True )
		# WEEK OF YEAR
	#     date_modified_raw

	# print('cwoy ')

def movieTitle(pipeData):
	theResult = pipeData
	def clean( p ):
		p = p.replace('\n','')
		p = p.replace('\r','')
		p = p.replace('\t','')
		p = _str.replaceDuplicate(p,' ')
		p = _str.cleanBE(p,' ')
		# dots = p.split('.')
		# print(dots[len(dots)-1])
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
		# print(line.encode('ascii'))
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

			# print( record )
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
		# print( ( p ) )
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
		# print( line )
		if len(line) > 0 and not 'sample' in line:
			if dataType == 'filename':
				result.append(line)
			else:
				result.append( { 'title': line, 'folder': p['folder'], 'file': p['name'], 'mod': p['date_modified_raw'], 'bytes': p['bytes'] } )
	if dataType == 'filename':
		for res in  set(result):
			if app.switch.isActive('JustVar'):
				theTitle = res.title()
			else:
				theResult = res.title()
	else:
		for res in  (result):
			if app.switch.isActive('JustVar'):
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

	if app.switch.isActive('Minus'):
		if not app.showLine(folder):
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
		if app.switch.isActive('Files'):
			dirList = app.switch.values('Files')
			# print( dirList )
		for item in dirList:
			if not app.switch.isActive('Files'):
				path = folder + _v.slash + item
				path = path.replace(_v.slash+_v.slash,_v.slash)
			else:
				path = item
			if os.path.isfile(path):
				fileCount += 1
				if app.switch.isActive('PlusFile'):
					sL = app.showLine(item)
				else:
					sL = app.showLine(path)
				sL = True
				if app.switch.isActive('NameLength'): # ExtLength
					sL = True
				if app.switch.isActive('ExtLength'): # ExtLength
					sL = True
				if sL:
					shouldPrint = True

					if shouldPrint:
						addFile( path )

			if os.path.isdir(path) and app.switch.isActive('Recursive'):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):

					shouldRun = True
					if app.switch.isActive('FolderRefine'):
						sL = app.showLine(newFolder)
						if app.switch.isActive('NameLength'): # ExtLength
							sL = True
						if app.switch.isActive('ExtLength'): # ExtLength
							sL = True
						if not sL:
							shouldRun = False
					if shouldRun:

						try:
							getFolder(newFolder)
						except Exception as e:
							pass
				else:
					print('error')

def process( path ):
	global data
	global fileCount
	global i
	if os.path.isfile(path):
		fileCount += 1
		sL = app.showLine(path)
		if app.switch.isActive('NameLength'): # ExtLength
			sL = True
		if app.switch.isActive('ExtLength'): # ExtLength
			sL = True
		if sL:
			shouldPrint = True

			if shouldPrint:
				shouldPrint = False
				addFile( path )

def addFile( path, hasData=False ):
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
		record = _dir.fileInfo( path, sdate=app.sdate, meta=meta )
		# record['modified'] = _.friendlyDate( record['me'] )
	if type(record) == bool:
		error = ''
		try:
			_dir.fileInfo(path,err=True)
		except Exception as e:
			error = e
		print( 'Error:', os.path.isfile(path),path, error, '\n________________________\n' )

		return None
	
	if app.switch.isActive('PlusFile'):
		sL = app.showLine( record['name'] )
	else:
		sL = app.showLine( record['path'] )
	if app.switch.isActive('NameLength'): # ExtLength
		sL = True
	if app.switch.isActive('ExtLength'): # ExtLength
		sL = True
	if not sL:
		return None

	if record['name'].lower() in omit:
		return None

	if app.switch.isActive('Size'):
		shouldPrint = False
		shouldPrint_2 = False
		# stat = os.stat(path)
		# size = stat.st_size
		size = record['bytes']
		# print( app.switch.values('Size') )
		# sys.exit()
		if 'l' in app.switch.values('Size')[0]:
			if size < app.switch.values('Size')[1]:
				shouldPrint_2 = True
		if 'g' in app.switch.values('Size')[0]:
			if size > app.switch.values('Size')[1]:
				shouldPrint_2 = True

	if shouldPrint_2:
		shouldPrint = False
		if app.switch.isActive('Extensions'):
			
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

			if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
				i = i + 1
				shouldPrint = True
			else:
				if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(record['path']) == True :
					# print(isText(record['path']))
					i = i + 1
					shouldPrint = True
				elif not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
					i = i + 1
					shouldPrint = True
				elif not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(record['path']) == True:
					i = i + 1
					shouldPrint = True
				elif not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
					i = i + 1
					shouldPrint = True

	shouldAdd = shouldPrint
	if shouldAdd:
		if app.switch.isActive('Ago'):

			shouldAdd = False
			run = 'default'

			if len( app.switch.values('Ago') ) > 2:
				if 'a' in app.switch.values('Ago')[2]:
					run = 'a'
				elif 'md' in app.switch.values('Ago')[2]:
					run = 'md'
				elif 'cd' in app.switch.values('Ago')[2]:
					run = 'cd'
				elif 'resent' in app.switch.values('Ago')[2]:
					run = 'resent'
				elif 'm' in app.switch.values('Ago')[2]:
					run = 'md'
				elif 'c' in app.switch.values('Ago')[2]:
					run = 'cd'

			elif len( app.switch.values('Ago') ) > 1 and type(app.switch.values('Ago')[1]) == str:
				# print('asdf')
				if 'a' in app.switch.values('Ago')[1]:
					run = 'a'
				elif 'md' in app.switch.values('Ago')[1]:
					run = 'md'
				elif 'cd' in app.switch.values('Ago')[1]:
					run = 'cd'
				elif 'resent' in app.switch.values('Ago')[1]:
					run = 'resent'
				elif 'm' in app.switch.values('Ago')[1]:
					run = 'md'
				elif 'c' in app.switch.values('Ago')[1]:
					run = 'cd'

			# print(  len( app.switch.values('Ago') )  )
			# print(  ( app.switch.values('Ago') )  )
			# sys.exit()
			# accessed_raw

			agoRange = False
			if len( app.switch.values('Ago') ) > 1 and type(app.switch.values('Ago')[1]) == float:
				agoRange = True

			# print(  'agoRange', agoRange  )

			if not agoRange:
				if run == 'default':
					# print(record['date_modified_raw'])
					# print(app.switch.values('Ago'))
					if record['date_modified_raw'] > app.switch.values('Ago')[0] or record['date_created_raw'] > app.switch.values('Ago')[0]:
						shouldAdd = True
				elif run == 'resent':
					if record['date_modified_raw'] > app.switch.values('Ago')[0] or record['date_created_raw'] > app.switch.values('Ago')[0] or record['accessed_raw'] > app.switch.values('Ago')[0]:
						shouldAdd = True
				elif run == 'a':
					if record['accessed_raw'] > app.switch.values('Ago')[0]:
						# print( _.friendlyDate(app.switch.values('Ago')[0]), app.switch.values('Ago')[0], record['accessed_raw'], _.friendlyDate(record['accessed_raw']) )
						shouldAdd = True
				elif run == 'cd':
					if record['date_created_raw'] > app.switch.values('Ago')[0]:
						shouldAdd = True
				elif run == 'md':
					if record['date_modified_raw'] > app.switch.values('Ago')[0]:
						shouldAdd = True
			elif agoRange:
				if run == 'default':
					# print(record['date_modified_raw'])
					# print(app.switch.values('Ago'))
					if record['date_modified_raw'] < app.switch.values('Ago')[0] or record['date_created_raw'] < app.switch.values('Ago')[0]:
						if record['date_modified_raw'] > app.switch.values('Ago')[1] or record['date_created_raw'] > app.switch.values('Ago')[1]:
							shouldAdd = True
				elif run == 'resent':
					if record['date_modified_raw'] < app.switch.values('Ago')[0] or record['date_created_raw'] < app.switch.values('Ago')[0] or record['accessed_raw'] < app.switch.values('Ago')[0]:
						if record['date_modified_raw'] > app.switch.values('Ago')[1] or record['date_created_raw'] > app.switch.values('Ago')[1] or record['accessed_raw'] > app.switch.values('Ago')[1]:
							shouldAdd = True
				elif run == 'a':
					if record['accessed_raw'] < app.switch.values('Ago')[0]:
						if record['accessed_raw'] > app.switch.values('Ago')[1]:
							shouldAdd = True
				elif run == 'cd':
					if record['date_created_raw'] < app.switch.values('Ago')[0]:
						if record['date_created_raw'] > app.switch.values('Ago')[1]:
							shouldAdd = True
				elif run == 'md':
					if record['date_modified_raw'] < app.switch.values('Ago')[0]:
						if record['date_modified_raw'] > app.switch.values('Ago')[1]:
							shouldAdd = True
	if app.switch.isActive('Not'):
		if shouldAdd:
			shouldAdd = False
		else:
			shouldAdd = True

	if shouldAdd:

		if app.switch.isActive('MovieTitle'):
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
		if app.switch.isActive('Database'):
			_dir.fileInfo( path, sql=True, insert=True, sdate=app.sdate, meta=meta )
			# record['modified'] = _.friendlyDate( record['me'] )
		else:
			if not record is None:
				data.append(  record  )
			else:
				data.append(  _dir.fileInfo( path, sdate=app.sdate, meta=meta )  )

def action():

	if app.switch.isActive('Group>='):
		g = app.switch.values('Group>=')[0]
		s = str(app.size_group_size(g))
		app.switch.field_set( 'Size', 'active', True )
		app.switch.field_set( 'Size', 'value', 'g,'+s )
		app.switch.field_set( 'Size', 'values', ['g',s] )

	if app.switch.isActive('Group<='):
		g = app.switch.values('Group<=')[0]
		s = str(app.size_group_size(g))
		# print( g,s )
		app.switch.field_set( 'Size', 'active', True )
		app.switch.field_set( 'Size', 'value', 'l,'+s )
		app.switch.field_set( 'Size', 'values', ['l',s] )

	global i
	global data
	global fileCount
	global folderCount
	global _mime
	global meta

	isLegacy = False
	# load()
	start = time.time()
	if app.switch.isActive('Text') or app.switch.isActive('Binary'):
		import _rightThumb._mimetype as _mime

	if app.switch.isActive('Extensions') or app.switch.isActive('MovieTitle'):
		if app.switch.isActive('MovieTitle'):
			app.switch.field_set( 'Extensions', 'values', ['video'] )
		extensionsDatabank()
	if not type( reg.data['pipe'] ) == bool:
		app.pipeCleaner(0)
		app.switch.field_set( 'Files', 'active', True )
		app.switch.field_set( 'Files', 'values', reg.data['pipe'] )
		app.switch.field_set( 'Files', 'value', ','.join(reg.data['pipe']) )
		# print( app.switch.values('Files') )

	if app.switch.isActive('Files') and app.switch.isActive('JSON'):
		records = []
		for file in app.switch.values('Files'):
			records.append( _dir.info( file, sdate=app.sdate, meta=meta ) )
		app.printVarSimple( records )
		sys.exit()
	if app.switch.isActive('Database'):
		db = app.switch.value('Database')
		if not len(db):
			db = '_DIR_' + _.fileDate( time.time() ) + 'app.db'
		_dir.sqlCreateTable( db , delete=True )

	# if not type( reg.data['pipe'] ) == bool:
	#     app.pipeCleaner(0)
	#     # app.printVar( app.appData )
	#     for i,row in enumerate( reg.data['pipe'] ):
	#         print( row )
	#         process( row )

	else:
		if app.switch.isActive('Folder'):
			folder = app.switch.values('Folder')[0]
		else: 
			folder = os.getcwd()
 
		
		if app.switch.isActive('Cache') or ( app.switch.isActive('LoadEpoch') and not app.payload_cache is None ):
			app.switch.field_set( 'Cache', 'active', True )
			if app.switch.isActive('LoadEpoch'):
				dataCache = app.payload_cache
			else:
				dataCache = app.getTable2( app.switch.values('Cache')[0] )

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

			if app.switch.isActive('CacheInfo'):

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
						

				app.printVarSimple( dataCache )
				sys.exit()

			# {
			#     'folder': folder,
			#     'folders': folderCount,
			#     'files': fileCount,
			#     'data': data,
			# }

			for x in dataCacheX:
				# print(x)
				addFile( x, hasData=True )
		else:
			getFolder(folder)

	# if app.switch.isActive('Sort'): data = app.table.returnSorted( 'data', app.switch.value('Sort'), data );

	if app.switch.isActive('Database'):
		_dir.commit()
		app.cp( [ '\nDatabase Created' ], 'green' )
		app.cp( [ '\t', db ], 'yellow' )
		end = time.time()
	else:
		end = time.time()
		# if app.switch.isActive('Ago'):
		#     newData = []
		#     ago = app.switch.value('Ago')
		#     for record in data:
		#         if record['date_modified_raw'] < ago:
		#             newData.append( record )
		#     data = newData

		if app.switch.isActive('JSON'):
			# for x in data[0].keys():
			#     print(x)
			# sys.exit()
			app.printVarSimple( data )
		else:

			pass

			if not i == len(data):
				i = len(data)
			if not i == fileCount:
			# if not len(files) == i:
				# print('HERE')
				app.folderProfileAttribute( folder=folder, info = {
																'app': 'ls',
																'recursive': app.switch.isActive('Recursive'),
																'factors': {
																				'Text': app.switch.isActive('Text'),
																				'Binary': app.switch.isActive('Binary'),
																				'Extensions': app.switch.isActive('Extensions'),
																				'Type': app.switch.values('Extensions'),

																				'PlusOr': app.switch.isActive('PlusOr'),
																				'PlusClose': app.switch.isActive('PlusClose'),
																				'Ago': app.switch.isActive('Ago'),
																				'Plus': app.switch.isActive('Plus'),
																				'Minus': app.switch.isActive('Minus'),

																				'AgoVals': app.switch.values('Ago'),
																				'PlusVals': app.switch.values('Plus'),
																				'MinusVals': app.switch.values('Minus'),
																},
																'percentage': app.pDiff( fileCount, i, use='less' ),
																'count': i,
																'files': fileCount ,

				} )

			if app.switch.isActive('mimeType'):
				for i,record in enumerate(data):
					data[i]['mime'] = _mime.what( record['path'] )

			if app.switch.isActive('Hash'):
				import _rightThumb._md5 as _hash
				hashes = 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256'

				for i,record in enumerate(data):

					for h in hashes.split(' '):
						if h in app.switch.values('Hash'):
							data[i][h] = _hash.file( record['path'], h=h )
			# Cache FolderRefine Duplicate Hash mimeType MovieTitle
			saveFile = {
								'isLegacy':    False,
								'switches': {
									'active': [],
									'isActive': {},
									'values': {},
								},
								'folder': folder,
								'folders': folderCount,
								'files': fileCount,
								'data': data,
			}
			
			saveFile['switches'] = app.switch.records('dic_a-v')

			app.payload_cache( saveFile )
			

			if app.switch.isActive('Save'):
				# print(saveFile)
				# print(app.switch.values('Save')[0])
				print( 'Saved:', app.switch.values('Save')[0] )
				app.saveTable2( saveFile, app.switch.values('Save')[0] )

			elif not app.switch.isActive('Save'):

				if app.switch.isActive('Duplicate'):
					if app.switch.value('Duplicate') == '':
						keyType = 'bytes,epoch'
					else:
						keyType = app.switch.value('Duplicate').lower()
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
							# app.printTest(record)
							key += str(record['name'])
						if 'test0' in keyType:
							print(key)
						if key in table:
							table[key].append(i)
							if not key in duplicates:
								duplicates.append(key)
						else:
							table[key] = []
							table[key].append(i)

					pass
					if app.switch.isActive( 'GroupBy' ):
						keyType+='test11'
					for key in duplicates:
						print()
						if 'test1' in keyType:
							keyP = key
							if 'test11' in keyType:
								keyP = keyP.replace( '*', '' )
							print(keyP)
							print()
						for i in table[key]:
							# print(i)
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
								print( day, data[i]['path'] )
							else:
								print( day+data[i]['path'] )

					return None

				# if len(data) == 1:
					# app.printVarSimple( data )

				# app.switch.field_set( 'Long', 'active', True )

				# if app.switch.isActive('Sort'): data = app.table.returnSorted( 'data', app.switch.value('Sort'), data );

				if app.switch.isActive('NameLength'): # ExtLength
					if len(app.switch.value('NameLength')):
						ln = len(app.switch.values('NameLength'))
						length = int( app.switch.values('NameLength')[0] )
						op = '=='
						if ln > 1:
							if 'g' in app.switch.values('NameLength')[1].lower():
								op = '>='
							elif 'l' in app.switch.values('NameLength')[1].lower():
								op = '<='
						nw = []
						for record in data:
							# if True:
							if app.showLine(record['name']):
								if len(record['ext']):
									nN = record['name'][0:len(record['name'])-len(record['ext'])-1]
									fL = len(nN)
									# print( nN, record['name'], record['ext'], length, op, fL )
									# print( length, op, fL )
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
										# print( nN, record['name'], record['ext'], length, op, fL )
										record['length'] = fL
										nw.append(record)

						data = nw

				# ExtLength
				if app.switch.isActive('ExtLength'):
					if len(app.switch.value('ExtLength')):
						ln = len(app.switch.values('ExtLength'))
						length = int( app.switch.values('ExtLength')[0] )
						op = '=='
						if ln > 1:
							if 'g' in app.switch.values('ExtLength')[1].lower():
								op = '>='
							elif 'l' in app.switch.values('ExtLength')[1].lower():
								op = '<='
						nw = []
						for record in data:
							if app.showLine(record['ext']):
								nN = record['ext']
								fL = len(nN)
								# print( nN, record['name'], record['ext'], length, op, fL )
								# print( length, op, fL )
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
									# print( nN, record['name'], record['ext'], length, op, fL )
									record['length'] = fL
									nw.append(record)

						data = nw
				app.table.register( 'data', data, w=1 )
				# app.table.fieldProfileSet( 'data', 'week_of_year', 'trigger', app.woyTrigger )
				app.table.fieldProfileSet( 'data', 'meta.epoch.me', 'trigger', _.friendlyDate )
				app.table.fieldProfileSet( 'data', 'meta.epoch.ae', 'trigger', _.friendlyDate )
				app.table.fieldProfileSet( 'data', 'meta.epoch.ce', 'trigger', _.friendlyDate )
				# print('here')
				# app.table.fieldProfileSet( 'data', 'week_of_year', 'trigger', app.woyTrigger )
				# app.table.fieldProfileSet( 'data', '_header_', 'alignment', 'left' )
				# app.table.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
				# app.table.fieldProfileSet('data','phone,email,address','alignment','center')

				if not app.switch.isActive('Sort') and not app.switch.isActive('GroupBy') and not app.switch.isActive('Column'):
					if not app.switch.isActive('Files'):
						app.switch.field_set( 'GroupBy', 'active', True )
						if app.switch.isActive('mimeType'):
							app.switch.field_set( 'GroupBy', 'value', 'mime,ext,ago' )
							app.switch.field_set( 'GroupBy', 'values', ['mime','ext','ago'] )
						else:
							app.switch.field_set( 'GroupBy', 'value', 'ext,ago' )
							app.switch.field_set( 'GroupBy', 'values', ['ext','ago'] )
					# app.switch.field_set( 'Sort', 'active', True )
					# app.switch.field_set( 'Sort', 'value', 'ext' )
					# app.switch.field_set( 'Sort', 'value', 'ext,week_of_year' )
					# app.switch.field_set( 'Sort', 'values', ['ext','week_of_year'] )

				if not app.switch.isActive('Long') and not app.switch.isActive('Length') and not app.switch.isActive('Short'):
					app.switch.field_set( 'Length', 'active', True )
					app.switch.field_set( 'Length', 'value', '50' )
					app.switch.field_set( 'Length', 'values', ['50'] )
				if app.switch.isActive('Column'):
					if len( app.switch.values('Column') ) > 1:
						if not app.switch.isActive('Totals'):
							app.table.print( 'data', ','.join(app.switch.values('Column')) )
					else:
						# if not app.switch.isActive('Files') and not app.switch.isActive('Recursive'):
						if not app.switch.isActive('Files'):
							app.switch.field_set( 'Long', 'active', True )
							app.switch.field_set( 'GroupBy', 'active', False )
							app.switch.field_set( 'GroupBy', 'value', '' )
							if not app.switch.isActive('Sort'):
								app.switch.field_set( 'Sort', 'active', True )
								app.switch.field_set( 'Sort', 'value', app.switch.value('Column') )
								app.switch.field_set( 'Sort', 'values', app.switch.values('Column') )
							if not app.switch.isActive('Totals'):
								app.table.print( 'data', ','.join( app.switch.values('Column') ) )

						else:
							app.switch.field_set( 'Sort', 'active', True )
							app.switch.field_set( 'Sort', 'value', app.switch.value('Column') )
							app.switch.field_set( 'Sort', 'values', app.switch.values('Column') )
							if not app.switch.isActive('Totals'):
								app.table.print( 'data', ','.join( app.switch.values('Column') ) )
				elif not app.switch.isActive('Column'):
					
					if app.switch.isActive('Files') or app.switch.isActive('Recursive') or app.switch.isActive('Cache'):
						app.switch.field_set( 'GroupBy', 'active', True )
						GroupBy = ['folder']
						app.switch.field_set( 'GroupBy', 'value', ','.join(GroupBy) )
						app.switch.field_set( 'GroupBy', 'values', GroupBy )
						app.switch.field_set( 'Sort', 'active', True )
						# app.switch.field_set( 'Sort', 'value', 'folder,d.bytes' )
						app.switch.field_set( 'Sort', 'value', 'folder,d.date_modified_raw' )
						if not app.switch.isActive('Totals'):
							theColumns = 'folder,size,name,date_modified,date_created,date_accessed'
							if isLegacy:
								theColumns = theColumns.replace( ',date_accessed', '' )
							if len(data) and not 'date_accessed' in list(data[0].keys()):
								theColumns = theColumns.replace( ',date_accessed', '' )
							

							theColumns = theColumns.replace( ',date_accessed', '' )
							app.table.print( 'data', app.unix_auto_columns( data, theColumns, reg.rent ) )

					else:
						if not app.switch.isActive('Totals'):
							if app.switch.isActive('mimeType'):
								theColumns = 'mime,ext,ago,name,size,date_modified,date_created,date_accessed'
							else:
								theColumns = 'ext,ago,name,size,date_modified,date_created,date_accessed'
							if isLegacy:
								theColumns = theColumns.replace( ',date_accessed', '' )

							theColumns = theColumns.replace( ',date_accessed', '' )
							app.table.print( 'data', app.unix_auto_columns( data, theColumns, reg.rent ) )
							
					pass

				pass
			if not app.switch.isActive('Clean'):
				print()

				
				totalBytes = 0

				for record in data:
					try:
						totalBytes += record['bytes']
					except Exception as e:
						pass

				if i == fileCount:
					# app.cp(  [  '\t', i, 'files' , _.formatSize( totalBytes ), 'in', folderCount, 'folders' ], 'green'  )
					txt = '\t '
					txt += app.cp(  [  app.addComma(i), 'files '  ], 'yellow', p=0 )
					txt += app.cp(  [  _.formatSize( totalBytes ) ], 'green', p=0 )
					txt += ' in '
					txt += app.cp(  [  app.addComma(folderCount) + ' folders' ], 'blue', p=0 )
					print( txt )
				else:
					txt = '\t ' + app.addComma(fileCount) + ' total files '
					txt += app.cp(  [  app.addComma(i), 'selected '  ], 'yellow', p=0 )
					txt += app.cp(  [  _.formatSize( totalBytes ) ], 'green', p=0 )
					txt += ' in '
					txt += app.cp(  [  app.addComma(folderCount) + ' folders' ], 'blue', p=0 )
					print( txt )
				print()
				endPrint = time.time()
				if app.switch.isActive('Time'):
					app.cp( [ 'App Time:', round( end-start, 3 ) ], 'yellow' )
					app.cp( [ 'Print Time:', round( endPrint-end, 3 ) ], 'yellow' )
					app.cp( [ 'Total Time:', round( endPrint-start, 3 ) ], 'yellow' )
# EXT                  WEEK OF YEAR    DATE MODIFIED          NAME                                                     SIZE
# app.printVar( _dir.fileInfo( path ) )

# def load():
#     global data
#     data = app.getTable( 'table' )

# test
# test
# test
# test
# test
# test

app.sdate = None
if app.switch.isActive('SuperDate'):
	app.sdate = app.switch.values('SuperDate')[0]
def extensionsDatabank():
	global extensionList
	extensionList = []
	_db = app.regImp( app.rent, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )

	for index in app.switch.values('Extensions'):
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )
	# print( extensionList )
	# sys.exit()

	# print('done')
	# app.printVarSimple(woy_hash_table)

# datetime.datetime.fromtimestamp(epoch).strftime('%c')

if app.switch.isActive('mimeType'):
	import _rightThumb._mimetype as _mime

meta = True
if app.switch.isActive('NoMeta'):
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
	action()
	# print(_v.appLogs())




