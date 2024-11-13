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
	_.switches.register( 'CMD', '-cmd' )
	_.switches.register( 'Python', '-py,-python' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'history_indices.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search history indices',
	'categories': [
						'history',
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
						'p history_indices -cmd youtube-dl + youtube',
						'',
						'p history_indices -cmd aggregate -py + aggregate',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START



def action():
	load()
	global data
	global subject_index

	closed = 'closed-0000.txt'
	opened = 'open-0000.txt'


	try:    
		x = data[ _.switches.values('CMD')[0].lower() ]
	except Exception as e:
		_.pr()
		_.colorThis( [  'Error: app does not exist in this index '  ], 'red' )
		_.pr()
		_.colorThis( [  '\t index: ', subject_index  ], 'yellow' )
		sys.exit()

	_.pr( x )
	_.pr(  )
	_.pr( _v.myTickets )

	spent=[]

	for y in x:
		good=True
		path = _v.myTickets+_v.slash+closed.replace('0000',y)
		if not os.path.isfile(  path  ):
			path = _v.myTickets+_v.slash+opened.replace('0000',y)
			if not os.path.isfile(  path  ):
				good=False
		if good:
			file = _.getText( path, raw=True, clean=1 )
			for row in file.split('\n'):
				if _.showLine( row ):
					if not row in spent:
						spent.append(row)
						_.pr( row )


def load():
	"""
	index_py_switches    = _.getTableDB( 'history_index[py-switches].index' )
	index_edit_py        = _.getTableDB( 'history_index[edit-py].index' )
	index_cmd            = _.getTableDB( 'history_index[cmd].index' )
	index_py             = _.getTableDB( 'history_index[py].index' )

	index_edit_files     = _.getTableDB( 'history_index[edit-files].index' )
	index_tickets        = _.getTableDB( 'history_index[tickets].index' )
	index_rename         = _.getTableDB( 'history_index[rename].index' )

	index_day            = _.getTableDB( 'history_index[day].index' )
	index_tickets_day    = _.getTableDB( 'history_index[tickets-day].index' )
	index_day_edit       = _.getTableDB( 'history_index[day-edit].index' )

	index_labs           = _.getTableDB( 'history_index[labs].index' )
	

	history_index[cmd].index

	history_index[py-switches].index
	history_index[edit-py].index
	history_index[py].index
	history_index[edit-files].index
	history_index[tickets].index
	history_index[rename].index
	history_index[day].index
	history_index[tickets-day].index
	history_index[day-edit].index
	history_index[labs].index
	"""

	indices = {
					'cmd': 'history_index[cmd].index',
					'py': 'history_index[edit-py].index',
	}


	global data
	global subject_index

	if _.switches.isActive('Python'):
		subject_index = indices['py']
	elif _.switches.isActive('CMD'):
		subject_index = indices['cmd']
	if not subject_index is None:
		data = _.getTable( subject_index )
	# _.pr(data)
	if data is None:
		_.colorThis( 'Error: index not selected', 'red' )
		sys.exit()

subject_index = None
data = None

########################################################################################
if __name__ == '__main__':
	action()







