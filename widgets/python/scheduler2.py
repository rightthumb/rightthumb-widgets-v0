import sys
import time
import json
import os
from datetime import datetime, timedelta
import _rightThumb._construct as __
appDBA = __.clearFocus(__name__, __file__)
__.appReg = appDBA

def focus(parentApp='', childApp='', reg=True):
    global appDBA
    f = __.appName(appDBA, parentApp, childApp)
    if reg:
        __.appReg = f
    return f

import _rightThumb._base3 as _
fieldSet = _.l.vars(focus(), __name__, __file__, appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
    pass
    _.switches.register('NoBeep', '-nobeep')
    _.switches.register('List', '-list')
    _.switches.register('DaysOfWeek', '-dow,-day,-days', 'mon tue wed thu fri sat sun')
    _.switches.register('Delete', '-del')
    _.switches.register('Every', '-e,-every', 'day hour min sec OR d h m s')
    _.switches.register('Python', '-py', 'autoBackup')
    _.switches.register('Arguments', '-args', '-ago 1d (USE THIS SWITCH LAST)')
    _.switches.register('At', '-at', 'Specify a specific time in HH:MM format')
    _.switches.register('Monthly', '-monthly', 'Run the task on a specific day of the month (e.g., -monthly 15)')
    _.switches.register('Weekly', '-weekly', 'Run the task on specific days of the week (e.g., -weekly Mon Wed Fri)')

__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation', False)
__.setting('require-pipe', False)
__.setting('require-pipe||file', False)
__.setting('pre-error', False)
__.setting('switch-raw', [])

_.appInfo[focus()] = {
    'file': 'scheduler.py',
    'liveAppName': __.thisApp(__file__),
    'description': 'Added to always running hotkeys.py to schedule tasks',
    'categories': [
        'scheduler',
    ],
    'usage': [],
    'relatedapps': [],
    'prerequisite': [],
    'examples': [
        _.hp('p scheduler -py ephemeral--job-test -e m 2'),
        _.linePrint(label='simple', p=0),
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
        'field': {'sent': [], 'received': []},
        'table': {'sent': [], 'received': []},
    },
}

def triggers():
    _.switches.trigger('Files', _.myFileLocations, vs=True)
    _.switches.trigger('Ago', _.timeAgo)
    _.switches.trigger('Folder', _.myFolderLocations)
    _.switches.trigger('URL', _.urlTrigger)
    _.switches.trigger('Duration', _.timeFuture)

def _local_(do):
    exec(do)

_.l.conf('clean-pipe', True)
_.l.sw.register(triggers, sw)

# Scheduler JSON file path
SCHEDULER_FILE = 'scheduler.json'

# Load or create the scheduler database
def load_scheduler():
    if os.path.exists(SCHEDULER_FILE):
        with open(SCHEDULER_FILE, 'r') as f:
            return json.load(f)
    return []

# Save the scheduler database
def save_scheduler(db):
    with open(SCHEDULER_FILE, 'w') as f:
        json.dump(db, f, indent=4)

# Add a new task to the scheduler
def add_task(command, frequency, at_time=None, days_of_week=None):
    task = {
        'id': str(len(db) + 1),
        'command': command,
        'frequency': frequency,
        'at_time': at_time,
        'days_of_week': days_of_week,
        'next_run': calculate_next_run(frequency, at_time, days_of_week),
    }
    db.append(task)
    save_scheduler(db)
    print(f"Task '{command}' added successfully!")

# Calculate the next run time for a task
def calculate_next_run(frequency, at_time=None, days_of_week=None):
    now = datetime.now()
    if frequency == 'daily':
        next_run = now + timedelta(days=1)
    elif frequency == 'weekly':
        next_run = now + timedelta(weeks=1)
    elif frequency == 'monthly':
        next_run = now + timedelta(weeks=4)
    else:
        raise ValueError("Invalid frequency")

    if at_time:
        next_run = next_run.replace(hour=int(at_time.split(':')[0]), minute=int(at_time.split(':')[1]))

    if days_of_week:
        while next_run.strftime('%a').lower() not in [d.lower() for d in days_of_week]:
            next_run += timedelta(days=1)

    return next_run

# List all scheduled tasks
def list_tasks():
    print("Scheduled Tasks:")
    for task in db:
        print(f"ID: {task['id']}")
        print(f"Command: {task['command']}")
        print(f"Frequency: {task['frequency']}")
        print(f"Next Run: {task['next_run']}")
        if task['days_of_week']:
            print(f"Days of Week: {', '.join(task['days_of_week'])}")
        if task['at_time']:
            print(f"At Time: {task['at_time']}")
        print("-" * 20)

# Delete a task by ID
def delete_task(task_id):
    global db
    db = [task for task in db if task['id'] != task_id]
    save_scheduler(db)
    print(f"Task with ID {task_id} deleted.")

# Run due tasks
def run_due_tasks():
    now = datetime.now()
    for task in db:
        next_run = datetime.strptime(task['next_run'], '%Y-%m-%d %H:%M:%S.%f')
        if next_run <= now:
            os.system(task['command'])
            task['next_run'] = calculate_next_run(task['frequency'], task['at_time'], task['days_of_week'])
    save_scheduler(db)

# Display help menu
def display_help():
    print("Scheduler Application Help")
    print("Usage:")
    print("  -py <script_name> [arguments]   Runs a Python script with optional arguments.")
    print("  -list                            Lists all scheduled tasks.")
    print("  -del <task_id>                   Deletes a task by its ID.")
    print("  -run                             Runs all due tasks.")
    print("  -every <unit> <value>            Specifies the interval (day, hour, min, sec).")
    print("  -at <time>                       Specifies a specific time in HH:MM format.")
    print("  -dow <days>                      Specifies days of the week (Mon, Tue, etc.).")
    print("  -monthly <day>                   Run the task on a specific day of the month.")
    print("  -weekly <days>                   Run the task on specific days of the week.")
    print("Examples:")
    print("  p scheduler -py backup_script.py -e daily")
    print("  p scheduler -py update.py -at 14:30 -dow Mon Wed Fri")

if __name__ == '__main__':
    db = load_scheduler()

    if len(sys.argv) > 1:
        if sys.argv[1] == '-py':
            command = sys.argv[2]
            args = sys.argv[3:]
            os.system(f"python {command} {' '.join(args)}")
        elif sys.argv[1] == '-list':
            list_tasks()
        elif sys.argv[1] == '-del':
            delete_task(sys.argv[2])
        elif sys.argv[1] == '-run':
            run_due_tasks()
        else:
            display_help()
    else:
        display_help()
