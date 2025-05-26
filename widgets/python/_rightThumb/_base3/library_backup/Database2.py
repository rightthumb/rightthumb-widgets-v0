
class Database2:

	def __init__(self, data):

		appDB = '_Generated_App_Database.db'
		appJSON = '_Generated_App_Database_Config.json'
		appPyRaw = '_Gen_App_Database_Data'
		appPy = appPyRaw + '.py'
		self.appPyDefault = _v.myDatabases + _v.slash+'_default.py'


		self.data = {}
		self.tables = []
		self.name = data.replace(appDB,'').replace(appJSON,'').replace(appPy,'').replace('.json','')
		if os.path.isfile(self.name + appDB):
			self.appDB =   self.name + appDB
			self.appJSON = self.name + appJSON
			self.appPy =   self.name + appPy

		else:
			self.appDB = _v.myDatabases + _v.slash + self.name + appDB
			self.appJSON = _v.myDatabases + _v.slash + self.name + appJSON
			self.appPy = _v.myDatabases + _v.slash + self.name + appPy
		self.appPyRaw = self.name + appPyRaw

		self.tableDelim = '_x_'

		self.meta = []

	def registerTable(self, name):
		self.tables.append(TablesDB(name))

	def TableFieldCount(self):
		result = 0
		for i,ci in enumerate(self.tables):
			if ci.name == name:
				result = self.tables[i].getCount()
		return result
