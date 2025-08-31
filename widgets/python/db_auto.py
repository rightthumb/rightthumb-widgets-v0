import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Database', '-db' )
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

import os
import simplejson
import sqlite3

def get_sqlite_type(value):
	if isinstance(value, int):
		return 'INTEGER'
	elif isinstance(value, float):
		return 'REAL'
	elif isinstance(value, bool):
		return 'INTEGER'
	else:
		return 'TEXT'


def action(packages=None):
	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
	else:
		db = _.UUID_Epoch2() + '.db'

	# packages = os.getenv('packages') # Simulating PHP's $_REQUEST['packages']
	
	if packages is None:
		raise Exception("Package data not provided.")
	
	database_name = db
	database_dir = _v.myDatabases
	database_file = os.path.join(database_dir, f"{database_name}.db")
	key_file = os.path.join(database_dir, f"{database_name}.json")
	
	if not os.path.exists(database_dir):
		os.makedirs(database_dir, 0o777)
	
	# File existence check for the database file
	if not os.path.exists(database_file):
		conn = sqlite3.connect(database_file)
		cursor = conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS form_data (id INTEGER PRIMARY KEY AUTOINCREMENT)')
		conn.commit()
	else:
		conn = sqlite3.connect(database_file)
		cursor = conn.cursor()
	
	for package in packages:
		original_data = simplejson.loads(package)
		
		data = {}
		key_handler = {}
		for key, value in original_data.items():
			safe_key = key.replace('-', '_').replace(' ', '_')
			key_handler[safe_key] = key
			data[safe_key] = value
		
		# with open(key_file, 'w') as kf:
			# simplejson.dump(key_handler, kf)
		
		# Check each key in the data and add columns if necessary
		cursor.execute('PRAGMA table_info(form_data)')
		columns = [column[1] for column in cursor.fetchall()]
		
		for key, value in data.items():
			key_escaped = key.replace('"', '""')  # Escape double quotes
			if key_escaped not in columns:
				alter_sql = f'ALTER TABLE form_data ADD COLUMN "{key_escaped}" {get_sqlite_type(value)}'
				cursor.execute(alter_sql)
		
		# Inserting the data
		insert_columns = ['"{}"'.format(key.replace('"', '""')) for key in data.keys()]
		insert_values = [':{}'.format(key) for key in data.keys()]
		insert_sql = 'INSERT INTO form_data ({}) VALUES ({})'.format(", ".join(insert_columns), ", ".join(insert_values))
		
		cursor.execute(insert_sql, data)
		conn.commit()
	
	conn.close()
	
	print("Form data processed successfully.")


########################################################################################
if __name__ == '__main__':
	_.isExit(__file__)
