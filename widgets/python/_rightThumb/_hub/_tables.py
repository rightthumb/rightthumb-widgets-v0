#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

from _rightThumb._hub import _construct as __
from _rightThumb._hub import app
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _string as _str

############################################################## copy-fn-class




def line_print(  label=None, text=None, txt='_', mn=50, add=5, p=2 ):
	ln = mn
	if text is None and label is None:
		if __.terminal.width:
			ln = __.terminal.width
			add = 0


	if not label is None:
		global line_length_hash_table
		if not label in line_length_hash_table:
			line_length_hash_table[label] = ln
		else:
			ln = line_length_hash_table[label]
		if not text is None:
			if not p == True and not p == 1:
				p = 0
			if type(text) == str:
				t = len( str(text) )
				if t > ln:
					ln = t
					line_length_hash_table[label] = ln
			elif type(text) == list:
				for texty in text:
					t = len( str(texty) )
					if t > ln:
						ln = t
						line_length_hash_table[label] = ln

	if text is None and ln > 0:
		i = 0
		result = ''
		if add:
			add+=1
		ln += add
		while not i == ln:
			result += txt
			i+=1
		if p:
			print( result )
		return result


def gen_line(count,what, p=1):
	count = int(count)
	what = str(what)
	cnt = 0
	result = ''
	while cnt < count:
		result += what
		cnt += 1
	if p:
		print(result)
	return result


def check_field_match( actual, search ):
	if actual.lower() == search.lower() or actual.lower() == check_field_matcht(search):
		return True
	return False

TableProfile_Config = {}
line_length_hash_table = {}




############################################################## copy-fn-class


