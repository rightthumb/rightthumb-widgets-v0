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
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data', description='Files' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'decrypt-docs.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'decrypt registered documentation files',
	'categories': [
						'decrypt',
						'docs',
						'tool',
						'file',
						'text',
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
						_.hp('p thisApp -file file.txt'),
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


def identify(row):
	n = '0123456789'
	l = 'abcdefghijklmnopqrstuvwxyz'
	u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/+='
	for ch in row:
		if not ch in chars:
			return False
	if ' ' in row:
		return False
	elif '\\' in row:
		return False
	elif '//' in row:
		return False
	elif 'http' in row:
		return False
	elif '=' in row and not row.endswith('='):
		return False
	elif row.endswith('=='):
		return True
	elif row.endswith('=') and len(row) > 15:
		return True
	elif row.count('/') > 5 or row.startswith('/'):
		return False

	else:
		if len(row) < 7:
			return False

		doc = []
		nn = 0
		ll = 0
		uu = 0
		for ch in row:
			if ch in n:
				doc.append('n')
				nn+=1
			elif ch in l:
				doc.append('l')
				ll+=1
			elif ch in u:
				doc.append('u')
				uu+=1
		if uu == 0 or ll == 0  or nn == 0:
			return False
		if uu > ll and ll > 3:
			return True
		
		if nn < 3 and len(row) < 8:
			return False
		if uu < 3 or ll < 3 :
			return False
		p = _.percentageDiffInt( uu, ll )
		if p > 75:
			return True
		# print( p, uu, ll, row )
		# print( doc )
		return False


	return False

records = {}
maxLen = 0
def process(row):
	global records
	global maxLen
	if identify(row):
		try:
			row2 = _vault.imp.s.de( row )
			good = True
			if '\n' in row2:
				good = False
			for ch in row2:
				if ch not in _str.printable2:
					good = False
			if good:
				records[row] = row2
				if len(row2) > maxLen:
					maxLen = len(row2)
				# row = row2
		except Exception as e:
			pass
		# if row.startswith('!VAULT!'):
		# 	print( row )

	return row
	
def addSpaces(row):
	global maxLen
	y = maxLen - len(row) + 5
	i=0
	t = ''
	while not i == y:
		i+=1
		t+=' '
	return t

def action():
	global records
	global maxLen
	if _.switches.isActive('Test'):
		row = ' '.join( _.switches.values('Test') )
		row = process(row)
		return None

	# print(_.isData())
	file = []
	for i,row in enumerate( _.isData(r=1) ):
		row = process(row)
		file.append(row)
	nFile = []
	for row in file:
		if row in records:
			row = records[row] + addSpaces(records[row]) + '!VAULT!'
		nFile.append(row)
	data = '\n'.join(nFile)
	_.saveText( data, _.switches.values('Files')[0] )


import _rightThumb._vault as _vault

_vault = _.regImp( __.appReg, '_rightThumb._vault' )
focus()


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






