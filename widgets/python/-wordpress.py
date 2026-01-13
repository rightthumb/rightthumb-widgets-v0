import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register('Folders', '-f,-fo,-folder,-folders')
	_.switches.register('Depth', '-d,-depth')
	_.switches.register('ShowFolders', '-sf,-show,-showfolders')
	_.switches.register('DeepClean', '-dc,-deep,-deepclean')

	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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

# --------------------------------
# Core search (DFS limited by depth)
# --------------------------------
def find_all_wp_configs(base_path, max_depth):
	base_path = os.path.abspath(os.path.expanduser(base_path))
	results = []

	def _search(path, depth):
		if depth > max_depth:
			return
		try:
			with os.scandir(path) as it:
				for entry in it:
					if entry.is_file() and entry.name == "wp-config.php":
						results.append(os.path.abspath(entry.path))
					elif entry.is_dir():
						_search(entry.path, depth + 1)
		except (PermissionError, FileNotFoundError, NotADirectoryError):
			pass

	_search(base_path, 0)
	return results


# --------------------------------
# Helpers
# --------------------------------
def _top_level_dir_of(path, root):
	"""
	Return the top-level directory under 'root' that contains 'path'.
	For './siteA/wp/wp-config.php' with root='.', returns 'siteA'.
	Returns '.' if the file sits directly under root.
	"""
	root = os.path.abspath(root)
	path = os.path.abspath(path)
	rel = os.path.relpath(path, root)
	parts = rel.split(os.sep)
	return '.' if len(parts) <= 2 else parts[0]

def _gather_folders_from_cwd():
	"""
	Current folder plus all immediate subfolders.
	"""
	folders = ['.']
	for d in os.listdir('.'):
		if os.path.isdir(d):
			folders.append(os.path.join('.', d))
	return folders


# --------------------------------
# Action
# --------------------------------
def action():
	# ------------------------------
	# Switches
	# ------------------------------
	depth = 6
	if _.switches.isActive('Depth'):
		try:
			depth = int(_.switches.value('Depth')[0])
		except Exception:
			pass

	# Use current folder + immediate subfolders by default
	folders = _gather_folders_from_cwd()
	if _.switches.isActive('Folders'):
		# Allow overriding with -Folders "/var/www,/srv/www"
		raw = _.switches.values('Folders')
		override = []
		for item in raw:
			for part in str(item).split(','):
				part = part.strip()
				if part:
					override.append(os.path.expanduser(part))
		if override:
			folders = override

	_.pr('\n# WordPress Config Scan', c='cyan')
	_.pr(f'# Depth: {depth}', c='cyan')
	_.pr('# Folders:', c='cyan')
	for f in folders:
		_.pr('  - ' + os.path.abspath(f), c='darkcyan')

	# ------------------------------
	# Scan
	# ------------------------------
	all_matches = []
	folder_rows = []       # for ShowFolders table
	package_map = {}       # top-level => paths
	folder_map = {}        # top-level => set of containing folders (for conflicts)

	for folder in folders:
		matches = find_all_wp_configs(folder, depth)
		for p in matches:
			all_matches.append(p)
			# "package" = top-level dir under scanned root (closest site bucket)
			pkg = _top_level_dir_of(p, folder)
			package_map.setdefault(pkg, []).append(p)
			folder_map.setdefault(pkg, set()).add(os.path.dirname(p))

			# rows for pretty table
			folder_rows.append({
				'package': pkg,
				'folder': os.path.dirname(p),
				'path': p,
			})

	cnt = len(all_matches)
	deep_clean_set = set(all_matches)           # unique paths
	unique_cnt = len(deep_clean_set)

	# ------------------------------
	# Summary
	# ------------------------------
	if unique_cnt > 3:
		_.pr('\n# Unique (wp-config.php): ' + str(unique_cnt), c='yellow')

	if cnt != unique_cnt:
		_.pr('# Total (All Matches): ' + str(cnt), c='yellow')

	# ------------------------------
	# Conflict report (packages with >1 config)
	# ------------------------------
	if _.switches.isActive('DeepClean'):
		_.pr('\n# Deep Clean Conflicts:\n', c='purple')
		for pkg, paths in sorted(package_map.items()):
			unique_cmds = sorted(set(paths))
			if len(unique_cmds) > 1:
				print(f'\n# {pkg}')
				for path in unique_cmds:
					print(path)
				if _.switches.isActive('Folders'):
					for f in sorted(folder_map.get(pkg, [])):
						print(f'  - {f}')

	# ------------------------------
	# ShowFolders Table Output
	# ------------------------------
	if _.switches.isActive('ShowFolders'):
		def clean(path):
			# match your sample’s clean step idea
			return path.replace('wp-config.php', '')
		_.switches.set('Long', 'active', True)
		show_cols = 'package,folder'
		_.pt(folder_rows, show_cols, t={'folder': clean})

	# Default print (when no ShowFolders)
	if not _.switches.isActive('ShowFolders'):
		if unique_cnt:
			_.pr('\n# Paths:\n', c='green')
			for p in sorted(deep_clean_set):
				print(p)
		else:
			_.pr('\nNo wp-config.php files found', c='red')


# --------------------------------
# Expected switches (RightThumb-style)
# --------------------------------
# -Depth 6                 # max recursion depth
# -Folders /var/www,/srv/www  # override root(s); otherwise uses . + ./*
# -ShowFolders             # show table (package, folder)
# -DeepClean               # show “conflict” packages with >1 wp-config.php






########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)