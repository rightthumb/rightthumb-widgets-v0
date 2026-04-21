import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():

	swGrp = 0
	_.switches.register( 'DB', '-db,-database', group=[swGrp, 'Initialization'] )
	
	_.switches.register( 'Create/UpdateDatabase', '-create,-u,-up,-update', group=[swGrp, 'Used When Creating Or Updating The Database'] )
	_.switches.register( 'Ago', '-ago', '(blank=db date), 1w 1mo 1y, age/print-db-age', group=[swGrp, 'Used When Updating The Database'] )

	_.switches.register( 'DB-Type', '-t,-type', 'm c meta content', group=[swGrp, 'Used When Creating'] )
	swGrp += 1
	_.switches.register( 'Recursive', '-r,-recursive', group=[swGrp, 'Multipurpose'] )
	_.switches.register( 'SQL', '-sql', '''"select * from files where path = 'file.txt'"''', group=[swGrp, 'Multipurpose'] )

	swGrp += 1
	_.switches.register( 'Print-File-Content', '-pf,-pfc,-content', 'filename.txt/ or pipe|', group=[swGrp, 'Recovery'] )
	_.switches.register( 'Recover-Files', '-rFi,-recoverFile', 'filename.txt/or pipe|: backs up the overwrites file', group=[swGrp, 'Recovery'] )
	_.switches.register( 'Recover-Folders', '-rFo,-recoverFolder', 'optional folder/ or pipe|, can use with: -recursive', group=[swGrp, 'Recovery'] )
	
	# swGrp += 1
	# _.switches.register( 'Backup-Files', '-bk', '', group=[swGrp, 'Backup Files'] )
	
	swGrp += 1
	_.switches.register( 'Query', '-q,-query', '', group=[swGrp, 'Research'] )
	_.switches.register( 'Tool-List-Fields', '-fields', 'optional table name', group=[swGrp, 'Research'] )

	swGrp += 1
	_.switches.register( 'Tool-File-Meta', '-meta', group=[swGrp, 'Off Topic'] )


	
__.setting('omit-switch-triggers',['Ago'],[])
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p indexDBs -db -create -type meta -recursive'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	# _._default_triggers_()
	# _.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Print-File-Content', _.aliasesFi )
	_.switches.trigger( 'Tool-File-Meta', _.aliasesFi )
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


########################################################################################
# content database

MemoryBufferMB = 10

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
	'.txt', '.csv', '.tsv', '.xlsx', '.xls', '.ods',

	# Code artifacts and metadata
	'.class', '.rbi', '.pyc', '.pyo', '.log',
]

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
########################################################################################
def create_backup_filename(original_file):
	"""
	Creates a backup filename by appending the current date and epoch time.

	Parameters:
		original_file (str): The original file name with extension.

	Returns:
		str: The backup file name.
	"""
	import os
	from datetime import datetime
	# Split the file into path, name, and extension
	dir_name, file_name = os.path.split(original_file)
	base_name, extension = os.path.splitext(file_name)

	# Get current date and epoch time
	current_date = datetime.now().strftime("%Y-%m-%d")
	epoch_time = int(os.path.getmtime(original_file))

	# Create the backup file name
	backup_file_name = f"{file_name}__bk__{current_date}_{epoch_time}{extension}"

	# Return the full path if a directory is provided
	if dir_name:
		return os.path.join(dir_name, backup_file_name)
	return backup_file_name


fibk=create_backup_filename
backupName=create_backup_filename
########################################################################################




connect = None
cursor = None

