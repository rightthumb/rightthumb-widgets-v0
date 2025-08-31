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
import _rightThumb._mimetype as _mime
##################################################

__.isFiles=False


def appSwitches():
	if not __.isFiles:
		_.switches.register('Not-Recursive', '--r')
		_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Folders', '-f,-folder,-folders,-fo')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('Totals', '-total,-totals')
	_.switches.register('FolderRefine', '-fr')
	_.switches.register('Ago', '-ago', '1m')
	_.switches.register('MaxDepth', '-depth', '3')
	_.switches.register('Extensions', '-ext', 'db image graphic video app audio doc script archive')
	_.switches.register('Toggle-Relative-Path', '-rr')
	_.switches.register('Widget-V0', '-w,-v0')
	_.switches.register('Ago-Create-Date', '-cd')
	_.switches.register('Search-For-Text-Include', '-has,-search')
	_.switches.register('Search-For-Text-Exclude', '-not')
	_.switches.register('Search-Print-Line', '-p,-print','all')
	_.switches.register('No-Extension', '-noext')


fse=False
def fs(data):
	global fse
	if 'flag:' in data:
		return None

	if not __.isFiles:
		if 'flag: stop' in data:
			fse=True
			return None
		if 'flag: start' in data:
			fse=False
			return None
		if fse:
			return None
	if not __.isFiles:
		data = data.replace('files','file')
	if __.isFiles:
		data = ' '+data+' '
		data = data.replace('-recursive','')
		data = data.replace('-r ','')
		if data.startswith(' '):
			data = data[1:]
		if data.endswith(' '):
			data = data[:-1]

	return data


