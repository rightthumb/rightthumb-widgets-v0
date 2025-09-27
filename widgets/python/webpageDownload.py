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
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str



##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register( 'URL', '-url', isRequired=True )
	_.switches.register( 'Save', '-save', 'file.htm, file.json' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'webpageDownload.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Save url code',
	'categories': [
						'download',
						'url',
						'offline',
						'online',
						'code',
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
						'p webpageDownload -url http://rightthumb.com/ -save offline.txt',
						'',
						'p webpageDownload -url http://rightthumb.com/ ',
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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
	
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
########################################################################################
# START


from operator import itemgetter
from lxml import html
import requests
import cssselect
# import webbrowser

_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )



def action():

	_browser.imp.project.open( url )
	code = _.getText( _v.myAppsJs + _v.slash+'Church_Directory.js' )
	_browser.imp.project.jqueryInject()
	_browser.imp.project.inject( code )
	while not _browser.imp.project.injectReturn('return window.taskComplete;'): pass
	data =_browser.imp.project.injectReturn( 'window.hack.acquire.payload()' )
	_browser.imp.project.close()
	_.printVar( data )
	
	_.pr()
	_.saveTable( data, 'Church_Directory.json' )


def action2():
	pass
	# global data
	# load()


	page = requests.get( _.switches.values('URL')[0] )
	if _.switches.values('Save'):
		_.saveText( page.content , _.switches.values('Save')[0] )
		_.colorThis( 'Saved', 'green' )
	else:
		_.pr( page.content )
	# tree = html.fromstring(page.content)
	# tables = tree.cssselect('.r')
	# for t in tables:
	#     try:
	#         item = t.text_content()
	#     except Exception as e:
	#         item = ''
	#     if 'imdb' in item.lower():
	#         links = t.cssselect('a')
	#         link = str(links[0].attrib['href'])
	#         link = link.replace('/url?q=http:','http:')
	#         text = t.text_content()
	#         # _.pr(text)
	#         _.pr()
	#         _.pr(text)



# https://raw.githubusercontent.com/benjamincrom/scrabble/master/scrabble/dictionary.json
# def load():
#     global data
#     data = _.getTable( 'table' )


# data = []
########################################################################################
if __name__ == '__main__':
	action()






