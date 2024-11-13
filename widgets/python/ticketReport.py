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
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
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
	# _.switches.register('Input', '-i,-input','file.txt')
	# _.switches.register('Files', '-f,-file','file.txt')
	_.switches.register('WasOpen', '-wasclosed')
	_.switches.register('Open', '-open')
	_.switches.register('Closed', '-closed')

	

_.autoBackupData = False


_.appInfo[focus()] = {
	'file': 'ticketReport.py',
	'description': 'Report on closed tickets',
	'categories': [
						'ticket',
						'tickets',
						'report',
						'history',
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
						'p ticketReport -open',
						'p ticketReport -closed',
						'p ticketReport -wasclosed',
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

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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

_.postLoad( __file__ )

########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def refineOpen():
	global data
	results = []
	for ticket in data:
		if ticket.startswith( 'open-' ) and ticket.endswith( '.txt' ):
			ticketFile = _.getText( _v.myTickets + _v.slash + ticket )
			for row in ticketFile:
				if row.startswith( 'Session: ' ):
					row = row.replace( '\n', '' )
					row = _str.replaceDuplicate( row, ' ' )
					row = _str.cleanBE( row, ' ' )
					shouldSave = True
					if row.endswith( 'isAdmin:False' ):
						shouldSave = False
					if row.endswith( 'isAdmin:True' ):
						shouldSave = False
					if row.endswith( 'isAdmin:' ):
						shouldSave = False
					if row.endswith( ')' ):
						shouldSave = False
					if ') test' in row:
						shouldSave = False
					if shouldSave:
						results.append({ 'ticket': ticket, 'session': row })
					break
	return results


def closedSession():
	global data
	results = []
	for ticket in data:
		if ticket.startswith( 'closed-' ) and ticket.endswith( '.txt' ):
			ticketFile = _.getText( _v.myTickets + _v.slash + ticket )
			for row in ticketFile:
				if row.startswith( 'Session: ' ):
					results.append({ 'ticket': ticket, 'session': row.replace( '\n', '' ) })
					break
	return results

def wasClosedSession():
	global data
	results = []
	for ticket in data:
		if ticket.startswith( 'closed-' ) and ticket.endswith( '.txt' ):
			ticketFile = _.getText( _v.myTickets + _v.slash + ticket )
			for row in ticketFile:
				if row.startswith( 'Session: ' ):
					row = row.replace( '\n', '' )
					row = _str.replaceDuplicate( row, ' ' )
					row = _str.cleanBE( row, ' ' )
					shouldSave = True
					if row.endswith( 'isAdmin:False' ):
						shouldSave = False
					if row.endswith( 'isAdmin:True' ):
						shouldSave = False
					if row.endswith( 'isAdmin:' ):
						shouldSave = False
					if row.endswith( ')' ):
						shouldSave = False
					if ') test' in row:
						shouldSave = False
					if shouldSave:
						results.append({ 'ticket': ticket, 'session': row })
					break
	return results
	

def refineClosed():
	global data
	refinedTickets = []
	for ticket in data:
		if ticket.startswith( 'closed-' ) and ticket.endswith( '.txt' ):
			refinedTickets.append( ticket )

def action():
	load()

	if _.switches.isActive( 'Open' ):
		data = refineOpen()
		for record in data:
			_.pr( record['session'] )
	elif _.switches.isActive( 'WasOpen' ):
		data = wasClosedSession()
		for record in data:
			_.pr( record['session'] )
	elif _.switches.isActive( 'Closed' ):
		data = closedSession()
		for record in data:
			_.pr( record['session'] )



def load():
	global data
	data = os.listdir( _v.myTickets )
data = []
########################################################################################
if __name__ == '__main__':
	action()






