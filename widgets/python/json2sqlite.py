import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'DB', '-db', isRequired=True )
	_.switches.register( 'JSON', '-json', isRequired=False )
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

def json_to_sqlite1(json_data, output_sqlite_file):
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
            if columns:
                columns_sql = ", ".join([f"{col} TEXT" for col in columns])
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")
                if data_rows:
                    placeholders = ", ".join(["?"] * len(columns))
                    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data_rows)
    conn.commit()
    conn.close()

def json_to_sqlite2(json_data, output_sqlite_file):
    conn = sqlite3.connect(output_sqlite_file)
    cursor = conn.cursor()

    for item in json_data:
        if item["type"] == "table":
            table_name = item["name"]
            columns = []
            data_rows = []

            for row in item.get("data", []):
                # Ensure the columns are initialized only once
                if not columns:
                    columns = list(row.keys())
                # Align row values to match the column order
                aligned_row = tuple(row.get(col, None) for col in columns)
                data_rows.append(aligned_row)

            if columns:
                # Create table if it doesn't exist
                columns_sql = ", ".join([f"{col} TEXT" for col in columns])
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})")

                if data_rows:
                    placeholders = ", ".join(["?"] * len(columns))
                    try:
                        cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data_rows)
                    except sqlite3.ProgrammingError as e:
                        print(f"Error inserting into table {table_name}: {e}")
                        print(f"Columns: {columns}")
                        print(f"Data Rows: {data_rows}")
                        raise

    conn.commit()
    conn.close()
def action():
    try:
        json_data = json.loads('\n'.join(_.isData(r=1)))
    except:
        json_data = json.loads('[\n'+'\n'.join(_.isData(r=1)))
    # try:
    #     json_to_sqlite1(json_data, _.switches.value('DB'))
    # except:
    json_to_sqlite2(json_data, _.switches.value('DB'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);