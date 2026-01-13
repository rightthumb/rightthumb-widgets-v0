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


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'unclaimed_tickets.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Sync unclaimed_tickets on terminal close',
	'categories': [
						'close',
						'terminal exit',
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
						'p unclaimed_tickets',
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

# from shutil import copyfile

def action():
	a = _v.stmp +os.sep+ 'unclaimed_tickets'
	b = _v.stmp +os.sep+ 'unclaimed_tickets_history'
	# _.pr(folder)
	
	for i,folder in enumerate([a,b]):
		for file in os.listdir(folder):
			# _.pr(file)
			if file.startswith('closed') or file.startswith('open'):
				pre = ''
				if file.startswith('closed'):
					pre = 'closed'
					alt = file.replace('closed','open')
				else:
					pre = 'open'
					alt = file.replace('open','closed')
				path = folder +os.sep+ file

				# _.pr(file)
				session = file.replace(pre+'-','').replace('.txt','')
				path2 = folder+_v.slash+'history-'+session+'.txt'
				if os.path.isfile(path):
					# _.pr(path)
					myTicket = _v.myTickets +os.sep+ file
					if not os.path.isfile(myTicket) and not os.path.isfile(_v.myTickets + os.sep + alt):
						_.colorThis( [ 'reclaiming ticket for session: ', session ], 'cyan' )
						newFile = []
						for line in _.getText( path, raw=True ).split('\n'):
							if not 'being used by another process' in line:
								newFile.append(line)
						_.saveText( newFile, myTicket )
						try:
							_bk
						except:
							_bk = _.regImp( __.appReg, 'fileBackup' )
							_bk.switch( 'Silent' )
							_bk.switch( 'BypassScheduler' )
						# for x in dir(_bk): print(x)
						# sys.exit()
						# _bk[path].switch( 'Input', path )
						# _bk[path].switch( 'Output', path2 )
						if os.path.isfile(myTicket):
							bkfi = _bk.action(myTicket)
						# _.pr(bkfi)
						# time.sleep(.2)
						os.unlink(path)
						if os.path.isfile(path2):
							os.unlink(path2)
# _bk = _.regImp( __.appReg, 'fileBackup' )
# _bk.switch( 'Silent' )
# _bk.switch( 'BypassScheduler' )
########################################################################################
if __name__ == '__main__':
	action()







