import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register('Folders', '-f,-fo,-folder,-folders','L:\\ent')
	_.switches.register('DB', '-db','index.db')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start



from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from PIL import Image
import os

def extract_metadata(file_path):
	metadata = {}
	file_extension = os.path.splitext(file_path)[1].lower()

	if file_extension in ['.mp4', '.mkv', '.avi']:
		parser = createParser(str(file_path))
		if not parser:
			print(f"Unable to create parser for {file_path}")
			return metadata
		with parser:
			try:
				metadata_extracted = extractMetadata(parser)
			except Exception as e:
				print(f"Metadata extraction error for {file_path}: {e}")
				return metadata
		if metadata_extracted:
			current_section = ""  # Keep track of the current section
			for item in metadata_extracted.exportPlaintext():
				if ': ' in item:
					key, value = item.split(': ', 1)
					# Prepend section name to key if there is a current section
					full_key = f"{current_section}{key}" if current_section else key
					metadata[full_key.strip()] = value.strip()
				else:
					# Treat the item as a section header
					current_section = f"{item} - "  # Append '-' for readability

	# Similar handling for other file types

	return metadata



# def extract_metadata(file_path):
#     metadata = {}
#     file_extension = os.path.splitext(file_path)[1].lower()

#     # Example for video files using hachoir
#     if file_extension in ['.mp4', '.mkv', '.avi']:
#         parser = createParser(str(file_path))
#         if not parser:
#             print(f"Unable to create parser for {file_path}")
#             return metadata
#         with parser:
#             try:
#                 metadata_extracted = extractMetadata(parser)
#             except Exception as e:
#                 print(f"Metadata extraction error for {file_path}: {e}")
#                 return metadata
#         if metadata_extracted:
#             for item in metadata_extracted.exportPlaintext():
#                 key, value = item.split(': ')
#                 metadata[key.strip()] = value.strip()

#     # Example for image files using Pillow
#     elif file_extension in ['.jpg', '.jpeg', '.png']:
#         with Image.open(file_path) as img:
#             for key, value in img.info.items():
#                 metadata[key] = value
#             metadata["Dimensions"] = f"{img.width} x {img.height}"

#     return metadata





import os
import sqlite3
from pathlib import Path
# Import metadata extraction libraries as needed

def create_or_update_table(db_conn, table_name, columns):
	cur = db_conn.cursor()
	existing_cols = cur.execute(f"PRAGMA table_info({table_name})").fetchall()
	existing_col_names = [col[1] for col in existing_cols]

	for col in columns:
		if col not in existing_col_names:
			cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {col} TEXT")
	db_conn.commit()

def ensure_table_schema(db_conn, table_name, metadata):
	cur = db_conn.cursor()
	# Check if the table exists
	cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
	if cur.fetchone() is None:
		# Create table if it doesn't exist. Use a single column placeholder.
		cur.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY)")
	
	for key in metadata.keys():
		try:
			# Try adding each column. If it exists, this will fail silently.
			cur.execute(f"ALTER TABLE {table_name} ADD COLUMN [{key}] TEXT")
		except sqlite3.OperationalError:
			# Column already exists, so we can ignore the error
			pass

def insert_metadata(db_conn, table_name, metadata):
	if not metadata:  # Skip if metadata is empty
		return
	
	ensure_table_schema(db_conn, table_name, metadata)
	
	columns = ', '.join(f'[{k}]' for k in metadata.keys())
	placeholders = ', '.join('?' for _ in metadata)
	sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
	
	try:
		db_conn.execute(sql, list(metadata.values()))
		db_conn.commit()
	except sqlite3.OperationalError as e:
		print(f"Error inserting metadata: {e}")


# def insert_metadata(db_conn, table_name, metadata):
# 	columns = ', '.join(metadata.keys())
# 	placeholders = ', '.join(['?'] * len(metadata))
# 	sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
# 	db_conn.execute(sql, list(metadata.values()))

def action():
	if _.switches.isActive('DB'):
		db = _.switches.value('DB')
	else:
		db = 'index.db'
	db_conn = sqlite3.connect(db)
	files_processed = 0
	commit_threshold = 2000
	if _.switches.isActive('Folders'):
		folders = _.switches.values('Folders')
	else:
		folders = [os.getcwd()]

	for path in folders:
		for root, dirs, files in os.walk(path):
			for file in files:
				file_path = Path(root) / file
				# Detect file type and extract metadata using appropriate library
				metadata = extract_metadata(file_path)  # Implement this function based on file type

				if files_processed % commit_threshold == 0:
					# Dynamically create or update table schema
					create_or_update_table(db_conn, "movies", metadata.keys())

				insert_metadata(db_conn, "movies", metadata)

				files_processed += 1
				if files_processed % commit_threshold == 0:
					db_conn.commit()

	db_conn.commit()
	db_conn.close()


# pip install hachoir Pillow


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);