class Table:

	def __init__( self, name, asset=[], group_space=True, tab='', webtable=None ):
		global switches
		global _dir
		

		self.webtable = webtable
		self.group_space = group_space
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		if app.switch.isActive('Long'):
			try:
				self.maxNameLength = int(app.switch.value('Long'))
			except Exception as e:
				self.maxNameLength = 35
		self.columnTab = '   '
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

		self.wrapTableKey = 'Da529801Ef674997B9f3382B3eD2b93F'
		self.backup = dot()
		self.backup.asset = asset.copy()
		self.aggregate_processed = False
		self.isWrap = False
		self.hasAggregate = False
		self.hasGroups = False
		self.backup.fields = {}
		self.backup.allfields = {}
		self.backup.NGfields = {}
		self.groupID_KEY = genUUID()
		if len( self.asset ):
			for r in self.asset:
				for k in r:
					if not k in self.backup.fields:
						self.backup.fields[k] = 1
						self.backup.allfields[ tfc(k) ] = k
						self.backup.NGfields[ tfc(k) ] = k


		self.tab_color = ''
		if type(tab) == list:
			self.tab_color = tab[1]
			tab = tab[0]

		tabH = ''
		i=0
		while not i == len(tab):
			i+=1
			tabH+=' '

		self.tab = { 'header': tabH, 'table': tab }

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print()
			# for x in dir(self.views[i]):
			#   print(x)

			if self.views[i].name == name:
				# print('found')
				app.switch.fieldSet('Sort','active',True)
				app.switch.fieldSet('Sort','value',str(self.views[i].sort))
				# print(app.switch.value('Sort'))
				# try:
					
				# except Exception as e:
				#   pass
				# print('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#   self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if app.switch.isActive('Length'):
			result = self.nameLengthFix(string,app.switch.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += '  .' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += '  .' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print('*** ' + name)
		size = len(name) + spacer
		
		# print(name,00)
		# rows[0][name]
		try:
			pass
			if name in rows[0]:
				rows[0][name]
			else:
				# print(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
				eval(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			print(9)
			print(name)
			print(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
			printVarSimple(rows[0])
			printBold('record sample','red')
			os._exit(0)
		# print(name)
		for item in rows:
			shorten = True
			if app.switch.isActive('Long') == True:
				shorten = False
				if app.switch.isActive('ShortenColumn') == True:
					shortenColumn = app.switch.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
			
			if name in item:
				thisData = item[name]
			elif name.split('.')[0] in item:
				thisData = eval(  'item["' + '"]["'.join(name.split('.')) + '"]'  )


			if shorten == True and not app.switch.isActive('Length'):
				try:
					text = self.nameLength( str(self.scriptTriggerField(name,thisData)) ,'')
				except Exception as e:
					text = self.nameLength(str(thisData),'')
			else:
				if app.switch.isActive('Length'):
					# print('asdf')
					# sys.exit()
					try:
						
						text = self.nameLengthFix(  str(self.scriptTriggerField(name,thisData)) ,app.switch.value('Length'),'')
					except Exception as e:
						text = self.nameLengthFix(str(thisData),app.switch.value('Length'),'')
				else:
					# sys.exit()
					# if type(thisData) == int or type(thisData) == float:
					#     text = thisData
					# else:
					try:
						text = self.scriptTriggerField(name,thisData)
					except Exception as e:
						text = thisData
							
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			else:
				if type(value) == int:
					value = addComma( str(value) )
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print('ran')
		field = field.lower()
		i = 0
		value = ''
		if isHeader and '_header_' in TableProfile_Config.keys() and propertyName in TableProfile_Config['_header_'].keys():
			return TableProfile_Config['_header_'][propertyName]
		elif not isHeader and field in TableProfile_Config.keys() and propertyName in TableProfile_Config[field].keys():
			return TableProfile_Config[field][propertyName]
		elif '*' in TableProfile_Config.keys() and propertyName in TableProfile_Config['*'].keys():
			return TableProfile_Config['*'][propertyName]

		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1


		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader

		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print(rows)

		columnList = column
		if column in rows[i]:
			value = str(self.triggerExecute(column,rows[i][column]))
		elif column.split('.')[0] in rows[i]:
			value = str(self.triggerExecute(column,  eval(  'rows[i]["' + '"]["'.join(column.split('.')) + '"]'  )  ) )

		# value = rows[i][column]
		# print(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if app.switch.isActive('Long') == True:
			shorten = False
			if app.switch.isActive('ShortenColumn') == True:
				shortenColumn = app.switch.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = app.switch.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if app.switch.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							pass
							if self.group_space:
								print(self.groupLine(columnList,columnHeaderLength))
							if not self.isExtraRecord:
								for g in groupBy.split(','):
									groupByList[g] = ''
						else:
							pass
							if self.group_space:
								print('')
						

						if not self.isExtraRecord:
							groupByList[gb] = text
						else:
							if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
								text = ''

						# else:
						#   print(text)
					else:
						pass
						
						if len(self.isExtraRecord_000x):
							self.isExtraRecord_0001[ self.isExtraRecord_000x.split('-')[0] ] = 1
						text = ''
						
		alignment = self.fieldProfileGet(column,'alignment')
		# print(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print(column,theLeft,theRight,'0' + result + '0')
			# print(totalSpace,theLeft,theRight)
		#   result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ''
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',isHeader=True)
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'right'


			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		result += '\n'
		return '\n'+result

	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower() == column.lower():
				return k
		for k in self.asset[0].keys():
			if k.lower() == column.split('.')[0].lower():
				return column




	def prefixSize( self ):
		pre = ''
		for x in self.tab['table']+loopPrint(__.table_prefix_padding):
			if x == '\t':
				pre += '    '
			else:
				pre += x
		return len(pre)


	def wrapTable( self, cols=None ):
		# return None

		if not __.terminal.width:
			return None

		cols = __.terminal.width
		cols -= 8
		spaces = []
		theKeys = []
		for c in self.spaces:
			theKeys.append(c)
			spaces.append({ 'c': c, 's': self.spaces[c] })

		spaces = sorted(spaces, key=lambda d: (d['s']))
		spaces.reverse()

		fieldsToShorten = []

		if not len(app.switch.value('WrapTable')):
			fieldsToShorten.append( spaces[0]['c'] )
			if len( self.spaces.keys() ) > 1:
				diff = percentageDiffIntAuto( spaces[0]['s'], spaces[1]['s'] )
				if diff >= 50:
					fieldsToShorten.append( spaces[1]['c'] )
				# print( 'diff:', diff )

				if len( self.spaces.keys() ) > 2:
					diff = percentageDiffIntAuto( spaces[0]['s'], spaces[2]['s'] )
					if diff >= 50:
						fieldsToShorten.append( spaces[2]['c'] )
					# print( 'diff:', diff )
		elif len(app.switch.value('WrapTable')):
			done = False
			if len(app.switch.values('WrapTable')) == 1:
				done = False
				wrapBy = app.switch.value('WrapTable')
				if wrapBy in self.asset[0].keys():
					done = True
				if not done:
					if formatColumns(wrapBy) in self.asset[0].keys():
						wrapBy = formatColumns(wrapBy)
						done = True

				if not done:
					wrapBy = 0
					try:
						wrapBy = int(app.switch.value('WrapTable'))
					except Exception as e:
						wrapBy = 0
					if wrapBy > 0:
						done = True
			elif len(app.switch.values('WrapTable')) > 1:
				wrapBy = []
				for xx in app.switch.values('WrapTable'):
					y = formatColumns(xx)
					if y in self.asset[0].keys():
						wrapBy.append(y)
						done = True

			if done:
				if type(wrapBy) == str:
					fieldsToShorten.append( wrapBy )
				if type(wrapBy) == list:
					for yy in wrapBy:
						fieldsToShorten.append( yy )
				if type(wrapBy) == int:
					for isp, itx in enumerate(spaces):
						fieldsToShorten.append( itx['c'] )
						
						if isp+1 == wrapBy:
							break

				# print(type(wrapBy))
				# print(wrapBy)
				# sys.exit()

					


		# print(fieldsToShorten)
		# sys.exit()

		maxLen = self.maxNameLength
		total = self.prefixSize()
		for c in self.spaces:
			total += self.spaces[c]
			total += len(self.columnTab)
		
		tempSpaces = self.spaces.copy()
		for c in tempSpaces:
			if tempSpaces[c] > maxLen:
				if not c in fieldsToShorten:
					fieldsToShorten.append(c)

		while total > cols:
			hasGrtMax = False

			for fs in fieldsToShorten:
				if tempSpaces[fs] > maxLen:
					hasGrtMax = True
					tempSpaces[fs] -=1
			if not hasGrtMax:
				for fs in fieldsToShorten:
					tempSpaces[fs] -=1

			total = self.prefixSize()
			for c in tempSpaces:
				total += tempSpaces[c]
				total += len(self.columnTab)
		


		# percentageDiffIntAuto
		# printVarSimple( self.spaces )
		# print( '---------' )
		# printVarSimple( tempSpaces )
		# for x in spaces:
		#   print(x)

		wrapTableKey = self.wrapTableKey
		
		counter = 0
		global fields
		fields.register( wrapTableKey+'-b', 'val', 4, m=4 )
		fields.register( wrapTableKey, 'val', 7, m=12 )
		test = fields.padZeros( wrapTableKey, 'val', 5 )
		test = fields.padZeros( wrapTableKey+'-b', 'val', 5 )
		letters = {}
		

		# print(letterSet)
		# sys.exit()
		def letterBoost( i ):
			if not str(i) in letters:
				letters[str(i)] = 'a'
		

		recordsToAdd = []
		for i,record in enumerate(self.asset):
			letters[ str(i) ] = 'a'
			recordKey = 1
			

			this_key = fields.padZeros( wrapTableKey, 'val', i+1 )
			this_key_B = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )

			
			self.asset[i][wrapTableKey+'-sort'] = this_key+'-'+this_key_B
			rec = {}
			rec_last = {}
			for c in tempSpaces:

				if c in record and len( str(record[c]) ) > tempSpaces[c]:
					# rec[c] = {}
					recordKey = 1
					# cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					# # print(cs)
					# if not cs in rec:
					#   rec[cs] = {}
					# if not c in rec[cs]:
					#   rec[cs][c] = ''
					
					rec_parts = autoWrapText( str(record[c]), length=tempSpaces[c] )

					# print('_________________________________________')
					# print()
					# print(record[c])
					# print()
					# print(rec_parts)
					# print()
					# print('_________________________________________')
					rp = ''
					last_rp = ''
					for rp in rec_parts:
						if len(rp) and not last_rp == rp:
							last_rp = rp
							cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
							recordKey += 1
							if not cs in rec:
								rec[cs] = {}
							if not cs in rec_last:
								rec_last[cs] = {}
							# if not c in rec[cs]:
								# rec[cs][c] = ''
							
							# if c in rec_last[cs]:
							#   if 
							rec[cs][c] = rp
					rp = ''

					# for x in record[c]:
					#   rec[cs][c] += x
					#   if len( rec[cs][c] ) > tempSpaces[c]:
					#       recordKey += 1
					#       cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					#       # print(cs)
					#       if not cs in rec:
					#           rec[cs] = {}
					#       if not c in rec[cs]:
					#           rec[cs][c] = ''
					# printVarSimple(rec)
					# sys.exit()
			if rec:
				for iii,xXx in enumerate(rec):
					if xXx == '0001':
						for c in rec[xXx]:
							self.asset[i][c] = rec[xXx][c]
					else:
						# print(xXx)
						rec[xXx][wrapTableKey+'-sort'] = this_key +'-'+ xXx
						recordsToAdd.append(rec[xXx])
					# print(rec[x])
				# print(rec)

		for rec in recordsToAdd:
			self.asset.append(rec)
			# print(rec)
		# sys.exit()
		self.spaces = {}


		groupBy = app.switch.values('GroupBy')
		last = {}
		for gb in groupBy:
			last[gb] = '{7270D97A-CC1D-4365-9545-87CA34F2F026}'



		for i,record in enumerate(self.asset):
			ks = list(record.keys())
			for k in theKeys:
				if not k in ks:
					self.asset[i][k] = ''
			for k in theKeys:
				if not k in self.spaces:
					self.spaces[k] = 0
				if len(str(record[k])) > self.spaces[k]:
					self.spaces[k] = len(str(record[k]))


		# for i,record in enumerate(self.asset):
		#   for gb in groupBy:
		#       if gb in self.asset[i]:
		#           if self.asset[i][gb] == last[gb]:
		#               self.asset[i][gb] = ''
		#           else:
		#               last[gb] = self.asset[i][gb]
		self.asset = sorted(self.asset, key=lambda d: (d[wrapTableKey+'-sort']))


		# for x in self.asset:
		#   print()
		#   print(x)
		#   print()




		# for i,record in enumerate(self.asset):
		#   print( record[wrapTableKey+'-sort'] )
		# sys.exit()
		# print(self.asset)
		# for x in self.asset:
		#   print()
		#   print(x)
		#   print()
		# sys.exit()
		
		self.print(
					column=self.print_backup['column'],
					fieldLengths=self.print_backup['fieldLengths'],
					pc=self.print_backup['pc'],
					printColumns=self.print_backup['printColumns'],
					force=True
		)




	def aggregateRecord( self, i ):
		# print()
		
		for c in self.aggregates.columns:
			if not c in self.asset[i]:
				self.asset[i][c] = ''

		for seg in self.aggregates.segments:
			if seg['status']:
				record = self.aggregate_record_process( i, seg['i'] )


	def aggregateTop( self, s ):
		ss = str(s)
		if self.aggregates.index[ss]['rent'] >= 0:
			return self.aggregateTop(self.aggregates.index[ss]['rent'])
		else:
			return self.aggregates.index[ss]


	def aggregateItemValue( self, v, f ):
		if not 'params' in v:
			v['params'] = {}
		if not 'fields' in v:
			v['fields'] = {}
		if not 'data' in v:
			v['data'] = []

		# print( self.aggregate_backtrack )

		if 'data' in f:
			v['data'].append( f['data'] )
		if 'fields' in f:
			if not 'fields' in v:
				v['fields'] = {}
			for k in f['fields']:
				v['fields'][k] = f['fields'][k]
		elif 'params' in f:
			if not 'params' in v:
				v['params'] = {}
			for k in f['params']:
				v['params'][k] = f['params'][k]
		return v

	def aggregate_record_process_group( self, i, s ):
		ss = str(s)
		seg = self.aggregates.index[ss]
		if 'variable' in seg['l']:
			alpha = seg['l']
			if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				txtParts = seg['txt'].split('?')
				grp = txtParts[0]+'?'
				fld = txtParts[1]
				lbl = txtParts[2]
				if not lbl in self.aggregates.group_storage:
					self.aggregates.group_storage[lbl] = 0


				data = self.aggregate_record_process( i, seg['val'] )
				child = self.aggregates.index[ str(seg['val']) ]
				do = None
				if 'function' in child['l']:
					do = child['txt']
					done = False
					if do == 'max':
						done = True;
						try:
							if data['data'] > self.aggregates.group_storage[lbl]:
								self.aggregates.group_storage[lbl] = data['data']
						except Exception as e: cp('Error: group max variable', 'red');

					if do == 'add':
						done = True;
						try:
							self.aggregates.group_storage[lbl] += data['data']
						except Exception as e: cp('Error: group add variable', 'red');
					
					# if not done:
					#   self.aggregates.group_storage[lbl] = data['data']

				pass


				
				pass

				if i in self.aggregates.groups[fld]['e']:
					if  __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 3:
						self.asset[  self.aggregates.groups[fld]['e'][i]  ][lbl] = addComma( self.aggregates.group_storage[lbl] )
					else:
						if tfc(lbl) in self.backup.NGfields:
							if not str(i) in self.aggregates.agroupsADD:
								self.aggregates.agroupsADD[ str(i) ] = {}
							self.aggregates.agroupsADD[ str(i) ][lbl] = self.aggregates.group_storage[lbl]
						else:           
							self.asset[i][lbl] = addComma( self.aggregates.group_storage[lbl] )
					if not __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 2:
						self.aggregates.group_storage[lbl] = 0
			


		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print( list( self.asset[0].keys() ) )
		#   sys.exit()


	def aggregate_record_process( self, i, s ):

		ss = str(s)
		if True:
			seg = self.aggregates.index[ss]
			# print(seg)
			
			# self.aggregate_backtrack = { 'i': i, 's': s, 'seg': seg }


			if 'alpha' in seg['l'] and 'arg' in seg['l'] :
				simple_keys = {}
				for key in list(self.asset[i].keys()):
					simple_keys[ tfc(key) ] = key
				if tfc(formatColumns( seg['txt'] )) in simple_keys:
					vXv = simple_keys[tfc(formatColumns( seg['txt'] ))]
					return { 'fields': { vXv: self.asset[i][vXv] }, 'data': self.asset[i][vXv] }

				elif formatColumns( seg['txt'] ) in self.asset[i]:
					return { 'fields': { formatColumns( seg['txt'] ): self.asset[i][formatColumns( seg['txt'] )] }, 'data': self.asset[i][formatColumns( seg['txt'] )] }
				return { 'params': { seg['txt']: 1 } }



			if 'variable' in seg['l']:
				alpha = seg['l']
				isOF = False
				data = self.aggregate_record_process( i, seg['val'] )
				if '?' in seg['txt'] and  seg['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes:
					isOF = True
					if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
						return None
					if seg['txt'].startswith('eot?'):
						if not seg['txt'] in self.aggregates.storage:
							self.aggregates.storage[ seg['txt'] ] = {}
						if not alpha in self.aggregates.storage[seg['txt']]:
							self.aggregates.storage[seg['txt']][alpha] = {}
							self.aggregates.storage[seg['txt']][alpha]['data'] = 0
							self.aggregates.storage[seg['txt']][alpha]['settings'] = {}
					if seg['txt'].startswith('eof?'):
						# print( seg['txt'] ); sys.exit();
						if not seg['txt'] in __.aggregate.eof.storage:
							__.aggregate.eof.storage[ seg['txt'] ] = {}
						if not alpha in __.aggregate.eof.storage[seg['txt']]:
							__.aggregate.eof.storage[seg['txt']][alpha] = {}
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = 0
							__.aggregate.eof.storage[seg['txt']][alpha]['settings'] = {}
					
					
					# print(isOF, seg['txt'])

				
					child = self.aggregates.index[ str(seg['val']) ]
					do = None
					if 'function' in child['l']:
						do = child['txt']


					if seg['txt'].startswith('eot?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > self.aggregates.storage[seg['txt']][alpha]['data']:
									self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								self.aggregates.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');

						
						if not done:
							self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							
					elif seg['txt'].startswith('eof?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > __.aggregate.eof.storage[seg['txt']][alpha]['data']:
									__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								__.aggregate.eof.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');
						
						if not done:
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
				
				else:
					# print( i, seg['txt'], data['data'] )
					self.asset[i][seg['txt']] = data['data']

					

					return data
				return { 'data': '' }
			if 'function' in seg['l']:
				###########################################################################################################
				if seg['txt'] == 'trigger':
					pass

				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'add':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result += float( d )
								except Exception as e: pass;
						else:
							try:
								result += float( v['data'] )
							except Exception as e: pass;
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'int':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						nX = []
						if type(v['data']) == list:
							for d in v['data']:
								for cn in str(d):
									if cn in '0123456789.':
										nX.append(cn)
						else:
							for cn in str(v['data']):
								if cn in '0123456789.':
									nX.append(cn)
					result = float(''.join(nX))
					if str(result).endswith('.0'):
						result = int(result)
					# print(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'len':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								# print( 'len-d:', d )
								result += len( str( d ) )
						else:
							# print( 'len-vd:', v['data'] )
							result += len( str( v['data'] ) )
					# print( 'len-v', v )
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'max':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for d in v['data']:
						if '?date' in v['params']:
							try:
								ad = autoDate( d )
							except Exception as e: ad = 0;
							result.append(ad)
						else:
							try:
								ad = float( d )
							except Exception as e: ad = 0;
							result.append(ad)
					result.sort()
					result.reverse()

					return { 'data': result[0] }


				if seg['txt'] == 'config':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						try:
							eval( '__.aggregate.config'+suffix  )
						except Exception as e:
							exec( '__.aggregate.config'+suffix+' = { }'  )
					# printVarSimple(__.aggregate.config)
					# sys.exit()

				pass
				if seg['txt'] == 'format':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						# print( 'suffix:', suffix )
						try:
							eval( '__.aggregate.format'+suffix  )
						except Exception as e:
							exec( '__.aggregate.format'+suffix+' = { }'  )



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'isDate':
					result = None; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = autoDate( d )
								except Exception as e: pass;
						else:
							try:
								result = autoDate( v['data'] )
							except Exception as e: pass;
					
					if not result is None:
						try:
							global _dir
						except Exception as e:
							pass
						if _dir is None:
							import _rightThumb._dir as _dir
						# print( result )
						# self.asset[i]['month'] = _dir.getMonthFromEpoch( result )
						# self.asset[i]['year'] = _dir.getYearFromEpoch( result )
						# self.asset[i]['woy'] = _dir.getWeekAndYear( result )
						# self.asset[i]['dow'] = _dir.getDOWromEpochText( result )
						# self.asset[i]['ago'] = _dir.dateDiffText( result )
						self.asset[i] = isDate( result, self.asset[i] )
						
						# month year woy dow ago
						

						month = _dir.getMonthFromEpoch
						# year = _dir.getYearFromEpoch
						# woy = _dir.getWOYFromEpoch
						# dow = _dir.getDOWromEpochText
						# ago = _dir.dateDiffText
					return { 'data': None }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'file':
					result = ''; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = d
								except Exception as e: pass;
						else:
							try:
								result = v['data']
							except Exception as e: pass;


					# global _dir
					if _dir is None:
						import _rightThumb._dir as _dir
					# info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					# print( info )
					try:
						info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					except Exception as e:
						info = {
									"path": "",
									"name_": "",
									"name": "",
									"folder": "",
									"bytes": 0,
									"size": "",
									"date_created_raw": 0,
									"date_modified_raw": 0,
									"date_created": "",
									"date_modified": "",
									"type": "File",
									"typesort": 1,
									"ext": "txt",
									"week_of_year": "",
									"week_of_year_": 0,
									"day_of_the_week": "",
									"month": "",
									"friendly_week": "",
									"friendly_month": "",
									"md5": "",
									"year": 2021,
									"accessed_raw": 0,
									"date_accessed": "",
									"ce": 0,
									"me": 0,
									"ae": 0,
									"meta": {},
									"ago": "",
									"header": "",
									"error": 0
								}
					
					for k in info:
						if not k in self.asset[i]:
							self.asset[i][k] = info[k]

					return { 'data': result }




				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				###########################################################################################################



	def aggregateBuild( self ):
		if self.aggregate_processed:
			return None
		
		self.aggregate_processed = True


		a = ' '.join( app.switch.values('Aggregate') )
		# print( a )

		
		self.aggregates = dot()

		
		self.aggregates.storage = {}
		self.aggregates.group_storage = {}
		# self.aggregates.segments = __.code.process( a, addString=[['alphaParam','?']] )
		# self.aggregates.segments = __.aggregate.data.records
		self.aggregates.segments = __.aggregate.obj.build( self.name, addSwitch=True )

		self.aggregates.index = {}

		self.aggregates.groups = {}
		self.aggregates.agroups = {}
		self.aggregates.agroupsADD = {}
		self.aggregates.columns = []
		for rec in self.aggregates.segments:
			self.aggregates.index[ str(rec['i']) ] = rec
			if rec['status'] and rec['l'] == 'variable':
				# if not rec['txt'].startswith('eot?'):
				# if not rec['txt'].startswith('eot?') and not rec['txt'].startswith('eof?') and not rec['txt'].startswith('eog?') and  not rec['txt'].startswith('bog?') and  not rec['txt'].lower().startswith('eoga?'):
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					self.aggregates.columns.append( rec['txt'] )
					if not rec['txt'] in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = rec['txt']
						self.backup.NGfields[ rec['txt'] ] = rec['txt']
		for rec in self.aggregates.segments:
			if rec['status'] and rec['l'] == 'variable':
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					pass
				elif '?' in rec['txt'] and rec['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				# elif 'g?' in rec['txt']:
					self.aggregates.agroups[ rec['i'] ] = rec
					
					try:
						gc = rec['txt'].split('?')[2]

					except Exception as e:
						cp( 'Error: aggregates, group split', 'red' )
						sys.exit()
					else:
						self.aggregates.columns.append( gc )
					if not gc in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = gc

		# self.hasGroups

		pass
		# print( self.aggregates.columns )
		# sys.exit()



		# sys.exit()
		# for x in segments:
		#   if x['status']:
		#       cp( x, 'green' )
		#   else:
		#       cp( x, 'cyan' )
		#       # print( x )

		for i,record in enumerate(self.asset):
			self.aggregateRecord( i )


		# sys.exit()
		__.aggregate.storage = self.aggregates.storage
		return self.aggregates.columns


	def aggregateRecordGroups( self, i ):
		# print()

		for seg in self.aggregates.segments:
			if seg['status']:
				# record = self.aggregate_record_process_group( i, seg['i'] )
				try:
					record = self.aggregate_record_process_group( i, seg['i'] )
				except Exception as e:
					cp( 'Error: aggregate, group error', 'red' )
					cp( '\t expected:', 'yellow' )
					cp( '\t\t eog?level?group-len=add(len)', 'green' )
					print()
					cp( [ 'Specifically:', e ], 'red' )
					print()
					sys.exit()




	def aggregateGroup( self ):
		# NOTE: reprocess after aggregates added        
		for ix in self.aggregates.agroups:
			seg = self.aggregates.agroups[ix]
			q = seg['txt'].split('?')
			subject = q[1]
			# print( self.asset[0].keys() )
			# print(subject); sys.exit();
			if subject in self.asset[0] and not subject in self.aggregates.groups:
				self.aggregates.groups[subject] = {}
				self.aggregates.groups[subject]['b'] = {}
				self.aggregates.groups[subject]['e'] = {}
				lastQ = ''
				lastID = -1
				for i,record in enumerate(self.asset):
					# print(subject)
					if subject in record:
						# print( record[subject] )
						if not record[subject] == lastQ:
							if not lastID == -1:
								self.aggregates.groups[subject]['b'][lastID] = i
								self.aggregates.groups[subject]['e'][i] = lastID
							lastQ = record[subject]
							lastID = i
				self.aggregates.groups[subject]['b'][lastID] = len(self.asset)-1
				self.aggregates.groups[subject]['e'][len(self.asset)-1] = lastID

		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print( list( self.asset[0].keys() ) )
		#   sys.exit()

	def aggregate( self, script ):
		self.hasAggregate = True
		__.aggregate.obj.code( script, label=self.name )

	def aggregateBuildGroup( self ):
		self.aggregateGroup()
		for i,record in enumerate(self.asset):
			self.aggregateRecordGroups( i )

		if self.aggregates.agroupsADD:
			

			fields.register( self.groupID_KEY, 'val', 7, m=6 )
			test = fields.padZeros( self.groupID_KEY, 'val', 5 )
			newRecords = []
			for i,record in enumerate(self.asset):
				ii = str(i)
				ix = fields.padZeros( self.groupID_KEY, 'val', i )
				record[ self.groupID_KEY ] = ix + '-A'
				newRecords.append(record)
				if ii in self.aggregates.agroupsADD:
					rec = self.aggregates.agroupsADD[ii]
					rec[ self.groupID_KEY ] = ix + '-B'
					for k in self.backup.allfields:
						if not self.backup.allfields[k] in rec:
							rec[ self.backup.allfields[k] ] = ''
					newRecords.append(rec)
			self.asset = newRecords
	def print( self, column, fieldLengths=False, pc=None, printColumns=True, force=False, l=None, p=None ):
		global switches

		if app.switch.isActive('TableJSON'):
			if len(app.switch.value('TableJSON')):
				saveTable2( self.asset, app.switch.values('TableJSON')[0] )
				cp( [ 'saved:', app.switch.values('TableJSON')[0] ], 'green' )
			else:
				# printVarSimple(self.asset)
				print( d2json(self.asset) )
			return None


		if not p is None:
			self.tab['table'] = p

		if not type(self.asset) == list or len(self.asset) == 0:
			print('Null Set')
			sys.exit()




		if not force:
			if not app.switch.isActive('Help'):
				if app.switch.isActive('Column'):
					column = app.switch.value('Column')
			
				if app.switch.isActive('Sort'):
					self.asset = self.sort()
				elif app.switch.isActive('GroupBy'):
					
					app.switch.fieldSet('Sort','active',True)
					app.switch.fieldSet('Sort','value',app.switch.value('GroupBy'))
					self.asset = self.sort()

			pass
			__.aggregate.storage = {}
			__.aggregate.config = {}
			__.aggregate.format = {}
			__.aggregate.prefix = self.tab['table']+loopPrint(__.table_prefix_padding)
			if app.switch.isActive('Aggregate') or self.hasAggregate:
				aggregate_columns = self.aggregateBuild()
				if  type(aggregate_columns) == list:
					columns = column.split(',')
					for ac in aggregate_columns:
						if not ac in columns:
							columns.append(ac)
					column = ','.join(columns)
				__.aggregate.columns = columns

				shouldSortAgain = False
				if app.switch.isActive('Sort'):
					for sxy in app.switch.values('Sort'):
						if sxy in aggregate_columns:
							shouldSortAgain = True

					if shouldSortAgain:
						self.asset = self.sort()
				self.aggregateBuildGroup()
				for i,record in enumerate(self.asset):
					for c in record:
						nw = __.aggregate.obj.format( c, record[c] )
						if not nw == record[c]:
							self.asset[i][c] = nw
			pass
			for i,record in enumerate( self.asset ):
				for k in record:
					if record[k] is None:
						self.asset[i][k] = ''



		if self.webtable and app.switch.isActive('WebTable') and len(app.switch.value('WebTable')):
			asset = []
			for record in self.asset:
				rec = {}
				for k in column.split(','):
					rec[k] = record[k]
				asset.append(rec)
			saveTable( asset, 'web-tmp-'+app.switch.values('WebTable')[0]+'.json' )


		self.isExtraRecord = False
		if force:
			self.isWrap = True
		self.print_backup = {
								'column': column,
								'fieldLengths': fieldLengths,
								'pc': pc,
								'printColumns': printColumns,
		}
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''
		# print('here',column)
		if not pc is None:
			printColumns = pc
		self.groupByTrigger()
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print(column)
		# print(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			print('Null Set')
			sys.exit()
		global errors
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			try:
				column += self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column += cs + ','
				# print( 'Error: print column', cs )
				# sys.exit()
			# print(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								try:
									if len(str(dpi[dpic])) > 1:
										hasData = True
								except Exception as e:
									pass
								try:
									y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
								except Exception as e:
									pass
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print(newData)
			# print('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print('IS')
								# print(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if app.switch.isActive('PlusOr') == True:
										#   if cnt > 0:
										#       rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(ci(s)) == -1:
												cnt += 1
											# if not string.find(ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print(self.asset)





		# if not len(groupByList):


		# if not column == False:
			# app.switch.fieldSet('Column','value',column)
			# column = app.switch.value('Column')

		# print('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		# print(columnHeader)


		self.groupByList = {}
		try:
			for gb in app.switch.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass



		if not force and not app.switch.isActive('NoWrapTable'):

			if __.terminal.width:
				maxSize = 0
				i=0
				for item in self.asset:
					result = ''
					for c in column.split(','):
						try:
							result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
						except Exception as e:
							pass
					# print(result)
					maxSize = len(result)+self.prefixSize()
					i+=1


				# print( maxSize )
				if maxSize > __.terminal.width and not app.switch.isActive('NoWrapTable'):
					self.wrapTable(__.terminal.width)
					# print( 'error' )
					# sys.exit()
					return None


		pass
		self.groupByList = {}
		try:
			for gb in app.switch.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		if printColumns:
			columnHeader = self.tab['table']+loopPrint(__.table_prefix_padding) + columnHeader.replace( '\n', '' )
			print()
			printBold( columnHeader )
			# printBold( columnHeader, prefix=self.tab['header'] )
			print()
		i = 0
		# print(self.asset)
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''
		tableLine = '|'
		if l is None:
			if app.switch.isActive('NoTableLines'):
				tableLine = ''
		elif not l:
			tableLine = ''

		for item in self.asset:
			# print(item)
			result = ''
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print(result)
				self.isExtraRecord = False
				
				
				# if self.wrapTableKey+'-sort' in item:
					# print(  item[self.wrapTableKey+'-sort']  )
					# print(    )

				if self.wrapTableKey+'-sort' in item:
					self.isExtraRecord_000x = item[self.wrapTableKey+'-sort']

				if self.wrapTableKey+'-sort' in item and not item[self.wrapTableKey+'-sort'].endswith('-0001'):
					self.isExtraRecord = True
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab+tableLine
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					print(12)
					print(c)
					print(12)
					os._exit(0)
			# print(_str.totalStrip5(result)) #TESTING
			
			maxSize = len(result)+self.prefixSize()
			if maxSize > __.terminal.width and not app.switch.isActive('NoWrapTable'):
				ToDo = " result = ''   "
				ToDo = ' for sult in self.wrapTable2(i):  '
				ToDo = '     result += sult  '
			else:
				ToDo = ' the below if will be under this else '

			if len(result) > 0:
				# print(result)
				shouldPrint = True
				if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
					testResult = result
					testResult = testResult.replace( ' ', '' ).replace( '\t', '' )
					if not len(testResult):
						shouldPrint = False
				# if self.isExtraRecord:
				#   print( self.isExtraRecord )

				if shouldPrint:
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						app.colorizeRow( tableLine+result, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:
				if '??' in __.switch_skimmer.active:
					sys.exit()
				pass
				print('')
		# if len(oldData) > 0:
		#   self.asset = oldData
		self.asset = self.backup.asset.copy()
		self.aggregate_processed = False
		# print( 'recovered' )


		footer = {}
		aSettings = {}
		for k in __.aggregate.storage:
			if k.startswith('eot?'):
				f = k[len('eot?'):]
				for y in __.aggregate.storage[k]:
					for sv in __.aggregate.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.storage[k][y]['settings']:
						__.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					theKey = f 
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eot?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?fl' in special:
						theKey = f + ' '+ y
					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y


					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = addComma( __.aggregate.storage[k][y]['data'] )
					# # print(  )
					# footer[ theKey ] = __.aggregate.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.storage[k][y]['data'] )
		if footer:
			print()
			# print()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			# print( __.aggregate.config )
			print()
					# print( f, y, __.aggregate.storage[k][y]['data'] )
			# print( k )
			# sys.exit()

	def sort(self,fields=''):# sortThis
		rows = self.asset

		if not len(self.asset):
			return None

		if self.wrapTableKey+'-sort' in self.asset[0]:
			return rows
		

		global errors
		global switches
		# self.sort = name
		tempFields = []
		delim = ':'
		if fields == '':
			name = app.switch.value('Sort')
		else:
			name = fields
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})

		# itemgetter = __.imp('operator.itemgetter')
		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = self.findColumName(item.split(delim)[1])
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				
			uuid = __.imp('uuid')
			sortBy[item] = str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		if len( tempFields ):
			# print( tempFields )
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True, me=0):
		HD.chmod(theFile)
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0 = _v.stmp + _v.slash + theFile
		dataDump = simplejson.dumps(self.asset, indent=4, sort_keys=True)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		HD.chmod(theFile)
		if printThis:
			print('Saved: ' + file0)
		if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );
	def get(self,theFile = '',tableTemp = True,printThis = False):
		if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = self.file
		self.file = theFile
		# defaults to myTables
		if tableTemp == True:
			file0 = _v.myTables + _v.slash + theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
		if printThis:
			print('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = simplejson.load(json_file)
				# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

	def groupByTrigger( self ):
		try:
			if app.switch.isActive('GroupBy') and len(self.asset):
				newValues = []
				keys = []
				for key in self.asset[0].keys():
					keys.append( key )
				for val in app.switch.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower() == val.lower():
							newValues.append( key )
				if len(newValues):
					app.switch.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass


def changeM( path, stampM, stampA=None, meta=False, p=0 ):
	if p:
		mn = ''
		if time_diff(stampM) == 'today':
			mn = ', '+str(int((time.time() - stampM) /60)) + ' min'
			if mn == '0 min':
				mn = ', just now'
		print( friendlyDate(stampM), colorThis( [time_diff(stampM)+ mn], 'yellow', p=0 ), path )
	if stampA is None:
		stampA = stampM
	# print(stampM)
	# print(stampA)
	global changeDate_Table
	global _dir
	global touch_meta



	if _dir is None:
		import _rightThumb._dir as _dir

	if meta:
		touch_meta = getTable( 'touch.meta' )
		if not path in touch_meta:
			touch_meta[path] = {}
		if not 'epoch' in touch_meta[path]:
			touch_meta[path]['epoch'] = {}
		touch_meta[path]['epoch']['me'] = stampM
		touch_meta[path]['epoch']['ae'] = stampA
		saveTable( touch_meta, 'touch.meta', p=0 )

	if not meta:
		if changeDate_Table is None:
			changeDate_Table = getTable( 'touch.index' )
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		if os.path.isfile(path):
			if not path in changeDate_Table:
				changeDate_Table[path] = _dir.info(path)
				saveTable( changeDate_Table, 'touch.index', p=0 )
			try:
				os.utime(path,(stampA, stampM))
			except Exception as e:
				pass


def getTable( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	# defaults to myTables
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile


	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		# print( 'theFile', theFile )
		# print( 'file0', file0 )
		# import bigjson
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		return json_data
		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()


def time_diff(epoch):
	return dateDiffText( epoch )
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	return _dir.time_diff(autoDate(epoch))


def autoDate( theDate ):
	# if type(theDate) == float or type(theDate) == int:
	#   return theDate
	import _rightThumb._date as _date
	return _date.autoDate( theDate )


def dateDiffText( theDate, epoch=None ):

	y=0
	m=0
	w=0

	theDate = autoDate( theDate )
	if epoch is None:
		epoch = time.time()
	# woy = getWOY( theDate )
	days = abs(daysDiff( theDate, epoch ))
	
	if theDate < epoch:
		end = '<'
	else:
		end = '>'

	msDiff = epoch - theDate

	if msDiff > 0 and msDiff <= 86400:
		return 'today'
	elif msDiff > 0 and msDiff <= 82800:
		return 'today'
	elif msDiff > 0 and msDiff <= 169200:
		return 'yesterday'
	elif msDiff > 0 and msDiff <= 604801:
		return 'this week'



	# print( theDate, days, theDate < epoch, theDate > epoch, epoch, time.time() )
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'

	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )

	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )


def daysDiff( one, two ):
	global date_datetime
	oneA = autoDate( one )
	twoB = autoDate( two )
	g = 1
	if two > one:
		g = 2

	if one == two:
		return 0
	elif one > two:
		one = friendlyDate( oneA ).split(' ')[0]
		two = friendlyDate( twoB ).split(' ')[0]
	else:
		one = friendlyDate( twoB ).split(' ')[0]
		two = friendlyDate( oneA ).split(' ')[0]


	# print( '090', one, two )

	oneB = one.split('-')
	twoB = two.split('-')
	if date_datetime is None:
		from datetime import date as date_datetime
	d0 = date_datetime(int(oneB[0]), int(oneB[1]), int(oneB[2]))
	# print( '080', twoB )
	d1 = date_datetime(int(twoB[0]), int(twoB[1]), int(twoB[2]))
	delta = d1 - d0
	dd = delta.days
	if g == 1:
		dd = abs(dd)
	return dd


def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )


def getWOY( theDate ):
	theDate = autoDate( theDate )
	woy = getWOYFromEpoch(theDate)
	year = getYearFromEpoch(theDate)
	weekAndYear = round(woy * 0.01,2) + year
	weekAndYear = str(weekAndYear)
	if len(weekAndYear) == 6:
		weekAndYear += '0' 
	return weekAndYear


def getYearFromEpoch(theDate):
	theDate = autoDate(theDate)
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]


def getWOYFromEpoch(theDate):
	# print('theDate:',theDate)
	theDate = autoDate(theDate)

	try:
		return datetime.datetime.fromtimestamp( theDate ).isocalendar()[1]
	except Exception as e:
		print( 'Error:', theDate )
		sys.exit()


def colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False, simpleDic=False, colorProfile=None,      p=None, c=None, sd=None, isError=False ):

	if isError:
		color = 'red'

	if not c is None:
		color = c
	if not sd is None:
		simpleDic = sd

	if not p is None:
		shouldPrint = p

	if simpleDic and type(strings) == dict:
		newString = ''
		for k in strings.keys():
			newString += ' ' + k + ': ' + str(strings[k]) + ' '
		strings = newString

	if simpleDic and type(strings) == list:
		for i,thisItem in enumerate(strings):
			if type(thisItem) == dict:
				newString = ''
				for k in thisItem.keys():
					newString += ' ' + k + ': ' + str(thisItem[k]) + ' '
				strings[i] = newString

