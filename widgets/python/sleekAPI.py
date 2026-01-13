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



'''
# what does this do?

That Python code defines a **client class (`SleekDBClient`)** that talks to a server (likely a PHP backend) using **HTTP POST requests** to perform CRUD (Create, Read, Update, Delete) operations on a SleekDB-like database.

Here’s the breakdown:

---

### **Main purpose**

It’s a wrapper around `requests.post` to send JSON commands to a given URL (default `http://localhost/index.php`) for database operations.

---

### **Key points**

1. **Initialization (`__init__`)**

   * Stores the target URL for API calls.
   * Builds a database path (`self.db_path`) based on the current working directory and a folder name (`data` by default).
   * Creates the folder if it doesn’t exist.

2. **`call()` method**

   * Sends an HTTP POST with:

     ```json
     {
         "action": <what to do>,
         "collection": <table or collection name>,
         "params": {...},
         "db": <absolute path to db folder>
     }
     ```
   * Tries to parse JSON response.
   * Optionally pretty-prints the result if `debug=True`.
   * Handles errors if the server says `success` is `false`.

3. **CRUD Aliases**

   * `insert`, `find`, `findOne`, `update`, `updateOrInsert`, `delete`
   * Just shortcuts that call `call()` with the right `action` and parameters.

4. **Child operations**

   * Functions like `insertChild`, `updateChild`, `findChild` let you modify nested/related records inside a parent record.

5. **SQL-like commands**

   * `sql(collection, sub_action, params)` sends SQL-style requests (still in JSON form) to the server.

6. **Diagnostics**

   * `logs()` gets logs.
   * `close()` closes the database connection (server-side).

---

### **So what it does in practice**

If you run:

```python
client = SleekDBClient()
client.insert("users", [{"name": "Alice"}])
```

…it sends something like:

```json
POST http://localhost/index.php
{
    "action": "insert",
    "collection": "users",
    "params": {"records": [{"name": "Alice"}]},
    "db": "/your/current/path/data"
}
```

The server handles this request and returns a JSON response (success/failure + data).

---

This means the Python script is **not the database itself** — it’s just the client talking to a backend (probably PHP + SleekDB).

If you want, I can also show you **exactly what network traffic this would generate** for one of the methods so you can see the raw request. Would you like me to do that?



'''