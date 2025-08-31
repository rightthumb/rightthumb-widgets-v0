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

# _.pr(__.appReg)

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
		_.switches.register('AbsolutePath', '-a')
		_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Folders', '-f,-p,-path,-paths,-folder,-folders,-fo')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	# _.switches.register('Extensions', '-ext', 'image, video, audio, document')
	_.switches.register('Totals', '-total,-totals')
	_.switches.register('FolderRefine', '-fr')
	_.switches.register('Ago', '-ago', '1m')
	_.switches.register('MaxDepth', '-depth', '3')
	_.switches.register('Extensions', '-ext', 'db image graphic video app audio doc script archive')
	_.switches.register('Remove-Root-Folder', '-rr')
	_.switches.register('Widget-V0', '-w,-v0')
	_.switches.register('Ago-Create-Date', '-cd')
	_.switches.register('NoExtension', '-noext,--ne')
	_.switches.register('ForceSimple', '--s,-simple')
	_.switches.trigger( 'Folders', _.myFolderLocations )



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
						'p files --c ',
						'p files -text ',
						'',
						'p files -size g 2mb',
						'p files -size L 2mb',
						'p files -size g 2mb --c -folder D:\\techApps\\Python\\Python36-32'+_v.slash,
						'',
						'b pp',
						'p files + *.py *.bat *.sh *.js *.htm* *.php  -or -totals',
						'',
						'',
						'p files -ext db - *.json *.dat',
						'',
						'p files -w --c -ago 10h | p line --c -make "git add {}" | p -copy',
						'p files -w --c -ago 10h',
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
	# _.pr(__.appReg)
	_appReg_ = __.appReg
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	# _.pr(__.appReg)
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	# _.pr(__.appReg)

	_.switches.trigger( 'Size' , unFormatSize )
	# _.switches.trigger( 'Folders' , _.bAlias )
	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
	_.defaultScriptTriggers()
	# _.pr(__.appReg)
	# _.pr(__.appReg,11)
	_.switches.process()
	# _.pr(__.appReg, 22)
	



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

# x=_.switches.all()
# # _.pr(__.appReg)
# _.pv(x); sys.exit()

def formatResults(path):
	ran = False
	if _.switches.isActive('Remove-Root-Folder'):
		ran = True
		path = os.path.basename(path)

	if _.switches.isActive('NoExtension'):
		ran = True
		path = os.path.splitext(path)[0]
	
	for replace in _.switches.values('NoExtension'):
		ran = True
		path = path.replace(replace,' ')
		while '  ' in path:
			path = path.replace('  ',' ')
	path = path.strip()
	if ran:
		return path
	return False

def isText(file):
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result

def getFolder(folder,r=True):
	if folder.startswith('/proc'):
		return None
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
			path = path.replace(_v.slash+_v.slash,_v.slash)
			
			if os.path.isfile(path):
				pathX=path
				if not _.switches.isActive('AbsolutePath'):
					pathX=pathX.replace(base_path+os.sep,'')
				i = i + 1
				
				if _.showLine(os.path.basename(path)):
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
								# sys.exit()
								if record['date_modified_raw'] > _.switches.values('Ago')[0]:
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
									if _.switches.isActive('Remove-Root-Folder'):
										_.pr( pathX, c='cyan')
									else:
										_.pr( path, c='cyan')
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
									if _.switches.isActive('Remove-Root-Folder'):
										result += _.colorThis( pathX, 'cyan', p=0 )
									else:
										result += _.colorThis( path, 'cyan', p=0 )

									_.pr( result )
								
								# _.pr( formatedSize, '\t', path )


					if shouldAdd :

						global extensionList
						if len( extensionList ):
							if record is None:
								record = _dir.fileInfo( path )
							if not len( record['ext'] ):
								shouldAdd = False
							else:
								record['ext'] = record['ext'].lower()
								if not '.'+record['ext'] in extensionList:
									shouldAdd = False

							# if '.' in path:
							#     pathy = path.lower().split('.')
							#     pathy_test = pathy.pop()
							#     if not '.'+pathy_test in extensionList:
							#         shouldAdd = False



					if shouldAdd:

						if _.switches.isActive('ForceSimple'):
							possible = formatResults(path)
							if possible:
								# _.pr( possible, plus='yellow,cyan', c='cyan' )
								_.pr( possible, plus=1, h='chartreuse,cornflower_blue' )
								continue
						
						iS+=1
						if not _.switches.isActive('Totals'):


							if _.switches.isActive('Remove-Root-Folder'):
								if _.switches.isActive('NoExtension'):
									prt=pathX.split('.')
									prt.pop(-1)
									pathX='.'.join(prt)
									if '_' in _.switches.values(''): pathX = pathX.replace('_',' ')
								if not _.switches.isActive('Plus'):
									_.pr( pathX, c='cyan' )
								else:
									_.pr( _.colorPlus( pathX, 'cyan' ) )
							else:
								if _.switches.isActive('NoExtension'):
									prt=path.split('.')
									prt.pop(-1)
									path='.'.join(prt)
									
								if not _.switches.isActive('Plus'):
									_.pr( path, c='cyan' )
								else:
									_.pr( _.colorPlus( path, 'cyan' ) )

					# if shouldAdd:
					#     text_binary = False
					#     if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
					#         text_binary = True
					#     else:
					#         if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
					#             text_binary = True
					#         if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
					#             text_binary = True
					#         if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
					#             text_binary = True
					#         if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
					#             text_binary = True
					#     if not text_binary:
					#         shouldAdd = False


			# if os.path.isdir(path) and _.showLine(path):
			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					shouldRun = True
					if _.switches.isActive('FolderRefine'):
						if not _.showLine(newFolder):
							shouldRun = False
					if r and shouldRun:
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

	for index in _.switches.values('Extensions'):
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )

def action():
	if not __.isFiles:
		r = _.switches.isActive('Recursive')
		if not r:
			_.switches.fieldSet( 'Remove-Root-Folder', 'active', True )

	else:
		r = True
	if _.switches.isActive('Extensions'):
		extensionsDatabank()


	_.fields.register( 'files', 'name', '1000.43 KB' )
	global i
	global iS
	# load()
	if _.switches.isActive('Folders') == False:
		folder = os.getcwd()
	else:
		folder = _.switches.value('Folders')
	global baseDepth
	global base_path
	baseDepth = len( folder.split(_v.slash) )
	base_path=folder
	if not _.switches.isActive('Widget-V0'):
		getFolder(folder,r=r)
	else:
		# _.pr(_v.w)
		base_path=_v.widgets
		_.switches.fieldSet( 'Remove-Root-Folder', 'active', True )
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
		if not i == iS:
		# if _.switches.isActive('Size'):
			_.colorThis( [  '\n', _.addComma(iS), 'of', _.addComma(i), '\n'  ], 'yellow' )
		else:
			_.colorThis( [  '\n{}\n'.format( _.addComma(i) )  ], 'yellow' )
		# _.pr('\n{}\n'.format(i))

extensionList = []

i = 0
iS = 0
baseDepth = 0

# if _.switches.isActive('Ago'):
import _rightThumb._dir as _dir

# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
# 'Recursive'
########################################################################################
if __name__ == '__main__':
	action()