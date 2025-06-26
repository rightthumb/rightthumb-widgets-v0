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
	_.switches.register( 'add', '-add' )
	_.switches.register( 'index', '-index' )
	_.switches.register( 'Folders', '-f,-fo,-folder,-p,-path,-folders' )
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'File-Meta', '-meta' )
	pass

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
	# 'app': '7facG-jo0Cxk',
	'file': 'index-folder.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'indexes folders and schedules indexes',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'index',
						'folders',
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

def _fig(path,r=None,m=None):
	if r is None: r=_.switches.isActive('Recursive');
	if m is None: m=_.switches.isActive('File-Meta');
	dic = {
				'epoch': int(time.time()),
				'path': path,
				'recursive': r,
				'meta': m,
	}
	path = __.path(path)
	san=_v.sanitizeFolder(path)
	hashy=_md5.string(   san, 'sha256'   )
	pa=_v.myIndexes+os.sep+'folders'+os.sep+'config'+os.sep; _v.mkdir(pa);
	paf=pa+hashy
	if not _.switches.isActive('Clean'): _.pr(paf);
	_.saveTable2(dic,paf)
	return paf



def _f(path):
	path = __.path(path)
	san=_v.sanitizeFolder(path)
	hashy=_md5.string(   san, 'sha256'   )
	dex=_v.myIndexes+os.sep+'folders'+os.sep+'index'+os.sep; _v.mkdir(dex);
	fi=dex+hashy
	if not _.switches.isActive('Clean'): _.pr(san);
	return fi

def _m(path):
	path = __.path(path)
	san=_v.sanitizeFolder(path)
	hashy=_md5.string(   san, 'sha256'   )
	dex=_v.myIndexes+os.sep+'folders'+os.sep+'meta'+os.sep; _v.mkdir(dex);
	fi=dex+hashy
	if not _.switches.isActive('Clean'): _.pr(san);
	return fi

def action():
	#--> min, architecture {:strict:}
	if _.switches.isActive('Folders'):
		folders=_.switches.values('Folders')
	else:
		folders=[os.getcwd()]


	if _.switches.isActive('add'):
		for path in folders:
			_.linePrint()
			f=_fig(path)
			f=_f(path)
			_.pr(path)
			_.pr(f)
		_.linePrint()

	elif _.switches.isActive('index'):
		fo=_v.myIndexes+os.sep+'folders'+os.sep+'config'+os.sep;
		for fig in _.fo(fo):
			path=__.path(fig)
			cnf = _.getTable2(path)
			file=_.fo(cnf['path'],cnf['recursive'])
			_.saveText(file,_f(cnf['path']))
			if cnf['meta']:
				_dir=__.imp('_rightThumb._dir')
				m=_m(cnf['path'])
				records=[]
				for fi in file:
					records.append( _dir.info(fi) )
				_.saveTable2(records,m)






import _rightThumb._dir as _dir




import _rightThumb._md5 as _md5


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




