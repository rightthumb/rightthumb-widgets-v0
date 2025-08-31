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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='data', description='Files' )
	_.switches.register( 'Folder', '-folder,-end,-last','VC' )
	_.switches.register( 'OS', '-os','linux OR win OR w' )
	_.switches.register( 'Count', '-count' )
	_.switches.register( 'Clean', '--c' )


_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
__.isRequired_or_List = ['Pipe','Files']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'extract-folder.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'end file on a specific folder and remove duplicates',
	'categories': [
						'folder',
						'pop file',
						'pop folder',
						'end on',
						'last folder',
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
						_.hp('p dirDB + Visual Studio \\VC\\ --c  > %tmpf7%'),
						_.hp(''),
						_.hp('p extract-folder -f %tmpf7% -folder VC'),
						_.hp(''),
						_.hp('p dirDB + Visual Studio \\VC\\ --c | p extract-folder  -folder VC -count'),
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
	# _.switches.trigger( 'Files', _.myFileLocations )
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START


v = _.dot()


def test(path):
	if v.folder is None:
		return True
	if v.folder.lower() in path.lower():
		return True
	return False

def extract(path):
	if v.folder is None:
		return __.path(path,pop=True)

	parts = path.split(v.sep)
	result=[]
	for p in parts:
		result.append(p)
		if v.folder.lower() == p.lower():
			return v.sep.join( result )+v.sep
	return v.sep.join( result )+v.sep

def tPath(subject):
	if _.isWin:
		test_path = subject.lower()
	else:
		test_path = subject
	return test_path
def action():
	v.count = _.switches.isActive('Count')
	v.sep = os.sep
	if _.switches.isActive('Folder'):
		v.folder = ' '.join(  _.switches.values('Folder')  )
	else:
		v.folder = None
	if _.switches.isActive('OS'):
		if 'w' in _.switches.value('OS').lower():
			v.sep = '\\'
		else:
			v.sep = '/'

	result = []
	counter = {}
	

	for i,path in enumerate( _.isData(r=1) ):
		path = _str.replaceDuplicate(path,v.sep)
		if test(path):
			subject = extract(path)
			test_path = tPath(subject)
			if test_path in counter:
				counter[test_path] += 1
			else:
				counter[test_path] = 1
				result.append(subject)
	pass

	if v.count:
		_.switches.fieldSet( 'Long', 'active', True )
		records=[]
		for path in result:
			records.append({ 'sort': counter[tPath(path)], 'count': _.addComma(counter[tPath(path)]), 'path': path })
		pass
		new = _.tables.returnSorted( 'data', 'a.sort', records )
		_.tables.print( 'data', 'count,path' )

	elif not v.count:
		for path in result:
			_.cp(path,'cyan')

	if not _.switches.isActive('Clean'):
		_.cp( ['\n', _.addComma(len(result)), 'of', _.addComma(len(_.isData())) ], 'yellow' )






########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