# [ { 'color': 'red', 'field': 'match', 'i': 0  } ]
# [ { 'color': 'red', 'field': 'match' } ]
# [ { 'color': 'red', 'i': 0  } ]
# { 'color': 'red', 'i': 0  }
# ['red',1]
# [2,'red']
# ['name','yellow']
# 'red,green'
# 'red,green:*'
# '*red,green'
# 'green,red,green:*'
# 'green:2,red:*,green'

# topic_index
#   'float,2'


# ColorBold Color Background BackgroundGrey BackgroundGreyBold

	
	# color_index = generateColorIndex()
	# colorProfileTmp = []
	# index = {
	#             'i': [],
	#             'keys': [],
	#             'data': {},
	# }
	# if not colorProfile is None:
	#     if type(colorProfile) == str:
	#         if type(strings) == list and ',' in colorProfile:
	#             if colorProfile.count('*') > 1:
	#                 print( ' only 1 * ' )
	#             new_CP = []
	#             cp = colorProfile.split(',')
	#             end = len(strings)-1
	#             leftC = len(cp)-1
	#             leftL = end


	#             for i,xx in enumerate(strings):



	#     if type(colorProfile) == list:
	#         for i,record in enumerate(colorProfile):
	#             if type(record) == dict:
	#                 record['id'] = i
	#                 if 'c' in record.keys():
	#                     record['color'] = record['c']
	#                     del record['c']

	#                 if 'f' in record.keys():
	#                     record['field'] = record['f']
	#                     del record['f']

	#                 if 'column' in record.keys():
	#                     record['field'] = record['column']
	#                     del record['column']


	#                 if 'i' in record.keys():
	#                     index['i'].append( record['i'] )
	#                     index['data'][i] = record
					
	#                 if 'field' in record.keys():
	#                     if ',' in record['field']:
	#                         for ef in record['field'].split(','):
	#                             index['keys'].append( ef )
	#                             index['data'][ ef ] = record
	#                     else:
	#                         index['keys'].append( record['field'] )
	#                         index['data'][record['field']] = record
	#                 colorProfileTmp.append( record )
					
	#             if type(record) == list:
	#                 if len(record) == 2:
	#                     newRecord = { 'id': i }


	#                     if type( record[0] ) == int:
	#                         newRecord['i'] = record[0]
	#                         newRecord['color'] = record[1]

	#                     elif type( record[1] ) == int:
	#                         newRecord['i'] = record[1]
	#                         newRecord['color'] = record[0]
	#                     else:
	#                         if record[0].lower() in color_index:
	#                             newRecord['field'] = record[0]
	#                             newRecord['color'] = record[1]
	#                         if record[1].lower() in color_index:
	#                             newRecord['field'] = record[1]
	#                             newRecord['color'] = record[0]

	#                     if 'color' in newnewRecord.keys():

	#                         if 'i' in newRecord.keys():
	#                             index['i'].append( newRecord['i'] )
	#                             index['data'][i] = newRecord
							
	#                         if 'field' in newRecord.keys():
	#                             if ',' in newRecord['field']:
	#                                 for ef in newRecord['field'].split(','):
	#                                     index['keys'].append( ef )
	#                                     index['data'][ ef ] = newRecord
	#                             else:
	#                                 index['keys'].append( newRecord['field'] )
	#                                 index['data'][newRecord['field']] = newRecord
	#                         colorProfileTmp.append( newRecord )



	#     if type(colorProfile) == dict:
	#         record = colorProfile
	#         if 'c' in record.keys():
	#             colorProfile[i]['color'] = record['c']
	#             record['color'] = record['c']
	#         if 'f' in record.keys():
	#             colorProfile[i]['field'] = record['f']
	#             record['field'] = record['f']
	#         if 'column' in record.keys():
	#             colorProfile[i]['field'] = record['column']
	#             record['field'] = record['column']


	#         if 'i' in record.keys():
	#             index['i'].append( record['i'] )
			
	#         if 'field' in record.keys():
	#             index['keys'].append( record['field'] )
	#         colorProfile = [record]




	if type(strings) == list:

		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	global switches
	if app.switch.isActive( 'NoColor' ):
		if shouldPrint:
			print(string)
			return string
		else:
			return string

	if ipsum:
		string = ipsumSentence()

	found = False

	if color == 'help':
		print()
		print()
		print( "_.colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print()
		print()
		colorHelp( ipsum )


	if '.' in color:

		try:
			result = eval( color + '+ string + app.Color.end')
		except Exception as e:
			pass
		else:
			found = True

	else:
		color = color.lower()


	if not found and notBold:
		try:
			result = eval( 'app.Color.' + color + '+ string + app.Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'app.ColorBold.' + color + '+ string + app.ColorBold.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'app.Color.' + color + '+ string + app.Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'Background.' + color + '+ string + Background.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGrey.' + color + '+ string + BackgroundGrey.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGreyBold.' + color + '+ string + BackgroundGreyBold.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		printBold( 'Error: _.colorThis: color not found ' + str(color), 'red' )
		print()
		print( strings )
		print()
		colorHelp( ipsum )

		sys.exit()

	if shouldPrint:
		try:
			print( result )
		except Exception as e:

			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')
		if isError:
			sys.exit()
		return None



	return result


def colorHelp( ipsum=False ):
	global colorHelp_colorList
	for sample in colorHelp_colorList:
		if not len( sample ):
			print()
		else:
			result = eval( sample + '+ "THE_TEXT" + app.Color.end' )
			if ipsum:
				result = result.replace( 'THE_TEXT', ipsumSentence() )
			else:
				result = result.replace( 'THE_TEXT', sample )
			
			print( result )
	sys.exit()


def ipsumSentence():
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	ipsum = ipsum.replace( '\n', ' ' )
	sentences = []
	for sentence in ipsum.split('.'):
		sentence = _str.replaceDuplicate( sentence, ' ' )
		sentence = _str.cleanBE( sentence, ' ' )
		sentence = sentence + '.'
		sentences.append({ 'sentence': sentence, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', sentences )
	return randomized[0]['sentence']


def genUUID( project='', label='', uniqueTimestamp=False ):
	global appData
	global appInfo
	uuid = __.imp('uuid')
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	try:
		type(appData[__.appReg]['uuid'])
		good = True
	except Exception as e:
		good = False
	if good:

		try:
			timestamp = appData[__.appReg]['start']
		except Exception as e:
			timestamp = time.time()

		if not project == '' or not label == '':
			if type(appData[__.appReg]['uuid']) == str:
				# print()
				# print( '__.appReg', __.appReg )
				# print()
				# print(d2json( appData ))
				# print()
				appData[__.appReg]['uuid'] = {}
				# print(appInfo[__.appReg]['file'])
				# sys.exit()
				appData[__.appReg]['uuid']['app'] = appInfo[__.appReg]['file']

			if not type(appData[__.appReg]['uuid']) == str:
				
				appData[__.appReg]['uuid']['uuid'] = string
				appData[__.appReg]['uuid']['timestamp'] = timestamp
				appData[__.appReg]['uuid']['project'] = ''
				appData[__.appReg]['uuid']['label'] = ''

				if uniqueTimestamp:
					appData[__.appReg]['uuid']['timestamp'] = time.time()

				if not project == '':
					appData[__.appReg]['uuid']['project'] = project

				if not label == '':
					appData[__.appReg]['uuid']['label'] = label
					
				uuidLog = getTable('uuid_log.json')
				uuidLog.append(appData[__.appReg]['uuid'])
				saveTable(uuidLog,'uuid_log.json',printThis=False)
			# appData[__.appReg]['uuid'] = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string


def d2json( data, sort_keys=False ):
	simplejson = __.imp('simplejson')
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return simplejson.dumps(data, indent=4, sort_keys=sort_keys)


def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		if not e:
			return None
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines


def saveTable2( rows, theFile, printThis=False, sort_keys=False, indentCode=True, p=None, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not p is None:
		printThis = p
	# print('*******************',theFile)
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + theFile

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = simplejson.dumps(rows)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print('Saved: ' + theFile)
	if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );


def printBold( string, color='white', prefix='' ):
	
	if '\n' in string:
		string = string.replace( '\n', '\n'+prefix )
	else:
		string = prefix + string
	
	global switches
	if app.switch.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print( app.ColorBold.white + string + app.ColorBold.end )
	elif color == 'red':
		print( app.ColorBold.red + string + app.ColorBold.end )
	elif color == 'gray' or color == 'grey':
		print( app.ColorBold.gray + string + app.ColorBold.end )
	elif color == 'green':
		print( app.ColorBold.green + string + app.ColorBold.end )
	elif color == 'yellow':
		print( app.ColorBold.yellow + string + app.ColorBold.end )
	elif color == 'blue':
		print( app.ColorBold.blue + string + app.ColorBold.end )
	elif color == 'magenta':
		print( app.ColorBold.magenta + string + app.ColorBold.end )
	elif color == 'cyan':
		print( app.ColorBold.cyan + string + app.ColorBold.end )


def generateColorIndex():
	global app_full_color_index
	if not app_full_color_index is None:
		return app_full_color_index
	colorClasses = 'ColorBold Color Background BackgroundGrey BackgroundGreyBold'
	list_of_colors = []
	test = 0
	if test == 0:
		for cc in colorClasses.split(' '):
			for x in dir(  eval(  '_.'+cc  )  ):
				if not x.startswith('_'):
					
					subject = x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )

					subject = cc+'.'+x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )


	test = 1
	if test == 1:
		for x in _.colorHelp_colorList:
			if '.' in x:
				p = x.split('.')
				a = p[0]+'.'
				aa = a.lower()
				b = p[1]
				bb = b.lower()

				subject = bb
				if not subject in list_of_colors:
					list_of_colors.append( subject )

				subject = x.lower()
				if not subject in list_of_colors:
					list_of_colors.append( subject )


	app_full_color_index = []

	for x in list_of_colors:
		if not '.' in x:
			app_full_color_index.append( x )

	for x in list_of_colors:
		if '.' in x:
			app_full_color_index.append( x )

	return app_full_color_index


def addComma( data ):
	test = 0
	try:
		int(data)
		test+=1
	except Exception as e:
		pass
	try:
		float(data)
		test+=1
	except Exception as e:
		pass
	
	if not test:
		return data

	txt = str( data )
	if '.' in txt:
		txt = txt.split( '.' )[0]
	n = []
	for x in txt:
		n.append( x )
	n.reverse()
	y = []
	for i,x in enumerate(n):
		y.append( x )
		if ((i+1)%3==0):
			y.append( ',' )
	y.reverse()
	result = ''.join( y )
	result = _str.cleanBE( result, ',' )
	return result


def loopPrint(  length=5, txt=' ', p=0 ):
	if not length:
		return ''
	i=0
	result = ''
	while not i == length:
		result += txt
		i+=1
	if p:
		print(result)
	return result


def ci(string): 
	#switchValueClean
	global ciData
	# print( ciData )
	# sys.exit()
	for cx in ciData:
		if cx[0] in string:
			# print( 'HERE', cx )
			string = string.replace( cx[0], cx[1] )
	
	string = string.replace( ';d;', __.theDelim )
	string = string.replace( ';delim;', __.theDelim )
	string = string.replace( ';thedelim;', __.theDelim )
	string = string.replace( ';theDelim;', __.theDelim )



	return string


def printVarSimple( data, sort_keys=False, isDic=None, prefix=None, remove=None ):
	data = json_clean(data)
	if not isDic is None and isDic and type(data) == str:
		saveText( data, _v.myTemp + _v.slash+'printVarSimple.json' )
		data = getTable2( _v.myTemp + _v.slash+'printVarSimple.json' )
	printVarOld( data, sort_keys, prefix=prefix, remove=remove )


def printVarOld( data, sort_keys=False, prefix=None, remove=None ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	if not remove is None:
		for x in remove:
			result = result.replace(x,'')
	if prefix is None:
		print( result )
	else:
		for x in result.split('\n'):
			print( prefix+x )


def printVarColor_OLD( data ):
	result = ''
	for char in data:
		result += printVarColorChar( char )
	return result


def printVarColorChar( data ):


	what = '('
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )

	what = ')'
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )


	what = '{'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '}'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '['
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineColor( what, color ) )

	what = ']'
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '"'
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = "'"
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ':'
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ','
	color = 'Magenta'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '='
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	return data


