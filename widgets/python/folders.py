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

	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Folder', '-f,-folder')
	_.switches.register('Blank', '-blank')
	_.switches.register('Clean', '-clean')
	_.switches.register('MaxDepth', '-depth', '3')
	_.switches.register('Relative-Path', '-rr,-rel,-relative')
	_.switches.register('No-Linked-Folders', '-nl,-nolinks' )
	# _.switches.register('Not-Recursive', '-r' )


	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'folders.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'folder tool',
	'categories': [
						'folders',
						'tool',
						'os',
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
						'p folders ',
						'p folders ',
						'p folders -blank ',
						'p folders -blank -clean ',
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

def process( folder ):
	if folder.startswith('/proc'):
		return None

	global activeFolders
	global allFolders
	global i


	if not os.path.isdir(folder):
		return None
		
	if _.switches.isActive('No-Linked-Folders'):
		if os.path.islink(folder):
			return None
	folder = os.path.abspath( folder )



	global baseDepth
	global base_path
	if _.switches.isActive('MaxDepth'):
		if len(_.switches.value('MaxDepth')):
			maxDepth = int(_.switches.values('MaxDepth')[0])
		else:
			maxDepth = 4
		if len( folder.split(_v.slash) ) - baseDepth >= maxDepth:
			if len(_.switches.values('MaxDepth')) > 1 and 'p' in _.switches.values('MaxDepth')[1]:
				_.pr( folder )

			return None



	try:
		dirList = os.listdir(folder)
	except Exception as e:
		return None
		
	for item in dirList:
		path = folder + _v.slash + item
		path = path.replace( _v.slash+_v.slash, _v.slash )
		path = path.replace( _v.slash+_v.slash, _v.slash )
		# if os.path.isfile(item):
		if os.path.isfile(path):
			if not folder.lower() in activeFolders:
				activeFolders[ folder.lower() ] = 1
			pathParts = folder.split( _v.slash )
			while len(pathParts):
				pathParts.pop( len(pathParts)-1 )
				pp = _v.slash.join(pathParts)
				if not pp.lower() in activeFolders:
					activeFolders[ pp.lower() ] = 1

		elif os.path.isdir(path):
			if _.showLine(path):
				allFolders.append( path )
				i = i + 1
				if not _.switches.isActive('Blank'):
					if _.switches.isActive('Relative-Path'):
						pAth = path.replace(base_path,'')[1:]
						_.pr( pAth, c='cyan' )
					else:
						_.pr( path, c='cyan' )
			process( path )



		# _.pr('\n{}\n{}'.format(i,folder))
		# _.pr('',i)

baseDepth = 0
def action():

	if _.switches.isActive('Clean'):
		_.switches.fieldSet( 'Blank', 'active', True )

	global activeFolders
	global allFolders
	global i
	global baseDepth
	global base_path
	i = 0
	if not _.switches.isActive('Count'):
		_.pr()
		_.colorThis( [  'Folders:\n'  ], 'green' )
		# _.pr('Folders:\n')

	if _.switches.isActive('Folder'):
		for folder in _.switches.values('Folder'):
			baseDepth = len( folder.split(_v.slash) )
			base_path=folder
			process( folder )
			allFolders.append(folder)
	else:
		folder = os.getcwd()
		baseDepth = len( folder.split(_v.slash) )
		base_path=folder
		process( folder )
		allFolders.append(folder)

	# i = 0
	# print(allFolders)
	if  _.switches.isActive('Blank'):
		allFolders.reverse()
		ii = 0
		for f in allFolders:
			if not f.lower() in activeFolders:
				if _.switches.isActive('Clean'):
					if del_folder(f):
						ii+=1



	if  _.switches.isActive('Blank'):
		if not _.switches.isActive('Count') :
			if i == ii:
				_.colorThis( [  '',i  ], 'yellow' )
			else:
				_.colorThis( [  '',ii, 'of', i, 'are blank'  ], 'yellow' )
	

	elif  not _.switches.isActive('Blank'):
		if not _.switches.isActive('Count') :
			_.colorThis( [  '',i  ], 'yellow' )
	
	if not _.switches.isActive('Count') :
		_.pr()
		_.colorThis( [  folder  ], 'darkcyan' )


def del_folder(folder):
	

	# return None
	try:
		os.rmdir(folder)
		_.pr(folder,c='red')
		return True
	except OSError as e:
		_.pr(folder,c='green')
		return False
		_.pr("Error: %s : %s" % (folder, e.strerror))

activeFolders = {}
allFolders = []

########################################################################################
if __name__ == '__main__':
	action()