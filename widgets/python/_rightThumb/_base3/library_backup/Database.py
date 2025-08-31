
class Databases:

# FOREIGN KEY (project_id) REFERENCES projects (id)

	def __init__( self ):

		self.databases = []


	def register( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):

		idx = len( self.databases )
		self.databases.append( Database( name=name, file=file, table=table, records=records, fields=fields, delete=delete, description=description, project=project, auto=auto, printFileActivity=printFileActivity ) )


	def search( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].search( info )

	def getFields( self, name=False, table=False, exclude=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].getFields( table, exclude )

	def update( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].update( info )

	def add( self, name=False, info=False ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].add( info )

	def insertRecords( self, name, table, records ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].insertRecords( table=table, records=records )

	def trigger( self, name, table, field, trigger ):
		for i,d in enumerate(self.databases):
			if self.databases[i].name == name:
				return self.databases[i].addTrigger( table, field, trigger )


class Database:

	def __init__( self, name=False, file=False, table=False, records=False, fields=False, delete=False, description=False, project=False, auto=False, printFileActivity=False ):
		self.initialized = []
		self.initializedDB = False
		self.tableInfo = []
		self.tables = []
		self.relationships = []

		self.name = name
		self.file = _v.myDatabases + _v.slash + file
		self.delete = delete
		self.printFileActivity = printFileActivity

		self.project = project
		self.description = description
		self.apps = False

		self.table = table
		self.records = records

		self.fieldsManual = fields
		self.fields = {}

		if type( table ) == bool:
			auto = True
		if not type( self.records ) == bool:
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
				# print_( self.records[i] )

		if self.delete and os.path.isfile( self.file ):
			os.unlink( self.file )
			if self.printFileActivity:
				print_( ' file deleted ')
		if os.path.isfile( self.file ):
			if self.printFileActivity:
				print_( ' file exists ')

		if auto and os.path.isfile( self.file ):
			self.genInfo( process=True )
		else:
			if not type( table ) == bool:
				if not type( self.records ) == bool:
					self.insertRecords( table )



	def generateStructure( self, table ):
		if not table in self.initialized:
			self.initialized.append( table )
			if os.path.isfile( self.file ):
				self.genInfo( process=True )
			else:
				fieldsData = self.processRecords()
				self.create( table, fieldsData )

				self.genInfo( process=True )



	def addTrigger( self, table, field, trigger ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['trigger'] = trigger



	def updateFieldInfo( self, table, field, label, data ):
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for ii,fieldX in enumerate(self.tables[i].fields):
					if fieldX.name == field:
						self.tables[i].fields[ii].info['label'] = data
	def updateManualFieldInfo( self ):
		if not type( self.fieldsManual ) == bool:
			for i,f in enumerate(self.fieldsManual):
				for k in f.keys():
					if not k == 'name' and not k == 'type' and not k == 'table':
						self.updateFieldInfo( f['table'], f['name'], k, f[k] )

	def getFields( self, table, exclude=False ):
		result = []
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for field in self.tables[i].fields:
					add = True
					if not type( exclude ) == bool:

						if type( exclude ) == str:
							ex = exclude.split(',')
						else:
							ex = exclude

						for x in ex:
							if len( x ) > 0:
								if x in field.name:
									add = False
					if add:
						result.append( field.name )

		return result

	def getFieldType( self, table, field ):
		result = ''
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						result = fieldX.info['type']
		return result

	# def update( self, info ):

	#   sql = "update "+info['table']+" set [x] where " + info['update'] + " "
	#   u = ''
	#   for f in info['record'].keys():
	#       t = self.getFieldType( info['table'], f )
	#       if 'int' in t:
	#           u += f + " = " + str(info['record'][f]) + ","
	#       else:
	#           u += f + " = '" + str(info['record'][f]) + "',"
	#   u = _str.cleanBE( u, ',' )

	#   sql = sql.replace( '[x]', u )

	#   conn = sqlite3.connect( self.file )
	#   cursor = conn.cursor()
	#   tables = []
	#   rows = cursor.execute( sql )

	#   fields = self.getFields( info['table'] )
	#   results = []
	#   for row in (rows):
	#       d = {}
	#       for i,column in enumerate(row):
	#           d[ fields[i] ] = row[i]
	#       results.append( d )
	#   conn.commit()
	#   conn.close()

	def update( self, info ):
		import sqlite3
		sql = "update "+info['table']+" set [x] where " + info['update'] + " "
		u = ''
		for f in info['record'].keys():
			t = self.getFieldType( info['table'], f )
			if 'int' in t:
				u += f + " = " + str(info['record'][f]) + ","
			else:
				u += f + " = '" + str(info['record'][f]) + "',"
		u = _str.cleanBE( u, ',' )

		sql = sql.replace( '[x]', u )

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				d[ fields[i] ] = row[i]
			results.append( d )
		conn.commit()
		conn.close()

	def search( self, info ):
		import sqlite3
		if not self.initializedDB:
			print_( 'no data' )
			sys.exit()

		if not type( info['custom'] ) == bool and not info['force']:
			sql = "select * from "+info['table']+" where "+info['custom']
		elif info['force'] and not type( info['custom'] ) == bool:
			sql = info['custom']
		else:
			if info['type'] == 'text':
				sql = "select * from "+info['table']+" where "+info['field']+" like '"+info['search']+"'"
			else:
				sql = "select * from "+info['table']+" where "+info['field']+" "+info['search']

		conn = sqlite3.connect( self.file )
		cursor = conn.cursor()
		tables = []
		rows = cursor.execute( sql )

		fields = self.getFields( info['table'] )
		results = []
		for row in (rows):
			d = {}
			for i,column in enumerate(row):
				# d[ fields[i] ] = row[i]
				d[ fields[i] ] = self.trigger( info['table'], fields[i], row[i] )
			results.append( d )

		conn.close()

		return results
		# print_( info )
	def trigger( self, table, field, data ):
		result = data
		if field == 'date_created':
			return resolveEpochTest( data )
		for i,r in enumerate(self.tables):
			if self.tables[i].table == table:
				for fieldX in self.tables[i].fields:
					if fieldX.name == field:
						if not type( fieldX.info['trigger'] ) == bool:
							result = fieldX.info['trigger']( data )
		return result


	def insertRecords( self, table, records=[] ):
		import sqlite3
		if len( records ) > 0:
			self.records = records
			for i,r in enumerate(self.records):
				self.records[i]['date_created'] = time.time()
				self.records[i]['date_modified'] = ''
		self.generateStructure( table )

		conn = sqlite3.connect(self.file)
		cursor = conn.cursor()
		for record in self.records:
			# self.records[i]['date_created'] = time.time()
			record['date_created'] = time.time()
			record['date_modified'] = ''
			sql = self.genRecordInsert( table, record )
			# n = ''

			# for field in fields:
			#   n += field['name'] + ' ' + field['type'] + ','

			# n = _str.cleanBE( n, ',' )
			# sql = sql.replace( '[n]', n )


			cursor.execute( sql )
			conn.commit()
		conn.close()



	def genRecordInsert( self, table, record ):
		b = "'insert into [table] ( [names] ) values ( [dataDel] )'.format( [data] )"
		n = ''
		dd = ''
		d = ''
		b = b.replace( '[table]', table )
		x = []

		for k in record.keys():
			n += k + ','
			d += "record['"+k+"'],"
			dd += '"{}",'
			x.append( record[k] )
		n = _str.cleanBE( n, ',' )
		dd = _str.cleanBE( dd, ',' )
		d = _str.cleanBE( d, ',' )

		b = b.replace( '[names]', n )
		b = b.replace( '[dataDel]', dd )
		b = b.replace( '[data]', d )
		# print_( b )
		return eval( b )


	def genInfo( self, process=False ):
		import sqlite3
		if os.path.isfile( self.file ) and not self.initializedDB:
			self.initializedDB = True
			self.tableInfo = []
			sql = "select name from sqlite_master where type = 'table'"

			conn = sqlite3.connect( self.file )
			cursor = conn.cursor()
			tables = []
			tablesRaw = cursor.execute( sql )
			for table in tablesRaw:
				for data in table:
					if len( data ) > 1 and not 'sqlite' in data:
						tables.append( data )

			# print_( tables )

			for table in tables:
				sql = 'PRAGMA table_info('+table+')'
				fieldsRaw = cursor.execute( sql )
				fields = []
				for fieldsX in fieldsRaw:

					if not type( self.fieldsManual ) == bool:
						data = list(filter(lambda itemX: itemX['name'] == fieldsX[1], self.fieldsManual))
						if len( data ) > 0:
							data[0][ 'type' ] = fieldsX[2]
							fields.append( data[0] )
						else:
							fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })
					else:
						fields.append({ 'name': fieldsX[1], 'type': fieldsX[2],  })



				self.tableInfo.append({ 'name': table, 'fields': fields })

			conn.close()
			if process:
				self.addGeneratedTables()
			return self.tableInfo

	def addGeneratedTables( self ):
		dataOK = True
		if not type( self.records ) == bool:

			for record in self.processRecords():
				found = False
				for table in self.tableInfo:
					for field in table['fields']:
						if record['name'] == field:
							found = True
				if not found:
					dataOK = False

		for table in self.tableInfo:
			self.tables.append( DatabaseTables( table['name'], table['fields'] ) )
			self.updateManualFieldInfo()

	def processRecords( self ):
		autoFieldType = []
		for record in self.records:

			for field in record.keys():
				if len(list(filter(lambda itemX: itemX['name'] == field, autoFieldType))) == 0:
					if isText( record[ field ] ):
						t = 'text'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isNum( record[ field ] ):
						t = 'integer'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })
					if isFloat( record[ field ] ):
						t = 'real'
						if 'date_' in field:
							t = 'date'
						if not type( self.fieldsManual ) == bool:
							data = list(filter(lambda itemX: itemX['name'] == field, self.fieldsManual))
							if len( data ) > 0:
								data[0][ 'type' ] = t
								autoFieldType.append( data[0] )
							else:
								autoFieldType.append({ 'name': field, 'type': t })
						else:
							autoFieldType.append({ 'name': field, 'type': t })


		return autoFieldType

	def fieldInfo( self, table, field, fType ):
		self.fields[ field ] = fType

	def create( self, table=False, fields=False ):
		import sqlite3
		if os.path.isfile(self.file):
			print_( 'Database exists' )
		else:
			conn = sqlite3.connect(self.file)
			cursor = conn.cursor()
			# sql =  'CREATE TABLE '+table+' ([n])'
			sql =  'CREATE TABLE '+table+' (id integer primary key autoincrement not null, [n])'
			n = ''
			nn = ''
			for field in fields:
				n += field['name'] + ' ' + field['type'] + ','
				if not 'date_modified' == field['name']:
					nn += field['name'] + ','

			n = _str.cleanBE( n, ',' )
			nn = _str.cleanBE( nn, ',' )
			sql = sql.replace( '[n]', n )
			cursor.execute( sql )
			sql =   "CREATE TRIGGER UpdateLastTime UPDATE OF "+nn+" ON "+table+" "\
					" BEGIN"\
					"  UPDATE "+table+" SET date_modified=datetime('now','localtime') WHERE id=old.id;"\
					" END;"
			cursor.execute( sql )

			conn.close()



class DatabaseTables:
	def __init__( self, table=False, fields=False ):

		self.fields = []

		self.table = table

		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def setInfo( self, field, label, info ):
		for i,row in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = info


	def setFields( self, fields=False ):
		if not type( fields ) == bool:
			for i,field in enumerate(fields):
				idx = len( self.fields )
				self.fields.append( DatabaseFields( field['name'], field['type'] ) )
				for label in field.keys():
					if not label == 'name' and not label == 'type' and not label == 'table':
						self.fields[ idx ].addFieldInfo( label, field[ label ] )

	def updateFieldInfo( self, field, label, data ):
		for i,f in enumerate(self.fields):
			if self.fields[i].name == field:
				self.fields[i].info[ label ] = data


class DatabaseFields:
	def __init__( self, name=False, fieldType='text' ):
		self.name = name

		self.info = {
						'name': name,
						'type': fieldType,
						'trigger': False,
						'default': False,
		}

	def addFieldInfo( self, label, info ):
		self.info[ label ] = info

	def fieldInfo( self, label ):
		if label in list( self.info.keys() ):
			return self.info[ label ]
		else:
			return False
