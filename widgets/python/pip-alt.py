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
# import platform
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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str

##################################################
from operator import itemgetter
from lxml import html
import requests
import cssselect
import datetime
##################################################


def appSwitches():
	_.switches.register( 'Module', '-m,-i,-mod,-imp,-module,-import' )
	_.switches.register( 'Print', '-print' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'pip-alt.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Alternative to pip',
	'categories': [
						'pip',
						'tool',
						'online',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						'p pip-alt -m simplejson',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START

def process( module ):
	url = 'https://pypi.org/simple/'+module+'/'
	_.pr(url)
	page = requests.get(url)
	tree = html.fromstring(page.content)
	links = tree.cssselect('a')
	text = False
	link = False
	for item in links:
		if not _.switches.isActive('Print'):
			if item.text_content().endswith('.tar.gz'):
				link = str(item.attrib['href'])
				text = item.text_content()
		elif _.switches.isActive('Print'):
			link = str(item.attrib['href'])
			text = item.text_content()
			_.pr()
			_.pr(text)
			_.pr(link)

	_.linePrint()
	if not _.switches.isActive('Print'):
		if text:
			_.pr()
			_.pr( text )
			# _.pr( link  )
			_copy.imp.copy( 'wget '+link+' -O '+text, p=1 )
		else:
			_.pr()
			_.cp( [ 'Error, missing src only .whl:', module ], 'red' )


def action():

	for module in _.switches.values('Module'):
		

		# process( url )
		try:
			process( module )
		except Exception as e:
			_.pr()
			_.cp( [ 'Error, url:', module ], 'red' )

_copy = _.regImp( __.appReg, '-copy' )




########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()