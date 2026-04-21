import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'ShowSearchResults', '-r,-results,-ss,-ssr,-print' )
	_.switches.register( 'DebugDump', '-d,-debug,-dump', 'record: default is stats and search results' )
	_.switches.register( 'Minimal', '--c,-m,-min,-minimal', 'default' )
	_.switches.register( 'IndexDump', '-index', 'pre' )
	_.switches.register( 'JSON', '-json,-x,-export', 'output is mysql json format' )
	_.switches.register( 'Regex', '-regex', 'use Regex to parse sql' )
	_.switches.register( 'Cache', '-cache', 'cache.json: use this on large files when doing research' )


_._default_settings_()

_.appInfo[focus()] = {
	'file': 'sql.py',
	'description': [
		'Parse large sql file to table records and fields the datamine it',
		'convert sql to json formatted same as mysql export',
		'Do a search and list every record and fields in that record that contains the search term',
		'Great for research on wordpress databases',
		'Great for manually making wordpress database changes manually',
		'Great for research on sql files',
		'',
		'',
		'Convert sql to json then use the tool json2sqlite.py',
		'',
		],
	'categories': [
						'sql',
						'datamine',
						'parse sql',
						'sql research',
						'research',
						'wordpress',
				],
	'examples': [
						_.hp('(All results are colorized)'),
						_.hp('cat tpn_wp.sql | p sql + "Old Company Name"'),
						_.hp('cat tpn_wp.sql | p sql + "Old Company Name" -results'),
						_.hp('cat tpn_wp.sql | p sql + "Old Company Name" -debug'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': ['json2sqlite','sqlite2json','sql'],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def sqlDirty_not_used(data):
	import re
	active = False
	table = ''
	tables = {}

	for line in data.split('\n'):
		line = line.strip()

		# Detect start of INSERT INTO statement and extract table name and fields
		if line.startswith('INSERT INTO'):
			active = True
			# print(f"Detected INSERT INTO statement: {line}")

			# Extract table name and fields
			match = re.search(r'INSERT INTO `([^`]+)` \(([^)]+)\)', line)
			if match:
				table = match.group(1)
				# print(f"Parsed table name: {table}")

				if table not in tables:
					tables[table] = {'fields': [], 'records': []}

				# Extract fields
				fields = match.group(2).split(', ')
				fields = [field.strip('`') for field in fields]
				tables[table]['fields'].extend(fields)
				# print(f"Extracted fields: {tables[table]['fields']}")

		# Process each VALUES line
		elif active:
			if line.endswith(';'):
				active = False

			# Check if there are records in this line
			if line.startswith('('):
				# Remove the surrounding parentheses and semicolon/comma
				record_str = line[1:-1].strip()
				values = []
				current_value = ''
				in_quote = False
				quote_char = ''
				i = 0

				while i < len(record_str):
					char = record_str[i]

					# Handle quoted values
					if char in {"'", '"'}:
						if not in_quote:
							in_quote = True
							quote_char = char
						elif in_quote and char == quote_char:
							in_quote = False
						else:
							current_value += char
					elif char == ',' and not in_quote:
						# End of a value
						values.append(current_value.strip(')').strip())
						current_value = ''
					else:
						current_value += char
					i += 1

				# Add the last value
				if current_value:
					values.append(current_value.strip(')').strip())

				# Map values to fields
				record = {}
				for fi, value in enumerate(values):
					if fi < len(tables[table]['fields']):
						record[tables[table]['fields'][fi]] = value
				tables[table]['records'].append(record)

	return tables



def jsonExport(data):
	global database
	# Ensure the input is a dictionary
	if not isinstance(data, dict):
		raise TypeError("Input data should be a dictionary.")

	mysql_dump = [
		{
			"type": "header",
			"version": "5.2.1",
			"comment": "Export as JSON formatted as mysql json export"
		},
		{
			"type": "database",
			"name": database
		}
	]
	
	for table_name, table_data in data.items():
		table_entry = {
			"type": "table",
			"name": table_name,
			"database": database,
			"data": []
		}
		
		# Convert each record in 'records' using the field names in 'fields'
		for record in table_data["records"]:
			record_entry = {field: record.get(field, "") for field in table_data["fields"]}
			table_entry["data"].append(record_entry)
		
		mysql_dump.append(table_entry)
	
	return mysql_dump


def sql2dict_partial_fix_not_used(data):
	dex = __.Meta_Namespace()
	dex.p = _.deX.p(data.upper(), ['INSERT INTO', 'VALUES', 'CREATE TABLE'])
	dex.o = _.deX.o(data)
	dex.c = _.deX.c(data)
	dex.i = _.deX.i(data)
	# for o in dex.i:
	# 	c = dex.i[o]+1
	# 	snip = data[o:c]
	# 	print(snip)
	# _.isExit(__file__)
	dex.ii = []
	dex.ol = {}
	# print(dex.p['ph']['INSERT INTO']); return None
	tables = {}
	for o in dex.p['ph']['INSERT INTO']:
		# while not o in dex.i and not data[o] == '`': o += 1
		# print(data[o])
		o += 1
		while True:
			
			if o > len(data): _.e('out of range')
			if data[o] == '`': break
			elif o in dex.i and data[o:dex.i[o]+1].strip().upper() == 'INTO':pass
			elif o in dex.i and data[o:dex.i[o]+1] == '(': o += 1
			elif data[o] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and o in dex.i: break

			
			o += 1
		c = dex.i[o]+1
		table = data[o:c].strip('`').strip()
		if not table in tables:
			tables[table] = {}
			tables[table]['fields'] = []
			tables[table]['records'] = []
		o = c
		while not data[o] == '(': o += 1
		c = dex.i[o]+1
		end = dex.i[o]+1
		fields = data[o:c].strip('()').strip()
		o +=1
		while not o == end:
			
			if not o in dex.i: o += 1; continue
			c = dex.i[o]+1
			field = data[o:c].strip('`').strip()
			# print(field)
			tables[table]['fields'].append(field)
			o = c
		# newRecord = True
		while not data[o] == '(': o += 1
		while not o >= len(data) and not data[o] == ';':
			if not o in dex.i: o += 1; continue
			# print(o,data[o])
			c = dex.i[o]+1
			# while not data[c] == ')': c += 1
			
			start = o
			end = c
			rec = data[o:c]
			# .strip('()').strip()
			# print(rec)
			o += 1
			record = {}
			fields = []
			while not o == end:
				while not o in dex.i and not o > len(data): o += 1
				if o > len(data):
					break
				c = dex.i[o]+1
				if not data[o] == '`':
					me = data[o:c].strip()
					valid = False
					if '.' in me:
						if me[0] in '0123456789':
							try:
								field = float(me)
								valid = True
							except: pass
					if not valid:
						if me[0] in '0123456789':
							try:
								field = int(me)
							except:
								field = me.strip("'").strip('"').strip()
								if field == 'NULL': field = None
				else:
					field = data[o:c].strip('`').strip("'").strip('"').strip()
				if len(fields) == len(tables[table]['fields']):
					o-= len(field)+1
					# _.pr(data[o],c='cyan')
					# _.pr(field,c='yellow')
					if field in data:
						o = data.index(field)
					break
				fields.append(field)
				o = c
				o += 1
			# _.pv(tables)
			# _.pv(record)
			for i,f in enumerate(fields):
				# print(i,o,len(data),f)
				record[tables[table]['fields'][i]] = f
			if type(record) == dict:
				tables[table]['records'].append(record)
			o = c
			o += 1
			if o > len(data):
				# _.pr(data[start:end],c='red')
				o = dex.i[start]+1
				break

			# tables[table]['records'].append(rec)
		# c = dex.i[o]+1

		# _.pv(tables)
	return tables


def sql2dict(data):
	dex = __.Meta_Namespace()
	dex.p = _.deX.p(data.upper(), ['INSERT INTO', 'VALUES', 'CREATE TABLE'])
	dex.o = _.deX.o(data)
	dex.c = _.deX.c(data)
	dex.i = _.deX.i(data)
	dex.ii = []
	dex.ol = {}
	# print(dex.p['ph']['INSERT INTO']); return None
	tables = {}
	for o in dex.p['ph']['INSERT INTO']:
		# while not o in dex.i and not data[o] == '`': o += 1
		# print(data[o])
		o += 1
		while True:
			
			if o > len(data): _.e('out of range')
			if data[o] == '`': break
			elif o in dex.i and data[o:dex.i[o]+1].strip().upper() == 'INTO':pass
			elif o in dex.i and data[o:dex.i[o]+1] == '(': o += 1
			elif data[o] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and o in dex.i: break

			
			o += 1
		c = dex.i[o]+1
		table = data[o:c].strip('`').strip()
		if not table in tables:
			tables[table] = {}
			tables[table]['fields'] = []
			tables[table]['records'] = []
		o = c
		while not data[o] == '(': o += 1
		c = dex.i[o]+1
		end = dex.i[o]+1
		fields = data[o:c].strip('()').strip()
		o +=1
		while not o == end:
			
			if not o in dex.i: o += 1; continue
			c = dex.i[o]+1
			field = data[o:c].strip('`').strip()
			tables[table]['fields'].append(field)
			o = c

		while not data[o] == '(': o += 1
		while not data[o] == ';' and not o > len(data):
			# print(data[o])
			if not o in dex.i: o += 1; continue
			c = dex.i[o]+1
			end = c
			rec = data[o:c].strip('()').strip()
			# print(rec)
			o += 1
			record = {}
			fields = []
			while not o == end:
				while not o in dex.i and not o > len(data): o += 1
				if o > len(data):
					break
				c = dex.i[o]+1
				if not data[o] == '`':
					me = data[o:c].strip()
					valid = False
					if '.' in me:
						try:
							field = float(me)
							valid = True
						except: pass
					if not valid:
						try:
							field = int(me)
						except:
							field = me.strip("'").strip('"').strip()
							if field == 'NULL': field = None
				else:
					field = data[o:c].strip('`').strip("'").strip('"').strip()
				fields.append(field)
				o = c
				o += 1

			for i,f in enumerate(fields):
				record[tables[table]['fields'][i]] = f
			if type(record) == dict:
				tables[table]['records'].append(record)
			o = c
			o += 1

	return tables
		



def sql2dictRegex(data):
	import re
	tables = {}

	# Regex pattern to match INSERT INTO statements
	insert_pattern = re.compile(
		r"INSERT INTO\s+`?(\w+)`?\s*\((.*?)\)\s*VALUES\s*(.+?);",
		re.IGNORECASE | re.DOTALL
	)

	# Find all matches for the INSERT INTO statements
	matches = insert_pattern.findall(data)
	for table_name, fields, values in matches:
		fields = [f.strip("` ") for f in fields.split(",")]

		# Ensure the table structure is initialized in the dictionary
		if table_name not in tables:
			tables[table_name] = {"fields": fields, "records": []}

		# Combine multi-line values into a single line
		values = re.sub(r"\s*\n\s*", " ", values)

		# Parse records in the VALUES section
		value_sets = re.findall(r"\((.*?)\)", values)
		for value_set in value_sets:
			# Split values, handle quoted strings, and handle NULL
			raw_values = re.split(r",(?=(?:[^']*'[^']*')*[^']*$)", value_set)
			parsed_values = [
				# Strip quotes, preserve backslashes without adding extra escaping
				re.sub(r"\\\\", r"\\", v.strip(" '\"")) if v.strip(" '\"").upper() != "NULL" else None
				for v in raw_values
			]

			# Map values to their corresponding fields
			record = dict(zip(fields, parsed_values))
			tables[table_name]["records"].append(record)

	return tables







database = 'Converted_Database'
def action():
	if _.switches.isActive('Files'):
		data = open(_.switches.value('Files'), encoding='utf-8').read()
	else:
		data = '\n'.join(_.isData(r=0))
	if len(_.FilesFiles):
		global database
		database = _.FilesFiles[0].replace('.sql','').replace('.SQL','')
	# print(_.FilesFiles); _.isExit(__file__)
	if _.switches.isActive('IndexDump') and 'pre' in _.switches.value('IndexDump'):
		index = _.simpleIndex(data)
		_.pv(index)
		for o in index:
			c = index[o]+1
			_.pr( data[o:c] )
		return None
	shouldProcess = True
	if _.switches.isActive('Cache'):
		if __.os.path.isfile(_.switches.values('Cache')[0]):
			shouldProcess = False
			result = _.getTable2(_.switches.values('Cache')[0])
	if shouldProcess:
		if _.switches.isActive('Regex'):
			result = sql2dictRegex(data)
		else:
			try:
				result = sql2dict(data)
			except:
				result = sql2dictRegex(data)
		if _.switches.isActive('Cache'):
			_.saveTable2(result,_.switches.values('Cache')[0])
	# _.pv(result)
	# result = sql(data)
	# _.pv(result)
	if _.switches.isActive('JSON'):
		_.pv(jsonExport(result))
		return None
	if _.switches.isActive('IndexDump') or not _.switches.isActive('Plus'):
		_.pv(result)
		return None
		
	# _.pv(result); return False
	datamine = {
		'field_ids': {},
		'field_counts': {},
		'id_fields': {},
		'search_hits': {},
		'total': 0,
	}
	global RelevantRecords
	RelevantRecords = {}
	for table_name, table in result.items():
		for record in table['records']:
			for f in record:
				first_field = f
				break
			# first_field = next(iter(record))
			# print(type(first_field),type(record))
			record_id = record[first_field]

			for field, value in record.items():
				if _.showLine(value):
					datamine['total'] += 1
					if not table_name in datamine['field_ids']: datamine['field_ids'][table_name] = {}
					if not table_name in datamine['field_counts']: datamine['field_counts'][table_name] = {}
					if not table_name in datamine['id_fields']: datamine['id_fields'][table_name] = {}
					if not table_name in datamine['search_hits']: datamine['search_hits'][table_name] = {}
					# Initialize field-specific structures if needed
					if field not in datamine['field_ids'][table_name]:
						datamine['field_ids'][table_name][field] = []
						datamine['field_counts'][table_name][field] = 0
					datamine['field_counts'][table_name][field] += 1
					datamine['field_ids'][table_name][field].append(record_id)

					# Initialize search hits and ID field mappings
					if record_id not in datamine['id_fields'][table_name]:
						datamine['id_fields'][table_name][record_id] = []
						datamine['search_hits'][table_name][record_id] = {}
					if field not in datamine['id_fields'][table_name][record_id]:
						datamine['id_fields'][table_name][record_id].append(field)
						for plusSearchX in _.switches.values('Plus'):
							plusSearchX = _.ci( plusSearchX )
							for subject in _.caseUnspecificCode( value, plusSearchX ):
								value = value.replace( subject, _.colorThis( subject, 'green', p=0 ) )
								if not table_name in RelevantRecords:
									RelevantRecords[table_name] = {}
								if not record_id in RelevantRecords[table_name]:
									RelevantRecords[table_name][record_id] = record
						datamine['search_hits'][table_name][record_id][field] = value


	def searchResults(datamine):
		for table_name in datamine['search_hits']:
			_.pr(line=1, c='blue')
			_.pr(table_name, c='yellow')
			for id in datamine['search_hits'][table_name]:
				_.pr('  ',id,c='cyan')
				for field in datamine['search_hits'][table_name][id]:
					_.pr('    ',field,c='darkcyan')
					# print(datamine['search_hits'][table_name][id][field])
					print('      ',datamine['search_hits'][table_name][id][field])

		_.pr('\n','',_.addComma(datamine['total']),c='Background.blue')


  
	if _.switches.isActive('DebugDump'):
		if 'r' in _.switches.value('DebugDump'):
			_.pv(RelevantRecords)
		else:
			# Print outputs for debugging and verification
			color = 'Background.green'
			_.pr(line=1, c='green')
			_.pr('Count of Results in a Field by Table',c=color)
			_.pv(datamine['field_counts'])
			_.pr(line=1, c='green')
			_.pr('ID Priority and Fields by Table',c=color)
			_.pv(datamine['id_fields'])
			_.pr(line=1, c='green')
			_.pr('Field Priority and IDs by Table',c=color)
			_.pv(datamine['field_ids'])
			_.pr(line=1, c='green')
			_.pr('Search Results by Table ID and Field',c=color)
			# _.pv(datamine['search_hits'])
			searchResults(datamine)
			_.pr(line=1, c='green')

	# import simplejson
	# print( simplejson.dumps(datamine['search_hits'], indent=4) )
	elif _.switches.isActive('ShowSearchResults'):
		searchResults(datamine)
	else:
		_.pv(datamine['id_fields'])


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);