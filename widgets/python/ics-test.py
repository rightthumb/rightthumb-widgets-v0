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
	# _.switches.register( 'Input', '-i' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
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



def action():
	pass 

#!/usr/bin/env python3

import os.path
from ics import Calendar, Event
import simplejson as json
import sys
import os
import io

taskwarrior_formatted_data_location = _.switches.values('Files')[0]
ics_calendar_full_path = "tasks.ics"
ics_calendar_full_path_chores = "chores.ics"
ics_calendar_full_path_announcements = "announcements.ics"
unique_list_of_calendar_tasks = []

valid_statuses_for_calendar = ['pending', 'waiting']
invalid_statuses_for_calendar = ['completed', 'deleted']


def create_uniqueness(task):
	""" creates a definition of uniqueness from a task's attributes
	input: task: an object with a Taskwarrior set of attributes
	output: a string of the unique signature of this task """

	if not task:
		return None

	if task.get('due') and task.get('description'):
		return task['due'] + task['description']
	else:
		return task['uuid']


def is_unique_calendar_task(task):
	""" if this task exists in the list of tasks to make a calendar already
	input: task: an object with a Taskwarrior set of attributes
	output: boolean - true if the task is unique, false if it already existed in the list """

	if not task:
		return None
	if task['status'] in invalid_statuses_for_calendar:
		return False

	if task.get('status') and task['status'] in valid_statuses_for_calendar:
		unique_task_id = create_uniqueness(task)
		if unique_task_id in unique_list_of_calendar_tasks:
			return False
		unique_list_of_calendar_tasks.append(unique_task_id)
		return True
	return False


def create_task_calendar_description(task):
	""" creates a custom description of the task for the calendar summary
	input: task: an object with a Taskwarrior set of attributes
	output: string to be used for the calendar event summary """
	project = "{} {} {}".format("[", task['project'], "] ") if task.get('project') else ""
	tags = " [" + ", ".join([k for k in task['tags'] if 'cal.' not in k]) + "]" if (task.get('tags') and [k for k in
		task['tags'] if 'cal.' not in k]) else ""
	return project + task['description'] + tags


def get_task_first_calendar(task):
	""" find the first cal.<xyz> tag, which indicates which calendar this task should appear on. Defaults to the
	general calendar
	input: task: an object with a Taskwarrior set of attributes
	output: string with the name of the calendar this event should go on """
	if task.get('tags') is None:
		return ""
	cals = [s for s in task['tags'] if 'cal.' in s]
	if not cals:
		return ""
	return cals[0].replace("cal.", "")


def get_unique_task():
	""" read the JSON-like file, filtering out lines I don't need, and calling the unique function to create tasks to
	be processed
	input: none
	output: yields a unique task """
	real_lines = []
	for line in io.open(taskwarrior_formatted_data_location, 'r', encoding='utf8'):
		li = line.strip()
		if li.startswith("{"):
			real_lines.append(li)

	lines_as_string = "[" + ",".join(real_lines) + "]"
	for task in json.loads(lines_as_string):
		if is_unique_calendar_task(task):
			yield task


def get_task_start_date_for_event(task):
	""" find the calendar event start date based on a hierarchy of which date to use
	input: task: an object with a Taskwarrior set of attributes
	output: date to use in Taskwarrior format """
	if task is None:
		return ""
	if task.get('due'):
		return task['due']
	if task.get('scheduled'):
		return task['scheduled']
	if task.get('wait'):
		return task['wait']
	else:
		return ""


if __name__ == "__main__":
	general_cal = Calendar(creator="My TaskWarrior Calendar")
	chores_cal = Calendar(creator="My TaskWarrior Chores Calendar")
	ann_cal = Calendar(creator="My TaskWarrior Announcements Calendar")
	for task in get_unique_task():

		event_due = get_task_start_date_for_event(task)
		if event_due in (None, ""):
			continue
		cal_event = Event()
		cal_event.begin = event_due
		cal_event.name = create_task_calendar_description(task)


		task_first_calendar = get_task_first_calendar(task)
		if task_first_calendar == "":
			general_cal.events.append(cal_event)
		if task_first_calendar == "chores":
			chores_cal.events.append(cal_event)
		if task_first_calendar == "announcements":
			ann_cal.events.append(cal_event)


	with open(os.path.expanduser(ics_calendar_full_path), 'w') as f:
		f.writelines(general_cal)

	with open(os.path.expanduser(ics_calendar_full_path_chores), 'w') as f:
		f.writelines(chores_cal)

	with open(os.path.expanduser(ics_calendar_full_path_announcements), 'w') as f:
		f.writelines(ann_cal)

	sys.exit(0)


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()