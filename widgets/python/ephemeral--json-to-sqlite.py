#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] },
		},
	}


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def action(): pass

import simplejson
import sqlite3

def clean_field_names(field_names):
	"""
	Clean field names by removing any non-alphanumeric characters and converting to lowercase.

	Args:
		field_names (list of str): The original field names.

	Returns:
		list of str: The cleaned field names.
	"""
	cleaned_names = []
	for field_name in field_names:
		cleaned_name = ''.join(char for char in field_name if char.isalnum()).lower()
		cleaned_names.append(cleaned_name)
	return cleaned_names

def determine_column_types(sample_data):
	"""
	Determine the data types of each column based on a sample of data.

	Args:
		sample_data (list of dict): A sample of data from the JSON file.

	Returns:
		list of str: The data types of each column.
	"""
	column_types = []
	for field_name in sample_data[0].keys():
		column_type = None
		for row in sample_data:
			if isinstance(row[field_name], (int, float)):
				column_type = 'REAL'
				break
			elif isinstance(row[field_name], str):
				column_type = 'TEXT'
		if column_type is None:
			column_type = 'TEXT'
		column_types.append(column_type)
	return column_types

def create_sqlite_table(table_name, field_names, column_types):
	"""
	Create a SQLite table with the specified name, field names, and column types.

	Args:
		table_name (str): The name of the table to create.
		field_names (list of str): The cleaned field names.
		column_types (list of str): The data types of each column.
	"""
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	column_names = ','.join(field_names)
	column_defs = ','.join([f'{name} {column_types[i]}' for i, name in enumerate(field_names)])
	create_table_query = f'CREATE TABLE {table_name} ({column_defs})'
	c.execute(create_table_query)
	conn.commit()
	conn.close()

def import_json_data(table_name, filename):
	"""
	Import data from a JSON file into a SQLite table.

	Args:
		table_name (str): The name of the table to import the data into.
		filename (str): The name of the JSON file to import data from.
	"""
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	with open(filename) as f:
		data = simplejson.load(f)
		for row in data:
			values = [row[field_name] for field_name in cleaned_headers]
			insert_query = f'INSERT INTO {table_name} VALUES ({",".join(["?" for _ in range(len(values))])})'
			c.execute(insert_query, values)
	conn.commit()
	conn.close()

# Read the JSON file and extract the first 5 records
with open('example.json') as f:
	data = simplejson.load(f)
	sample_data = data[:5]

# Clean the field names
cleaned_headers = clean_field_names(sample_data[0].keys())

# Determine the data types of each column
column_types = determine_column_types(sample_data)

# Create the SQLite table
table_name = 'example_table'
create_sqlite_table(table_name, cleaned_headers, column_types)

# Import data from the JSON file into the SQLite table
import_json_data(table_name, 'example.json')




##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

