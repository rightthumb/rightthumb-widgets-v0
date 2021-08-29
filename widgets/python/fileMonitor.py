#!/usr/bin/python3
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
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'fileMonitor.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Monitor files',
	'categories': [
						'file',
						'mon',
						'monitor',
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
						'p fileMonitor',
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

def on_created(event):
	print(f"hey, {event.src_path} has been created!")

def on_deleted(event):
	print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
	print(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
	print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

def action():
	patterns = "*"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)



	my_event_handler.on_created = on_created
	my_event_handler.on_deleted = on_deleted
	my_event_handler.on_modified = on_modified
	my_event_handler.on_moved = on_moved



	path = "."
	go_recursively = True
	my_observer = Observer()
	my_observer.schedule(my_event_handler, path, recursive=go_recursively)



	my_observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		my_observer.stop()
		my_observer.join()



from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

########################################################################################
if __name__ == '__main__':
	action()