def inlineBold( string, color='white' ):
	global switches
	if app.switch.isActive( 'NoColor' ):
		return string
	
	string = str(string)
	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		return app.ColorBold.white + string + app.ColorBold.end 
	elif color == 'red':
		return app.ColorBold.red + string + app.ColorBold.end 
	elif color == 'gray' or color == 'grey':
		return app.ColorBold.gray + string + app.ColorBold.end 
	elif color == 'green':
		return app.ColorBold.green + string + app.ColorBold.end 
	elif color == 'yellow':
		return app.ColorBold.yellow + string + app.ColorBold.end 
	elif color == 'blue':
		return app.ColorBold.blue + string + app.ColorBold.end 
	elif color == 'magenta':
		return app.ColorBold.magenta + string + app.ColorBold.end 
	elif color == 'cyan':
		return app.ColorBold.cyan + string + app.ColorBold.end
	elif color == 'underline':
		return app.ColorBold.underline + string + app.ColorBold.end


def inlineColor( string, color='red' ):

	global switches
	if app.switch.isActive( 'NoColor' ):
		return string

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		return app.Color.red + string + app.Color.end
	elif color == 'cyan':
		return app.Color.cyan + string + app.Color.end
	elif color == 'darkcyan' or color == 'grey':
		return app.Color.darkcyan + string + app.Color.end
	elif color == 'blue':
		return app.Color.blue + string + app.Color.end
	elif color == 'green':
		return app.Color.green + string + app.Color.end
	elif color == 'yellow':
		return app.Color.yellow + string + app.Color.end
	elif color == 'underline':
		return app.Color.underline + string + app.Color.end