_.appInfo[focus()] = {
	'file': 'files.py',
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
						fs('p files --c '),
						fs('p files -text '),
						fs(''),
						fs('p files -size L 2mb'),
						fs('p files -size g 2mb --c -folder D:\\techApps\\Python\\Python36-32'+_v.slash),
						fs(''),
						fs('b pp'),
						fs('p files + *.py *.bat *.sh *.js *.htm* *.php  -or -totals'),
						fs(''),
						fs('p files -ext db - *.json *.dat'),
						fs('flag: stop'),
						fs('p files -w --c -ago 10h | p line --c -make "git add {}" | p -copy'),
						fs('p files -w --c -ago 10h | p line --c -make "git add {}" | p execute'),
						fs('p files -w --c -ago 10h'),
						fs('flag: start'),
						fs('p files - /bin /boot /dev /lib /lib64 /lost+found /media /mnt /proc /srv /sys -f / -r'),
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
	elif size > 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#   result = ''
	return result

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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	# _.switches.trigger( 'Minus' , _.ci )
	_.switches.trigger( 'Size' , unFormatSize )
	# _.switches.trigger( 'Folders' , _.bAlias )
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

def minusF():
	mi=_.switches.values('Minus')
	mii=[]
	for m in mi:
		m=_.ci2(m)
		mii.append(m)
	_.switches.fieldSet( 'Minus', 'values', mii )
	_.switches.fieldSet( 'Minus', 'value', ','.join(mii) )

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



def isText(file):
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result




def getFolder(folder,r=True):
	folder=folder.replace(os.sep+os.sep,os.sep)
	folder=folder.replace(os.sep+os.sep,os.sep)
	# if not _.isWin:
	#   for test in '/bin /boot /dev /lib /lib64 /lost+found /media /mnt /proc /srv /sys'.split(' '):
	#       if folder.startswith(test+'/'):
	#           return None
	#   if folder in '/bin /boot /dev /lib /lib64 /lost+found /media /mnt /proc /srv /sys'.split(' '):
	#       return None


	# if _.switches.isActive('Minus') and not _.showLine(folder,):
	#     return None
	

	if not sw(folder):
		# return None
		if not sw(os.getcwd()):
			# _.pr(os.getcwd(),folder)
			# _.pr(folder)
			pass
		elif not len(_.switches.value('Folders')):
			return None
		else:
			good=False
			for f in _.switches.values('Folders'):
				if not sw(f):
					good=True
			if not good:
				return None

	# _.pr(folder)


	global i
	global iS
	global baseDepth
	global base_path
	if _.switches.isActive('MaxDepth'):
		if len(_.switches.value('MaxDepth')):
			maxDepth = int(_.switches.values('MaxDepth')[0])
		else:
			maxDepth = 4
		if len( folder.split(_v.slash) ) - baseDepth >= maxDepth:
			if len(_.switches.values('MaxDepth')) > 1 and 'p' in _.switches.values('MaxDepth')[1]:
				_.pr( folder )

			return None
	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			record = None
			path = folder + _v.slash + item
			add(path,r)
def add(path,r=False):
	global i
	global iS
	global baseDepth
	global base_path
	path = path.replace(_v.slash+_v.slash,_v.slash)
	if os.path.isfile(path):
		pathX=path.replace(base_path,'')
		if pathX.startswith(os.sep): pathX=pathX[1:]
		
		# print(pathX)
		i = i + 1

		if _.showLine(path):
			shouldAdd = False

			if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
				# _.pr(0,whatIsIt(path),path)
				# _.pr(path)
				shouldAdd = True
			else:
				if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
					# _.pr(1,whatIsIt(path),path)
					# _.pr(path)
					shouldAdd = True
				if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
					# _.pr(2,whatIsIt(path),path)
					# _.pr(path)
					shouldAdd = True
				if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
					# _.pr(3,whatIsIt(path),path)
					# _.pr(path)
					shouldAdd = True
				if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
					# _.pr(4,whatIsIt(path),path)
					# _.pr(path)
					shouldAdd = True

			pass

			pass


			if _.switches.isActive('Ago'):
				# sys.exit()
				record = _dir.fileInfo( path )
				# _.pr( _.switches.values('Ago'), record['date_modified_raw'], record['date_created_raw'],  )
				# if os.path.isfile(path):
				shouldAdd = False
				run = 'default'
				if len( _.switches.values('Ago') ) > 2:
					if 'a' in _.switches.values('Ago')[2]:
						run = 'a'
					elif 'md' in _.switches.values('Ago')[2]:
						run = 'md'
					elif _.switches.isActive('Ago-Create-Date'):
						run = 'cd'
					elif 'resent' in _.switches.values('Ago')[2]:
						run = 'resent'
					elif 'm' in _.switches.values('Ago')[2]:
						run = 'md'


				elif len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == str:
					# _.pr('asdf')
					if 'a' in _.switches.values('Ago')[1]:
						run = 'a'
					elif 'md' in _.switches.values('Ago')[1]:
						run = 'md'
					elif _.switches.isActive('Ago-Create-Date'):
						run = 'cd'
					elif 'resent' in _.switches.values('Ago')[1]:
						run = 'resent'
					elif 'm' in _.switches.values('Ago')[1]:
						run = 'md'


				# _.pr(  len( _.switches.values('Ago') )  )
				# _.pr(  ( _.switches.values('Ago') )  )
				# sys.exit()
				# accessed_raw


				agoRange = False
				if len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == float:
					agoRange = True

				# _.pr( run, agoRange, _.switches.values('Ago')[0], _.friendlyDate(_.switches.values('Ago')[0]) )

				if not agoRange:
					if run == 'default':
						if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True
							# _.pr(path)
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
						if record['date_created_raw'] < _.switches.values('Ago')[0]:
							if record['date_created_raw'] > _.switches.values('Ago')[1]:
								shouldAdd = True
					elif run == 'md':
						if record['date_modified_raw'] < _.switches.values('Ago')[0]:
							if record['date_modified_raw'] > _.switches.values('Ago')[1]:
								shouldAdd = True



			pass

			pass
			# if shouldAdd: _.pr( 1001, path );
			if shouldAdd:
				if _.switches.isActive('Size'):
					shouldAdd = False
					shouldAdd_2 = False
					stat = os.stat(path)
					size = stat.st_size
					if 'l' in _.switches.values('Size')[0]:
						if size < _.switches.values('Size')[1]:
							shouldAdd_2 = True
					if 'g' in _.switches.values('Size')[0]:
						if size > _.switches.values('Size')[1]:
							shouldAdd_2 = True

					if shouldAdd_2:
						shouldAdd = False

						if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
							
							shouldAdd = True
						else:
							if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
								shouldAdd = True
							if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
								shouldAdd = True
							if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
								shouldAdd = True
							if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
								shouldAdd = True



					if shouldAdd:
						shouldAdd = False
						

						if _.switches.isActive('Count'):
							if not _.v.show_full_path:
								# process(pathX)
								process(path)
							else:
								process(path)
						else:
							iS+=1

							formatedSize = formatSize( size )
							formatedSize = _.fields.value( 'files', 'name', formatedSize )
							result = ''
							fs = formatedSize.split(' ')
							result += _.colorThis( fs[0], 'Color.purple', p=0 )
							result += ' '
							result += _.colorThis( fs[1], 'Color.darkcyan', p=0 )
							fs.reverse()
							fs.pop()
							fs.pop()
							fs.reverse()
							result += ' '.join(fs)
							result += '\t'
							if not _.v.show_full_path:
								result += _.colorThis( pathX, 'cyan', p=0 )
							else:
								result += _.colorThis( path, 'cyan', p=0 )

							_.pr( result )
						
						# _.pr( formatedSize, '\t', path )


			if shouldAdd :
				global extensionList
				try: record
				except Exception as ee: record = None
				if len( extensionList ):
					if record is None:
						record = _dir.info( path )
					if not len( record['ext'] ):
						shouldAdd = False
					else:
						record['ext'] = record['ext'].lower()
						if not '.'+record['ext'] in extensionList:
							shouldAdd = False

					# if '.' in path:
					#   pathy = path.lower().split('.')
					#   pathy_test = pathy.pop()
					#   if not '.'+pathy_test in extensionList:
					#       shouldAdd = False



			if shouldAdd:
				iS+=1
				if not _.switches.isActive('Totals'):
					if not _.v.show_full_path:
						if not _.switches.isActive('Plus'):
							# process(pathX)
							process(path)
						else:
							# process(pathX)
							process(path)
					else:
						if not _.switches.isActive('Plus'):
							process(path)
						else:
							process(path)


			# if shouldAdd:
			#   text_binary = False
			#   if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
			#       text_binary = True
			#   else:
			#       if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
			#           text_binary = True
			#       if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
			#           text_binary = True
			#       if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
			#           text_binary = True
			#       if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
			#           text_binary = True
			#   if not text_binary:
			#       shouldAdd = False


	# if os.path.isdir(path) and _.showLine(path):
	if os.path.isdir(path):
		newFolder = path
		if os.path.isdir(newFolder):
			shouldRun = True
			if _.switches.isActive('FolderRefine'):
				if not _.showLine(newFolder):
					shouldRun = False
			if r and shouldRun:
				if not _.switches.isActive('Not-Recursive'):
					try:
						getFolder(newFolder,r)
					except Exception as e:
						pass
		else:
			_.pr('error')







def extensionsDatabank():
	global extensionList
	extensionList = []
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )
	useDB=True
	for index in _.switches.values('Extensions'):
		if index.startswith('.'):
			useDB=False
			extensionList.append(index)
	if useDB:
		for index in _.switches.values('Extensions'):
			_db.switch( 'Plus', [index] )
			for i,x in enumerate(_db.do( 'action' )):
				x = x.replace('.','')
				if not x.startswith('.'):
					x = '.'+x
				if not x in extensionList:
					extensionList.append( x.lower() )

