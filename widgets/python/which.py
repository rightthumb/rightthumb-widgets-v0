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
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Path', '-path' )
	_.switches.register( 'Clean', '--c`' )


_.autoBackupData = False
# _.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'which.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'find location of executables',
	'categories': [
						'which',
						'tool',
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
						'p which -f python3.exe',
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


def check_folders( file, folders ):
	for folder in folders:
		# _.pr( folder )
		if _.switches.isActive('Path'):
			if _.showLine( folder ):
				_.pr( folder )
		else:
			if not folder.endswith( _v.slash ):
				folder = folder + _v.slash
			path = folder + file
			# _.pr(path)
			if os.path.isfile( path ):
				# _.pr(path)
				if not _.switches.isActive('Clean'):
					_.pr( _.cp( 'path:', 'cyan', p=0 ), _.cp(  path, 'green', p=0  ) )
				return path
			
			if _.isWin:
				if os.path.isfile( path+'.exe' ):
					if not _.switches.isActive('Clean'):
						_.pr( _.cp( 'path:', 'cyan', p=0 ), _.cp(  path+'.exe', 'green', p=0  ) )
					return path+'.exe'
	return None

def cleanLineB( line ):
	line = _str.cleanBE( line, '\r' )
	line = _str.cleanBE( line, '\n' )
	line = _str.cleanBE( line, '\t' )
	line = _str.cleanBE( line, ' '  )
	line = _str.replaceDuplicate( line, ' ' )
	return line

def cleanLine( line ):
	line = cleanLineB( line )
	line = cleanLineB( line )
	line = cleanLineB( line )
	line = cleanLineB( line )
	return line

def check_alias( file ):

	global aliases
	if not len( list(aliases.keys()) ):
		alias_path = _v.home +_v.slash+ '.bashrc'
		if os.path.isfile(alias_path):
			alias_temp = _.getText( alias_path )
			for line in alias_temp:
				line = cleanLine( line )
				if line.startswith('alias'):
					line = line[6:]
					for i,x in enumerate(line):
						if x == '=':
							a = line[ : i ]
							line = line[ i+1 : ]
							break
					line = line[:-1]
					line = line[1:]
					aliases[a] = line
	
	if file in aliases:
		if not _.switches.isActive('Clean'):
			_.pr( _.cp( 'alias:', 'cyan', p=0 ), _.cp(  aliases[file], 'green', p=0  ) )
		return aliases[file]
	return None
	

def check_variables( file ):
	global variables
	if not len( list(variables.keys()) ):
		variables = dict(os.environ)

	if file in variables:
		if not _.switches.isActive('Clean'):
			_.pr( _.cp( 'variable: ', 'cyan', p=0 ), _.cp(  variables[file], 'green', p=0  ) )
		return variables[file]

	for v in variables:
		if v.lower() == file.lower():
			if not _.switches.isActive('Clean'):
				_.pr( _.cp( 'variable: '+ v, 'cyan', p=0 ), _.cp(  variables[v], 'green', p=0  ) )
			return variables[v]
	for v in variables:
		if variables[v].lower().endswith( file.lower() ):
			if not _.switches.isActive('Clean'):
				_.pr( _.cp( 'variable: '+ v, 'cyan', p=0 ), _.cp(  variables[v], 'green', p=0  ) )
			return variables[v]

	for v in variables:
		if file.lower() in variables[v].lower():
			if not _.switches.isActive('Clean'):
				_.pr( _.cp( 'variable: ' + v, 'cyan', p=0 ), _.cp(  variables[v], 'green', p=0  ) )
			return variables[v]

def action():
	if _.switches.isActive('Path'):
		if _.isWin:
			check_folders(  'row', os.environ['PATH'].split(';')  )
		else:
			check_folders(  'row', os.environ['PATH'].split(':')  )
		return None

	for i,row in enumerate(_.isData(r=1)):
		if os.path.isfile(row):
			if not _.switches.isActive('Clean'):
				_.pr( _.cp( 'auto:', 'cyan', p=0 ), _.cp(  row, 'green', p=0  ) )
			return row
		if _.isWin:
			result = check_folders(  row, os.environ['PATH'].split(';')  )
		else:
			result = check_folders(  row, os.environ['PATH'].split(':')  )
			if not result is None:
				return result
			result = check_alias(  row  )
		# _.pr( 'here', row, result )
		if not result is None:
			return result

		result = check_variables( row )
		if not result is None:
			return result

		_.cp( 'not found' )


aliases = {}
variables = {}

import subprocess



########################################################################################
if __name__ == '__main__':
	action()