def connectDB(db,dbType=None):
	if _.switches.isActive('DB-Type'):
		dbType = _.switches.value('DB-Type')
		if dbType.startswith('m'):
			dbType = 'meta'
		elif dbType.startswith('c'):
			dbType = 'content'
	shouldCreateTable = False
	if not os.path.isfile(db):
		shouldCreateTable = True
		
	global connect
	global cursor
	connect = sqlite3.connect(db)
	cursor = connect.cursor()

	if not tableExists('files'):
		shouldCreateTable = True
	
	if shouldCreateTable:
		if not _.switches.isActive('Create/UpdateDatabase'):
			_.e('Database does not exist','Please specify to create',['ex: -create -type meta','ex: -create -type content'])
		if dbType is None:
			_.e('Database does not exist','Please specify the database type to create',['ex: -type meta','ex: -type content'])
		if dbType == 'meta':
			sql =  'CREATE TABLE files (path text,  name_ text, name text, folder text, stat text, attrib text, bytes int, size text, date_created_raw double, date_modified_raw double, date_created text, date_modified text, type text, typesort text, ext text, week_of_year text, week_of_year_ text, day_of_the_week text, month text, friendly_week text, friendly_month text, accessed_raw double, date_accessed text                        , ce double, me double, ae double, meta text, header text, err int        )'
		else:
			sql = 'CREATE TABLE files (name text, path text, size real, created real, modified real, is_dir integer, content text, mime text, skipped integer)'
		cursor.execute(sql)


def closeDB():
	global connect
	global cursor
	cursor.close()
	connect.close()

def queryDB(path):
	global connect
	global cursor
	sql = 'select * from files where path = "'+path+'"'
	if _.switches.isActive('SQL'): _.pr(sql); _.pr('\nd114'); _.isExit(__file__);
	cursor.execute(sql)
	records = cursor.fetchall()
	if len(records) == 0:
		return False
	return records

import sqlite3

# Assuming `connect` and `cursor` are defined globally
def fields(table_name='files'):
	global sqlMgr
	return sqlMgr.fields('files')
	global connect
	global cursor

	try:
		cursor.execute(f"PRAGMA table_info({table_name});")
		columns = cursor.fetchall()

		fields = [column[1] for column in columns]
		return fields
	except sqlite3.Error as e:
		print(f"An error occurred: {e}")
		return []


def insertDB(data, table='files'):
	global connect
	global cursor

	fld = fields(table)
	for rec in data:
		for k in rec:
			if not k in fld:
				del rec[k]

	# Prepare the column names and placeholders for values
	columns = ', '.join([f'"{key}"' for key in data.keys()])
	placeholders = ', '.join(['?' for _ in data.keys()])
	values = list(data.values())

	sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

	# Debugging: Print the query and parameter values
	if _.switches.isActive('SQL'):
		_.pr(f"SQL Query: {sql}")
		_.pr(f"Values: {values}")
		_.pr('\nd114')
		_.isExit(__file__)

	try:
		cursor.execute(sql, values)
		connect.commit()
	except Exception as e:
		print(f"Error inserting into database: {e}")



def updateDB(path, data, table='files'):
	global sqlMgr
	info = sqlMgr.update_or_insert('files', {'path': path}, data, {})
	return info
	global connect
	global cursor
	fld = fields(table)
	for rec in data:
		for k in rec:
			if not k in fld:
				del rec[k]

	# Escape column names and prepare the set clause
	set_clause = ', '.join([f'"{key}" = ?' for key in data.keys()])
	values = list(data.values())
	values.append(path)

	sql = f"UPDATE {table} SET {set_clause} WHERE path = ?"

	# Debugging: Print the query and parameter values
	if _.switches.isActive('SQL'):
		_.pr(f"SQL Query: {sql}")
		_.pr(f"Values: {values}")
		_.pr('\nd114')
		_.isExit(__file__)

	try:
		cursor.execute(sql, values)
		connect.commit()
	except Exception as e:
		print(f"Error updating database: {e}")

def tableExists(table='files'):
	"""
	Checks if a table exists in the SQLite database.

	Parameters:
		table_name (str): The name of the table to check.

	Returns:
		bool: True if the table exists, False otherwise.
	"""
	global connect
	global cursor

	try:
		sql = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
		cursor.execute(sql, (table,))
		result = cursor.fetchone()
		return result is not None
	except Exception as e:
		print(f"Error checking if table exists: {e}")
		return False


