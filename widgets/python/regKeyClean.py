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
# import _rightThumb._encryptString as _blowfish
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
	pass
	_.switches.register('Batch', '-batch')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'regKeyClean.py',
	'description': 'Takes piped reg query and extracts key data',
	'categories': [
						'research',
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

_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path | p regKeyClean')
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
########################################################################################
# START


def action():
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		if _.switches.isActive('Batch'):
			_.pr( '@echo off' )
		for row in _.appData[__.appReg]['pipe']:
			if 'REG_EXPAND_SZ' in row or 'REG_SZ' in row:
				if 'REG_EXPAND_SZ' in row:
					data = row.split( 'REG_EXPAND_SZ' )
				if 'REG_SZ' in row:
					data = row.split( 'REG_SZ' )
				if len( data ) > 1:
					for i,d in enumerate( data ):
						data[i] = data[i].replace( '\t', '' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
						data[i] = _str.cleanBE( data[i], ' ' )
					if _.switches.isActive('Batch'):
						_.pr( 'SET '+ data[0]+'='+data[1] )
					else:
						if _.showLine( data[0]+' '+data[1] ):
							_.pr( data[0]+' = '+data[1] )






########################################################################################
if __name__ == '__main__':
	action()






