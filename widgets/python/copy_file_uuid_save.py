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

def appSwitches():
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Path', '-p,-path,-folder')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')
	_.switches.register('Size', '-size',' g 10mb, L 2kb ')
	_.switches.register('Extensions', '-ext', 'image, video, audio, document')
	_.switches.register('Totals', '-total,-totals')
	_.switches.register('FolderRefine', '-fr')
	_.switches.register('SaveFolder', '-save')



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

from shutil import copyfile

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
				i = i + 1

				if _.showLine(path):
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
									result += _.colorThis( path, 'cyan', p=0 )
									processTheFile(path)
									# _.pr( result )
								
								# _.pr( formatedSize, '\t', path )


					if shouldPrint :

						global extensionList
						if len( extensionList ):
							if '.' in path:
								pathy = path.lower().split('.')
								pathy_test = pathy.pop()
								if not '.'+pathy_test in extensionList:
									shouldPrint = False



					if shouldPrint:
						iS+=1
						if not _.switches.isActive('Totals'):
							if not _.switches.isActive('Plus'):
								processTheFile(path)
							else:
								processTheFile(path)

			# if os.path.isdir(path) and _.showLine(path):
			if os.path.isdir(path):
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


def processTheFile(path):
	global epoch
	global theLOG
	pass
	# _.pr( theLOG )
	# sys.exit()
	# newName = _.randomizeCase(  _.longID()  )
	newName = _.longID()
	newName = newName.replace('{','').replace('}','')
	newNameID = newName
	parts = path.split(_v.slash)
	oldname = parts.pop()
	theEXT = ''
	if '.' in oldname:
		extParts = oldname.split('.')
		theEXT = extParts.pop()
		newName += '.'+ theEXT
	SaveFolder = _.switches.values('SaveFolder')[0]
	if not _v.slash in SaveFolder:
		SaveFolder = os.getcwd() + _v.slash + SaveFolder
	if not os.path.isdir(SaveFolder):
		os.mkdir(SaveFolder)
	newPath = SaveFolder + _v.slash + newName
	s = path
	d = newPath
	try:
		result = copyfile( s, d )
	except Exception as e:
		result = 'Error'
	if result == d:
		theLOG[ newName ] = {
								'epoch': epoch,

								'id': newNameID,
								'ext': theEXT,
								
								'original_name': oldname,
								'original_path': path,
								
								'new_name': newName,
								'new_path': newPath,
								
								'save': _.switches.values('SaveFolder')[0]
							}
		_.saveTableDB( theLOG, 'copy_file_uuid_save.index' )
		didR = 'C'
		did = _.colorThis( 'C', 'green', p=0 )
	else:
		didR = 'E'
		did = _.colorThis( 'E', 'red', p=0 )
	_.pr( did, '\t', path )
	# _.pr( newPath )

def action():

	if not _.switches.isActive('SaveFolder') or not len(  _.switches.value('SaveFolder')  ) :
		_.colorThis( [ 'Switch SaveFolder is required' ], 'red' )
		sys.exit()


	global theLOG
	theLOG = _.getTableDB( 'copy_file_uuid_save.index' )


	global i
	global iS
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for ii,row in enumerate( _.appData[__.appReg]['pipe'] ):
			processTheFile(row)

	else:

		if _.switches.isActive('Extensions'):
			extensionsDatabank()


		_.fields.register( 'files', 'name', '1000.43 KB' )

		# load()
		if _.switches.isActive('Path') == False:
			folder = os.getcwd()
		else:
			folder = _.switches.value('Path')
		
		getFolder(folder)
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
															'recursive': True,
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
epoch = time.time()
i = 0
iS = 0
theLOG = {}
# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()







