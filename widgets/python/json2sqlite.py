import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=True )
	_.switches.register( 'DB', '-db', isRequired=True )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'json2sqlite.py',
	'description': 'Convert json to sqlite. mysql json dump or ` p sql -f mysql_dump.sql -json > mysql_dump.json `',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p json2sqlite -file file.txt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

########################################################################################
#n)--> start

import json
import sqlite3

def json_to_sqlite(json_data, output_sqlite_file):
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

def action():
    with open(_.switches.value('Files'), "r") as f:
        json_data = json.load(f)
    json_to_sqlite(json_data, _.switches.value('DB'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);