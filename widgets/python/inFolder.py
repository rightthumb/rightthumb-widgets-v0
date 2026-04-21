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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._encryptString as _blowfish
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
##################################################

def appSwitches():
	pass
	_.switches.register('Recursion', '-r,-recursion,-recursive','5')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'inFolder.py',
	'description': 'Finds files in the same folder as other files',
	'categories': [
						'research'
						'files',
						'folders',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						'p dirdb + *.pdf  > %tmpf5%',
	],
	'examples': [
						'type %tmpf5% | p inFolder + *.txt',
						'type %tmpf5% | p inFolder + *.txt -r 5 | p f + armandpowers -jn ',
						''
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# START

def processFolder( folder ):
	global data
	global depth
	global defaultMaxDepth
	# _.pr( folder )
	for file in os.listdir( folder ):
		path = folder + _v.slash + file
		if _.switches.isActive( 'Recursion' ):
			if os.path.isdir( path ):
				r = _.switches.value( 'Recursion' )

				if len( r ):
					defaultMaxDepth = int( r )
				else:
					defaultMaxDepth = 5
				depth += 1
				if not depth > defaultMaxDepth:
					try:
						processFolder( path )
					except Exception as e:
						pass

		if _.showLine( file ):
			data.append( path )



def action():
	global data
	global depth
	pass
	# load()
	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	if _.switches.isActive('Input'):
	#     _.setPipeData( _.getText( _.switches.value('Input') ), focus() )
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			for row in _.switches.value('Input').split( ',' ):
				_.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		folders = []
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if os.path.isfile( row ):
				row = os.path.abspath( row )
				folder = _.popDelim( row, _v.slash )
				if not folder in folders:
					if os.path.isdir( folder ):
						folders.append( folder )
						# _.pr( folder )
		for i,folder in enumerate(folders):
			# _.pr( i, folder )
			depth = 0
			processFolder( folder )

		for i,row in enumerate( data ):
			# _.pr( i, row )
			_.pr( row )

data = []
depth = 0
defaultMaxDepth = 10
# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()