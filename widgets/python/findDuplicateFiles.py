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

# import os
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
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Flag', '-flag')
	_.switches.register('ShowFlagged', '-printflag')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'findDuplicateFiles.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT'
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
						'p findDuplicateFiles -i %mData%',
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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def findLastFolder( data ):
	x = data.split(_v.slash)
	x.reverse()
	x.pop(0)
	return x[0]


def flag( xID, data ):

	if not _.switches.isActive( 'Flag' ) and not _.switches.isActive( 'ShowFlagged' ):

		return data

	global flagData
	global flagged
	folder = findLastFolder( data )
	if not ' ' in folder:

		try:
			flagData[xID] += 1
			isFirst = False
		except Exception as e:
			flagData[xID] = 0
			isFirst = True

		if isFirst:
			# return str(xID) + ' DELETE\t' + data
			if not data in flagged:
				flagged.append( data )
			return 'DELETE\t' + data
	return data


def action():
	global data
	global flagged
	spent = []
	load()
	if not _.switches.isActive( 'ShowFlagged' ):
		_.pr( 'Files:', len(data) )
	records = {}
	for i,file in enumerate(data):
		try:
			theID = str(file['bytes'])+'_'+str(file['date_modified_raw'])
		except Exception as e:
			shouldRun = False
		else:
			shouldRun = True
		
		if shouldRun:
			if not file in spent:
				spent.append( file )
				try:
					records[theID].append( i )
				except Exception as e:
					records[theID]=[]
					records[theID].append( i )
	dup = 0
	size = 0
	spent = []
	for theID in records.keys():
		if len(records[theID]) > 1:
			dup+=1
			if not _.switches.isActive( 'ShowFlagged' ):
				_.pr()
			for i,xID in enumerate(records[theID]):
				if not i == 0:
					size+=data[xID]['bytes']
				thisRecord = flag( theID, data[xID]['path'] )
				if not _.switches.isActive( 'ShowFlagged' ):
					if not thisRecord in spent:
						spent.append( thisRecord )
						_.pr( thisRecord )
	if _.switches.isActive( 'ShowFlagged' ):
		# _.pr('HERE')
		# _.pr( flagged )
		for row in flagged:
			_.pr( row )
	if not _.switches.isActive( 'ShowFlagged' ):
		_.pr()
		_.pr('Duplicates:',dup)
		_.pr( 'Space:',_.formatSize(size) )

# findDuplicateFiles


def load():
	global data
	data = _.getTable2( _.switches.value( 'Input' ) )
	# _.pr( len(data), type(data), type(data[0]) )
	# sys.exit()
data = []
flagData = {}
flagged = []
########################################################################################
if __name__ == '__main__':
	action()