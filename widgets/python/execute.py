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
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime
##################################################
# from lxml import html
# import requests
# import cssselect
##################################################

def appSwitches():
	_.switches.register('Threaded', '-t,-thread,-threaded')
	_.switches.register('Stats', '-stats,-stat')
	_.switches.register('NoCount', '--c')
	_.switches.register('Command', '-cmd,-command','if not set, will use pipe data')

_.appInfo[focus()] = {
	'file': 'execute.py',
	'description': 'Execute pipe data',
	'categories': [
						'execute',
						'pipe',
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

_.appInfo[focus()]['examples'].append('type %tmpf1% | p execute')

_.appInfo[focus()]['examples'].append('')

_.appInfo[focus()]['examples'].append('type %tmpf1% | p execute -t --c -stats')

_.appInfo[focus()]['examples'].append('')
# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})

def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()

		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
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

def notThreaded():
	code = '\n'.join(_.appData[__.appReg]['pipe'])
	if '********************************************************' in code or '**' in code:
		print(code)
		sys.exit()
	for pip in _.appData[__.appReg]['pipe']:
		if not  _.switches.isActive('NoCount'):
			_.pr(pip)
		
		try:
			os.system(pip)
		except Exception as e:
			_.pr('Error')

def threaded():
	_.threads.add( 'execute', trigger=complete, loaded=False )
	_.threads.autoLoadedAfter = .5
	_.threads.scheduleLoop = .01
	_.threads.auditLoop = .1
	# _.threads.timeout = 1
	# _.threads.maxThreads = 100
	# _.threads.maxThreadsSafe = 250
	# _.threads.minThreads = 50
	if _.switches.isActive('Stats'):
		_.threads.report = True
		_.threads.auditPrint = True
	else:
		_.threads.report = False
		_.threads.auditPrint = False
	for pip in _.appData[__.appReg]['pipe']:
		_.threads.add( 'execute', executePipeRow, [ pip ] )

def executePipeRow( pip, qID=False ):
	if not  _.switches.isActive('NoCount'):
		_.pr(pip)
	try:
		os.system(pip)
	except Exception as e:
		_.pr('Error')
	if not type(qID) == bool:
		_.threads.spent( qID, sys.getsizeof( 'obj') )

def action():
	if _.switches.isActive('Command'):
		_.appData[__.appReg]['pipe'] = [ ' '.join( _.switches.values('Command') ) ]
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		if _.switches.isActive('Threaded'):
			threaded()
		else:
			notThreaded()

def complete():
	_.pr()
	_.pr()
	_.pr( 'done' )

########################################################################################
if __name__ == '__main__':
	action()
