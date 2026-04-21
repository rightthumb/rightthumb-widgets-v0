import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Keys', '-k,-key,-keys', 'key1,key2' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'merge-json-lists.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp(p merge-json-lists -f 1713723638.6172287-2024_04_21-14_11_20-fileBackup.json fileBackup.json -keys id timestamp'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


# def update_index(index, rec, keys):
#     # Base case: If no more keys to process, return
#     if not keys:
#         return

#     key = keys[0]  # Get the current key
#     if key not in index:
#         index[key] = {}
	
#     if len(keys) == 1:
#         # If this is the last key, update the index with the record
#         if rec[key] not in index[key]:
#             index[key][rec[key]] = []
#         index[key][rec[key]].append(rec)
#     else:
#         # Recursive case: Process the next level
#         next_keys = keys[1:]
#         if rec[key] not in index[key]:
#             index[key][rec[key]] = {}
#         update_index(index[key][rec[key]], rec, next_keys)

# def valid(rec):
# 	global index, keys, wasIndexed
# 	if not wasIndexed:
# 		update_index(index, rec, keys)


# 	return True
# wasIndexed = False
# index = {}
# keys = _.switches.values('Keys')
# def action():
# 	global index, keys
# 	data = []
	
# 	for file in _.switches.values('Files'):
# 		this = _.getTable2(file)
# 		if not data:
# 			data = this
			
# 			for key in keys:
				
# 		else:







import json

def update_index(index, rec, keys):
	# Create a unique key by concatenating values of specified keys into a single string
	key_values = '_'.join([str(rec[k]) for k in keys])
	
	if key_values not in index:
		index[key_values] = rec
	else:
		# Optionally merge records if there's a conflict
		for k, v in rec.items():
			if k not in index[key_values] or index[key_values][k] == "":
				index[key_values][k] = v

def merge_data(data_sets, keys):
	index = {}

	# Build index for all records in all data sets
	for data in data_sets:
		for rec in data:
			update_index(index, rec, keys)

	# Convert the index back into a list of records
	merged_data = list(index.values())
	
	return merged_data

def action():
	global wasIndexed
	wasIndexed = False

	# Retrieve the list of files and keys from your framework
	files = _.switches.values('Files')
	keys = _.switches.values('Keys')

	# Load data from all files
	data_sets = []
	for file in files:
		with open(file, 'r') as f:
			data = json.load(f)
			data_sets.append(data)
	
	# Merge data from all files
	merged_data = merge_data(data_sets, keys)
	
	# Write merged data to a new file or overwrite
	with open('merged_output.json', 'w') as f:
		json.dump(merged_data, f, indent=4)

# Example usage
# Ensure to define `_.switches.values` method to retrieve file paths and keys
# action()










########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);