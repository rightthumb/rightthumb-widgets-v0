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
from datetime import datetime

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
import _rightThumb._dir as _dir

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

##################################################

def appSwitches():
	_.switches.register( 'Folders', '-f,-fo,-folder' )

_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False

_.appInfo[focus()] = {
	'file': 'fileMonitor.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Monitor files',
	'categories': [
		'file',
		'mon',
		'monitor',
	],
	'usage': [],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [
		'p fileMonitor',
		'',
	],
	'columns': [],
	'aliases': [],
	'notes': [],
}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
		'field': {'sent': [], 'received': [] },
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

def stamp(ts):
	try:
		return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	except Exception:
		return str(ts)

def on_created(event):
	if event.is_directory:
		_.pr(f"created, dir {event.src_path} has been created!")
	else:
		_.pr(f"created, {event.src_path} has been created!")

def on_deleted(event):
	if event.is_directory:
		_.pr(f"deleted dir {event.src_path}!")
	else:
		_.pr(f"deleted {event.src_path}!")

def on_modified(event):
	if event.is_directory:
		_.pr(f"modified dir, {event.src_path} has been modified")
	else:
		_.pr(f"modified, {event.src_path} has been modified")

def on_moved(event):
	if event.is_directory:
		_.pr(f"moved dir {event.src_path} to {event.dest_path}")
	else:
		_.pr(f"moved {event.src_path} to {event.dest_path}")

def action():
	patterns = "*"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True

	my_event_handler = PatternMatchingEventHandler(
		patterns=patterns,
		ignore_patterns=ignore_patterns,
		ignore_directories=ignore_directories,
		case_sensitive=case_sensitive
	)

	my_event_handler.on_created = on_created
	my_event_handler.on_deleted = on_deleted
	my_event_handler.on_modified = on_modified
	my_event_handler.on_moved = on_moved

	path = "."
	if _.switches.isActive('Folder'):
		path = __.path(_.switches.values('Folder')[0])

	go_recursively = True
	my_observer = Observer()
	my_observer.schedule(my_event_handler, path, recursive=go_recursively)

	# Track file access times
	access_times = {}

	def seed_access_times():
		for root, dirs, files in os.walk(path):
			for name in files:
				file_path = os.path.join(root, name)
				try:
					access_times[file_path] = os.stat(file_path).st_atime
				except Exception:
					pass

	def scan_access_times():
		current_files = set()

		for root, dirs, files in os.walk(path):
			for name in files:
				file_path = os.path.join(root, name)
				current_files.add(file_path)

				try:
					atime = os.stat(file_path).st_atime
				except Exception:
					continue

				if file_path not in access_times:
					access_times[file_path] = atime
					continue

				if atime != access_times[file_path]:
					access_times[file_path] = atime
					_.pr(f"accessed, {file_path} was accessed at {stamp(atime)}")

		# remove deleted files from tracking cache
		dead_files = set(access_times.keys()) - current_files
		for dead in dead_files:
			del access_times[dead]

	seed_access_times()

	my_observer.start()
	try:
		while True:
			scan_access_times()
			time.sleep(1)
	except KeyboardInterrupt:
		my_observer.stop()
		my_observer.join()

########################################################################################
if __name__ == '__main__':
	action()







































# #!/usr/bin/python3

# # ## {R2D2919B742E} ##
# # ###########################################################################
# # What if magic existed?
# # What if a place existed where your every thought and dream come to life.
# # There is only one catch: it has to be written down.
# # Such a place exists, it is called programming.
# #    - Scott Taylor Reph, RightThumb.com
# # ###########################################################################
# # ## {C3P0D40fAe8B} ##

# import os
# import sys
# import time
# # import platform
# ##################################################
# import _rightThumb._construct as __
# appDBA = __.clearFocus( __name__, __file__ )
# __.appReg = appDBA
# def focus( parentApp='', childApp='', reg=True ):
# 	global appDBA
# 	f = __.appName( appDBA, parentApp, childApp )
# 	if reg:
# 		__.appReg = f
# 	return f
# __.registeredApps.append( focus() )
# import _rightThumb._base3 as _
# _.load()
# ##################################################
# import _rightThumb._vars as _v
# import _rightThumb._string as _str

# ##################################################


# def appSwitches():
# 	_.switches.register( 'Folders', '-f,-fo,-folder' )


# _.autoBackupData = __.autoCreationConfiguration['backup']
# __.isRequired_Pipe = False
# __.isRequired_Pipe_or_File = False
# __.pre_error = False
# # __.isRequired_or_List = ['Pipe','Files','Plus']

# _.appInfo[focus()] = {
# 	'file': 'fileMonitor.py',
# 	'liveAppName': __.thisApp( __file__ ),
# 	'description': 'Monitor files',
# 	'categories': [
# 						'file',
# 						'mon',
# 						'monitor',
# 				],
# 	'usage': [
# 						# 'epy another',
# 						# 'e nmap',
# 						# '',
# 	],
# 	'relatedapps': [
# 						# 'p another -file file.txt',
# 						# '',
# 	],
# 	'prerequisite': [
# 						# 'p another -file file.txt',
# 						# '',
# 	],
# 	'examples': [
# 						'p fileMonitor',
# 						'',
# 	],
# 	'columns': [
# 					# { 'name': 'name', 'abbreviation': 'n' },
# 					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
# 	],
# 	'aliases': [
# 					# 'this',
# 					# 'app',
# 	],
# 	'notes': [
# 					# {},
# 	],
# }

