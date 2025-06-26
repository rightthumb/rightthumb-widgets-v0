
### **Explanation of MongoDB-Like Query Operators (`$ne`, `$in`, `$size`, etc.)**

In **UnQLite**, we mimic MongoDB’s query operators to filter data efficiently. These **operators** allow you to perform **advanced searches** on documents.

---

### **1. `$eq` (Equal)**

Finds records where a field **exactly matches** a value.

```python
db.find("users", {"name": {"$eq": "Alice"}})
```

✅ Finds users **where `name` is exactly `"Alice"`**.

---

### **2. `$ne` (Not Equal)**

Finds records where a field is **NOT equal** to a value.

```python
db.find("users", {"name": {"$ne": "Alice"}})
```

✅ Finds **users whose `name` is NOT `"Alice"`**.

---

### **3. `$gt` (Greater Than)**

Finds records where a field is **greater than** a value.

```python
db.find("users", {"age": {"$gt": 25}})
```

✅ Finds **users older than `25`**.

---

### **4. `$gte` (Greater Than or Equal)**

Finds records where a field is **greater than or equal to** a value.

```python
db.find("users", {"age": {"$gte": 30}})
```

✅ Finds **users `30` or older**.

---

### **5. `$lt` (Less Than)**

Finds records where a field is **less than** a value.

```python
db.find("users", {"age": {"$lt": 40}})
```

✅ Finds **users younger than `40`**.

---

### **6. `$lte` (Less Than or Equal)**

Finds records where a field is **less than or equal to** a value.

```python
db.find("users", {"age": {"$lte": 30}})
```

✅ Finds **users `30` or younger**.

---

### **7. `$in` (Matches Any Value in a List)**

Finds records where a field **matches any value** in a given list.

```python
db.find("users", {"name": {"$in": ["Alice", "Bob", "Charlie"]}})
```

✅ Finds **users named `Alice`, `Bob`, or `Charlie`**.

---

### **8. `$nin` (Does NOT Match Any Value in a List)**

Finds records where a field **does NOT match any value** in a list.

```python
db.find("users", {"name": {"$nin": ["Alice", "Bob"]}})
```

✅ Finds **users NOT named `Alice` or `Bob`**.

---

### **9. `$size` (Match Array Length)**

Finds records where an **array field** has a specific number of elements.

```python
db.find("users", {"tags": {"$size": 2}})
```

✅ Finds **users who have exactly `2` tags**.

---

### **10. `$all` (Match All Values in an Array)**

Finds records where an **array contains ALL specified values**.

```python
db.find("users", {"tags": {"$all": ["developer", "python"]}})
```

✅ Finds **users who have BOTH `"developer"` and `"python"` in their `tags` array**.

---

### **11. `$exists` (Check If a Field Exists)**

Finds records where a **specific field is present** (or not).

```python
db.find("users", {"profile.bio": {"$exists": True}})
```

✅ Finds **users who have a `profile.bio` field**.

```python
db.find("users", {"profile.website": {"$exists": False}})
```

✅ Finds **users who DO NOT have a `profile.website` field**.

---

### **12. `$type` (Match Field Type)**

Finds records where a field is of a **specific type**.

```python
db.find("users", {"age": {"$type": "int"}})
```

✅ Finds **users where `age` is stored as an `integer`**.

---

### **13. `$regex` (Match a Pattern)**

Finds records where a **string field contains a pattern**.

```python
db.find("users", {"name": {"$regex": "^A"}})
```

✅ Finds **users whose names start with `"A"`**.

---

## **💡 Summary Table**

| **Operator** | **Description** | **Example** |
|-------------|---------------|------------|
| **`$eq`**  | Matches **exact** value | `{"name": {"$eq": "Alice"}}` |
| **`$ne`**  | **Not equal** to value | `{"age": {"$ne": 30}}` |
| **`$gt`**  | Greater than value | `{"age": {"$gt": 25}}` |
| **`$gte`** | Greater than or equal to value | `{"age": {"$gte": 30}}` |
| **`$lt`**  | Less than value | `{"age": {"$lt": 40}}` |
| **`$lte`** | Less than or equal to value | `{"age": {"$lte": 30}}` |
| **`$in`**  | Field matches any value in list | `{"name": {"$in": ["Alice", "Bob"]}}` |
| **`$nin`** | Field does **not** match any value in list | `{"name": {"$nin": ["Alice", "Bob"]}}` |
| **`$size`** | Matches **array length** | `{"tags": {"$size": 2}}` |
| **`$all`**  | Matches **all values** in an array | `{"tags": {"$all": ["python", "developer"]}}` |
| **`$exists`** | Checks if field exists | `{"profile.bio": {"$exists": True}}` |
| **`$type`** | Matches field type | `{"age": {"$type": "int"}}` |
| **`$regex`** | Matches a **text pattern** | `{"name": {"$regex": "^A"}}` |

