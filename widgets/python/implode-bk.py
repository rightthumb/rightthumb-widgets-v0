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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', isRequired=True, description='Files' )
	# _.switches.register( 'Save', '-save', isRequired=True )
	# _.switches.register( 'Compile', '-compile' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'implode.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'stickytape a python file to a single file not requiring any imports   AND THEN   compile',
	'categories': [
						'stickytape',
						'single file',
						'imports',
						'import',
						'single',
						'python',
						'tool',
						'utility',
						'convert',
						'adapt',
						'process',
						'pre compile',
						'compile',
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
						'p implode -f pass.py',
						'p implode -f *.py',
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

import stickytape
import py_compile
import shutil

def saveFile( path ):
	ff = _.fileFolder( path )

	if _v.python['src']['windows'] in ff['folder']:
		folder = _v.python['imploded']['windows']

	elif _v.python['src']['unix'] in ff['folder']:
		folder = _v.python['imploded']['unix']

	# if not os.path.isdir(folder):
	#     os.mkdir(folder)
	return folder + _v.slash + ff['file']


def pycFolder():


	# _v.python['compiled']['unix']

	f = _v.python['imploded']['windows']+_v.slash+'__pycache__'
	if os.path.isdir(f):
		for file in os.listdir(f):
			if file.endswith('.pyc'):
				oFile = f +_v.slash+ file
				nFile = _v.python['compiled']['windows'] +_v.slash+ file.replace( 'cpython-36.', '' )
				try:
					shutil.move( oFile, nFile )
				except Exception as e:
					_.colorThis( [ 'Error: moving file', file.replace( 'cpython-36.', '' ) ], 'red' )
		i=0
		for file in os.listdir(f):
			if file.endswith('.pyc'):
				i+=1
		if not i:
			try:
				shutil.rmtree(f)
			except Exception as e:
				_.colorThis( [ 'Error: moving folder', f ], 'red' )


	f = _v.python['imploded']['unix']+_v.slash+'__pycache__'
	if os.path.isdir(f):
		for file in os.listdir(f):
			if file.endswith('.pyc'):
				oFile = f +_v.slash+ file
				nFile = _v.python['compiled']['unix'] +_v.slash+ file.replace( 'cpython-36.', '' )
				try:
					shutil.move( oFile, nFile )
				except Exception as e:
					_.colorThis( [ 'Error: moving file', file.replace( 'cpython-36.', '' ) ], 'red' )
		i=0
		for file in os.listdir(f):
			if file.endswith('.pyc'):
				i+=1
		if not i:
			try:
				shutil.rmtree(f)
			except Exception as e:
				_.colorThis( [ 'Error: moving folder', f ], 'red' )



def action():

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			_.pr( row )
			# _.pr( saveFile( row ) )
			try:
				if os.path.isfile(row):
					try:
						result = stickytape.script( row )
						try:
							_.saveText( result, saveFile( row ) )
							try:
								py_compile.compile( saveFile( row ) )
							except Exception as e:
								_.colorThis( '\tError: compile', 'red' )
						except Exception as e:
							_.colorThis( '\tError: save', 'red' )
					except Exception as e:
						_.colorThis( '\tError: stickytape', 'red' )
			except Exception as e:
				pass
	pycFolder()



########################################################################################
if __name__ == '__main__':
	action()