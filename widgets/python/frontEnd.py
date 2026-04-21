#!/usr/bin/python3

##################################################
'''
epyi toolsScrapeFrontEnd

 def URL
 class ProxyManager
	def __init__
	def start_server
	def start_client
	def client
	def server
 class FrontEnd(object)
	def __init__
	def is_cookie_expired
	def extractDomain
	def preURL
	def postURL
	def url
	def getCookies
	def initialize
	def select
	def setField
	def login
	def loginIndividually
	def open
	def jqueryInject
	def inject
	def injectReturn
	def injectFile
	def close
	def wait
	def code
'''
##################################################

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
# import _rightThumb._toolsScrapeFrontEnd as _browser
# from _rightThumb._toolsScrapeFrontEnd import jquery


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
	'file': 'thisApp.py',
	'description': 'Changes the world',
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

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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

_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd2' )
import _rightThumb._encryptString as _blowfish


def action():
	project = _browser.imp.FrontEnd()
	# project.initialize()
	project.url('https://www.google.com/search?q=computer')
	for i,result in enumerate(project.select('h3')):
		text = result.text.strip()
		if text: print(i,text)
	project.close()
	
	

	

	# string = 'scott'
	# en = _blowfish.encrypt( string )
	# _.pr( en )
	# de = _blowfish.decrypt( en )
	# _.pr( de )

	# sys.exit()
	
	# who = 'mom'
	# if who == 'dad':
	#     username = 's.rephsr@gmail.com'
	#     password = 'OntNu4Y13rXWB8UMWROHHw=='
	# elif who == 'mom':
	#     username = 'aireph51@gmail.com'
	#     password = 'TWaNVzohgkGth877srTXjw=='
	# else:
	#     username = 'scott.reph@gmail.com'
	#     password = 'YYHeOQgMCOk9e6ETwJzd+Q=='

	# _browser.imp.project.loginIndividually( 'https://play.google.com/apps', username, password, '#identifierId', '[type=password]', login_button='span.RveJvd' )


	# # _browser.imp.project.open( 'http://www.pillerbeauty.com/blank.htm' )
	# code = _.getText( _v.myAppsJs + _v.slash+'test2.js' )
	# # _browser.imp.project.inject( code )
	# _browser.imp.project.jqueryInject()
	# _browser.imp.project.inject( code )
	# # _browser.imp.project.inject( 'window.scrollEnd();' )
	# # pause = input( 'pause' )
	# data = _browser.imp.project.injectReturn( 'window.acquirePayload()' )
	# for row in data:
		# _.pr( row['name'] )
	
	




########################################################################################
if __name__ == '__main__':
	action()


# https://help.crossbrowsertesting.com/selenium-testing/getting-started/python/