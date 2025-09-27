import json
import os
import re
import copy
from functools import reduce
import glob
import time

class JsonDatabase:
	def __init__(self, input_data):
		self.data = {}
		self.file_path = None
		self.backup_dir = './.JsonDatabase/'
		self.is_file_mode = False
		self.transaction_data = None
		self.disable_backup = True

		if isinstance(input_data, str):
			if os.path.isfile(input_data):
				self.file_path = input_data
				self.is_file_mode = True
				with open(self.file_path, 'r') as file:
					self.data = json.load(file)
			else:
				try:
					self.data = json.loads(input_data)
				except json.JSONDecodeError:
					raise ValueError("Invalid JSON string provided.")
		elif isinstance(input_data, dict):
			self.data = input_data
		else:
			raise ValueError("Input must be a file path, JSON string, or dict.")

		self.index = self.indexJson(self.data)
		if self.is_file_mode and not self.disable_backup:
			self.initializeBackupDir()

	def initializeBackupDir(self):
		if not os.path.exists(self.backup_dir):
			os.makedirs(self.backup_dir, exist_ok=True)
			with open(os.path.join(self.backup_dir, '.htaccess'), 'w') as f:
				f.write("Deny from all\n")

	def indexJson(self, data, prefix=''):
		result = {}
		if isinstance(data, dict):
			for key, value in data.items():
				full_key = f"{prefix}.{key}" if prefix else key
				if isinstance(value, dict):
					result.update(self.indexJson(value, full_key))
				else:
					result[full_key] = value
		return result

	def jsonByPath(self, path):
		keys = path.split('.')
		temp = self.data
		for key in keys:
			if key not in temp:
				return None
			temp = temp[key]
		return temp

	def deleteMany(self, path, search_conditions=None, omit_conditions=None):
		records = self.jsonByPath(path)
		if not records:
			return {"error": "No records found at path: " + path}

		initial_length = len(records)
		records = [record for record in records if not self.matchConditions(record, search_conditions) or self.matchConditions(record, omit_conditions)]
		if len(records) == initial_length:
			return {"error": "No records matched the deletion criteria"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": "Records deleted"}

	def matchConditions(self, record, conditions):
		if not conditions:
			return True
		return all(self.matchOperator(record.get(field), condition) for field, condition in conditions.items())

	def matchOperator(self, value, condition):
		operator, expected = next(iter(condition.items()))
		return {
			'==': lambda v: v == expected,
			'!=': lambda v: v != expected,
			'<': lambda v: v < expected,
			'>': lambda v: v > expected,
			'<=': lambda v: v <= expected,
			'>=': lambda v: v >= expected,
			'like': lambda v: expected in v
		}.get(operator, lambda v: False)(value)

	def overwriteEnd(self, path, json_data):
		data_to_insert = json.loads(json_data)
		keys = path.split('.')
		temp = self.data
		for key in keys[:-1]:
			if key not in temp:
				temp[key] = {}
			temp = temp[key]
		temp[keys[-1]] = data_to_insert
		if self.is_file_mode and not self.disable_backup:
			self.writeJson(self.data)

	def writeJson(self, data):
		with open(self.file_path, 'w') as file:
			json.dump(data, file, indent=4)

	def aggregate(self, path, operation, field, search_conditions=None, omit_conditions=None):
		records = self.jsonByPath(path)
		if not records:
			return {"error": "No records found at path: " + path}

		filtered_records = [r[field] for r in records if field in r and isinstance(r[field], (int, float))]
		if operation == "sum":
			return sum(filtered_records)
		elif operation == "avg":
			return sum(filtered_records) / len(filtered_records) if filtered_records else 0
		elif operation == "min":
			return min(filtered_records)
		elif operation == "max":
			return max(filtered_records)
		else:
			return {"error": "Invalid operation"}

	def findSorted(self, path, sort_field, sort_order='asc', search_conditions=None, omit_conditions=None):
		records = self.find(path, search_conditions, omit_conditions)
		return sorted(records, key=lambda x: x[sort_field], reverse=(sort_order == 'desc'))

	def backupChanges(self, path, old_data, new_data):
		"""
		Creates a backup of the old data at a given path before changes are applied.
		
		:param path: The JSON path where changes occur
		:param old_data: The data before changes
		:param new_data: The new data to be saved
		"""
		# Create a directory path for the backups based on the path to avoid conflicts
		backup_path = self.backup_dir + path.replace('.', '/') + '/'
		if not os.path.exists(backup_path):
			os.makedirs(backup_path, exist_ok=True)

		# Create a backup file with a timestamp
		timestamp = time.strftime("%Y%m%d-%H%M%S")
		file_name = f"{timestamp}.json"
		full_path = os.path.join(backup_path, file_name)

		# Save the old data to the backup file
		with open(full_path, 'w') as backup_file:
			json.dump(old_data, backup_file, indent=4)

		# Optionally, you could log this action
		print(f"Backup created at {full_path}")

	def recoverPath(self, path, epoch, protect=None):
		"""
		Recovers data from a backup file for a given path using a specific timestamp (epoch).
		
		:param path: The JSON path where data needs to be restored
		:param epoch: The timestamp of the backup file to restore
		:param protect: Optional list of fields to protect from being overwritten during recovery
		"""
		# Create a directory path for the backups based on the path
		backup_path = self.backup_dir + path.replace('.', '/') + '/'
		backup_file_name = f"{epoch}.json"
		full_path = os.path.join(backup_path, backup_file_name)

		# Check if the backup file exists
		if not os.path.exists(full_path):
			return {"error": "Backup file not found"}

		# Load the backup data
		with open(full_path, 'r') as backup_file:
			backup_data = json.load(backup_file)

		# Optionally protect certain fields from being overwritten
		if protect:
			current_data = self.jsonByPath(path)
			for key in protect:
				if key in current_data:
					backup_data[key] = current_data[key]

		# Write the recovered data back to the main data structure
		self.overwriteEnd(path, json.dumps(backup_data))
		return {"success": f"Data recovered from backup at {full_path}"}

	def mergeData(self, target, newData, overwriteIfExists=True):
		"""
		Merges newData into the target dictionary. It recursively merges dictionaries and
		updates lists or values based on the overwriteIfExists flag.

		:param target: The target data structure (dictionary) to merge into.
		:param newData: The new data to be merged into the target.
		:param overwriteIfExists: A boolean flag that, if True, allows existing values to be overwritten.
		"""
		for key, value in newData.items():
			if isinstance(value, dict) and key in target and isinstance(target[key], dict):
				# Recursively merge dictionaries
				self.mergeData(target[key], value, overwriteIfExists)
			elif overwriteIfExists or key not in target:
				# Overwrite if allowed or key does not exist in target
				target[key] = value
			elif isinstance(value, list) and key in target and isinstance(target[key], list):
				# Extend the list if the key exists and it's also a list
				target[key].extend(value)
			# Optionally handle other types of merges like set, etc.

	def appendEnd(self, path, jsonData, overwriteIfExists=True):
		"""
		Appends data to the end of a JSON structure at the specified path. If the path
		doesn't exist, it initializes it as a new list before appending.

		:param path: The JSON path where data should be appended.
		:param jsonData: The JSON data to append in string format.
		:param overwriteIfExists: If True, allows overwriting existing non-list items.
		"""
		dataToInsert = json.loads(jsonData)
		keys = path.split('.')
		temp = self.data

		# Navigate to the correct location in the data structure or create new dicts/lists as needed
		for key in keys[:-1]:
			if key not in temp or not isinstance(temp[key], dict):
				temp[key] = {}
			temp = temp[key]
		
		last_key = keys[-1]
		if last_key not in temp or not isinstance(temp[last_key], list):
			if overwriteIfExists:
				temp[last_key] = []  # Initialize as a new list if not existing or not a list
			else:
				return {"error": "Target is not a list and overwrite is not allowed"}

		# Append the new data
		if isinstance(dataToInsert, list):
			temp[last_key].extend(dataToInsert)
		else:
			temp[last_key].append(dataToInsert)

		# Optionally, update the file if operating in file mode
		if self.is_file_mode and not self.disable_backup:
			self.writeJson(self.data)

		return {"success": f"Data appended at {path}"}


	def recoverRollback(self, epoch, protect=None):
		"""
		Recovers all paths modified at a given backup timestamp (epoch).

		:param epoch: The timestamp of the backup file to restore.
		:param protect: Optional list of fields to protect from being overwritten during recovery.
		:return: Success or error message.
		"""

		# rollback_result = db.recoverRollback("20240219-123456", protect=["settings.version"])


		if not self.is_file_mode and not self.disable_backup:
			return {"error": "File mode is disabled; cannot recover backups"}

		# Find all backup files corresponding to the provided epoch
		backup_files = glob.glob(os.path.join(self.backup_dir, "*/*", f"{epoch}.json"))
		if not backup_files:
			return {"error": "No backups found for the given epoch"}

		for backup_file in backup_files:
			# Extract the JSON path from the backup file's location
			relative_path = backup_file.replace(self.backup_dir, '').replace('/', '.').replace(f".{epoch}.json", "")

			# Recover data from the backup for this path
			self.recoverPath(relative_path, epoch, protect)

		return {"success": "Rollback completed successfully"}


	def insert(self, path, newData):
		"""
		Inserts a new record into a JSON structure at the specified path.
		If the path points to a list, the new data is appended. 
		If the path doesn't exist, it initializes it as a new list.

		:param path: The JSON path where data should be inserted.
		:param newData: The data to be inserted (can be dict, list, or primitive value).
		:return: Success or error message.
		"""
		keys = path.split('.')
		temp = self.data

		# Navigate to the correct location in the data structure
		for key in keys[:-1]:
			if key not in temp or not isinstance(temp[key], dict):
				temp[key] = {}
			temp = temp[key]

		last_key = keys[-1]
		if last_key not in temp:
			temp[last_key] = []  # Initialize as a list if it doesn't exist
		elif not isinstance(temp[last_key], list):
			return {"error": "Target is not a list, cannot insert"}

		# Append the new data
		temp[last_key].append(newData)

		# Write changes to file if in file mode
		if self.is_file_mode and not self.disable_backup:
			self.writeJson(self.data)

		return {"success": f"Data inserted at {path}"}



	def insertMany(self, path, records):
		"""
		Inserts multiple records into a JSON structure at the specified path.
		If the path points to a list, the new records are appended.
		If the path does not exist, it initializes it as a list.

		:param path: The JSON path where data should be inserted.
		:param records: A list of records (dictionaries, lists, or primitive values).
		:return: Success or error message.
		"""
		if not isinstance(records, list):
			return {"error": "Records must be a list"}

		keys = path.split('.')
		temp = self.data

		# Navigate to the correct location in the data structure
		for key in keys[:-1]:
			if key not in temp or not isinstance(temp[key], dict):
				temp[key] = {}
			temp = temp[key]

		last_key = keys[-1]
		if last_key not in temp:
			temp[last_key] = []  # Initialize as a list if it doesn't exist
		elif not isinstance(temp[last_key], list):
			return {"error": "Target is not a list, cannot insert multiple records"}

		# Append the new records
		temp[last_key].extend(records)

		# Write changes to file if in file mode
		if self.is_file_mode and not self.disable_backup:
			self.writeJson(self.data)

		return {"success": f"{len(records)} records inserted at {path}"}


	def insertChild(self, path, parentCondition, omitConditions, childField, childData):
		"""
		Inserts a child record into a nested field of parent records that match the given conditions.

		:param path: The JSON path where the parent records are located.
		:param parentCondition: Conditions that a parent record must meet to receive the child data.
		:param omitConditions: Conditions that prevent a parent record from receiving the child data.
		:param childField: The field inside the parent record where the child data should be inserted.
		:param childData: The data to insert as a child.
		:return: Success or error message.
		"""
		records = self.jsonByPath(path)
		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of parent records"}

		modified = False

		for record in records:
			if self.matchConditions(record, parentCondition) and not self.matchConditions(record, omitConditions):
				if childField not in record:
					record[childField] = []  # Initialize child list if it doesn't exist
				if not isinstance(record[childField], list):
					return {"error": f"Field '{childField}' is not a list in some records"}

				record[childField].append(childData)
				modified = True

		if not modified:
			return {"error": "No matching parent records found for insertion"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": "Child data inserted successfully"}


	def find(self, path, searchConditions=None, omitConditions=None):
		"""
		Finds records in the JSON structure at the given path that match search conditions
		and do not match omit conditions.

		:param path: The JSON path where records should be searched.
		:param searchConditions: Dictionary of conditions that records must match.
		:param omitConditions: Dictionary of conditions that records must not match.
		:return: List of matching records.
		"""
		# db.find("settings", {"theme": {"==": "dark"}})
		# db.find("users", {"age": {">": 30}})



		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		# Apply filtering based on search and omit conditions
		filtered_records = [
			record for record in records
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions)
		]

		return filtered_records


	def findOne(self, path, searchConditions=None, omitConditions=None):
		"""
		Finds a single record in the JSON structure at the given path that matches search conditions
		and does not match omit conditions.

		:param path: The JSON path where records should be searched.
		:param searchConditions: Dictionary of conditions that the record must match.
		:param omitConditions: Dictionary of conditions that the record must not match.
		:return: The first matching record or None if no match is found.
		"""

		# db.findOne("users", {"role": {"==": "admin"}})
		# db.findOne("users", {}, {"role": {"==": "user"}})
		# db.findOne("users", {"age": {">": 30}})
		# db.findOne("settings", {"theme": {"==": "dark"}})




		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		# Find the first matching record
		for record in records:
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions):
				return record

		return None  # No matching record found


	def updateNestedField(self, path, searchConditions, omitConditions, field, nestedUpdates):
		"""
		Updates a nested field inside records that match the search conditions and do not match omit conditions.

		:param path: The JSON path where records should be searched.
		:param searchConditions: Conditions that records must match.
		:param omitConditions: Conditions that records must not match.
		:param field: The nested field that needs to be updated.
		:param nestedUpdates: The new data to apply to the nested field.
		:return: Success or error message.
		"""

		# db.updateNestedField("users", {"id": {"==": 1}}, {}, "settings", {"theme": "dark", "notifications": False})
		# db.updateNestedField("users", {"id": {"==": 2}}, {}, "preferences", {"newsletter": True})
		# db.updateNestedField("settings", {"theme": {"==": "light"}}, {}, "language", "fr")



		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		modified = False

		for record in records:
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions):
				if field in record and isinstance(record[field], dict):
					# Merge nested dictionary updates
					self.mergeData(record[field], nestedUpdates, overwriteIfExists=True)
				else:
					record[field] = nestedUpdates  # Directly assign the new value if field is missing
				modified = True

		if not modified:
			return {"error": "No matching records found for update"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Nested field '{field}' updated successfully"}


	def deleteNestedField(self, path, searchConditions, omitConditions, nestedField):
		"""
		Deletes a nested field inside records that match the search conditions and do not match omit conditions.

		:param path: The JSON path where records should be searched.
		:param searchConditions: Conditions that records must match.
		:param omitConditions: Conditions that records must not match.
		:param nestedField: The field inside matching records to be deleted.
		:return: Success or error message.
		"""

		# db.deleteNestedField("users", {"id": {"==": 1}}, {}, "settings")
		# db.deleteNestedField("users", {}, {"id": {"==": 1}}, "preferences")
		# db.deleteNestedField("settings", {"theme": {"==": "light"}}, {}, "language")




		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		modified = False

		for record in records:
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions):
				if nestedField in record:
					del record[nestedField]
					modified = True

		if not modified:
			return {"error": "No matching records found for deletion"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Nested field '{nestedField}' deleted successfully"}


	def computeField(self, path, operation, computeField, searchConditions=None, omitConditions=None):
		"""
		Computes a new field based on an operation involving other fields within records at a given path.

		:param path: The JSON path where records should be searched.
		:param operation: The mathematical expression to evaluate (e.g., "price * quantity").
		:param computeField: The name of the field where the computed value will be stored.
		:param searchConditions: Conditions that records must match.
		:param omitConditions: Conditions that records must not match.
		:return: Success or error message.
		"""

		# db.computeField("orders", "price * quantity", "totalPrice")
		# db.computeField("orders", "price * 0.1", "discountPrice")
		# db.computeField("orders", "price * quantity", "totalPrice", {"quantity": {">": 3}})
		# db.computeField("orders", "price * tax", "taxedPrice")





		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		modified = False

		for record in records:
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions):
				try:
					# Extract fields from the record and evaluate the operation
					computed_value = eval(operation, {}, record)
					record[computeField] = computed_value
					modified = True
				except Exception as e:
					return {"error": f"Failed to compute field '{computeField}': {str(e)}"}

		if not modified:
			return {"error": "No matching records found for computation"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Computed field '{computeField}' updated successfully"}


	def beginTransaction(self):
		"""
		Starts a new transaction by saving a copy of the current data state.
		Prevents starting another transaction if one is already in progress.

		:return: Success or error message.
		"""

		# db.beginTransaction()



		if self.transaction_data is not None:
			return {"error": "Transaction already in progress"}

		# Store a deep copy of the current data to allow rollback
		self.transaction_data = json.loads(json.dumps(self.data))  # Deep copy

		return {"success": "Transaction started"}

	def commit(self):
		"""
		Commits the current transaction, making all changes permanent.
		Clears the transaction backup once committed.

		:return: Success or error message.
		"""

		# db.beginTransaction()  # Start transaction
		# db.insert("users", {"id": 3, "name": "Alice"})  # Insert a new record
		# db.commit()  # Make the changes permanent


		if self.transaction_data is None:
			return {"error": "No active transaction to commit"}

		# Clear transaction data since changes are now permanent
		self.transaction_data = None

		# Write changes to file if in file mode
		if self.is_file_mode and not self.disable_backup:
			self.writeJson(self.data)

		return {"success": "Transaction committed"}


	def rollback(self):
		"""
		Rolls back the current transaction, restoring the data to its previous state.

		:return: Success or error message.
		"""

		# db.beginTransaction()  # Start transaction
		# db.insert("users", {"id": 3, "name": "Alice"})  # Insert a new record
		# db.rollback()  # Undo the insert



		if self.transaction_data is None:
			return {"error": "No active transaction to roll back"}

		# Restore the original data from the transaction backup
		self.data = self.transaction_data
		self.transaction_data = None  # Clear the transaction backup

		return {"success": "Transaction rolled back"}


	def deleteChild(self, path, parentCondition, omitConditions, childField, childCondition):
		"""
		Deletes child records from a nested field within parent records that match the search conditions.

		:param path: The JSON path where parent records should be searched.
		:param parentCondition: Conditions that parent records must match.
		:param omitConditions: Conditions that parent records must not match.
		:param childField: The nested list field from which child records will be deleted.
		:param childCondition: Conditions that a child record must match to be deleted.
		:return: Success or error message.
		"""

		# db.deleteChild("users", {"id": {"==": 1}}, {}, "phoneNumbers", {"type": {"==": "work"}})
		# db.deleteChild("users", {}, {"id": {"==": 2}}, "permissions", {"role": {"==": "editor"}})




		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of parent records"}

		modified = False

		for parent in records:
			if self.matchConditions(parent, parentCondition) and not self.matchConditions(parent, omitConditions):
				if childField in parent and isinstance(parent[childField], list):
					# Filter out children that match the deletion condition
					new_children = [child for child in parent[childField] if not self.matchConditions(child, childCondition)]
					
					if len(new_children) != len(parent[childField]):
						parent[childField] = new_children  # Apply filtered child list
						modified = True

		if not modified:
			return {"error": "No matching child records found for deletion"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": f"Child records deleted from '{childField}'"}


	def findLimited(self, path, searchConditions=None, omitConditions=None, limit=10, offset=0):
		"""
		Finds a limited number of records in the JSON structure at the given path
		that match search conditions and do not match omit conditions.

		:param path: The JSON path where records should be searched.
		:param searchConditions: Dictionary of conditions that records must match.
		:param omitConditions: Dictionary of conditions that records must not match.
		:param limit: Maximum number of records to return.
		:param offset: Number of records to skip before returning results.
		:return: A limited list of matching records.
		"""

		# db.findLimited("users", {}, {}, limit=2, offset=1)
		# db.findLimited("users", {"role": {"==": "admin"}}, {}, limit=3, offset=2)
		# db.findLimited("settings", {}, {}, limit=5)



		records = self.find(path, searchConditions, omitConditions)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		return records[offset:offset + limit]


	def updateMany(self, path, searchConditions=None, omitConditions=None, updates=None):
		"""
		Updates multiple records in a JSON structure at the given path
		that match search conditions and do not match omit conditions.

		:param path: The JSON path where records should be updated.
		:param searchConditions: Dictionary of conditions that records must match.
		:param omitConditions: Dictionary of conditions that records must not match.
		:param updates: Dictionary of updates to apply to matching records.
		:return: Success or error message.
		"""

		# db.updateMany("users", {"role": {"==": "user"}}, {}, {"status": "inactive"})
		# db.updateMany("users", {"role": {"==": "admin"}}, {"id": {"==": 1}}, {"status": "superadmin"})
		# db.updateMany("settings", {"theme": {"==": "light"}}, {}, {"theme": "dark"})





		records = self.jsonByPath(path)

		if not isinstance(records, list):
			return {"error": "Target path does not contain a list of records"}

		if not updates or not isinstance(updates, dict):
			return {"error": "Updates must be a valid dictionary"}

		modified = False

		for record in records:
			if self.matchConditions(record, searchConditions) and not self.matchConditions(record, omitConditions):
				# Apply updates
				for key, value in updates.items():
					record[key] = value
				modified = True

		if not modified:
			return {"error": "No records matched update conditions"}

		self.overwriteEnd(path, json.dumps(records))
		return {"success": "Records updated successfully"}


	def findRegex(self, path, field, pattern):
		records = self.jsonByPath(path)
		if not records:
			return {"error": "No records found at path: " + path}

		return [r for r in records if re.match(pattern, r[field])]

	def findProjected(self, path, search_conditions=None, omit_conditions=None, fields=None):
		records = self.find(path, search_conditions, omit_conditions)
		return [{field: record[field] for field in fields if field in record} for record in records]

	def navigateOrCreate(self, path):
		"""
		Ensures the path exists as a dictionary in self.data, creating dicts along the way if needed.
		Returns the reference to the final sub-dict.
		"""
		keys = path.split('.')
		temp = self.data
		for k in keys:
			if k not in temp or not isinstance(temp[k], dict):
				# Create a dict if it doesn't exist or it's not a dict
				temp[k] = {}
			temp = temp[k]
		return temp

	def mergePathProtected(self, path, backupData, protect):
		"""
		Merges `backupData` only at the given `path` in self.data, skipping any dotted keys in `protect`.
		
		1. Use `indexJson` to check if `path` is in the index (full dotted path).
		2. If the path doesn't exist, create it as a dict.
		3. Merge `backupData` into that sub-dictionary with field-level protection.
		4. Update `self.index` after merging.
		"""
		# Refresh or get a fresh index of current data
		self.index = self.indexJson(self.data)

		# 1. Check if the full dotted path is recognized as existing in self.index
		#    (meaning it's a "leaf" or final value). But we actually want
		#    to treat the path as a sub-dict. So if it's not in index, we assume partial or no existence.
		if path not in self.index:
			# This means there's no exact "leaf" value at that path (maybe doesn't exist or is partially missing).
			# We'll ensure the path leads to a dict (potentially newly created).
			subDictRef = self.navigateOrCreate(path)
		else:
			# If path is in the index, it might currently be a leaf. We want to convert it into a dict if it's not one.
			# We'll attempt to "navigate" anyway; if it's not a dict, we'll forcibly turn it into one.
			subCheck = self.jsonByPath(path)
			if isinstance(subCheck, dict):
				# It's already a dict
				subDictRef = subCheck
			else:
				# If it's not a dict (leaf), replace that leaf with a dict
				parentKeys = path.split('.')[:-1]
				lastKey = path.split('.')[-1]
				
				# Navigate to parent
				temp = self.data
				for k in parentKeys:
					if k not in temp or not isinstance(temp[k], dict):
						temp[k] = {}
					temp = temp[k]
				
				# Overwrite the leaf with an empty dict
				temp[lastKey] = {}
				subDictRef = temp[lastKey]

		# 2. Now we do the protected merge from backupData into subDictRef
		#    ignoring dotted keys in `protect`
		self.mergeProtected(backupData, subDictRef, protect, prefix="")  # prefix is blank since we are merging into subDictRef

		# 3. Optionally, update self.index to reflect new changes
		self.index = self.indexJson(self.data)

		# If you have file mode, you can write here...
		# if self.is_file_mode:
		#     self.writeJson(self.data)

		return {"success": f"Merged data into path '{path}', respecting protected fields."}

	def mergeProtected(self, backup, current, protect, prefix=""):
		"""
		Recursively merges `backup` into `current`, skipping any full dotted key in `protect`.
		This version tracks the dotted path as we descend.
		"""
		if not isinstance(backup, dict) or not isinstance(current, dict):
			# If either is not dict, overwrite if the current path isn't protected
			if prefix not in protect:
				return backup
			else:
				return current

		for key, backupValue in backup.items():
			full_path = f"{prefix}.{key}" if prefix else key
			if full_path in protect:
				# Skip overwriting a fully protected path
				continue

			currentValue = current.get(key)
			if isinstance(backupValue, dict) and isinstance(currentValue, dict):
				current[key] = self.mergeProtected(backupValue, currentValue, protect, full_path)
			else:
				current[key] = self.mergeProtected(backupValue, currentValue, protect, full_path)

		return current


	def findDifferences(self, oldData, newData, path=""):
		"""
		Compares two JSON structures and returns the differences.

		:param oldData: The original JSON data.
		:param newData: The modified JSON data.
		:param path: (Internal) Tracks the JSON path for nested fields.
		:return: Dictionary containing changed, added, and removed fields.
		"""

		# db.findDifferences(old_data, new_data)


		differences = {}

		# Detect removed keys
		for key in oldData:
			full_path = f"{path}.{key}" if path else key
			if key not in newData:
				differences[full_path] = {"removed": oldData[key]}

		# Detect added or changed keys
		for key, new_value in newData.items():
			full_path = f"{path}.{key}" if path else key
			old_value = oldData.get(key, None)

			if key not in oldData:
				differences[full_path] = {"added": new_value}
			elif isinstance(new_value, dict) and isinstance(old_value, dict):
				# Recursively check nested dictionaries
				nested_diff = self.findDifferences(old_value, new_value, full_path)
				differences.update(nested_diff)
			elif old_value != new_value:
				differences[full_path] = {"changed": {"old": old_value, "new": new_value}}

		return differences


	def getJson(self):
		return json.dumps(self.data, indent=4)

# Additional methods like aggregate, findSorted, backupChanges, recoverPath etc. need to be similarly detailed.