# {
#   'table': 'table,name',
#   'fields': [
#       {'names': 'one,two'},
#       {'names': 'three', 'table': 'name', 'as': 'threeish'}
#   ],
#   'action': [
#       { 'type': 'text', 'names': 'field', 'table': 'your_mom', 'search': '*.txt,desktop'},
#       { 'type': 'text', 'names': 'testy', 'and_or': 'or', 'table': 'or_test', 'search': '*.py,*.txt'},
#       { 'type': 'field_type(text)', 'table': 'name', 'names': 'field,names', 'and_or': 'and',  'search': '*.py,tech'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': '1000,2000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'g,1000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'l,1000'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(ago(2000))'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07))'},
#       { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07)),str(epoch('2018.10',True))'},
#       { 'type': 'field_type(sort)', 'names': 'field', 'order': 'asc'},
#       { 'type': 'field_type(sort)', 'names': 'field', 'order': 'desc'},
#   ]
# }

	def queryBuilder(self,data): # queryBuilder
		self.data = data
		# print_(data['fields'])
		# sys.exit()
		self.qbFields = []
		tbls = data['table'].split(',')
		if len(tbls) > 1:
			multi_Table = True
		else:
			multi_Table = False
		if multi_Table:
			sql = 'SELECT '
			# print_(data['fields'])
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' '
			for iJ,tJ in enumerate(tbls):
				if iJ > 0:
					sql += ' JOIN ' + tJ + ' ON ' + tJ + '.id_parent = ' + tbls[0] + '.id_uuid '

			sql += ' WHERE '
		else:
			sql = 'SELECT '
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' WHERE '
		# JOIN albums ON albums.albumid = tracks.albumid
		orderBy = False
		for i,action in enumerate(data['action']):
			if action['type'] == 'text':
				sql += '('
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "" + thisT + '.' + name + ""
					try:
						and_or = action['and_or']
					except Exception as e:
						and_or =  'and'
					for tv in action['search'].split(','):
						if tv.startswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '%" + tv + "' " + and_or + ' '
						elif tv.endswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '" + tv + "%' " + and_or + ' '
						else:
							sql += ' ' + name + " like '%" + tv + "%' " + and_or + ' '
				sql = _str.replaceDuplicate(sql,' ')
				sql = _str.cleanLast(sql,' and ')
				sql = _str.cleanLast(sql,' or ')
				sql += ') and '
			sql = sql.replace('WHERE and ','WHERE ')
			if action['type'] == 'number':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						print_('bad input')
						sys.exit()
					if isNu(coin[0]):
						do = 'b'
					else:
						do = coin[0]
					if do == 'b':
						sql += name + ' > ' + str(coin[0]) + " and " + name + " < " + str(coin[1]) + ' and '
					if do == 'l':
						sql += name + ' < ' + str(coin[1]) + ' and '
					if do == 'g':
						sql += name + ' > ' + str(coin[1]) + ' and '



			if action['type'] == 'date':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						if isNu2(coin[0]):
							sql += name + ' > ' + str(epoch(coin[0])) + ' and '
						else:
							sql += name + ' > ' + str(timeAgo(coin[0])) + ' and '
					else:
						if isNu2(coin[0]):
							do = 'b'
						else:
							do = coin[0]
						if do == 'b':
							sql += name + ' > ' + str(epoch(coin[0])) + " and " + name + " < " + str(epoch(coin[1],True)) + ' and '
						if do == 'l':
							sql += name + ' < ' + str(epoch(coin[1])) + ' and '
						if do == 'g':
							sql += name + ' > ' + str(epoch(coin[1])) + ' and '



			if action['type'] == 'bytes':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if coin[0] == 'l':
						sql += name + ' < ' + str(unFormatSize(coin[1])) + ' and '
					elif coin[0] == 'g':
						sql += name + ' > ' + str(unFormatSize(coin[1])) + ' and '
					else:
						sql += name + ' > ' + str(unFormatSize(coin[0])) + " and " + name + " < " + str(unFormatSize(coin[1])) + ' and '



			if action['type'] == 'sort':
				orderBy = True
		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		if orderBy:
			sql += ' ORDER BY '
			for i,action in enumerate(data['action']):
				if action['type'] == 'sort':
					try:
						if 'a' in action['order'].lower():
							order = 'ASC'
						else:
							order = 'DESC'
					except Exception as e:
						order = 'ASC'
					for name in action['names'].split(','):
						if multi_Table:
							try:
								thisT =  action['table']
							except Exception as e:
								thisT =  tbls[0]
							name = "'" + thisT + '.' + name + "'"
						sql += name + ' ' + order + ', '

		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		sql = _str.cleanLast(sql,', ')
		sql = _str.replaceDuplicate(sql,' ')
		sql = _str.cleanLast(sql,' ')
		sql += ';'
		sql = sql.replace('WHERE;',';')
		return sql
	def metaGen(self):
		import sqlite3
		import re
		# import numpy as np
		meta = []
		con = sqlite3.connect(self.appDB)
		for line in con.iterdump():
			if 'CREATE TABLE' in line and not 'INSERT INTO' in line:
				# print_(line)
				one = line.split('CREATE TABLE ')[1]
				two = one.split(' (')
				table = two[0]
				# print_(table)
				fieldRaw = two[1].split(')')[0]
				f = []
				for field in fieldRaw.split(', '):
					# print_('\t',field)
					fd = field.split(' ')
					f.append({'type': fd[1], 'field': fd[0], 'max': 0, 'min': 0, 'average': 0})


				if self.tableDelim in table:
					parent = ''
					mx = len(table.split(self.tableDelim))-1
					for iT,tX in enumerate(table.split(self.tableDelim)):
						if iT < mx:
							parent += tX + self.tableDelim
					parent = _str.cleanLast(parent,self.tableDelim)
				else:
					parent = ''


				meta.append({'table': table, 'parent': parent, 'fields': f})
			elif 'INSERT INTO' in line:
				pass
				# break
		average = {}
		for im,m in enumerate(meta):
			sql = 'SELECT * FROM ' + m['table']
			conn = sqlite3.connect(self.appDB)
			c = conn.cursor()
			c.execute(sql)
			rows = c.fetchall()
			for row in rows:
				# print_(row)
				for fi,field in enumerate(m['fields']):
					# print_(field['field'],row[fi])
					aKey = str(m['table']) + '-' + str(number2Words(field['field']))
					# print_(aKey)

					try:
						if not type(average[aKey]['datapoints']) == list:
							average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}

						# print_(type())
					except Exception as e:
						average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}
					average[aKey]
					# print_(aKey)
					if field['type'] == 'int':
						if type(row[fi]) == int:
							size = row[fi]
						else:
							string = re.sub('[^0-9]', '', str(row[fi]))
							# print_(type(string),string)
							# print_(string)
							if len(string) == 0:
								size = 0
							else:
								size = int(string)
					if field['type'] == 'str':
						size = len(str(row[fi]))
					# print_()
					# print_(type(average[aKey]['max']),average[aKey]['max'])
					# print_(type(size),size)
					if average[aKey]['max'] < size:
						average[aKey]['max'] = size
					if average[aKey]['min'] == 'first':
						average[aKey]['min'] = size
					elif average[aKey]['min'] > size:
						average[aKey]['min'] = size
					average[aKey]['datapoints'].append(size)

		errors = []
		totalCount = 0
		for im,m in enumerate(meta):

			for row in rows:
				# print_(row)
				for fi,field in enumerate(m['fields']):
					# print_(meta[im]['fields'][fi]['max'])
					aKey = m['table'] + '-' + number2Words(field['field'])
					# print_(aKey)
					try:
						# print_(average[aKey]['max'])
						meta[im]['fields'][fi]['max'] = average[aKey]['max']
						meta[im]['fields'][fi]['min'] = average[aKey]['min']
						# meta[im]['fields'][fi]['average'] = int(np.mean(average[aKey]['datapoints']))
						meta[im]['count'] = len(average[aKey]['datapoints'])
						total = meta[im]['count']
					except Exception as e:
						errors.append(aKey)
				totalCount += total

		self.meta = {'data': meta, 'records': totalCount, 'errors': errors}
		saveTable2(meta,'database_meta.json')

		return meta
	def metaPrint(self):
		if self.meta == []:
			self.metaGen()

		totalColumnWidth = 0
		for m in self.meta['data']:
			tables.register(m['table'],m['fields'])
			spaces = tables.getLength(m['table'],'type,field,max,min,average')
			if spaces > totalColumnWidth:
				totalColumnWidth = spaces



		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		for m in self.meta['data']:
			genLine(totalColumnWidth,'=')
			print_('Table:\t',m['table'])
			print_('Parent:\t',m['parent'])
			print_('Records:',m['count'])
			print_()
			tables.register(m['table'],m['fields'])
			# tables.fieldProfileSet(m['table'],'*','alignment','center')
			# tables.print(m['table'],'type,field,max,min,average',fieldLengths)
			tables.print(m['table'],'type,field,max,min,average')

			genLine(totalColumnWidth,'=')
		print_()
		print_('Records:',self.meta['records'])
		print_()
		print_('Errors:')
		for e in self.meta['errors']:
			print_('\t',e)
		print_()
		print_()
		print_('Example:')
		print_('\t p dba -app',self.name)
		print_()
		print_()
	def findParent(self,table):
		# parent = 'Error'
		# for m in self.meta['data']:
		#   if m['table'] == table:
		#       parent = m['parent']
		#       break
		if self.tableDelim in table:
			parent = ''
			mx = len(table.split(self.tableDelim))-1
			for iT,tX in enumerate(table.split(self.tableDelim)):
				if iT < mx:
					parent += tX + self.tableDelim
			parent = _str.cleanLast(parent,self.tableDelim)
		else:
			parent = ''
		return parent

	def findChildren(self,table):
		if self.meta == []:
			self.metaGen()
		children = []
		for m in self.meta['data']:
			if m['parent'] == table:
				children.append(m['table'])

		return children

	def findType(self,column):
		mainTable = self.data['table'].split(',')[0]
		found = False
		nm = ''
		result = ''

		for action in self.data['fields']:
			for name in action['names'].split(','):
				if name == column:
					try:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']
					except Exception as e:
						pass

		if len(result) == 0:
			for action in self.data['action']:
				for name in action['names'].split(','):
					if name == column:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']

		if len(result) == 0:
			for field in self.data['fields']:
				try:
					table = field['table']
				except Exception as e:
					table = mainTable
				if ',' in field['names']:
					for name in field['names'].split(','):
						if name == column:
							nm = name
							found = True
				else:
					try:
						newName = field['as']
					except Exception as e:
						newName = field['names']
					if newName == column:
						nm = newName
						found = True
				# print_(field)
				if found:
					break

			result = self.checkConfig(table,nm)
		# print_(mainTable)
		return result
	def checkConfig(self,tbl,nm):
		self.appJSON
		# print_(self.appJSON)
		# print_(tbl,nm)
		structure = getTable2(self.appJSON)
		result = ''
		if tbl == structure['name']:
			for zs in structure['zstructure']:
				if zs['field'] == nm:
					result = zs['type']
					break
		return result

	def executeSQL(self,sql,group=0):
		import sqlite3
		conn = sqlite3.connect(self.appDB)
		c = conn.cursor()
		c.execute(sql)
		all_rows = c.fetchall()
		records = []
		for f in all_rows:
			row = {}
			for ic,c in enumerate(self.qbFields):
				row[c] = f[ic]

			records.append(row)
		col = ''
		for c in self.qbFields:
			col += c + ','
		col = _str.cleanLast(col,',')
		tables.register('sql',records)
		for ic,c in enumerate(self.qbFields):
			if self.findType(c) == 'date':
				tables.fieldProfileSet('sql',c,'trigger',float2Date2)
			if 'byte' in self.findType(c):
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			if self.findType(c) == 'bytes':
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			# print_(self.findType(c))
		tables.print('sql',col)