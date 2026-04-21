import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.md' )
	_.switches.register( 'Scan', '-scan' )
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Markdown', '-md' )
	_.switches.register( 'Database', '-db', 'documents.db | if swich not used it defaults to postgres' )
	_.switches.register( 'CreateTables', '-create' )
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start



import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'db', 'tools')))
from StemPhraseProcessor import StemPhraseProcessor

import os
import re

class DocumentPhraseIndexer:
	def __init__(self, pg_mgr, language='english', databaseType='postgres'):
		self.pg = pg_mgr
		self.databaseType = databaseType
		self.processor = StemPhraseProcessor(pg_mgr,language=language,databaseType=databaseType)


	def extract_functions(self, content):
		# Matches myFunc(), myFunc(arg), my.namespace.path()
		pattern = r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\s*\([^()]*\)'
		return list(dict.fromkeys(re.findall(pattern, content)))  # preserve order

	def save_functions_and_links(self, function_names, document_id):
		for position, fn in enumerate(function_names):
			self.pg.update_or_insert('functions', {'fn': fn}, {'fn': fn})
			res = self.pg.read('functions', {'fn': fn})
			if res:
				fn_id = res[0]['id']
				self.pg.update_or_insert(
					'document_functions',
					{'document_id': document_id, 'function_id': fn_id},
					{'document_id': document_id, 'function_id': fn_id, 'position': position}
				)

	def strip_functions_from_content(self, content):
		# Remove all function calls (preserve structure minimally)
		return re.sub(r'\b([a-zA-Z_][a-zA-Z0-9_.]*)\s*\([^()]*\)', '', content)

	# def index_file(self, file_path):
	#     if not os.path.isfile(file_path):
	#         raise FileNotFoundError(f"File not found: {file_path}")

	#     with open(file_path, 'r', encoding='utf-8') as f:
	#         content = f.read()

	#     title = os.path.basename(file_path)

	#     # Step 1: Insert document
	#     insert_sql = '''
	#         INSERT INTO documents (title, path, content)
	#         VALUES (%s, %s, %s)
	#         RETURNING id
	#     '''
	#     self.pg.cursor.execute(insert_sql, (title, file_path, content))
	#     doc_id = self.pg.cursor.fetchone()['id']

	#     # Step 2: Extract and link functions
	#     function_names = self.extract_functions(content)
	#     self.save_functions_and_links(function_names, doc_id)

	#     # Step 3: Clean content and process phrases
	#     cleaned = self.strip_functions_from_content(content)
	#     phrase_data = self.processor.save(cleaned)
	#     if not phrase_data:
	#         print(f"No phrases found in: {file_path}")
	#         return None

	#     # Step 4: Link document to phrases
	#     for position, entry in enumerate(phrase_data):
	#         self.pg.update_or_insert(
	#             'document_phrases',
	#             {'document_id': doc_id, 'phrase_id': entry['id']},
	#             {'document_id': doc_id, 'phrase_id': entry['id'], 'position': position}
	#         )

	#     return {
	#         'document_id': doc_id,
	#         'path': file_path,
	#         'functions': function_names,
	#         'phrase_ids': [entry['id'] for entry in phrase_data]
	#     }

	def index_file(self, file_path):
		if not os.path.isfile(file_path):
			raise FileNotFoundError(f"File not found: {file_path}")

		with open(file_path, 'r', encoding='utf-8') as f:
			content = f.read()

		title = os.path.basename(file_path)

		# SQL placeholder and RETURNING clause depend on databaseType
		if self.databaseType == 'postgres':
			insert_sql = '''
				INSERT INTO documents (title, path, content)
				VALUES (%s, %s, %s)
				RETURNING id
			'''
			self.pg.cursor.execute(insert_sql, (title, file_path, content))
			doc_id = self.pg.cursor.fetchone()['id']

		else:  # sqlite or other
			insert_sql = '''
				INSERT INTO documents (title, path, content)
				VALUES (?, ?, ?)
			'''
			self.pg.cursor.execute(insert_sql, (title, file_path, content))
			doc_id = self.pg.cursor.lastrowid





def indexDocument(path):
	if _.switches.isActive('Markdown') and not path.endswith('.md'):
		print(f"Skipping non-Markdown file: {path}")
		return
	global indexer
	result = indexer.index_file(path)
	print(result)






