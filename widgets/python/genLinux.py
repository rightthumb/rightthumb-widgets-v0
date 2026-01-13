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
	_.switches.register( 'PrintPath', '-pp,-path,-print' )
	_.switches.register( 'SH', '-sh' )
	# _.switches.register( 'Files', '-f,-file,-files' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'tool.js.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'upload tool.js',
	'categories': [
						'tool.js',
						'upload',
						'ftp',
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
						'p tool.js',
						'',
						'p genLinux',
						'p genLinux -sh',
						'p genLinux + tool2',
						'p genLinux + linux',
						'p genLinux + databank',
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


def ftp_upload():
	# ftp_upload_ssh()

	# _.pr( 'upload', upload )
	# sys.exit()

	userA = 'ay7q2HGaNN6mSWaVZniaEw=='
	passwordA = 'Vpcgt45SYQBXyM7q3c8CfeP0x9fixit2Ar7NJT3b3B7n/x8vIFGNjQ=='

	userB = _blowfish.decrypt( userA, _vault.key() )
	passwordB = _blowfish.decrypt( passwordA, _vault.key() )

	userB = _str.cleanBE( userB, ' ' )
	passwordB = _str.cleanBE( passwordB, ' ' )

	# _.pr( userB )
	# _.pr( passwordB )
	# sys.exit()

	ftp = FTP()
	ftp.connect('107.180.54.171', 21)
	ftp.login(userB, passwordB)
	if _.showLine('linux.zip'):
		# _.pr('D:\\websites\\tools.RightThumb\\tools\\linux.zip')
		_.updateLine('')
		_.updateLine( 'uploading linux.zip', 'darkcyan' )
		ftp.storbinary('STOR linux.zip', open('D:\\websites\\tools.RightThumb\\tools\\linux.zip', 'rb'))
		_.updateLine('')
		_.cp(['uploaded','linux.zip'],'green')
		md5_check('linux.zip')

	if _.showLine('databank.zip'):
		# _.pr('D:\\websites\\tools.RightThumb\\tools\\databank.zip')
		_.updateLine('')
		_.updateLine( 'uploading databank.zip', 'darkcyan' )
		ftp.storbinary('STOR databank.zip', open('D:\\websites\\tools.RightThumb\\tools\\databank.zip', 'rb'))
		_.updateLine( '' )
		_.cp(['uploaded','databank.zip'],'green')
		md5_check('databank.zip')
		
	ftp.close()
	_.updateLine( 'connection closed', 'darkcyan', .5 )
	_.updateLine('')
	_beep.beep()


def ftp_upload_ssh():
	paths = []

	# paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'python'  +os.sep+ 'src' +os.sep+ 'unity' +os.sep+ 'bashrc.py' )
	paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  '101-auto-setup.sh' )
	if os.path.isfile('D:\\websites\\Reph.us\\tools\\tool.js'):
		paths.append( 'D:\\websites\\Reph.us\\tools\\tool.js' )
	paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'load-vars.sh' )
	# paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+    'help.txt' )
	# paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'py'  +os.sep+  'tool2' )
	paths.append( _v.widgets+os.sep+'install'  +os.sep+  'installer.py' )
	paths.append( _v.widgets+os.sep+'install'  +os.sep+  'README.TXT' )
	paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'php'  +os.sep+  'zip.php' )
	paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'php'  +os.sep+  'md5.php' )
	# paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'php'  +os.sep+  'frame.php' )
	# paths.append( _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'php'  +os.sep+  'socket.php' )
	# paths.append( _v.myHome  +os.sep+  'projects'  +os.sep+  'pip' )
	filename_replace = {
							'101-auto-setup.sh': 'tool.sh',
							'installer.py': 'tool',
	}
	userA = 'ay7q2HGaNN6mSWaVZniaEw=='
	passwordA = 'Vpcgt45SYQBXyM7q3c8CfeP0x9fixit2Ar7NJT3b3B7n/x8vIFGNjQ=='

	userB = _blowfish.decrypt( userA, _vault.key() )
	passwordB = _blowfish.decrypt( passwordA, _vault.key() )

	userB = _str.cleanBE( userB, ' ' )
	passwordB = _str.cleanBE( passwordB, ' ' )

	# _.pr( userB )
	# _.pr( passwordB )
	# sys.exit()

	ftp = FTP()
	ftp.connect('107.180.54.171', 21)
	ftp.login(userB, passwordB)
	focus()

	for path in paths:
		if os.path.isfile(path):
			popper = __.path(path,file=True)
			if popper in filename_replace:
				popper = filename_replace[popper]
			if _.showLine(path) or _.showLine(popper) :

				file = _.getText( path, raw=True )
				# _.cp( [ 'CLEANED:', path ], 'cyan' )
				file = _.getText( path, raw=True )
				file = file.replace( chr(10), '\n' )
				file = file.replace( chr(27), '' )
				file = file.replace( '\r', '' )
				_.saveText( file, path, me=1 )


				# ii=0
				# while chr(10) in file or '\r' in file:
				#     ii+=1
				#     if ii == 100:
				#         break
				#     file = file.replace( chr(10), '\n' )
				#     file = file.replace( '\r', '' )
				#     # _.pr(ii)
				# _.saveText( file, path )

				

				_.updateLine( ['uploading', popper], 'darkcyan' )
				ftp.storbinary('STOR '+popper, open(path, 'rb'))
				_.updateLine( '' )
				_.cp(['uploaded',popper],'green')



	_.updateLine('')
	ftp.close()
	_.updateLine( 'connection closed', 'darkcyan', .5 )
	_.updateLine('')

	_beep.beep()


