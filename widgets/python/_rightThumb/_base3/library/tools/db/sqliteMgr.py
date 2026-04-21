import sqlite3
import json

class sqliteMgr:
    def __init__(self, database):
        self.logs = ['fn: __init__']
        self.logs.append(f'init: {database}')
        self.database_name = database
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.structure = False

    def insert(self, table_name, records):
        self.logs.append('fn: insert')
        if not self.structure:
            self.structureMgr(table_name, records)
        
        for record in records:
            columns = [f'"{col}"' for col in record.keys()]
            placeholders = [f':{col}' for col in record.keys()]
            insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
            try:
                self.cursor.execute(insert_sql, record)
                self.conn.commit()
                self.logs.append(f'Inserted record into table {table_name}')
            except sqlite3.Error as e:
                self.logs.append(f'Error: {str(e)}')
    def read(self, table_name, conditions={}):
        self.logs.append('fn: read')
        self.logs.append(f'Reading from table: {table_name}')
        
        where_clauses = [f'"{key}" = :{key}' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
        select_sql = f'SELECT * FROM {table_name} {where_sql}'
        
        try:
            self.cursor.execute(select_sql, conditions)
            results = [dict(row) for row in self.cursor.fetchall()]
            self.logs.append(f'Read {len(results)} records from table {table_name}')
            return results
        except sqlite3.Error as e:
            self.logs.append(f'Error: {str(e)}')
            return []

    def update_or_insert(self, table_name, conditions, record, info):
        self.logs.append('fn: update_or_insert')
        existing_records = self.read(table_name, conditions)
        
        if existing_records:
            try:
                set_clauses = [f'"{key}" = :{key}' for key in record.keys()]
                where_clauses = [f'"{key}" = :where_{key}' for key in conditions.keys()]
                update_sql = f'UPDATE {table_name} SET {", ".join(set_clauses)} WHERE {" AND ".join(where_clauses)}'
                params = {**record, **{f'where_{k}': v for k, v in conditions.items()}}
                self.cursor.execute(update_sql, params)
                self.conn.commit()
                info['updated'] += 1
                info['success'] += 1
                self.logs.append(f'Updated: {table_name}')
            except sqlite3.Error as e:
                self.logs.append(f'Error updating record for: {table_name} - {str(e)}')
                info['failed'] += 1
                info['failed-updating'] += 1
        else:
            try:
                self.insert(table_name, [record])
                info['inserted'] += 1
                self.logs.append(f'Inserted: {table_name}')
            except sqlite3.Error as e:
                self.logs.append(f'Error inserting record for: {table_name} - {str(e)}')
                info['failed'] += 1
                info['failed-inserting'] += 1
    def structureMgr(self, table_name, records):
        self.logs.append('fn: structureMgr')
        try:
            self.createTable(table_name, records)
            self.ensure_columns_exist(table_name, records)
            self.structure = True
        except Exception as e:
            self.logs.append(f'Error in structureMgr: {str(e)}')
    
    def createTable(self, table_name, records):
        self.logs.append('fn: createTable')
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        table_exists = self.cursor.fetchone()
        
        if not table_exists:
            try:
                column_definitions = {key: self.get_sqlite_type(value) for record in records if isinstance(record, dict) for key, value in record.items()}
                columns_sql = ', '.join(f'"{col}" {dtype}' for col, dtype in column_definitions.items())
                create_sql = f'CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns_sql})'
                self.cursor.execute(create_sql)
                self.conn.commit()
                self.logs.append(f'Table created: {table_name}')
            except Exception as e:
                self.logs.append(f'Error creating table: {str(e)}')

    def ensure_columns_exist(self, table_name, records):
        self.logs.append('fn: ensure_columns_exist')
        existing_fields = self.fields(table_name)
        
        for record in records:
            if isinstance(record, dict):
                for key, value in record.items():
                    if key not in existing_fields:
                        alter_sql = f'ALTER TABLE {table_name} ADD COLUMN "{key}" {self.get_sqlite_type(value)}'
                        try:
                            self.cursor.execute(alter_sql)
                            self.conn.commit()
                            self.logs.append(f'Field added: {key}')
                        except sqlite3.Error as e:
                            self.logs.append(f'Error adding column: {str(e)}')

    def get_sqlite_type(self, value):
        if isinstance(value, int):
            return 'INTEGER'
        elif isinstance(value, float):
            return 'REAL'
        elif isinstance(value, bool):
            return 'INTEGER'
        elif isinstance(value, (dict, list)):
            return 'TEXT'
        else:
            return 'TEXT'
    def fields(self, table_name):
        self.logs.append('fn: fields')
        try:
            self.cursor.execute(f'PRAGMA table_info({table_name})')
            return [row['name'] for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            self.logs.append(f'Error retrieving fields for {table_name}: {str(e)}')
            return []
    def close(self):
        self.conn.close()
        self.logs.append('Database connection closed.')


'''
# Example usage

# Initialize the database
db = SQLiteTableManager('path/to/database.db')

# Example info dictionary to track results
info = {'updated': 0, 'success': 0, 'failed': 0, 'failed-updating': 0, 'inserted': 0, 'failed-inserting': 0}

# Example record
record = {'name': 'John Doe', 'email': 'john@example.com'}
conditions = {'name': 'John Doe'}

# Use update_or_insert
db.update_or_insert('users', conditions, record, info)

# Print results
print("Operation Summary:", info)

# Close the database connection
db.close()

'''