def indexDB(files):
	global sqlMgr
	
	info = {
		'total': len(files),
		'success': 0,
		'updated': 0,
		'inserted': 0,
		'failed': 0,
		'failed-updating': 0,
		'failed-inserting': 0,
	}
	
	for path in files:
		if not _.showLine(path): continue
		path = os.path.abspath(path)
		if _.switches.isActive('Ago'):
			if os.path.getmtime(path) < _.switches.value('Ago'): continue
		record = _dir.fileInfo( path )
		info = sqlMgr.insert('files', record)
		return info
		if queryDB(path):
			try:
				updateDB(path, record)
				info['updated'] += 1
				info['success'] += 1
				_.pr('Updated: '+path)
			except:
				_.pr('Error updating record for: '+path,c='red')
				info['failed'] += 1
				info['failed-updating'] += 1
		else:
			try:
				insertDB(record)
				info['inserted'] += 1
				_.pr('Inserted: '+path)
			except:
				_.pr('Error inserting record for: '+path,c='red')
				info['failed'] += 1
				info['failed-inserting'] += 1
	# _.printDicFields(info)
	


# def createContentRecord(path):
# 	global omit_extensions
# 	abs_path = os.path.abspath(path)
# 	rec = _dir.fileInfo( abs_path )
# 	try:
# 		if '.'+rec['ext'].lower() in omit_extensions: return False
# 	except: pass
# 	try:
# 		created = os.path.getctime(abs_path)
# 		modified = os.path.getmtime(abs_path)
# 		is_dir = 1 if os.path.isdir(abs_path) else 0
# 		rawMime = file_mime(abs_path)
# 		isText = is_text_file(abs_path)
		
# 		content = ""
# 		try:
# 			content = get_content(abs_path)
# 		except:
# 			skipped = 1
# 		else:
# 			skipped = 0
# 		record = {
# 			'name': rec['name'],
# 			'path': abs_path,
# 			'size': rec['bytes'],
# 			'created': created,
# 			'modified': modified,
# 			'is_dir': is_dir,
# 			'content': content,
# 			'mime': rawMime,
# 			'skipped': skipped
# 		}
# 		return record
# 	except Exception as e:
# 		_.pr(f"Error inserting record for {abs_path}: {e}")
# 		return False

def getCachedContents(path,table='files'):
	global connect
	global cursor

	try:
		# Query to fetch paths and content from the table
		sql = f"SELECT path, content FROM {table} WHERE path = '{path}' AND content IS NOT NULL AND content != ''"
		cursor.execute(sql)
		records = cursor.fetchall()

		# Print each cached content with its corresponding path
		for record in records:
			path, content = record
			return content
			# print(f"Path: {path}\nContent:\n{content}\n{'-' * 40}\n")

	except Exception as e:
		print(f"Error fetching cached contents: {e}")


	return None



def createContentRecord(path):
	global omit_extensions
	abs_path = os.path.abspath(path)
	rec = _dir.fileInfo(abs_path)
	
	try:
		# Skip files with specified extensions
		if '.' + rec.get('ext', '').lower() in omit_extensions:
			return False
	except Exception:
		pass

	try:
		# File metadata
		created = os.path.getctime(abs_path)
		modified = os.path.getmtime(abs_path)
		is_dir = 1 if os.path.isdir(abs_path) else 0
		rawMime = file_mime(abs_path)
		isText = is_text_file(abs_path)

		content = ""
		skipped = 0

		# Read file content for text files
		if isText:
			try:
				with open(abs_path, 'r', encoding='utf-8', errors='ignore') as file:
					content = file.read()
			except Exception as e:
				_.pr(f"Error reading content for {abs_path}: {e}", c='red')
				skipped = 1
		else:
			skipped = 1

		# Create the record dictionary
		record = {
			'name': rec['name'],
			'path': abs_path,
			'size': rec['bytes'],
			'created': created,
			'modified': modified,
			'is_dir': is_dir,
			'content': content,
			'mime': rawMime,
			'skipped': skipped
		}
		return record

	except Exception as e:
		_.pr(f"Error creating content record for {abs_path}: {e}", c='red')
		return False

