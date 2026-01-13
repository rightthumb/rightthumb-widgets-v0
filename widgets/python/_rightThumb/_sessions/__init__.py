import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
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
						'p thisApp -file file.txt',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START









import subprocess

class Sessions:
	def __init__( self ):
		self.session = _v.session()
		self.folder_waiting = _v.programs + _v.slash+'sessions\\waiting'+_v.slash
		self.format = 'Session-0.hash'
		self.broadcast = self.folder_waiting + self.format.replace( '0', self.session )
		self.active = None


	def wait( self ):
		self.activate()
		while self.active is None:
			self.active = _.getTable2( self.broadcast )
			# _.pr('self.active',self.active)
			if self.active['request'] is None:
				self.active = None
			time.sleep(1)
		# _.pr( 'HERE' )
		for do in self.active['request']:
			try:
				os.system(do)
			except Exception as e:
				_.colorThis( [ 'Error:', do ] )
		self.deactivate()



	def activate( self ):
		_.saveTable2( {'busy': False, 'request': None,'result':None}, self.broadcast )

	def deactivate( self ):
		if os.path.isfile( self.broadcast ):
			os.remove(self.broadcast)

	def request( self, request ):
		self.request_count = 0
		result = self.requestLoop( request)
		if result is None:
			_.colorThis( [ 'Error: timout' ], 'red' )
			sys.exit()
	def requestLoop( self, request ):
		l = 10
		s = 1
		t = 5
		self.request_count+=1
		if self.request_count > t:
			return None
		self.scan(request)
		if self.active is None:
			self.openTerminal()
		i=0
		while self.active is None and i < l:
			# _.pr( 'requestLoop', i )
			self.scan(request)
			time.sleep(s)
			i+=1
		if self.active is None:
			return self.requestLoop( request )
		return self.active
	def scan( self, request ):
		if self.active is None:
			folder = self.folder_waiting
			dirList = os.listdir(folder)
			for item in dirList:
				if self.active is None:
					path = folder+item
					valid = True
					ticket = item
					for x in self.format.split('0'):
						ticket = ticket.replace( x, '' )
						if not x in item:
							valid = False
					# if not valid:
					#     _.pr( 'invalid' )
					if valid:
						# _.pr( 'valid' )
						status = _.getTable2( path )
						if not status['busy']:
							_.saveTable2( {'busy': True, 'request': request}, path )
							self.active = { 'session': ticket, 'path': path }
							return self.active
					

		# _.pr('End Scan')
		return self.active



	def openTerminal( self ):

		import _rightThumb._simpleThreads as _threads

		
		_threads.manager.register(
			name = 'New Terminal',
			fn = self.terminal,
			timeout = None
		)

	def terminal( self ):
		subprocess.call( '"'+_v.userprofile+_v.slash+'newSession.bat"', creationflags=subprocess.CREATE_NEW_CONSOLE)

		# subprocess.call('python bb.py', creationflags=subprocess.CREATE_NEW_CONSOLE)




def action():
	pass


########################################################################################
if __name__ == '__main__':
	action()






