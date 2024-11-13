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
	_.switches.register( 'Shorter', '-t,-short,-mini,-small' )
	_.switches.register( 'Tiny', '-tiny' )
	_.switches.register( 'Strip', '-cl,-clean,-st,-strip', 'be' )
	_.switches.register( 'Count', '-cnt,-count' )
	_.switches.register( 'PrintCharLength', '-print,-printlen,-lenprint,-len' )
	_.switches.register( 'LowerCase', '-lo,-lower' )
	_.switches.register( 'MixedCase', '-m,-mix,-mixed,-case' )
	_.switches.register( 'NoPrint', '--c' )
	_.switches.register( 'Pre-Date', '-e,-epoch' )
	_.switches.register( 'Find-Date', '-uuid,-guid' )
	_.switches.register( 'Multiple', '-n,-nth,-multi' )



	
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

def process(vVv):
	return _.UUID_Epoch(vVv)


def action(first=True):

	if _.switches.isActive('Find-Date'):
		_.pr('poo')
		for uuid in _.switches.values('Find-Date'):
			uuid = _str.do('an',uuid)
			if len(uuid) > 30:
				if 'epoc' in uuid:
					d=int(uuid.split('epoc')[1][:10])
					_.cp( _.isDate( d, f='fdate') , 'cyan' )
			elif len(uuid) < 15 and len(uuid) > 10:
				if 'e' in uuid:
					d=int(uuid.split('e')[1][:10])
					_.cp( _.isDate( d, f='fdate') , 'cyan' )



		return None

	if first and _.switches.isActive('Count'):
		ids=[]
		i=0
		while i < int(_.switches.value('Count')):
			i+=1
			ids.append(action(first=False))
		return ids

	focus()

	if not _.switches.isActive('Long') and not _.switches.isActive('Shorter'):
		genid = _.genUUID()
	if _.switches.isActive('Tiny'):
		genid = _.tinyUUID()
	if _.switches.isActive('Shorter'):
		genid = _.miniUUID()
	elif _.switches.isActive('Long'):
		if  len( _.switches.value('Long') ):
			genid = _.longID( int( _.switches.value('Long') ) )
		else:
			genid = _.longID()
	if _.switches.isActive('Pre-Date'):
		genid=process(genid)
	if _.switches.isActive('Strip'):
		if 'be' in _.switches.value('Strip'):
			genid = genid.replace( '{', '' ).replace( '}', '' )
		else:
			genid = genid.replace( '{', '' ).replace( '}', '' ).replace( '-', '' )


	if not _.switches.isActive('LowerCase') and not _.switches.isActive('MixedCase'):
		if not _.switches.isActive('NoPrint'):
			_.pr( genid )
	elif _.switches.isActive('LowerCase'):
		if not _.switches.isActive('NoPrint'):
			_.pr( genid.lower() )
	elif _.switches.isActive('MixedCase'):
		import randomTool
		if not _.switches.isActive('NoPrint'):
			_.pr( randomTool.case(genid) )


	if _.switches.isActive('PrintCharLength'):
		_.pr()
		_.colorThis( [  '', _.addComma(len(genid)), 'characters'  ], 'yellow' )
  
	return genid

from random import randrange



########################################################################################
if __name__ == '__main__':
	if _.switches.isActive('Multiple'):
		if _.switches.value('Multiple'):
			n=int(_.switches.value('Multiple'))
		else:
			n=10
		i=0
		while not i==n:
			i+=1
			action()
	else:
		action()







