import pymongo
import uuid
from datetime import datetime
from pymongo import MongoClient


class MongoDBMgr:
    def __init__(self, database, uri="mongodb://localhost:27017/"):
        """Initializes MongoDB connection."""
        self.logs = ["fn: __init__"]
        self.logs.append(f"init: {database}")
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def insert(self, collection_name, records):
        """Inserts multiple records into a collection, ensuring unique _id."""
        self.logs.append("fn: insert")
        collection = self.db[collection_name]

        if isinstance(records, dict):  # Handle single record insertion
            records = [records]

        for record in records:
            if "_id" not in record:
                record["_id"] = self.generate_object_id()
            record = self.serialize_special_types(record)
        
        result = collection.insert_many(records)
        self.logs.append(f"Inserted {len(result.inserted_ids)} records into {collection_name}")

    def insertChild(self, collection_name, parent_condition, child_field, child_data):
        """Inserts a child object into an array inside a parent document."""
        self.logs.append("fn: insertChild")
        collection = self.db[collection_name]

        if "_id" not in child_data:
            child_data["_id"] = self.generate_object_id()

        update_result = collection.update_one(
            parent_condition,
            {"$push": {child_field: self.serialize_special_types(child_data)}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Inserted child into {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"Parent record not found for {parent_condition}")
            return False

    def insertRecordsChild(self, collection_name, parent_condition, child_field, child_records):
        """Inserts multiple child objects into an array inside a parent document."""
        self.logs.append("fn: insertRecordsChild")
        collection = self.db[collection_name]

        for record in child_records:
            if "_id" not in record:
                record["_id"] = self.generate_object_id()

        update_result = collection.update_one(
            parent_condition,
            {"$push": {child_field: {"$each": self.serialize_special_types(child_records)}}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Inserted {len(child_records)} children into {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"Parent record not found for {parent_condition}")
            return False

    def updateChild(self, collection_name, parent_condition, child_field, child_condition, updated_data):
        """Updates a specific child inside an array in a parent document."""
        self.logs.append("fn: updateChild")
        collection = self.db[collection_name]

        update_result = collection.update_one(
            {**parent_condition, f"{child_field}._id": child_condition["_id"]},
            {"$set": {f"{child_field}.$": updated_data}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Updated child in {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"No matching child found for update")
            return False

    def update_nested_field(self, collection_name, conditions, field, nested_updates):
        """Updates a nested field inside a document."""
        self.logs.append("fn: update_nested_field")
        collection = self.db[collection_name]

        update_result = collection.update_one(
            conditions,
            {"$set": {field: nested_updates}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Updated {field}: {nested_updates}")
            return True
        else:
            self.logs.append(f"Record not found.")
            return False

    def delete_nested_field(self, collection_name, conditions, nested_field):
        """Deletes a specific nested field in a document."""
        self.logs.append("fn: delete_nested_field")
        collection = self.db[collection_name]

        update_result = collection.update_one(
            conditions,
            {"$unset": {nested_field: ""}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Deleted {nested_field}")
            return True
        else:
            self.logs.append(f"Field {nested_field} not found.")
            return False

    def deleteChild(self, collection_name, parent_condition, child_field, child_condition):
        """Removes a specific child object from an array in a parent document."""
        self.logs.append("fn: deleteChild")
        collection = self.db[collection_name]

        update_result = collection.update_one(
            parent_condition,
            {"$pull": {child_field: child_condition}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Deleted child from {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"No matching child found for deletion")
            return False

    def delete(self, collection_name, conditions):
        """Deletes documents matching the conditions."""
        self.logs.append("fn: delete")
        collection = self.db[collection_name]

        delete_result = collection.delete_many(conditions)

        self.logs.append(f"Deleted {delete_result.deleted_count} documents from {collection_name}")
        return delete_result.deleted_count > 0

    def find(self, collection_name, conditions={}):
        """Finds multiple records that match the given conditions."""
        self.logs.append("fn: find")
        collection = self.db[collection_name]

        return list(collection.find(conditions))

    def findOne(self, collection_name, conditions={}):
        """Finds a single record that matches the given conditions."""
        self.logs.append("fn: findOne")
        collection = self.db[collection_name]

        return collection.find_one(conditions)

    def findChild(self, collection_name, parent_condition, child_field, child_condition={}):
        """Finds all child objects in an array inside a parent document."""
        self.logs.append("fn: findChild")
        parent_record = self.findOne(collection_name, parent_condition)

        if not parent_record or child_field not in parent_record:
            self.logs.append(f"Parent or child field missing in {collection_name}")
            return []

        return [child for child in parent_record[child_field] if self.match_conditions(child, child_condition)]

    def findOneChild(self, collection_name, parent_condition, child_field, child_condition={}):
        """Finds a single child object inside an array in a parent document."""
        self.logs.append("fn: findOneChild")
        parent_record = self.findOne(collection_name, parent_condition)

        if not parent_record or child_field not in parent_record:
            self.logs.append(f"Parent or child field missing in {collection_name}")
            return None

        for child in parent_record[child_field]:
            if self.match_conditions(child, child_condition):
                return child

        return None

    def match_conditions(self, record, conditions):
        """Matches a record against conditions."""
        for key, condition in conditions.items():
            field_value = record.get(key, None)

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

    def close(self):
        """Closes the MongoDB connection."""
        self.client.close()
        self.logs.append("Database connection closed.")
