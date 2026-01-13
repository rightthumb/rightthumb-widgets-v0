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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )

##################################################

from shutil import copyfile
# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Function', '-function')
	_.switches.register('ReplaceFile', '-replacefile')

	



_.appInfo[focus()] = {
	'file': 'replaceFunction.py',
	'description': 'Replaces an entire function with a replacement',
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
_.appInfo[focus()]['examples'].append('p replaceFunction -i insertText.py -replacefile %tmpf0% -function focus')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.py + "def focus" -jn | p replaceFunction -replacefile %tmpf0% -function focus')
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

########################################################################################
########################################################################################
# START

fileBackup = _.regImp( __.appReg, 'fileBackup' )
# fileBackup.switch( 'Silent' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )

functionName = ''
replaceText = ''
def action():
	global functionName
	global replaceText

	# _.pr( _.switches.value('Input') )
	shouldRun = False

	if _.switches.isActive('Function'):
		shouldRun = True
		functionName = _.ci(_.switches.value('Function'))
		functionName = _str.cleanBE( functionName, ' ' )



	if _.switches.isActive('ReplaceFile'):
		if not os.path.isfile( _.switches.value('ReplaceFile') ):
			_.pr( 'Error: ReplaceFile' )
			sys.exit()
		else:
			shouldRun = True
			replaceText = _.getText( _.switches.value('ReplaceFile'), True )



	if len(functionName) == 0:
		confirm = input('Insert blank, run? ')
		if not 'y' in confirm.lower():
			sys.exit()

	if not shouldRun:
		_.pr( 'Error: Bad switch 1' )
		sys.exit()

	if not type( _.appData[__.appReg]['pipe'] ) == bool or _.switches.isActive('Input') and os.path.isfile( _.switches.value('Input') ):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			_.appData[__.appReg]['pipe'].append( _.switches.value('Input') )
		
		files = _.appData[__.appReg]['pipe']
		for filename in files:
			if os.path.isfile( filename ):
				processFile(filename)
	else:
		_.pr( 'Error: No Files' )
		sys.exit()


def getTabs( line ):
	pre = ''
	for ch in str(line):
		if ch == ' ' or ch == '\t':
			pre += ch
		else:
			return pre
	return pre

def processFile( filename ):
	global functionName
	global replaceText
	replaceText = replaceText.replace( ';n', _v.slash+'n' )
	_.pr()
	_.pr('processing:', filename)
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre replaceFunction' )
	recoveryFile = fileBackup.do( 'action' )

	file = _.getText( filename )

	newFile = []
	rows = []
	found = False
	done = False
	ri = 0
	noSpace = []
	blank = []
	comment_blank = []
	omit = []
	hasText = []

	for i,line in enumerate(file):
		line = line.replace( '\n', '' )
		blnk = line.replace( '\t', '' ).replace( ' ', '' )
		if blnk == '':
			comment_blank.append( i )
		else:
			if blnk.startswith( '#' ):
				comment_blank.append( i )
			elif not line[0] == ' ' and not line[0] == '\t':
				noSpace.append( i )

			if not blnk.startswith( '#' ):
				hasText.append( i )



	for i,line in enumerate(file):
		line = line.replace( '\n', '' )

		
		if line.startswith( 'def ' + functionName + '(' ):

			# for newline in replaceText:
			#     newFile.append( newline.replace( '\n', '' ) )
			
			newFile.append( replaceText )



			x = i
			xx = i

			loop = True            
			while loop:
				xx+=1
				if xx in noSpace:
					xx-=1
					loop = False

			loop = True            
			while loop:
				if xx in hasText:
					# _.pr( 'h', file[xx] )
					loop = False
					# xx+=1
				# elif xx in comment_blank:
					# _.pr( 'c', file[xx] )
					# loop = False
				else:
					xx-=1
			y = i
			while not y > xx:
				omit.append( y )
				y+=1



		if not i in omit:
			newFile.append( line )





	_.saveText( newFile, filename )

	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'replaceFunction' )
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