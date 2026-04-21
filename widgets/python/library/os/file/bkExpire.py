import _rightThumb._base3 as _
import _rightThumb._vars as _v
import os
import shutil

def bkExpire(file, backup, age='1d', p=0, pCP=1, ago=None, cp=None, force=False):
	import shutil
	if not ago is None:
		age = ago
	file_path = file
	backup_path = backup
	age_in_epoch = _.timeAgo(age)
	if not os.path.exists(file_path):
		if p:
			print(f"Error: File '{file_path}' does not exist.")
		return False
	if os.path.isfile(backup_path):
		file_mod_time = os.path.getmtime(backup_path)
	if force or not os.path.isfile(backup_path) or file_mod_time < age_in_epoch:
		_v.mkdir(backup_path, pop=True)
		shutil.copy2(file_path, backup_path)
		if p or pCP:
			print(f"Backup created: '{file_path}' -> '{backup_path}'")
		if cp:
			bk = _.create_backup_filename(file_path, cp)
			_v.mkdir(bk, pop=True)
			shutil.copy2(file_path, bk)
		return True
	else:
		if p:
			print(f"No backup needed. The file '{file_path}' is not older than the specified age.")
		return False