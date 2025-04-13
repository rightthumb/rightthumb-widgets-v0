import duckdb
import json

class duckdbMgr:
    def __init__(self, database):
        self.logs = ['fn: __init__']
        self.logs.append(f'init: {database}')
        self.database_name = database
        self.conn = duckdb.connect(database)
        self.cursor = self.conn.cursor()
        self.structure = False

    def insert(self, table_name, records):
        self.logs.append('fn: insert')
        if not self.structure:
            self.structureMgr(table_name, records)
        
        for record in records:
            columns = [f'"{col}"' for col in record.keys()]
            placeholders = [f'${i+1}' for i in range(len(record))]
            insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
            try:
                self.cursor.execute(insert_sql, tuple(record.values()))
                self.logs.append(f'Inserted record into table {table_name}')
            except Exception as e:
                self.logs.append(f'Error: {str(e)}')

    def read(self, table_name, conditions={}):
        self.logs.append('fn: read')
        if conditions and not self.structure:
            self.structureMgr(table_name, [conditions])

        where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
        select_sql = f'SELECT * FROM {table_name} {where_sql}'

        try:
            self.cursor.execute(select_sql, tuple(conditions.values()))
            columns = [desc[0] for desc in self.cursor.description]
            results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            self.logs.append(f'Read {len(results)} records from table {table_name}')
            return results
        except Exception as e:
            self.logs.append(f'Error: {str(e)}')
            return []


    def delete(self, table_name, conditions):
        self.logs.append('fn: delete')
        where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
        delete_sql = f'DELETE FROM {table_name} {where_sql}'
        try:
            self.cursor.execute(delete_sql, tuple(conditions.values()))
            self.logs.append(f'Deleted {self.cursor.rowcount} records from {table_name}')
        except Exception as e:
            self.logs.append(f'Error deleting from {table_name}: {str(e)}')

    def update_or_insert(self, table_name, conditions, record):
        self.logs.append('fn: update_or_insert')
        if not self.structure:
            self.structureMgr(table_name, [record, conditions])

        existing = self.read(table_name, conditions)
        if existing:
            try:
                set_clause = ', '.join(f'"{k}" = ?' for k in record.keys())
                where_clause = ' AND '.join(f'"{k}" = ?' for k in conditions.keys())
                sql = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'
                self.cursor.execute(sql, tuple(record.values()) + tuple(conditions.values()))
                self.logs.append(f'Updated record in table {table_name}')
            except Exception as e:
                self.logs.append(f'Error updating: {str(e)}')
        else:
            try:
                self.insert(table_name, [record])
                self.logs.append(f'Inserted record into table {table_name}')
            except Exception as e:
                self.logs.append(f'Error inserting: {str(e)}')

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
        self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name = ?", (table_name,))
        exists = self.cursor.fetchone()

        if not exists:
            fields = {}
            for record in records:
                if isinstance(record, dict):
                    for key, value in record.items():
                        fields[key] = self.get_type(value)
            columns_sql = ', '.join(f'"{k}" {v}' for k, v in fields.items())
            sql = f'CREATE TABLE {table_name} ({columns_sql})'
            self.cursor.execute(sql)
            self.logs.append(f'Table created: {table_name}')

    def ensure_columns_exist(self, table_name, records):
        self.logs.append('fn: ensure_columns_exist')
        current_fields = self.fields(table_name)
        for record in records:
            for key, val in record.items():
                if key not in current_fields:
                    try:
                        self.cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN "{key}" {self.get_type(val)}')
                        self.logs.append(f'Added column {key}')
                    except Exception as e:
                        self.logs.append(f'Error adding column {key}: {str(e)}')

    def fields(self, table_name):
        self.logs.append('fn: fields')
        try:
            self.cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = ?", (table_name,))
            return [row[0] for row in self.cursor.fetchall()]
        except Exception as e:
            self.logs.append(f'Error retrieving fields: {str(e)}')
            return []

    def get_type(self, val):
        if isinstance(val, int):
            return 'INTEGER'
        elif isinstance(val, float):
            return 'DOUBLE'
        elif isinstance(val, bool):
            return 'BOOLEAN'
        elif isinstance(val, (dict, list)):
            return 'VARCHAR'
        else:
            return 'VARCHAR'

    def close(self):
        self.conn.close()
        self.logs.append('Database closed.')

    def ensureTable(self, table, sql):
        self.logs.append('fn: ensureTable')
        try:
            self.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_name = ?", (table,))
            if not self.cursor.fetchone():
                self.cursor.execute(sql)
                self.logs.append(f'Table ensured: {table}')
        except Exception as e:
            self.logs.append(f'Error ensuring table: {str(e)}')



    def r(self, table_name, conditions={}):
        return self.read(table_name, conditions)

    def get(self, table_name, conditions={}):
        return self.read(table_name, conditions)


    def create(self, table_name, record):
        return self.insert(table_name, record)

    def c(self, table_name, record):
        return self.insert(table_name, record)


    def i(self, table_name, record):
        return self.insert(table_name, record)

    def ui(self, table_name, conditions, record):
        return self.update_or_insert(table_name, conditions, record)


    def d(self, table_name, conditions={}):
        return self.delete(table_name, conditions)

duck = duckdbMgr
db = duckdbMgr
