import mysql.connector

class mysqlMgr:
	def __init__(self, host, database, user, password, port=3306):
		self.logs = ['fn: __init__']
		self.logs.append(f'Connecting to {database}@{host}:{port}')
		self.conn = mysql.connector.connect(
			host=host,
			database=database,
			user=user,
			password=password,
			port=port
		)
		self.cursor = self.conn.cursor(dictionary=True)
		self.structure = False

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
				self.logs.append(f'Inserted into {table_name}')
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
			return self.cursor.fetchall()
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
		exists = self.read(table_name, conditions)
		if exists:
			try:
				set_clause = ', '.join([f"{key} = %s" for key in record])
				where_clause = ' AND '.join([f"{key} = %s" for key in conditions])
				sql = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'
				self.cursor.execute(sql, list(record.values()) + list(conditions.values()))
				self.conn.commit()
				self.logs.append(f'Updated {table_name}')
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
		self.cursor.execute("SHOW TABLES LIKE %s", (table_name,))
		if not self.cursor.fetchone():
			fields = {}
			for record in records:
				for key, val in record.items():
					fields[key] = self.get_mysql_type(val)
			columns = ', '.join([f'`{k}` {v}' for k, v in fields.items()])
			sql = f'CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {columns})'
			self.cursor.execute(sql)
			self.conn.commit()
			self.logs.append(f'Created table {table_name}')

	def ensure_columns_exist(self, table_name, records):
		self.cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
		existing = [row['Field'] for row in self.cursor.fetchall()]
		for record in records:
			for key, val in record.items():
				if key not in existing:
					try:
						sql = f'ALTER TABLE `{table_name}` ADD COLUMN `{key}` {self.get_mysql_type(val)}'
						self.cursor.execute(sql)
						self.conn.commit()
						self.logs.append(f'Added column {key}')
					except Exception as e:
						self.logs.append(f'Add column error: {e}')

	def get_mysql_type(self, val):
		if isinstance(val, int):
			return 'INT'
		elif isinstance(val, float):
			return 'DOUBLE'
		elif isinstance(val, bool):
			return 'TINYINT(1)'
		elif isinstance(val, (dict, list)):
			return 'TEXT'
		else:
			return 'TEXT'

	def fields(self, table_name):
		self.cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
		return [row['Field'] for row in self.cursor.fetchall()]

	def close(self):
		self.conn.close()
		self.logs.append('Connection closed.')




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

db=mysqlMgr

'''
db = mysqlMgr(
	host='localhost',
	database='mydb',
	user='myuser',
	password='mypassword'
)

record = {'username': 'john', 'email': 'john@example.com'}
db.update_or_insert('users', {'username': 'john'}, record)
db.close()

'''