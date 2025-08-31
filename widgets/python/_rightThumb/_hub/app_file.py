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

# for i,arg in enumerate(sys.argv):
#     print('file',i,arg)

from _rightThumb._hub import _construct as __
from _rightThumb._hub import app
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _func as _
reg = app.space(__name__, __file__)
app.debug()
app.reg = reg
reg.rent = app.register(reg)
__.rent=reg.rent
app.rent = app.focus(reg.rent)


app.rent = '123'
reg.rent = '123'


app.switches()
# app.tables()
def app_switches():
	app.switch.reg('Help', '?,??,/?,-?,/h,/help,-help,--help', 'copy  OR ids  OR  12  OR  ?? x')
	app.switch.reg('Folder', '-f,-folder')
	app.switch.reg('Path', '-p')
	app.switch.reg('Text', '-t,-text')
	app.switch.reg('Binary', '-bin')
	app.switch.reg('Size', '-size',' g 10mb, L 2kb ')
	app.switch.reg('Extensions', '-ext', 'image, video, audio, document')
	app.switch.reg('Count', '-c,-count,--c')
	app.switch.reg('NoExtension', '-noext,-noextension')
	app.switch.reg('Label', '-label',';tApp')
	app.switch.reg('Prefix', '-prefix',';t')
	app.switch.reg('Silent', '-silent')
	app.switch.reg('Recursive', '-r,-recursive')
	app.switch.reg('Totals', '-total,-totals')

	app.switch.reg('Plus', '+')
	app.switch.reg('Minus', '-')
	app.switch.reg('PlusOr', '-or')
	app.switch.reg('PlusClose', '+close', '90%')

	# app.switch.reg( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
	# app.switch.reg( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )
	

app.autoBackupData = True
reg.documentation = {
	'file': 'file.py',
	'liveAppName': app.this_app( __file__ ),
	'description': 'Displays file in folder',
	'categories': [
						'file',
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
						'p file',
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

def sw( argvProcessForce=True ):
	
	if True:

		if not __name__ == '__main__':
			app.argv_process = argvProcessForce
		else:
			app.argv_process = True

		app.load()
	app.construct_registration(reg.documentation['file'],app.rent)
	app_switches()

	app.myFileLocation_Print = False
	app.switch.trigger('Files',app.myFileLocations)
	# app.switch.trigger('Files',app.inRelevantFolder)
	

	# app.switch.trigger('Watched', app.txt2Date)
	# app.switch.trigger('Input',app.formatColumns)
	# app.switch.trigger('Franchise',app.triggerSpace)
	app.switch.trigger( 'Size' , unFormatSize )
	# app.default_script_triggers()
	app.switch.process(arg=True)

if not __name__ == '__main__':
	app.argv_process = False
	app.argv_process = True
else:
	app.argv_process = True
def loader():
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
# p = app.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# app.set_pipe_data( os.listdir(os.getcwd()), focus() )
# app.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# app.rentPipe
########################################################################################
# START

def formatPrint( item, noPrefix=False ):
	if app.switch.isActive( 'NoExtension' ):
		if '.' in item:
			s = item.split('.')
			s.reverse()
			ext = s[0]
			item = item[:-(len(ext)+1)]
		else:
			item = item.replace( ' \t', ' ' )
	if app.switch.isActive( 'Prefix' ) and not noPrefix:
		item = app.ci(app.switch.value( 'Prefix' )) + item

	return item

def silent():
	global files
	global folders
	global recursive
	
	if app.switch.isActive( 'Recursive' ):
		recursive = True
	else:
		recursive = False
	if app.switch.isActive( 'NoExtension' ):
		pass

	if app.switch.isActive( 'Folder' ):
		folder = app.switch.values( 'Folder' )[0]
	else:
		folder = os.getcwd()

	getFolder( folder )
	return { 'files': files, 'folders': folders  }
def getFolder( folder ):
	global files
	global folders
	global recursive
	global i
	dirList = os.listdir(folder)
	# i = 0

	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(path):
			i = i + 1

				
			

			if app.showLine( item ) or app.showLine( formatPrint(item) ):
			# if app.showLine( formatPrint(item) ):
				# if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
				#     i = i + 1
				#     if app.switch.isActive('Path'):
				#         files.append( path )
				#     elif not app.switch.isActive('Count'):
				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )
				#     else:
				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )
						
				# else:
				#     if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and _mime.isText(path):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )

						
				#     if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )
						

				#     if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not _mime.isText(path):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )

						
				#     if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
				#         i = i + 1
				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )

				pass
				shouldPrint = False

				if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
					# print(0,whatIsIt(path),path)
					# print(path)
					shouldPrint = True
				else:
					if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(path):
						# print(1,whatIsIt(path),path)
						# print(path)
						shouldPrint = True
					if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
						# print(2,whatIsIt(path),path)
						# print(path)
						shouldPrint = True
					if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(path):
						# print(3,whatIsIt(path),path)
						# print(path)
						shouldPrint = True
					if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
						# print(4,whatIsIt(path),path)
						# print(path)
						shouldPrint = True

				if app.switch.isActive('Size'):
					shouldPrint = False
					shouldPrint_2 = False
					stat = os.stat(path)
					size = stat.st_size
					if 'l' in app.switch.values('Size')[0]:
						if size < app.switch.values('Size')[1]:
							shouldPrint_2 = True
					if 'g' in app.switch.values('Size')[0]:
						if size > app.switch.values('Size')[1]:
							shouldPrint_2 = True

					if shouldPrint_2:
						shouldPrint = False

						if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
							shouldPrint = True
						else:
							if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and isText(path):
								
								shouldPrint = True
							if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
								shouldPrint = True
							if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not isText(path):
								shouldPrint = True
							if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
								shouldPrint = True

						if shouldPrint:
							shouldPrint = False
							
							if app.switch.isActive('Count'):
								print( app.cp( path, 'cyan', p=0 ) )
							else:

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
				if shouldPrint:

					global extensionList
					if len( extensionList ):
						# print( 'here' )
						# sys.exit()
						if '.' in item:
							pathy = item.lower().split('.')
							pathy_test = pathy.pop()
							# print(pathy_test)
							if not '.'+pathy_test in extensionList:
								shouldPrint = False

				if shouldPrint:
					if not recursive:
						if not app.switch.isActive('Totals'):
							if app.switch.isActive('Count'):
								app.cp( [  formatPrint(item)  ], 'cyan' )
							else:
								app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
						files.append( formatPrint(item,noPrefix=True) )
					else:
						if not app.switch.isActive('Totals'):
							app.cp( [  path  ], 'cyan' )
						files.append( path )

		if os.path.isdir( path ):
			if recursive:
				getFolder( path )
				folders.append( path )
			else:
				folders.append( item )

