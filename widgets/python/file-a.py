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
	# _blowfish.genPassword('string')
import _rightThumb._mimetype as _mime


	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
##################################################

def appSwitches():

	_.switches.register('Folder', '-f,-folder')
	_.switches.register('Path', '-p')
	_.switches.register('Text', '-t,-text')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('Extensions', '-ext', 'image, video, audio, document')
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('NoExtension', '-noext,-noextension')
	_.switches.register('Label', '-label',';tApp')
	_.switches.register('Prefix', '-prefix',';t')
	_.switches.register('Silent', '-silent')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Totals', '-total,-totals')



	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


	

_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'file.py',
	'liveAppName': __.thisApp( __file__ ),
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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	_.switches.trigger( 'Size' , unFormatSize )
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START



def formatPrint( item, noPrefix=False ):
	if _.switches.isActive( 'NoExtension' ):
		if '.' in item:
			s = item.split('.')
			s.reverse()
			ext = s[0]
			item = item[:-(len(ext)+1)]
		else:
			item = item.replace( ' \t', ' ' )
	if _.switches.isActive( 'Prefix' ) and not noPrefix:
		item = _.ci(_.switches.value( 'Prefix' )) + item

	return item



def silent():
	global files
	global folders
	global recursive
	
	if _.switches.isActive( 'Recursive' ):
		recursive = True
	else:
		recursive = False


	if _.switches.isActive( 'NoExtension' ):
		pass

	if _.switches.isActive( 'Folder' ):
		folder = _.switches.values( 'Folder' )[0]
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
		path = folder + '\\' + item
		if os.path.isfile(path):
			i = i + 1

				
			

			if _.showLine( item ) or _.showLine( formatPrint(item) ):
			# if _.showLine( formatPrint(item) ):
				# if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
				#     i = i + 1
				#     if _.switches.isActive('Path'):
				#         files.append( path )
				#     elif not _.switches.isActive('Count'):
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
				#     if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and _mime.isText(path):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )

						
				#     if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )
						

				#     if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not _mime.isText(path):
				#         i = i + 1

				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )

						
				#     if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
				#         i = i + 1


				#         if not recursive:
				#             files.append( formatPrint(item,noPrefix=True) )
				#         else:
				#             files.append( path )



				pass
				shouldPrint = False

				if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
					# _.pr(0,whatIsIt(path),path)
					# _.pr(path)
					shouldPrint = True
				else:
					if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
						# _.pr(1,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
						# _.pr(2,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
						# _.pr(3,whatIsIt(path),path)
						# _.pr(path)
						shouldPrint = True
					if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
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
							shouldPrint = True
						else:
							if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
								
								shouldPrint = True
							if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
								shouldPrint = True
							if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
								shouldPrint = True
							if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
								shouldPrint = True



						if shouldPrint:
							shouldPrint = False
							
							if _.switches.isActive('Count'):
								_.pr( _.colorThis( path, 'cyan', p=0 ) )
							else:

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
								result += _.colorThis( path, 'cyan', p=0 )

								_.pr( result )
							
							# _.pr( formatedSize, '\t', path )


				if shouldPrint:

					global extensionList
					if len( extensionList ):
						# _.pr( 'here' )
						# sys.exit()
						if '.' in item:
							pathy = item.lower().split('.')
							pathy_test = pathy.pop()
							# _.pr(pathy_test)
							if not '.'+pathy_test in extensionList:
								shouldPrint = False



				if shouldPrint:
					if not recursive:
						if not _.switches.isActive('Totals'):
							if _.switches.isActive('Count'):
								_.colorThis( [  formatPrint(item)  ], 'cyan' )
							else:
								_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
						files.append( formatPrint(item,noPrefix=True) )
					else:
						if not _.switches.isActive('Totals'):
							_.colorThis( [  path  ], 'cyan' )
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
	recursive = _.switches.isActive('Recursive')
	if _.switches.isActive('Extensions'):
		extensionsDatabank()

	# _.pr( 'HERE' )
	# sys.exit()

	if _.switches.isActive( 'Silent' ):
		return silent()


	if _.switches.isActive( 'Folder' ):
		folder = _.switches.values( 'Folder' )[0]
	else:
		folder = os.getcwd()
	# _.pr( folder )
	# sys.exit()
	if not _.switches.isActive('Count'):
		if not _.switches.isActive('Label'):
			_.pr()
			_.colorThis( 'Files:\n', 'green' )
		else:
			_.colorThis( [ _.ci(_.switches.value( 'Label' )) + ':\n' ], 'green' )
	global i
	global files
	
	if recursive:
		getFolder( folder )
	elif not recursive:
		dirList = os.listdir(folder)
		for item in dirList:
			path = folder + '\\' + item
			if os.path.isfile(path):
				i = i + 1
			# if os.path.isdir(item):
				if _.showLine( formatPrint(item) ):

					if len( extensionList ):
						# _.pr( 'here' )
						# sys.exit()
						if '.' in item:
							# _.pr( item )
							pathy = item.lower().split('.')
							pathy_test = pathy.pop()
							if '.'+pathy_test in extensionList:
								# _.pr(pathy_test)
								if not _.switches.isActive('Totals'):
									if _.switches.isActive('Count'):
										_.colorThis( [  formatPrint(item)  ], 'cyan' )
									else:
										_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
					else:

						if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
							# _.pr(0,_mime.what(path),path)
							# _.pr(path)

							if _.switches.isActive('Path'):
								if not _.switches.isActive('Totals'):
									_.pr( path )
								files.append( path,noPrefix=True )
							elif not _.switches.isActive('Count'):
								if not _.switches.isActive('Totals'):
									_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								# _.pr( '\t', formatPrint(item) )
								files.append( formatPrint(item,noPrefix=True) )
							else:
								# _.pr( formatPrint(item) )
								if not _.switches.isActive('Totals'):
									_.colorThis( [  formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
						else:
							if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and _mime.isText(path):
								# _.pr(1,_mime.what(path),path)
								# _.pr(path)
								# _.pr( '\t', formatPrint(item) )
								if not _.switches.isActive('Totals'):
									if _.switches.isActive('Count'):
										_.colorThis( [  formatPrint(item)  ], 'cyan' )
									else:
										_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
							if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
								# _.pr(2,_mime.what(path),path)
								# _.pr(path)
								# _.pr( '\t', formatPrint(item) )
								if not _.switches.isActive('Totals'):
									if _.switches.isActive('Count'):
										_.colorThis( [  formatPrint(item)  ], 'cyan' )
									else:
										_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )

							if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not _mime.isText(path):
								# _.pr(3,_mime.what(path),path)
								# _.pr(path)
								# _.pr( '\t', formatPrint(item) )
								if not _.switches.isActive('Totals'):
									if _.switches.isActive('Count'):
										_.colorThis( [  formatPrint(item)  ], 'cyan' )
									else:
										_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )
							if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
								
								# _.pr(4,_mime.what(path),path)
								# _.pr(path)
								# _.pr( '\t', formatPrint(item) )
								if not _.switches.isActive('Totals'):
									if _.switches.isActive('Count'):
										_.colorThis( [  formatPrint(item)  ], 'cyan' )
									else:
										_.colorThis( [  '\t', formatPrint(item)  ], 'cyan' )
								files.append( formatPrint(item,noPrefix=True) )

	# if _.switches.isActive('Count') == False and _.switches.isActive('NoFolder') == False:
	#     _.pr('\n{}\n{}'.format(i,folder))
	# if _.switches.isActive('NoFolder'):
	#     _.pr('',i)
	if not len(files) == i:
		# _.pr('HERE')
		_.folderProfileAttribute( folder=folder, info = {
														'app': 'file',
														'recursive': _.switches.isActive('Recursive'),
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
																		'MinuVals': _.switches.values('Minus'),
														},
														'percentage': _.pDiff( len(files), i, use='less' ),
														'count': len(files),
														'files': i ,

		} )
	if _.switches.isActive('Label'):
		c = _v.myTemp + '\\app(file.py)_Count.txt'
		_.saveText( str( len(files) ), c )
		f = _v.myTemp + '\\app(file.py).txt'
		if os.path.isfile( f ):
			os.remove( f )
		if len(files) == 1:
			_.saveText( files[0], f )
	if not _.switches.isActive('Count'):

		if not len(files) == i:
			_.colorThis( [  '\n', _.addComma( len(files) ), 'of', _.addComma(i), '\n'  ], 'yellow' )

		else:

			if i == 0:
				if not _.switches.isActive('Label'):
					_.colorThis( [  formatPrint('\tNo Files')  ], 'red' )
					# _.pr( formatPrint('\tNo Files') )
				else:
					_.colorThis( [  formatPrint('\tNo ' +_.ci(_.switches.value( 'Label' )))  ], 'red' )
					# _.pr( formatPrint('\tNo ' +_.ci(_.switches.value( 'Label' ))) )
			# _.pr('',i)
			_.colorThis( [  '',i  ], 'yellow' )
			_.pr()
			_.colorThis( [  folder  ], 'darkcyan' )
			



	pass
	# global data
	# load()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner()
	#     # _.printVar(_.appData)
	#     for i,row in enumerate(_.appData[__.appReg]['pipe']):
	#         pass



# def load():
#     global data
#     data = _.getTable( 'table.json' )

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


extensionList = []
i=0
# data = []
files = []
folders = []
recursive = False
########################################################################################
if __name__ == '__main__':
	action()