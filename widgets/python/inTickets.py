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
import platform
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
import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	_.switches.register('App', '-a,-app','fileRecover')
	_.switches.register('Ticket', '-t,-Ticket','5017,5018')
	



_.appInfo[focus()] = {
	'file': 'inTickets.py',
	'description': 'Searches in tickets where the timestamp is withing the modification date of an app',
	'categories': [
						'history',
						'apps',
						'tool',
						'research',
						'development',
						'help',
						'enviroment',
						'command',
						'example',
						'app'
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
						'p inTickets -app imdb + imdb "-ep"',
						'',
						'p inTickets -app line + -ps',
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
# START

def searchInTicket( ticket ):
	results = []
	c = _v.myTickets + _v.slash+'closed-THEID.txt'
	o = _v.myTickets + _v.slash+'open-THEID.txt'

	cc = c.replace( 'THEID', str(ticket) )
	oo = o.replace( 'THEID', str(ticket) )
	chosen = False
	if os.path.isfile( cc ):
		chosen = cc
	elif os.path.isfile( oo ):
		chosen = oo

	if not type( chosen ) == bool:
		try:
			file = _.getText( chosen, clean=3 )

			for row in file:
				if _.showLine( row ):
					results.append( row )
					# _.pr( row )
		except Exception as e:
			_.pr( 'Error:', chosen )



	return results
def processTickets():
	results = []
	if _.switches.isActive('Ticket'):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			for row in _.switches.value('Ticket').split( ',' ):
				_.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			data = searchInTicket( row )
			for d in data:
				results.append( d )
	return results


def getTicket( epoch ):
	global epochTickets
	result = ''
	for ticket in epochTickets:
		# _.pr( epoch, ticket['start'], ticket['end'] )
		# sys.exit()
		try:
			if float(epoch) > float(ticket['start']) and float(epoch) < float(ticket['end']):
				result += ticket['id'] + ','
		except Exception as e:
			pass
	result = _str.cleanBE( result, ',' )
	return result

def findTickets():
	global backupLog
	app = _.switches.value('App')
	search = _v.slash+   app.lower()   +'.py'
	for record in backupLog:
		if search in record['file'].lower():
		# if record['file'].lower().endswith(  _.genAppName( app ).lower()+'.py' ):
			ticketData = getTicket( record['timestamp'] )
			if not ticketData == '':
				for t in ticketData.split( ',' ):
					if type( _.appData[__.appReg]['pipe'] ) == bool:
						_.appData[__.appReg]['pipe'] = []
					_.appData[__.appReg]['pipe'].append( t )
			
			


def action():
	load()

	if _.switches.isActive('Plus') and ( _.switches.isActive('Ticket') or not type( _.appData[__.appReg]['pipe'] ) == bool ):
		processTickets()
	else:
		if _.switches.isActive('App'):
			findTickets()
			if not type( _.appData[__.appReg]['pipe'] ) == bool:
				data = processTickets()
				if not len( data ):
					_.pr( 'No Results' )
				else:
					nData = []
					for row in set(data):
						nData.append({ 'row': row })
						
					# _.pr( type( nData ) )
					for row in _.tables.returnSorted( 'row', 'd.row', nData ):
						_.pr( row['row'] )
			else:
				_.pr( 'No tickets found' )



# App
# Ticket
# Plus

# 

def load():
	global backupLog
	global epochTickets

	backupLog = _.tables.returnSorted( 'fileBackup_log', 'd.timestamp', _.getTable('fileBackup.json') )

	ticketTimeline = _.regImp( __.appReg, 'ticketTimeline' )
	ticketTimeline.do( ticketTimeline.imp.tickets_of_the_day )
	epochTickets = _.tables.returnSorted( 'ticketTimeline', 'd.start', _.getTable('ticketTimeline.json') )
	if platform.system() == 'Windows':
		do = 'cls'
	else:
		do = 'clear'
	os.system( '"' + do + '"' )
	_.pr()

backupLog = []
epochTickets = []
########################################################################################
if __name__ == '__main__':
	action()