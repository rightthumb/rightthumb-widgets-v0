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
##################################################
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

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='name', description='Files' )
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'Preview', '-p,-prev,-preview' )
	_.switches.register( 'DumpFields', '-dump,-field,-fields,-fi' )
	_.switches.register( 'Language', '-l,-lan,-language' )
	_.switches.register( 'Show-Depth', '-depth' )

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'tinydic.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'tiny json tool',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'json',
						'profile',
						'dict',
						'dic',
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
						_.hp('p tinydic -f www.iheartjane.com.har + 74.6 -prev -dump url'),
						_.hp('p tinydic -url https://materialdesignicons.com/api/package/38EF63D0-4744-11E4-B3CF-842B2B6CFE1B'),
						_.hp(''),
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


def language_trigger(data):
	if 'py' in data:
		return 'py'
	if 'javascript' in data:
		return 'js'
	return data

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

	_.switches.trigger( 'Language', language_trigger )

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

import simplejson


def action():

	if _.switches.isActive('URL'):
		import requests
		url = _.switches.values('URL')[0]
		data = data=simplejson.loads(str(requests.get(url).content,'iso-8859-1'))
	elif _.isData():
		try:
			data=simplejson.loads( '\n'.join(_.isData()) )
		except Exception as e:
			data=simplejson.loads( _.getText(_.switches.values('Files')[0],raw=True) )
	else:
		import requests
		url='https://dutchie.com/graphql?operationName=FilteredProducts&variables=%7B%22includeTerpenes%22%3Atrue%2C%22includeEnterpriseSpecials%22%3Atrue%2C%22productsFilter%22%3A%7B%22cName%22%3A%22maui-wowie-cartridge%22%2C%22dispensaryId%22%3A%226074c54c93af6d00d1a80ecc%22%2C%22removeProductsBelowOptionThresholds%22%3Atrue%2C%22isKioskMenu%22%3Afalse%2C%22bypassKioskThresholds%22%3Afalse%2C%22bypassOnlineThresholds%22%3Atrue%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%222dbddbf08502941c361a322a70087d6dfe085437f6cb99c32dd1852a513bf579%22%7D%7D'
		data=simplejson.loads(str(requests.get(url).content,'iso-8859-1'))

	if _.switches.isActive('Preview'):
		prev=True
	else:
		prev=False

	if _.switches.isActive('Plus'):
		skim=True
	else:
		skim=None

	if _.switches.isActive('DumpFields'):
		dump=_.switches.values('DumpFields')
	else:
		dump=None

	if _.switches.isActive('Language'):
		lan=_.switches.value('Language')
	else:
		lan='js'


	if _.switches.isActive('Show-Depth'):
		list0 = False
	else:
		list0 = True

	_.linePrint(c='yellow')
	# for x in _.tinydic(data,skim=None,lan='py',prev=False,dump=None,list0=True)
	for x in _.tinydic(data,skim=skim,lan=lan,prev=prev,dump=dump,list0=list0):
		_.pr(x)
	_.linePrint(c='yellow')


def load():
	global data
	if _.switches.isActive('Files'):
		data = _.getTable2( _.switches.values('Files')[0] )





########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





