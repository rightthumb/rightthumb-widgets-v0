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
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
	# _blowfish.genPassword('string')
import _rightThumb._mimetype as _mime


	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
##################################################

def sw():

	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='' )
	_.switches.register('Folder', '-folder')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register('Editor', '-editor')
	_.switches.register('Scan', '-scan', 'r fix')
	_.switches.register('NoPrint', '--c')
	# _.switches.register('Spaces', '-spaces')
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
	'file': 'shClean.py',
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
def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
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
	sw()

	_.myFileLocation_Print = False
	# _.switches.trigger('Files',_.myFileLocations)
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

def getFolder(folder):
	dirList = os.listdir(folder)
	# i = 0

	for item in dirList:
		path = folder + _v.slash + item
		path = path.replace(os.sep+os.sep,os.sep)
		path = path.replace(os.sep+os.sep,os.sep)
		if os.path.isfile(path):
			if path.endswith('.sh') or path.endswith('.py') or path.endswith('.bat'):
				if _.showLine(path):
					processFile(path)

		if os.path.isdir(path):
			if _.switches.isActive( 'Recursive' ):
				try:
					getFolder(path)
				except Exception as e:
					pass
import re

def replace_leading_spaces_with_tab(file_content):
	# Split the file content into lines
	lines = file_content.split("\n")
	# Iterate over the lines
	for i in range(len(lines)):
		# Replace leading spaces with a tab
		lines[i] = re.sub(r"^    +", lambda m: "\t" * (len(m.group()) // 4), lines[i])
	# Join the lines back into a single string
	file_content = "\n".join(lines)
	return file_content


def processFile(path):
	if not os.path.isfile(path):
		return None
	if not _.isWin:
		try:
			os.chmod( path, 0o777 )
		except Exception as e:
			pass
	if not _.switches.isActive('NoPrint'): _.cp( [ 'CLEANED:', path ], 'cyan' )
	file = _.getText( path, raw=True )
	file = file.replace( chr(10), '\n' )
	file = file.replace( chr(27), '' )
	file = file.replace( '\r', '' )
	file=file.rstrip()
	file = replace_leading_spaces_with_tab(file)
	# if _.switches.isActive('Spaces'):
	#     while '\t' in file: file = file.replace( '\t', '    ' )
	# else:
	#     while '\t' in file: file = file.replace( '    ', '\t' )
	if _.switches.isActive('Editor'):
		file = file.replace( 'subl', _.switches.value('Editor') )

	_.saveText( file, path )

def fileCheck(file):
	data = _.getText(file,raw=True)
	# if chr(10) in data or chr(27) in data:
	if chr(27) in data:
		return True
	return False

def action():
	if _.switches.isActive('Scan'):
		if 'r' in _.switches.value('Scan'):
			r = True
		else:
			r = False
		if 'f' in _.switches.value('Scan'):
			f = True
		else:
			f = False
		for file in _.fo(r=r):
			if file.endswith('.sh') or file.endswith('.py') or file.endswith('.bat'):
				if fileCheck(file):
					if _.showLine(file):
						if f:
							if not os.path.isfile(file) and os.path.isfile(__.wsl(file)):
								file=__.wsl(file)
							if not os.path.isfile(file):
								continue
							processFile(file)
						# _.pr(file)

		return None
	for path in _.switches.values('Files'):
		if '*' in path:
			for f in glob.glob( path ):
				if _.showLine(f):
					f = __.path(f)
					if not os.path.isfile(f) and os.path.isfile(__.wsl(f)):
						f=__.wsl(f)
					if not os.path.isfile(f):
						continue
					processFile(f)

		elif not '*' in path:
			f = path
			# path=__.path(path)
			if _.showLine(f):
				f = __.path(f)
				w = __.wsl(f)
				print(w)
				if not os.path.isfile(f) and os.path.isfile(__.wsl(f)):
					f=__.wsl(f)
				if not os.path.isfile(f):
					continue
				processFile(f)
					# processFile(path)


	if _.switches.isActive( 'Folder' ):
		if len( _.switches.value('Folder') ):
			for folder in _.switches.values( 'Folder' ):
				getFolder(folder)
			
		else:
			folder = os.getcwd()
			getFolder(folder)


	else:
		_.pipeCleaner(0)
		for i,row in enumerate(_.isData(r=1)):
			if _.showLine(row):
				processFile(row)


import glob


########################################################################################
if __name__ == '__main__':
	action()






