import unqlite  # type: ignore
import uuid
from datetime import datetime


class UnQLiteMgr:
	def __init__(self, database):
		self.logs = ['fn: __init__']
		self.logs.append(f'init: {database}')
		self.database_name = database
		self.db = unqlite.UnQLite(database)
		self.structure = True
		self.registry_collection = '__collections__'
		self._register_collection(self.registry_collection)

	def _register_collection(self, name):
		registry = self.db.collection(self.registry_collection)
		if not registry.exists():
			registry.create()
		if name not in [x.get('name') for x in registry.all()]:
			self.logs.append(f'[REGISTER] {name}')
			registry.store({'name': name})

	def _get_record_id(self, record):
		return record.get('_id') or record.get('__id')

	def generate_object_id(self):
		return str(uuid.uuid4())

	def serialize_special_types(self, obj):
		if isinstance(obj, dict):
			return {k: self.serialize_special_types(v) for k, v in obj.items()}
		elif isinstance(obj, list):
			return [self.serialize_special_types(v) for v in obj]
		elif isinstance(obj, datetime):
			return obj.isoformat()
		return obj

	def insert(self, table, records):
		self.logs.append('fn: insert')
		self._register_collection(table)
		collection = self.db.collection(table)
		if not collection.exists():
			collection.create()
		for record in records:
			if '_id' not in record:
				record['_id'] = self.generate_object_id()
			collection.store(self.serialize_special_types(record))
			self.logs.append(f'Inserted record into table {table}')

	def insertChild(self, table, parent_condition, child_field, child_data):
		self.logs.append('fn: insertChild')
		self._register_collection(table)
		collection = self.db.collection(table)
		parent_record = self.findOne(table, parent_condition)
		if not parent_record:
			return False
		if child_field not in parent_record:
			parent_record[child_field] = []
		if '_id' not in child_data:
			child_data['_id'] = self.generate_object_id()
		parent_record[child_field].append(self.serialize_special_types(child_data))
		collection.update(parent_record, self._get_record_id(parent_record))
		return True

	def insertRecordsChild(self, table, parent_condition, child_field, child_records):
		self.logs.append('fn: insertRecordsChild')
		self._register_collection(table)
		collection = self.db.collection(table)
		parent_record = self.findOne(table, parent_condition)
		if not parent_record:
			return False
		if child_field not in parent_record:
			parent_record[child_field] = []
		for record in child_records:
			if '_id' not in record:
				record['_id'] = self.generate_object_id()
			parent_record[child_field].append(self.serialize_special_types(record))
		collection.update(parent_record, self._get_record_id(parent_record))
		return True

	def updateChild(self, table, parent_condition, child_field, child_condition, updated_data):
		self.logs.append('fn: updateChild')
		self._register_collection(table)
		collection = self.db.collection(table)
		parent_record = self.findOne(table, parent_condition)
		if not parent_record or child_field not in parent_record:
			return False
		updated = False
		for child in parent_record[child_field]:
			if all(child.get(k) == v for k, v in child_condition.items()):
				child.update(updated_data)
				updated = True
		if updated:
			collection.update(parent_record, self._get_record_id(parent_record))
			return True
		return False

	def deleteChild(self, table, parent_condition, child_field, child_condition):
		self.logs.append('fn: deleteChild')
		self._register_collection(table)
		collection = self.db.collection(table)
		parent_record = self.findOne(table, parent_condition)
		if not parent_record or child_field not in parent_record:
			return False
		original = len(parent_record[child_field])
		parent_record[child_field] = [
			child for child in parent_record[child_field]
			if not all(child.get(k) == v for k, v in child_condition.items())
		]
		if len(parent_record[child_field]) < original:
			collection.update(parent_record, self._get_record_id(parent_record))
			return True
		return False

	def delete(self, table, conditions):
		self.logs.append('fn: delete')
		self._register_collection(table)
		collection = self.db.collection(table)
		records = [r for r in collection.all() if self.match_conditions(r, conditions)]
		for rec in records:
			if '_id' in rec:
				collection.delete(rec['_id'])
		return bool(records)

	def delete_nested_field(self, table, conditions, nested_field):
		self.logs.append('fn: delete_nested_field')
		self._register_collection(table)
		record = self.findOne(table, conditions)
		if not record or "_id" not in record:
			return False
		keys = nested_field.split(".")
		ref = record
		for key in keys[:-1]:
			ref = ref.get(key)
			if ref is None:
				return False
		ref.pop(keys[-1], None)
		self.db.collection(table).update(record, record["_id"])
		return True

	def update_nested_field_lists(self, table, conditions, field_path, value):
		self.logs.append("fn: update_nested_field_lists")
		self._register_collection(table)
		record = self.findOne(table, conditions)
		if not record or "_id" not in record:
			return False
		ref = record
		for part in field_path.split(".")[:-1]:
			ref = ref.setdefault(part, {})
		ref[field_path.split(".")[-1]] = value
		self.db.collection(table).update(record, record["_id"])
		return True

	def get_nested_field_lists(self, table, conditions, field_path):
		self.logs.append("fn: get_nested_field_lists")
		self._register_collection(table)
		record = self.findOne(table, conditions)
		if not record:
			return None
		ref = record
		for part in field_path.split("."):
			if part.isdigit():
				part = int(part)
				if isinstance(ref, list) and 0 <= part < len(ref):
					ref = ref[part]
				else:
					return None
			elif part.startswith("{") and part.endswith("}"):
				key, val = part[1:-1].split(":")
				val = val.strip().strip("~ ")
				ref = next((item for item in ref if val in str(item.get(key, ""))), None)
			else:
				ref = ref.get(part)
			if ref is None:
				return None
		return ref
	

	def delete_nested_field_lists(self, table, conditions, field_path):
		self.logs.append("fn: delete_nested_field_lists")
		record = self.findOne2(table, conditions)
		if not record or "_id" not in record:
			self.logs.append("Record not found or missing _id")
			return False
		keys = field_path.split(".")
		ref = record
		for key in keys[:-1]:
			if key.isdigit():
				key = int(key)
				ref = ref[key]
			else:
				ref = ref.get(key)
				if ref is None:
					return False
		ref.pop(keys[-1], None)
		self.db.collection(table).update(record, record["_id"])
		return True

	def find(self, table, conditions={}):
		self.logs.append('fn: find')
		self._register_collection(table)
		collection = self.db.collection(table)
		if not collection.exists():
			return []
		return [r for r in collection.all() if self.match_conditions(r, conditions)]

	def findOne(self, table, conditions={}):
		self.logs.append('fn: findOne')
		self._register_collection(table)
		collection = self.db.collection(table)
		if not collection.exists():
			return None
		for r in collection.all():
			if self.match_conditions(r, conditions):
				return r
		return None

	def findChild(self, table, parent_condition, child_field, child_condition={}):
		self.logs.append('fn: findChild')
		parent = self.findOne(table, parent_condition)
		if not parent or child_field not in parent:
			return []
		return [c for c in parent[child_field] if self.match_conditions(c, child_condition)]

	def findOneChild(self, table, parent_condition, child_field, child_condition={}):
		self.logs.append('fn: findOneChild')
		parent = self.findOne(table, parent_condition)
		if not parent or child_field not in parent:
			return None
		for c in parent[child_field]:
			if self.match_conditions(c, child_condition):
				return c
		return None

	def match_conditions(self, record, conditions):
		for key, cond in conditions.items():
			value = record.get(key)
			if isinstance(cond, dict):
				for op, v in cond.items():
					if not self.match_operator(value, op, v):
						return False
			elif value != cond:
				return False
		return True

	def match_operator(self, value, op, cond_val):
		if op == '~':
			return cond_val in str(value)
		return value == cond_val

	def dump(self):
		self.logs.append("fn: dump")
		result = {}
		registry = self.db.collection(self.registry_collection)
		if not registry.exists():
			return result
		for entry in registry.all():
			name = entry.get("name")
			if name:
				col = self.db.collection(name)
				if col.exists():
					result[name] = col.all()
		return result

	def index_list_add(self, label, concat_path, list_index):
		self.logs.append("fn: index_list_add")
		self._register_collection("indexes.indexes")
		collection = self.db.collection("indexes.indexes")
		if not collection.exists():
			collection.create()
		collection.store({"label": label, concat_path: list_index})

	def index_list_del(self, label):
		self.logs.append("fn: index_list_del")
		self._register_collection("indexes.indexes")
		collection = self.db.collection("indexes.indexes")
		for i in collection.all():
			if i.get("label") == label:
				collection.delete(i["_id"])

	def index_list_get(self, label):
		self.logs.append("fn: index_list_get")
		self._register_collection("indexes.indexes")
		collection = self.db.collection("indexes.indexes")
		return [i for i in collection.all() if i.get("label") == label]

	def index_list_all(self):
		self.logs.append("fn: index_list_all")
		self._register_collection("indexes.indexes")
		return self.db.collection("indexes.indexes").all()


	def close(self):
		self.logs.append("fn: close")
		"""Closes the UnQLite database."""
		self.db.close()
		self.logs.append('Database connection closed.')

