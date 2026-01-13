import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Scan', '-scan' )
	_.switches.register( 'Recursive', '-r', '3 (depth)' )
	_.switches.register( 'DeepClean', '-d' )
	_.switches.register( 'ShowFolders', '-f' )
	_.switches.register( 'IncludeCommands', '-i' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': '-composer.py',
	'description': 'Rebuilds composer command from meta (composer.json)',
	'categories': [
						'reverse-engineer',
						'composer',
						'cli',
				],
	'examples': [

						_.hp('p -composer.py'),
						_.hp('p -composer.py -scan'),
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


# import os
# import json

# def reverse_engineer_composer_require(path='composer.json'):
#     with open(path, 'r', encoding='utf-8') as f:
#         composer_data = json.load(f)

#     commands = []

#     def generate_command(deps, dev=False):
#         if not deps:
#             return
#         cmd = ['composer require']
#         if dev:
#             cmd.append('--dev')
#         for package, version in deps.items():
#             cmd.append(f'{package}:{version}')
#         commands.append(' '.join(cmd))
	
#     generate_command(composer_data.get('require'), dev=False)
#     generate_command(composer_data.get('require-dev'), dev=True)

#     return commands


# import os

# def get_folders_in_current_dir():
#     current_dir = os.getcwd()
#     return [name for name in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, name))]


# def scan_and_process_composer_files(base_dir='.'):
#     results = {}



#     return results



# def action():

#     if _.switches.isActive('Scan'):
#         folders = get_folders_in_current_dir()
#         for folder in folders:
#             path = os.path.join(os.getcwd(), folder)
#             if os.path.isdir(path):
#                 try:
#                     for cmd in reverse_engineer_composer_require(os.path.join(path, 'composer.json')):
#                         print(cmd)
#                 except:
#                     pass

#     else:
#         try:
#             for cmd in reverse_engineer_composer_require():
#                 print(cmd)
#         except:
#             _.pr('Error: No composer.json file found in the current directory.', c='red')









cnt = 0

import os
import json

def reverse_engineer_composer_require(path='composer.json'):
	global cnt
	with open(path, 'r', encoding='utf-8') as f:
		composer_data = json.load(f)

	commands = []

	def generate_command(deps, dev=False):
		if not deps:
			return
		cmd = ['composer require']
		if dev:
			cmd.append('--dev')
		for package, version in deps.items():
			cmd.append(f'{package}:{version}')
		commands.append(' '.join(cmd))

	generate_command(composer_data.get('require'), dev=False)
	generate_command(composer_data.get('require-dev'), dev=True)
	cnt += len(commands)
	return commands


def scan_composer_folders(base_dir='.'):
	results = {}
	for name in os.listdir(base_dir):
		path = os.path.join(base_dir, name, 'composer.json')
		if os.path.isfile(path):
			try:
				commands = reverse_engineer_composer_require(path)
				results[path] = commands
			except Exception as e:
				results[path] = [f"# Error: {e}"]
	return results


def scan_composer_folders_recursive(base_dir='.', max_depth=0):
	results = {}

	def walk(current_path, current_depth):
		if max_depth and current_depth > max_depth:
			return
		composer_path = os.path.join(current_path, 'composer.json')
		if os.path.isfile(composer_path):
			try:
				commands = reverse_engineer_composer_require(composer_path)
				results[composer_path] = commands
			except Exception as e:
				results[composer_path] = [f"# Error: {e}"]
		try:
			for item in os.listdir(current_path):
				item_path = os.path.join(current_path, item)
				if os.path.isdir(item_path):
					walk(item_path, current_depth + 1)
		except Exception as e:
			pass

	walk(base_dir, 0)
	return results





def generate_include_commands():
	include_lines = []
	seen_paths = set()

	def get_include(path):
		composer_dir = os.path.dirname(os.path.abspath(path))
		autoload_path = os.path.join(composer_dir, 'vendor', 'autoload.php')
		return f"include_once('{autoload_path}');"

	targets = {}

	# Recursive if active
	if _.switches.isActive('Recursive'):
		depth = int(_.switches.value('Recursive')[0]) if _.switches.value('Recursive') else 0
		targets.update(scan_composer_folders_recursive('.', depth))

	# Flat scan if active
	if _.switches.isActive('Scan'):
		targets.update(scan_composer_folders())

	# Always check current folder's composer.json
	current_path = './composer.json'
	if os.path.isfile(current_path):
		targets[current_path] = reverse_engineer_composer_require(current_path)

	for composer_path in targets:
		resolved = os.path.abspath(composer_path)
		if resolved not in seen_paths:
			seen_paths.add(resolved)
			try:
				line = get_include(composer_path)
				include_lines.append(line)
			except Exception as e:
				include_lines.append(f"# Error generating include for {composer_path}: {e}")

	return include_lines







from collections import defaultdict
def action():

	if _.switches.isActive('IncludeCommands'):
		include_lines = generate_include_commands()
		for line in include_lines:
			_.pr(line, c='cyan')
		return

	_commands = []
	seen = set()
	package_map = defaultdict(list)
	folder_map = defaultdict(set)
	folder_rows = []
	global cnt
	cnt = 0

	if _.switches.isActive('Recursive'):
		if len(_.switches.value('Recursive')):
			depth = int(_.switches.value('Recursive'))
		else:
			depth = 0  # unlimited
		results = scan_composer_folders_recursive('.', depth)
	elif _.switches.isActive('Scan'):
		results = scan_composer_folders()
	else:
		try:
			results = {'./composer.json': reverse_engineer_composer_require()}
		except:
			_.pr('Error: No composer.json file found in the current directory.', c='red')
			return

	for path, commands in results.items():
		for cmd in commands:
			cnt += 1
			parts = cmd.split()
			if parts[0] == 'composer' and parts[1] == 'require':
				for token in parts[2:]:
					if ':' in token:
						pkg = token.split(':')[0]
						package_map[pkg].append(cmd)
						folder_map[pkg].add(path)
						folder_rows.append({'package': pkg, 'folder': path, 'command': cmd})

			if not _.switches.isActive('DeepClean'):
				if cmd not in seen:
					seen.add(cmd)
					_commands.append(cmd)

	# ------------------------------
	# DeepClean OFF
	# ------------------------------
	if not _.switches.isActive('DeepClean'):
		if not _.switches.isActive('ShowFolders'):
			for cmd in _commands:
				_.pr(cmd, c='cyan')

		if len(_commands) > 3:
			_.pr('\n# Unique: ', len(_commands), c='yellow')

		if cnt != len(_commands):
			_.pr('# Total: ', cnt, c='yellow')

	# ------------------------------
	# DeepClean ON
	# ------------------------------
	else:
		deep_clean_set = set()
		for pkg, cmds in package_map.items():
			deep_clean_set.add(sorted(set(cmds))[0])  # one representative command

		if not _.switches.isActive('ShowFolders'):
			for cmd in sorted(deep_clean_set):
				_.pr(cmd, c='cyan')

		if len(deep_clean_set) > 3:
			_.pr('\n# Unique (Cleaned): ', len(deep_clean_set), c='yellow')

		if cnt != len(deep_clean_set):
			_.pr('# Total (All Commands): ', cnt, c='yellow')

		# ------------------------------
		# Conflict report
		# ------------------------------
		if len(_.switches.value('DeepClean')):
			_.pr('\n# Deep Clean Conflicts:\n', c='magenta')
			for pkg, cmds in package_map.items():
				unique_cmds = sorted(set(cmds))
				if len(unique_cmds) > 1:
					print(f'\n# {pkg}')
					for cmd in unique_cmds:
						print(cmd)
					if _.switches.isActive('Folders'):
						for f in sorted(folder_map[pkg]):
							print(f'  - {f}')

	# ------------------------------
	# ShowFolders Table Output
	# ------------------------------
	if _.switches.isActive('ShowFolders'):
		def clean(path):
			path = path.replace('composer.json', '')
			return path
		_.switches.set('Long','active',True)
		show_cols = 'package,folder,command'
		show_cols = 'package,folder'
		# folder_rows = trig(folder_rows, {'folder': clean})
		_.pt(folder_rows, show_cols,t={'folder':clean})







########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)