def recoverFolder(folder=None,recursive=False,table='files'):
	global connect
	global cursor
	if folder is None: folder = os.getcwd()
	if not len(folder.strip()): folder=os.getcwd()
	folder = folder.rstrip(os.sep) + os.sep  # Ensure the folder ends with the correct separator

	if not recursive:
		slash_count = folder.count(os.sep)

		sql_query = f"""
		SELECT path, content
		FROM {table}
		WHERE path LIKE ? AND 
			(LENGTH(path) - LENGTH(REPLACE(path, ?, ''))) = ?
		"""

		try:
			cursor.execute(sql_query, (f"{folder}%", os.sep, slash_count))
			files = cursor.fetchall()
			return files		

		except sqlite3.Error as e:
			_.pr("SQLite error:", e,c='red')
	elif recursive:
		sql_query = f"""
		SELECT path, content
		FROM {table}
		WHERE path LIKE ?
		"""

		try:
			cursor.execute(sql_query, (f"{folder}%",))
			files = cursor.fetchall()
			return files		

		except sqlite3.Error as e:
			_.pr("SQLite error:", e,c='red')



def contentDB(files):
	max_size = calculate_max_size(MemoryBufferMB)
	info = {
		'total': len(files),
		'success': 0,
		'updated': 0,
		'inserted': 0,
		'failed': 0,
		'failed-updating': 0,
		'failed-inserting': 0,
		'failed-creating': 0,
	}
	
	for path in files:
		path = os.path.abspath(path)
		if _.switches.isActive('Ago'):
			if os.path.getmtime(path) < _.switches.value('Ago'): continue
		if not os.path.isfile(path): continue
		if isLink(path): continue
		if is_binary_file(path): continue
		sizeSkipped = False
		try:
			size = os.path.getsize(path)
			if max_size is not None and size > max_size:
				_.pr(f"Skipping {path} because it is too large ({size} bytes)", c='red')
				continue
		except:
			continue
		record = createContentRecord(path)
		if record is False:
			info['failed'] += 1
			info['failed-creating'] += 1
			continue
		if queryDB(path):
			try:
				updateDB(path, record)
				info['updated'] += 1
				info['success'] += 1
				_.pr('Updated: '+path)
			except:
				_.pr('Error updating record for: '+path,c='red')
				info['failed'] += 1
				info['failed-updating'] += 1
		else:
			try:
				insertDB(record)
				info['inserted'] += 1
				_.pr('Inserted: '+path)
			except:
				_.pr('Error inserting record for: '+path,c='red')
				info['failed'] += 1
				info['failed-inserting'] += 1
	# _.printDicFields(info)
	

def dbQuery():
	global connect
	global cursor
	if _.switches.isActive('SQL'):
		sql = _.switches.value('SQL')
	
	cursor.execute(sql)
	records = cursor.fetchall()
	for record in records:
		_.pr(record)
	

def fo(folder=None,r=False,script=None):
	if folder is None:
		folder=os.getcwd()

	if not os.path.isdir(folder): return None

	try:
		files=os.listdir(folder)
	except Exception as e:
		_.pr('Error listing files in '+folder,c='red')
		return None
	for item in files:
		path=folder+os.sep+item
		path=__.path(path)
		if not script is None: script(path);
		if r and os.path.isdir(path): fo(path,r,script)
	return None






import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'db')))
from sqliteMgr import sqliteMgr