def getTable2( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def saveText( rows, theFile, errors=True, me=0 ):
	HD.chmod(theFile)
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print(type(rows))
		if type(rows) == str:
			# print(rows)
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		try:
			open(theFile, 'wb').write(rows)
		except Exception as e:
			try:
				open(theFile, 'w').write(rows)
			except Exception as e:
				new_text = ''
				for x in rows:
					if x in _str.printable:
						new_text+=x
				open(theFile, 'w', encoding='utf-8').write(new_text)
		HD.chmod(theFile)
		# if errors:
		#   print( 'Auto correction when saving text' )
	if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );


def json_clean(obj):
	if hasattr(obj, '__class__') and '.'  in str(obj.__class__):
		obj = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__'))
		obj = prep4JSON(obj)
	return obj


def prep4JSON(d, to_delete=None):
	# remove keys from multidimensional dicts and lists
	def autoFindKeys(d):
		# removes functions and methods
		global autoFindKeys_temp
		if isinstance(d, dict):
			for k in d.keys():
				t = type( d[k] )
				if 'function' in str(t):
					autoFindKeys_temp.append( k )
				elif 'method' in str(t):
					autoFindKeys_temp.append( k )
				
			for k, v in d.items():
				autoFindKeys(v)
		elif isinstance(d, list):
			for i in d:
				autoFindKeys(i)
		return d

	if to_delete is None:
		global autoFindKeys_temp
		autoFindKeys_temp = []
		autoFindKeys(d)
		return prep4JSON(d, to_delete=autoFindKeys_temp)

	if isinstance(to_delete, str):
		to_delete = [to_delete]
	if isinstance(d, dict):
		for single_to_delete in set(to_delete):
			if single_to_delete in d:
				d[single_to_delete] = ' ** removed ** '
		for k, v in d.items():
			prep4JSON(v, to_delete)
	elif isinstance(d, list):
		for i in d:
			prep4JSON(i, to_delete)
	return d


