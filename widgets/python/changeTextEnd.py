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
# import _rightThumb._date as _date
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################
from shutil import copyfile
##################################################

def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Text', '-text')
	_.switches.register('Add', '-a,-add')
	_.switches.register('Remove', '-r,-remove')
	_.switches.register('Payload', '-payload',';. 0 (ns/be/d/i/f)')

	


_.appInfo[focus()] = {
	'file': 'changeTextEnd.py',
	'description': 'Add or remove text from the end of the line',
	'categories': [
						'json',
						'javascript',
						'programming',
						'text manipulation',
						'file manipulation',
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
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p changeTextEnd -i auditCodeBase.json + ";\'hasClose;\'" -text ";c" -add')
_.appInfo[focus()]['examples'].append('p changeTextEnd -i auditCodeBase.json + ";\'hasClose;\'" -text ";c" -remove')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p f -in *.js + ;. "function(" -jn | p line --c - jquery > %tmpf0%')
_.appInfo[focus()]['examples'].append('type %tmpf0% | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({\'action\';.\'change\',\'function\';.\'*_*\',\'timestamp\';.(new Date).getTime(),\'id\';.family.talk.thisTable});" -payload ;. 0 nsif -add ')
_.appInfo[focus()]['examples'].append('echo shared.js | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({\'action\';.\'change\',\'function\';.\'*_*\',\'timestamp\';.(new Date).getTime()});" -payload ;. 0 nsif -add')
_.appInfo[focus()]['examples'].append('')
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
fileBackup.switch( 'Flag', 'changeTextEnd' )
theText = ''
def action():
	global theText

	# _.pr( _.switches.value('Input') )

	if _.switches.isActive('Text'):
		
		theText = _.ci(_.switches.value('Text'))
		theText = _str.cleanBE( theText, ' ' )

	if len(_.switches.value('Plus'))<3:
		_.pr( 'Error: Plus' )
		sys.exit()

	if not type( _.appData[__.appReg]['pipe'] ) == bool or _.switches.isActive('Input') and os.path.isfile( _.switches.value('Input') ):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			_.appData[__.appReg]['pipe'].append( _.switches.value('Input') )
		
		files = _.appData[__.appReg]['pipe']
		for filename in files:
			if os.path.isfile( filename ):
				processFile(filename)



def getTabs( line ):
	pre = ''
	for ch in str(line):
		if ch == ' ' or ch == '\t':
			pre += ch
		else:
			return pre
	return pre

def processFile( filename ):
	global theText

	_.pr()
	_.pr('processing:', filename)
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre changeTextEnd' )
	recoveryFile = fileBackup.do( 'action' )

	file = _.getText( filename, raw=True )

	newFile = []
	rows = []
	

	if _.switches.isActive('Payload'):
		payload = _.switches.value('Payload').split( ',' )
		nospace = False
		be = False
		dup = False
		addi = False
		addf = False
		for ii,p in enumerate(payload):
			payload[ii] = _.ci( payload[ii] )
			if ii == 0:
				delim = payload[ii]
			elif ii == 1:
				row = int(payload[ii])
			elif ii == 2:
				if 'n' in payload[ii].lower() and 's' in payload[ii].lower():
					nospace = True
				if 'b' in payload[ii].lower() and 'e' in payload[ii].lower():
					be = True
				if 'd' in payload[ii].lower():
					dup = True
				if 'i' in payload[ii].lower():
					addi = True
				if 'f' in payload[ii].lower():
					addf = True
					f_info = _dir.fileInfo( filename )['name']

	newText = theText
	for i,line in enumerate(file.split('\n')):
		line = line.replace( '\n', '' )
		found = False
		if _.showLine(line):
			found = True

			if _.switches.isActive('Add'):
				if _.switches.isActive('Payload'):
					# _.pr()
					# _.pr(line)
					payloadData = line.split( delim )[ row ]
					# _.pr(payloadData)
					if dup:
						payloadData = _str.replaceDuplicate( payloadData, ' ' )
						payloadData = _str.replaceDuplicate( payloadData, '\t' )
					if be:
						payloadData = _str.cleanBE( payloadData, ' ' )
						payloadData = _str.cleanBE( payloadData, '\t' )
					if nospace:
						payloadData = payloadData.replace( ' ', '' )
						payloadData = payloadData.replace( '\t', '' )
					pass
					if addf:
						payloadData += '[' + str( f_info ) + ']'
					if addi:
						payloadData += '(' + str( i ) + ')'
					newText = theText.replace( '*_*', payloadData )
					payloadData = ''


				newFile.append( line + newText )


			# pass

					
			if _.switches.isActive('Remove'):
				line = _str.cleanEnd( line, ' ' )
				line = _str.cleanEnd( line, '\t' )
				line = _str.cleanEnd( line, theText )
				newFile.append( line )

		if not found:
			newFile.append( line )

	_.saveText( newFile, filename )

	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'changeTextEnd' )
	recoveryFile = fileBackup.do( 'action' )

	if _.switches.isActive('Input'):

		keep=input('Keep changes? ')
		if 'n' in keep.lower():
			try:
				copyfile(recoveryFile, filename)
				_.pr( 'Undo successful' )
			except Exception as e:
				_.pr( 'Undo fail' )

# type %tmpf0% | p changeTextEnd + ;. "function(" -text  ";n;t;tfamily.v.tracker.push({'action';.'change','function';.'*_*','timestamp';.(new Date).getTime(),'id';.family.talk.thisTable,'d';.family.talk.adherence.r_d(),'a';.family.talk.adherence.r_a()});" -payload ;. 0 nsif -add - setTimeout

########################################################################################
if __name__ == '__main__':
	action()