def action():
	_.v.no_extension = _.switches.isActive('No-Extension')
	if __.isFiles:
		_.v.show_full_path = True
		if _.switches.isActive('Toggle-Relative-Path'):_.v.show_full_path = False
	else:
		_.v.show_full_path = False
		if _.switches.isActive('Toggle-Relative-Path'): _.v.show_full_path = True
	if _.switches.isActive('Minus'): minusF()

	global base_path
	if _.switches.isActive('Extensions'): extensionsDatabank()
	if _.isData():
		base_path=''
		if _.switches.isActive('Toggle-Relative-Path'):
			fi0=_.isData()[0]
			err=0

			while True:
				try: fi0=__.path(fi0,pop=True)
				except Exception as ee: err=1; break;
				good=True
				for path in _.isData():

					if not path.lower().startswith(fi0.lower()) and os.path.isfile(path):
						print(fi0,path,path.lower().startswith(fi0.lower()))
						good=False; break;
				if not os.sep in fi0 or fi0 == os.sep:
					err=1; break;
				if good:
					base_path=fi0
					break
			if base_path: _.v.show_full_path = False
		for path in _.isData():
			if os.path.isfile(path):
				add(path)
	
	elif not _.isData():
		if not __.isFiles:
			r = _.switches.isActive('Recursive')

		else:
			r = True



		_.fields.register( 'files', 'name', '1000.43 KB' )
		global i
		global iS
		global infile
		global scan
		# load()
		if _.switches.isActive('Folders') == False:
			folder = os.getcwd()
		else:
			folder = _.switches.value('Folders')
		global baseDepth
		# global base_path
		baseDepth = len( folder.split(_v.slash) )
		base_path=folder
		if not _.switches.isActive('Widget-V0'):
			getFolder(folder,r=r)
		else:
			# _.pr(_v.ww)
			# _.pr(_v.widgets)
			# _.pr(_v.w)
			base_path=_v.widgets
			_.switches.fieldSet( 'Toggle-Relative-Path', 'active', True )
			_.switches.fieldSet( 'Minus', 'active', True )
			_.switches.fieldSet( 'Minus', 'value', 'minecraft.py,vps-' )
			_.switches.fieldSet( 'Minus', 'values', ['minecraft.py','vps-'] )
			_.switches.fieldSet( 'Plus', 'active', True )
			_.switches.fieldSet( 'Plus', 'value', '*.py,*.sh,*.bat,*.MD' )
			_.switches.fieldSet( 'Plus', 'values', ['*.py','*.sh','*.bat','*.MD'] )
			_.switches.fieldSet( 'PlusOr', 'active', True )
			getFolder(_v.ww+os.sep+'python')
			getFolder(_v.ww+os.sep+'batch', r=False)
			getFolder(_v.ww+os.sep+'powershell', r=False)
			getFolder(_v.ww+os.sep+'php', r=False)
			getFolder(_v.ww+os.sep+'windows')
			getFolder(_v.ww+os.sep+'bash')
			getFolder(_v.widgets+os.sep+'install')
			getFolder(_v.widgets, r=False)
		
		"""
		if _.switches.isActive('Extensions'):
			folderProfileAttribute( folder=folder, info={
															'recursive': True,
															'count': iS,
															'files': i ,
															'diff': _.pDiff( iS, i, use='less' ) ,
			} )
		"""
		if not iS == i:
			_.folderProfileAttribute( folder=folder, info = {
															'app': 'files',
															'recursive': r,
															'factors': {
																			'Text': _.switches.isActive('Text'),
																			'Binary': _.switches.isActive('Binary'),
																			'Extensions': _.switches.isActive('Extensions'),
																			'Type': _.switches.values('Extensions'),

																			'PlusOr': _.switches.isActive('PlusOr'),
																			'PlusClose': _.switches.isActive('PlusClose'),
																			'Plus': _.switches.isActive('Plus'),
																			'Minus': _.switches.isActive('Minus'),
																			
																			'PlusVals': _.switches.values('Plus'),
																			'MinusVals': _.switches.values('Minus'),
															},
															'percentage': _.pDiff( iS, i, use='less' ),
															'count': iS,
															'files': i,

			} )

	if _.switches.isActive('Count') == False:
		if not scan:
			if not i == iS:
			# if _.switches.isActive('Size'):
				_.colorThis( [  '\n', _.addComma(iS), 'of', _.addComma(i), '\n'  ], 'yellow' )
			else:
				_.colorThis( [  '\n{}\n'.format( _.addComma(i) )  ], 'yellow' )
		elif scan:
			if not i == iS:
			# if _.switches.isActive('Size'):
				_.colorThis( [  '\n','in', _.addComma(infile), 'subset', _.addComma(iS), 'of', _.addComma(i), '\n'  ], 'yellow' )
			else:
				_.colorThis( [  '\n','in', _.addComma(infile), 'of', _.addComma(i), '\n'  ], 'yellow' )
		# _.pr('\n{}\n'.format(i))