class dot:
	def __init__( self ):
		pass


def isDate( theDate, record={}, tz=None, q=True ):
	s = time.time()
	# slow from loading pandas
	if not tz is None and not len(tz):
		tz = None

	global _tz
	if _tz is None:
		import _rightThumb._tz as _tz

	local_tz = str(time.strftime("%z")).replace(':','')

	hasTZ = False
	if type(theDate) == str and len(theDate) > 11:
		if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
			hasTZ = theDate[-6:].replace(':','')

	if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
		if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
			hasTZ = theDate[-5:].replace(':','')








	epoch = autoDate(theDate)

	if not type(hasTZ) == bool:
		if not hasTZ == local_tz:
			epoch = _tz.convert( epoch, hasTZ, local_tz )

	if not tz is None and not local_tz == tz:
		epoch = _tz.convert( epoch, local_tz, tz )
		local_tz = tz


		if '/' in tz:
			global arrow
			if arrow is None:
				import arrow
			utc = arrow.utcnow()
			theDate = str(utc.to(tz))
			hasTZ = False
			if type(theDate) == str and len(theDate) > 11:
				if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
					hasTZ = theDate[-6:].replace(':','')

			if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
				if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
					hasTZ = theDate[-5:].replace(':','')
			local_tz = hasTZ

	

	if not epoch:
		return record
	global _dir
	global pandas
	if pandas is None:
		if q:
			try:
				#  pandas  takes .5 seconds to load 
				import pandas
			except Exception as e:
				pass
	if _dir is None:
		import _rightThumb._dir as _dir
	ss = time.time()
	record['epoch'] = epoch
	record['ordinal'] = datetime.datetime.fromtimestamp( epoch ).toordinal()
	record['sdate'] = friendlyDate2( epoch )
	record['strip'] = onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0])
	record['stript'] = onlyNumbers_strip(friendlyDate( epoch ))
	record['date'] = friendlyDate( epoch ).split(' ')[0]
	record['time'] = friendlyDate2( epoch ).split(' ')[1]
	record['fdate'] = friendlyDate( epoch )
	record['month'] = _dir.getMonthFromEpoch( epoch )
	record['year'] = _dir.getYearFromEpoch( epoch )
	record['woy'] = _dir.getWeekAndYear( epoch )
	record['dow'] = _dir.getDOWromEpochText( epoch )
	record['ago'] = _dir.dateDiffText( epoch )
	record['days'] = daysDiff(  epoch, time.time()  )
	record['tz'] = local_tz
	

	try:
		import _rightThumb._nID as _nID
		_nID.mini.password( '1970' )
		eee = ''
		ee = str(record['epoch'])
		for c in ee:
			if '.' == c:
				break
			eee+=c
		record['nID'] = _nID.mini.gen( record['strip'] )
		record['nIDt'] = _nID.mini.gen( record['stript'] )
		record['nIDe'] = _nID.mini.gen( int(eee) )
	except Exception as e:
		pass


	try:
		import _rightThumb._stardate as _sd
		record['stardate'] = _sd.gen(  epoch  )
	except Exception as e:
		pass

	dt = record['fdate'].split(' ')[0].split('-')
	try:
		record['quarter'] = str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
	except Exception as e:
		pass

	e = time.time()
	# print( e-s )
	# print( e-ss )
	return record


