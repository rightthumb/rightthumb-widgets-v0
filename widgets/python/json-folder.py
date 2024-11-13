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
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob', description='Files' )
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Folders', '-fo,-folder,-folders','/var/log/' )

	_.switches.register( 'index-by', '-index', 'Id' )

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
	'file': 'ls-json.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'ls json',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'ls',
						'json',
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


def getFolder(folder,r=False):
	if not os.path.isdir(folder): return None;

	try:
		files=os.listdir(folder)
	except Exception as e:
		return None

	for item in files:
		path=folder+os.sep+item
		if os.path.isfile(path): process(path);

		if r and os.path.isdir(path): getFolder(folder,r=r);



def process(path):
	path=__.path(path)
	# _.pr(path);sys.exit();
	# info = _dir.info(path)

	if True:
		try:

			_.v_file.append(  simplejson.loads( _.getText(path,raw=True) )  )

		except Exception as e:
			pass

def action():
	#--> min, architecture {:strict:}

	r=_.switches.isActive('Recursive')

	if _.switches.isActive('Files'):
		for path in _.switches.values('Files'):
			if type(path) == list:
				for p in path:
					process(p)
			else:
				process(path)
	elif _.switches.isActive('Folders') and len(_.switches.value('Folders')):
		for path in _.switches.values('Folders'):
			getFolder(path,r)
	elif _.switches.isActive('Folders') and not len(_.switches.value('Folders')):
		getFolder(os.getcwd(),r)
	else:
		getFolder(os.getcwd(),r)


	# _.pr(_.v_file)
	# _.pv(_.v_file)

	if not _.switches.isActive('index-by') or not len(_.switches.value('index-by')):
		_.pr( simplejson.dumps(_.v_file, indent=4, sort_keys=False ) )
	else:
		index={}
		for rec in _.v_file:
			index[ rec[_.switches.value('index-by')] ] = rec

		_.pr( simplejson.dumps(index, indent=4, sort_keys=False ) )

'''
simplejson.loads(var)
simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
'''
simplejson = __.imp('simplejson')

_.v_file = []

# import _rightThumb._dir as _dir

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





