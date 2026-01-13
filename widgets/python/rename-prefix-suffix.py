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
import shutil
##################################################

def appSwitches():
	pass
	_.switches.register( 'Prefix', '-p,-prefix', 'dnd' )
	_.switches.register( 'Suffix', '-x,-suffix', 'client' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )
	_.switches.register( 'Folder', '-o,-folder' )
	_.switches.register( 'Recursive', '-r,-recursive' )

_.autoBackupData = False
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
	'file': 'rename-prefix-suffix.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Rename file with prefix or suffix',
	'categories': [
						'rename',
						'prefix',
						'file',
						'suffix',
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

def rename(a,b):
	_.pr()
	_.pr(a)
	_.pr(b)
	_.pr()
	shutil.move(a,b)

def process(path):
	path = __.path(path)
	if not os.path.isfile(path):
		return None
	if not os.sep in path:
		file = path
		folder = ''
	else:
		tmp = path.split(os.sep)
		tmp.reverse()
		file = tmp[0]
		folder = path[:-len(file)]
		# dic={'i':file,'o':folder}
		# _.pr(dic)
	pass

	if _.switches.isActive('Suffix'):
		if not '.' in file:
			file = file + _.switches.values('Suffix')[0]
		else:
			tmp = path.split('.')
			tmp.reverse()
			ext = tmp[0]
			fi = path[:-len(ext)+1]
			fi = fi + _.switches.values('Suffix')[0]
			file = fi +'.'+ ext

	pass
	if _.switches.isActive('Prefix'):
		file = _.switches.values('Prefix')[0] + file
	pass
	rename(path,folder+file)



def getFolder(folder,r=False):
	if not os.path.isdir(folder):
		return None
	for file in os.listdir(folder):
		path = folder +os.sep+ file
		if os.path.isfile(path):
			process(path)
		elif r:
			getFolder(path,r)
			



def action():
	if _.switches.isActive('Recursive'):
		_.switches.fieldSet( 'Folder', 'active', True )

	if _.switches.isActive('Folder'):
		if len(_.switches.value('Folder')):
			_.pr('a',_.switches.value('Folder'))
			for folder in _.switches.values('Folder'):
				getFolder(folder,r=_.switches.isActive('Recursive'))
		else:
			_.pr('b')
			folder = os.getcwd()
			getFolder(folder,r=_.switches.isActive('Recursive'))


	if _.switches.isActive('Files'):
		for file in _.switches.values('Files'):
			process(file)


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()