def action():
	global extensionList
	global recursive
	recursive = app.switch.isActive('Recursive')
	if app.switch.isActive('Extensions'):
		extensionsDatabank()

	# print( 'HERE' )
	# sys.exit()

	if app.switch.isActive( 'Silent' ):
		return silent()
	if app.switch.isActive( 'Folder' ):
		folder = app.switch.values( 'Folder' )[0]
	else:
		folder = os.getcwd()
	# print( folder )
	# sys.exit()
	if not app.switch.isActive('Count'):
		if not app.switch.isActive('Label'):
			print()
			app.cp( 'Files:\n', 'green' )
		else:
			app.cp( [ app.ci(app.switch.value( 'Label' )) + ':\n' ], 'green' )
	global i
	global files
	
	if recursive:
		getFolder( folder )
	elif not recursive:
		dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			if os.path.isfile(path):
				i = i + 1
			# if os.path.isdir(item):
				if app.showLine( formatPrint(item) ):

					if len( extensionList ):
						# print( 'here' )
						# sys.exit()
						if '.' in item:
							# print( item )
							pathy = item.lower().split('.')
							pathy_test = pathy.pop()
							if '.'+pathy_test in extensionList:
								# print(pathy_test)
								if not app.switch.isActive('Totals'):
									if app.switch.isActive('Count'):
										app.cp( [  formatPrint(item)  ], 'cyan' )
									else:
										app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
					else:

						if not app.switch.isActive('Text') and not app.switch.isActive('Binary'):
							# print(0,_mime.what(path),path)
							# print(path)

							if app.switch.isActive('Path'):
								if not app.switch.isActive('Totals'):
									print( path )
								files.append( path,noPrefix=True )
							elif not app.switch.isActive('Count'):
								if not app.switch.isActive('Totals'):
									app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								# print( '\t', formatPrint(item) )
								files.append( formatPrint(item,noPrefix=True) )
							else:
								# print( formatPrint(item) )
								if not app.switch.isActive('Totals'):
									app.cp( [  formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
						else:
							if not app.switch.isActive('Binary') and  app.switch.isActive('Text') and _mime.isText(path):
								# print(1,_mime.what(path),path)
								# print(path)
								# print( '\t', formatPrint(item) )
								if not app.switch.isActive('Totals'):
									if app.switch.isActive('Count'):
										app.cp( [  formatPrint(item)  ], 'cyan' )
									else:
										app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
							if not app.switch.isActive('Binary') and not app.switch.isActive('Text'):
								# print(2,_mime.what(path),path)
								# print(path)
								# print( '\t', formatPrint(item) )
								if not app.switch.isActive('Totals'):
									if app.switch.isActive('Count'):
										app.cp( [  formatPrint(item)  ], 'cyan' )
									else:
										app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )

							if not app.switch.isActive('Text') and  app.switch.isActive('Binary') and not _mime.isText(path):
								# print(3,_mime.what(path),path)
								# print(path)
								# print( '\t', formatPrint(item) )
								if not app.switch.isActive('Totals'):
									if app.switch.isActive('Count'):
										app.cp( [  formatPrint(item)  ], 'cyan' )
									else:
										app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
							if not app.switch.isActive('Text') and  not app.switch.isActive('Binary'):
								
								# print(4,_mime.what(path),path)
								# print(path)
								# print( '\t', formatPrint(item) )
								if not app.switch.isActive('Totals'):
									if app.switch.isActive('Count'):
										app.cp( [  formatPrint(item)  ], 'cyan' )
									else:
										app.cp( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )

	# if app.switch.isActive('Count') == False and app.switch.isActive('NoFolder') == False:
	#     print('\n{}\n{}'.format(i,folder))
	# if app.switch.isActive('NoFolder'):
	#     print('',i)
	# if not len(files) == i:
		
	#     app.folderProfileAttribute( folder=folder, info = {
	#                                                     'app': 'file',
	#                                                     'recursive': app.switch.isActive('Recursive'),
	#                                                     'factors': {
	#                                                                     'Text': app.switch.isActive('Text'),
	#                                                                     'Binary': app.switch.isActive('Binary'),
	#                                                                     'Extensions': app.switch.isActive('Extensions'),
	#                                                                     'Type': app.switch.values('Extensions'),

	#                                                                     'PlusOr': app.switch.isActive('PlusOr'),
	#                                                                     'PlusClose': app.switch.isActive('PlusClose'),
	#                                                                     'Plus': app.switch.isActive('Plus'),
	#                                                                     'Minus': app.switch.isActive('Minus'),

	#                                                                     'PlusVals': app.switch.values('Plus'),
	#                                                                     'MinuVals': app.switch.values('Minus'),
	#                                                     },
	#                                                     'percentage': app.pDiff( len(files), i, use='less' ),
	#                                                     'count': len(files),
	#                                                     'files': i ,

	#     } )
	if app.switch.isActive('Label'):
		c = _v.myTemp + _v.slash+'app(file.py)_Count.txt'
		app.saveText( str( len(files) ), c )
		f = _v.myTemp + _v.slash+'app(file.py).txt'
		if os.path.isfile( f ):
			os.remove( f )
		if len(files) == 1:
			app.saveText( files[0], f )
	if not app.switch.isActive('Count'):

		if not len(files) == i:
			app.cp( [  '\n', app.addComma( len(files) ), 'of', app.addComma(i), '\n'  ], 'yellow' )

		else:

			if i == 0:
				if not app.switch.isActive('Label'):
					app.cp( [  formatPrint('\tNo Files')  ], 'red' )
					# print( formatPrint('\tNo Files') )
				else:
					app.cp( [  formatPrint('\tNo ' +app.ci(app.switch.value( 'Label' )))  ], 'red' )
					# print( formatPrint('\tNo ' +app.ci(app.switch.value( 'Label' ))) )
			# print('',i)
			app.cp( [  '',i  ], 'yellow' )
			print()
			app.cp( [  folder  ], 'darkcyan' )
			

	pass
	# global data
	# load()

	# if not type( reg.data['pipe'] ) == bool:
	#     app.pipeCleaner()
	#     # app.printVar(app.appData)
	#     for i,row in enumerate(reg.data['pipe']):
	#         pass

# def load():
#     global data
#     data = app.getTable( 'table.json' )
	print( app.stack.fn() )

def extensionsDatabank():
	global extensionList
	_db = app.regImp( app.rent, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )
	_db.switch( 'Plus', app.switch.values('Extensions') )
	extensionList = _db.do( 'action' )
	for i,x in enumerate(extensionList):
		extensionList[i] = x.lower()
	# print( extensionList )
extensionList = []
i=0
# data = []
files = []
folders = []
recursive = False
########################################################################################
if __name__ == '__main__':
	action()


