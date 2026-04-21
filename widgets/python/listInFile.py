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
	# _blowfish.genPassword('string')
# import _rightThumb._md5 as _md5


	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
##################################################

def appSwitches():
	pass
	_.switches.register( 'EndsWith', '-endswith' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isRequired=True, description='Files' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'listInFile.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Check a file for a list of things',
	'categories': [
						'research',
						'tool',
						'xref',
						'crossref',
						'search',
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
						'type %tmpf0% | p listInFile -f index.txt',
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

	_.myFileLocation_Print = False
	# _.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START



def process( line ):
	for i,record in enumerate(_.appData[__.appReg]['pipe']):
		if _.switches.isActive('EndsWith'):
			if line.lower().endswith( record.lower() ):
				# _.pr(   _.caseUnspecific( line, record.lower() )   )
				for x in _.caseUnspecific( line, record.lower() ):
					line = line.replace( x, _.colorThis( x, 'cyan', p=0 ) )
				return line
		else:
			if record.lower() in line.lower():
				# _.pr(   _.caseUnspecific( line, record.lower() )   )
				for x in _.caseUnspecific( line, record.lower() ):
					line = line.replace( x, _.colorThis( x, 'cyan', p=0 ) )
				return line
	return None

		


def action():
	load()

	# test()

	for line in data:
		test = process( line )
		if not test is None:
			_.pr( test )



def test():
	global data
	for record in data:
		_.pr( record )

	sys.exit()


def load():
	global data
	data = _.getText( _.switches.values('Files')[0], raw=1, clean=2 ).split('\n')
	_.pipeCleaner()

data = []

########################################################################################
if __name__ == '__main__':
	action()