extensionList = []

i = 0
iS = 0
baseDepth = 0

if _.switches.isActive('Search-For-Text-Include'):
	scan=True
else:
	scan=False

if not _.switches.isActive('Search-Print-Line'):
	pr=0
elif 'a' in _.switches.value('Search-Print-Line').lower():
	pr=2
else:
	pr=1

inc=_.switches.values('Search-For-Text-Include')
ex=_.switches.values('Search-For-Text-Exclude')
infile=0

def process3(path):
	pass

spent=[]

def printer(path,ni=0):
	global spent
	global infile
	global base_path
	if _.isWin:
		p = path.lower()
	else:
		p=path
	if p in spent:
		return None
	spent.append(p)
	if not _.v.show_full_path:
		path=path.replace(base_path,'')
		if path.startswith(os.sep): path=path[1:]

		if _.v.no_extension and '.' in path:
			path=path[:-len(path.split('.')[-1])-1]


	_.pr( _.colorThis( path, 'cyan', p=0 ) )
	infile+=1

def process(path):
	if not os.path.isfile(path):
		return path
	# _.pr(path)
	# char = chardet.detect(open( path, 'rb' ).read(200))['encoding']\
	char='utf-8'
	char='iso-8859-1'
	# _.pr(char)
	global scan
	global pr
	global inc
	global ex
	if not scan:
		printer(path)
		return path
	else:
		i=0
		if len(inc) == 1 and not len(ex):
			fast=True
			find = inc[0].lower()

		else:
			fast=False

		# with open(path,encoding=char) as f:
		# _.pr(os.path.isfile(path),path)
		if not os.path.isfile(path):
			return path
		for line in _.getText(path,raw=True).split('\n'):
			# for line in f:
			i+=1
			
			if fast:
				# _.cp('fast','green')
				if find in line.lower():
					
					if pr:
						_.pr()
					printer(path,ni=1)
					if pr:
						print_line(i,line,inc)
					if pr == 1:
						return path



			else:
				# _.pr(inc)
				# _.pr(ex)
				# sys.exit()
				if _.showLine(line, plus=inc, minus=ex,OR=False):
					if pr:
						_.pr()
					printer(path,ni=1)
					if pr:
						print_line(i,line,inc)
					if pr == 1:
						return path

def cleaner(line):
	line=line.replace('\r','').replace('\n','')
	line=_str.cleanBE(line,' ')
	line=_str.cleanBE(line,'\t')
	return line

def print_line(i,line,inc):
	# _.pr(line)
	line=cleaner(line)
	line=cleaner(line)
	subjects=[]
	for xXx in inc:
		for subject in _.caseUnspecific( line, xXx ):
			subjects.append(subject)
	for subject in subjects:
		line = line.replace( subject, _.cp( subject, 'green', p=0 ) )
	_.pr('',_.cp(i,'yellow',p=0),line)

def sw(path):
	# _.pr(path)
	for check in '/bin /boot /dev /lib /lib64 /lost+found /proc /srv /sys'.split(' '):
		if path.lower() == check or path.lower().startswith(check+'/'):
			# _.pr(path)
			return False
	return True



# import chardet


# if _.switches.isActive('Ago'):
import _rightThumb._dir as _dir

# def load():
#   global data
#   data = _.getTable( 'table.json' )
# data = []
# 'Recursive'


# getFolder
# getFolder
# getFolder
# with open(path,encoding=char) as f:


########################################################################################
if __name__ == '__main__':
	action()


