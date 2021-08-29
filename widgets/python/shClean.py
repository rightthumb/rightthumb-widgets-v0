#!/usr/bin/python3
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

	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='' )
	_.switches.register('Folder', '-folder')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Editor', '-editor')
	# _.switches.register('Path', '-p')
	# _.switches.register('Text', '-t,-text')
	# _.switches.register('Binary', '-bin')
	# _.switches.register('Size', '-size',' g 10mb, L 2kb ')
	# _.switches.register('Extensions', '-ext', 'image, video, audio, document')
	# _.switches.register('Count', '-c,-count,--c')
	# _.switches.register('NoExtension', '-noext,-noextension')
	# _.switches.register('Label', '-label',';tApp')
	# _.switches.register('Prefix', '-prefix',';t')
	# _.switches.register('Silent', '-silent')
	# _.switches.register('Recursive', '-r,-recursive')
	# _.switches.register('Totals', '-total,-totals')



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
						'p shClean -f d.sh',
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
	elif size > 1073741824 and size < 1099511627776	:
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	# 	result = ''
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
# 	if os.path.isdir(row):
# 	if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START

def getFolder(folder):
	dirList = os.listdir(folder)
	# i = 0

	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(path):
			if path.endswith('.sh') or path.endswith('.py'):
				processFile(path)

		if os.path.isdir(path):
			if _.switches.isActive( 'Recursive' ):
				try:
					getFolder(path)
				except Exception as e:
					pass

def processFile(path):
	if _.isWin:
		os.chmod( path, '777' )
	_.cp( [ 'CLEANED:', path ], 'cyan' )
	file = _.getText( path, raw=True )
	file = file.replace( chr(10), '\n' )
	file = file.replace( chr(27), '' )
	file = file.replace( '\r', '' )
	if _.switches.isActive('Editor'):
		file = file.replace( 'subl', _.switches.value('Editor') )

	_.saveText( file, path )



def action():

	for path in _.switches.values('Files'):
		processFile(path)


	if _.switches.isActive( 'Folder' ):
		if len( _.switches.value('Folder') ):
			folder = _.switches.values( 'Folder' )[0]
		else:
			folder = os.getcwd()

		getFolder(folder)

	else:
		_.pipeCleaner(0)
		for i,row in enumerate(_.isData(r=1)):
			processFile(row)



########################################################################################
if __name__ == '__main__':
	action()



