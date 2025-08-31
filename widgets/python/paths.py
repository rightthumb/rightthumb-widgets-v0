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
	_.switches.register( 'Files', '-f,-file,-files','file.txt' )
	_.switches.register( 'Folders', '-folder,-folders' )
	_.switches.register( 'Validate', '-v,-validate' )
	_.switches.register( 'WSL', '-wsl' )
	_.switches.register( 'Multiple', '-m,,-multi,-multiple' )
	_.switches.register( 'DoubleSlash', '-d,-b,-dd,-double,-doubleslash' )


# _.autoBackupData = __.autoCreationConfiguration['backup']
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'paths.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Print to full path to specified files',
	'categories': [
						'tool',
						'path',
						'file',
						'files',
						'print',
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
						'',
						'b git',
						'p paths',
						'',
						'p paths -f index.htm',
						'',
						'p file --c | p paths -v',
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



	########################################################################################
	# _.switches.trigger( 'Files', _.path_sep )
	_.switches.trigger( 'Files', _.aliasesFi )
	########################################################################################
	
	
	
	
	# _.switches.trigger( 'Files', _.myFileLocations )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Duration', _.timeFuture )
	
	
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

def wsl(path,just=False):
	subject = path
	if not just:
		if not _.switches.isActive('WSL'):
			subby = subject.replace( '\\', '\\\\' )
			if _.switches.isActive('DoubleSlash'):
				_copy = _.regImp( __.appReg, '-copy' )
				try:
					_copy.imp.copy( subby )
				except:
					_pr( subby )
			else:
				_pr( subby )
	git_path = subject
	git_path = git_path.replace( _v.slashes['w'], _v.slashes['u'] )
	git_path = git_path.replace( ':', '' )
	git_path = _v.slashes['u'] + git_path
	if not _.switches.isActive('WSL'): _pr( git_path )
	wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
	wsl5=wsl5.replace(' ','\\ ')
	# _pr( wsl5 )
	return wsl5

def _pr(*args,**kwargs):
	if args:
		_.pr(*args,**kwargs)


import platform

def action():
	


	if not _.switches.isActive('Validate'):


		if type(_.appData[__.appReg]['pipe']) == list:
			subjects = _.appData[__.appReg]['pipe']
		
		elif _.switches.isActive( 'Files' ):
			if _.switches.isActive('Multiple'):
				subjects = _.switches.values('Files')
			else:
				subjects = [' '.join(_.switches.values('Files'))]	
		elif _.switches.isActive( 'Folders' ):
			if _.switches.isActive('Multiple'):
				subjects = _.switches.values('Folders')
			else:
				subjects = [' '.join(_.switches.values('Folders'))]	

		else:
			subjects = [os.getcwd()]

		# _site = _.regImp(__.appReg,'site')
		# _site = _.regImp( __.appReg, 'site' )
		# _site.switch('Files',subjects)
		# _site.action()
		for subject in subjects:
			subject = __.path(subject)
			_.pr( subject, c='cyan' )
			_.pr(line=1,c='yellow')
			if _.switches.isActive('WSL'):
				wslPath = wsl(subject,True)
				_copy = _.regImp( __.appReg, '-copy' )
				try:
					_copy.imp.copy( wslPath )
				except:
					_pr( wslPath )
				return None
			try:
				subject = __.path(subject)
				subby = subject.replace(os.getcwd(),'')
				if subby and not subby == subject:
					if __.isWin and subby.startswith(os.sep):
						subby = subby[1:]
					if not __.isWin and subby.startswith(os.sep):
						subby = '.'+subby
					if not _.switches.isActive('WSL'): _pr(subby)
				if not _.switches.isActive('WSL'):
					if not _.switches.isActive('DoubleSlash'):
						_copy = _.regImp( __.appReg, '-copy' )
						try:
							_copy.imp.copy( subject )
						except:
							_pr( subject )
					else:
						_pr( subject )
				if subject.startswith('/mnt/'):
					sub = subject[5:]
					dr=sub[0]
					sub = sub[1:]
					if not _.switches.isActive('WSL'): _pr( dr.upper()+':'+sub.replace('/','\\') )

				if platform.system() == 'Windows':
					_pr(wsl(subject))






				if not _.switches.isActive('WSL'): _pr( _.path2url( subject ) )

				if _v.sanitizeFolder( subject ).startswith('{'):
					if not _.switches.isActive('WSL'): _pr( _v.sanitizeFolder( subject ) )
		

			except Exception as e:
				pass


			if not _.switches.isActive('WSL'): _pr()
			def cend(sub):
				if sub.endswith('/'): return sub;
				return sub
			def cstart(sub):
				if sub.startswith('/'): return sub;
				return '/'+sub

			def me(fi,fo): return cstart(fi.replace(fo,'').replace(os.sep,'/'));
			def pr(sub,fi,fo, c='cyan'): _pr('\t',(cend(sub.replace('://','8f13ad0d8a77'))+me(fi,fo)).replace('//','/').replace('//','/').replace('8f13ad0d8a77','://'),c=c);
			dic=_.fometa(subject)
			if 'sftp' in dic:
				if not _.switches.isActive('WSL'): _pr('.folder.meta',_.pr(dic['folder'],p=0,c='yellow'))
				# if 'path' in dic['sftp']: pr( dic['sftp']['path'],subject,dic['folder'] );
				if 'full-path' in dic['sftp']: pr( dic['sftp']['full-path'],subject,dic['folder'] );
			if 'url' in dic:
				if not _.switches.isActive('WSL'): pr( dic['url'],subject,dic['folder'], c='green' );
			for srv in '.h .b .m .e'.split(' '):
				if not _.switches.isActive('WSL'): _pr()
				dic=_.fometa(subject,srv)
				# _pr(dic)
				if 'sftp' in dic:
					if not _.switches.isActive('WSL'): _pr('.folder.meta'+srv,_pr(dic['folder'],p=0,c='yellow'));
					# if 'path' in dic['sftp']: pr( dic['sftp']['path'], subject,dic['folder'] );
					if 'full-path' in dic['sftp']: pr( dic['sftp']['full-path'], subject,dic['folder'] );
				if 'url' in dic:
					if not _.switches.isActive('WSL'): pr( dic['url'],subject,dic['folder'], c='green' );
			if not _.switches.isActive('WSL'): _pr()






	elif _.switches.isActive('Validate'):
		for i,row in enumerate(_.isData(r=1)):
			try:
				path = os.path.abspath(row)
				if os.path.isfile(path) or os.path.isdir(path):
					_.colorThis( path , 'yellow'  )
				else:
					_.colorThis( row , 'red'  )
			except Exception as e:
				_.colorThis( row , 'red'  )


########################################################################################
if __name__ == '__main__':
	action()








