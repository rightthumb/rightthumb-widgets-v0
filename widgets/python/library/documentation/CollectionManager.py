import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db')))
from UnQLiteMgr import UnQLiteMgr
from datetime import datetime

class CollectionManager:
    def __init__(self, db_path="collections_db.db"):
        """Initialize the Collection Manager with UnQLite database."""
        self.db = UnQLiteMgr(db_path)

    # -------------------------------
    # 1. CREATE A NEW COLLECTION
    # -------------------------------
    def create_collection(self, name):
        """Creates a new collection and returns its ID."""
        collection_id = self.db.insert_collection(name)
        print(f"Collection created: {name} (ID: {collection_id})")
        return collection_id

    # -------------------------------
    # 2. ADD A NEW ITEM (FILE, FOLDER, NOTE, URL)
    # -------------------------------
    def add_item(self, item_type, name_or_url):
        """Adds a new item (file, folder, note, or URL) and returns its ID."""
        if item_type not in ["files", "folders", "notes", "urls"]:
            print("Invalid item type. Choose from 'files', 'folders', 'notes', 'urls'.")
            return None
        item_id = self.db.insert_item(item_type, name_or_url)
        print(f"{item_type.capitalize()} added: {name_or_url} (ID: {item_id})")
        return item_id

    # -------------------------------
    # 3. LINK AN ITEM TO A COLLECTION
    # -------------------------------
    def link_item(self, collection_id, item_id, item_type):
        """Links an item to a collection."""
        if item_type not in ["files", "folders", "notes", "urls"]:
            print("Invalid item type. Choose from 'files', 'folders', 'notes', 'urls'.")
            return False
        success = self.db.add_item_to_collection(collection_id, item_id, item_type)
        if success:
            print(f"Linked {item_type} (ID: {item_id}) to Collection (ID: {collection_id})")
        else:
            print(f"Failed to link {item_type} to Collection.")
        return success

    # -------------------------------
    # 4. GET ALL ITEMS IN A COLLECTION
    # -------------------------------
    def get_collection_items(self, collection_id):
        """Retrieves all items in a collection."""
        items = self.db.get_collection_items(collection_id)
        if items:
            print(f"\nItems in Collection (ID: {collection_id}):")
            for item_type, item_list in items.items():
                print(f"\n{item_type.capitalize()}:")
                for item in item_list:
                    print(f" - {item}")
        else:
            print("No items found.")

    # -------------------------------
    # 5. REMOVE AN ITEM FROM A COLLECTION
    # -------------------------------
    def remove_item(self, collection_id, item_id, item_type):
        """Removes an item from a collection."""
        if item_type not in ["files", "folders", "notes", "urls"]:
            print("Invalid item type. Choose from 'files', 'folders', 'notes', 'urls'.")
            return False
        success = self.db.remove_item_from_collection(collection_id, item_id, item_type)
        if success:
            print(f"Removed {item_type} (ID: {item_id}) from Collection (ID: {collection_id})")
        else:
            print(f"Failed to remove {item_type} from Collection.")
        return success

    # -------------------------------
    # 6. FIND AN ITEM IN MULTIPLE COLLECTIONS
    # -------------------------------
    def find_item_in_collections(self, item_id, item_type):
        """Finds all collections an item belongs to."""
        item = self.db.findOne(item_type, {"_id": item_id})
        if item:
            print(f"\nItem (ID: {item_id}) is in the following collections:")
            for collection_id in item["collections"]:
                collection = self.db.findOne("collections", {"_id": collection_id})
                if collection:
                    print(f" - {collection['name']} (ID: {collection_id})")
        else:
            print("Item not found.")

    # -------------------------------
    # 7. DELETE A COLLECTION
    # -------------------------------
    def delete_collection(self, collection_id):
        """Deletes a collection and removes its references from items."""
        collection = self.db.findOne("collections", {"_id": collection_id})
        if not collection:
            print("Collection not found.")
            return False

        # Remove collection reference from all items
        for item_type in ["files", "folders", "notes", "urls"]:
            for item_id in collection[item_type]:
                item = self.db.findOne(item_type, {"_id": item_id})
                if item:
                    item["collections"] = [c for c in item["collections"] if c != collection_id]
                    self.db.db.collection(item_type).update(item)

        # Delete collection
        self.db.delete("collections", {"_id": collection_id})
        print(f"Deleted Collection (ID: {collection_id})")
        return True

    # -------------------------------
    # 8. CLOSE THE DATABASE
    # -------------------------------
    def close(self):
        """Closes the database connection."""
        self.db.close()
        print("Database closed.")


if __name__ == "__main__":
    manager = CollectionManager()

    # Create a collection
    collection_id = manager.create_collection("Project A")

    # Add items
    file_id = manager.add_item("files", "document.pdf")
    folder_id = manager.add_item("folders", "Project Folder")
    note_id = manager.add_item("notes", "Meeting Notes")
    url_id = manager.add_item("urls", "https://example.com")

    # Link items to the collection
    manager.link_item(collection_id, file_id, "files")
    manager.link_item(collection_id, folder_id, "folders")
    manager.link_item(collection_id, note_id, "notes")
    manager.link_item(collection_id, url_id, "urls")

    # Get all items in the collection
    manager.get_collection_items(collection_id)

    # Remove an item
    manager.remove_item(collection_id, file_id, "files")

    # Find which collections an item belongs to
    manager.find_item_in_collections(file_id, "files")

    # Delete a collection
    manager.delete_collection(collection_id)

    # Close the database
    manager.close()
