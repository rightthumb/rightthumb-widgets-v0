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
##################################################
import os, sys, time
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
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Encrypt', '-en' )
	_.switches.register( 'Decrypt', '-de' )
	_.switches.register( 'App', '-app' )
	_.switches.register( 'Client', '-client' )
	_.switches.register( 'Date', '-d,-date' )
	_.switches.register( 'Epoch', '-e,-epoch' )
	_.switches.register( 'List', '-list' )
	_.switches.register( 'Subject-New-ID', '-id,-sub,-subject' )

	pass
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'nID.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Compress and encrypt numbers, and reverse',
	'categories': [
						'nid',
						'compress',
						'encrypt.crypt',
						'decompress',
						'decrypt',
						'number',
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
						_.hp('p nID -app a'),
						_.hp('p nID -en 123456789 '),
						_.hp('p nID -en 1000 -list'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
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

_key = _.regImp( __.appReg, 'vps-text-key' )
from random import randrange
def action(new=None):
	if new or _.switches.isActive('Subject-New-ID'):
		if new:
			subject=new
		else:
			subject=_.switches.values('Subject-New-ID')[0]
		table=_.getTable('nID-Subject-ID.hash')
		keys=_key.imp.shapeKee()
		key=randrange(len(keys))
		# _.pr()
		if not subject in table:
			# _.pr(key)
			table[subject] = {
								'subject': subject,
								'number': 999,
								'key': key,
			}
		
		key=table[subject]['key']
		table[subject]['number']+=1
		# _.pr(keys[ key ])
		_nID.mini.password(   keys[ key ]   )
		n=_nID.mini.gen( table[subject]['number'] )
		_.saveTable( table, 'nID-Subject-ID.hash', p=0 )
		_.pr(n)
		return n

		return None
	load()
	if _.switches.isActive('Client'):
		epoch=_.friendlyDate(time.time()).split(' ')[0].replace('-','')
		if len(_.switches.value('Client')):
			epoch=_.switches.value('Client').replace('-','')
		xx=[]
		for y in _key.imp.shapeKee():
			# _.pr(type(y),y)
			_nID.mini.password( y )
			x = _nID.mini.gen( int(epoch) )
			xx.append(x)
			_.pr(x)
		return xx
	if _.switches.isActive('App'):
		if len(_.switches.value('App')):
			epoch=time.time()
			xx=[]
			for y in _key.imp.shapeKee():
				# _.pr(type(y),y)
				_nID.mini.password( y )
				x = _nID.mini.gen( int(epoch) )
				xx.append(x)
				_.pr(x)
			return xx


		x = _nID.mini.gen( int( time.time() ) )
		_.pr(x)
		return x



	if _.switches.isActive('Epoch'):
		x = _nID.mini.gen( int( time.time() ) )
		_.pr(x)
		return x
	if _.switches.isActive('Date'):
		x = _nID.mini.gen( int( _.isDate( ' '.join(_.switches.values('Date')), f='epoch' ) ) )
		_.pr(x)
		return x

	# if _.switches.isActive('App'):
	#     import random
	#     n = random.randint(1000000000,9999999999)
	#     x = _nID.mini.gen( n )
	#     _.pr(x)        

	

	if _.switches.isActive('Encrypt'):
		x = _nID.mini.gen( _.switches.values('Encrypt')[0] )
		_.pr(x)
		if _.switches.isActive('List'):
			_.pr()
			for y in _key.imp.shapeKee():
				_nID.mini.password( y )
				x = _nID.mini.gen( _.switches.values('Encrypt')[0] )
				_.pr(x)

		return x

	if _.switches.isActive('Decrypt'):
		x = _nID.mini.resolve( _.switches.values('Decrypt')[0] )
		_.pr(x)
		return x



def load():
	if _.switches.isActive('Password'):
		_nID.mini.password( _.switches.values('Password')[0] )
	else:
		# _nID.mini.password( _keychain.imp.key('nID') )
		_nID.mini.password( _.appID_nID_password() )
	

import _rightThumb._nID as _nID
_keychain = _.regImp( __.appReg, 'keychain' )
# _.pr("_keychain.imp.key('nID')",_keychain.imp.key('nID'))
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()