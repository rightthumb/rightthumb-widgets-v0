import sqlite3
import json

class MySQLTableManager:
    def __init__(self, credentials):
        self.logs = ['fn: __init__']
        self.logs.append(f"init: {credentials['db']}")
        self.database_name = credentials['db']
        self.conn = sqlite3.connect(credentials['db'])
        self.cursor = self.conn.cursor()

    def insert(self, table_name, records):
        self.logs.append('fn: insert')
        self.logs.append(f'Table: {table_name} Records: {len(records)}')
        self.ensure_table_exists(table_name, records)
        self.ensure_columns_exist(table_name, records)
        
        for record in records:
            columns = ', '.join([f'`{key}`' for key in record.keys()])
            placeholders = ', '.join([f':{key}' for key in record.keys()])
            insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            try:
                self.cursor.execute(insert_sql, record)
                self.conn.commit()
                self.logs.append(f"Inserted record into table {table_name}")
            except sqlite3.Error as e:
                self.logs.append(f"Error: {e}")

    def read(self, table_name, conditions=None):
        self.logs.append('fn: read')
        self.logs.append(f"Reading from table: {table_name}")
        conditions = conditions or {}
        
        where_clauses = ' AND '.join([f'`{key}` = :{key}' for key in conditions.keys()])
        where_sql = f"WHERE {where_clauses}" if conditions else ''
        select_sql = f"SELECT * FROM {table_name} {where_sql}"
        
        try:
            self.cursor.execute(select_sql, conditions)
            results = self.cursor.fetchall()
            self.logs.append(f"Read {len(results)} records from table {table_name}")
            return results
        except sqlite3.Error as e:
            self.logs.append(f"Error: {e}")
            return []

    def delete(self, table_name, conditions=None):
        self.logs.append('fn: delete')
        self.logs.append(f"Deleting from table: {table_name}")
        conditions = conditions or {}
        
        where_clauses = ' AND '.join([f'`{key}` = :{key}' for key in conditions.keys()])
        where_sql = f"WHERE {where_clauses}" if conditions else ''
        delete_sql = f"DELETE FROM {table_name} {where_sql}"
        
        try:
            self.cursor.execute(delete_sql, conditions)
            self.conn.commit()
            self.logs.append(f"Deleted records from table {table_name}")
        except sqlite3.Error as e:
            self.logs.append(f"Error: {e}")

    def ensure_table_exists(self, table_name, records):
        self.logs.append('fn: ensureTableExists')
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = self.cursor.fetchone()

        if not table_exists:
            column_definitions = {key: self.get_sqlite_type(value) for record in records for key, value in record.items()}
            column_definitions_sql = ', '.join([f'`{col}` {dtype}' for col, dtype in column_definitions.items()])
            sql = f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {column_definitions_sql})"
            self.cursor.execute(sql)
            self.conn.commit()
            self.logs.append(f"Table created: {table_name}")

    def get_sqlite_type(self, value):
        self.logs.append('fn: getSQLiteType')
        if isinstance(value, int):
            return 'INTEGER'
        elif isinstance(value, float):
            return 'REAL'
        elif isinstance(value, bool):
            return 'BOOLEAN'
        else:
            return 'TEXT'

    def ensure_columns_exist(self, table_name, records):
        self.logs.append('fn: ensureColumnsExist')
        existing_columns = [col['name'] for col in self.fields(table_name)]
        
        for record in records:
            for key, value in record.items():
                if key not in existing_columns:
                    alter_sql = f"ALTER TABLE {table_name} ADD COLUMN `{key}` {self.get_sqlite_type(value)}"
                    try:
                        self.cursor.execute(alter_sql)
                        self.conn.commit()
                        self.logs.append(f"Field added: {key}")
                    except sqlite3.Error as e:
                        self.logs.append(f"Error adding column: {e}")

    def fields(self, table_name):
        self.logs.append('fn: fields')
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        return self.cursor.fetchall()

    def tables(self):
        self.logs.append('fn: tables')
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in self.cursor.fetchall()]
        return json.dumps({'success': True, 'tables': tables}, indent=4)

    def get_database_name(self):
        self.logs.append('fn: getDatabaseName')
        return self.database_name

# Example Usage:
# credentials = {'db': 'test.db'}
# db_manager = MySQLTableManager(credentials)
# db_manager.insert('users', [{'name': 'John Doe', 'email': 'john@example.com'}])
# records = db_manager.read('users', {'name': 'John Doe'})
# db_manager.delete('users', {'id': 123})
# fields = db_manager.fields('users')
# tables = db_manager.tables()
# db_name = db_manager.get_database_name()