---

## **Final Thoughts**

✅ **Easy-to-use query filters** for NoSQL-style searches  
✅ **Supports complex filtering on nested fields**  
✅ **Works with both primitive types and arrays**  

Would you like **more examples with nested queries or performance optimizations** next? 🚀

___

### **Simple & Complex Examples for Every Function in `UnQLiteMgr`**

Here’s a structured breakdown of **each function** in `UnQLiteMgr`, with **both simple and complex usage examples**.

---

## **1. `insert` (Insert a Document)**

### **Simple Example**

```python
db.insert("users", [{"_id": db.generate_object_id(), "name": "Alice", "age": 30}])
```

### **Complex Example**

```python
db.insert("users", [{
    "_id": db.generate_object_id(),
    "name": "Bob",
    "email": "bob@example.com",
    "profile": {
        "bio": "Software Engineer",
        "social": {"twitter": "@bob_dev", "github": "bob123"}
    },
    "tags": ["developer", "python", "database"]
}])
```

---

## **2. `find` (Find Multiple Records)**

### **Simple Example**

```python
users = db.find("users", {"name": "Alice"})
print(users)
```

### **Complex Example with Operators**

```python
results = db.find("users", {
    "age": {"$gte": 25},          # Age greater than or equal to 25
    "tags": {"$in": ["python"]}   # Has 'python' in tags
})
print(results)
```

---

## **3. `findOne` (Find a Single Record)**

### **Simple Example**

```python
user = db.findOne("users", {"name": "Alice"})
print(user)
```

### **Complex Example with Nested Fields**

```python
user = db.findOne("users", {"profile.social.twitter": "@bob_dev"})
print(user)
```

---

## **4. `match_conditions` (Match Records Against Conditions)**

### **Simple Example**

```python
user = {"name": "Alice", "age": 30}
conditions = {"name": "Alice", "age": {"$gte": 25}}
print(db.match_conditions(user, conditions))  # Output: True
```

### **Complex Example**

```python
user = {"name": "Bob", "tags": ["developer", "python", "database"]}
conditions = {"tags": {"$all": ["developer", "python"]}}  # Must contain both
print(db.match_conditions(user, conditions))  # Output: True
```

---

## **5. `insertChild` (Insert a Child Object in an Array)**

### **Simple Example**

```python
db.insertChild("articles", {"title": "Understanding UnQLite"}, "comments", {
    "comment_id": db.generate_object_id(),
    "user": "Jane Doe",
    "text": "Great article!",
    "timestamp": datetime.now()
})
```

### **Complex Example (Adding Multiple Nested Comments)**

```python
db.insertChild("articles", {"title": "Understanding UnQLite"}, "comments", {
    "comment_id": db.generate_object_id(),
    "user": {
        "user_id": db.generate_object_id(),
        "name": "Jane Doe"
    },
    "text": "This article was insightful!",
    "replies": [
        {"user": "John", "text": "I agree!", "timestamp": datetime.now()},
        {"user": "Mary", "text": "Well explained!", "timestamp": datetime.now()}
    ],
    "timestamp": datetime.now()
})
```

---

## **6. `findChild` (Find Multiple Child Objects)**

### **Simple Example**

```python
comments = db.findChild("articles", {"title": "Understanding UnQLite"}, "comments")
print(comments)
```

### **Complex Example with Filtering**

```python
comments = db.findChild("articles", {"title": "Understanding UnQLite"}, "comments", {
    "user": "Jane Doe"
})
print(comments)
```

---

## **7. `findOneChild` (Find a Single Child Object)**

### **Simple Example**

```python
comment = db.findOneChild("articles", {"title": "Understanding UnQLite"}, "comments", {"user": "Jane Doe"})
print(comment)
```

### **Complex Example (Nested Queries)**

```python
comment = db.findOneChild("articles", {"title": "Understanding UnQLite"}, "comments", {
    "replies.user": "John"
})
print(comment)
```

---

## **8. `insertRecordsChild` (Insert Multiple Child Records)**

### **Simple Example**

```python
db.insertRecordsChild("articles", {"title": "Understanding UnQLite"}, "comments", [
    {"comment_id": db.generate_object_id(), "user": "Jane Doe", "text": "Nice!", "timestamp": datetime.now()},
    {"comment_id": db.generate_object_id(), "user": "John Smith", "text": "Helpful!", "timestamp": datetime.now()}
])
```

### **Complex Example (Adding Comments with Nested Replies)**

```python
db.insertRecordsChild("articles", {"title": "Understanding UnQLite"}, "comments", [
    {
        "comment_id": db.generate_object_id(),
        "user": "Alice",
        "text": "Loved this article!",
        "replies": [
            {"user": "John", "text": "I agree!", "timestamp": datetime.now()},
            {"user": "Mary", "text": "Great explanation!", "timestamp": datetime.now()}
        ],
        "timestamp": datetime.now()
    }
])
```

