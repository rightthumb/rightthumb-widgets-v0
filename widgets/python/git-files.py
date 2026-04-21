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

import _rightThumb._dir as _dir

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
##################################################


def appSwitches():
	# _.switches.register( 'Project', '-p,-project' )
	_.switches.register( 'Add-File-Or-Folder', '-f' )
	_.switches.register( 'Project-Scan', '-p,-project,-ps,-pscan,-project.scan' )
	_.switches.register( 'Add-File', '-add' )
	_.switches.register( 'Remove-File', '-rm' )
	_.switches.register( 'Add-EXT', '-add.ext' )
	_.switches.register( 'Remove-EXT', '-rm.ext' )
	_.switches.register( 'Add-Folder', '-add.folder' )
	_.switches.register( 'Remove-Folder', '-rm.folder' )
	_.switches.register( 'Folder-Recursive', '-r,-recursive' )
	_.switches.register( 'Folder-All', '-all' )
	_.switches.register( 'Show-Settings', '-settings' )
	_.switches.register( 'Scan-then-List-All-Files', '-scan,-files' )
	_.switches.register( 'Listen', '-listen' )


_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.isRequired_or_List = ['Add','Remove','Listen']

_.appInfo[focus()] = {
	'file': 'git-files.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage git project files or LIVE monitor changes',
	'categories': [
						'git',
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
						'cd D:\\.rightthumb-widgets',
						'    p git-files -project widgets ',
						'',
						'p git-files -add hotkeys-Text.dex',
						'p git-files -rm keychain.hash',
						'p git-files -listen',
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
	_.pr(f"hey, {event.src_path} has been created!")

def on_deleted(event):
	_.pr(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
	_.pr(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
	_.pr(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")


# _dir.info(path)


def listen():
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



def add_file(path):
	global settings
	if not os.path.isfile(path):
		project_error(path)

	git = scan_project(path,err=True)




def rm_file(path):
	git = scan_project(path,err=True)
def add_ext(subject):
	git = scan_project(os.getcwd(),err=True)
def rm_ext(subject):
	git = scan_project(os.getcwd(),err=True)

def add_folder(path):
	git = scan_project(path,err=True)
	# if _.switches.isActive('Folder-Recursive'):
	# if _.switches.isActive('Show-Settings'):
	# if _.switches.isActive('Folder-All'):
	# if _.switches.isActive('Remove-File'):
	# if _.switches.isActive('Add-EXT'):
	# if _.switches.isActive('Remove-EXT'):
def rm_folder(path):
	git = scan_project(path,err=True)

def show_settings():
	git = scan_project(os.getcwd(),err=True)

def scan_files():
	git = scan_project(os.getcwd(),err=True)

def git_project( path ):
	for line in _.getText(path):
		line = line.replace(' ','')
		if 'url=' in line:
			subject = line.split('url=')[1].replace('\n','').replace('\r','')
			git = {
						'account': subject.split('/')[ len(subject.split('/'))-2 ],
						'project': subject.split('/')[ len(subject.split('/'))-1 ].replace('.git',''),
						'path': __.path( path, pop=2 ),
			}
			_.pv(git)
			git_check(git)
			# _.v.git = _.dot()
			# _.v.git.account = git['account']
			# _.v.git.project = git['project']
			return git


def scan_project(path,err=False):
	path = __.path(path)

	if os.path.isfile(path):
		path = __.path( path, pop=True )

	try:
		loop=0
		while True:
			loop+=1
			if loop > 1000:
				if err:
					project_error()
				return None
			test = path +os.sep+ '.git' +os.sep+ 'config'
			if os.path.isfile(test):
				return git_project( test )
				break
			path = __.path( path, pop=True )
	except Exception as e:
		_.e(e)

def project_test_return(git):
	if git is None:
		project_error()
	else:
		return git




def project_error(path=None):
	global settings
	text = '\n'
	if not path is None:
		text = '\n'
		if type(path) == list:
			text += '             : '+ '\n             : '.join(path)
		else:
			text += '             : '+path
		_.e( 'path does not exist', text )
	if not settings:
		text += 'no git projects have been configured'


	if settings:
		for account in children(settings):
			text += '\n'
			text += account+'\n'
			for proj in children(settings[account]):
				text += '\t'+proj+'   '+settings[account][proj]['path']+'\n'
			text += '\n'
	_.e( 'project not found', text )

def children(table):
	result = []
	for k in table:
		result.append(k)
	return result


def print_project(git):
	_.pv(  project_test_return(git)  )

def git_check(git):
	global settings
	added = False
	if not git['account'] in settings:
		added = True
		settings[git['account']] = {}
	if not git['project'] in settings[git['account']]:
		added = True
		settings[git['account']][git['project']] = {
														'path': git['path'],
														'ext': {},
														'files': {},
														'folders': {
															'single': {},
															'recursive': {},
														},
													}
	if added:
		save()


def save():
	global settings
	_.saveTableDB( settings, _.v.settings )
	_.cp( 'saved', 'green' )



def action():
	load()
	if _.switches.isActive('Add-File-Or-Folder'):
		files = []
		folders = []
		err = []
		for path in _.switches.values('Add-File-Or-Folder'):
			if os.path.isfile(path):
				files.append(path)
			elif os.path.isdir(path):
				folders.append(path)
			else:
				err.append(path)
		pass
		if err:
			project_error(err)
		if folders:
			_.switches.fieldSet( 'Add-Folder', 'active', True )
			_.switches.fieldSet( 'Add-Folder', 'values', folders )
			_.switches.fieldSet( 'Add-Folder', 'value', ','.join(folders) )
		if files:
			_.switches.fieldSet( 'Add-File', 'active', True )
			_.switches.fieldSet( 'Add-File', 'values', files )
			_.switches.fieldSet( 'Add-File', 'value', ','.join(files) )

	if _.switches.isActive('Listen'):
		listen()
	elif _.switches.isActive('Add-Folder'):
		for path in _.switches.values('Add-Folder'):
			add_folder(  __.path(path)  )
	elif _.switches.isActive('Remove-Folder'):
		for path in _.switches.values('Remove-Folder'):
			rm_folder(  __.path(path)  )
	elif _.switches.isActive('Add-File'):
		for path in _.switches.values('Add-File'):
			add_file(  __.path(path)  )
	elif _.switches.isActive('Remove-File'):
		for path in _.switches.values('Remove-File'):
			rm_file(  __.path(path)  )
	elif _.switches.isActive('Add-EXT'):
		for ext in _.switches.values('Add-EXT'):
			add_ext(  ext  )
	elif _.switches.isActive('Remove-EXT'):
		for ext in _.switches.values('Remove-EXT'):
			rm_ext(  ext  )
	elif _.switches.isActive('Show-Settings'):
		list()
	elif _.switches.isActive('Scan-then-List-All-Files'):
		show_settings()
	elif _.switches.isActive('Project-Scan'):
		if len(_.switches.value('Project-Scan')):
			for path in _.switches.values('Project-Scan'):
				print_project(  scan_project(  __.path(path), err=True  )  )
		else:
			print_project(  scan_project( os.getcwd(), err=True )  )



def load():
	global settings
	_.v.settings = 'git-projects.settings'
	settings = _.getTableDB( _.v.settings )

	{
		'ACCOUNT': {
			'PROJECT': {
				'ext': {
					'EXT': 1,
				},
				'files': {
					'PATH': 1,
				},
				'folders': {

					'single': {
						'SANITARY-PATH': {
							'status': 1,
							'force-all-ext': 0,
						}
					},
					'recursive': {},

				},
			}
		}
	}


# _.saveTableDB( settings, _.v.settings )


########################################################################################
if __name__ == '__main__':
	action()