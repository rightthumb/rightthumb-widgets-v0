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


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'burn.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'write zeros to temp python files',
	'categories': [
						'secure',
						'zeros',
						'over-write',
						'burn',
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
						'p burn',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START

import shutil

def genZeros():
	global overwriteWith
	if not overwriteWith is None:
		return overwriteWith
	char = '0'
	overwriteWith = ''
	row = ''
	for x in range(1,2000):
		row += char
	row += '\n'
	for x in range(1,2000):
		overwriteWith += row
	return overwriteWith



def buildFolders( path ):
	folder = path
	parts = folder.split( _v.slash )
	parts.pop()

	newParts = []

	for p in parts:

		newParts.append( p )
		f = _v.slash.join( newParts )

		if os.name == 'posix':
			if not f.startswith(_v.slash):
				f = _v.slash+f
		# _.pr(f)
		exist = os.path.isdir( f )
		if not exist:
			try:
				# _.pr(f)
				os.mkdir( f )
			except Exception as e:
				pass


def process( path ):
	_.saveText( genZeros(), path )
	os.remove(path)



def getFolder( folder ):
	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path):
				# _.pr(path)
				if path.endswith('.py'):
					process( path )

			if os.path.isdir(path):
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder):
					try:
						getFolder( newFolder )
					except Exception as e:
						pass

def action():
	global srcfolder


	
	getFolder( _v.python['burn']['windows'] )
	shutil.rmtree( _v.python['burn']['windows']+_v.slash+'_rightThumb' )
	getFolder( _v.python['burn']['unix'] )
	shutil.rmtree( _v.python['burn']['unix']+_v.slash+'_rightThumb' )



overwriteWith = None
########################################################################################
if __name__ == '__main__':
	action()