---

## **9. `updateChild` (Update a Specific Child Object)**

### **Simple Example**

```python
db.updateChild("articles", {"title": "Understanding UnQLite"}, "comments", {"user": "Jane Doe"}, {"text": "Fantastic article!"})
```

### **Complex Example (Updating Nested Data)**

```python
db.updateChild("articles", {"title": "Understanding UnQLite"}, "comments", {"user": "Alice"}, {
    "replies": [{"user": "John", "text": "Updated reply!", "timestamp": datetime.now()}]
})
```

---

## **10. `deleteChild` (Delete a Child Object from an Array)**

### **Simple Example**

```python
db.deleteChild("articles", {"title": "Understanding UnQLite"}, "comments", {"user": "Jane Doe"})
```

### **Complex Example (Delete Based on Multiple Conditions)**

```python
db.deleteChild("articles", {"title": "Understanding UnQLite"}, "comments", {
    "user": "Alice",
    "replies.user": "John"
})
```

---

## **11. `delete` (Delete an Entire Document)**

### **Simple Example**

```python
db.delete("articles", {"title": "Understanding UnQLite"})
```

### **Complex Example (Deleting Multiple Records)**

```python
db.delete("articles", {"tags": {"$in": ["nosql", "database"]}})
```

---

### **Saving and Querying Nested Structures in UnQLite**

Here’s how to **store, update, and retrieve nested structures**, including `profile.social.twitter`.  
We'll also create **functions to store deeply nested data** and retrieve **specific nested values**.











---

## **1. Insert a Nested Document**

### **Example: User Profile with Nested Social Handles**

```python
db.insert("users", [
    {
        "_id": db.generate_object_id(),
        "name": "Alice",
        "profile": {
            "bio": "Software Engineer",
            "website": "https://alice.dev",
            "social": {
                "twitter": "@alice_dev",
                "github": "alice123"
            }
        }
    }
])
```

✅ **Data Structure in UnQLite**

```json
{
    "_id": "uuid-1",
    "name": "Alice",
    "profile": {
        "bio": "Software Engineer",
        "website": "https://alice.dev",
        "social": {
            "twitter": "@alice_dev",
            "github": "alice123"
        }
    }
}
```

---

## **2. Find a User by Nested Field**

### **Find a User by `profile.social.twitter`**

```python
user = db.findOne("users", {"profile.social.twitter": "@alice_dev"})
print(user)
```

✅ **Expected Output**

```json
{
    "_id": "uuid-1",
    "name": "Alice",
    "profile": {
        "bio": "Software Engineer",
        "website": "https://alice.dev",
        "social": {
            "twitter": "@alice_dev",
            "github": "alice123"
        }
    }
}
```

---

## **3. Retrieve Only a Specific Nested Field**

### **Get Only `profile.social.twitter` Instead of Full Document**

```python
user = db.findOne("users", {"name": "Alice"})

if user:
    twitter_handle = user.get("profile", {}).get("social", {}).get("twitter")
    print(f"Alice's Twitter: {twitter_handle}")
```

✅ **Expected Output**

```shell
Alice's Twitter: @alice_dev
```

---

## **4. Update a Specific Nested Field**

### **Change `profile.social.twitter`**

```python
db.updateChild("users", {"name": "Alice"}, "profile.social", {"twitter": "@alice_dev"}, {"twitter": "@alice_new"})
```

✅ **Updated Data**

```json
{
    "profile": {
        "social": {
            "twitter": "@alice_new",
            "github": "alice123"
        }
    }
}
```

---

## **5. Insert or Update Nested Data (Ensure Exists)**

### **Function to Create or Update Nested Field**

```python
update_nested_field(db, "users", {"name": "Alice"}, "profile.social.twitter", "@alice_new")
```

✅ **Ensures the field exists and updates it.**

---

## **6. Retrieve Users with a Specific Social Handle**

### **Find All Users with GitHub Accounts**

```python
users = db.find("users", {"profile.social.github": {"$ne": None}})
print(users)
```

✅ **Returns Users Who Have a GitHub Username Set.**

---

## **7. Delete a Specific Nested Field**

### **Remove Only `profile.social.twitter`**

```python
delete_nested_field(db, "users", {"name": "Alice"}, "profile.social.twitter")
```

✅ **Removes `twitter` while keeping `profile.social.github`.**

---

## **8. Find Users with Any Social Media Account**

### **Users with Twitter, GitHub, or LinkedIn**

```python
users = db.find("users", {"profile.social": {"$in": ["twitter", "github", "linkedin"]}})
print(users)
```

✅ **Returns users who have at least one of these accounts.**

