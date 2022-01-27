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
	_.switches.trigger( 'Files', _.path_sep )
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

import platform

def action():

	if not _.switches.isActive('Validate'):


		if type(_.appData[__.appReg]['pipe']) == list:
			subjects = _.appData[__.appReg]['pipe']
		
		elif _.switches.isActive( 'Files' ):
			subjects = _.switches.values( 'Files' )

		elif _.switches.isActive( 'Folders' ):
			subjects = _.switches.values( 'Folders' )

		else:
			subjects = [os.getcwd()]


		for subject in subjects:
			try:
				subject = __.path(subject)
				subby = subject.replace(os.getcwd(),'')
				if subby and not subby == subject:
					if __.isWin and subby.startswith(os.sep):
						subby = subby[1:]
					if not __.isWin and subby.startswith(os.sep):
						subby = '.'+subby

					print(subby)
				print( subject )
				if subject.startswith('/mnt/'):
					sub = subject[5:]
					dr=sub[0]
					sub = sub[1:]
					print( dr.upper()+':'+sub.replace('/','\\') )

				if platform.system() == 'Windows':
					print( subject.replace( '\\', '\\\\' ) )
					git_path = subject
					git_path = git_path.replace( _v.slashes['w'], _v.slashes['u'] )
					git_path = git_path.replace( ':', '' )
					git_path = _v.slashes['u'] + git_path
					print( git_path )

					wsl = '/mnt/'+ git_path[1].lower() + git_path[2:]
					print( wsl )
					




				print( _.path2url( subject ) )

				if _v.sanitizeFolder( subject ).startswith('{'):
					print( _v.sanitizeFolder( subject ) )
		

			except Exception as e:
				pass









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






