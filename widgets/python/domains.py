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
	_.switches.register( 'Build', '-build' )
	_.switches.register( 'JustReturn', '-return' )
	_.switches.register( 'Color', '-color' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'domains.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Identify internet top-level website domains and return or colorize',
	'categories': [
						'domain',
						'tool',
						'List of Internet top-level domains',
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
						' type %tiktok% | p domains',
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
					{ 'resource': 'https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains' },
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START





def process(row):
	global index
	global color
	
	# _.updateLine( 'Processing...' )
	for domain in _.internet_domains(row):
		row = row.replace( domain, _.colorThis( domain, color, p=0 ) )

	# _.updateLine( '                     ' )
	# _.updateLine( '' )
	if not _.switches.isActive('JustReturn'):
		_.pr( row )
	return row





def action():
	pass
	global tables
	global index
	global color


	results = ''
	if _.switches.isActive('Color'):
		color = _.switches.value('Color')


	if _.switches.isActive('Build'):
		tables = _.getTableDB( 'domains.json' )
		index = {}
		i = 0
		for table in tables:
			if 'Name' in table[0] and table[0]['Name'].startswith('.'):
				# _.printVar( table[0] )
				for record in table:
					i+=1
					if record['Name'].startswith('.'):
						index[ record['Name'] ] = record

		_.saveTableDB( index, 'domains.index' )
		_.colorThis( [ 'Saved', _.addComma(i), ': domains.index' ], 'green' )
		sys.exit()



	index = _.getTableDB( 'domains.index' )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:

		file = ''.join( _.appData[__.appReg]['pipe'] )

		# process(file)

		for i,row in enumerate( file.split('\n') ):
			results += process(row) 
			

	return results
	


index = {}
tables = []
color = 'yellow'


########################################################################################
if __name__ == '__main__':
	action()