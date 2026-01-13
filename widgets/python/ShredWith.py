import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'OverwriteWith', '-w,-with','/opt/a_large_shred_file_to_overwrite_with_before_delete' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Recursive', '-r,-recursive' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
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
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start




import shutil
import os

def create_shred_templates(folder_path):
	sizes = [1, 10, 500, 1024, 5120, 10240]  # Sizes in MB: 1MB, 10MB, 500MB, 1GB, 5GB, 10GB
	chunk_size = 1024 * 1024  # 1MB chunk size

	for size in sizes:
		file_path = os.path.join(folder_path, f"shred_{size}MB")
		if not os.path.exists(file_path):
			with open(file_path, 'wb') as f:
				for _ in range(size):
					f.write(os.urandom(chunk_size))
			print(f"Created shred template: {file_path}")

def get_shred_template(size_in_bytes, folder_path):
	size_in_mb = size_in_bytes // (1024 * 1024)
	sizes = [1, 10, 500, 1024, 5120, 10240]
	best_match = min(sizes, key=lambda x: abs(x - size_in_mb))
	return best_match,os.path.join(folder_path, f"shred_{best_match}MB")

def overwrite_file(path, shred_template):
	chunk_size = 1024 * 1024  # 1MB chunk size
	with open(path, 'wb') as f:
		with open(shred_template, 'rb') as shred_file:
			while True:
				chunk = shred_file.read(chunk_size)
				if not chunk:
					break
				f.write(chunk)

def actionTest():
	if _.isData():
		files = _.isData()
	else:
		files = _.fo(r=_.switches.isActive('Recursive'))

	for path in files:
		if os.path.exists(path):
			print(f"Processing: {path}")

def shred_file(path):
	path = __.path(path)
	shred_template_folder = _v.stmp
	if os.path.isfile(path):
		# print(f"Processing: {path}")
		# continue
		try:
			file_size = os.path.getsize(path)
			best_match,template = get_shred_template(file_size, shred_template_folder)
			overwrite_file(path, template)
			os.remove(path)
			print(f"File {best_match} Securely deleted: {path}")
		except Exception as e:
			print(f"Error processing {path}: {e}")
	
def action():
	if _.isData():
		files = _.isData()
		for path in files:
			shred_file(path)
	else:
		files = _.fo(r=_.switches.isActive('Recursive'),script=shred_file)











########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);