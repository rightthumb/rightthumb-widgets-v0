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
	_.switches.register( 'Long', '-long' )
	_.switches.register( 'Short', '-short,-mini,-small' )
	_.switches.register( 'Strip', '-strip' )
	_.switches.register( 'Count', '-cnt,-count' )
	_.switches.register( 'PrintCharLength', '-print,-printlen,-lenprint,-len' )
	_.switches.register( 'LowerCase', '-lo,-lower' )
	_.switches.register( 'MixedCase', '-m,-mix,-mixed' )
	_.switches.register( 'NoPrint', '--c' )



	
_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'genuuid.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Generates uuid/guid',
	'categories': [
						'guid',
						'uuid',
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
						'p genuuid -long 5 -printlen',
						'',
						'p genuuid -short -printlen',
						'p genuuid -short -len',
						'',
						'9.16 MB',
						'\tp genuuid -strip -long 300000 > temp.txt',
						'',
						'937.5 KB',
						'\tp genuuid -strip -long 30000 > temp.txt',
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

def action(first=True):

	if first and _.switches.isActive('Count'):
		ids=[]
		i=0
		while i < int(_.switches.value('Count')):
			i+=1
			ids.append(action(first=False))
		return ids

	focus()
	if not _.switches.isActive('Long') and not _.switches.isActive('Short'):
		genid = _.genUUID()
	elif _.switches.isActive('Short'):
		genid = _.miniUUID()
	elif _.switches.isActive('Long'):
		if  len( _.switches.value('Long') ):
			genid = _.longID( int( _.switches.value('Long') ) )
		else:
			genid = _.longID()

	if _.switches.isActive('Strip'):
		genid = genid.replace( '{', '' ).replace( '}', '' ).replace( '-', '' )


	
	if not _.switches.isActive('LowerCase') and not _.switches.isActive('MixedCase'):
		if not _.switches.isActive('NoPrint'):
			print( genid )
	elif _.switches.isActive('LowerCase'):
		if not _.switches.isActive('NoPrint'):
			print( genid.lower() )
	elif _.switches.isActive('MixedCase'):
		import randomTool
		if not _.switches.isActive('NoPrint'):
			print( randomTool.case(genid) )


	if _.switches.isActive('PrintCharLength'):
		print()
		_.colorThis( [  '', _.addComma(len(genid)), 'characters'  ], 'yellow' )
  
	return genid



########################################################################################
if __name__ == '__main__':
	action()






