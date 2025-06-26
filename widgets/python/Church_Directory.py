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
import _rightThumb._encryptString as _blowfish
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )



##################################################

# from lxml import html
import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	


_.appInfo[focus()] = {
	'file': 'yahooGroupSyFyTranscripts.py',
	'description': 'Acquire transcripts for SyFy stuff',
	'categories': [
						'online',
						'syfy',
						'yahoo',
						'yahoo group',
						'acquire',
						'transcripts',
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
						'p yahooGroupSyFyTranscripts',
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
# os.system('"' + do + '"')
########################################################################################
# START

# from subprocess import call
# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys


def action():
	global data
	# load()

	# _.pr( _v.chromedriver )
	# sys.exit()

	url                = 'https://covenantlifetampa.org/church-directory/'
	password           = 'harmony'
	selector           = '#pwbox-3255'

	# _.pr( password )

	_browser.imp.project.open( url )
	_browser.imp.project.setField( password, selector, enter=True )



	code = _.getText( _v.myAppsJs + _v.slash+'Church_Directory.js' )
	_browser.imp.project.jqueryInject()
	_browser.imp.project.inject( code )
	# _.copyVar( 'copy( window.hack.acquire.payload() );' )

	data =_browser.imp.project.injectReturn( 'window.hack.acquire.payload()' )
	_.printVar( data )
	
	_.pr()
	_.saveTable( data, 'Church_Directory.json' )
# 

	# pause = input( 'pause' )
	_browser.imp.project.close()



# def load():
#     global data
#     data = _.getTable( 'table.json' )
data = []
########################################################################################
if __name__ == '__main__':
	action()


# p dir3 -ago 1d -c n --c | p cleanEnd | p line --c -make "del ;'{};'" | p execute
# window.hack.acquire.done = true;
# p dir3 -ago 1d -c n
# p dirdb + *.py selenium chrome techApps Python36






