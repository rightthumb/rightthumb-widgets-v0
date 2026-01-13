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
# import platform

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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str


##################################################
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	_.switches.register('Strait', '-0,-strait')
	_.switches.register('End', '-end')
	_.switches.register('Epoch', '-epoch')
	_.switches.register('Replace', '-replace')
	_.switches.register('Short', '-short')
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'resolveIDs.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Resolve IDs',
	'categories': [
						'resolve',
						'tool',
						'id',
						'ids',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						'p file --c | p resolveIDs',
						'',
						'p generateIdResolution  OR  a.idGen',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

















def resolveIDsNEW(line,clean=False):
	global idResolution
	theID = ''
	pre = line
	once = False
	records = []
	for idr in idResolution:
		if idr['id'] in line:
			records.append([ idr['id'],idr['name'] ])  
	return records


def resolveIDs(line,clean=False):
	global idResolution
	theID = ''
	pre = line
	once = False
	for idr in idResolution:
		if _.switches.isActive('Strait') == True:
			newName = idr['name']
		else:
			newName = ' { { ' + idr['name'] + ' } } '
		line = line.replace(idr['id'],newName)
		if not pre == line and not once:
			once = True
			theID = idr['name']
	if clean:
		line = theID

	return line

def getLabels(line):
	global idResolution
	result = ' >> '
	for idr in idResolution:
		if not len(line) == len(line.replace(idr['id'],'')):
			result += str(idr['name']) + ', '
	result = _str.cleanLast(result,', ')
	if result == ' >> ':
		result = ''
	return result




def resolveEpoch(line,clean=False):
	epoch = ''
	data = _str.totalStrip9(line)
	result = ''

	for word in data.split(' '):
		if word.count('.') > 1:
			wDots = word.split('.')
			wDots.reverse()
			wDots.pop(0)
			wDots.reverse()
			word = '.'.join( wDots )

		if True:
		# if len(word) > 12 and len(word) < 20:
			# result += str(len(word)) + ' '
			test = word.split('.')
			try:
				float(word)
				good = True
			except Exception as e:
				good = False
			if good:
				pass
				# result += str(len(test[0]))
			if good and len(test[0]) == 10 or len(test[0]) == 13 :

				this_is_a_test = False

				epochTest = _.resolveEpochTest( word, showPrint=this_is_a_test, showPrintTry=this_is_a_test, onlyEpoch=False )
				# [ result, epoch ]
				if this_is_a_test:
					_.pr( 'word:', word )
					_.pr( 'epochTest:', epochTest )
				if type( epochTest ) == list:
					result += epochTest[0]
					epoch = epochTest[1]


	if clean:
		result = epoch
	return result


def resolveEpochNEW(line,clean=False):
	epoch = ''
	data = _str.totalStrip9(line)
	result = ''
	record = []
	for word in data.split(' '):
		if word.count('.') > 1:
			wDots = word.split('.')
			wDots.reverse()
			wDots.pop(0)
			wDots.reverse()
			word = '.'.join( wDots )

		if True:
		# if len(word) > 12 and len(word) < 20:
			# result += str(len(word)) + ' '
			test = word.split('.')
			try:
				float(word)
				good = True
			except Exception as e:
				good = False
			if good:
				pass
				# result += str(len(test[0]))
			if good and len(test[0]) == 10 or len(test[0]) == 13 :

				this_is_a_test = False

				epochTest = _.resolveEpochTest( word, showPrint=this_is_a_test, showPrintTry=this_is_a_test, onlyEpoch=False )
				# [ result, epoch ]
				if this_is_a_test:
					_.pr( 'word:', word )
					_.pr( 'epochTest:', epochTest )
				if type( epochTest ) == list:
					record.append( [word,_.friendlyDate(float(word))] )
					result += epochTest[0]
					epoch = epochTest[1]


	if clean:
		result = epoch
	return record
	return result


def action():
	load()
	global pipeResults
	global idResolution
	data = []
	epochCount = 0
	idCount = 0

	# for line in pipeResults:
	for i,line in enumerate( _.isData(r=1) ):
		line = line.replace('\n','')
		
		if _.switches.isActive('End'):
			_.pr(line,getLabels(line),resolveEpoch(line))
		elif _.switches.isActive('Replace'):
		
			for rec in resolveEpochNEW(line):
				line = line.replace( str(rec[0]), _.colorThis( [ str(rec[1]) ], 'yellow', p=0 ) )
			for rec in resolveIDsNEW(line):
				new = _.colorThis( [ '( ' ], 'red', p=0 )
				new += _.colorThis( [ rec[0][0:3]+'..'+rec[0][-3:] ], 'blue', p=0 )
				new+= ' '
				new+= _.colorThis( [ str(rec[1]) ], 'green', p=0 )
				new+= _.colorThis( [ ' )' ], 'red', p=0 )
				
				line = line.replace( str(rec[0]), new )

			_.pr(line)
				# data.append({ 'id': str(rec[0]), 'epoch': str(rec[0]), 'line': line })
			# _.pr( 'resolveEpochNEW:', epochs )
			# _.pr(resolveEpoch(line),resolveIDs(line))
		else:
			epoch = resolveEpoch(line,True)
			theID = resolveIDs(line,True)
			if len(epoch) > 0:
				epochCount += 1
			if len(theID) > 0:
				idCount += 1
			data.append({ 'id': theID, 'epoch': epoch, 'line': line })

	_.tables.register('resolvedData',data)
	_.tables.fieldProfileSet('resolvedData','id','alignment','right')
	_.pr()


	if not _.switches.isActive('Short'):
		_.switches.fieldSet('Long','active',True)

	if idCount == 0 and epochCount == 0:
		_.pr()
		_.pr('Nothing to resolve')
	elif idCount > 0 and epochCount > 0:
		_.tables.print('resolvedData','epoch,id,line')
	elif idCount > 0 and epochCount == 0:
		_.tables.print('resolvedData','id,line')
	elif idCount == 0 and epochCount > 0:
		_.tables.print('resolvedData','epoch,line')
















def load():
	global idResolution
	idResolution = _.getTable('idResolution.json')



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()