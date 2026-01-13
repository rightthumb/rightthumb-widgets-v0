import os, sys, time
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
	_.switches.register( 'Database', '-db', 'index.db' )
	_.switches.register( 'PrintMemory', '-printMem' )
	_.switches.register( 'Commit', '-commit', '1000' )
	_.switches.register( 'MemoryBufferMB', '-mem', '10' )
	_.switches.register( 'Test', '-test' )
	pass
__.setting('receipt-log',True)
__.setting('receipt-file',True)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	'file': 'indexDB-files.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Index files and there contents',
	'categories': [
						'index',
						'contents',
						'websites',
						'database',
						'sqlite',
						'index.db',
				],
	'usage': [
						'dex.',
	],
	'relatedapps': [
						'dex.',
						'dex',
						'search-indexDB-files',
	],
	'prerequisite': [
	],
	'examples': [
						_.hp('p indexDB-files'),
						_.hp('p indexDB-files -db /opt/home_index.db'),
						_.linePrint(label='simple',p=0),
						_.hp('pip3 install python-magic'),
						'',
	],
	'columns': [
	],
	'aliases': [
	],
	'notes': [
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

def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import sqlite3
import os

def is_binary_file(file_path):
	try:
		with open(file_path, 'rb') as file:
			chunk = file.read(1024)
			if b'\0' in chunk:  # Null byte indicates binary
				return True
			return False
	except:
		return True  # Assume binary if the file cannot be read


def is_text(filename):
	try:
		with open(filename, 'rb') as check_file:
			# Read a small chunk to check if it's text
			chunk = check_file.read(1024)
			if b'\0' in chunk:
				return False
			# Check for non-printable characters
			if any(b < 32 or b > 126 for b in chunk):
				return False
			return True
	except:
		return False


def get_content(filename):
	global report
	try:
		with open(filename, 'r') as read_file:
			content = read_file.read()
			report['indexed'] += 1
			report['size'] += len(content)
			return content
	except:
		return ""
cnt = 0

def isLink(path):
	if os.path.islink(path): return True
	try: return os.stat(path).st_nlink > 1
	except: return False

import platform
import psutil
def get_memory_available():
	if platform.system() == 'Linux':
		mem = psutil.virtual_memory()
		return mem.available
	else:
		return None
def calculate_max_size(buffer_mb=10):
	if not platform.system() == 'Linux': return None
	available_memory = get_memory_available()
	if available_memory is not None:
		# Convert buffer from MB to bytes
		buffer_bytes = buffer_mb * 1024 * 1024
		max_size = available_memory - buffer_bytes
		return max_size
	return None


def is_text_file(file_path):
	try:
		with open(file_path, 'rb') as file:
			chunk = file.read(1024)
			return all(byte < 128 or byte in (9, 10, 13) for byte in chunk)
	except Exception:
		return False



report = {
	'files': 0,
	'indexed': 0,
	'size': 0,
}

skipReport = {
	'0': 0,
	'1': 0,
	'2': 0,
	'3': 0,
}

if _.switches.isActive('Commit'):
	CommitEvery = int(_.switches.value('Commit'))
else:
	CommitEvery = 1000
if _.switches.isActive('MemoryBufferMB'):
	MemoryBufferMB = int(_.switches.value('MemoryBufferMB'))
else:
	MemoryBufferMB = 10

# omit_extensions = [
#     '.log',     # Log files
#     '.gz',      # Compressed log or backup files
#     '.sql',     # SQL dump files
#     '.tar',     # Archive files
#     '.zip',     # Compressed archive files
#     '.bak',     # Backup files
#     '.old',     # Old configuration or log files
#     '.eml',     # Email message files
#     '.msg',     # Email message files
#     '.txt',     # Text files that can be large
#     '.csv',     # CSV files that may contain large datasets
#     '.conf',    # Configuration files
#     '.out',     # Output log files
#     '.err',     # Error log files
#     '.pid',     # Process ID files, typically text-based
#     '.swp',     # Swap files, usually created by editors like vim
#     '.cache',   # Cache files
#     '.dmp',     # Dump files
#     '.tmp',     # Temporary files
#     '.rbi',      # Ruby interface files (as seen in your logs)
# 	'.cfg',
# 	'.dat',
# 	'.lock',
# 	'.rar',
# 	'.7z', '.bin', '.iso', '.exe', '.dll', '.db'
# ]

omit_extensions = [
	# Logs and temporary files
	'.log', '.out', '.err', '.tmp', '.swp', '.pid', '.cache', '.dmp', '.bak', '.old', '.lock',

	# Compressed and archive files
	'.gz', '.tar', '.zip', '.rar', '.7z', '.bz2', '.xz', '.tgz', '.iso',

	# Binary executables and libraries
	'.bin', '.exe', '.dll', '.so', '.o', '.class', '.jar',

	# Disk and backup files
	'.img', '.vmdk', '.qcow2', '.vdi', '.bak', '.backup', '.ghost', '.dmg', '.bk',

	# Database and data dumps
	'.sql', '.db', '.sqlite', '.dbf', '.mdb', '.dat', '.sav',

	# Media files (images, videos, audio)
	'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg',
	'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.mpg', '.mpeg',
	'.mp3', '.wav', '.flac', '.aac', '.ogg',

	# Configuration and markup files
	'.conf', '.cfg', '.ini', '.plist', '.json', '.xml', '.yaml', '.yml',

	# Email and messaging files
	'.eml', '.msg', '.mbox', '.pst', '.ost',

	# Large text or dataset files
	'.csv', '.tsv', '.xlsx', '.xls', '.ods',

	# Code artifacts and metadata
	'.class', '.rbi', '.pyc', '.pyo', '.log',
]



def get_extension(abs_path):
	_, ext = os.path.splitext(abs_path)
	return ext

testStuff = {
	'cnt': 0,
	'size': 0
}
def index_files(c, directory, recursion=False, max_size=None):
	global cnt
	global conn
	global report
	global skipReport
	global CommitEvery
	global MemoryBufferMB
	global omit_extensions
	global testStuff

	commitOn = 1000

	for filename in os.listdir(directory):
		if not _.showLine(filename): continue
		max_size = calculate_max_size(MemoryBufferMB)
		try:
			abs_path = os.path.join(directory, filename)
		except:
			continue
		
		try:

			if _.switches.isActive('Test'):

				if os.path.isdir(abs_path) and recursion:
					index_files(c, abs_path, recursion, max_size)
				else:
					testStuff['cnt'] += 1
					try:
						size = os.path.getsize(abs_path)
						testStuff['size'] += size
						fSize = _.formatSize(size)
						_.pr(fSize,c='cyan')
					except Exception as e:
						_.pr('Error:',e,c='red')
						_.pr(abs_path,c='yellow')
						_.isExit(__file__)
				continue
				



			# ext = get_extension(abs_path).lower()
			ext = '.'+abs_path.split('.')[-1]
			# if ext: print(ext); _.isExit(__file__)
			if ext in omit_extensions:
				continue
			# print(abs_path)
			if os.path.isdir(abs_path) and recursion:
				index_files(c, abs_path, recursion, max_size)  # Pass the max_size parameter to subdirectories
			else:
				if isLink(abs_path): continue
				if is_binary_file(abs_path): continue
				sizeSkipped = False
				try:
					size = os.path.getsize(abs_path)
					if max_size is not None and size > max_size:
						sizeSkipped = True
						_.pr(abs_path,c='red')
						skipReport['1'] += 1
						continue
				except:
					skipReport['1'] += 1
					_.pr(abs_path,c='purple')
					continue

				try:
					created = os.path.getctime(abs_path)
					modified = os.path.getmtime(abs_path)
					is_dir = 1 if os.path.isdir(abs_path) else 0
					rawMime = file_mime(abs_path)
					isText = is_text_file(abs_path)
					
					content = ""
					if sizeSkipped:
						skipped = 1
						skipReport['1'] += 1
					else:
						if not os.path.isfile(abs_path):
							skipped = 3
							skipReport['3'] += 1
						else:
							if not isText:
								skipped = 2
								skipReport['2'] += 1
							else:
								skipped = 0
								skipReport['0'] += 1
								content = get_content(abs_path)
					cnt += 1
					c.execute("INSERT INTO files VALUES (?,?,?,?,?,?,?,?,?)", (filename, abs_path, size, created, modified, is_dir, content, rawMime, skipped))
					report['files'] += 1
					if cnt % commitOn == 0:
						conn.commit()
						_.pr(cnt, r=1)
				except Exception as e:
					print(f"Error processing {abs_path}: {e}")
		except Exception as e:
			print(f"Error accessing {abs_path}: {e}")



# def index_files(c, directory, recursion=False):
# 	global cnt
# 	global conn
# 	for filename in os.listdir(directory):
# 		try:
# 			abs_path = os.path.join(directory, filename)
# 			if os.path.isdir(abs_path) and recursion:
# 				index_files(c, abs_path, recursion)  # Corrected the arguments here
# 			else:
# 				try:
# 					size = os.path.getsize(abs_path)
# 					created = os.path.getctime(abs_path)
# 					modified = os.path.getmtime(abs_path)
# 					is_dir = 1 if os.path.isdir(abs_path) else 0
# 					content = get_content(abs_path) if is_text(abs_path) else ""
# 					cnt += 1
# 					c.execute("INSERT INTO files VALUES (?,?,?,?,?,?,?)", (filename, abs_path, size, created, modified, is_dir, content))
# 					if cnt % 100 == 0:
# 						conn.commit()
# 						_.pr( cnt, r=1 )
# 				except: pass
# 		except: pass

def numb(num):
	num = int(num)
	if num < 10:
		return '0'+str(num)
	else:
		return str(num)

def dbRename(db):
	db = __.path(db)
	fo = __.path(db,fo=True)+os.sep
	fi = __.path(db,fi=True)
	if os.path.isfile(db):
		import shutil
		modified = _.friendlyDate( _.autoDate( _.mod(db) ) ).split(' ')[0].replace('-','.')
		to = fo+modified+'-'+fi
		i=1
		while os.path.isfile(to):
			i+=1
			to = fo+modified+'-'+numb(i)+'-'+fi
		shutil.move(db,to)
try:
	import magic
except: pass
def file_mime(file_path):
	try:
		mime = magic.Magic()
		try:
			mime_type = mime.from_file(file_path)
			return mime_type.split()[0]
		except:
			return 'error'
	except:
		return 'unavailable'

def action():
	if _.switches.isActive('Test'):
		global testStuff
		index_files(1,os.getcwd(), True)
		testStuff['cnt'] = _.addComma(testStuff['cnt'])
		testStuff['size'] = _.formatSize(testStuff['size'])
		_.pr()
		_.pr('testStuff')
		_.printDicFields(testStuff)
		return False

	global report
	global skipReport
	if _.switches.isActive('PrintMemory'):
		max_size = get_memory_available()
		if not max_size is None:
			_.pr(max_size)
			_.pr( _.formatSize(max_size) )
		else:
			_.pr('No memory information available')
		_.isExit(__file__)
	global conn
	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
	else:
		db = 'index.db'
	dbRename(db)
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute('''CREATE TABLE files
				 (name text, path text, size real, created real, modified real, is_dir integer, content text, mime text, skipped integer)''')
	index_files(c,os.getcwd(), True)
	conn.commit()
	conn.close()
	# _.pr()
	# _.pr('Raw Report')
	# _.printDicFields(report)
	# _.pr('Raw Skip')
	# _.printDicFields(skipReport)
	for k in report: report[k] = _.addComma(report[k])
	for k in skipReport: skipReport[k] = _.addComma(skipReport[k])
	_.pr()
	_.pr('Report')
	_.printDicFields(report)
	_.pr('Cache')
	SkipReportFinal = {
		'Cached': skipReport['0'],
		'Skip, Size': skipReport['1'],
		'Skip, Binary': skipReport['2'],
		'Skip, Not a file': skipReport['3'],
	}
	_.printDicFields(SkipReportFinal)

########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)