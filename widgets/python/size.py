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
	_.switches.register( 'Size', '-z,-size,-i', '15mb  OR 356900864  ' )
	_.switches.register( 'Print', '-print' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'size.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'to bytes or from bytes',
	'categories': [
						'size',
						'calc',
						'bytes',
						'file size',
						'file',
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
						'p size -size 1kb ',
						'p size -size 1mb ',
						'p size -size 1gb ',
						'p size -size 1tb ',
						'',
						'p size -size 2899102925',
						'p size -size 2.7gb',
						'p size -size 57646075230342348809999',
						'p size -size 57.65zb',
						'p size -size 1.75yb',
						'',
						'',
						'p size -size 1kb 1mb 1gb 1tb 1pb 1eb 1zb 1yb',
						'',
						'p size -size 1024 1048576 1073741824 1099511627776 1125899906842624 1152921504606847000 1180591620717411303424 1208925819614629174706176',
						# 'p size -size 1024 1048576 1073741824 1099511627776 1125899906842624',
						# 'p size -size 1152921504606847000 1180591620717411303424 1208925819614629174706176',
						'',
						'includes:',
						'            petabyte, exabyte, zettabyte, yottabyte',
						'',
						'p size -print',
						'p size -print g',
						'p size -print g f',
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

sizes="""
1 Bit = Binary Digit
8 Bits = 1 Byte
1024 Bytes = 1 Kilobyte
1024 Kilobytes = 1 Megabyte
1024 Megabytes = 1 Gigabyte
1024 Gigabytes = 1 Terabyte
1024 Terabytes = 1 Petabyte
1024 Petabytes = 1 Exabyte
1024 Exabytes = 1 Zettabyte
1024 Zettabytes = 1 Yottabyte
1024 Yottabytes = 1 Brontobyte
1024 Brontobytes = 1 Geopbyte
"""


def action():
	if _.switches.isActive('Print'):
		_.pr()
		global sizes
		s = []
		for row in sizes.split('\n'):
			row = _str.cleanBE(row,' ')
			if '=' in row:
				a = row.split('=')[0]
				b = row.split('=')[1]
				a = _str.cleanBE(a,' ')
				b = _str.cleanBE(b,' ')
				s.append({ 'a': a, 'b': b })
		m=True
		if 'f' in _.switches.value('Print').lower():
			m=False
		if 'g' in _.switches.value('Print').lower():
			_.size_group__.pr(m)
		else:
			_.tables.r_.pr(s,h=0,l=0, p='  ')


	if len( _.switches.value('Size') ):
		for do in _.switches.values('Size'):
			if len(do):
				byt = True
				for x in do:
					if x in _str.alphaChar:
						byt = False
				if byt:
					_.pr( _.formatSize( int(do) ) )
				else:
					_.pr( int(_.unFormatSize( do )) )



########################################################################################
if __name__ == '__main__':
	action()