import sqlite3
import os
import _rightThumb._dir as _dir
########################################################################################
def action():
	global sqlMgr
	# print(backupName('index.db')); _.isExit(__file__)
	if _.switches.isActive('DB'):
		db = _.switches.value('DB')
	else:
		db = 'index.db'
	sqlMgr = sqliteMgr(db)

	if _.switches.isActive('Ago'):
		if _.switches.value('Ago') == '':
			_.switches.fieldSet('Ago','value',os.path.getmtime(db))
		elif 'age' in _.switches.value('Ago'):
			_.pr( _.friendlyDate(os.path.getmtime(db)) )
			return
		else:
			_.switches.fieldSet('Ago','value',_.timeAgo(_.switches.value('Ago')))

	if _.switches.isActive('Tool-File-Meta'):
		_.pv(_dir.fileInfo( _.switches.values('Tool-File-Meta')[0] )); _.isExit(__file__)

	# connectDB(db)

	if _.switches.isActive('Query'):
		dbQuery()
		return

	if _.switches.isActive('Recover-Folders'):
		from shutil import copyfile
		folders = _.switches.values('Recover-Folders')
		if not len(folders): folders = _.isData()
		for folder in folders:
			records = recoverFolder(folder=folder,recursive=_.switches.isActive('Recursive'))
			for record in records:
				path = record[0]
				content = record[1]
				# print(path)
				# print(content)
				# return
				# _.pr(path,c='green')
				folder = __.path(path,pop=True)
				os.makedirs(folder, exist_ok=True)
				if not os.path.isfile(path):
					_.saveText(content, path)
					continue
				
				path = os.path.abspath(path)
				backup = backupName(path)
				copyfile(path, backup)
				if not os.path.isfile(backup) or not os.path.getsize(backup) == os.path.getsize(path):
					_.pr(f"Error backing up {path} to {backup}", c='red')
					continue
				_.saveText(content, path)
				_.pr()
				_.pr(path,c='green')
				_.pr(backup,c='cyan')
				_.pr()
		return
	if _.switches.isActive('Recover-Files'):
		from shutil import copyfile
		files = _.switches.values('Recover-Files')
		if not len(files): files = _.isData()
		for path in files:
			content = getCachedContents(path)
			if content is None or not len(content):
				_.pr(f"No content found for {path}", c='red')
				continue
			if not os.path.isfile(path):
				folder = __.path(path,pop=True)
				os.makedirs(folder, exist_ok=True)
				_.saveText(content, path)
				continue
			
			path = os.path.abspath(path)
			backup = backupName(path)
			copyfile(path, backup)
			if not os.path.isfile(backup) or not os.path.getsize(backup) == os.path.getsize(path):
				_.pr(f"Error backing up {path} to {backup}", c='red')
				continue
			_.saveText(content, path)

			_.pr(f"Backed up {path} to {backup}")
		return

	if _.switches.isActive('Print-File-Content'):
		files = _.switches.values('Print-File-Content')
		if not len(files): files = _.isData()
		for path in files:
			path = os.path.abspath(path)
			content = getCachedContents(path)
			if content is not None:
				_.pr(content)
			else:
				_.pr(f"No content found for {path}", c='red')
		return

	if _.switches.isActive('Tool-List-Fields'):
		table = _.switches.value('Tool-List-Fields').strip()
		if not table: table = 'files'
		for field in fields(table):
			_.pr(field)
		return
	
	if not _.switches.isActive('Create/UpdateDatabase'):
		_.e('No action specified','Please specify to update or create the database',['ex: -update','ex: -create'])


	files = _.isData()
	if not files:
		script = None
		def indexDBFi(path): indexDB([path])
		def contentDBFi(path): contentDB([path])
		if _.switches.isActive('DB-Type'):
			dbType = _.switches.value('DB-Type')
			if dbType.startswith('m'):
				script=indexDBFi
			elif dbType.startswith('c'):
				script=contentDBFi
		else:
			dbType = None

		if os.path.isfile(db):
			if not 'content' in fields():
				script=indexDBFi
			else:
				script=contentDBFi


		if script is None:
			_.e('Database does not exist','Please specify the database type to create',['ex: -type meta','ex: -type content'])

		fo(r=_.switches.isActive('Recursive'),script=script)
		return


	if not 'content' in fields():
		indexDB(files)
	else:
		contentDB(files)
	sqlMgr.close()
	# closeDB()
if __name__ == '__main__':
	action(); _.isExit(__file__);