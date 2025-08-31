import psycopg2
import psycopg2.extras

class postgresMgr:
    def __init__(self, host, dbname, user, password, port=5432):
        self.logs = ['fn: __init__']
        self.logs.append(f'Connecting to {dbname}@{host}:{port}')
        self.conn = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        self.structure = False
        
    def sql(self, sql, params=None, fetch=False):
        """
        Execute arbitrary SQL commands, optionally with parameters.
        Set fetch=True to return results (e.g., for SELECT queries).

        Examples:
            # Create a table
            db.sql('CREATE TABLE IF NOT EXISTS demo_table (id SERIAL PRIMARY KEY, name TEXT)')

            # Insert
            db.sql('INSERT INTO demo_table (name) VALUES (%s)', ('Alice',))

            # Read
            rows = db.sql('SELECT * FROM demo_table', fetch=True)

            # Alter table
            db.sql('ALTER TABLE demo_table ADD COLUMN age INT')
        """
        self.logs.append('fn: sql')
        self.logs.append(f'Executing SQL: {sql}')
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            if fetch:
                results = self.cursor.fetchall()
                self.logs.append(f'Fetched {len(results)} records.')
                return results
            else:
                self.conn.commit()
                self.logs.append('Executed successfully.')
        except psycopg2.Error as e:
            self.logs.append(f'Error executing SQL: {type(e).__name__}: {e}')
            return None




        def insert(self, table_name, records):
        self.logs.append('fn: insert')
        if not self.structure:
            self.structureMgr(table_name, records)
        for record in records:
            columns = list(record.keys())
            values = list(record.values())
            placeholders = ', '.join(['%s'] * len(columns))
            insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({placeholders})'
            try:
                self.cursor.execute(insert_sql, values)
                self.conn.commit()
                self.logs.append(f'Inserted record into {table_name}')
            except Exception as e:
                self.logs.append(f'Insert error: {e}')

    def read(self, table_name, conditions={}):
        self.logs.append('fn: read')
        if conditions and not self.structure:
            self.structureMgr(table_name, [conditions])
        where_clause = ''
        values = []
        if conditions:
            where_clause = 'WHERE ' + ' AND '.join([f"{key} = %s" for key in conditions])
            values = list(conditions.values())
        sql = f'SELECT * FROM {table_name} {where_clause}'
        try:
            self.cursor.execute(sql, values)
            results = self.cursor.fetchall()
            self.logs.append(f'Read {len(results)} records from {table_name}')
            return results
        except Exception as e:
            self.logs.append(f'Read error: {e}')
            return []

    def delete(self, table_name, conditions):
        self.logs.append('fn: delete')
        if not self.structure:
            self.structureMgr(table_name, [conditions])
        where_clause = ' AND '.join([f"{key} = %s" for key in conditions])
        values = list(conditions.values())
        sql = f'DELETE FROM {table_name} WHERE {where_clause}'
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            self.logs.append(f'Deleted from {table_name}')
        except Exception as e:
            self.logs.append(f'Delete error: {e}')

    def update_or_insert(self, table_name, conditions, record):
        self.logs.append('fn: update_or_insert')
        if not self.structure:
            self.structureMgr(table_name, [record, conditions])
        results = self.read(table_name, conditions)
        if results:
            try:
                set_clause = ', '.join([f"{key} = %s" for key in record])
                where_clause = ' AND '.join([f"{key} = %s" for key in conditions])
                sql = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'
                self.cursor.execute(sql, list(record.values()) + list(conditions.values()))
                self.conn.commit()
                self.logs.append(f'Updated record in {table_name}')
            except Exception as e:
                self.logs.append(f'Update error: {e}')
        else:
            self.insert(table_name, [record])

    def structureMgr(self, table_name, records):
        self.logs.append('fn: structureMgr')
        try:
            self.createTable(table_name, records)
            self.ensure_columns_exist(table_name, records)
            self.structure = True
        except Exception as e:
            self.logs.append(f'Structure error: {e}')

    def createTable(self, table_name, records):
        self.cursor.execute(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)",
            (table_name,)
        )
        if not self.cursor.fetchone()['exists']:
            fields = {}
            for record in records:
                for key, val in record.items():
                    fields[key] = self.get_pg_type(val)
            cols = ', '.join([f'"{k}" {v}' for k, v in fields.items()])
            sql = f'CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, {cols})'
            self.cursor.execute(sql)
            self.conn.commit()
            self.logs.append(f'Created table {table_name}')

    def ensure_columns_exist(self, table_name, records):
        self.cursor.execute("""
            SELECT column_name FROM information_schema.columns
            WHERE table_name = %s
        """, (table_name,))
        existing = [row['column_name'] for row in self.cursor.fetchall()]
        for record in records:
            for key, val in record.items():
                if key not in existing:
                    try:
                        self.cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN "{key}" {self.get_pg_type(val)}')
                        self.conn.commit()
                        self.logs.append(f'Added column {key}')
                    except Exception as e:
                        self.logs.append(f'Add column error: {e}')

    def get_pg_type(self, val):
        if isinstance(val, int):
            return 'INTEGER'
        elif isinstance(val, float):
            return 'REAL'
        elif isinstance(val, bool):
            return 'BOOLEAN'
        elif isinstance(val, (dict, list)):
            return 'JSONB'
        else:
            return 'TEXT'

    def fields(self, table_name):
        self.cursor.execute("""
            SELECT column_name FROM information_schema.columns
            WHERE table_name = %s
        """, (table_name,))
        return [row['column_name'] for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()
        self.logs.append('Database connection closed.')


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

db=postgresMgr

'''
db = postgresMgr(
    host='localhost',
    dbname='mydb',
    user='myuser',
    password='mypassword'
)

record = {'name': 'Alice', 'email': 'alice@example.com'}
db.update_or_insert('users', {'name': 'Alice'}, record)
db.close()

'''