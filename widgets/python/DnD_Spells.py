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
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str



_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
##################################################

def appSwitches(): pass



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'DnD_Spells.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Acquire spells database for DnD',
	'categories': [
						'DnD',
						'spells',
						'front end',
						'scrape',
						'scraping',
						'acquire',
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
						'p DnD_Spells',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
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
# START



def action():
	
	data = []
	code = _.getText( _v.myAppsJs + _v.slash+'dnd_spells.js', raw=True )


	# url = 'http://tools.rightthumb.com/test/cookies.php'
	url = 'https://www.dndbeyond.com/spells'
	# url = 'https://www.dndbeyond.com/spells?filter-class=2&filter-search=&page=1'
	"""
	cookies = [
					{
						"domain": "tools.rightthumb.com",
						"expiry": 1590411992.924958,
						"httpOnly": False,
						"name": "_tccl_visit",
						"path": "/",
						"secure": False,
						"value": "2330f1cc-8079-48e1-a11c-01ff36506400"
					},
					{
						"domain": "tools.rightthumb.com",
						"expiry": 1621946192.924415,
						"httpOnly": False,
						"name": "_tccl_visitor",
						"path": "/",
						"secure": False,
						"value": "2330f1cc-8079-48e1-a11c-01ff36506400"
					},
					{
						"domain": "tools.rightthumb.com",
						"expiry": 1593002192.707124,
						"httpOnly": False,
						"name": "user",
						"path": "/",
						"secure": False,
						"value": "John+Doe"
					}
				]
	"""

	"""
	cookies = [{
						'name': 'user',
					'value': 'John+Doe',
					'domain': 'tools.rightthumb.com',
					'expires': '',
						'path': '/',
					'httpOnly': False,
					'HostOnly': False,
					'Secure': False,
	},]
	"""
	"""
	cookies = [{
						'name': 'user',
					'value': 'John+Doe',
						'path': '/test/',
	},]
	"""
	# cookies = [
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1598187152,
	#                     "httpOnly": False,
	#                     "name": "_fbp",
	#                     "path": "/",
	#                     "sameSite": "Lax",
	#                     "secure": False,
	#                     "value": "fb.1.1590411148582.1721840930"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1605963151,
	#                     "httpOnly": False,
	#                     "name": "optimizelyEndUserId",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "oeu1590411148395r0.8017107595131803"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1598187151,
	#                     "httpOnly": False,
	#                     "name": "rdt_uuid",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "bd361569-5373-4a44-8efc-ecf9a781103b"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1590497551,
	#                     "httpOnly": False,
	#                     "name": "_uetsid",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "6b470c93-9b79-1c73-d4b8-8e9f1c3bd1f2"
	#                 },
	#                 {
	#                     "domain": ".www.dndbeyond.com",
	#                     "expiry": 1624510351,
	#                     "httpOnly": False,
	#                     "name": "sib_cuid",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "1807c6cf-83fa-4ede-8399-d3ed45155095"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "httpOnly": False,
	#                     "name": "Preferences",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "undefined"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1590412351,
	#                     "httpOnly": False,
	#                     "name": "_sg_b_p",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "%2Fspells%2C%2Fspells"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "httpOnly": False,
	#                     "name": "sublevel",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "ANON"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1590497552,
	#                     "httpOnly": False,
	#                     "name": "_gid",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "GA1.2.378889079.1590411147"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1637067148,
	#                     "httpOnly": False,
	#                     "name": "_pxvid",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "944a6051-9e86-11ea-893d-9f47300e23fd"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1598187147,
	#                     "httpOnly": False,
	#                     "name": "_gcl_au",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "1.1.974007695.1590411147"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1621947147,
	#                     "httpOnly": False,
	#                     "name": "_attrb",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "%2267ec1029-81d0-4952-9608-a0066f08f90f%22"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1621947151,
	#                     "httpOnly": False,
	#                     "name": "_attrg",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "null"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1621947151,
	#                     "httpOnly": False,
	#                     "name": "_attru",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "null"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "httpOnly": False,
	#                     "name": "Geo",
	#                     "path": "/",
	#                     "sameSite": "None",
	#                     "secure": True,
	#                     "value": "{%22region%22:%22FL%22%2C%22country%22:%22US%22%2C%22continent%22:%22NA%22}"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1598187149,
	#                     "httpOnly": False,
	#                     "name": "_sg_b_v",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "1%3B1%3B1590411148"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1653483152,
	#                     "httpOnly": False,
	#                     "name": "_ga",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "GA1.2.1411587341.1590411147"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1621947151.184939,
	#                     "httpOnly": False,
	#                     "name": "_pxhd",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "151d36a2bde79a49326e09b1ca2627d32e79cff20896162cde606dc3ecd65f55:944a6051-9e86-11ea-893d-9f47300e23fd"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1590414746.086748,
	#                     "httpOnly": False,
	#                     "name": "AWSELBCORS",
	#                     "path": "/",
	#                     "sameSite": "None",
	#                     "secure": True,
	#                     "value": "17A593B6CA59C3C4856B812F84CD401A582EF083467276F6C69E1D56867D29F5D7C31B8EB284A9F525C1AA0DF220CB30AEE9DCF6792D00A9777539B2936FD3FBDEB9EAF5"
	#                 },
	#                 {
	#                     "domain": ".dndbeyond.com",
	#                     "expiry": 1590411207,
	#                     "httpOnly": False,
	#                     "name": "_gat_UA-26524418-48",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "1"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1621515147,
	#                     "httpOnly": False,
	#                     "name": "ResponsiveSwitch.DesktopMode",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "1"
	#                 },
	#                 {
	#                     "domain": "www.dndbeyond.com",
	#                     "expiry": 1590414746.086622,
	#                     "httpOnly": False,
	#                     "name": "AWSELB",
	#                     "path": "/",
	#                     "secure": False,
	#                     "value": "17A593B6CA59C3C4856B812F84CD401A582EF083467276F6C69E1D56867D29F5D7C31B8EB284A9F525C1AA0DF220CB30AEE9DCF6792D00A9777539B2936FD3FBDEB9EAF5"
	#                 }
	# ]
	_browser.imp.project.cookies = 'recent'
	lastCookies = _.getTable( 'DnD_Spells_Cookies.json' )
	_browser.imp.project.setCookies(cookies)
	_browser.imp.project.open( url )
	_browser.imp.project.wait()

	# agent = _browser.imp.project.injectReturn( 'navigator.userAgent;' )
	# _.pr( agent )
	pause=input('pause: ')
	# data = _browser.imp.project.getCookies()
	# _.printVarSimple( data )


	# _browser.imp.project.close()
	# sys.exit()


	nextCheck = 99
	while not nextCheck == 0:
		_browser.imp.project.wait()
		_browser.imp.project.inject( code )
		payload = _browser.imp.project.injectReturn( 'window.hackData_DnD_Payload_Complete;' )
		# _.pr( test )
		while payload is None:
			payload = _browser.imp.project.injectReturn( 'window.hackData_DnD_Payload_Complete;' )
		
		for record in payload:
			data.append( record )
		_.pr()
		_.pr()
		_.pr('data:', len(data))
		_.pr()
		_.pr()
		time.sleep(.5)
		nextCheck = _browser.imp.project.injectReturn( 'window.hackData_DnD_Payload_Complete;' )
		_browser.imp.project.inject( 'window.hackData_DnD_Payload_Acquired = false;' )
		time.sleep(.5)


	
	_browser.imp.project.close()
	_.printVarSimple( data )
	# global data
	# load()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner(0)
	#     # _.printVar( _.appData )
	#     for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
	#         pass



# def load():
#     global data
#     data = _.getTable( 'table' )


# data = []



########################################################################################
if __name__ == '__main__':
	action()