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
	_.switches.register( 'App', '-app' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Alias', '-alias','' )
	_.switches.register( 'Backup', '-backup' )

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
	'file': 'file-open.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'open files such as a text file with sublime',
	'categories': [
						'open',
						'file',
						'sublime',
						'app',
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
						_.hp('p file-open -app %code_editor% -f app.js'),
						_.hp('p file-open -app $code_editor -f app.js'),
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

import subprocess
# focus()
# if _.switches.isActive('Backup'): 
# _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
# focus()

def action():
	paths=[]
	if _.switches.isActive('Files'):
		paths=_.switches.values('Files')
	elif _.isData():
		paths=_.isData()

	if _.isWin and not 'code_editor' in _v.fig: app = 'C:\\Windows\\System32\\notepad.exe'
	elif _.isWin and 'code_editor' in _v.fig: app = _v.fig['code_editor']
	elif not _.isWin and not 'code_editor' in _v.fig: app = 'nano'
	elif not _.isWin and 'code_editor' in _v.fig: app = _v.fig['code_editor']
	if _.switches.isActive('App'): app = _.switches.values('App')[0]
	if _.switches.isActive('Alias'):
		_aliases=_.switches.values('Alias')
		aliases=_.getTable('file-open-aliases.hash')


		if not aliases and paths:
			aliases={
						'aliases':{},
						'files':{},
			}
		elif not aliases:
			_.e('no aliases, create an alias','p file-open -alias important -f file.md')
		if paths:
			for path in paths:
				path=__.path(path)
				for _alias in _aliases: aliases['aliases'][_alias]=path; aliases['files'][path]=_alias;
			_.saveTable(aliases,'file-open-aliases.hash')
		elif not paths:
			for _alias in _aliases:
				if _alias in aliases['aliases']:
					paths.append( aliases['aliases'][_alias] )



	appReg=__.appReg
	__.appReg=appReg
	_.ad()
	if paths:
		
		for path in paths:
			# print('Backup',_.switches.isActive('Backup'))
			if _.switches.isActive('Backup'): _bk = _.regImp( __.appReg, 'fileBackup' ); __.appReg=appReg; _bk.switch( 'isPreOpen' ); _bk.switch( 'Input', path ); bkfi = _bk.action();
			# if _.switches.isActive('Backup'): _bk = _.regImp( __.appReg, 'fileBackup' ); bkfi = _bk.imp.action(path,o=1);
			# _.pr(__.path(path))
			subprocess.Popen([ app, __.path(path)])


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





