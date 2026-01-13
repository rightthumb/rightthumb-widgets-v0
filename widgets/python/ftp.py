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
	_.switches.register( 'Server', '-server' )
	_.switches.register( 'Upload', '-upload' )
	_.switches.register( 'Download', '-download' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name' )

	_.switches.register( 'Config', '-config' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ftp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage files on FTP server',
	'categories': [
						'ftp',
						'server',
						'manager',
						'config',
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
						'p ftp -file file.txt',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


"""

Google:
	python ftp upload to folder
	python ftp download file
	python ftp list folder contents


ToDo:
	make config file manager
	tool.js config
	
	possibly make multi technology app
		PHP json, etc

	possibly
				epyi servers
				epyi servers -files -file _ftp
				epyi servers -files -file _php_json
				epyi servers -files -file _php_files
				epyi servers -files -file _sftp
				epyi servers -files -file _.........

"""



class FTP_SRV(object):
	def __init__( self, server, username, password, folder=None ):
		self.ftp = FTP( server, username, password )
		if not folder is None:
			self.dir( folder )
	
	def dir( folder ):
		self.ftp.cwd( folder )

	def up( file, folder ):
		pass

	def down( file, folder ):
		pass

	def ls():
		pass

def action():
	pass
	# global data
	# load()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner(0)
	#     # _.printVar( _.appData )
	#     for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
	#         pass



# def load():
#     global data
#     data = _.getTable( 'table' )


# data = []



########################################################################################
if __name__ == '__main__':
	action()