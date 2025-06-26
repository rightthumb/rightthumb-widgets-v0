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
	pass
	_.switches.register( 'Files', '-f,-file,-files' )

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
	'file': 'blank-file.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'create blank file with header or template',
	'categories': [
						'.sh',
						'.bat',
						'.htm',
						'.html',
						'file',
						'template',
						'blank',
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
						_.hp(''),
						_.hp('bl dl.sh'),
						_.hp(''),
						_.hp('p blank-file -f index.htm'),
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
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

def confirm():
	_.cp( _.linePrint(txt='*',p=0), 'red' )
	_.cp( [ '  \t', 'ABOUT TO ERASE FILE!!!!!!!!!' ], 'yellow' )
	_.cp( _.linePrint(txt='*',p=0), 'red' )
	
		


def process(path):
	if os.sep in path:
		_v.dir_check_create( _v.popFile(path) )
	if os.path.isfile(path):
		_.cp('The file already exists!!','red')
		ask=input('   clear? Y/n/o:').lower()
		if 'o' in ask:
			editor(path)
			return None
		if 'n' in ask:
			return None
		confirm()
		ask=input('   SURE ? Y/n/o:').lower()
		if 'o' in ask:
			editor(path)
			return None
		if 'n' in ask:
			return None
		ask=input('   LAST CHANCE!! ? Y/n/o:').lower()
		if 'o' in ask:
			editor(path)
			return None
		if 'n' in ask:
			return None
		return __.file_headers(path).default()
	return __.file_headers(path).default()

def action():
	if _.switches.isActive('Files'):
		for path in _.switches.values('Files'):
			# _.pr('____________')
			# test=__.file_headers(path).default()
			# _.pr(test)
			# _.pr(type(test))
			# _.pr('____________')

			f = process(path)
			if type(f) == str:
				if _.isWin:
					editor(path)
					time.sleep(.01)
				_.saveText( f, path )
				if not _.isWin:
					editor(path)
				_.cp('saved','green')
			else:
				_.cp('aborted','red')

def editor(path):
	if _.isWin:
		_file_open.switch('Files',path)
		_file_open.action()
	else:
		_file_open.switch('Files',path)
		_file_open.action()
	_.pr(_v.meta['code_editor'],path)


_file_open = _.regImp( __.appReg, 'file-open' )
_file_open.switch('App',_v.meta['code_editor'])
import _rightThumb._string as _str


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





