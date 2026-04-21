
def create_backup_filename(original_file,folder=None,mkdir=True,label=None,md5=False):
	import os
	from datetime import datetime
	if not folder is None and type(folder) == bool and folder == False: folder = None
	if not folder is None and type(folder) == bool and folder == True:
		global switches
		if switches.isActive('Folder'): folder = switches.value('Folder')
		elif switches.isActive('Folders'): folder = switches.value('Folders')
		elif switches.isActive('BackupFolder'): folder = switches.value('BackupFolder')
	if not folder is None and type(folder) == list and not len(folder): folder = None
	if not folder is None and type(folder) == list:
		folder = folder[0]
	
	if not type(folder) == str: folder = None
	if not folder is None and not len(folder.strip()): folder = None
	if not folder is None and not os.path.isdir(folder) and mkdir:
		os.mkdir(folder)


	# Split the file into path, name, and extension
	dir_name, file_name = os.path.split(original_file)
	base_name, extension = os.path.splitext(file_name)

	# Get current date and epoch time
	current_date = datetime.now().strftime("%Y-%m-%d")
	try:
		epoch_time = int(os.path.getmtime(original_file))
	except:
		import time
		epoch_time = int(time.time())
	if os.path.isfile(original_file):
		regID(epoch_time,os.path.abspath(original_file))

	inner = '__bk__'
	if not label is None:
		label = label.replace(' ','.')
		inner = f'__bk-{label}__'
	# if md5:
	# 	if os.path.isfile(original_file):
	# 		absPath = os.path.abspath(original_file)
	# 		inner += '__'+regMD5Mini(absPath,absPath)+'__'
	# 	else:
	# 		inner += '__'+genUUID(original_file)+'__'
	inner = inner.replace('__'+'__','__')

	# Create the backup file name
	backup_file_name = f"{file_name}{inner}{current_date}_{epoch_time}{extension}"
	
	# Return the full path if a directory is provided
	if dir_name:
		if not folder is None:
			if os.sep in folder:
				return os.path.join(folder, backup_file_name)
			else:
				return os.path.join(dir_name.rstrip(os.sep)+os.sep+folder, backup_file_name)
		else:
			return os.path.join(dir_name, backup_file_name)
	else:
		if not folder is None:
			return os.path.join(folder, backup_file_name)
	return backup_file_name