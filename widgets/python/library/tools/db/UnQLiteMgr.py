import unqlite     # type: ignore
import uuid
from datetime import datetime

class UnQLiteMgr:
	def __init__(self, database):
		self.logs = ['fn: __init__']
		self.logs.append(f'init: {database}')
		self.database_name = database
		self.db = unqlite.UnQLite(database)
		self.structure = True  # No need for table structure management

	def insert(self, table_name, records):
		"""Inserts complex JSON-like records, supporting nested objects & arrays."""
		self.logs.append('fn: insert')
		collection = self.db.collection(table_name)

		if not collection.exists():
			collection.create()

		for record in records:
			if '_id' not in record:
				record['_id'] = self.generate_object_id()
			record = self.serialize_special_types(record)
			collection.store(record)
			self.logs.append(f'Inserted record into table {table_name}')

	def insertChild(self, table_name, parent_condition, child_field, child_data):
		"""Inserts a child object into an array inside a parent document."""
		self.logs.append('fn: insertChild')
		collection = self.db.collection(table_name)
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record:
			self.logs.append(f'Parent record not found for {parent_condition}')
			return False

		if child_field not in parent_record:
			parent_record[child_field] = []

		if '_id' not in child_data:
			child_data['_id'] = self.generate_object_id()

		parent_record[child_field].append(self.serialize_special_types(child_data))
		collection.update(parent_record)
		self.logs.append(f'Inserted child into {child_field} in table {table_name}')
		return True

	def insertRecordsChild(self, table_name, parent_condition, child_field, child_records):
		"""Inserts multiple child objects into an array inside a parent document."""
		self.logs.append('fn: insertRecordsChild')
		collection = self.db.collection(table_name)
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record:
			self.logs.append(f'Parent record not found for {parent_condition}')
			return False

		# Ensure child array exists
		if child_field not in parent_record:
			parent_record[child_field] = []

		for record in child_records:
			if '_id' not in record:
				record['_id'] = self.generate_object_id()  # Assign unique ID if missing
			parent_record[child_field].append(record)

		collection.update(parent_record)
		self.logs.append(f'Inserted {len(child_records)} records into {child_field} in {table_name}')
		return True


	def updateChild(self, table_name, parent_condition, child_field, child_condition, updated_data):
		"""Updates a specific child inside an array in a parent document."""
		self.logs.append('fn: updateChild')
		collection = self.db.collection(table_name)
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record or child_field not in parent_record:
			self.logs.append(f'Parent or child field missing in {table_name}')
			return False

		if "_id" not in parent_record:
			self.logs.append(f"Error: Parent record is missing '_id'")
			return False

		updated = False
		for child in parent_record[child_field]:
			if all(child.get(k) == v for k, v in child_condition.items()):
				child.update(updated_data)
				updated = True

		if updated:
			collection.update(parent_record, parent_record["_id"])  # ✅ FIXED: Ensure `_id` is passed
			self.logs.append(f'Updated child in {child_field} in table {table_name}')
			return True
		else:
			self.logs.append(f'No matching child found for update')
			return False

	# def update_nested_field(self, table, conditions, field, nested_updates):
	# 	"""
	# 	Update multiple nested fields in a document, creating missing structures as needed.

	# 	:param table: The collection/table name.
	# 	:param conditions: The conditions to locate the record.
	# 	:param field: The root field where updates should be applied.
	# 	:param nested_updates: A dictionary or direct value to be set in a nested field.
	# 	:return: True if updated, False if record not found.
	# 	"""
	# 	record = self.findOne(table, conditions)

	# 	if not record:
	# 		print("Record not found.")
	# 		return False

	# 	if "_id" not in record:
	# 		print("Error: Record is missing '_id', cannot update.")
	# 		return False

	# 	if isinstance(nested_updates, dict):
	# 		if field not in record:
	# 			record[field] = {}

	# 		data = record[field]

	# 		for nested_field, new_value in nested_updates.items():
	# 			keys = nested_field.split(".")
	# 			nested_data = data

	# 			for key in keys[:-1]:
	# 				if key not in nested_data or not isinstance(nested_data[key], dict):
	# 					nested_data[key] = {}
	# 				nested_data = nested_data[key]

	# 			nested_data[keys[-1]] = new_value

	# 	else:
	# 		record[field] = nested_updates

	# 	self.db.collection(table).update(record, record["_id"])

	# 	print(f"Updated {field}: {nested_updates}")
	# 	return True







	def delete_nested_field(self, table, conditions, nested_field):
		"""Delete a specific nested field in a record."""
		self.logs.append('fn: delete_nested_field')
		record = self.findOne(table, conditions)  # ✅ FIXED: Corrected function call

		if not record:
			print("Record not found.")
			return False

		if "_id" not in record:
			print("Error: Record is missing '_id', cannot delete field.")
			return False

		keys = nested_field.split(".")
		data = record

		for key in keys[:-1]:
			if key in data:
				data = data[key]
			else:
				print(f"Field {nested_field} not found.")
				return False

		deleted = data.pop(keys[-1], None)
		if deleted is None:
			print(f"Field {nested_field} was not found in the document.")
			return False

		self.db.collection(table).update(record, record["_id"])  # ✅ FIXED: Pass `_id`
		print(f"Deleted {nested_field}")
		return True




	def deleteChild(self, table_name, parent_condition, child_field, child_condition):
		"""Removes a specific child object from an array in a parent document."""
		self.logs.append('fn: deleteChild')
		collection = self.db.collection(table_name)
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record or child_field not in parent_record:
			self.logs.append(f'Parent or child field missing in {table_name}')
			return False

		if "_id" not in parent_record:
			self.logs.append(f"Error: Parent record is missing '_id'")
			return False

		if not isinstance(parent_record[child_field], list):
			print(f"{child_field} is not a list in the document.")
			return False

		original_length = len(parent_record[child_field])
		parent_record[child_field] = [
			child for child in parent_record[child_field]
			if not all(child.get(k) == v for k, v in child_condition.items())
		]

		if len(parent_record[child_field]) < original_length:
			collection.update(parent_record, parent_record["_id"])  # ✅ FIXED: Pass `_id`
			self.logs.append(f'Deleted child from {child_field} in table {table_name}')
			return True
		else:
			self.logs.append(f'No matching child found for deletion')
			return False


	def delete(self, table_name, conditions):
		"""Deletes an entire document matching the conditions."""
		self.logs.append('fn: delete')
		collection = self.db.collection(table_name)

		matching_records = [rec for rec in collection.all() if self.match_conditions(rec, conditions)]

		if not matching_records:
			self.logs.append(f'No matching document found for deletion')
			return False

		for record in matching_records:
			if "_id" in record:
				collection.delete(record["_id"])  # ✅ FIXED: Ensure `_id` exists
			else:
				self.logs.append(f"Error: Record missing '_id', cannot delete.")

		self.logs.append(f'Deleted {len(matching_records)} documents from table {table_name}')
		return True


	def find(self, table_name, conditions={}):
		"""Finds multiple records that match the given conditions."""
		self.logs.append('fn: find')
		collection = self.db.collection(table_name)

		if not collection.exists():
			return []

		return [rec for rec in collection.all() if self.match_conditions(rec, conditions)]

	def findOne(self, table_name, conditions={}):
		"""Finds a single record that matches the given conditions."""
		self.logs.append('fn: findOne')
		collection = self.db.collection(table_name)

		if not collection.exists():
			return None

		for record in collection.all():
			if self.match_conditions(record, conditions):
				return record
		return None

	def findChild(self, table_name, parent_condition, child_field, child_condition={}):
		"""Finds all child objects in an array inside a parent document."""
		self.logs.append('fn: findChild')
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record or child_field not in parent_record:
			self.logs.append(f'Parent or child field missing in {table_name}')
			return []

		# Filter children based on conditions
		matching_children = [
			child for child in parent_record[child_field]
			if self.match_conditions(child, child_condition)
		]
		
		self.logs.append(f'Found {len(matching_children)} matching children in {child_field}')
		return matching_children

	def findOneChild(self, table_name, parent_condition, child_field, child_condition={}):
		"""Finds a single child object inside an array in a parent document."""
		self.logs.append('fn: findOneChild')
		parent_record = self.findOne(table_name, parent_condition)

		if not parent_record or child_field not in parent_record:
			self.logs.append(f'Parent or child field missing in {table_name}')
			return None

		for child in parent_record[child_field]:
			if self.match_conditions(child, child_condition):
				self.logs.append(f'Found matching child in {child_field}')
				return child
		
		self.logs.append(f'No matching child found in {child_field}')
		return None

	def match_conditions(self, record, conditions):
		"""Matches a record against conditions supporting MongoDB-like queries."""
		for key, condition in conditions.items():
			field_value = record.get(key, None)  # Ensure missing fields don't cause errors

			if isinstance(condition, dict):
				for operator, value in condition.items():
					if not self.match_operator(field_value, operator, value):
						return False
			elif field_value != condition:
				return False
		return True

	def generate_object_id(self):
		"""Mimics MongoDB's ObjectId using UUID."""
		return str(uuid.uuid4())

	def serialize_special_types(self, obj):
		"""Converts special types like datetime into string format."""
		if isinstance(obj, dict):
			return {k: self.serialize_special_types(v) for k, v in obj.items()}
		elif isinstance(obj, list):
			return [self.serialize_special_types(v) for v in obj]
		elif isinstance(obj, datetime):
			return obj.isoformat()
		return obj

	def serialize_special_types(self, obj):
		"""Converts special types like datetime into string format."""
		if isinstance(obj, dict):
			return {k: self.serialize_special_types(v) for k, v in obj.items()}
		elif isinstance(obj, list):
			return [self.serialize_special_types(v) for v in obj]
		elif isinstance(obj, datetime):
			return obj.isoformat()
		return obj

	def close(self):
		"""Closes the UnQLite database."""
		self.db.close()
		self.logs.append('Database connection closed.')
