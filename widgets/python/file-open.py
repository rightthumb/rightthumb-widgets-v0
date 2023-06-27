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
	_.switches.register( 'Backup', '-b,-backup' )
	_.switches.register( 'Clean', '--c,-clean' )

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

def action(path=None):

	if _.switches.isActive('Alias') and not _.switches.isActive('Files') and len(_.switches.values('Alias')) ==2:
		aa=None
		for a in _.switches.values('Alias'):
			if os.path.isfile(a):
				_.switches.fieldSet( 'Files', 'active', True )
				_.switches.fieldSet( 'Files', 'value', a )
				_.switches.fieldSet( 'Files', 'values', [a] )
			else:
				aa=a
		
		_.switches.fieldSet( 'Alias', 'value', aa )
		_.switches.fieldSet( 'Alias', 'values', [aa] )
	paths=[]
	if not path is None:
		paths=[path]
	else:
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
		elif not aliases: _.e('no aliases, create an alias','p file-open -alias important -f file.md')

		if paths:
			for path in paths:
				path=__.path(path)
				for _alias in _aliases:

					#b)--> actual code
					aliases['aliases'][_alias]=path
					if not path in aliases['files']: aliases['files'][path]=[]
					if not _alias in aliases['files'][path]: aliases['files'][path].append(_alias)
					#e)--> actual code
					
					#b)--> testing
					# if _alias in aliases['aliases']:
					# 	# _.pr('taco',c='r')
					# 	if (list == type(aliases['aliases'][_alias]) and path in aliases['aliases'][_alias]) or (str == type(aliases['aliases'][_alias]) and path == aliases['aliases'][_alias]):
					# 		_.e('works')
					#e)--> testing







			_.saveTable(aliases,'file-open-aliases.hash')
		elif not paths:
			for _alias in _aliases:
				if _alias in aliases['aliases']:
					if list == type(aliases['aliases'][_alias]):
						for _al in aliases['aliases'][_alias]:
							paths.append( _al )

					elif str == type(aliases['aliases'][_alias]):
						paths.append( aliases['aliases'][_alias] )


	appReg=__.appReg
	__.appReg=appReg
	if not _.switches.isActive('Clean'):
		# print(paths)
		_.ad()
	if paths:
		logFi = _v.tt+os.sep+'file-open'+os.sep+_.friendlyDate(time.time()).split(' ')[0]+'.hash'
		_v.mkdir(logFi,f=1)
		log = _.getTable2(logFi)
		session = str(__.startTime2)
		try: session = os.getenv('Session_ID')
		except: pass
		for path in paths:
			path=__.path(path)
			path=_.zZip(path)
			_.pr(path)
			if _.switches.isActive('Backup'): backup(path)
			if _.isWin:
				subprocess.Popen([ app, path])
			else:
				command = f'{app} {path}'
				os.system(command)
			if not path in log: log[path] = []
			log[path].append(session)
		_.saveTable2(log,logFi)
		_.cleanUnzip()

def backup(path):
	appReg=__.appReg
	_bk = _.regImp( __.appReg, 'fileBackup' )
	_bk.switch( 'Silent' )
	_bk.switch( 'isPreOpen' )
	_bk.switch( 'Input', path )
	bkfi = _bk.action()
	__.appReg=appReg
	return bkfi

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





