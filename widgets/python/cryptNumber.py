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
	_.switches.register( 'Number', '-n' )
	_.switches.register( 'Resolve', '-r' )
	_.switches.register( 'Password', '-password' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'numberID.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Number compression and encryption',
	'categories': [
						'nid',
						'number',
						'compression',
						'encryption',
						'crypt',
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
						'p numberID -n 1620652634',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


from tkinter import * 

import math
import _rightThumb._nID as _nID
_nID.mini.safe = True

def ask( label=None ):
	global xyz
	xyz = None
	def show():
		global xyz
		xyz = password.get()
		_.colorThis( [ '\t\t code:', label ], 'green' )

	app = Tk()   
	password = StringVar() #Password variable
	passEntry = Entry(app, textvariable=password, show='*').pack()
	submit = Button(app, text='Show Console',command=show).pack()
	app.mainloop() 
	return xyz

def action():
	n = 436942671737277407348192807075945686997744513
	# _.pr( 436942671737277407348192807075945686997744513 )
	# n = input(' n: ')
	# n = int( ask('n') )

	if _.switches.isActive('Password'):
		p = _.switches.value('Password')
		_nID.mini.password( p )
	if _.switches.isActive('Number'):
		n = _.switches.value('Number')

	if not _.switches.isActive('Number') and not _.switches.isActive('Resolve'):
		x = _nID.mini.gen( n )
		_.pr( x )
		y = _nID.mini.resolve( x )
		_.pr( y )
		# _.printVarSimple( _nID.mini.table )
	if _.switches.isActive('Number'):
		for n in _.switches.values('Number'):
			_.pr()
			x = _nID.mini.gen( n )
			_.pr( x )
			y = _nID.mini.resolve( x )
			_.pr( y )
			_.pr()
	elif _.switches.isActive('Resolve'):
		x = _.switches.value('Resolve')
		y = _nID.mini.resolve( x )
		_.pr( y )



########################################################################################
if __name__ == '__main__':
	action()