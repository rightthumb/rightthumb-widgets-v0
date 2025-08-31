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
import re
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

__.isFiles=True


def appSwitches():

	

	# , group=[swGrp,'A Group'] )
	swGrp = 1
	_.switches.trigger( 'Folders', _.myFolderLocations )
	if not __.isFiles:
		_.switches.register('Recursive', '-r,-recursive', group=[swGrp,'Folder Settings'] )
	else:
		_.switches.register('Not-Recursive', '-r', group=[swGrp,'Folder Settings'] )
	_.switches.register('Folders', '-f,-folder,-folders,-fo', group=[swGrp,'Folder Settings'] )
	_.switches.register('FolderRefine', '-fr', group=[swGrp,'Folder Settings'] )
	_.switches.register('MaxDepth', '-depth', '3', group=[swGrp,'Folder Settings'] )
	
	swGrp += 1
	_.switches.register('Print-Clean', '--c,-clean', group=[swGrp,'Formatting and Output'] )
	_.switches.register('No-Extension', '-noext', group=[swGrp,'Formatting and Output'] )
	_.switches.register('Toggle-Relative-Path', '-rr', group=[swGrp,'Formatting and Output'] )
	_.switches.register('Force-Full-Path', '-fp,-pf,-forcepath', group=[swGrp,'Formatting and Output'] )
	_.switches.register('Relative-Path-Persistent', '-rrr', group=[swGrp,'Formatting and Output'] )
	_.switches.register('Force-Relative-Path', '-rf,-forcerelative', group=[swGrp,'Formatting and Output'] )
	_.switches.register('Reverse', '-rev,-reverse', group=[swGrp,'Formatting and Output'] )


	swGrp += 1
	_.switches.register('Symlink-Path-Integrity', '-si,-spi,-sym,-symlink', group=[swGrp,'OS Links'] )
	swGrp += 1
	_.switches.register('Kind', '-kind,-ext', 'db image graphic video app audio doc script archive', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Text', '-t,-text,-txt', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Binary', '-bin', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Encrypted', '-en,-crypt,-encryption,-encrypted', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Size', '-size',' g 10mb, L 2kb ', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Totals', '-total,-totals', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Ago', '-ago', '1m', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Ago-Create-Date', '-cd', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Search-Print-Line', '-p,-print','all', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Contains-IPs', '-ip','domains', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('Disable-Intelligence', '-showall', group=[swGrp,'File Search Toolbox'] )
	_.switches.register('No-Linked-Folders', '-nl,-nolinks', group=[swGrp,'File Search Toolbox'] )

	swGrp += 1


	_.switches.register('Search-For-Text-Include', '-has,-search', group=[swGrp,'Contents Search Toolbox'] )
	_.switches.register('Search-For-Text-Exclude', '-not', group=[swGrp,'Contents Search Toolbox'] )
	_.switches.register('Search-For-Text-Dump', '--dump', group=[swGrp,'Contents Search Toolbox'] )
	_.switches.register('Search-For-Text-TOP_Of_File', '-top','10', group=[swGrp,'Contents Search Toolbox'] )
	_.switches.register('Not-In-Comments', '-nocomment','html py php js', group=[swGrp,'Contents Search Toolbox'] )


	swGrp += 1
	_.switches.register('Delete', '--delete', group=[swGrp,'Delete and Secure Delete'] )
	_.switches.register('DeleteConfirm', '--confirm', group=[swGrp,'Delete and Secure Delete'] )
	_.switches.register('SecureDelete', '--secure', group=[swGrp,'Delete and Secure Delete'] )
	_.switches.register('SecureDeleteCriteria', '--criteria','*backup*.zip', group=[swGrp,'Delete and Secure Delete'] )

	swGrp += 1
	_.switches.register('Widget-V0', '-w,-v0', group=[swGrp,'Extra Features'] )
	_.switches.register('Copy', '-copy', group=[swGrp,'Extra Features'] )
	swGrp += 1
	_.switches.register('Backup', '-b,-bk,-backup', group=[swGrp,'Extra Features'] )
	
	swGrp += 1
	_.switches.register('InvertResults', '-invert', group=[swGrp,'Invert'] )
	swGrp += 1
	_.switches.register('FileNameIs', '-is', group=[swGrp,'FileIs'] )
	swGrp += 1
	_.switches.register('f1', '-f1', 'Kill: esc + f1', group=[swGrp,'No f1 Listener to add omit mid app'] )
	swGrp += 1
	_.switches.register('AlmaFixPipe', '-alma', 'On Alma Linux regular pipe does not work, this fixes it', group=[swGrp,'Alma Fix Pipe'] )


_bk = None
def backup(path):
	if not os.path.isfile(path): return None
	global _bk
	if not _bk:
		_bk = _.regImp( __.appReg, 'fileBackup' )
	_bk.switch( 'Silent' )
	_bk.switch( 'isRunOnce' )
	_bk.switch( 'Flag', 'APP' )
	_bk.switch( 'DoNotSchedule' )
	_bk.switch( 'Input', path )
	bkfi = _bk.action()
	return bkfi


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




def getSome(path, num=10, mode='lines'):
	if mode.lower().startswith('c'): mode = 'characters'
	if mode.lower().startswith('l'): mode = 'lines'
	try:
		with open(path, 'r') as file:
			if mode == 'lines':
				lines = []
				for i, line in enumerate(file):
					if i < num:
						lines.append(line)
					else:
						break
				return ''.join(lines)

			elif mode == 'characters':
				content = file.read(num)
				return content
			else:
				return ''
	except: return ''
	return ''

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
	_.switches.trigger( 'Folder', _.myFolder )
	_.switches.trigger( 'Folders', _.myFolder )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	# _.load()
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True
		_.switches.trigger( 'Folder', _.myFolder )
		_.switches.trigger( 'Folders', _.myFolder )
		print('123')
		_.load()
		print('456')
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
if _.switches.isActive('AlmaFixPipe'):
	_.postLoad( __file__ )


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

def remove_html_comments(string):
	pattern = re.compile(r'<!--.*?-->', re.DOTALL)
	return pattern.sub('', string)

def remove_python_comments(code):
	code = re.sub(r'#.*', '', code)
	code = re.sub(r'(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")', '', code, flags=re.DOTALL)
	return code

def remove_php_comments(code):
	code = re.sub(r'(//.*|#.*)', '', code)
	code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
	return code

def remove_javascript_comments(code):
	code = re.sub(r'//.*', '', code)
	code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
	return code


def isText(file):
	result = _.isTextFi(file)
	return result
	if result:
		return _mime.isText(file)
	return False

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result




def getFolder(folder,r=True):
	while os.sep+os.sep in folder: folder=folder.replace(os.sep+os.sep,os.sep)

	if not os.path.isdir(folder): return None

	if not _.v.do_not_hide__pycache:
		if '__pycache__' in folder.split(os.sep)[-1]: return None

	# if not _.isWin:
	#   for test in '/bin /boot /dev /lib /lib64 /lost+found /media /mnt /proc /srv /sys'.split(' '):
	#       if folder.startswith(test+'/'):
	#           return None
	#   if folder in '/bin /boot /dev /lib /lib64 /lost+found /media /mnt /proc /srv /sys'.split(' '):
	#       return None


	# if _.switches.isActive('Minus') and not _.showLine(folder,):
	#   return None
	

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
		# if _.switches.isActive('Reverse'): dirList.reverse()
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			if _.switches.isActive('No-Linked-Folders'):
				if os.path.islink(folder):
					return None
			dirList = os.listdir(folder)
			if _.switches.isActive('Reverse'): dirList.reverse()
		for item in dirList:
			path = folder + _v.slash + item
			if __.MonActivated:
				if not _.showLine(folder) or not _.showLine(item+_v.slash,run=480):
					break
				elif not _.showLine(path,run=482):
					continue
			record = None
			add(path,r,l=1)
			possiblyWait()
isClean = _.switches.isActive('Print-Clean')
_.showLine2=True
def add(path,r=False,l=-1):
	
	# print(path,l)
	global i
	global iS
	global baseDepth
	global base_path
	global isClean
	# if not isClean:
	# 	_.pr(' ',r=1)
	path = path.replace(_v.slash+_v.slash,_v.slash)
	path = path.replace('",','')
	path = path.replace('"','')
	path=path.strip()
	if os.path.isfile(path):
		path = __.path(path)
		pathX=path.replace(base_path,'')
		if pathX.startswith(os.sep): pathX=pathX[1:]

		i = i + 1
		# print(__.appReg)
		if not os.path.isfile(path) or not os.path.exists(path):
			# _.pr( 1000, path )
			return None
		# print(path)
		if _.showLine(path,run=510):
			# print(path)
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

			ago1 = None
			ago2 = None
			agoType = None

			if _.switches.isActive('Ago'):

				ago1 = _.switches.values('Ago')[0]

				if len( _.switches.values('Ago') ) > 1:
					ago2 = _.switches.values('Ago')[1]
					agoType = 'Range'
					if not type(ago2) == float:
						ago2 = None
						agoType = None
						

				# sys.exit()
				record = _dir.fileInfo( path )
				# _.pr( _.switches.values('Ago'), record['date_modified_raw'], record['date_created_raw'],  )
				# if os.path.isfile(path):
				shouldAdd = False
				run = 'default'
				if _.switches.isActive('Ago-Create-Date'):
					run = 'cd'
				if len( _.switches.values('Ago') ) > 1:
					actionTaken = False
					if 'cd' in _.switches.values('Ago')[1]:
						run = 'cd'
						actionTaken = True
					if 'md' in _.switches.values('Ago')[1]:
						actionTaken = True
						run = 'md'
					# if actionTaken:
					# 	_.switches.set('Ago', 'value', _.switches.values('Ago')[0])
					# 	_.switches.set('Ago', 'values', [_.switches.values('Ago')[0]])

				if len( _.switches.values('Ago') ) > 2:
					if 'a' in _.switches.values('Ago')[2]:
						run = 'a'
					elif 'md' in _.switches.values('Ago')[2]:
						run = 'md'

					elif 'resent' in _.switches.values('Ago')[2]:
						run = 'resent'
					elif 'm' in _.switches.values('Ago')[2]:
						run = 'md'
					agoType = run


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
					agoType = run


				# _.pr(  len( _.switches.values('Ago') )  )
				# _.pr(  ( _.switches.values('Ago') )  )
				# sys.exit()
				# accessed_raw

				# print(run)
				agoRange = False
				if len( _.switches.values('Ago') ) > 1 and type(_.switches.values('Ago')[1]) == float:
					agoRange = True

				# _.pr( run, agoRange, _.switches.values('Ago')[0], _.friendlyDate(_.switches.values('Ago')[0]) )
				# _.pr( run, agoRange, _.switches.values('Ago')[0], _.friendlyDate(_.switches.values('Ago')[0]), _.switches.values('Ago')[1], _.friendlyDate(_.switches.values('Ago')[1]) )

				if not agoRange:
					if run == 'default':
						if record['date_modified_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True
							# _.pr(path)
					elif run == 'resent':
						if record['date_modified_raw'] > _.switches.values('Ago')[0]:
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
						if (record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1]):
								shouldAdd = True
					elif run == 'resent':
						if (record['date_modified_raw'] < _.switches.values('Ago')[0] or record['date_created_raw'] < _.switches.values('Ago')[0] or record['accessed_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1] or record['date_created_raw'] > _.switches.values('Ago')[1] or record['accessed_raw'] > _.switches.values('Ago')[1]):
								shouldAdd = True
					elif run == 'a':
						if (record['accessed_raw'] < _.switches.values('Ago')[0]) and (record['accessed_raw'] > _.switches.values('Ago')[1]):
								shouldAdd = True
					elif run == 'cd':
						if (record['date_created_raw'] < _.switches.values('Ago')[0]) and (record['date_created_raw'] > _.switches.values('Ago')[1]):
								shouldAdd = True
					elif run == 'md':
						if (record['date_modified_raw'] < _.switches.values('Ago')[0]) and (record['date_modified_raw'] > _.switches.values('Ago')[1]):
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
						

						if _.switches.isActive('Print-Clean'):
							if not _.v.show_full_path:
								# process(pathX)
								process(path,l=702)
							else:
								process(path,l=704)
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
								if __.filesCopy: _copy.imp.copy(  __.path(pathX)  , p=0   )
								result += _.colorThis( pathX, 'cyan', p=0 )
							else:
								if __.filesCopy: _copy.imp.copy(  __.path(path)  , p=0   )
								result += _.colorThis( path, 'cyan', p=0 )

							_.pr( result )
							global totals_bytes
							totals_bytes+=size
						
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



			if shouldAdd and _.switches.isActive('Encrypted') and not _.isCrypt(path): shouldAdd = False


			if shouldAdd:
				if not _.v.do_not_hide__pycache and path.endswith('.pyc'): shouldAdd=False


			if ago2 and shouldAdd:
				# 'ago'
				# 'agoAGO'
				ago = _.md(path)
				if ago > ago1 and ago < ago2:
					pass
				else:
					shouldAdd = False
				# if shouldAdd:
				# 	print(path)
				# 	return None
			if _.switches.isActive('InvertResults'):
				shouldAdd = not shouldAdd
			if shouldAdd:
				if _.switches.isActive('Backup'):
					bkFi = backup(path)
				iS+=1
				if not _.switches.isActive('Totals'):
					if not _.v.show_full_path:
						if not _.switches.isActive('Plus'):
							# process(pathX)
							process(path,l=783)
						else:
							# process(pathX)
							process(path,l=786)
					else:
						if not _.switches.isActive('Plus'):
							process(path,l=789)
						else:
							process(path,l=791)


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
				if not _.showLine(newFolder,run=813):
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
	_db.switch( 'Tables', [ 'file', 'Kind' ] )
	useDB=True
	for index in _.switches.values('Kind'):
		if index.startswith('.'):
			useDB=False
			extensionList.append(index)
	if useDB:
		for index in _.switches.values('Kind'):
			_db.switch( 'Plus', [index] )
			for i,x in enumerate(_db.action()):
				# print(x)
				x = x.replace('.','')
				if not x.startswith('.'):
					x = '.'+x
				if not x in extensionList:
					extensionList.append( x.lower() )
	# print(extensionList); sys.exit();

def Relative_Path_Persistent():
	if 'noFig' in _.switches.values('Relative-Path-Persistent'):
		return None
	def rpp_notify(say,m=False):
		c='yellow'
		_.pr()
		if m:
			_.pr('','Relative-Path-Persistent:',say,'min',c=c)
		else:
			_.pr('','Relative-Path-Persistent:',say,c=c)
		_.pr()
	rpp_fig='files_Relative-Path-Persistent.fig'
	try:
		Session_ID = os.environ['Session_ID']
	except:
		Session_ID = ''
	fig=_.getTable(rpp_fig)
	# _.pv(fig)
	if _.switches.isActive('Relative-Path-Persistent'):

		rpp = False
		if Session_ID in fig and time.time() < fig[Session_ID]:
			rpp=True

		if _.switches.value('Relative-Path-Persistent'):
			mins=int(_.switches.value('Relative-Path-Persistent'))
		else:
			mins=9999
		if rpp:
			rpp_notify('disabled')
			fig[Session_ID]=time.time()-(60*mins)
			_.saveTable(fig,rpp_fig,p=0)
			return None


		rpp_notify(mins,m=1)
		fig[Session_ID]=time.time()+(60*mins)
		_.saveTable(fig,rpp_fig,p=0)

	if Session_ID in fig and time.time() < fig[Session_ID]:
		if __.isFiles:
			if _.switches.isActive('Toggle-Relative-Path'):
				_.switches.fieldSet( 'Toggle-Relative-Path', 'active', False )
			else:
				_.switches.fieldSet( 'Toggle-Relative-Path', 'active', True )

_paste = None


def possiblyWait():
	while __.Mon.pause:
		time.sleep(1)


def addOmit():
	global _paste
	if _paste is None:
		_paste = _.regImp( __.appReg, '-paste' )
	omit=_paste.imp.paste()
	omit = omit.strip()
	if not omit: return None
	_.switches.Add( 'Minus', omit )
	__.MonActivated = True
	# __.Mon.pause = False

	# current = _.switches.value('Minus')
	# current.append(omit)
	# _.switches.fieldSet( 'Minus', 'active', True )
	# _.switches.fieldSet( 'Minus', 'values', current )
	# _.switches.fieldSet( 'Minus', 'value', ','.join(current) )
	# __.Mon.pause = False

__.filesCopy = _.switches.isActive('Copy')
if _.switches.isActive('Copy'):
	_copy = _.regImp( __.appReg, '-copy' )


def action():
	
	__.appRegBK = __.appReg
	__.MonActivated = False

	if _.switches.isActive('f1'):
		__.F1 = True
		__.Mon = _.KeyMon({'f1': lambda:addOmit()},strict=True)
	else:
		__.F1 = False
		__.Mon = _.dot(); __.Mon.pause = False
	
	Relative_Path_Persistent()

	_.v.no_extension = _.switches.isActive('No-Extension')
	_.v.do_not_hide__pycache = _.switches.isActive('Disable-Intelligence')

	if _.switches.isActive('Force-Full-Path') or _.switches.isActive('Force-Relative-Path'):
		if _.switches.isActive('Force-Full-Path'):
			_.v.show_full_path = True
		else:
			_.v.show_full_path = False
	else:
		if __.isFiles:
			_.v.show_full_path = True
			if _.switches.isActive('Toggle-Relative-Path'):_.v.show_full_path = False
		else:
			_.v.show_full_path = False
			if _.switches.isActive('Toggle-Relative-Path'): _.v.show_full_path = True

	if _.switches.isActive('Minus'): minusF()

	global base_path
	if _.switches.isActive('Kind'): extensionsDatabank()
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

					# if not path.lower().startswith(fi0.lower()) and os.path.isfile(path):
						# print(fi0,path,path.lower().startswith(fi0.lower()))
						good=False; break;
				if not os.sep in fi0 or fi0 == os.sep:
					err=1; break;
				if good:
					base_path=fi0
					break
			if base_path: _.v.show_full_path = False
		for path in _.isData():
			path = path.replace(_v.slash+_v.slash,_v.slash)
			path = path.replace('",','')
			path = path.replace('"','')
			path=path.strip()
			if os.path.isfile(path):
				add(path,l=1)
	
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
		if not _.switches.isActive('Folders'):
			folder = os.getcwd()
		else:
			folder = _.switches.value('Folders')
		folder = __.path(folder)
		# print(folder)
		global baseDepth
		# global base_path
		baseDepth = len( folder.split(_v.slash) )
		base_path=folder

		if not _.switches.isActive('Widget-V0'):
			
			getFolder(folder,r=r)
			if _.switches.isActive('Size'):
				if not _.switches.isActive('Print-Clean'):
					_.pr()
					_.pr('total:',formatSize(totals_bytes),c='Background.light_blue')
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
			_.switches.fieldSet( 'Plus', 'value', '*.py,*.sh,*.bat,*.MD,*.ad,*.ps1,*.yml,*.cpp' )
			_.switches.fieldSet( 'Plus', 'values', ['*.py','*.sh','*.bat','*.MD','*.ad','*.ps1','*.yml','*.cpp'] )
			_.switches.fieldSet( 'PlusOr', 'active', True )
			getFolder(_v.ww+os.sep+'python')
			getFolder(_v.ww+os.sep+'batch', r=False)
			getFolder(_v.ww+os.sep+'powershell', r=False)
			getFolder(_v.ww+os.sep+'php', r=False)
			getFolder(_v.ww+os.sep+'windows')
			getFolder(_v.ww+os.sep+'bash')
			getFolder(_v.ww+os.sep+'ads')
			getFolder(_v.widgets+os.sep+'install')
			getFolder(_v.widgets, r=False)
		
		"""
		if _.switches.isActive('Kind'):
			folderProfileAttribute( folder=folder, info={
															'recursive': True,
															'Print-Clean': iS,
															'files': i ,
															'diff': _.pDiff( iS, i, use='less' ) ,
			} )
		"""
		# if not iS == i:

		# 	_.folderProfileAttribute( folder=folder, info = {
		# 													'app': 'files',
		# 													'recursive': r,
		# 													'factors': {
		# 																	'Text': _.switches.isActive('Text'),
		# 																	'Binary': _.switches.isActive('Binary'),
		# 																	'Kind': _.switches.isActive('Kind'),
		# 																	'Type': _.switches.values('Kind'),

		# 																	'PlusOr': _.switches.isActive('PlusOr'),
		# 																	'PlusClose': _.switches.isActive('PlusClose'),
		# 																	'Plus': _.switches.isActive('Plus'),
		# 																	'Minus': _.switches.isActive('Minus'),
																			
		# 																	'PlusVals': _.switches.values('Plus'),
		# 																	'MinusVals': _.switches.values('Minus'),
		# 													},
		# 													'percentage': _.pDiff( iS, i, use='less' ),
		# 													'Print-Clean': iS,
		# 													'files': i,

		# 	} )
	global deletedFiles
	if _.switches.isActive('Delete'):
		iS = deletedFiles
	if _.switches.isActive('Print-Clean') == False:
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

if _.switches.isActive('Contains-IPs'):
	scan_IPs=True
	if 'd' in _.switches.value('Contains-IPs'):
		scan_domains=True
	else:
		scan_domains=False

else:
	scan_domains=False
	scan_IPs=False
if _.switches.isActive('Search-For-Text-Include'):
	scan=True
else:
	scan=False
def nocomment(text):
	text=remove_php_comments(text)
	text=remove_html_comments(text)
	text=remove_python_comments(text)
	text=remove_javascript_comments(text)
	return text
def NOTHING(text): return text
if _.switches.isActive('Not-In-Comments'):
	if not 'html' in _.switches.value('Not-In-Comments'): remove_html_comments=NOTHING
	if not 'py' in _.switches.value('Not-In-Comments'): remove_python_comments=NOTHING
	if not 'php' in _.switches.value('Not-In-Comments'): remove_php_comments=NOTHING
	if not 'js' in _.switches.value('Not-In-Comments'): remove_javascript_comments=NOTHING
else:
	remove_html_comments=NOTHING
	remove_python_comments=NOTHING
	remove_php_comments=NOTHING
	remove_javascript_comments=NOTHING
if not _.switches.isActive('Search-Print-Line'):
	pr=0
elif 'a' in _.switches.value('Search-Print-Line').lower():
	pr=2
else:
	pr=1
if not _.switches.values('Search-For-Text-TOP_Of_File'):
	some=0
elif _.switches.value('Search-For-Text-TOP_Of_File'):
	some=int(_.switches.value('Search-For-Text-TOP_Of_File'))
else:
	some=10
inc=_.switches.values('Search-For-Text-Include')
for i,x in enumerate(inc): inc[i] = _.ci(inc[i])
# the_file=_.getText(path,raw=True)
ex=_.switches.values('Search-For-Text-Exclude')
for i,x in enumerate(ex): ex[i] = _.ci(ex[i])
if _.switches.isActive('Search-For-Text-Dump'):
	_.pr('-has',inc)
	_.pr('-not',ex)
	sys.exit()
for i,x in enumerate(inc):
	inc[i]=_.ci(x)
	if not i and _.switches.isActive('Plus-single'):
		inc[i]=inc[i].replace("'",'"')
		# break

for i,x in enumerate(ex):
	ex[i]=_.ci(x)
	if not i and _.switches.isActive('Minus-single'):
		ex[i]=ex[i].replace("'",'"')
		# break
infile=0

def process3(path):
	pass

spent=[]


def _domains(text,domains=False):
	ips = []
	text=text.lower()
	lines = []
	for line in text.split('\n'):
		lines.append( line.split('#')[0] )
	text='\n'.join( lines )
	# https://data.iana.org/TLD/tlds-alpha-by-domain.txt
	_domains_='AAA AARP ABARTH ABB ABBOTT ABBVIE ABC ABLE ABOGADO ABUDHABI AC ACADEMY ACCENTURE ACCOUNTANT ACCOUNTANTS ACO ACTOR AD ADAC ADS ADULT AE AEG AERO AETNA AF AFL AFRICA AG AGAKHAN AGENCY AI AIG AIRBUS AIRFORCE AIRTEL AKDN AL ALFAROMEO ALIBABA ALIPAY ALLFINANZ ALLSTATE ALLY ALSACE ALSTOM AM AMAZON AMERICANEXPRESS AMERICANFAMILY AMEX AMFAM AMICA AMSTERDAM ANALYTICS ANDROID ANQUAN ANZ AO AOL APARTMENTS APP APPLE AQ AQUARELLE AR ARAB ARAMCO ARCHI ARMY ARPA ART ARTE AS ASDA ASIA ASSOCIATES AT ATHLETA ATTORNEY AU AUCTION AUDI AUDIBLE AUDIO AUSPOST AUTHOR AUTO AUTOS AVIANCA AW AWS AX AXA AZ AZURE BA BABY BAIDU BANAMEX BANANAREPUBLIC BAND BANK BAR BARCELONA BARCLAYCARD BARCLAYS BAREFOOT BARGAINS BASEBALL BASKETBALL BAUHAUS BAYERN BB BBC BBT BBVA BCG BCN BD BE BEATS BEAUTY BEER BENTLEY BERLIN BEST BESTBUY BET BF BG BH BHARTI BI BIBLE BID BIKE BING BINGO BIO BIZ BJ BLACK BLACKFRIDAY BLOCKBUSTER BLOG BLOOMBERG BLUE BM BMS BMW BN BNPPARIBAS BO BOATS BOEHRINGER BOFA BOM BOND BOO BOOK BOOKING BOSCH BOSTIK BOSTON BOT BOUTIQUE BOX BR BRADESCO BRIDGESTONE BROADWAY BROKER BROTHER BRUSSELS BS BT BUGATTI BUILD BUILDERS BUSINESS BUY BUZZ BV BW BY BZ BZH CA CAB CAFE CAL CALL CALVINKLEIN CAM CAMERA CAMP CANCERRESEARCH CANON CAPETOWN CAPITAL CAPITALONE CAR CARAVAN CARDS CARE CAREER CAREERS CARS CASA CASE CASH CASINO CAT CATERING CATHOLIC CBA CBN CBRE CBS CC CD CENTER CEO CERN CF CFA CFD CG CH CHANEL CHANNEL CHARITY CHASE CHAT CHEAP CHINTAI CHRISTMAS CHROME CHURCH CI CIPRIANI CIRCLE CISCO CITADEL CITI CITIC CITY CITYEATS CK CL CLAIMS CLEANING CLICK CLINIC CLINIQUE CLOTHING CLOUD CLUB CLUBMED CM CN CO COACH CODES COFFEE COLLEGE COLOGNE COM COMCAST COMMBANK COMMUNITY COMPANY COMPARE COMPUTER COMSEC CONDOS CONSTRUCTION CONSULTING CONTACT CONTRACTORS COOKING COOKINGCHANNEL COOL COOP CORSICA COUNTRY COUPON COUPONS COURSES CPA CR CREDIT CREDITCARD CREDITUNION CRICKET CROWN CRS CRUISE CRUISES CU CUISINELLA CV CW CX CY CYMRU CYOU CZ DABUR DAD DANCE DATA DATE DATING DATSUN DAY DCLK DDS DE DEAL DEALER DEALS DEGREE DELIVERY DELL DELOITTE DELTA DEMOCRAT DENTAL DENTIST DESI DESIGN DEV DHL DIAMONDS DIET DIGITAL DIRECT DIRECTORY DISCOUNT DISCOVER DISH DIY DJ DK DM DNP DO DOCS DOCTOR DOG DOMAINS DOT DOWNLOAD DRIVE DTV DUBAI DUNLOP DUPONT DURBAN DVAG DVR DZ EARTH EAT EC ECO EDEKA EDU EDUCATION EE EG EMAIL EMERCK ENERGY ENGINEER ENGINEERING ENTERPRISES EPSON EQUIPMENT ER ERICSSON ERNI ES ESQ ESTATE ET ETISALAT EU EUROVISION EUS EVENTS EXCHANGE EXPERT EXPOSED EXPRESS EXTRASPACE FAGE FAIL FAIRWINDS FAITH FAMILY FAN FANS FARM FARMERS FASHION FAST FEDEX FEEDBACK FERRARI FERRERO FI FIAT FIDELITY FIDO FILM FINAL FINANCE FINANCIAL FIRE FIRESTONE FIRMDALE FISH FISHING FIT FITNESS FJ FK FLICKR FLIGHTS FLIR FLORIST FLOWERS FLY FM FO FOO FOOD FOODNETWORK FOOTBALL FORD FOREX FORSALE FORUM FOUNDATION FOX FR FREE FRESENIUS FRL FROGANS FRONTDOOR FRONTIER FTR FUJITSU FUN FUND FURNITURE FUTBOL FYI GA GAL GALLERY GALLO GALLUP GAME GAMES GAP GARDEN GAY GB GBIZ GD GDN GE GEA GENT GENTING GEORGE GF GG GGEE GH GI GIFT GIFTS GIVES GIVING GL GLASS GLE GLOBAL GLOBO GM GMAIL GMBH GMO GMX GN GODADDY GOLD GOLDPOINT GOLF GOO GOODYEAR GOOG GOOGLE GOP GOT GOV GP GQ GR GRAINGER GRAPHICS GRATIS GREEN GRIPE GROCERY GROUP GS GT GU GUARDIAN GUCCI GUGE GUIDE GUITARS GURU GW GY HAIR HAMBURG HANGOUT HAUS HBO HDFC HDFCBANK HEALTH HEALTHCARE HELP HELSINKI HERE HERMES HGTV HIPHOP HISAMITSU HITACHI HIV HK HKT HM HN HOCKEY HOLDINGS HOLIDAY HOMEDEPOT HOMEGOODS HOMES HOMESENSE HONDA HORSE HOSPITAL HOST HOSTING HOT HOTELES HOTELS HOTMAIL HOUSE HOW HR HSBC HT HU HUGHES HYATT HYUNDAI IBM ICBC ICE ICU ID IE IEEE IFM IKANO IL IM IMAMAT IMDB IMMO IMMOBILIEN IN INC INDUSTRIES INFINITI INFO ING INK INSTITUTE INSURANCE INSURE INT INTERNATIONAL INTUIT INVESTMENTS IO IPIRANGA IQ IR IRISH IS ISMAILI IST ISTANBUL IT ITAU ITV JAGUAR JAVA JCB JE JEEP JETZT JEWELRY JIO JLL JM JMP JNJ JO JOBS JOBURG JOT JOY JP JPMORGAN JPRS JUEGOS JUNIPER KAUFEN KDDI KE KERRYHOTELS KERRYLOGISTICS KERRYPROPERTIES KFH KG KH KI KIA KIDS KIM KINDER KINDLE KITCHEN KIWI KM KN KOELN KOMATSU KOSHER KP KPMG KPN KR KRD KRED KUOKGROUP KW KY KYOTO KZ LA LACAIXA LAMBORGHINI LAMER LANCASTER LANCIA LAND LANDROVER LANXESS LASALLE LAT LATINO LATROBE LAW LAWYER LB LC LDS LEASE LECLERC LEFRAK LEGAL LEGO LEXUS LGBT LI LIDL LIFE LIFEINSURANCE LIFESTYLE LIGHTING LIKE LILLY LIMITED LIMO LINCOLN LINDE LINK LIPSY LIVE LIVING LK LLC LLP LOAN LOANS LOCKER LOCUS LOFT LOL LONDON LOTTE LOTTO LOVE LPL LPLFINANCIAL LR LS LT LTD LTDA LU LUNDBECK LUXE LUXURY LV LY MA MACYS MADRID MAIF MAISON MAKEUP MAN MANAGEMENT MANGO MAP MARKET MARKETING MARKETS MARRIOTT MARSHALLS MASERATI MATTEL MBA MC MCKINSEY MD ME MED MEDIA MEET MELBOURNE MEME MEMORIAL MEN MENU MERCKMSD MG MH MIAMI MICROSOFT MIL MINI MINT MIT MITSUBISHI MK ML MLB MLS MM MMA MN MO MOBI MOBILE MODA MOE MOI MOM MONASH MONEY MONSTER MORMON MORTGAGE MOSCOW MOTO MOTORCYCLES MOV MOVIE MP MQ MR MS MSD MT MTN MTR MU MUSEUM MUSIC MUTUAL MV MW MX MY MZ NA NAB NAGOYA NAME NATURA NAVY NBA NC NE NEC NET NETBANK NETFLIX NETWORK NEUSTAR NEW NEWS NEXT NEXTDIRECT NEXUS NF NFL NG NGO NHK NI NICO NIKE NIKON NINJA NISSAN NISSAY NL NO NOKIA NORTHWESTERNMUTUAL NORTON NOW NOWRUZ NOWTV NP NR NRA NRW NTT NU NYC NZ OBI OBSERVER OFFICE OKINAWA OLAYAN OLAYANGROUP OLDNAVY OLLO OM OMEGA ONE ONG ONL ONLINE OOO OPEN ORACLE ORANGE ORG ORGANIC ORIGINS OSAKA OTSUKA OTT OVH PA PAGE PANASONIC PARIS PARS PARTNERS PARTS PARTY PASSAGENS PAY PCCW PE PET PF PFIZER PG PH PHARMACY PHD PHILIPS PHONE PHOTO PHOTOGRAPHY PHOTOS PHYSIO PICS PICTET PICTURES PID PIN PING PINK PIONEER PIZZA PK PL PLACE PLAY PLAYSTATION PLUMBING PLUS PM PN PNC POHL POKER POLITIE PORN POST PR PRAMERICA PRAXI PRESS PRIME PRO PROD PRODUCTIONS PROF PROGRESSIVE PROMO PROPERTIES PROPERTY PROTECTION PRU PRUDENTIAL PS PT PUB PW PWC QA QPON QUEBEC QUEST RACING RADIO RE READ REALESTATE REALTOR REALTY RECIPES RED REDSTONE REDUMBRELLA REHAB REISE REISEN REIT RELIANCE REN RENT RENTALS REPAIR REPORT REPUBLICAN REST RESTAURANT REVIEW REVIEWS REXROTH RICH RICHARDLI RICOH RIL RIO RIP RO ROCHER ROCKS RODEO ROGERS ROOM RS RSVP RU RUGBY RUHR RUN RW RWE RYUKYU SA SAARLAND SAFE SAFETY SAKURA SALE SALON SAMSCLUB SAMSUNG SANDVIK SANDVIKCOROMANT SANOFI SAP SARL SAS SAVE SAXO SB SBI SBS SC SCA SCB SCHAEFFLER SCHMIDT SCHOLARSHIPS SCHOOL SCHULE SCHWARZ SCIENCE SCOT SD SE SEARCH SEAT SECURE SECURITY SEEK SELECT SENER SERVICES SES SEVEN SEW SEX SEXY SFR SG SHANGRILA SHARP SHAW SHELL SHIA SHIKSHA SHOES SHOP SHOPPING SHOUJI SHOW SHOWTIME SI SILK SINA SINGLES SITE SJ SK SKI SKIN SKY SKYPE SL SLING SM SMART SMILE SN SNCF SO SOCCER SOCIAL SOFTBANK SOFTWARE SOHU SOLAR SOLUTIONS SONG SONY SOY SPA SPACE SPORT SPOT SR SRL SS ST STADA STAPLES STAR STATEBANK STATEFARM STC STCGROUP STOCKHOLM STORAGE STORE STREAM STUDIO STUDY STYLE SU SUCKS SUPPLIES SUPPLY SUPPORT SURF SURGERY SUZUKI SV SWATCH SWISS SX SY SYDNEY SYSTEMS SZ TAB TAIPEI TALK TAOBAO TARGET TATAMOTORS TATAR TATTOO TAX TAXI TC TCI TD TDK TEAM TECH TECHNOLOGY TEL TEMASEK TENNIS TEVA TF TG TH THD THEATER THEATRE TIAA TICKETS TIENDA TIFFANY TIPS TIRES TIROL TJ TJMAXX TJX TK TKMAXX TL TM TMALL TN TO TODAY TOKYO TOOLS TOP TORAY TOSHIBA TOTAL TOURS TOWN TOYOTA TOYS TR TRADE TRADING TRAINING TRAVEL TRAVELCHANNEL TRAVELERS TRAVELERSINSURANCE TRUST TRV TT TUBE TUI TUNES TUSHU TV TVS TW TZ UA UBANK UBS UG UK UNICOM UNIVERSITY UNO UOL UPS US UY UZ VA VACATIONS VANA VANGUARD VC VE VEGAS VENTURES VERISIGN VERSICHERUNG VET VG VI VIAJES VIDEO VIG VIKING VILLAS VIN VIP VIRGIN VISA VISION VIVA VIVO VLAANDEREN VN VODKA VOLKSWAGEN VOLVO VOTE VOTING VOTO VOYAGE VU VUELOS WALES WALMART WALTER WANG WANGGOU WATCH WATCHES WEATHER WEATHERCHANNEL WEBCAM WEBER WEBSITE WED WEDDING WEIBO WEIR WF WHOSWHO WIEN WIKI WILLIAMHILL WIN WINDOWS WINE WINNERS WME WOLTERSKLUWER WOODSIDE WORK WORKS WORLD WOW WS WTC WTF XBOX XEROX XFINITY XIHUAN XIN XXX XYZ YACHTS YAHOO YAMAXUN YANDEX YE YODOBASHI YOGA YOKOHAMA YOU YOUTUBE YT YUN ZA ZAPPOS ZARA ZERO ZIP ZM ZONE ZUERICH ZW'
	# PY   SH 
	_domains_=_domains_.lower()
	u='._-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	cleaned=''
	for c in text:
		if c in u: cleaned+=c
		else: cleaned+=' '
	cleaned = _str.do('dup',cleaned, ' ')
	for gr in cleaned.split(' '):
		if gr.count('.') > 0:
			test = gr.split('.')
			good=False
			for ext in _domains_.split(' '):
				if gr.endswith('.'+ext): good=True
			if good:
				for omit in 'background _ . self. datetime.'.split(' '):
					if gr.startswith(omit): good=False
			if good and not gr in ips:
				ips.append(gr)
	return ips
def IPs(text,domains=False):
	ips = []
	if domains: ips=_domains(text)
	u='0123456789.'
	cleaned=''
	for c in text:
		if c in u: cleaned+=c
		else: cleaned+=' '
	cleaned = _str.do('dup',cleaned, ' ')
	for gr in cleaned.split(' '):
		if gr.count('.') == 3:
			test = gr.split('.')
			good=True
			for t in test:
				if len(t) >3 or len(t) ==0: good=False
			if good and not gr in ips:
				ips.append(gr)
	return ips
###################################################################################################
deletedFiles = 0
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
	# path = _.pyApp(path)
	if not _.v.show_full_path:
		path=path.replace(base_path,'')
		if path.startswith(os.sep): path=path[1:]

		if _.v.no_extension and '.' in path:
			path=path[:-len(path.split('.')[-1])-1]
	
	global shouldDelete
	if shouldDelete:
		global deletedFiles
		global deleteConfirmed
		global secureDelete
		global SecureDeleteCriteria
		if not secureDelete:
			if _.isCrypt(path):
				deletedFiles+=1
				secure_delete(path)
			elif not deleteConfirmed:
				deletedFiles+=1
				_.pr('Would Deleted:',path,c='green')
			else:
				deletedFiles+=1
				os.remove(path)
				_.pr('Deleted:',path,c='red')
		elif secureDelete:
			shouldSecureDelete = False
			if not SecureDeleteCriteria:
				shouldSecureDelete = True
			elif star(path,SecureDeleteCriteria):
				shouldSecureDelete = True
			if shouldSecureDelete:
				deletedFiles+=1
				secure_delete(path)
			
	else:
		if __.filesCopy: _copy.imp.copy(  __.path(path)  , p=0   )
		_.pr( _.colorThis( path, 'cyan', p=0 ) )
	# _.pr( _.colorThis( [_.pyApp(path)], 'cyan', p=0 ) )
	# _.pr( _.colorThis( [_.pyApp(path),path], 'cyan', p=0 ) )
	infile+=1
deleteConfirmed = _.switches.isActive('DeleteConfirm')
shouldDelete = _.switches.isActive('Delete')
secureDelete = _.switches.isActive('SecureDelete')
SecureDeleteCriteria = _.switches.values('SecureDeleteCriteria')
# if SecureDeleteCriteria: print(   ' '.join(SecureDeleteCriteria)  )
def secure_delete(path):
	global deleteConfirmed
	if not deleteConfirmed:
		_.pr('Would Delete:',path,c='green')
		return False
	if not os.path.isfile(path): return False
	try:
		file_size = os.path.getsize(path)
		with open(path, 'wb') as f:
			f.write(b'\x00' * file_size)
		with open(path, 'wb') as f:
			f.truncate(0)
		os.remove(path)
		_.pr('Secure Deleted:',path,c='red')
		return True
	except Exception as e:
		print(f"Error during secure delete: {e}")
		return False


def star(string, criteria=[], case_sensitive=False):
    if not case_sensitive:
        string = string.lower()

    # Ensure criteria is a list
    if not isinstance(criteria, list):
        criteria = [criteria]

    for crit in criteria:
        if not crit:  # Skip empty criteria
            continue

        # No wildcard, check for direct substring match
        if '*' not in crit:
            if crit in string:
                return True

        # Handle *wildcard* pattern
        pattern = re.escape(crit).replace(r'\*', '.*')
        if re.search(pattern, string):  # Changed to re.search for partial matches
            return True

    return False

###################################################################################################


def process(path,l=-1):
	# print('process',path,l)
	# return
	# possiblyWait()
	if _.switches.isActive('FileNameIs'):
		filename = os.path.basename(path)
		filename2 = filename.lower()
		if not filename in _.switches.values('FileNameIs') and not filename2 in _.switches.values('FileNameIs'):
			return None
	path=path.strip()
	if not os.path.isfile(path):
		return path
	# _.pr(path)
	# char = chardet.detect(open( path, 'rb' ).read(200))['encoding']\
	char='utf-8'
	char='iso-8859-1'
	# _.pr(char)
	global scan_IPs
	global scan
	global pr
	global inc
	global ex
	global scan_IPs
	global scan_domains
	global some

	if scan_IPs:
		ipsFound = IPs(_.getText(path,raw=True),domains=scan_domains)
		if pr:
			for ip in ipsFound:
				_.pr(ip,c='red')
		elif not pr:
			if ipsFound:
				if __.filesCopy: _copy.imp.copy(  __.path(path)  , p=0   )
				_.pr(path,c='cyan')
		return None


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
		if _.switches.isActive('PlusCode'): fast=False

		# with open(path,encoding=char) as f:
		# _.pr(os.path.isfile(path),path)
		if not os.path.isfile(path):
			return path
		if some:
			if _.isTextFi(path):
				the_file=getSome(path,some)
				# the_file=_.getText(path,raw=True)
			else: the_file=''
		else:
			# _.pr(path,c='purple')
			if _.isTextFi(path):
				# _.pr(path,c='green')
				the_file=nocomment(_.getText(path,raw=True))
				# if 'load.php' in path.lower(): print(the_file)
				# the_file=_.getText(path,raw=True)
			else: the_file=''
		# print(l,path)
		# print('ex',ex)
		# return

		'''
		VALID = True
		vRan = False
		# if not _.switches.isActive('StrictCase'):
		# 	inc = [s.lower() for s in inc]

		if VALID and not ex:
			# if all(word in text for word in words):
			if not all(word in the_file for word in inc):
				vRan = True
				VALID = False
		if not vRan:
			if not _.showLine(the_file, plus=inc, minus=ex,OR=False,code=True,run=1389):
				VALID = False
		if VALID:
			pass
		else:
			return path
		'''

		# _.validLine(string, has=None, omit=None, Any=False, caseStrict=False, strict=None)
		
		# if _.showLine(the_file, plus=inc, minus=ex,OR=False,code=True,run=1389):
		if _.validLine( the_file, has=inc, omit=ex, Any=False, caseStrict=_.switches.isActive('StrictCase') ):
			pass
		else:
			return path






		for line in the_file.split('\n'):
			# if _.showLine(line, plus=inc, minus=ex,OR=False,code=True): _.pr(line)
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

				# if _.showLine(line, plus=inc, minus=ex,OR=False,code=False,run=1417):
				if _.validLine(line, has=inc, omit=ex):
					# print('here');sys.exit();
					if pr: _.pr()
					printer(path,ni=1)
					if pr: print_line(i,line,inc)
					if pr == 1: return path

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


if _.switches.isActive('Symlink-Path-Integrity'):
	__.truePath = False

totals_bytes=0

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
# getSome

########################################################################################
if __name__ == '__main__':
	action()
	if _.switches.isActive('Backup') and not _.switches.isActive('Widget-V0'):
		if not _.switches.isActive('Print-Clean'):
			_.pr()
			_.pr()
			_.pr()
			_.pr('    File Backup Complete',h='light_steel_blue')
			_.pr()
			_.pr()
			_.pr()
	_.isExit(__file__)