def md5_check(file):
	local  = _md5.md5File('D:\\websites\\tools.RightThumb\\tools\\'+file)
	remote = _.v.online.page('http://reph.us/tools/md5.php?file='+file)
	# _.pr('local',local)
	# _.pr('remote',remote)
	# _.pr( local, remote )
	if local == remote:
		_.cp( [ 'validation success', remote ], 'green' )
	else:
		_.pr( 'local:',local, 'remote:',remote )
		_.e( 'validation failure' )
def action():

	# md5_check('linux.zip')
	# sys.exit()
	# _.updateLine_disable = True

	_py3to2 = _.regImp( __.appReg, 'py3to2' )
	_py3to2.switch( 'Files', _v.drive  +os.sep+  'install'  +os.sep+  'py'  +os.sep+  'tool' )
	_py3to2.switch( 'Save', _v.widgets+os.sep+'widgets'  +os.sep+  'bash'  +os.sep+  'install'  +os.sep+  'py'  +os.sep+  'tool2' )
	_py3to2.action()

	# sys.exit()

	focus()
	if _.switches.isActive('SH'):
		ftp_upload_ssh()
		return None
	if _.switches.isActive('PrintPath'):
		_.pr( 'wget -o https://reph.us/tools/setup.sh | bash' )
		_.pr( '' )
		_.pr( '# or' )
		_.pr( 'wget https://reph.us/tools/linux.zip' )
		_.pr( 'wget https://reph.us/tools/databank.zip' )
		_.pr( '' )
		_.pr( 'unzip linux.zip -d linux' )
		_.pr( '' )
	else:
		_.updateLine( 'Uploading...', 'darkcyan' )
		ftp_upload()
	_.updateLine( '' )


import _rightThumb._encryptString as _blowfish
# import ftplib
from ftplib import FTP
import _rightThumb._vault as _vault
import _rightThumb._beep as _beep
import _rightThumb._md5 as _md5
_.v.online = _.ONLINE()



# FTP.maxline = 32558667

########################################################################################
if __name__ == '__main__':
	action()

# https://stackoverflow.com/questions/21998013/python-ftplib-show-ftp-upload-progress