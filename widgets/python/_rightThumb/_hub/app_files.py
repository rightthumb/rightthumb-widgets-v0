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

import sys, os
from _rightThumb._hub import app
from _rightThumb._hub import _func as _
from _rightThumb._hub import _vars as _v

reg = app.space(__name__, __file__)
app.reg = reg
reg.rent = app.register(reg)
app.rent = app.focus(reg.rent)
app.switches()
app.fields()
# app.tables()

def app_switches():

	app.switch.reg('Count', '-c,-count,--c')
	app.switch.reg('Path', '-p,-path,-folder')
	app.switch.reg('Text', '-t,-text,-txt')
	app.switch.reg('Binary', '-bin')
	app.switch.reg('Size', '-size',' g 10mb, L 2kb ')
	# app.switch.reg('Extensions', '-ext', 'image, video, audio, document')
	app.switch.reg('Totals', '-total,-totals')
	app.switch.reg('FolderRefine', '-fr')
	app.switch.reg('Ago', '-ago', '1m')
	app.switch.reg('MaxDepth', '-depth', '3')
	app.switch.reg('Extensions', '-ext', 'db image graphic video app audio doc script archive')

reg.documentation = {
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

# reg.documentation['examples'].append('p thisApp -file file.txt')

# reg.documentation['columns'].append({'name': 'name', 'abbreviation': 'n'})

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

def sw( argvProcessForce=False ):
	global appDBA
	if True:

		if not __name__ == '__main__':
			app.argv_process = argvProcessForce
		else:
			app.argv_process = True

		app.load()
	app.construct_registration(reg.documentation['file'],app.rent)
	app_switches()

	app.switch.trigger( 'Size' , unFormatSize )
	# app.switch.trigger('Input',app.myFileLocations)
		# trigger settings
	app.myFileLocation_Print = False

	# app.switch.trigger('Watched', app.txt2Date)
	# app.switch.trigger('Input',app.formatColumns)
	
	app.default_script_triggers()
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
reg.data['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		app.set_pipe_data( sys.stdin.readlines(), app.rent )
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

def getFolder(folder):
	if folder.startswith('/proc'):
		return None
	global i
	global iS
	global baseDepth
	if app.switch.isActive('MaxDepth'):
		if len(app.switch.value('MaxDepth')):
			maxDepth = int(app.switch.values('MaxDepth')[0])
		else:
			maxDepth = 4
		if len( folder.split(_v.slash) ) - baseDepth >= maxDepth:
			if len(app.switch.values('MaxDepth')) > 1 and 'p' in app.switch.values('MaxDepth')[1]:
				print( folder )

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
				i = i + 1

				if app.showLine(path):
					shouldAdd = False

					if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
						# print(0,whatIsIt(path),path)
						# print(path)
						shouldAdd = True
					else:
						if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(path):
							# print(1,whatIsIt(path),path)
							# print(path)
							shouldAdd = True
						if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
							# print(2,whatIsIt(path),path)
							# print(path)
							shouldAdd = True
						if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(path):
							# print(3,whatIsIt(path),path)
							# print(path)
							shouldAdd = True
						if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
							# print(4,whatIsIt(path),path)
							# print(path)
							shouldAdd = True

					pass

					pass
					if app.switch.isActive('Ago'):
						# sys.exit()
						record = _dir.fileInfo( path )
						# print( app.switch.values('Ago'), record['date_modified_raw'], record['date_created_raw'],  )
						# if os.path.isfile(path):
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

						# print( run, agoRange, app.switch.values('Ago')[0], app.friendlyDate(app.switch.values('Ago')[0]) )

						if not agoRange:
							if run == 'default':
								if record['date_modified_raw'] > app.switch.values('Ago')[0] or record['date_created_raw'] > app.switch.values('Ago')[0]:
									shouldAdd = True
									# print(path)
							elif run == 'resent':
								if record['date_modified_raw'] > app.switch.values('Ago')[0] or record['date_created_raw'] > app.switch.values('Ago')[0] or record['accessed_raw'] > app.switch.values('Ago')[0]:
									shouldAdd = True
							elif run == 'a':
								if record['accessed_raw'] > app.switch.values('Ago')[0]:
									# print( app.friendlyDate(app.switch.values('Ago')[0]), app.switch.values('Ago')[0], record['accessed_raw'], app.friendlyDate(record['accessed_raw']) )
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

					pass

					pass
					# if shouldAdd: print( 1001, path );
					if shouldAdd:
						if app.switch.isActive('Size'):
							shouldAdd = False
							shouldAdd_2 = False
							stat = os.stat(path)
							size = stat.st_size
							if 'l' in app.switch.values('Size')[0]:
								if size < app.switch.values('Size')[1]:
									shouldAdd_2 = True
							if 'g' in app.switch.values('Size')[0]:
								if size > app.switch.values('Size')[1]:
									shouldAdd_2 = True

							if shouldAdd_2:
								shouldAdd = False

								if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
									
									shouldAdd = True
								else:
									if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(path):
										shouldAdd = True
									if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
										shouldAdd = True
									if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(path):
										shouldAdd = True
									if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
										shouldAdd = True

							if shouldAdd:
								shouldAdd = False
								
								if app.switch.isActive('Count'):
									print( app.cp( path, 'cyan', p=0 ) )
								else:
									iS+=1

									formatedSize = formatSize( size )
									formatedSize = app.field.value( 'files', 'name', formatedSize )
									result = ''
									fs = formatedSize.split(' ')
									result += app.cp( fs[0], 'Color.purple', p=0 )
									result += ' '
									result += app.cp( fs[1], 'Color.darkcyan', p=0 )
									fs.reverse()
									fs.pop()
									fs.pop()
									fs.reverse()
									result += ' '.join(fs)
									result += '\t'
									result += app.cp( path, 'cyan', p=0 )

									print( result )
								
								# print( formatedSize, '\t', path )
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
						iS+=1
						if not app.switch.isActive('Totals'):
							if not app.switch.isActive('Plus'):
								app.cp( path, 'cyan' )
							else:
								print( app.colorPlus( path, 'cyan' ) )

					# if shouldAdd:
					#     text_binary = False
					#     if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
					#         text_binary = True
					#     else:
					#         if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(path):
					#             text_binary = True
					#         if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
					#             text_binary = True
					#         if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(path):
					#             text_binary = True
					#         if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
					#             text_binary = True
					#     if not text_binary:
					#         shouldAdd = False
			# if os.path.isdir(path) and app.showLine(path):
			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					shouldRun = True
					if app.switch.isActive('FolderRefine'):
						if not app.showLine(newFolder):
							shouldRun = False
					if shouldRun:
						try:
							getFolder(newFolder)
						except Exception as e:
							pass
				else:
					print('error')
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

def action():
	if app.switch.isActive('Extensions'):
		extensionsDatabank()
	app.field.register( 'files', 'name', '1000.43 KB' )
	global i
	global iS
	# load()
	if app.switch.isActive('Path') == False:
		folder = os.getcwd()
	else:
		folder = app.switch.value('Path')
	global baseDepth
	baseDepth = len( folder.split(_v.slash) )
	getFolder(folder)
	"""
	if app.switch.isActive('Extensions'):
		folderProfileAttribute( folder=folder, info={
														'recursive': True,
														'count': iS,
														'files': i ,
														'diff': app.pDiff( iS, i, use='less' ) ,
		} )
	"""
	if not iS == i:
		app.folderProfileAttribute( folder=folder, info = {
														'app': 'files',
														'recursive': True,
														'factors': {
																		'Text': app.switch.isActive('Text'),
																		'Binary': app.switch.isActive('Binary'),
																		'Extensions': app.switch.isActive('Extensions'),
																		'Type': app.switch.values('Extensions'),

																		'PlusOr': app.switch.isActive('PlusOr'),
																		'PlusClose': app.switch.isActive('PlusClose'),
																		'Plus': app.switch.isActive('Plus'),
																		'Minus': app.switch.isActive('Minus'),
																		
																		'PlusVals': app.switch.values('Plus'),
																		'MinusVals': app.switch.values('Minus'),
														},
														'percentage': app.pDiff( iS, i, use='less' ),
														'count': iS,
														'files': i,

		} )

	if app.switch.isActive('Count') == False:
		if not i == iS:
		# if app.switch.isActive('Size'):
			app.cp( [  '\n', app.addComma(iS), 'of', app.addComma(i), '\n'  ], 'yellow' )
		else:
			app.cp( [  '\n{}\n'.format( app.addComma(i) )  ], 'yellow' )
		# print('\n{}\n'.format(i))

extensionList = []

i = 0
iS = 0
baseDepth = 0

# if app.switch.isActive('Ago'):
import _rightThumb._dir as _dir

# def load():
#     global data
#     data = app.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()




