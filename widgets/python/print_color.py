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
	_.switches.register( 'Line', '-line' )
	_.switches.register( 'Text', '-text' )
	_.switches.register( 'Color', '-color' )
	_.switches.register( 'Tabs', '-tab,-tabs', '1' )
	_.switches.register( 'Fi', '-f,-file,-files', '~/pr.tmp' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'print_color.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Print text',
	'categories': [
						'print',
						'color',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'p colors',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p print_color -text this is a test -color red',
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
	_.switches.trigger( 'Text', _.ci )
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

	pre=''
	if _.switches.isActive('Tabs'):
		tabs=int(_.switches.value('Tabs'))
		i=0
		while not i==tabs:
			i+=1
			pre+='    '


	if _.switches.isActive('Fi'):
		for path in _.switches.values('Fi'):
			if os.path.isfile(path):
				for line in _.getText( path, raw=True ).split('\n'):
					# _.pr( 55, line, c='yellow' )
					if not type(line) == str: return None
					if not len(line): _.pr()
					test = _str.do('trim',line)
					if not test:
						_.pr()
					else:
						line = line.replace( '\t', '    ' )
						line=_str.do('be',line,' ')
						words = line.split(' ')
						color = words[0]
						words.pop(0)
						txt = ' '.join(words)
						if 'linePrint'.lower() in txt.lower():
							_.linePrint(c=color)
						else:
							_.pr( pre+txt, c=color )
					# _.pr( 66, line, c='yellow' )


		return None






	if _.switches.isActive('Line') and _.switches.isActive('Color'):
		_.linePrint(c=_.switches.values('Color')[0])
	elif _.switches.isActive('Line') and not _.switches.isActive('Color'):
		_.linePrint()
	else:
		_.colorThis( pre+' '.join(_.switches.values('Text')), _.switches.values('Color')[0] )


########################################################################################
if __name__ == '__main__':
	action()