# _.appData[focus()] = {
# 		'start': __.startTime,
# 		'uuid': '',
# 		'audit': [],
# 		'pipe': False,
# 		'data': {
# 					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
# 					'table': {'sent': [], 'received': [] }, 
# 		},
# 	}



# def registerSwitches( argvProcessForce=False ):
# 	global appDBA
# 	if not __.appReg == appDBA and appDBA in __.appReg:

# 		if not __name__ == '__main__':
# 			_.argvProcess = argvProcessForce
# 		else:
# 			_.argvProcess = True

# 		_.load()
# 		_.appInfo[__.appReg] = _.appInfo[appDBA]
# 		_.appData[__.appReg] = _.appData[appDBA]
# 	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
# 	appSwitches()

# 	_.myFileLocation_Print = False
# 	__.myFileLocations_SKIP_VALIDATION = False
# 	_.switches.trigger( 'Files', _.myFileLocations )
# 	_.switches.trigger( 'Folder', _.myFolderLocations )
# 	_.switches.trigger( 'URL', _.urlTrigger )
# 	_.switches.trigger( 'Ago', _.timeAgo )
# 	_.switches.trigger( 'Duration', _.timeFuture )
	
	
# 	_.defaultScriptTriggers()
# 	_.switches.process()


# if not __name__ == '__main__':
# 	_.argvProcess = False
# else:
# 	_.argvProcess = True

# registerSwitches()


# def fieldSet( switchName, switchField, switchValue, theFocus=False ):
# 	if not type( theFocus ) == bool:
# 		theFocus = theFocus
# 	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


# if __name__ == '__main__':
# 	if not sys.stdin.isatty():
# 		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


# _.postLoad( __file__ )

# ########################################################################################
# # START

# # def on_created(event):
# # 	_.pr(f"created, {event.src_path} has been created!")

# # def on_deleted(event):
# # 	_.pr(f"deleted {event.src_path}!")

# # def on_modified(event):
# # 	_.pr(f"modified, {event.src_path} has been modified")

# # def on_moved(event):
# # 	_.pr(f"moved {event.src_path} to {event.dest_path}")

# # def action():
# # 	patterns = "*"
# # 	ignore_patterns = ""
# # 	ignore_directories = False
# # 	case_sensitive = True
# # 	my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)



# # 	my_event_handler.on_created = on_created
# # 	my_event_handler.on_deleted = on_deleted
# # 	my_event_handler.on_modified = on_modified
# # 	my_event_handler.on_moved = on_moved

# # 	# for x in dir(my_event_handler): print('my_event_handler.',x)

# # 	path = "."
# # 	if _.switches.isActive('Folder'): path = __.path(_.switches.values('Folder')[0])


# # 	go_recursively = True
# # 	my_observer = Observer()
# # 	my_observer.schedule(my_event_handler, path, recursive=go_recursively)



# # 	my_observer.start()
# # 	try:
# # 		while True:
# # 			time.sleep(1)
# # 	except KeyboardInterrupt:
# # 		my_observer.stop()
# # 		my_observer.join()




# # import _rightThumb._dir as _dir
# # from watchdog.observers import Observer
# # from watchdog.events import PatternMatchingEventHandler





# import os
# import time
# from datetime import datetime

# import _rightThumb._dir as _dir
# from watchdog.observers import Observer
# from watchdog.events import PatternMatchingEventHandler

# def on_created(event):
# 	_.pr(f"created, {event.src_path} has been created!")

# def on_deleted(event):
# 	_.pr(f"deleted {event.src_path}!")

# def on_modified(event):
# 	_.pr(f"modified, {event.src_path} has been modified")

# def on_moved(event):
# 	_.pr(f"moved {event.src_path} to {event.dest_path}")

# def action():
# 	patterns = "*"
# 	ignore_patterns = ""
# 	ignore_directories = False
# 	case_sensitive = True
# 	my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

# 	my_event_handler.on_created = on_created
# 	my_event_handler.on_deleted = on_deleted
# 	my_event_handler.on_modified = on_modified
# 	my_event_handler.on_moved = on_moved

# 	path = "."
# 	if _.switches.isActive('Folder'):
# 		path = __.path(_.switches.values('Folder')[0])

# 	go_recursively = True
# 	my_observer = Observer()
# 	my_observer.schedule(my_event_handler, path, recursive=go_recursively)

# 	# --- Track access times ---
# 	access_times = {}

# 	def scan_access_times():
# 		for root, _, files in os.walk(path):
# 			for name in files:
# 				file_path = os.path.join(root, name)
# 				try:
# 					stat = os.stat(file_path)
# 					atime = stat.st_atime
# 					if file_path in access_times:
# 						if atime != access_times[file_path]:
# 							access_times[file_path] = atime
# 							_.pr(f"accessed, {file_path} was accessed at {datetime.fromtimestamp(atime)}")
# 					else:
# 						access_times[file_path] = atime
# 				except Exception:
# 					pass

# 	my_observer.start()
# 	try:
# 		while True:
# 			scan_access_times()
# 			time.sleep(1)
# 	except KeyboardInterrupt:
# 		my_observer.stop()
# 		my_observer.join()














































# ########################################################################################
# if __name__ == '__main__':
# 	action()