def friendlyDate2( theDate ):
	fd = friendlyDate( theDate )
	if type(fd) == str and len(fd):
		fd = fd[:-3][2:]
		# if fd.startswith('21-'):
		#   fd = fd[3:]
	return fd


def onlyNumbers_strip(n):
	n = str(n)
	t = ''
	for c in n:
		if c in '0123456789':
			t+=c
	return t


def formatColumns(columns):
	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if ':' in c:
				hasPre = True
				# c = c.replace(':','.')
				preDataR = c.split(':')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a == c:
						c = col['name']
			if hasPre:
				c = preData + ':' + c
			result += c + ','
		result = result[:-1]
	# print(result)
	return result


def tfc(c):
	return c.lower().replace(' ','_')


def autoWrapText( text, length=None, txt=False, prefix='', breakOn=None, pre_skip_0=False ):
	if type(prefix) == int:
		n = ''
		i=0
		while i < prefix:
			n += ' '
			i+=1
		prefix=n
	if length is None:
		length = __.terminal.cols-5
	# -copy
	if not pre_skip_0:
		length = length - len(prefix)
	text = str(text)
	if len(text) <= length:
		if not pre_skip_0:
			return prefix+text
		else:
			return text
	if breakOn is None:
		breakAfter = ' ,;(+)\\/.?*&@!_{-}:=`"<~>\'| !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
	else:
		breakAfter = breakOn
	broken = []
	parts = []
	flag = None
	i = 0
	last = -1
	ii = 0
	while i <= len(text)-1:
		ii+=1
		if text[i] in breakAfter:
			flag = i
		if ii > length:
			if not flag is None:
				prt = text[ last+1 : flag+1 ]
				i = flag
				last = flag
			else:
				prt = text[ last+1 : i ]
				last = i-1
			if pre_skip_0 and not parts:
				parts.append(prt)
			else:
				parts.append(prefix+prt)
			flag = None
			ii=0
		i+=1
	if not last == i:
		prt = text[ last+1 : i ]
		if pre_skip_0 and not parts:
			parts.append(prt)
		else:
			parts.append(prefix+prt)

	if txt:
		return '\n'.join(parts)

	return parts