def CreateTables(db, databaseType):
	if databaseType == 'postgres':		
		db.sql('''
CREATE TABLE IF NOT EXISTS stems (
	id SERIAL PRIMARY KEY,
	stem TEXT UNIQUE NOT NULL
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS stem_bigrams (
	id SERIAL PRIMARY KEY,
	id1 INTEGER REFERENCES stems(id),
	id2 INTEGER REFERENCES stems(id)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS phrases (
	id SERIAL PRIMARY KEY,
	stem_ids INTEGER[] NOT NULL,
	phrase_text TEXT,
	watch INTEGER DEFAULT 20000000000,
	frequency INTEGER DEFAULT 1
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS phrase_stems (
	phrase_id INTEGER REFERENCES phrases(id) ON DELETE CASCADE,
	position INTEGER,
	stem_id INTEGER REFERENCES stems(id),
	PRIMARY KEY (phrase_id, position)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS functions (
	id SERIAL PRIMARY KEY,
	fn TEXT UNIQUE NOT NULL
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS documents (
	id SERIAL PRIMARY KEY,
	title TEXT,
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS document_phrases (
	document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
	phrase_id INTEGER REFERENCES phrases(id) ON DELETE CASCADE,
	position INTEGER,
	PRIMARY KEY (document_id, phrase_id)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS document_functions (
	document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
	function_id INTEGER REFERENCES functions(id) ON DELETE CASCADE,
	position INTEGER,
	PRIMARY KEY (document_id, function_id)
);
		''')

	elif databaseType == 'sqlite':
		db.sql('''
CREATE TABLE IF NOT EXISTS stems (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	stem TEXT UNIQUE NOT NULL
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS stem_bigrams (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id1 INTEGER REFERENCES stems(id),
	id2 INTEGER REFERENCES stems(id)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS phrases (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	stem_ids TEXT NOT NULL, -- JSON-encoded array
	phrase_text TEXT,
	watch INTEGER DEFAULT 20000000000,
	frequency INTEGER DEFAULT 1
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS phrase_stems (
	phrase_id INTEGER REFERENCES phrases(id) ON DELETE CASCADE,
	position INTEGER,
	stem_id INTEGER REFERENCES stems(id),
	PRIMARY KEY (phrase_id, position)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS functions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fn TEXT UNIQUE NOT NULL
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS documents (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	content TEXT,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS document_phrases (
	document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
	phrase_id INTEGER REFERENCES phrases(id) ON DELETE CASCADE,
	position INTEGER,
	PRIMARY KEY (document_id, phrase_id)
);
		''')
		db.sql('''
CREATE TABLE IF NOT EXISTS document_functions (
	document_id INTEGER REFERENCES documents(id) ON DELETE CASCADE,
	function_id INTEGER REFERENCES functions(id) ON DELETE CASCADE,
	position INTEGER,
	PRIMARY KEY (document_id, function_id)
);
		''')


def action():
	global indexer
	
	databaseType = 'postgres'
	



	if _.switches.isActive('Database'):
		databaseType = 'sqlite'
		database = 'documents.db'
		if _.switches.values('Database'):
			database = _.switches.values('Database')[0]

	if databaseType == 'postgres':
		
		import sys, os
		sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'db')))
		from postgresMgr import postgresMgr
		
		db = postgresMgr(
			
			database=_v.yFig('pgDocuments','db'),
			user=_v.yFig('pgDocuments','user'),
			password=(_v.yFig('pgDocuments','password')),
			host=_v.yFig('pgDocuments','host'),
			port=_v.yFig('pgDocuments','port')
		)

	elif databaseType == 'sqlite':
		from library.db.sqliteMgr import  sqliteMgr
		db = sqliteMgr(database=database)

	if _.switches.isActive('CreateTables'):
		CreateTables(db,databaseType)


	indexer = DocumentPhraseIndexer(db,databaseType=databaseType)

	if _.switches.isActive('Files'):
		for path in _.switches.values('Files'):
			if os.path.isfile(path):
				indexDocument(path)
			else:
				print(f"File not found: {path}")


	if _.switches.isActive('Scan'):
		if not _.switches.values('Scan'):
			_.fo(folder=None,r=_.switches.isActive('Recursive'),script=indexDocument)
		elif _.switches.values('Scan'):
			
			for folder in _.switches.values('Scan'):
				_.fo(folder=folder,r=_.switches.isActive('Recursive'),script=indexDocument)
				


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)