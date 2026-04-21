class TableView:
	def __init__(self,name,table,fields,sort):
		self.name=name
		self.fields=fields
		self.sort=sort
		self.table=table
TableProfile_Config={}
class Table:
	def __init__( self, name, asset=[], group_space=True, tab='' ):
		global switches
		global _dir
		self.group_space=group_space
		self.name=name
		self.asset=asset
		self.fields=[]
		self.views=[]
		self.spaces={}
		self.maxNameLength=35
		if switches.isActive('Long'):
			try:
				self.maxNameLength=int(switches.value('Long'))
			except Exception as e:
				self.maxNameLength=35
		self.columnTab='   '
		self.groupSeparator='_'
		self.tableProfile=[]
		self.tableProfileDefaultAlignment='left'
		self.tableProfileDefaultAlignmentHeader=''
		self.tableProfileDefaultAlignmentChanged=False
		self.tableProfileDefaultAlignment=False
		self.tableProfileDefaultSupersedes=False
		self.views=[]
		self.universalSpacing=False
		self.wrapTableKey='Da529801Ef674997B9f3382B3eD2b93F'
		self.backup=dot()
		self.backup.asset=asset.copy()
		self.aggregate_processed=False
		self.isWrap=False
		self.hasAggregate=False
		self.hasGroups=False
		self.backup.fields={}
		self.backup.allfields={}
		self.backup.NGfields={}
		self.groupID_KEY=genUUID()
		if len( self.asset ):
			for r in self.asset:
				for k in r:
					if not k in self.backup.fields:
						self.backup.fields[k]=1
						self.backup.allfields[ tfc(k) ]=k
						self.backup.NGfields[ tfc(k) ]=k
		self.tab_color=''
		if type(tab)==list:
			self.tab_color=tab[1]
			tab=tab[0]
		tabH=''
		i=0
		while not i==len(tab):
			i+=1
			tabH+=' '
		self.tab={ 'header': tabH, 'table': tab }
	def registerView(self,name,fields,sort=''):
		self.views.append(TableView(name,self.name,fields,sort))
	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			if self.views[i].name==name:
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				self.print(self.views[i].fields)
			i +=1
	def nameLength(self,string,suffix):
		result=''
		toLong=False
		if switches.isActive('Length'):
			result=self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i=0
				for L in string:
					if i <=self.maxNameLength:
						result +=L
					else:
						toLong=True
					i +=1
				if toLong==True:
					result +='...'
					if len(suffix) > 0:
						result +='  .' + suffix
			except Exception as e:
				result=string
		return result
	def nameLengthFix(self,string,change,suffix):
		result=''
		toLong=False
		change=change.lower()
		old=self.maxNameLength
		if 'x' in change:
			change=change.replace('x','')
			newLength=self.maxNameLength * int(change)
		else:
			newLength=self.maxNameLength + int(change)
		try:
			i=0
			for L in string:
				if i <=newLength:
					result +=L
				else:
					toLong=True
				i +=1
			if toLong==True:
				result +='...'
				if len(suffix) > 0:
					result +='  .' + suffix
		except Exception as e:
			result=string
		return result
	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows=self.asset
		spacer=1
		size=len(name) + spacer
		try:
			pass
			if name in rows[0]:
				rows[0][name]
			else:
				eval(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
		except Exception as e:
			pass
		for item in rows:
			shorten=True
			if switches.isActive('Long')==True:
				shorten=False
				if switches.isActive('ShortenColumn')==True:
					shortenColumn=switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc==name:
							shorten=True
			if name in item:
				thisData=item[name]
			elif name.split('.')[0] in item:
				thisData=eval(  'item["' + '"]["'.join(name.split('.')) + '"]'  )
			if shorten==True and not switches.isActive('Length'):
				try:
					text=self.nameLength( str(self.scriptTriggerField(name,thisData)) ,'')
				except Exception as e:
					text=self.nameLength(str(thisData),'')
			else:
				if switches.isActive('Length'):
					try:
						text=self.nameLengthFix(  str(self.scriptTriggerField(name,thisData)) ,switches.value('Length'),'')
					except Exception as e:
						text=self.nameLengthFix(str(thisData),switches.value('Length'),'')
				else:
					try:
						text=self.scriptTriggerField(name,thisData)
					except Exception as e:
						text=thisData
			itemSize=len(str(text)) + spacer
			if itemSize > size:
				size=itemSize
		return size
	def addSpace(self,string,max):
		dif=int(max) - len(string)
		build=''
		for x in range(dif):
			build=build + ' '
		return build
	def addSpace2(self,max):
		dif=int(max)
		build=''
		for x in range(dif):
			build=build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i=0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes']==True:
					if ',' in self.tableProfile[i]['name']:
						found=False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found=True
						if found:
							value=self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value=self.tableProfile[i]['script_trigger'](value)
				else:
					if field==self.tableProfile[i]['name']:
						value=self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i +=1
		return value
	def triggerExecute(self,field,value):
		i=0
		for s in self.tableProfile:
			if self.tableProfile[i]['name']==field:
				try:
					value=self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			else:
				if type(value)==int:
					value=addComma( str(value) )
			i +=1
		return value
	def fieldProfileSet(self,field,propertyName,value):
		field=field.lower()
		if field=='*' and propertyName=='alignment':
			self.tableProfileDefaultAlignment=value
			self.tableProfileDefaultAlignmentChanged=True
		if field=='_header_' and propertyName=='alignment':
			self.tableProfileDefaultAlignmentHeader=value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)
			found=False
			i=0
			for s in self.tableProfile:
				if self.tableProfile[i]['name']==field:
					found=True
					self.tableProfile[i][propertyName]=value
				i +=1
			if not found:
				item=len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})
	def fieldProfileGet(self,field,propertyName,isHeader=False):
		field=field.lower()
		i=0
		value=''
		if isHeader and '_header_' in TableProfile_Config.keys() and propertyName in TableProfile_Config['_header_'].keys():
			return TableProfile_Config['_header_'][propertyName]
		elif not isHeader and field in TableProfile_Config.keys() and propertyName in TableProfile_Config[field].keys():
			return TableProfile_Config[field][propertyName]
		elif '*' in TableProfile_Config.keys() and propertyName in TableProfile_Config['*'].keys():
			return TableProfile_Config['*'][propertyName]
		if propertyName=='alignment':
			value=self.tableProfileDefaultAlignment
		for s in self.tableProfile:
			if self.tableProfile[i]['name']==field:
				try:
					value=self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i +=1
		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value=self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value=self.tableProfileDefaultAlignmentHeader
		elif isHeader:
			value='center'
		if propertyName=='alignment' and value=='':
			value='left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		global errors
		global lastGroup
		global switches
		def test(one,two):
			if(one)==(two):
				return True
			else:
				return False
		groupByList=self.groupByList
		rows=self.asset
		columnList=column
		if column in rows[i]:
			value=str(self.triggerExecute(column,rows[i][column]))
		elif column.split('.')[0] in rows[i]:
			value=str(self.triggerExecute(column,  eval(  'rows[i]["' + '"]["'.join(column.split('.')) + '"]'  )  ) )
		value=value.replace('\n','')
		try:
			pass
		except Exception as e:
			pass
		shorten=True
		if switches.isActive('Long')==True:
			shorten=False
			if switches.isActive('ShortenColumn')==True:
				shortenColumn=switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc==column:
						shorten=True
		text=str(value)
		if shorten==True:
			text=self.nameLength(str(value),'')
		else:
			text=str(value)
		groupBy=switches.value('GroupBy')
		try:
			tabFix=self.spaces[column]
		except Exception as e:
			tabFix=self.tabGetMaxSpace(column)
			self.spaces[column]=tabFix
		if switches.isActive('GroupBy')==True:
			for gb in groupBy.split(','):
				gb=str(gb)
				if column==gb:
					if not test(groupByList[gb],text)==True:
						if groupBy.split(',')[0]==column:
							pass
							if self.group_space:
								print(self.groupLine(columnList,columnHeaderLength))
							if not self.isExtraRecord:
								for g in groupBy.split(','):
									groupByList[g]=''
						else:
							pass
							if self.group_space:
								print('')
						if not self.isExtraRecord:
							groupByList[gb]=text
						else:
							if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
								text=''
					else:
						pass
						if len(self.isExtraRecord_000x):
							self.isExtraRecord_0001[ self.isExtraRecord_000x.split('-')[0] ]=1
						text=''
		alignment=self.fieldProfileGet(column,'alignment')
		result=text + self.addSpace(text,tabFix)
		if alignment=='left':
			result=text + self.addSpace(text,tabFix)
		if alignment=='right':
			result=self.addSpace(text,tabFix) + text
		if alignment=='center':
			totalSpace=int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2==0:
					div2=totalSpace/2
					theLeft=div2
					theRight=div2
				else:
					divTMP=totalSpace - 1
					div2=divTMP/2
					theLeft=div2 + 1
					theRight=div2
			else:
				theLeft=0
				theRight=0
			result=self.addSpace2(theLeft) + text + self.addSpace2(theRight)
		return result
	def groupLine(self,columnList,columnHeaderLength):
		columnNumber=len(columnList.split(','))
		loop=0
		result=''
		while loop < columnHeaderLength +(columnNumber * 4):
			result +=self.groupSeparator
			loop +=1
		return result
	def showColumnHeader(self,column):
		result=''
		if type(self.universalSpacing)==dict:
			self.spaces=self.universalSpacing
		for c in column.split(','):
			try:
				tabFix=self.spaces[c]
			except Exception as e:
				tabFix=self.tabGetMaxSpace(c)
				self.spaces[c]=tabFix
			alignment=self.fieldProfileGet(c,'alignment',isHeader=True)
			if alignment=='':
				alignment='right'
			if alignment=='center':
				totalSpace=int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2==0:
						div2=totalSpace/2
						theLeft=div2
						theRight=div2
					else:
						divTMP=totalSpace - 1
						div2=divTMP/2
						theLeft=div2 + 1
						theRight=div2
				else:
					theLeft=0
					theRight=0
				result +=self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment=='left':
				result +=c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment=='right':
				result +=self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
		result +='\n'
		return '\n'+result
	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower()==column.lower():
				return k
		for k in self.asset[0].keys():
			if k.lower()==column.split('.')[0].lower():
				return column
	def prefixSize( self ):
		pre=''
		for x in self.tab['table']+loopPrint(__.table_prefix_padding):
			if x=='\t':
				pre +='	'
			else:
				pre +=x
		return len(pre)
	def wrapTable( self, cols=None ):
		if not __.terminal.width:
			return None
		cols=__.terminal.width
		cols -=8
		spaces=[]
		theKeys=[]
		for c in self.spaces:
			theKeys.append(c)
			spaces.append({ 'c': c, 's': self.spaces[c] })
		spaces=sorted(spaces, key=lambda d:(d['s']))
		spaces.reverse()
		fieldsToShorten=[]
		if not len(switches.value('WrapTable')):
			fieldsToShorten.append( spaces[0]['c'] )
			if len( self.spaces.keys() ) > 1:
				diff=percentageDiffIntAuto( spaces[0]['s'], spaces[1]['s'] )
				if diff >=50:
					fieldsToShorten.append( spaces[1]['c'] )
				if len( self.spaces.keys() ) > 2:
					diff=percentageDiffIntAuto( spaces[0]['s'], spaces[2]['s'] )
					if diff >=50:
						fieldsToShorten.append( spaces[2]['c'] )
		elif len(switches.value('WrapTable')):
			done=False
			if len(switches.values('WrapTable'))==1:
				done=False
				wrapBy=switches.value('WrapTable')
				if wrapBy in self.asset[0].keys():
					done=True
				if not done:
					if formatColumns(wrapBy) in self.asset[0].keys():
						wrapBy=formatColumns(wrapBy)
						done=True
				if not done:
					wrapBy=0
					try:
						wrapBy=int(switches.value('WrapTable'))
					except Exception as e:
						wrapBy=0
					if wrapBy > 0:
						done=True
			elif len(switches.values('WrapTable')) > 1:
				wrapBy=[]
				for xx in switches.values('WrapTable'):
					y=formatColumns(xx)
					if y in self.asset[0].keys():
						wrapBy.append(y)
						done=True
			if done:
				if type(wrapBy)==str:
					fieldsToShorten.append( wrapBy )
				if type(wrapBy)==list:
					for yy in wrapBy:
						fieldsToShorten.append( yy )
				if type(wrapBy)==int:
					for isp, itx in enumerate(spaces):
						fieldsToShorten.append( itx['c'] )
						if isp+1==wrapBy:
							break
		maxLen=self.maxNameLength
		total=self.prefixSize()
		for c in self.spaces:
			total +=self.spaces[c]
			total +=len(self.columnTab)
		tempSpaces=self.spaces.copy()
		for c in tempSpaces:
			if tempSpaces[c] > maxLen:
				if not c in fieldsToShorten:
					fieldsToShorten.append(c)
		while total > cols:
			hasGrtMax=False
			for fs in fieldsToShorten:
				if tempSpaces[fs] > maxLen:
					hasGrtMax=True
					tempSpaces[fs] -=1
			if not hasGrtMax:
				for fs in fieldsToShorten:
					tempSpaces[fs] -=1
			total=self.prefixSize()
			for c in tempSpaces:
				total +=tempSpaces[c]
				total +=len(self.columnTab)
		wrapTableKey=self.wrapTableKey
		counter=0
		global fields
		fields.register( wrapTableKey+'-b', 'val', 4, m=4 )
		fields.register( wrapTableKey, 'val', 7, m=12 )
		test=fields.padZeros( wrapTableKey, 'val', 5 )
		test=fields.padZeros( wrapTableKey+'-b', 'val', 5 )
		letters={}
		def letterBoost( i ):
			if not str(i) in letters:
				letters[str(i)]='a'
		recordsToAdd=[]
		for i,record in enumerate(self.asset):
			letters[ str(i) ]='a'
			recordKey=1
			this_key=fields.padZeros( wrapTableKey, 'val', i+1 )
			this_key_B=fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
			self.asset[i][wrapTableKey+'-sort']=this_key+'-'+this_key_B
			rec={}
			rec_last={}
			for c in tempSpaces:
				if c in record and len( str(record[c]) ) > tempSpaces[c]:
					recordKey=1
					rec_parts=autoWrapText( str(record[c]), length=tempSpaces[c] )
					rp=''
					last_rp=''
					for rp in rec_parts:
						if len(rp) and not last_rp==rp:
							last_rp=rp
							cs=fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
							recordKey +=1
							if not cs in rec:
								rec[cs]={}
							if not cs in rec_last:
								rec_last[cs]={}
							rec[cs][c]=rp
					rp=''
			if rec:
				for iii,xXx in enumerate(rec):
					if xXx=='0001':
						for c in rec[xXx]:
							self.asset[i][c]=rec[xXx][c]
					else:
						rec[xXx][wrapTableKey+'-sort']=this_key +'-'+ xXx
						recordsToAdd.append(rec[xXx])
		for rec in recordsToAdd:
			self.asset.append(rec)
		self.spaces={}
		groupBy=switches.values('GroupBy')
		last={}
		for gb in groupBy:
			last[gb]='{7270D97A-CC1D-4365-9545-87CA34F2F026}'
		for i,record in enumerate(self.asset):
			ks=list(record.keys())
			for k in theKeys:
				if not k in ks:
					self.asset[i][k]=''
			for k in theKeys:
				if not k in self.spaces:
					self.spaces[k]=0
				if len(str(record[k])) > self.spaces[k]:
					self.spaces[k]=len(str(record[k]))
		self.asset=sorted(self.asset, key=lambda d:(d[wrapTableKey+'-sort']))
		self.print(
					column=self.print_backup['column'],
					fieldLengths=self.print_backup['fieldLengths'],
					pc=self.print_backup['pc'],
					printColumns=self.print_backup['printColumns'],
					force=True
		)
	def aggregateRecord( self, i ):
		for c in self.aggregates.columns:
			if not c in self.asset[i]:
				self.asset[i][c]=''
		for seg in self.aggregates.segments:
			if seg['status']:
				record=self.aggregate_record_process( i, seg['i'] )
	def aggregateTop( self, s ):
		ss=str(s)
		if self.aggregates.index[ss]['rent'] >=0:
			return self.aggregateTop(self.aggregates.index[ss]['rent'])
		else:
			return self.aggregates.index[ss]
	def aggregateItemValue( self, v, f ):
		if not 'params' in v:
			v['params']={}
		if not 'fields' in v:
			v['fields']={}
		if not 'data' in v:
			v['data']=[]
		if 'data' in f:
			v['data'].append( f['data'] )
		if 'fields' in f:
			if not 'fields' in v:
				v['fields']={}
			for k in f['fields']:
				v['fields'][k]=f['fields'][k]
		elif 'params' in f:
			if not 'params' in v:
				v['params']={}
			for k in f['params']:
				v['params'][k]=f['params'][k]
		return v
	def aggregate_record_process_group( self, i, s ):
		ss=str(s)
		seg=self.aggregates.index[ss]
		if 'variable' in seg['l']:
			alpha=seg['l']
			if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				txtParts=seg['txt'].split('?')
				grp=txtParts[0]+'?'
				fld=txtParts[1]
				lbl=txtParts[2]
				if not lbl in self.aggregates.group_storage:
					self.aggregates.group_storage[lbl]=0
				data=self.aggregate_record_process( i, seg['val'] )
				child=self.aggregates.index[ str(seg['val']) ]
				do=None
				if 'function' in child['l']:
					do=child['txt']
					done=False
					if do=='max':
						done=True;
						try:
							if data['data'] > self.aggregates.group_storage[lbl]:
								self.aggregates.group_storage[lbl]=data['data']
						except Exception as e: cp('Error: group max variable', 'red');
					if do=='add':
						done=True;
						try:
							self.aggregates.group_storage[lbl] +=data['data']
						except Exception as e: cp('Error: group add variable', 'red');
				pass
				pass
				if i in self.aggregates.groups[fld]['e']:
					if  __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ]==3:
						self.asset[  self.aggregates.groups[fld]['e'][i]  ][lbl]=addComma( self.aggregates.group_storage[lbl] )
					else:
						if tfc(lbl) in self.backup.NGfields:
							if not str(i) in self.aggregates.agroupsADD:
								self.aggregates.agroupsADD[ str(i) ]={}
							self.aggregates.agroupsADD[ str(i) ][lbl]=self.aggregates.group_storage[lbl]
						else:		   
							self.asset[i][lbl]=addComma( self.aggregates.group_storage[lbl] )
					if not __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ]==2:
						self.aggregates.group_storage[lbl]=0
	def aggregate_record_process( self, i, s ):
		ss=str(s)
		if True:
			seg=self.aggregates.index[ss]
			if 'alpha' in seg['l'] and 'arg' in seg['l'] :
				simple_keys={}
				for key in list(self.asset[i].keys()):
					simple_keys[ tfc(key) ]=key
				if tfc(formatColumns( seg['txt'] )) in simple_keys:
					vXv=simple_keys[tfc(formatColumns( seg['txt'] ))]
					return { 'fields': { vXv: self.asset[i][vXv] }, 'data': self.asset[i][vXv] }
				elif formatColumns( seg['txt'] ) in self.asset[i]:
					return { 'fields': { formatColumns( seg['txt'] ): self.asset[i][formatColumns( seg['txt'] )] }, 'data': self.asset[i][formatColumns( seg['txt'] )] }
				return { 'params': { seg['txt']: 1 } }
			if 'variable' in seg['l']:
				alpha=seg['l']
				isOF=False
				data=self.aggregate_record_process( i, seg['val'] )
				if '?' in seg['txt'] and  seg['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes:
					isOF=True
					if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
						return None
					if seg['txt'].startswith('eot?'):
						if not seg['txt'] in self.aggregates.storage:
							self.aggregates.storage[ seg['txt'] ]={}
						if not alpha in self.aggregates.storage[seg['txt']]:
							self.aggregates.storage[seg['txt']][alpha]={}
							self.aggregates.storage[seg['txt']][alpha]['data']=0
							self.aggregates.storage[seg['txt']][alpha]['settings']={}
					if seg['txt'].startswith('eof?'):
						if not seg['txt'] in __.aggregate.eof.storage:
							__.aggregate.eof.storage[ seg['txt'] ]={}
						if not alpha in __.aggregate.eof.storage[seg['txt']]:
							__.aggregate.eof.storage[seg['txt']][alpha]={}
							__.aggregate.eof.storage[seg['txt']][alpha]['data']=0
							__.aggregate.eof.storage[seg['txt']][alpha]['settings']={}
					child=self.aggregates.index[ str(seg['val']) ]
					do=None
					if 'function' in child['l']:
						do=child['txt']
					if seg['txt'].startswith('eot?'):
						done=False
						if do=='max':
							done=True;
							try:
								if data['data'] > self.aggregates.storage[seg['txt']][alpha]['data']:
									self.aggregates.storage[seg['txt']][alpha]['data']=data['data']
							except Exception as e: cp('Error: max variable', 'red');
						if do=='add':
							done=True;
							try:
								self.aggregates.storage[seg['txt']][alpha]['data'] +=data['data']
							except Exception as e: cp('Error: add variable', 'red');
						if not done:
							self.aggregates.storage[seg['txt']][alpha]['data']=data['data']
					elif seg['txt'].startswith('eof?'):
						done=False
						if do=='max':
							done=True;
							try:
								if data['data'] > __.aggregate.eof.storage[seg['txt']][alpha]['data']:
									__.aggregate.eof.storage[seg['txt']][alpha]['data']=data['data']
							except Exception as e: cp('Error: max variable', 'red');
						if do=='add':
							done=True;
							try:
								__.aggregate.eof.storage[seg['txt']][alpha]['data'] +=data['data']
							except Exception as e: cp('Error: add variable', 'red');
						if not done:
							__.aggregate.eof.storage[seg['txt']][alpha]['data']=data['data']
				else:
					self.asset[i][seg['txt']]=data['data']
					return data
				return { 'data': '' }
			if 'function' in seg['l']:
				if seg['txt']=='trigger':
					pass
				if seg['txt']=='add':
					result=0; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data'])==list:
							for d in v['data']:
								try:
									result +=float( d )
								except Exception as e: pass;
						else:
							try:
								result +=float( v['data'] )
							except Exception as e: pass;
					if str(result).endswith('.0'):
						result=int(result)
					return { 'data': result }
				if seg['txt']=='int':
					result=0; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f );
					if 'data' in v:
						nX=[]
						if type(v['data'])==list:
							for d in v['data']:
								for cn in str(d):
									if cn in '0123456789.':
										nX.append(cn)
						else:
							for cn in str(v['data']):
								if cn in '0123456789.':
									nX.append(cn)
					result=float(''.join(nX))
					if str(result).endswith('.0'):
						result=int(result)
					return { 'data': result }
				if seg['txt']=='len':
					result=0; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data'])==list:
							for d in v['data']:
								result +=len( str( d ) )
						else:
							result +=len( str( v['data'] ) )
					if str(result).endswith('.0'):
						result=int(result)
					return { 'data': result }
				if seg['txt']=='max':
					result=[]; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f ); 
					for d in v['data']:
						if '?date' in v['params']:
							try:
								ad=autoDate( d )
							except Exception as e: ad=0;
							result.append(ad)
						else:
							try:
								ad=float( d )
							except Exception as e: ad=0;
							result.append(ad)
					result.sort()
					result.reverse()
					return { 'data': result[0] }
				if seg['txt']=='config':
					result=[]; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix=''
					for par in result:
						suff="['"+par+"']"
						suffix +=suff
						try:
							eval( '__.aggregate.config'+suffix  )
						except Exception as e:
							exec( '__.aggregate.config'+suffix+'={ }'  )
				pass
				if seg['txt']=='format':
					result=[]; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix=''
					for par in result:
						suff="['"+par+"']"
						suffix +=suff
						try:
							eval( '__.aggregate.format'+suffix  )
						except Exception as e:
							exec( '__.aggregate.format'+suffix+'={ }'  )
				if seg['txt']=='isDate':
					result=None; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data'])==list:
							for d in v['data']:
								try:
									result=autoDate( d )
								except Exception as e: pass;
						else:
							try:
								result=autoDate( v['data'] )
							except Exception as e: pass;
					if not result is None:
						try:
							global _dir
						except Exception as e:
							pass
						if _dir is None:
							import _rightThumb._dir as _dir
						self.asset[i]=isDate( result, self.asset[i] )
						month=_dir.getMonthFromEpoch
					return { 'data': None }
				if seg['txt']=='file':
					result=''; v={};
					for s in seg['args']:
						f=self.aggregate_record_process( i, s ); v=self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data'])==list:
							for d in v['data']:
								try:
									result=d
								except Exception as e: pass;
						else:
							try:
								result=v['data']
							except Exception as e: pass;
					if _dir is None:
						import _rightThumb._dir as _dir
					try:
						info=_dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					except Exception as e:
						info={
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
							self.asset[i][k]=info[k]
					return { 'data': result }
	def aggregateBuild( self ):
		if self.aggregate_processed:
			return None
		self.aggregate_processed=True
		a=' '.join( switches.values('Aggregate') )
		self.aggregates=dot()
		self.aggregates.storage={}
		self.aggregates.group_storage={}
		self.aggregates.segments=__.aggregate.obj.build( self.name, addSwitch=True )
		self.aggregates.index={}
		self.aggregates.groups={}
		self.aggregates.agroups={}
		self.aggregates.agroupsADD={}
		self.aggregates.columns=[]
		for rec in self.aggregates.segments:
			self.aggregates.index[ str(rec['i']) ]=rec
			if rec['status'] and rec['l']=='variable':
				if not '?' in rec['txt'] or( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					self.aggregates.columns.append( rec['txt'] )
					if not rec['txt'] in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ]=rec['txt']
						self.backup.NGfields[ rec['txt'] ]=rec['txt']
		for rec in self.aggregates.segments:
			if rec['status'] and rec['l']=='variable':
				if not '?' in rec['txt'] or( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					pass
				elif '?' in rec['txt'] and rec['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
					self.aggregates.agroups[ rec['i'] ]=rec
					try:
						gc=rec['txt'].split('?')[2]
					except Exception as e:
						cp( 'Error: aggregates, group split', 'red' )
						sys.exit()
					else:
						self.aggregates.columns.append( gc )
					if not gc in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ]=gc
		pass
		for i,record in enumerate(self.asset):
			self.aggregateRecord( i )
		__.aggregate.storage=self.aggregates.storage
		return self.aggregates.columns
	def aggregateRecordGroups( self, i ):
		for seg in self.aggregates.segments:
			if seg['status']:
				try:
					record=self.aggregate_record_process_group( i, seg['i'] )
				except Exception as e:
					cp( 'Error: aggregate, group error', 'red' )
					cp( '\t expected:', 'yellow' )
					cp( '\t\t eog?level?group-len=add(len)', 'green' )
					print()
					cp( [ 'Specifically:', e ], 'red' )
					print()
					sys.exit()
	def aggregateGroup( self ):
		for ix in self.aggregates.agroups:
			seg=self.aggregates.agroups[ix]
			q=seg['txt'].split('?')
			subject=q[1]
			if subject in self.asset[0] and not subject in self.aggregates.groups:
				self.aggregates.groups[subject]={}
				self.aggregates.groups[subject]['b']={}
				self.aggregates.groups[subject]['e']={}
				lastQ=''
				lastID=-1
				for i,record in enumerate(self.asset):
					if subject in record:
						if not record[subject]==lastQ:
							if not lastID==-1:
								self.aggregates.groups[subject]['b'][lastID]=i
								self.aggregates.groups[subject]['e'][i]=lastID
							lastQ=record[subject]
							lastID=i
				self.aggregates.groups[subject]['b'][lastID]=len(self.asset)-1
				self.aggregates.groups[subject]['e'][len(self.asset)-1]=lastID
	def aggregate( self, script ):
		self.hasAggregate=True
		__.aggregate.obj.code( script, label=self.name )
	def aggregateBuildGroup( self ):
		self.aggregateGroup()
		for i,record in enumerate(self.asset):
			self.aggregateRecordGroups( i )
		if self.aggregates.agroupsADD:
			fields.register( self.groupID_KEY, 'val', 7, m=6 )
			test=fields.padZeros( self.groupID_KEY, 'val', 5 )
			newRecords=[]
			for i,record in enumerate(self.asset):
				ii=str(i)
				ix=fields.padZeros( self.groupID_KEY, 'val', i )
				record[ self.groupID_KEY ]=ix + '-A'
				newRecords.append(record)
				if ii in self.aggregates.agroupsADD:
					rec=self.aggregates.agroupsADD[ii]
					rec[ self.groupID_KEY ]=ix + '-B'
					for k in self.backup.allfields:
						if not self.backup.allfields[k] in rec:
							rec[ self.backup.allfields[k] ]=''
					newRecords.append(rec)
			self.asset=newRecords
	def print( self, column, fieldLengths=False, pc=None, printColumns=True, force=False ):
		if not type(self.asset)==list or len(self.asset)==0:
			print('Null Set')
			sys.exit()
		if not force:
			if not switches.isActive('Help'):
				if switches.isActive('Column'):
					column=switches.value('Column')
				if switches.isActive('Sort'):
					self.asset=self.sort()
				elif switches.isActive('GroupBy'):
					switches.fieldSet('Sort','active',True)
					switches.fieldSet('Sort','value',switches.value('GroupBy'))
					self.asset=self.sort()
			pass
			__.aggregate.storage={}
			__.aggregate.config={}
			__.aggregate.format={}
			__.aggregate.prefix=self.tab['table']+loopPrint(__.table_prefix_padding)
			if switches.isActive('Aggregate') or self.hasAggregate:
				aggregate_columns=self.aggregateBuild()
				if  type(aggregate_columns)==list:
					columns=column.split(',')
					for ac in aggregate_columns:
						if not ac in columns:
							columns.append(ac)
					column=','.join(columns)
				__.aggregate.columns=columns
				shouldSortAgain=False
				if switches.isActive('Sort'):
					for sxy in switches.values('Sort'):
						if sxy in aggregate_columns:
							shouldSortAgain=True
					if shouldSortAgain:
						self.asset=self.sort()
				self.aggregateBuildGroup()
				for i,record in enumerate(self.asset):
					for c in record:
						nw=__.aggregate.obj.format( c, record[c] )
						if not nw==record[c]:
							self.asset[i][c]=nw
			pass
			for i,record in enumerate( self.asset ):
				for k in record:
					if record[k] is None:
						self.asset[i][k]=''
		self.isExtraRecord=False
		if force:
			self.isWrap=True
		self.print_backup={
								'column': column,
								'fieldLengths': fieldLengths,
								'pc': pc,
								'printColumns': printColumns,
		}
		self.isExtraRecord_0001={}
		self.isExtraRecord_000x=''
		if not pc is None:
			printColumns=pc
		self.groupByTrigger()
		if type(fieldLengths)==dict:
			self.universalSpacing=fieldLengths
		if not type(self.asset)==list or len(self.asset)==0:
			print('Null Set')
			sys.exit()
		global errors
		global switchDefault
		column=column.lower()
		columnSearch=column
		column=''
		for cs in columnSearch.split(','):
			try:
				column +=self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column +=cs + ','
		column=_str.cleanBE(column,',')
		newData=[]
		oldData=[]
		if ':' in column or '=' in columnSearch:
			oldData=self.asset
		if ':' in column:
			depth=[]
			flat=[]
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found=False
						i=0
						for dp in depth:
							if depth[i]['parent']==c.split(':')[0]:
								found=True
								dpID=i
							i+=1
					except Exception as e:
						found=False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			i=0
			for data in self.asset:
				r={}
				for f in flat:
					r[f]=data[f]
				x=[]
				hasRecords=False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords=True
						for dpi in data[dp['parent']]:
							y={}
							hasData=False
							for dpic in dp['children']:
								try:
									if len(str(dpi[dpic])) > 1:
										hasData=True
								except Exception as e:
									pass
								try:
									y[str(dp['parent']) + ':' + str(dpic)]=dpi[dpic]
								except Exception as e:
									pass
							for f in flat:
								y[f]=r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)]=''
					newData.append(r)
				i+=1
			self.asset=newData
		newData=[]
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude=True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc=c.split('=')
							string=data[cc[0]]
							string=_str.cleanBE(string.lower(),' ')
							cc[1]=_str.cleanBE(cc[1],' ')
							try:
								dataYes=_str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes=''
							try:
								dataNo=_str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo=''
							if len(dataYes) > 0:
								length=0
								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude=False
										if len(s) > 0:
											length +=1
											s=s.lower()
											cnt=0
											if len(s) > 1 and s[0]=='*':
												s=s.replace('*','')
												if string.endswith(s):
													cnt +=1
													rowInclude=True
											elif len(s) > 1 and s[-1]=='*':
												s=s.replace('*','')
												if string.startswith(s):
													cnt +=1
													rowInclude=True
											elif s in string:
												cnt +=1
												rowInclude=True
							if len(dataNo) > 0 and rowInclude:
								rowInclude=True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s=s.lower()
											cnt=0
											if len(s) > 1 and s[0]=='*':
												s=s.replace('*','')
												if string.endswith(s):
													cnt +=1
											elif len(s) > 1 and s[-1]=='*':
												s=s.replace('*','')
												if string.startswith(s):
													cnt +=1
											elif not string.find(ci(s))==-1:
												cnt +=1
											if cnt > 0:
												rowInclude=False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset=newData
		columnHeader=self.showColumnHeader(column)
		columnHeaderLength=len(columnHeader)
		self.groupByList={}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)]=''
		except Exception as e:
			pass
		if not force and not switches.isActive('NoWrapTable'):
			if __.terminal.width:
				maxSize=0
				i=0
				for item in self.asset:
					result=''
					for c in column.split(','):
						try:
							result +=self.showColumn(c,i,columnHeaderLength) + self.columnTab
						except Exception as e:
							pass
					maxSize=len(result)+self.prefixSize()
					i+=1
				if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
					self.wrapTable(__.terminal.width)
					return None
		pass
		self.groupByList={}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)]=''
		except Exception as e:
			pass
		if printColumns:
			columnHeader=self.tab['table']+loopPrint(__.table_prefix_padding) + columnHeader.replace( '\n', '' )
			print()
			printBold( columnHeader )
			print()
		i=0
		self.isExtraRecord_0001={}
		self.isExtraRecord_000x=''
		for item in self.asset:
			result=''
			for c in column.split(','):
				try:
					pass
				except Exception as e:
					pass
				self.isExtraRecord=False
				if self.wrapTableKey+'-sort' in item:
					self.isExtraRecord_000x=item[self.wrapTableKey+'-sort']
				if self.wrapTableKey+'-sort' in item and not item[self.wrapTableKey+'-sort'].endswith('-0001'):
					self.isExtraRecord=True
				try:
					pass
					result +=self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result +=showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					print(12)
					print(c)
					print(12)
					os._exit(0)
			maxSize=len(result)+self.prefixSize()
			if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
				ToDo=" result=''   "
				ToDo=' for sult in self.wrapTable2(i):  '
				ToDo='	 result +=sult  '
			else:
				ToDo=' the below if will be under this else '
			if len(result) > 0:
				shouldPrint=True
				if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
					testResult=result
					testResult=testResult.replace( ' ', '' ).replace( '\t', '' )
					if not len(testResult):
						shouldPrint=False
				if shouldPrint:
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						colorizeRow( result, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
			i +=1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault==i:
				if '??' in __.switch_skimmer.active:
					sys.exit()
				pass
				print('')
		self.asset=self.backup.asset.copy()
		self.aggregate_processed=False
		footer={}
		aSettings={}
		for k in __.aggregate.storage:
			if k.startswith('eot?'):
				f=k[len('eot?'):]
				for y in __.aggregate.storage[k]:
					for sv in __.aggregate.storage[k][y]['settings']:
						aSettings[sv]=__.aggregate.storage[k][y]['settings'][sv]
					if '?date' in __.aggregate.storage[k][y]['settings']:
						__.aggregate.storage[k][y]['data']=friendlyDate( __.aggregate.storage[k][y]['data'] )
					theKey=f 
					special={}
					kk=k
					var='var'
					if 'var' in __.aggregate.config:
						var='var'
					if '?var' in __.aggregate.config:
						var='?var'
					if 'var?' in __.aggregate.config:
						var='var?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='eot?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					if '?fl' in special:
						theKey=f + ' '+ y
					if '?first' in special:
						theKey=f
					elif '?second' in special:
						theKey=y
					footer[ theKey ]=__.aggregate.obj.format( [k,y], __.aggregate.storage[k][y]['data'] )
		if footer:
			print()
			footer_txt=[]
			footer_txt.append( __.aggregate.prefix )
			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			print()
	def sort(self,fields=''):
		rows=self.asset
		if not len(self.asset):
			return None
		if self.wrapTableKey+'-sort' in self.asset[0]:
			return rows
		global errors
		global switches
		tempFields=[]
		delim=':'
		if fields=='':
			name=switches.value('Sort')
		else:
			name=fields
		name=name.replace(':',delim)
		sortBy={}
		sortList=name.split(',')
		sortList.reverse()
		for item in sortList:
			item=item
			try:
				if item.count(delim) > 0:
					sb=item.split(delim)[1]
				else:
					sb=item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
		itemgetter=__.imp('operator.itemgetter')
		for item in sortList:
			try:
				direction=item.split(delim)[0]
				sb=self.findColumName(item.split(delim)[1])
				if 'a' in direction:
					self.asset=sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset=sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset=sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows=sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			uuid=__.imp('uuid')
			sortBy[item]=str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i=0
			for row in self.asset:
				self.asset[i][sortBy[item]]=i
				i +=1
		sortCode='rows=sorted(rows, key=lambda d:('
		for item in sortList:
			sortCode +="d['" + str(sortBy[item]) + "'],"
		sortCode=sortCode[:-1]
		sortCode +='))'
		exec(sortCode)
		if len( tempFields ):
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset
	def countThis(self):
		rows=self.asset
		i=0
		for x in self.asset:
			i +=1
		return i
	def file(self,file):
		self.file=file
	def save(self,theFile='',tableTemp=True,printThis=True):
		HD.chmod(theFile)
		simplejson=__.imp('simplejson')
		if theFile=='':
			theFile=str(self.file)
		self.file=theFile
		if tableTemp==True:
			file0=str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0=_v.stmp + _v.slash + theFile
		dataDump=simplejson.dumps(self.asset, indent=4, sort_keys=True)
		f=open(file0,'w')
		f.write(str(dataDump))
		f.close()
		HD.chmod(theFile)
		if printThis:
			print('Saved: ' + file0)
	def get(self,theFile='',tableTemp=True,printThis=False):
		simplejson=__.imp('simplejson')
		if theFile=='':
			theFile=self.file
		self.file=theFile
		if tableTemp==True:
			file0=_v.myTables + _v.slash + theFile
		else:
			file0=_v.stmp + _v.slash + theFile
		if printThis:
			print('Loaded: ' + file0)
		if os.path.isfile(file0)==True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data=simplejson.load(json_file)
		else:
			json_data=[]
		self.asset=json_data
		return json_data
	def assets(self):
		return self.asset
	def set(self,asset):
		self.asset=asset
		return self.asset
	def groupByTrigger( self ):
		try:
			if switches.isActive('GroupBy') and len(self.asset):
				newValues=[]
				keys=[]
				for key in self.asset[0].keys():
					keys.append( key )
				for val in switches.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower()==val.lower():
							newValues.append( key )
				if len(newValues):
					switches.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass
class Tables:
	def __init__(self):
		self.tables=[]
		self.index={}
		self.maxNameLength=35
		self.columnTab='\t'
		self.groupSeparator='_'
		self.group_space=False
	def aggregate( self, name=None, code=None ):
		if code is None:
			return None
		if name is None:
			name=self.tables[ len(self.tables)-1 ].name
		self.tables[ self.index[name] ].aggregate( code )
	def rprint( self, asset, columns, name=None, n=None, sc=True ):
		if not n is None:
			name=n
		if name is None:
			name=genUUID()
		self.register( name, asset )
		if sc and switches.isActive('Column'):
			columns=switches.value('Column')
		self.print( name, columns )
	def rsort( self, asset, columns, name=None, n=None ):
		if not n is None:
			name=n
		if name is None:
			name=genUUID()
		self.register( name, asset )
		return self.returnSorted( name,columns,asset )
	def register( self, name=None, asset=[], group_space=True, tab='',	gs=None, t=None, n=None ):
		global TableProfile_Config
		if not n is None:
			name=n
		if name is None:
			name=genUUID()
		if not __.table_b_print:
			for i,record in enumerate(asset):
				for field in record.keys():
					if str( record[field] )=='b':
						asset[i][field]=''
		found=False
		thisID=False
		if not gs is None:
			group_space=gs
		elif 'ALLTABLES' in TableProfile_Config.keys() and 'GroupSpaces' in TableProfile_Config['ALLTABLES'].keys():
			group_space=TableProfile_Config['ALLTABLES']['GroupSpaces']
		else:
			group_space=switches.isActive('GroupSpaces')
		if not t is None:
			tab=t
		for i,t in enumerate(self.tables):
			if t.name==name:
				thisID=i
				found=True
				self.tables[i].maxNameLength=self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if found:
			self.tables.pop( thisID )
			found=False
		if not found:
			self.tables.append(Table( name, asset, group_space, tab ))
			self.tables[ len( self.tables )-1 ].maxNameLength=self.maxNameLength
			self.index[name]=len( self.tables )-1
		return name
	def trigger(self,name,field,script,includes=False):
		i=0
		for t in self.tables:
			if t.name==name:
				self.tables[i].trigger(field,script,includes)
			i +=1
	def registerView(self,table,name,fields,sort):
		i=0
		for t in self.tables:
			if t.name==table:
				self.tables[i].registerView(name,fields,sort)
			i +=1
	def fieldProfileSet(self,table,field,propertyName,value):
		i=0
		found=False
		for t in self.tables:
			if t.name==table:
				found=True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i +=1
		if not found:
			self.tables.append(Table(table,[]))
			i=0
			for t in self.tables:
				if t.name==table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i +=1
	def print(self,name,fields,fieldLengths=False, pc=None, printColumns=True ):
		global switches
		if not ',' in fields:
			pc=False
		xXx=switches.records('dic_on-off-v')
		if 'Sort' in xXx['on']:
			sortBy=xXx['values']['Sort']
			self.sort( name, ','.join( sortBy ) )
		if not pc is None:
			printColumns=pc
		sI=None
		i=0
		for t in self.tables:
			if t.name==name:
				if len(self.tables[i].asset) > 0:
					if not ',' in fields:
						printColumns=False
					self.tables[i].print(fields,fieldLengths,printColumns=printColumns)
					sI=i
				else:
					print('Null Set')
			i +=1
		if switches.isActive('FieldTotal'):
			fieldTotals={}
			for field in switches.values('FieldTotal'):
				fieldTotals[field]={ 'actual': None, 'total': 0 }
				for rec in self.tables[sI].asset:
					for key in rec.keys():
						if check_field_match( key, field ):
							fieldTotals[field]['actual']=key
							thisFieldA=str(rec[key])
							thisFieldB=[]
							for char in thisFieldA:
								if char in '0123456789':
									thisFieldB.append(char)
							thisFieldC=int(''.join(thisFieldB))
							fieldTotals[field]['total'] +=thisFieldC
			print()
			print()
			for field in fieldTotals:
				print( addComma(fieldTotals[field]['total']),'\t', fieldTotals[field]['actual'] )
	def sort(self,name,fields):
		fields=fields.replace('.',':')
		i=0
		for t in self.tables:
			if t.name==name:
				self.tables[i].sort(fields)
			i +=1
	def returnSorted(self,name,fields,asset=[]):
		fields=fields.replace('.',':')
		if len(asset) > 0:
			self.register(name,asset)
		result=[]
		i=0
		for t in self.tables:
			if t.name==name:
				self.tables[i].sort(fields)
				result=self.tables[i].asset
			i +=1
		return result
	def view(self,table,name):
		i=0
		for t in self.tables:
			if t.name==table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i +=1
	def save(self,table,theFile='',tableTemp=True,printThis=True):
		HD.chmod(theFile)
		theFile=str(theFile)
		if not theFile=='' and not '.json' in theFile:
			theFile=theFile + '.json'
		i=0
		for t in self.tables:
			if t.name==table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i +=1
		HD.chmod(theFile)
	def get(self,table,theFile='',tableTemp=True,printThis=False):
		theFile=str(theFile)
		if not theFile=='' and not '.json' in theFile:
			theFile=theFile + '.json'
		i=0
		for t in self.tables:
			if t.name==table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i +=1
	def asset(self,table):
		i=0
		for t in self.tables:
			if t.name==table:
				return self.tables[i].assets()
			i +=1
	def file(self,table,theFile):
		i=0
		for t in self.tables:
			if t.name==table:
				return self.tables[i].file(theFile)
			i +=1
	def set(self,table,asset):
		i=0
		for t in self.tables:
			if t.name==table:
				return self.tables[i].set(asset)
			i +=1
	def alignmentMasterSupersedes(self,table,value):
		i=0
		for t in self.tables:
			if t.name==table:
				self.tables[i].tableProfileDefaultSupersedes=value
			i +=1
	def getLength(self,name,fields):
		i=0
		for t in self.tables:
			if t.name==name:
				self.tables[i].showColumnHeader(fields)
				result=self.tables[i].spaces
			i +=1
		total=0
		for r in result.keys():
			total +=result[r]
			total +=5
		return total
	def getFieldLengths(self,name,fields):
		i=0
		for t in self.tables:
			if t.name==name:
				self.tables[i].showColumnHeader(fields)
				result=self.tables[i].spaces
			i +=1
		return result
	def eof( self ):
		try:
			__.aggregate.eof.storage
		except Exception as e:
			shouldPrint=False
		else:
			shouldPrint=True
		if not __.aggregate.eof.storage:
			shouldPrint=False
		if shouldPrint:
			print()
			print()
			linePrint()
		footer={}
		aSettings={}
		for k in __.aggregate.eof.storage:
			if k.startswith('eof?'):
				f=k[len('eof?'):]
				for y in __.aggregate.eof.storage[k]:
					for sv in __.aggregate.eof.storage[k][y]['settings']:
						aSettings[sv]=__.aggregate.eof.storage[k][y]['settings'][sv]
					if '?date' in __.aggregate.eof.storage[k][y]['settings']:
						__.aggregate.eof.storage[k][y]['data']=friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					theKey=f +' '+ y
					special={}
					kk=k
					var='var'
					if 'var' in __.aggregate.config:
						var='var'
					if '?var' in __.aggregate.config:
						var='?var'
					if 'var?' in __.aggregate.config:
						var='var?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					kk='eof?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK]=__.aggregate.config[var][kk][spK]
					if '?first' in special:
						theKey=f
					elif '?second' in special:
						theKey=y
					footer[ theKey ]=__.aggregate.obj.format( [k,y], __.aggregate.eof.storage[k][y]['data'] )
		if footer:
			print()
			footer_txt=[]
			footer_txt.append( __.aggregate.prefix )
			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( '  ' )
			cp( footer_txt, 'cyan' ) 
			print()
