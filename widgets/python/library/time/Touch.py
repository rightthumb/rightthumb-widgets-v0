
import os
import time
import re


class Touch:
	base_dir = os.path.normpath(os.path.expanduser(os.path.expandvars('~/.rt/Scheduled/touch')))
	durations = {
		's': 1, 'sec': 1, 'secs': 1, 'second': 1, 'seconds': 1,
		'n': 60, 'mn': 60, 'min': 60, 'mins': 60, 'minute': 60, 'minutes': 60,
		'h': 3600, 'hr': 3600, 'hrs': 3600, 'hour': 3600, 'hours': 3600,
		'd': 86400, 'day': 86400, 'days': 86400,
		'w': 604800, 'week': 604800, 'weeks': 604800,
		'm': 2592000, 'mo': 2592000, 'month': 2592000, 'months': 2592000,
		'y': 31536000, 'yr': 31536000, 'yrs': 31536000, 'year': 31536000, 'years': 31536000,
	}

	@staticmethod
	def _get_path(name):
		os.makedirs(Touch.base_dir, exist_ok=True)
		return os.path.join(Touch.base_dir, f"{name}.touch")

	@staticmethod
	def touch(name):
		"""Create or update a touch file with current time."""
		path = Touch._get_path(name)
		with open(path, 'a'):
			os.utime(path, None)

	@staticmethod
	def read(name,path=None):
		"""Return last modified time as datetime, or None if missing."""
		from datetime import datetime, timedelta
		if path is None:
			path = Touch._get_path(name)
		if os.path.exists(path):
			ts = os.path.getmtime(path)
			return datetime.fromtimestamp(ts)
		return None

	@staticmethod
	def schedule(name, interval='3h'):
		"""Returns True if task is due to run based on interval."""
		from datetime import datetime, timedelta
		if os.path.isfile(name):
			path = name
			name = os.path.splitext(path)[0]
		name = name.replace(' ', '_')
		last = Touch.read(name, path)
		if last is None:
		
			Touch.touch(name)
			return True
		threshold = datetime.now() - timedelta(seconds=Touch.parse_duration(interval))
		if last < threshold:
			if path is None:
				Touch.touch(name)
			return True
		return False

	@staticmethod
	def parse_duration(s):
		"""Parses durations like '1d 3h' to total seconds."""
		s = s.lower().strip()
		total = 0
		matches = re.findall(r'([-+]?\d*\.?\d+)\s*([a-z]+)', s)
		for num, unit in matches:
			if unit in Touch.durations:
				total += float(num) * Touch.durations[unit]
		return int(total)



'''
_.Touch.touch('win_cron_3hr')

if _.Touch.schedule('backup', interval='3h'):
	print("Running backup task...")
	# Do your backup here
else:
	print("Skip — already ran recently.")


if _.Touch.schedule(path, interval='3h'):
	pass
'''

'''
Touch — lightweight filesystem-based scheduling and state tracking.

This class uses small ".touch" files to record when a task last ran.
The modification time of the touch file represents the last execution
time for a named task.

Touch files are stored in:
    ~/.rt/Scheduled/touch/<name>.touch

Core idea:
    Instead of a database or cron state, the filesystem timestamp
    becomes the execution memory.

Common Usage
------------

Run a task every interval:

    if Touch.schedule('backup', '6h'):
        run_backup()

Mark a task as completed:

    Touch.touch('backup')

Read last execution time:

    last = Touch.read('backup')


Durations
---------

Intervals support combined human-readable durations:

    '10s'
    '5min'
    '3h'
    '1d'
    '1w'
    '1d 3h 15min'

parse_duration() converts these into seconds.


File-Based Scheduling
---------------------

schedule() can accept a real file path instead of a task name.

This allows external files to act as triggers:

    if Touch.schedule('/tmp/cache_refresh.touch', '1h'):
        rebuild_cache()


Watching Edited Files (Unconventional Use)
------------------------------------------

Touch can also track when a naturally edited file should trigger
processing. The real file's modification time is compared with the
touch record.

Example:

    config = '/etc/app/config.json'

    file_time  = os.path.getmtime(config)
    touch_time = Touch.read(config)

    if touch_time is None or file_time > touch_time.timestamp():
        reload_config()
        Touch.touch(config)

This allows any editable file (config, rules, commands, etc.)
to act as a trigger source.


Common Automation Patterns
--------------------------

• cron replacement inside long-running scripts
• rate limiting expensive operations
• polling APIs safely
• detecting external configuration changes
• coordinating jobs between scripts
• persistent timers that survive program restarts
• file-trigger automation (edit file → run action)


Advantages
----------

• no database required
• human-readable state files
• works across scripts and processes
• survives restarts
• extremely lightweight
'''