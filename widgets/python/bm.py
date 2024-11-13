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
	# _.switches.register( 'Index', '-index' )
	_.switches.register('BuildFolders', '-build')
	_.switches.register('Export', '-export')


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'bm.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Bookmark tool',
	'categories': [
						'bm',
						'bookmark',
						'bookmarks',
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
						'p bm -index ',
						'',
						'',
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
	_.switches.trigger( 'Files',_.myFileLocations )
	
	
	
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
# __.appRegPipe
########################################################################################
# START



# index['labels']
# index['paths']


def action():

	global index
	folder = os.getcwd()
	import _rightThumb._bookmarks as _bm
	focus()
	bm = _bm.Bookmarks(path=folder)
	index = bm.index
	script = ''
	if _.switches.isActive('BuildFolders'):
		for alias in index['labels']:
			if _.showLine(alias):
				# _.pr(alias)
				# _.pr(  _.showLine(alias),  alias)
				path = _v.resolveFolderIDs( index['labels'][alias] )
				_.cp( [ '\n', 'cd', path, '\n', 'm', alias, '\n' ], 'cyan' )
				script += '\n' +' '+ 'cd' +' '+ path +' '+ '\n' +' '+ 'm' +' '+ alias +' '+ '\n'
				# script += '\n' +' '+ 'cd' +' '+ path +' '+ '\n' +' '+ 'm' +' '+ alias.replace( '.live', '.l' ) +' '+ '\n'

	if _.switches.isActive('Export'):
		for alias in index['labels']:
			if _.showLine(alias):
				raw = index['labels'][alias]
				path = _v.resolveFolderIDs( raw )
				script += alias+'|'+raw+'\n'
				_.pr(script)

		pass
		script
		_copy = _.regImp( __.appReg, '-copy' )
		_copy.imp.copy( script, p=0 )
		return None


	# load()
	# _.printVarSimple( index )

	# labels paths

	
	bm = _bm.Bookmarks(path=folder)
	index = bm.index
	# bm.path = os.getcwd()

	sanitized = bm.sanitize()

	# _.pr( folder )
	# _.pr( sanitized )

	try:
		try:
			for record in index['paths'][folder]:
				_.colorThis( [ record ], 'yellow' )
		except Exception as e:
			for record in index['paths'][sanitized]:
				_.colorThis( [ record ], 'yellow' )

	except Exception as e:
		_.colorThis( [ 'Error: no bookmarks' ], 'red' )

	_.pr( _v.sanitizeFolder(folder) )


# def load():
#     global index
#     if _.switches.isActive('Index'):
#         _bm = _.regImp( __.appReg, 'bookmarks' )
#         index = _bm.imp.index()
#     else:
#         index = _.getTable( 'bookmarks_index.json' )

index = []
########################################################################################
if __name__ == '__main__':
	action()



import glob
import os.path
import sys
from os.path import join, getsize, isfile, isdir, splitext
# import _rightThumb._vars as _v







