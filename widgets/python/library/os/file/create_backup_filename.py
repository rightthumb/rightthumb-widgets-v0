import _rightThumb._base3 as _

def create_backup_filename(original_file, folder=None, mkdir=True, label=None, md5=False):
	import os
	from datetime import datetime
	if not folder is None and type(folder) == bool and (folder == False):
		folder = None
	if not folder is None and type(folder) == bool and (folder == True):
		if _.switches.isActive('Folder'):
			folder = _.switches.value('Folder')
		elif _.switches.isActive('Folders'):
			folder = _.switches.value('Folders')
		elif _.switches.isActive('BackupFolder'):
			folder = _.switches.value('BackupFolder')
	if not folder is None and type(folder) == list and (not len(folder)):
		folder = None
	if not folder is None and type(folder) == list:
		folder = folder[0]
	if not type(folder) == str:
		folder = None
	if not folder is None and (not len(folder.strip())):
		folder = None
	if not folder is None and (not os.path.isdir(folder)) and mkdir:
		os.mkdir(folder)
	dir_name, file_name = os.path.split(original_file)
	base_name, extension = os.path.splitext(file_name)
	current_date = datetime.now().strftime('%Y-%m-%d')
	try:
		epoch_time = int(os.path.getmtime(original_file))
	except:
		import time
		epoch_time = int(time.time())
	if os.path.isfile(original_file):
		_.regID(epoch_time, os.path.abspath(original_file))
	inner = ''
	name = os.path.basename(original_file)
	if name == '__init__.py':
		base = os.path.basename(os.path.dirname(original_file))
		inner += '...(' + base + ')...'
		
	
	if not label is None:
		label = label.replace(' ', '.')
		if len(inner):
			inner += f'{label}...'+'__bk__'
		else:
			inner += f'...{label}...'+'__bk__'
	else:
		inner += '__bk__'
	inner = inner.replace('__' + '__', '__')
	backup_file_name = f'{file_name}{inner}{current_date}_{epoch_time}{extension}'
	if dir_name:
		if not folder is None:
			if os.sep in folder:
				return os.path.join(folder, backup_file_name)
			else:
				return os.path.join(dir_name.rstrip(os.sep) + os.sep + folder, backup_file_name)
		else:
			return os.path.join(dir_name, backup_file_name)
	elif not folder is None:
		return os.path.join(folder, backup_file_name)
	return backup_file_name.replace(' ','_')