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
	_.switches.register( 'Generate', '-gen' )


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
	'file': 'bm-dirty.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'auto add bookmarks',
	'categories': [
						'bookmarks',
						'default',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'create bookmark to current folder',
						'    p m -a test',
						'list all bookmarks',
						'    p bookmarks',
						'quick generate bookmarks if blank',
						'   p bm-dirty | bash',
						'remove all bookmarks that no longer exist',
						'    p clean-bm -good -save',
						'bookmark location',
						'    p b -a ww',
						# '',
						# 'old not sure what it does',
						# '    p cleanBookmarks -?',
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


data=''



def action():
	global data
	d = _v.ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bm-dirty.txt'
	data = _.getText(d,raw=True)
	data+='\n\n'
	d = _v.ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bm-dirty.txt'
	if _.switches.isActive('Generate'):
		table = _.getTable('bookmarks.index')
		for k in table['labels']:
			kk = k.replace( chr(27), '' )
			kk = kk.replace( chr(10), '\n' )
			kk = kk.replace( '\r', '' )
			data+=kk+'|'+table['labels'][k]+'\n'
		data+='\n\n'
		_.saveText( data, d )
		# return None
	file = ''
	data = data.replace( chr(27), '' )
	data = data.replace( chr(10), '\n' )
	data = data.replace( '\r', '' )
	l=0
	while l < 50 and '\n|' in data:
		l+=1
		data=data.replace('\n|','|')
	text=''
	if not _.isWin:
		text += 'source $HOME/.bashrc\n\n'
	else:
		text += '%USERPROFILE%\\rr.bat\n\n'
	_.pr(text)
	spent={}
	data2 = data.split('\n')
	data2.reverse()
	for line in data2:
		text=''
		if line.count('|') == 1:
			a = line.split('|')[0]
			a=a.replace('\r','')
			a=a.replace('\n','')
			if len(a):
				bm = _v.resolveFolderIDs(line.split('|')[1])
				if os.path.isdir(bm):
					if not a in spent:
						spent[a]=1
						text += '\n'
						if _.isWin:
							text += bm[0]+':'
							text += '\n'

						text += 'cd '
						text += bm
						text += '\n'

						if _.isWin:
							text += _v.w+'\\widgets\\batch\\m.bat '
						else:
							text += _v.w+'/widgets/bash/nav/m.sh '
						text += a
						text += '\n'
						text += '\n'
						file += text
						_.pr(text)
	_copy.imp.copy( file )

_copy = _.regImp( __.appReg, '-copy' )


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







