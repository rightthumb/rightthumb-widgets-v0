import os
import requests
import json

class SleekDBClient:
    def __init__(self, url="http://localhost/index.php", db_folder_name="data"):
        self.url = url

        # Always use the terminal's current working directory
        self.db_path = os.path.join(os.getcwd(), db_folder_name)

        # Ensure the folder exists
        os.makedirs(self.db_path, exist_ok=True)

    def call(self, action, collection, params=None, debug=False):
        data = {
            "action": action,
            "collection": collection,
            "params": params or {},
            "db": self.db_path
        }

        response = requests.post(self.url, json=data)
        try:
            result = response.json()
        except Exception as e:
            print(f"[!] Failed to decode JSON: {e}")
            print(response.text)
            return None

        if debug:
            print(json.dumps(result, indent=4))

        if not result.get('success', True):
            print(f"[!] SleekDB Error: {result.get('error')}")
        return result.get('result')

    # CRUD Aliases
    def insert(self, collection, records): return self.call("insert", collection, {"records": records})
    def find(self, collection, filter={}): return self.call("find", collection, {"filter": filter})
    def findOne(self, collection, filter={}): return self.call("findOne", collection, {"filter": filter})
    def update(self, collection, filter, update): return self.call("update", collection, {"filter": filter, "update": update})
    def updateOrInsert(self, collection, filter, record): return self.call("updateOrInsert", collection, {"filter": filter, "record": record})
    def delete(self, collection, filter): return self.call("delete", collection, {"filter": filter})

    # Child operations
    def insertChild(self, collection, parent, field, child):
        return self.call("insertChild", collection, {
            "parent": parent,
            "field": field,
            "child": child
        })

    def insertRecordsChild(self, collection, parent, field, children):
        return self.call("insertRecordsChild", collection, {
            "parent": parent,
            "field": field,
            "children": children
        })

    def updateChild(self, collection, parent, field, filter, update):
        return self.call("updateChild", collection, {
            "parent": parent,
            "field": field,
            "filter": filter,
            "update": update
        })

    def updateNestedField(self, collection, filter, field, update):
        return self.call("updateNestedField", collection, {
            "filter": filter,
            "field": field,
            "update": update
        })

    def deleteNestedField(self, collection, filter, field):
        return self.call("deleteNestedField", collection, {
            "filter": filter,
            "field": field
        })

    def deleteChild(self, collection, parent, field, filter):
        return self.call("deleteChild", collection, {
            "parent": parent,
            "field": field,
            "filter": filter
        })

    def findChild(self, collection, parent, field, filter={}):
        return self.call("findChild", collection, {
            "parent": parent,
            "field": field,
            "filter": filter
        })

    def findOneChild(self, collection, parent, field, filter={}):
        return self.call("findOneChild", collection, {
            "parent": parent,
            "field": field,
            "filter": filter
        })

    # Raw SQL-style commands
    def sql(self, collection, sub_action, params):
        params = dict(params)
        params["action"] = sub_action
        return self.call("sql", collection, params)

    # Diagnostics
    def logs(self, collection="_"): return self.call("log", collection)
    def close(self): return self.call("close", "_")

