#!/usr/bin/python3
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
	_.switches.register( 'Loops', '-loops' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'pass.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Generate password',
	'categories': [
						'password,tool',
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
						'p pass',
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
import math
import _rightThumb._nID as _nID
_nID.mini.safe = True
# _nID.mini.return_test = True
import _rightThumb._md5 as _md5



def action():
	# print(ord('\\'));sys.exit();
	# print(ord('/'));sys.exit();
	# print( _v.slashes['windows']['char'] );sys.exit();
	# print( _v.slashes['unix']['char'] );sys.exit();
	_.printVarSimple( _.stringType( '5Ab' ) )
	_.printVarSimple( _.stringType( '4fAb' ) )
	_.printVarSimple( _.stringType( '23465437476!Ab' ) )
	_.printVarSimple( _.stringType( '5Ab654asdf345FDSFG' ) )
	_.printVarSimple( _.stringType( '5Ab' ) )
	print( _.stringType( 123, mini=0 ) )
	print( _.stringType( 123.1, mini=0 ) )
	print( _.stringType( _md5, mini=0 ) )
	# print( _.stringType( saasdfadsf, mini=0 ) )
	sys.exit()

	if _.switches.isActive('Loops'):
		l = int( _.switches.values('Loops')[0] )
	else:
		l = 0
	n = int( input( 'n: ' ) )
	a = input( 'a: ' )
	b = input( 'b: ' )
	c = input( 'c: ' )

	p = str(n)+a+c+b

	_nID.mini.password( p )
	x = _nID.mini.gen( n )

	md5 = _md5.md5(x)

	i = 0
	while not i == l:
		md5 += _md5.md5(md5)
		i+=1

	print( md5 )
	print( 'md5:',len(md5) )
	print( 'n:',len(str(n)) )
	print( 'p:',len(p) )


	# y = _nID.mini.resolve( x[0] )



# 2303585560878385625050422819510267939516367434716039644230519160439390347999256009693752580598140272903504385643122809197417221457139238741549966340010235237572445


########################################################################################
if __name__ == '__main__':
	action()




         