def percentageDiffIntAuto( smaller, bigger, isFloat=False ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float((s/b)*100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result


class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table

# switches = Switches()
_dir = None
errors = []
# fields = Fields()
changeDate_Table = None
touch_meta = None
date_datetime = None
colorHelp_colorList = app.colorHelp_colorList
ipsum = None
appData = {}
appInfo = {}
app_full_color_index = None
colorizeRow_last = None
row_colors_ID = 0
row_colors = []
ciData = app.ciData
_tz = None
arrow = None
pandas = None




############################################################## copy-fn-class


class Subject:

	def __init__(self):
		self.tables = []
		self.index = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.group_space = False



	def aggregate( self, name=None, code=None ):
		if code is None:
			return None
		if name is None:
			name = self.tables[ len(self.tables)-1 ].name
		
		self.tables[ self.index[name] ].aggregate( code )


	def rprint( self, asset, columns=None, name=None, n=None, sc=True, printColumns=True, h=None, l=None, p=None ):
		if columns is None:
			columns = ','.join(list(asset[0].keys()))
		

		if not h is None:
			printColumns = h
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		if sc and app.switch.isActive('Column'):
			columns = app.switch.value('Column')
		self.print( name, columns, printColumns=printColumns, l=l, p=p )



	def rsort( self, asset, columns, name=None, n=None ):
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		return self.returnSorted( name,columns,asset )
		# return self.sort( name, columns )


	def register( self, name=None, asset = [], group_space=True, tab='',    gs=None, t=None, n=None, w=True ):
		global TableProfile_Config
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		if not __.table_b_print:
			for i,record in enumerate(asset):
				for field in record.keys():
					if str( record[field] ) == 'b':
						asset[i][field] = ''


		found = False
		thisID = False
		if not gs is None:
			group_space = gs
		elif 'ALLTABLES' in TableProfile_Config.keys() and 'GroupSpaces' in TableProfile_Config['ALLTABLES'].keys():
			group_space = TableProfile_Config['ALLTABLES']['GroupSpaces']
		else:
			group_space = app.switch.isActive('GroupSpaces')
		if not t is None:
			tab = t
		for i,t in enumerate(self.tables):
			if t.name == name:
				thisID = i
				found = True
				self.tables[i].maxNameLength = self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if found:
			self.tables.pop( thisID )
			found = False

		if not found:
			self.tables.append(Table( name, asset, group_space, tab, w ))
			self.tables[ len( self.tables )-1 ].maxNameLength = self.maxNameLength
			self.index[name] = len( self.tables )-1
		return name

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False, pc=None, printColumns=True, h=None, l=None, p=None ):
		if not h is None:
			printColumns = h
		global switches
		if not ',' in fields:
			pc = False

		xXx = app.switch.records('dic_on-off-v')
		if 'Sort' in xXx['on']:
			sortBy = xXx['values']['Sort']
			self.sort( name, ','.join( sortBy ) )
			# print( sortBy )
			# sys.exit()
		if not pc is None:
			printColumns = pc
		# print(name,fields)
		sI = None
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					if not ',' in fields:
						printColumns = False
					self.tables[i].print(fields,fieldLengths,printColumns=printColumns, l=l, p=p)
					sI = i
				else:
					print('Null Set')
			i += 1
		if app.switch.isActive('FieldTotal'):
			fieldTotals = {}
			for field in app.switch.values('FieldTotal'):
				fieldTotals[field] = { 'actual': None, 'total': 0 }
				for rec in self.tables[sI].asset:
					for key in rec.keys():
						if check_field_match( key, field ):
							fieldTotals[field]['actual'] = key
							thisFieldA = str(rec[key])
							thisFieldB = []
							for char in thisFieldA:
								if char in '0123456789':
									thisFieldB.append(char)
							thisFieldC = int(''.join(thisFieldB))
							fieldTotals[field]['total'] += thisFieldC
			print()
			print()
			for field in fieldTotals:
				print( addComma(fieldTotals[field]['total']),'\t', fieldTotals[field]['actual'] )




	def sort(self,name,fields):
		fields = fields.replace('.',':')
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def returnSorted(self,name,fields,asset = []):
		fields = fields.replace('.',':')
		if len(asset) > 0:
			self.register(name,asset)

		result = []
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
				result = self.tables[i].asset
			i += 1
		return result
	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True, me=0):
		HD.chmod(theFile)
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1
		HD.chmod(theFile)
		if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#   if spaces > totalColumnWidth:
		#       totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		# for m in self.meta['data']:
		#   genLine(totalColumnWidth,'=')
		#   print('Table:\t',m['table'])
		#   print('Parent:\t',m['parent'])
		#   print('Records:',m['count'])
		#   print()
		#   tables.register(m['table'],m['fields'])
		#   tables.fieldProfileSet(m['table'],'*','alignment','center')
		#   tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#   genLine(totalColumnWidth,'=')
		# print()
		# print('Records:',self.meta['records'])
		# print()
		# print('Errors:')
		# for e in self.meta['errors']:
		#   print('\t',e)

		return result



	def eof( self ):
		try:
			__.aggregate.eof.storage
		except Exception as e:
			shouldPrint = False
		else:
			shouldPrint = True

		if not __.aggregate.eof.storage:
			shouldPrint = False

		if shouldPrint:
			print()
			print()

			linePrint()

			# print()
			# printVarSimple( __.aggregate.eof.storage )


		footer = {}
		aSettings = {}

		for k in __.aggregate.eof.storage:
			if k.startswith('eof?'):
				f = k[len('eof?'):]
				for y in __.aggregate.eof.storage[k]:
					for sv in __.aggregate.eof.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.eof.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.eof.storage[k][y]['settings']:
						__.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					theKey = f +' '+ y
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eof?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y

					# print( 'format:', __.aggregate.format )
					# print( 'k y:', k, y  )

					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = addComma( __.aggregate.eof.storage[k][y]['data'] )



					# # print(  )
					# footer[ theKey ] = __.aggregate.eof.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.eof.storage[k][y]['data'] )
		if footer:
			print()
			# print()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			# print( __.aggregate.config )
			print()





