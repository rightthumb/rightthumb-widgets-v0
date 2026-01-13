import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import os
import shutil
db = None
def load():
	global db
	db = _.getTable('fileBackup.json')
	return

def pr(*args,**kwargs):
	_.pr(*args,**kwargs)

def action():
	global db
	load()
	base = os.getcwd() + os.sep

	# Collect all backup candidates per file, newest first
	candidates = {}
	for i, rec in enumerate(db):
		file_path = rec.get('file')
		backup_path = rec.get('backup')
		ts = rec.get('timestamp', 0)

		if not file_path or not backup_path:
			continue
		# Only consider files under the current working directory
		if not file_path.startswith(base):
			continue

		candidates.setdefault(file_path, []).append((ts, i))

	# Sort candidates for each file by timestamp (newest first)
	for file_path in candidates:
		candidates[file_path].sort(key=lambda t: t[0], reverse=True)

	restored, failed = [], []

	for path, items in candidates.items():
		# Only restore if the destination file exists and is exactly 0 bytes
		if not os.path.isfile(path):
			continue
		if os.path.getsize(path) != 0:
			continue

		# pr(path); continue

		# Find the newest backup that exists and is non-zero
		chosen_backup = None
		for _, idx in items:
			rec = db[idx]
			bpath = rec.get('backup')
			if bpath and os.path.isfile(bpath) and os.path.getsize(bpath) > 0:
				chosen_backup = bpath
				break

		if chosen_backup:
			os.makedirs(os.path.dirname(path), exist_ok=True)
			shutil.copy2(chosen_backup, path)
			pr(f"[restored] {path} <- {chosen_backup}")
			restored.append(path)
		else:
			pr(f"[no valid backup] {path}", c='red')
			failed.append(path)

	# Optionally return or log counts
	return {"restored": len(restored), "failed": len(failed)}




########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)