---

## **9. Query by Partial Match (`$regex` Equivalent)**

### **Find Users with Twitter Handles Starting with "@alice"**

```python
users = db.find("users", {
    "profile.social.twitter": {"$in": ["@alice_dev", "@alice_new"]}
})
print(users)
```

✅ **Finds Users Matching Partial Social Handles.**

---

## **10. Query Users by Nested Data Size**

### **Find Users with at Least 2 Social Accounts**

```python
users = db.find("users", {"profile.social": {"$size": 2}})
print(users)
```

✅ **Finds users who have exactly 2 social media accounts stored.**

---

### **Final Features**

✅ **Stores, Updates, and Deletes Nested Fields**  
✅ **Finds Users by `profile.social.twitter`**  
✅ **Returns Specific Nested Fields (e.g., Just `twitter`)**  
✅ **Handles Many-to-Many Relationships in NoSQL Format**  

___

### **Handling Field Inconsistency in UnQLite**

Since **UnQLite is a schema-less NoSQL database**, it **does not enforce a fixed schema** like SQL databases do. This means:

- **Documents in the same collection can have different fields.**
- **Some fields may be missing in certain documents.**
- **Extra fields can exist in some records but not in others.**

#### **Key Behavior:**

1. **Missing Fields:** Queries that reference a missing field simply return `None` or **exclude those records** from results.
2. **Extra Fields:** New fields are automatically stored without affecting existing documents.
3. **Updating Documents:** Updating a document only modifies the fields provided, leaving others unchanged.
4. **Querying Missing Fields:**  
   - `$exists: True` finds documents that have a specific field.  
   - `$exists: False` finds documents that do **not** have a field.

---

## **1️⃣ Example: Field Inconsistency in UnQLite**

### **Inserting Inconsistent Data**

```python
db.insert("users", [
    {"_id": db.generate_object_id(), "name": "Alice", "age": 30},  # No "email"
    {"_id": db.generate_object_id(), "name": "Bob", "email": "bob@example.com"},  # No "age"
    {"_id": db.generate_object_id(), "name": "Charlie", "age": 25, "email": "charlie@example.com"}  # Has both
])
```

✅ **All documents are stored despite missing/extra fields.**

---

## **2️⃣ Querying and Handling Missing Fields**

### **Find Users Who Have an Email (`$exists: True`)**

```python
users_with_email = db.find("users", {"email": {"$exists": True}})
print(users_with_email)
```

✅ **Returns only users who have an `email` field.**

### **Find Users Who Do NOT Have an Email (`$exists: False`)**

```python
users_without_email = db.find("users", {"email": {"$exists": False}})
print(users_without_email)
```

✅ **Returns only users who lack an `email` field.**

---

## **3️⃣ Querying Fields That Might Be Missing**

### **Find Users Over 25 (Handles Missing `age`)**

```python
users = db.find("users", {"age": {"$gte": 25}})
print(users)
```

✅ **Only users with an `age` field will be returned. If a user doesn’t have `age`, they are ignored.**

---

## **4️⃣ Updating Documents with Extra Fields**

### **Adding a `phone` Field Only to Bob**

```python
db.update_or_insert("users", {"name": "Bob"}, {"phone": "555-1234"}, {})
```

✅ **Now, Bob has a `phone` field while others do not.**

---

## **5️⃣ Removing Extra Fields**

### **Delete Only the `phone` Field from Bob**

```python
db.deleteChild("users", {"name": "Bob"}, "phone", {"$exists": True})
```

✅ **Removes only the `phone` field, keeping the rest of Bob’s data.**

---

## **6️⃣ Ensuring a Field Exists Before Querying**

### **Safe Lookup of a Nested Field**

```python
user = db.findOne("users", {"name": "Alice"})

# Handle missing fields safely
email = user.get("email", "No Email Found")
print(email)
```

✅ **Prevents errors when a field is missing.**

---

## **7️⃣ Querying for Fields That Contain Data**

### **Find Users Where `profile.bio` Is Not Empty**

```python
db.find("users", {"profile.bio": {"$ne": None}})
```

✅ **Returns users who have a `profile.bio` field that is not empty.**

---

### **🚀 Summary: How UnQLite Handles Field Inconsistencies**

| **Scenario** | **Behavior** | **Solution** |
|-------------|-------------|-------------|
| **Missing fields** | Query ignores missing fields | Use `$exists: True/False` |
| **Extra fields** | Stored without issues | No action needed |
| **Querying missing fields** | Returns only matching docs | Use `.get("field", default_value)` |
| **Updating documents** | Only provided fields change | Unmodified fields remain |
| **Deleting fields** | Only deletes specified fields | Use `deleteChild` |

---

### **Would You Like More Help With Bulk Operations or Indexing Next? 🚀**
