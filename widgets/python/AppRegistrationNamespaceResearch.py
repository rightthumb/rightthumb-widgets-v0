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
##################################################

def appSwitches():
	pass
	_.switches.register( 'App', '-app' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']



_.appInfo[focus()] = {
	'file': 'AppRegistrationNamespaceResearch.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Research how global namespace is used',
	'categories': [

						'research',
						'tool',
						'namespace',
						'python',
						'programming',
						'import',
						'example',
						'examples',
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
						'p AppRegistrationNamespaceResearch -app base3 + switches|p line --c -mps ;p switches. = ( ;; ;+ -cb -nb |sort|p countEach',
						'p AppRegistrationNamespaceResearch -app base3 + tables|p line --c -mps ;p tables. = ( ;; ;+ -cb -nb |sort|p countEach',
						'',
						['p AppRegistrationNamespaceResearch -app os |p line --c -mps ;p os. = ( ;; ;+ -cb -nb |sort|p countEach','red'],
						'',
						'',
						['p AppRegistrationNamespaceResearch -app base3 + switches | p line -ps = switches. --c | p line -cb -nb --c -ps ( switches.  | p line -ps _ switches. --c |  sort | p countEach','red'],
						'',
						'a.appInfoImport base3 switches',
						'a.appInfoImport base3 tables',
						'a.appInfoImport os path',
						'',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					'AppRegistrationImportExamples',
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
	global data
	load()


	for record in data:
		for imp in record['file_profile']['imports']:
			raw = _str.stripNonAlphaNumaric(  imp['raw'].lower()  ).split(' ')
			if _.switches.values('App')[0].lower() in raw or '_'+_.switches.values('App')[0].lower() in raw:
				# _.pr( imp['raw'] )
				for ex in imp['examples']:
					if _.showLine( ex ):
						_.pr( ex )



def load():
	global data
	data = _.getTableDB( 'appRegistration.json' )


data = []



########################################################################################
if __name__ == '__main__':
	action()







