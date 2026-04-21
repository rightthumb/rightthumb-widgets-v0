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

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Reset', '-r,-reset')
	_.switches.register('ReturnFiles', '-files')
	



_.appInfo[focus()] = {
	'file': 'ticketTimeline.py',
	'description': 'Create a ticket epoch time range table',
	'categories': [
						'research',
						'tickets',
						'ticketing',
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

_.appInfo[focus()]['examples'].append('p ticketTimeline')
_.appInfo[focus()]['examples'].append('p ticketTimeline -reset')

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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

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

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
########################################################################################
# START

def records():

	returnFiles = _.switches.isActive( 'ReturnFiles' )

	tickets = []
	ids = []
	dirList = os.listdir(_v.myTickets)
	i = 0
	for item in dirList:
		path = _v.myTickets + _v.slash + item
		if os.path.isfile(path) and item.lower().endswith('.txt'):
			if item.lower().startswith('closed-') or item.lower().startswith('open-'):
				idx = item.lower().replace( 'closed-', '' ).replace( 'open-', '' ).replace( '.txt', '' )
				if len( idx ):
					if not idx in ids:
						ids.append(ids)
						txtFile = _.getText( path, clean=2 )
						data = ''
						for line in txtFile:
							line = line.replace( '\n', '' )
							if 'Session:' in line:
								data = line
								data = data.replace( ' ', '' )
								break
						start = data.split( '(' )[1].split( '-' )[0]
						end = data.split( '-' )[1].split( ')' )[0]

						s = _.resolveEpochTest(start)
						e = _.resolveEpochTest(end)
						# x = 0
						# if type(e) == bool:
						#     tickets.append({ 'id': idx, 'start': s, 'end': e, 'path': path })

						i+=1
						if returnFiles:
							tickets.append({ 'id': idx, 'start': s, 'end': e, 'path': path, 'file': txtFile })
						else:
							tickets.append({ 'id': idx, 'start': s, 'end': e, 'path': path })
	return tickets


def action():
	if _.switches.isActive('Reset'):
		log = []
	else:
		log = _.getTable( 'ticketTimeline.json' )


	ids = []
	if len( log ) > 0:
		for l in log:
			ids.append( l['id'] )

	dirList = os.listdir(_v.myTickets)
	# _.pr( _v.myTickets )
	# _.pr( dirList )
	i = 0
	for item in dirList:
		path = _v.myTickets + _v.slash + item
		if os.path.isfile(path) and item.lower().endswith('.txt'):
			if item.lower().startswith('closed-') or item.lower().startswith('open-'):
				idx = item.lower().replace( 'closed-', '' ).replace( 'open-', '' ).replace( '.txt', '' )
				if len( idx ):
					if not idx in ids:
						_.pr( path )
						txtFile = _.getText( path )
						data = ''
						for line in txtFile:
							line = line.replace( '\n', '' )
							if 'Session:' in line:
								data = line
								data = data.replace( ' ', '' )
								break
						_.pr()
						_.pr( data )
						try:
							start = data.split( '(' )[1].split( '-' )[0]
							end = data.split( '-' )[1].split( ')' )[0]
							_.pr( _.resolveEpochTest(start), _.resolveEpochTest(end) )
							log.append({ 'id': idx, 'start': _.autoDate(start), 'end': _.autoDate(end) })
							i+=1
						except Exception as e:
							_.pr(path.split(os.sep)[-1],c='red')



			# if i > 10:
			#     sys.exit()
	_.saveTable( log, 'ticketTimeline.json', printThis=False, lock=True )














def tickets_of_the_day():


	shouldPrint = False


	if _.switches.isActive('Reset'):
		log = []
	else:
		log = _.getTable( 'ticketTimeline_Day.json' )

	# log = []
	ids = []
	if len( log ) > 0:
		for l in log:
			ids.append( l['id'] )

	dirList = os.listdir(_v.myTickets)
	# _.pr( _v.myTickets )
	# _.pr( dirList )
	i = 0
	for item in dirList:
		path = _v.myTickets + _v.slash + item
		if os.path.isfile(path) and item.lower().endswith('.txt'):
			if item.lower().startswith('closed-') or item.lower().startswith('open-'):
				idx = item.lower().replace( 'closed-', '' ).replace( 'open-', '' ).replace( '.txt', '' )
				if len( idx ):
					if not idx in ids:
						if shouldPrint:
							_.pr( path )
						txtFile = _.getText( path )
						data = ''
						for line in txtFile:
							line = line.replace( '\n', '' )
							if 'Session:' in line:
								data = line
								data = data.replace( ' ', '' )
								break
						if shouldPrint:
							_.pr()
							_.pr( data )
						start = data.split( '(' )[1].split( '-' )[0]
						end = data.split( '-' )[1].split( ')' )[0]
						if shouldPrint:
							_.pr( _.resolveEpochTest(start), _.resolveEpochTest(end) )
						s = _.resolveEpochTest(start).split(' ')[0]
						e = _.resolveEpochTest(end).split(' ')[0] + ' 23:59:59'
						s = _.resolveEpochTest(  _.autoDate(s)  )
						e = _.resolveEpochTest(  _.autoDate(e)  )
						if shouldPrint:
							_.pr( s, e )
						# sys.exit()
						log.append({ 'id': idx, 'start': _.autoDate(s), 'end': _.autoDate(e) })
						i+=1



			# if i > 10:
			#     sys.exit()
	_.saveTable( log, 'ticketTimeline_Day.json', printThis=False, lock=True )













########################################################################################
if __name__ == '__main__':
	action()






