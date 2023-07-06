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
	### EXAMPLE: START
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob', description='Files' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Text', '-text' )
	_.switches.register( 'Read', '-r,-read' )
	_.switches.register( 'NoPrint', '--c' )
	_.switches.register( 'Innocent', '-innocent' )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	# 'app': '7facG-jo0Cxk',
	'file': 'steg.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Steganography app',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'steg',
						'steno',
						'stegano',
						'steganography',
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
						_.hp('p thisApp -file file.txt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
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
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START


def read(path,password=None):
	hidden=None
	unhider=unistego.get_unhider(open(path, 'rt'), 'joiners')
	with unhider:
		unhider.read()
	hidden=unhider.get_message().decode('utf-8')
	if not password is None:
		hidden=_blowfish.decrypt( hidden, _hash.string(password) )
	if not _.switches.isActive('NoPrint'):
		_.cp( hidden, 'green' )
	try:
		pass
	except Exception as e:
		_.e(e)
	return hidden


def write(path,hidden,password=None):
	_.pr(path,hidden,password)
	if not password is None:
		hidden = _blowfish.encrypt( hidden, _hash.string(password) )


	# carrier_text=open(path, 'rt')
	carrier_text=open(path, 'rt')
	# hider=unistego.get_hider(open(path+'.h', 'wt'), hidden, 'joiners')
	hider=unistego.get_hider(open(path+'.h', 'wt'), hidden, 'spaces')
	
	with carrier_text, hider:
		hider.write(carrier_text.read())
	# read(path,password)
	# try:
	#     return True
	# except Exception as e:
	#     return False
	#     _.e(e)

def process(path):

	password=None
	hidden=None

	if _.switches.isActive('Text'):
		if _.switches.value('Text'):
			hidden=' '.join(_.switches.values('Text'))
		else:
			hidden=input('Text: ')

	if _.switches.isActive('Password'):
		if _.switches.value('Password'):
			password=_.switches.values('Password')[0]
		else:
			password=getpass.getpass()

	if _.switches.isActive('Read'):
		read(path,password)
		try:
			pass
		except Exception as e:
			_.e( e )
		return None
	
	write(path,hidden,password)




def action( path=None, hidden=None, password=None ):
	if 0:
		pass
	elif not path is None and not hidden is None and not password is None:
		return write(path,hidden,password)
	elif not path is None and not hidden is None and password is None:
		return write(path,hidden)
	elif not path is None and hidden is None and password is None:
		return read(path)
		

	if path is None:
		for i,path in enumerate( _.isData(r=1) ):
			process(path)


import unistego
# _vault = _.regImp( __.appReg, '_rightThumb._vault' )
import _rightThumb._encryptString as _blowfish

import _rightThumb._md5 as _hash
import getpass

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






