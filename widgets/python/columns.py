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


def appSwitches():
	_.switches.register( 'Number_of_Columns', '-n', '4' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'columns.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'pipe list to columns',
	'categories': [
						'tool',
						'columns',
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
						'p ls -ago 1y -c n --c | p f3 + session +dup -jn | p columns -n 4',
						'',
						'p ls -ago 1m -c n --c | p columns -n 6',
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



def action():

	col = 4
	if _.switches.isActive('Number_of_Columns'):
		col = int( _.switches.values('Number_of_Columns')[0] )

	table = []
	for i,row in enumerate(_.isData(r=1)):
		table.append(row)

	l = len(table)
	gs = int(str( len(table)/col ).split('.')[0])+1

	groups = {}
	g=1
	i=0
	for x in table:
		i+=1
		if i >= gs:
			if i == gs and g ==1:
				pass
			else:
				i=0
				g+=1
		if not str(g) in groups:
			groups[ str(g) ] = []

		groups[ str(g) ].append(x)

	i=0
	done=False
	records = []
	sizes = {}
	while not done:
		record = {}
		fnd = False
		for key in list(groups.keys()):
			record[ key ] = ''
			if key in sizes:
				record[ key ] = blanks(sizes[key])
			if len( groups[key] ) -1 >= i:
				fnd=True
				record[ key ] = groups[key][i]
				if not key in sizes:
					sizes[key] = 0
				if len(record[ key ]) > sizes[key]:
					sizes[key] = len(record[ key ])
		if not fnd:
			done=True
		else:
			records.append(record)
		i+=1
		# _.pr( record )


	_.tables.register( 'data', records )
	_.tables.print( 'data', ','.join(list(groups.keys())) )

	# _.pr( l, gs )

	# _.printVarSimple( groups )
	# _.printVarSimple( table )


def blanks(cnt):
	result = ''
	i=0
	while i == cnt:
		result += ' '
		i+=1
	return result



########################################################################################
if __name__ == '__main__':
	action()