import uuid
import math
from datetime import datetime, timezone
from typing import Any, Dict
import re

import pymongo # type: ignore
from pymongo import MongoClient # type: ignore
from pymongo.errors import BulkWriteError # type: ignore
from bson.objectid import ObjectId # type: ignore
from bson.binary import Binary # type: ignore
from bson.decimal128 import Decimal128 # type: ignore
from decimal import Decimal

INT64_MIN = -(2**63)
INT64_MAX = (2**63) - 1

class MongoDBMgr:
    def __init__(self, database, uri="mongodb://localhost:27017/", sanitize_keys=False):
        """Initializes MongoDB connection."""
        self.logs = ["fn: __init__"]
        self.logs.append(f"init: {database}")
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.sanitize_keys = sanitize_keys  # set True if you expect '.' or leading '$' in keys

    # ---------- BSON safety helpers ----------
    def _sanitize_key(self, key: str) -> str:
        if not isinstance(key, str):
            key = str(key)
        k = key.replace(".", "·")
        if k.startswith("$"):
            k = "﹩" + k[1:]
        return k

    def _sanitize_dict_keys(self, d: Dict[str, Any]) -> Dict[str, Any]:
        if not self.sanitize_keys:
            return d
        out = {}
        for k, v in d.items():
            out[self._sanitize_key(k)] = v
        return out

    def _to_bson_safe(self, obj: Any) -> Any:
        """Recursively convert to types accepted by PyMongo/BSON."""

        if obj is None or isinstance(obj, (bool, str)):
            return obj

        if isinstance(obj, Decimal):
            try:
                return Decimal128(str(obj))
            except Exception:
                return float(obj)

        if isinstance(obj, float):
            if math.isnan(obj) or math.isinf(obj):
                return None
            return obj

        if isinstance(obj, int):
            if obj < INT64_MIN or obj > INT64_MAX:
                return Decimal128(str(obj))
            return obj

        if isinstance(obj, datetime):
            # Force UTC tz-aware
            if obj.tzinfo is None:
                return obj.replace(tzinfo=timezone.utc)
            return obj.astimezone(timezone.utc)

        if isinstance(obj, (bytes, bytearray)):
            return Binary(bytes(obj))

        if isinstance(obj, (set, tuple, list)):
            return [self._to_bson_safe(x) for x in obj]

        if isinstance(obj, dict):
            clean = self._sanitize_dict_keys(obj)
            return {k: self._to_bson_safe(v) for k, v in clean.items()}

        # Unknown custom types: stringify
        return str(obj)

    # ---------- Public API ----------
    def insert(self, collection_name, records):
        """Inserts one or many records; ensures _id and BSON-safe types."""
        self.logs.append("fn: insert")
        collection = self.db[collection_name]

        if isinstance(records, dict):
            records = [records]

        safe_docs = []
        for record in records:
            rec = dict(record)
            if "_id" not in rec or rec["_id"] is None:
                rec["_id"] = self.generate_object_id()
            else:
                # If user passed string UUID, let it be; if 24-hex, make ObjectId
                if isinstance(rec["_id"], str) and len(rec["_id"]) == 24:
                    try:
                        rec["_id"] = ObjectId(rec["_id"])
                    except Exception:
                        pass
            rec = self._to_bson_safe(rec)
            safe_docs.append(rec)

        try:
            result = collection.insert_many(safe_docs, ordered=False)
            self.logs.append(f"Inserted {len(result.inserted_ids)} records into {collection_name}")
        except BulkWriteError as e:
            self.logs.append(f"Bulk insert error: {e.details}")

    def insertChild(self, collection_name, parent_condition, child_field, child_data, safe=False):
        """Push a child object into an array field in the parent doc."""
        if safe:
            parent_condition = self._to_bson_safe(parent_condition)
        self.logs.append("fn: insertChild")
        collection = self.db[collection_name]

        child = dict(child_data)
        if "_id" not in child or child["_id"] is None:
            child["_id"] = self.generate_object_id()
        child = self._to_bson_safe(child)

        update_result = collection.update_one(
            parent_condition,
            {"$push": {child_field: child}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Inserted child into {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"Parent record not found for {parent_condition}")
            return False

    def insertRecordsChild(self, collection_name, parent_condition, child_field, child_records, safe=False):
        """Push many child objects into an array field in the parent doc."""
        if safe:
            parent_condition = self._to_bson_safe(parent_condition)
        self.logs.append("fn: insertRecordsChild")
        collection = self.db[collection_name]

        children = []
        for record in child_records:
            child = dict(record)
            if "_id" not in child or child["_id"] is None:
                child["_id"] = self.generate_object_id()
            children.append(self._to_bson_safe(child))

        update_result = collection.update_one(
            parent_condition,
            {"$push": {child_field: {"$each": children}}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Inserted {len(children)} children into {child_field} in {collection_name}")
            return True
        else:
            self.logs.append(f"Parent record not found for {parent_condition}")
            return False

    def updateChild(self, collection_name, parent_condition, child_field, child_condition, updated_data, safe=False):
        """Replace a specific child in an array (matched by _id) with updated_data."""
        if safe:
            parent_condition = self._to_bson_safe(parent_condition)
            child_condition = self._to_bson_safe(child_condition)

        self.logs.append("fn: updateChild")
        collection = self.db[collection_name]

        # Ensure we match on child's _id
        if "_id" not in child_condition:
            self.logs.append("updateChild requires child_condition with _id")
            return False

        # If _id is 24-hex, coerce to ObjectId to match stored value
        cc = dict(child_condition)
        if isinstance(cc["_id"], str) and len(cc["_id"]) == 24:
            try:
                cc["_id"] = ObjectId(cc["_id"])
            except Exception:
                pass

        update_result = collection.update_one(
            {**parent_condition, f"{child_field}._id": cc["_id"]},
            {"$set": {f"{child_field}.$": self._to_bson_safe(updated_data)}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Updated child in {child_field} in {collection_name}")
            return True
        else:
            self.logs.append("No matching child found for update")
            return False

    def update_nested_field(self, collection_name, conditions, field, nested_updates, safe=False):
        """Set a nested field (dot notation) on a document."""
        if safe:
            conditions = self._to_bson_safe(conditions)
        self.logs.append("fn: update_nested_field")
        collection = self.db[collection_name]

        update_result = collection.update_one(
            conditions,
            {"$set": {field: self._to_bson_safe(nested_updates)}}
        )

        if update_result.modified_count > 0:
            self.logs.append(f"Updated {field}: {nested_updates}")
            return True
        else:
            self.logs.append("Record not found.")
            return False

    def delete_nested_field(self, collection_name, conditions, nested_field, safe=False):
        """Unset a nested field (dot notation)."""
        if safe:
            conditions = self._to_bson_safe(conditions)
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

    def deleteChild(self, collection_name, parent_condition, child_field, child_condition, safe=False):
        """Pull a matching child object from an array."""
        if safe:
            parent_condition = self._to_bson_safe(parent_condition)
            child_condition = self._to_bson_safe(child_condition)

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
            self.logs.append("No matching child found for deletion")
            return False

    def delete(self, collection_name, conditions, safe=False):
        """Delete documents matching conditions."""
        if safe:
            conditions = self._to_bson_safe(conditions)
        self.logs.append("fn: delete")
        collection = self.db[collection_name]
        delete_result = collection.delete_many(conditions)
        self.logs.append(f"Deleted {delete_result.deleted_count} documents from {collection_name}")
        return delete_result.deleted_count > 0

    def find(self, collection_name, conditions={}, safe=False):
        """Find many documents."""
        if safe:
            conditions = self._to_bson_safe(conditions)
        self.logs.append("fn: find")
        collection = self.db[collection_name]
        return list(collection.find(conditions))

    def findOne(self, collection_name, conditions={}, safe=False):
        """Find one document."""
        if safe:
            conditions = self._to_bson_safe(conditions)
        self.logs.append("fn: findOne")
        collection = self.db[collection_name]
        return collection.find_one(conditions)

    def findChild(self, collection_name, parent_condition, child_field, child_condition={}):
        """Return all children under child_field that match child_condition."""
        self.logs.append("fn: findChild")
        parent_record = self.findOne(collection_name, parent_condition)
        if not parent_record or child_field not in parent_record:
            self.logs.append(f"Parent or child field missing in {collection_name}")
            return []
        return [child for child in parent_record[child_field] if self.match_conditions(child, child_condition)]

    def findOneChild(self, collection_name, parent_condition, child_field, child_condition={}):
        """Return first matching child under child_field."""
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
        """Simple in-Python matcher (for in-memory child filtering)."""
        for key, condition in conditions.items():
            field_value = record.get(key, None)
            if isinstance(condition, dict):
                for operator, value in condition.items():
                    if not self.match_operator(field_value, operator, value):
                        return False
            elif field_value != condition:
                return False
        return True

    def match_operator(self, field_value, operator, value):
        """Extend if you need operators like $gt/$lt etc for in-memory checks."""
        if operator in ("$eq",):
            return field_value == value
        if operator in ("$ne",):
            return field_value != value
        if operator in ("$gt",):
            return field_value is not None and field_value > value
        if operator in ("$gte",):
            return field_value is not None and field_value >= value
        if operator in ("$lt",):
            return field_value is not None and field_value < value
        if operator in ("$lte",):
            return field_value is not None and field_value <= value
        if operator in ("$in",):
            return field_value in value
        if operator in ("$nin",):
            return field_value not in value
        # default: unknown operator -> no match
        return False

    def generate_object_id(self):
        """Return a real BSON ObjectId (preferred)."""
        return ObjectId()

    def close(self):
        """Close the MongoDB connection."""
        self.client.close()
        self.logs.append("Database connection closed.")




    def toQuery(self,field="title", has=None, omit=None ):
        """
        Convert lists of include/exclude patterns into a MongoDB query.
        
        has:  list of strings or lists of strings
            ['a', 'b']       => a AND b
            [['a','b'], 'c'] => (a OR b) AND c
        omit: list of strings or lists of strings
            works same as has, but negates
        field: MongoDB field name to search in
        """
        has = has or []
        omit = omit or []

        def pattern_to_regex(pattern):
            pattern = re.escape(pattern).replace(r"\*", ".*").replace(r"\?", ".")
            return re.compile(pattern, re.IGNORECASE)

        def build_group(terms, negate=False):
            """Build a Mongo $or/$and group for a list of terms."""
            if isinstance(terms, str):
                terms = [terms]
            if not isinstance(terms, (list, tuple)):
                raise ValueError("Terms must be string or list of strings")

            # OR inside group
            ors = []
            for term in terms:
                if negate:
                    ors.append({field: {"$not": pattern_to_regex(term)}})
                else:
                    ors.append({field: pattern_to_regex(term)})

            if len(ors) == 1:
                return ors[0]
            return {"$or": ors} if not negate else {"$and": ors}

        query_parts = []

        # Positive matches (has)
        for item in has:
            query_parts.append(build_group(item, negate=False))

        # Negative matches (omit)
        for item in omit:
            query_parts.append(build_group(item, negate=True))

        if not query_parts:
            return {}

        if len(query_parts) == 1:
            return query_parts[0]
        return {"$and": query_parts}

