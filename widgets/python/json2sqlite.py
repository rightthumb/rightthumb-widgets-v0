import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'DB', '-db', isRequired=True )
	# _.switches.register( 'JSON', '-json', isRequired=False )
	_.switches.register( 'LS', '-ls', 'p ls -cache', isRequired=False )
_._default_settings_()

__.setting('require-list',['Pipe','Files'])

_.appInfo[focus()] = {
	'file': 'json2sqlite.py',
	'description': 'Convert json to sqlite. mysql json dump or ` p sql -f mysql_dump.sql -json > mysql_dump.json `',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p sql -f tpn_wp.sql -json > tpn_wp.sql.json'),
						_.hp('p json2sqlite -f tpn_wp.sql.json | sqlite3 tpn_wp.db'),
						_.hp(''),
						_.hp('p sqlite2json -f tpn_wp.db'),
						_.hp('p json2sqlite -f tpn_wp_export.json | sqlite3 tpn_wp_clone.db'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': ['json2sqlite','sqlite2json','sql'],
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

########################################################################################
#n)--> start

import json
import sqlite3

def json_to_sqlite(json_data, output_sqlite_file):
	print('json_to_sqlite:',json_data)
	conn = sqlite3.connect(output_sqlite_file)
	cursor = conn.cursor()
	for item in json_data:
		if item["type"] == "table":
			table_name = item["name"]
			columns = []
			data_rows = []
			for row in item.get("data", []):
				if not columns:
					columns = row.keys()
				data_rows.append(tuple(row.values()))
			# print(columns)
			if columns:
				columns_sql = ", ".join([f"{col} TEXT" for col in columns])
				cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")
				if data_rows:
					placeholders = ", ".join(["?"] * len(columns))
					try:
						cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data_rows)
					except Exception as e:
						_.pr(e,c='red')
						# print(f"INSERT INTO {table_name} VALUES ({placeholders})")
						
					

	conn.commit()
	conn.close()

def p_ls_cache(json_data):
		lsData = []
		for rec in json_data['data']:
			del rec['stat']
			del rec['group']
			del rec['type']
			del rec['name_']
			del rec['typesort']
			del rec['friendly_week']
			del rec['friendly_month']
			del rec['md5']
			del rec['sha256']
			del rec['header']
			del rec['error']
			del rec['date_created_raw']
			del rec['date_modified_raw']
			del rec['date_created']
			del rec['date_modified']
			del rec['accessed_raw']
			del rec['date_accessed']
			del rec['week_of_year']
			del rec['week_of_year_']
			del rec['day_of_the_week']
			del rec['month']
			del rec['ago']
			del rec['meta']
			if len(list(rec.keys())) == 10:
				lsData.append(rec)
		data = [
			{
				"type": "header",
				"version": "5.2.1",
				"comment": "Export as JSON formatted as mysql json export"
			},
			{
				"type": "database",
				"name": "FilesDatabase"
			},
			{
				"type": "table",
				"name": "files",
				"database": "FilesDatabase",
				"data": lsData
			}
		]
		_.saveTable2(data,'ls.json')

def action():
	if _.switches.isActive('Files'):
		fi = _.switches.values('Files')[0]
		# if _.isWin:
		# 	json_file = open(fi, 'r', encoding='utf-8')
		# else:
		# 	json_file = open(fi, 'r')
		# json_data = json.load(json_file)
		json_data = _.getTable2(_.switches.values('Files')[0])
	else:
		try:
			json_data = json.loads('\n'.join(_.isData(r=1)))
		except:
			json_data = json.loads('[\n'+'\n'.join(_.isData(r=1)))

	if _.switches.isActive('LS'): json_data = p_ls_cache(json_data)
	json_to_sqlite(json_data, _.switches.value('DB'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);