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

# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################
from shutil import copyfile
##################################################

def appSwitches():
	_.switches.register('Input', '-f,-file','file.txt', isData='name')
	_.switches.register('Insert', '-i,-insert')
	_.switches.register('InsertFile', '-if,-insertfile')
	_.switches.register('Replace', '-r,-replace')
	_.switches.register('ReplaceFile', '-rf,-replacefile')
	_.switches.register('Test', '-test')
	_.switches.register('EntireQuotes', '-q,-quotes')


	


_.appInfo[focus()] = {
	'file': 'replaceText.py',
	'description': 'Replaces text in a file or set of files',
	'categories': [
						'file manipulation',
						'text manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

# epy replaceText
# epy insertText
# epy changeTextEnd
# epy moveText
# epy replaceFunction



_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p replaceText ?')
_.appInfo[focus()]['relatedapps'].append('p insertText ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p changeTextEnd ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p moveText ?')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('p replaceFunction ?')

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p replaceText -i blank20.py -insert "not _.appData[__.appReg][\'pipe\'][0][0] in _str.safeChar" -replace "_.appData[__.appReg][\'pipe\'][0][0].isalnum() == False"')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.py + OLDTEXT - SKIP -jn | p replaceText -insert NEWTEXT -replace OLDTEXT')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.py + "def registerSwitches()"  -jn | p replaceText -insert "def registerSwitches( argvProcessForce=False )" -replace "def registerSwitches()"')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	_.defaultScriptTriggers()

	_.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################
# START

fileBackup = _.regImp( __.appReg, 'fileBackup' )
# fileBackup.switch( 'Silent' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )

insertText = ''
replaceText = ''
def action():
	# _.pv(_.switches.all() ); _.isExit(__file__)
	if _.switches.isActive('Test'):
		_.pr( _.switches.values('Replace')[0] )
		sys.exit()
	global insertText
	global replaceText

	# _.pr( _.switches.value('Input') )
	shouldRun = False
	if _.switches.isActive('InsertFile'):
		if not os.path.isfile( _.switches.value('InsertFile') ):
			_.pr( 'Error: InsertFile' )
			sys.exit()
		else:
			shouldRun = True
			insertText = _.getText( _.switches.value('InsertFile'), True )
			insertText = insertText.replace( '\n', '' )

	if _.switches.isActive('Insert'):
		shouldRun = True
		insertText = _.ci(_.switches.value('Insert'))
		# insertText = _str.cleanBE( insertText, ' ' )



	if _.switches.isActive('ReplaceFile'):
		if not os.path.isfile( _.switches.value('ReplaceFile') ):
			_.pr( 'Error: ReplaceFile' )
			sys.exit()
		else:
			shouldRun = True
			replaceText = _.getText( _.switches.value('ReplaceFile'), True )
			replaceText = replaceText.replace( '\n', '' )

	if _.switches.isActive('Replace'):
		shouldRun = True
		replaceText = _.ci(_.switches.value('Replace'))
		# replaceText = _str.cleanBE( replaceText, ' ' )

	# if len(insertText) == 0:
	# 	confirm = input('Insert blank, run? ')
	# 	if not 'y' in confirm.lower():
	# 		sys.exit()

	if not shouldRun:
		_.pr( 'Error: Bad switch 1' )
		sys.exit()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool or _.switches.isActive('Input') and os.path.isfile( _.switches.value('Input') ):
	# 	if type( _.appData[__.appReg]['pipe'] ) == bool:
	# 		_.appData[__.appReg]['pipe'] = []
	# 		_.appData[__.appReg]['pipe'].append( _.switches.value('Input') )
		
	files = _.isData(2)
	for filename in files:
		filename.strip()
		if os.path.isfile( filename ):
			processFile(filename)
	# else:
	# 	_.pr( 'Error: No Files' )
	# 	sys.exit()


def getTabs( line ):
	pre = ''
	for ch in str(line):
		if ch == ' ' or ch == '\t':
			pre += ch
		else:
			return pre
	return pre

EntireQuotes = _.switches.isActive('EntireQuotes')
def processFile( filename ):
	global insertText
	global replaceText
	global EntireQuotes

	_.pr()
	_.pr('processing:', filename)
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre replaceText' )
	recoveryFile = fileBackup.do( 'action' )

	file = _.getText( filename )

	newFile = []
	rows = []
	for i,line in enumerate(file):
		line = line.replace( '\n', '' )
		if not EntireQuotes:
			newFile.append( line.replace( replaceText, insertText ) )
		elif EntireQuotes:
			if not replaceText in line:
				newFile.append( line )
			elif replaceText in line:
				q='"'
				parts=line.split(q)
				po=[]
				for ii,px in enumerate(parts):
					if replaceText in px: parts[ii]=insertText
				line=q.join(parts)
				newFile.append( line )


	_.saveText( newFile, filename )

	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'replaceText' )
	recoveryFile = fileBackup.do( 'action' )

	if _.switches.isActive('Input'):

		keep=input('Keep changes? ')
		if 'n' in keep.lower():
			try:
				copyfile(recoveryFile, filename)
				_.pr( 'Undo successful' )
			except Exception as e:
				_.pr( 'Undo fail' )



########################################################################################
if __name__ == '__main__':
	action()







