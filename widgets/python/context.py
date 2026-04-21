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
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################
import time
import datetime
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'context.py',
	'description': 'Searches through command line history',
	'categories': [
						'history',
						'research',
						'auto',
						'help',
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

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('context json2DB')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p context + 7z -u | p line + " 7z " ";_u "')
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
# START

def expireCheck(theDate):
	timestamps = theDate.split(' - ')
	try:
		now = datetime.datetime.now()
		today = now.strftime("%Y-%m-%d")
		fdtl = theDate.split('.')
		# foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
		foundDate = datetime.datetime.utcfromtimestamp( _.autoDate( timestamps[0] ) )
		td = str(today).split('-')
		# tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
		tdd = datetime.datetime.utcfromtimestamp( time.time() )
		diff = tdd - foundDate
		return int(diff.days)
	except Exception as e:
		try:
			now = datetime.datetime.now()
			today = now.strftime("%Y-%m-%d")
			fdtl = theDate.split('.')
			# foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			foundDate = datetime.datetime.utcfromtimestamp( _.autoDate( timestamps[1] ) )
			td = str(today).split('-')
			# tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
			tdd = datetime.datetime.utcfromtimestamp( time.time() )
			diff = tdd - foundDate
			return int(diff.days)
		except Exception as e:
			return 'Unknown'

def action():

	fileList = _.getText(_v.contextTemp)
	result = []
	for fl in fileList:
		fl = fl.replace('\n','')
		# _.pr(fl)
		file = _.getText(_v.myHome + _v.slash+'tickets'+_v.slash + fl)
		show = False
		for f in file:
			f = f.replace('\n','')
			if 'Session:' in f:                
				result.append(f)
			if '</pre>' in f:
				show = False
			if show:
				result.append(f)
			if '<pre>' in f:
				show = True

	
	for data in (result):
		if 'Session:' in data:
			_.pr('\n\n\n')
			one = data.split('(')[1]
			theDate = one.split(')')[0]

			d = expireCheck(theDate)

		_.pr(data)
		if 'Session:' in data:
			_.pr('Days ago:',d)
			_.pr('\n')
			
	_.pr()
	_.pr()
	_.pr('Records:',len(fileList))



########################################################################################
if __name__ == '__main__':
	action()