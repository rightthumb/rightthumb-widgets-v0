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
	_.switches.register( 'AS', '-as', 'psd, xls' )
	_.switches.register( 'Path', '-path' )
	_.switches.register( 'App', '-app' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Alias', '-a,-alias','' )
	_.switches.register( 'Backup', '-b,-backup' )
	_.switches.register( 'Clean', '--c,-clean' )
	_.switches.register( 'OpenSingle', '-single', 'joins by space' )
	_.switches.register( 'ForceSublime', '-sub,-sublime' )
	_.switches.register( 'PrintAliasLocation', '-print' )
	_.switches.register( 'PrintAliases', '-pa,-ap,-printaliases', 'path' )
	_.switches.register( 'HostedTemp', '-tmp,-temp', 'ext name |alias> o.t' )
	_.switches.register( 'DoNotOpen', '-n,-no,-nope', 'used to create aliases but not open' )

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
	if _.switches.isActive('HostedTemp'):
		if not 'HostedTemp' in _v.fig:
			_.pr()
			_.pr()
			_.pr()
			_.pr('HostedTemp not found in settings',c='red')
			_.pr()
			_.pr('\tEdit this file:',_v.figpath,c='yellow')
			_.pr()
			_.pr('\tAdd this line:',c='green')
			_.pr()
			_.pr()
			_.pr('"HostedTemp": "{folder path to temp folder in a website project)}",',c='cyan')
			_.pr()
			_.pr()
			
			return None

		fo = _v.fig['HostedTemp']
		ext = None
		if not fo.endswith(os.sep): fo += os.sep
		if _.switches.value('HostedTemp'):
			ext =_.switches.values('HostedTemp')[0].strip().lower()
		if not ext: ext = '.htm'
		if not '.' in ext: ext = '.'+ext
		if _.switches.value('HostedTemp'):
			HT = _.switches.values('HostedTemp')
			HT[0]=ext.replace('.','')
			_.switches.fieldSet( 'HostedTemp', 'value', ','.join(HT) )
			_.switches.fieldSet( 'HostedTemp', 'values', HT )
		if not ext.startswith('.') and len(ext) < 5 and not '.' in ext:
			ext = '.'+ext 
		elif not ext.startswith('.'):
			ext = '_'+ext
		fi = fo + str(int(time.time())) + ext
		open(fi, 'w').close()
		_.switches.fieldSet( 'Files', 'active', True )
		_.switches.fieldSet( 'Files', 'value', fi )
		_.switches.fieldSet( 'Files', 'values', [fi] )


	if _.switches.isActive('Files'):
		paths=[]
		for _path_ in _.switches.values('Files'):
			if _path_.startswith('http:'): _path_ = _path_.replace('http:','https:')
			if _path_.startswith('http:') or _path_.startswith('https:'):
				_path_=_.url2file(_path_)
			if not os.path.isfile(_path_):
				_err = False
				if os.sep in _path_:
					try:
						_fo = __.path(_path_,pop=True)
					except:
						_err = True
						_.pr( 'Unable pop path to get folder: '+_path_ )
					if not os.path.isdir(_fo):
						try:
							os.makedirs(_fo)
						except:
							_err = True
							_.pr( 'Unable to create file: '+_fo )
				if not _err:
					try:
						if not _err:
							open(_path_, 'w').close()
					except:
						_.pr( 'Unable to create file: '+_path_ )
			paths.append(_path_)
		_.switches.fieldSet( 'Files', 'value', ','.join(paths) )
		_.switches.fieldSet( 'Files', 'values', paths )
	if _.switches.isActive('Alias') and not _.switches.isActive('Files') and len(_.switches.values('Alias')) ==1:
		_path_=_.switches.values('Alias')[0]
		if _path_.startswith('http:') or _path_.startswith('https:'):
			_path_=_.url2file(_path_)
			# print('here'); sys.exit();
			_.switches.fieldSet( 'Alias', 'active', False )
			_.switches.fieldSet( 'Files', 'active', True )
			_.switches.fieldSet( 'Files', 'value', _path_ )
			_.switches.fieldSet( 'Files', 'values', [_path_] )

	if _.switches.isActive('Alias') and not _.switches.isActive('Files') and len(_.switches.values('Alias')) ==1 and os.path.isfile(_.switches.values('Alias')[0]):
		aliases=_.getTable('file-open-aliases.hash')
		a=_.switches.values('Alias')[0]
		if 'aliases' in aliases and not a in aliases['aliases']:
			_.switches.fieldSet( 'Alias', 'active', False )
			_.switches.fieldSet( 'Files', 'active', True )
			_.switches.fieldSet( 'Files', 'value', a )
			_.switches.fieldSet( 'Files', 'values', [a] )

	if _.switches.isActive('OpenSingle'):
		if _.switches.value('OpenSingle').strip():
			paths=[ ' '.join(_.switches.values('OpenSingle')) ]
		else:
			if not sys.stdin.isatty():
				_.setPipeData( sys.stdin.readlines(), __.appReg, clean=_.l.conf('clean-pipe' ,d=True) )
			if _.appData[focus()]['pipe']:
				if type(_.appData[focus()]['pipe'][0]) == str:
					paths=[ ' '.join(_.appData[focus()]['pipe']) ]
				else:
					paths=[ ' '.join(_.appData[focus()]['pipe'][0]) ]
		# _.pv(_.appData)
		# print(_.appData[focus()]['pipe'])
		# print(paths)
		# sys.exit()

	if _.switches.isActive('Alias') and not _.switches.isActive('Files') and len(_.switches.values('Alias')) ==2:
		aa=None
		for a in _.switches.values('Alias'):
			if os.path.isfile(a):
				a=__.path(a)
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
	# elif not _.isWin and not 'code_editor' in _v.fig: app = 'nano'
	elif not _.isWin and 'code_editor' in _v.fig: app = _v.fig['code_editor']
	if not _.isWin:
		try:
			isgui = str(os.environ['isgui'])
		except:
			isgui = 'false'
		if not 'true' in isgui:
			app='nano'
		else:
			if not _.isWin:
				servers = {
								'yavin.m-eta.app': 'sudo -u scott /opt/sublime_text/sublime_text',
				}
				import socket
				host=str(socket.gethostname()).strip()
				if host in servers:
					app = servers[host]
				elif os.path.isfile('/opt/sublime_text/sublime_text'):
					app = '/opt/sublime_text/sublime_text'
	if _.switches.isActive('App'): app = ' '.join(_.switches.values('App'))
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
					#     # _.pr('taco',c='r')
					#     if (list == type(aliases['aliases'][_alias]) and path in aliases['aliases'][_alias]) or (str == type(aliases['aliases'][_alias]) and path == aliases['aliases'][_alias]):
					#         _.e('works')
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
		if _.switches.isActive('Files') or _.switches.isActive('Alias'):
			# if not _.switches.isActive('PrintAliases') and not _.switches.isActive('PrintAliasLocation'):
			if not _.switches.isActive('PrintAliases'):
				_.ad()
	if paths:
		logFi = _v.tt+os.sep+'file-open'+os.sep+_.friendlyDate(time.time()).split(' ')[0]+'.hash'
		_v.mkdir(logFi,f=1)
		log = _.getTable2(logFi)
		# print(logFi)
		session = str(__.startTime2)
		try: session = os.getenv('Session_ID')
		except: pass
		for path in paths:
			if _.switches.isActive('PrintAliases'):
				try:
					aliases
				except:
					aliases=_.getTable('file-open-aliases.hash')
				if _.switches.isActive('Clean'):
					for alias in aliases['files'][__.path(path)]:
						_.pr(alias,c='cyan')
					pass
				elif not _.switches.isActive('Clean'):
					if _.switches.value('PrintAliases') == 'path':
						_.pr(__.path(path),c='darkcyan')
						return __.path(path)
					_.pr()
					_.pr(__.path(path),c='darkcyan')
					_.pr()
					ai=0
					for alias in aliases['files'][__.path(path)]:
						ai+=1
						_.pr('\t',alias,c='cyan')
					_.pr('\n',_.addComma(ai),c='yellow')
				return None


				# try:
				# except: pass
				if not 'aliases' in aliases: aliases['aliases']={}
				if not 'files' in aliases: aliases['files']={}
				aliases['aliases']['last']=path

			path=__.path(path)
			path=_.zZip(path)
			if not _.switches.isActive('Path'):
				_.pr(path,c='yellow')
			aliases=_.getTable('file-open-aliases.hash')
			if not 'aliases' in aliases: aliases['aliases']={}
			if not 'files' in aliases: aliases['files']={}
			aliases['aliases']['last']=path
			if _.switches.isActive('HostedTemp'):
				HT = _.switches.values('HostedTemp')
				if len(HT) > 0:
					_ext_ = HT[0]
				else:
					_ext_ = 'htm' 
				aliases['aliases']['tmp']=path
				if len(HT) > 1:
					customAlias = 'ht.'+HT[1]
					aliases['aliases'][customAlias]=path
					_.pr('Alias:',customAlias)
				aliases['aliases']['ht.']=path
				_.pr('Alias:','ht.')
				i=1
				while 'ht.'+str(i) in aliases['aliases']: i+=1
				aliases['aliases']['ht.'+str(i)]=path
				_.pr('Alias:','ht.'+str(i))

				aliases['aliases']['ht.'+_ext_]=path
				_.pr('Alias:','ht.'+_ext_)

			_.saveText(path,_v.tt+os.sep+'file-open.last')
			if _.switches.isActive('PrintAliasLocation'): return None
				
			_.saveTable(aliases,'file-open-aliases.hash',p=0)
			if _.switches.isActive('DoNotOpen') and (  not 'bk' in _.switches.value('DoNotOpen') and not 'backup' in _.switches.value('DoNotOpen')   ):
				return None
			if _.switches.isActive('Backup'): backup(path)
			if _.switches.isActive('DoNotOpen'): return None
			if _.isWin:
				if os.path.isfile(path):
					found=False
					ext=_v.rt+os.sep+'file-open-ext.yml'
					if os.path.isfile(ext):
						exts=_.getYML(ext)
						for ex in exts:
							if _.switches.isActive('AS'):
								if _.switches.value('AS') == ex:  found=True;app=exts[ex];
							else:
								if path.lower().endswith('.'+ex): found=True;app=exts[ex];

					if not found:
						head=_v.rt+os.sep+'file-open-headers.yml'
						if os.path.isfile(head):
							headers=_.getYML(head)
							for header in headers:
								if _.IS(path,header): app = headers[header]
				# print('app',app)
				# print(_v.fig['code_editor'])
				# _.pv(_v.fig);
				# sys.exit();
				if _.switches.isActive('Path'):
					_copy = _.regImp( __.appReg, '-copy' )
					_copy.imp.copy( path, p=0 )
					return path
				if app == 'C:\\Program': app=_v.fig['code_editor']
				if _.switches.isActive('ForceSublime'): app = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
				# print(app);sys.exit();
				if not os.path.isfile(app):
					try:
						app=_v.fig['code_editor']
					except:
						_.e('Unable to open','app issue')
				if _.IS(path,'gzip'):
					gzip=True
					_.decompress(path)
				else:
					gzip=False
				try:
					if app == 0:
						subprocess.Popen([path])
					else:
						subprocess.Popen([ app, path])
				except:
					try:
						app=_v.fig['code_editor']
					except:
						_.e('Unable to open','app issue')

				if gzip:
					_.compress(path)
			else:
				if app == 'C:\\Program': app=_v.fig['code_editor']
				command = f'{app} {path}'
				os.system(command)
			if not path in log: log[path] = []
			log[path].append(session)
			if _.switches.isActive('Backup') and 'secure' in  _.switches.value('Backup'):
				if __.setting('fileBackup-secure_file'):
					backup(path,False)

		_.saveTable2(log,logFi)
		_.cleanUnzip()
bki=0

def backup(path,pre=True):
	if not os.path.isfile(path): return path
	global bki
	bki+=1
	appReg=__.appReg
	_bk={}
	_bk[bki] = _.regImp( __.appReg, 'fileBackup' )
	_bk[bki].switch( 'Silent' )
	
	if pre:
		_bk[bki].switch( 'isPreOpen' )
		isPreOpen=True
	else:
		# _bk[bki].switch( 'Silent',delete=True )
		_bk[bki].switch( 'isPreOpen', delete=True )
		isPreOpen=False
	_bk[bki].switch( 'Input', path )
	bkfi = _bk[bki].kwargs(pre=isPreOpen)
	__.appReg=appReg
	return bkfi

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()

# D:\websites\domains\sds.sh\public_html\tmp\1722636323ht.load2_js_body.js     ht.load2B     1



