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

import os, sys, time
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



def appSwitches():
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'URL-Include', '-has' )
	_.switches.register( 'URL-Exclude', '-not' )
	_.switches.register( 'Dates', '-dates' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'crawler3.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'payload finder',
	'categories': [
						'payload',
						'crawler',
						'web',
						'tool',
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
						_.hp('p crawler3 -url https://www.mt-vernon.k12.oh.us/MV_Athletics.aspx -has mt vernon -not maps download email + 740'),
						_.hp('p crawler3 -url https://www.mt-vernon.k12.oh.us/MV_Athletics.aspx -has mt vernon -not maps download email -dates'),
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

if _.switches.isActive('Dates'):
	import datefinder

def dicURL(url,page):
	par = urlparse(url)
	return par.scheme + '://'+par.netloc+page
	
def findString(content):
	good = _str.alphanumeric+'-.()'
	if _.switches.isActive('Plus'):
		good += ''.join(_.switches.values('Plus'))
	data = str(content,'iso-8859-1')
	if _.switches.isActive('Dates'):
		for match in datefinder.find_dates(data):
			d = match.strftime('%Y-%m-%d %H:%M:%S')
			if _.showLine(d):
				_.cp( d ,'green')
	else:
		stripped = ''
		for d in data:
			if d in good:
				stripped += d
			else:
				stripped += ' '
		while ') ' in stripped:
			stripped = stripped.replace( ') ', ')' )
		stripped = stripped.replace( '(', ' (' )
		for seg in stripped.split(' '):
			if _.showLine(seg):
				_.cp(seg,'green')

spent = []
def process(url):
	run = True
	for has in _.switches.values('URL-Include'):
		if not has.lower() in url.lower():
			run = False
	for has in _.switches.values('URL-Exclude'):
		if has.lower() in url.lower():
			run = False
	if not run:
		return None

	global spent
	if url in spent:
		return None
	else:
		spent.append(url)
	_.cp(url,'cyan')
	page = requests.get(url)
	tree = html.fromstring(page.content)
	findString(page.content)
	for lin in tree.cssselect('a'):
		try:
			link = str(lin.attrib['href'])
			if link.startswith('http'):
				process(link)

			if link.startswith('/'):
				path = dicURL(url,link)
				process(path)
				# _.pr(path)

		except Exception as e:
			pass



def action():

	for url in _.switches.values('URL'):
		process(url)

from urllib.parse import urlparse

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







