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
import _rightThumb._encryptString as _blowfish
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
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'fullPathToPyProject.py',
	'description': 'Removes python path and adds epy or epyi, etc',
	'categories': [
						'dirty',
						'quick',
						'tool',
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

_.appInfo[focus()]['examples'].append('p dir3 --c -r -ago 1w cd -c p + *.py | p fullPathToPyProject')
_.appInfo[focus()]['examples'].append('p dir3 --c -r -ago 1w md -c p + *.py | p fullPathToPyProject')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p dir3 --c -r -ago 2d md -c p + *.py | p fullPathToPyProject')
_.appInfo[focus()]['examples'].append('p dir3 --c -r -ago 2d cd -c p + *.py | p fullPathToPyProject')
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

def cleaner( data ):
	epyi = _v.myAppsPy + _v.slash+'_rightThumb\_'
	epy = _v.myAppsPy + _v.slash
	data = data.replace( epyi, 'epyi ' )
	data = data.replace( epy, 'epy ' )
	data = data.replace( '__init__.py', '' )
	data = data.replace( '.py', '' )
	if not data.endswith( _v.slash ):
		data = data.replace( _v.slash, ' -file ' )
	else:
		data = data.replace( _v.slash, '' )
	data = _str.replaceDuplicate( data, ' ' )
	data = _str.cleanBE( data, ' ' )
	if data.endswith( '-file' ):
		data = data.replace( ' -file', '' )
	data = data.replace( 'epyi base3', 'epyi base' )
	data = data.replace( '-file _base3_init_example', '-e' )
	return data


def action():
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		epyi = []
		epy = []
		for row in _.appData[__.appReg]['pipe']:
			data = cleaner( row )
			if data.startswith( 'epyi ' ):
				epyi.append( data )
			else:
				epy.append( data )

		for row in epy:
			_.pr( row )
		_.pr(len(epy))
		_.pr()
		for row in epyi:
			_.pr( row )
		_.pr(len(epyi))
		_.pr()
		_.pr(len(epyi)+len(epy))






########################################################################################
if __name__ == '__main__':
	action()






