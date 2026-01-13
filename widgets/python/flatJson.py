import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','roles.json', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'flatJson.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p flatJson -f roles.json'),
						_.hp('p flatJson -f roles.json | p flatJson'),
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

def flatten_namespace(data, parent_key='', sep='.'):
	flat = {}
	if isinstance(data, dict):
		for k, v in data.items():
			new_key = f"{parent_key}{sep}{k}" if parent_key else k
			flat.update(flatten_namespace(v, new_key, sep=sep))
	elif isinstance(data, list):
		for i, item in enumerate(data):
			new_key = f"{parent_key}{sep}{i}"
			flat.update(flatten_namespace(item, new_key, sep=sep))
	else:
		flat[parent_key] = data
	return flat
















import json

def set_deep(nested, keys, value):
	current = nested
	for i, key in enumerate(keys):
		is_last = i == len(keys) - 1

		if key.isdigit():
			key = int(key)
			if not isinstance(current, list):
				current_parent[last_key] = []
				current = current_parent[last_key]
			while len(current) <= key:
				current.append({})
			if is_last:
				current[key] = value
			else:
				if not isinstance(current[key], dict):
					current[key] = {}
				current_parent = current
				current = current[key]
		else:
			if is_last:
				current[key] = value
			else:
				if key not in current or not isinstance(current[key], (dict, list)):
					current[key] = {}
				current_parent = current
				current = current[key]
		last_key = key

def parse_lines_to_nested(lines):
	nested = {}
	for line in lines:
		if '=' not in line:
			continue
		key, value = map(str.strip, line.split('=', 1))
		path = key.split('.')
		set_deep(nested, path, value)
	return nested

def convert_users_dict_to_list(nested):
	if 'users' in nested and isinstance(nested['users'], dict):
		user_list = []
		for i in sorted(nested['users'], key=int):
			user_list.append(nested['users'][i])
		nested['users'] = user_list
	return nested







import json
def action():
	if _.switches.isActive('Files'):
		_.switches.set('Long','active',True)
		data = _.getTable2(_.switches.value('Files'))
		flat = flatten_namespace(data)
		table = []
		for k, v in flat.items():
			table.append({'key': k, 'eq':'=', 'value': v})
		_.pt(table)
		return




	data = _.isData()
	data = '\n'.join(data).strip()

	
	if data.startswith('[') or data.startswith('{'):
		data = json.loads(data)
		
		flat = flatten_namespace(data)
		table = []
		for k, v in flat.items():
			table.append({'key': k, 'eq':'=', 'value': v})
		_.pt(table)
		return




	while '  ' in data:
		data = data.replace('  ',' ')
	
	data = data.replace(' =','=')
	data = data.replace('= ','=')
	data = data.split('\n')
	flat_lines = []
	for i, line in enumerate(data):
		if '=' in line:
			data[i] = line.strip()
			flat_lines.append(data[i])
	# data = '\n'.join(new)
	# Build nested structure
	nested_data = parse_lines_to_nested(flat_lines)
	nested_data = convert_users_dict_to_list(nested_data)

	# Print JSON
	print(json.dumps(nested_data, indent=2))
	

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)