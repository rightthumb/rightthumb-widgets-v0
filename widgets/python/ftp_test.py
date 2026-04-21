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


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ftp_test.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'sftp',
	'categories': [
						'sftp',
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
						'p thisApp -file file.txt',
						''
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


from stat import S_ISDIR, S_ISREG



import paramiko


def getFolder( sftp, folder ):
	global user
	global total
	total['folders']+=1
	folder = folder.replace( '//', '/' )
	if folder.endswith('/'):
		folder = folder[:-1]
	sftp.chdir(folder)
	# _.pr( folder )
	items = sftp.listdir()
	folders = []
	for item in items:
		try:
			for entry in sftp.listdir_attr(item):
				mode = entry.st_mode
				if S_ISDIR(mode):
					if not folder+'/'+item in folders:
						folders.append( folder+'/'+item )

				elif S_ISREG(mode):
					total['files']+=1
					mod = sftp.stat(item).st_mtime
					_.pr(mod, '\t', folder+'/'+entry.filename)
		except Exception as e:
			pass
	for fld in folders:
		try:
			getFolder( sftp, fld )
		except Exception as e:
			pass



def action():
	global user
	global total
	load()
	# _.pr( _vault.imp.string('MVHip09oQqVQhbm9Fq8y8Q==') )
	# sys.exit()
	# https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	ssh.connect(
					hostname=      _vault.imp.string('oqrlNoR9SmPR9kXZZGJYYVPPMm3ySUwN'),
					username=      user,
					password=      _vault.imp.string(_v.config().cloud.ssh.password)
				)
	# _.pr( ssh.exec_command('pwd') )
	# stdin, stdout, stderr = ssh.exec_command(“sudo ls”)
	# stdin.write(‘mypassword\n’)
	# print stdout.readlines()

	sftp=ssh.open_sftp()
	# home = sftp.getcwd()
	# _.pr( home )
	sftp.chdir('/')
	# sftp.chdir('home')

	s = time.time()




	try:
		sftp.chdir(cloud_base)  # Test if remote_path exists
	except IOError:
		sftp.mkdir(cloud_base)  # Create remote_path

	getFolder( sftp, cloud_base )
	# getFolder( sftp, '/home/'+user+'/public_html' )
	_.pr(  )
	_.pr( time.time()-s )
	_.pr(total)
	# getFolder( sftp, '/home/ximlickficfp/public_html/tools.rightthumb.com' )
	_.pr()
	_.pr()
	_.pr()
	# getFolder( sftp, '/home/ximlickficfp/public_html/tools.rightthumb.com/crypt' )
	# sftp.chdir('/home/ximlickficfp/public_html/tools.rightthumb.com/crypt')
	# sftp.chdir('')
	# files = sftp.listdir()
	# for x in files:
	#     _.pr( x )

	# mod = sftp.stat( '{43E97BB4-EEB6-43A7-8A20-61A8123C17C1}.crypt' ).st_mtime
	# _.pr( mod )


	# try:
	#     sftp.chdir(remote_path)  # Test if remote_path exists
	# except IOError:
	#     sftp.mkdir(remote_path)  # Create remote_path


	sftp.close()
	ssh.close()


	# sftp.stat(PATH_TO_REMOTE_FILE).st_mtime

	# sftp.get(‘remotefileth’,’localfilepath’)

	# sftp=ssh.open_sftp()
	# sftp.put(‘localfilepath’,remotefilepath’)
	# sftp.close()

def load():
	global user
	global cloud
	user ='ximlickficfp'
	global total
	total = { 'files': 0, 'folders': 0 }

	cloud = {
				'base': '/home/'+user+'/cloud',
				'config': '/home/'+user+'/cloud/config',
				'files': '/home/'+user+'/cloud/files',
				'tech': '/home/'+user+'/cloud/files/tech',
				'programs': '/home/'+user+'/cloud/files/tech/programs',
				'web': '/home/'+user+'/public_html',
	}
	_v.programs
	_v.techFolder

user = None
total = None
cloud = {}

_vault = _.regImp( __.appReg, '_rightThumb._vault' )
########################################################################################
if __name__ == '__main__':
	action()