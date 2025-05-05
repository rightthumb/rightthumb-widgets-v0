import duckdb # type: ignore
import sys
import threading
import time
# import json
class duckdbMgr:
	def __init__(self, database):
		self.logs = ['fn: __init__']
		self.logs.append(f'init: {database}')
		self.database_name = database
		self.conn = duckdb.connect(database)
		self.cursor = self.conn.cursor()
		self.structure = False
		self.table_structure = {}






		# New Threaded Streaming
		self.threadData = {}         # { table: { 'a': [], 'b': [] } }
		self.activeSuffix = {}       # { table: 'a' or 'b' }
		self.processingThread = {}   # { table: Thread }
		self.monitorThread = {}      # { table: Thread }
		self.threadLock = threading.Lock()
		self.threadTimeoutSeconds = {}  # { table: int }


	def safe_log_sql(self, sql, params=None):
		"""Safely log SQL + params without messing up execution."""
		if params:
			param_str = ', '.join(repr(p) for p in params)
			self.logs.append(f'{sql} | PARAMS: {param_str}')
		else:
			self.logs.append(f'SQL: {sql}')

	def insert(self, table_name, records):
		self.logs.append('fn: insert')
		if not records:
			return
		sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = ?"
		params = (table_name,)
		self.safe_log_sql(sql, params)
		self.cursor.execute(sql, params)
		exists = self.cursor.fetchone()[0] > 0

		if not exists:
			self.createTable(table_name, records)

		self.ensure_columns_exist(table_name, records)

		for record in records:
			columns = [f'"{col}"' for col in record.keys()]
			placeholders = [f'${i+1}' for i in range(len(record))]
			insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
			params = tuple(record.values())
			self.safe_log_sql(insert_sql, params)
			try:
				self.cursor.execute(insert_sql, params)
				self.logs.append(f'Inserted record into table {table_name}')
			except Exception as e:
				self.logs.append(f'Error inserting: {str(e)}')





	def read(self, table_name, conditions={}):
		self.logs.append('fn: read')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)
		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]
			results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
			self.logs.append(f'Read {len(results)} records from table {table_name}')
			return results
		except Exception as e:
			self.logs.append(f'Error: {str(e)}')
			return []

	def query(self, sql):
		self.logs.append('fn: query')
		self.logs.append(sql)
		try:
			self.cursor.execute(sql)
			columns = [desc[0] for desc in self.cursor.description]
			results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
			self.logs.append(f'Read {len(results)} records')
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

		where_clause = ' AND '.join(f'"{k}" = ?' for k in conditions.keys())
		set_clause = ', '.join(f'"{k}" = ?' for k in record.keys())

		select_sql = f'SELECT 1 FROM {table_name} WHERE {where_clause} LIMIT 1'
		self.safe_log_sql(select_sql, tuple(conditions.values()))

		self.cursor.execute(select_sql, tuple(conditions.values()))
		exists = self.cursor.fetchone()

		if exists:
			# Update
			update_sql = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'
			self.safe_log_sql(update_sql, tuple(record.values()) + tuple(conditions.values()))
			try:
				self.cursor.execute(update_sql, tuple(record.values()) + tuple(conditions.values()))
				self.logs.append(f'Updated record in table {table_name}')
			except Exception as e:
				self.logs.append(f'Error updating: {str(e)}')
		else:
			# Insert
			try:
				self.insert(table_name, [{**conditions, **record}])
				self.logs.append(f'Inserted record into table {table_name}')
			except Exception as e:
				self.logs.append(f'Error inserting: {str(e)}')



	def structureMgr(self, table_name, records):
		self.logs.append('fn: structureMgr')
		try:
			if not self.table_exists(table_name):
				self.createTable(table_name, records)
			self.ensure_columns_exist(table_name, records)
			self.table_structure[table_name] = True
		except Exception as e:
			self.logs.append(f'Error in structureMgr: {str(e)}')



	def createTable(self, table_name, records):
		self.logs.append('fn: createTable')
		fields = {}
		for record in records:
			if isinstance(record, dict):
				for key, value in record.items():
					fields[key] = self.get_type(value)
		columns_sql = ', '.join(f'"{k}" {v}' for k, v in fields.items())

		sql = f'CREATE TABLE "{table_name}" ({columns_sql})'
		self.logs.append(sql)
		self.cursor.execute(sql)
		self.logs.append(f'Table created: {table_name}')






	def table_exists(self, table_name):
		self.logs.append('fn: table_exists')
		sql = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = ?", (table_name,)
		self.logs.append(sql)
		self.cursor.execute(sql)
		return self.cursor.fetchone()[0] > 0


	def ensure_columns_exist(self, table_name, records):
		self.logs.append('fn: ensure_columns_exist')
		current_fields = self.fields(table_name)
		for record in records:
			for key, val in record.items():
				if key not in current_fields and key != 'id':  # 🛠️ Skip id
					try:
						sql = f'ALTER TABLE {table_name} ADD COLUMN "{key}" {self.get_type(val)}'
						self.logs.append(sql)
						self.cursor.execute(sql)
						self.logs.append(f'Added column {key}')
					except Exception as e:
						self.logs.append(f'Error adding column {key}: {str(e)}')




	def fields(self, table_name):
		self.logs.append('fn: fields')
		try:
			sql = "SELECT column_name FROM information_schema.columns WHERE table_name = ?", (table_name,)
			self.logs.append(sql)
			self.cursor.execute(sql)
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
			sql = "SELECT table_name FROM information_schema.tables WHERE table_name = ?", (table,)
			self.logs.append(sql)
			self.cursor.execute(sql)
			if not self.cursor.fetchone():
				self.cursor.execute(sql)
				self.logs.append(f'Table ensured: {table}')
		except Exception as e:
			self.logs.append(f'Error ensuring table: {str(e)}')

	def streamFn(self, table_name, conditions={}, callback=None, batch_size=100):
		self.logs.append('fn: streamFn')
		self.logs.append(f'Streaming from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			batch = []
			while True:
				row = self.cursor.fetchone()
				if row is None:
					if batch and callback:
						callback(batch)
					break
				batch.append(dict(zip(columns, row)))
				if len(batch) >= batch_size:
					if callback:
						callback(batch)
					batch = []

			self.logs.append(f'Completed streaming from table {table_name}')
		except Exception as e:
			self.logs.append(f'Error streaming from {table_name}: {str(e)}')


	def streamSave(self, table_name, conditions={}, batch_size=1000, callback=None, end=False):
		if not hasattr(self, 'streamSaveData'):
			self.streamSaveData = []

		if end:
			if self.streamSaveData:
				if callback:
					callback(self.streamSaveData)
				self.streamSaveData = []
			return

		self.logs.append('fn: streamSave')
		self.logs.append(f'Stream saving from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			while True:
				row = self.cursor.fetchone()
				if row is None:
					break
				self.streamSaveData.append(dict(zip(columns, row)))
				if len(self.streamSaveData) >= batch_size:
					if callback:
						callback(self.streamSaveData)
					self.streamSaveData = []

			self.logs.append(f'Completed stream saving from table {table_name}')
		except Exception as e:
			self.logs.append(f'Error stream saving from {table_name}: {str(e)}')





	def streamSaveMem(self, table_name, conditions={}, batch_size=1000, memory_limit_mb=20, mb=None, callback=None, end=False):
		if not mb is None: memory_limit_mb = mb
		if not hasattr(self, 'streamSaveData'):
			self.streamSaveData = []

		if end:
			if self.streamSaveData:
				if callback:
					callback(self.streamSaveData)
				self.streamSaveData = []
			return

		self.logs.append('fn: streamSave')
		self.logs.append(f'Stream saving from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			while True:
				row = self.cursor.fetchone()
				if row is None:
					break

				self.streamSaveData.append(dict(zip(columns, row)))

				# Check flush conditions
				if len(self.streamSaveData) >= batch_size or self.estimate_memory_usage_mb() >= memory_limit_mb:
					if callback:
						callback(self.streamSaveData)
					self.streamSaveData = []

			self.logs.append(f'Completed stream saving from table {table_name}')
		except Exception as e:
			self.logs.append(f'Error stream saving from {table_name}: {str(e)}')

	def estimate_memory_usage_mb(self):
		"""
		Estimate memory usage of streamSaveData in megabytes (MB).
		"""
		try:
			return sys.getsizeof(self.streamSaveData) / (1024 * 1024)
		except Exception as e:
			self.logs.append(f'Error estimating memory: {str(e)}')
			return 0



	def streamGen(self, table_name, conditions={}):
		"""
		Stream one record at a time from DuckDB using a generator.
		"""
		self.logs.append('fn: streamGen')
		self.logs.append(f'Streaming records from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			while True:
				row = self.cursor.fetchone()
				if row is None:
					break
				yield dict(zip(columns, row))

		except Exception as e:
			self.logs.append(f'Error in streamGen: {str(e)}')
		'''
		for record in db.streamGen('files'):
			print(record)
		'''


	def streamBatchGen(self, table_name, conditions={}, batch_size=1000):
		"""
		Stream records in batches from DuckDB using a generator.
		"""
		self.logs.append('fn: streamBatchGen')
		self.logs.append(f'Streaming batches from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			batch = []
			while True:
				row = self.cursor.fetchone()
				if row is None:
					if batch:
						yield batch
					break
				batch.append(dict(zip(columns, row)))
				if len(batch) >= batch_size:
					yield batch
					batch = []

		except Exception as e:
			self.logs.append(f'Error in streamBatchGen: {str(e)}')
		'''
		for batch in db.streamBatchGen('files', batch_size=500):
			for record in batch:
				print(record)
		'''



	def streamSaveThrottle(self, table_name, conditions={}, start_batch_size=500, min_batch_size=100, max_batch_size=5000, memory_limit_mb=50, callback=None, end=False):
		if not hasattr(self, 'streamSaveData'):
			self.streamSaveData = []

		if end:
			if self.streamSaveData:
				if callback:
					callback(self.streamSaveData)
				self.streamSaveData = []
			return

		self.logs.append('fn: streamSaveThrottle')
		self.logs.append(f'Smart streaming from table: {table_name}')
		if conditions and not self.structure:
			self.structureMgr(table_name, [conditions])

		where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
		where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ''
		select_sql = f'SELECT * FROM {table_name} {where_sql}'
		self.logs.append(select_sql)

		batch_size = start_batch_size

		try:
			self.cursor.execute(select_sql, tuple(conditions.values()))
			columns = [desc[0] for desc in self.cursor.description]

			while True:
				row = self.cursor.fetchone()
				if row is None:
					break

				self.streamSaveData.append(dict(zip(columns, row)))

				# Check if we need to flush
				if len(self.streamSaveData) >= batch_size:
					if callback:
						callback(self.streamSaveData)
					self.streamSaveData = []

					# After flush, check memory
					mem_usage = self.estimate_memory_usage_mb()
					if mem_usage > memory_limit_mb:
						batch_size = max(min_batch_size, batch_size // 2)
						self.logs.append(f'[AutoThrottle] 🔻 Reducing batch size to {batch_size} (memory {mem_usage:.1f}MB)')
					else:
						batch_size = min(max_batch_size, batch_size + 250)
						self.logs.append(f'[AutoThrottle] 🔺 Increasing batch size to {batch_size} (memory {mem_usage:.1f}MB)')

			self.logs.append(f'Completed smart streaming from {table_name}')
		except Exception as e:
			self.logs.append(f'Error in streamSaveThrottle: {str(e)}')

		# db.streamSaveThrottle('files', callback=myCallback)
		# db.streamSaveThrottle('files', end=True)





	# def threadInsert(self, table, record, timeout_seconds=5):
	#     """
	#     Main public function to insert a record into a threaded table.
	#     """
	#     if table not in self.threadData:
	#         self.initThreadedTable(table, timeout_seconds)

	#     active = self.activeSuffix[table]
	#     with self.threadLock:
	#         self.threadData[table][active].append(record)

	# def initThreadedTable(self, table, timeout_seconds=5):
	#     """
	#     Initialize threaded buffers and monitor for a new table.
	#     """
	#     self.threadData[table] = {'a': [], 'b': []}
	#     self.activeSuffix[table] = 'a'
	#     self.processingThread[table] = None
	#     self.threadTimeoutSeconds[table] = timeout_seconds

	#     # Start monitor for table
	#     t = threading.Thread(target=self.monitorTable, args=(table,), daemon=True)
	#     self.monitorThread[table] = t
	#     t.start()

	# def monitorTable(self, table):
	#     """
	#     Monitor if new data is coming in for table.
	#     After timeout of inactivity, flush and stop.
	#     """
	#     idle_ticks = 0
	#     last_count = 0

	#     while True:
	#         with self.threadLock:
	#             current_count = len(self.threadData[table][self.activeSuffix[table]])

	#         if current_count == last_count:
	#             idle_ticks += 1
	#         else:
	#             idle_ticks = 0  # Reset if new data came in

	#         last_count = current_count

	#         if idle_ticks >= self.threadTimeoutSeconds[table]:
	#             # Flush if any remaining
	#             self.flushTable(table)
	#             break

	#         time.sleep(1)

	# def flushTable(self, table):
	#     """
	#     Flip buffers and flush the data.
	#     """
	#     with self.threadLock:
	#         active = self.activeSuffix[table]
	#         inactive = 'b' if active == 'a' else 'a'
	#         self.activeSuffix[table] = inactive

	#         to_save = self.threadData[table][active]
	#         self.threadData[table][active] = []

	#     if to_save:
	#         # Save in background
	#         t = threading.Thread(target=self.flushWorker, args=(table, to_save), daemon=True)
	#         self.processingThread[table] = t
	#         t.start()

	# def flushWorker(self, table, records):
	#     """
	#     Background worker to save records.
	#     """
	#     try:
	#         self.logs.append(f'[ThreadFlush] Saving {len(records)} records to {table}')
	#         self.i(table, records)
	#     except Exception as e:
	#         self.logs.append(f'[ThreadFlushError] {str(e)}')

	def i(self, table_name, records):
		"""
		Your insert function, slightly modified to accept list of records directly.
		"""
		if not records:
			return

		if not self.structure:
			self.structureMgr(table_name, records)

		for record in records:
			columns = [f'"{col}"' for col in record.keys()]
			placeholders = [f'${i+1}' for i in range(len(record))]
			insert_sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
			self.logs.append(insert_sql)
			try:
				self.cursor.execute(insert_sql, tuple(record.values()))
				self.logs.append(f'Inserted into {table_name}')
			except Exception as e:
				self.logs.append(f'Error inserting into {table_name}: {str(e)}')













	def threadInsert(self, table, record, timeout_seconds=5):
		""" Fast insert into memory with light lock. """
		if table not in self.threadData:
			self.initThreadedTable(table, timeout_seconds)

		active = self.activeSuffix[table]
		with self.threadLock:
			self.threadData[table][active].append(record)

	def flushTable(self, table):
		""" Flip buffers, start flush thread. """
		with self.threadLock:
			active = self.activeSuffix[table]
			inactive = 'b' if active == 'a' else 'a'
			self.activeSuffix[table] = inactive
			to_save = self.threadData[table][active]
			self.threadData[table][active] = []

		if to_save:
			threading.Thread(target=self.flushWorker, args=(table, to_save), daemon=True).start()

	def flushWorker(self, table, records):
		""" Save batch safely with file lock per flush. """
		lock_file = FileLocker.lockPath(table)
		FileLocker.lock(lock_file)
		try:
			self.insert_records(table, records)
		finally:
			FileLocker.unlock(lock_file)

	def insert_records(self, table_name, records):
		""" Batch insert into DuckDB. """
		if not records:
			return
		if not self.structure:
			self.structureMgr(table_name, records)
		for record in records:
			columns = [f'"{col}"' for col in record.keys()]
			placeholders = [f'${i+1}' for i in range(len(record))]
			sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
			self.logs.append(sql)
			try:
				self.cursor.execute(sql, tuple(record.values()))
			except Exception as e:
				self.logs.append(f'Insert error: {str(e)}')



	def clear_table(self, table):
		""" Flush and delete all rows """
		self.flushTable(table)
		time.sleep(0.5)  # Give flush thread slight time
		lock_file = FileLocker.lockPath(table)
		FileLocker.lock(lock_file)
		try:
			sql = f'DELETE FROM {table}'
			self.logs.append(sql)
			self.cursor.execute(sql)
			self.conn.commit()
		finally:
			FileLocker.unlock(lock_file)
		self.logs.append(f'🧹 Table cleared: {table}')











	def dump(self, tables=None):
		"""
		Dump database structure and data.
		If tables is None, dumps all tables.
		"""
		output = {
			'schema': {},
			'dump': {}
		}

		if tables is None:
			tables = self.list_tables()

		for table in tables:
			# Dump schema
			output['schema'][table] = self.get_table_schema(table)
			# Dump records
			output['dump'][table] = self.read(table)

		return output

	def list_tables(self):
		self.logs.append('fn: list_tables')
		"""
		List all user tables in the database.
		"""
		sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='main'"
		self.logs.append(sql)
		self.cursor.execute(sql)
		return [row[0] for row in self.cursor.fetchall()]

	def get_table_schema(self, table):
		self.logs.append('fn: get_table_schema')
		"""
		Get a dictionary of field_name: field_type for a given table.
		"""
		sql = "PRAGMA table_info('" + table + "')"
		self.logs.append(sql)
		self.cursor.execute(sql)
		result = {}
		for row in self.cursor.fetchall():
			result[row[1]] = row[2]
		return result












	def ti(self, table, record, timeout_seconds=5):
		return self.threadInsert(self, table, record, timeout_seconds)


	def r(self, table_name, conditions={}):
		return self.read(table_name, conditions)

	def get(self, table_name, conditions={}):
		return self.read(table_name, conditions)


	def create(self, table_name, record):
		return self.insert(table_name, record)

	def c(self, table_name, record):
		return self.insert(table_name, record)


	def I(self, table_name, record):
		return self.insert(table_name, record)

	def ui(self, table_name, conditions, record):
		return self.update_or_insert(table_name, conditions, record)


	def d(self, table_name, conditions={}):
		return self.delete(table_name, conditions)

duck = duckdbMgr
db = duckdbMgr


















import os
import re
import time

class FileLocker:
	@staticmethod
	def lockName(path):
		"""Strip non-filename safe characters."""
		return re.sub(r'[^\w\-_\. ]', '_', path)

	@staticmethod
	def lockPath(path):
		"""Get the lock file path, ensuring the directory exists."""
		folder_path = _v.fileLocks  # Assumes `_v.fileLocks` is defined in your framework
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
		return os.path.join(folder_path, FileLocker.lockName(path))

	@staticmethod
	def lock(path):
		"""Rename the file to create a lock."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		start_time = time.time()
		while True:
			try:
				# Try renaming the file to acquire the lock
				os.rename(lock_path, lock_file)
				return  # Lock acquired
			except FileNotFoundError:
				# If the original file doesn't exist, create a dummy lock
				with open(lock_file, "w") as f:
					f.write("")  # Create an empty lock file
				return
			except OSError:
				# Another process holds the lock; wait and retry
				if time.time() - start_time > 10:  # Optional timeout of 10 seconds
					raise TimeoutError("Timeout waiting for lock")
				time.sleep(0.1)  # Retry after a short delay

	@staticmethod
	def unlock(path):
		"""Rename the lock file back to its original name."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		try:
			os.rename(lock_file, lock_path)  # Release the lock
		except FileNotFoundError:
			pass  # Lock already released or doesn't exist

	@staticmethod
	def check(path):
		"""Wait until the lock file does not exist."""
		lock_path = FileLocker.lockPath(path)
		lock_file = lock_path + ".lock"
		while os.path.exists(lock_file):
			time.sleep(0.1)
			# if time.time() - md(path) > 15:
			# 	pr('File Lock Override in 15 Seconds',c='red')

			if time.time() - md(path) > 30:
				pr('Lock Override',c='red')
				FileLocker.unlock(path)


# FileLocker.check(path)
# FileLocker.lock(path)
# FileLocker.unlock(path)
# folderProfileAttribute <-- errors