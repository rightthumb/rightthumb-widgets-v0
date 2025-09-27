
class Switch:

	def __init__(self, name, switch, example_or_notes, description, space, default, group):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.default = default
		self.group = group
		self.pos = 0
		self.active = False
		self.value = None
		self.values = []
		self.example_or_notes = example_or_notes
		self.documentation = { 'description': description, 'examples': [], 'required': [], 'related': [] }
		self.space = space
		self.vs = False
		self.script_trigger_alt = None
		self.script=blank_script_trigger

	def trigger(self,script,vs=False,alt=None):
		if not alt is None:
			self.script_trigger_alt = alt
			vs = True
		self.vs = vs
		self.script_trigger = script
		self.script = script



class Switches:

	def __init__(self):
		self.switches = []
		self.index = {}
		self.appRegDefault = None
		self.appReg = __.appReg
		self.hasRequired = []
		self.isRequired = {}
		self.postScripts = []
		self.dex = {}


	def all( self, app=True, appReg=None, omit=None, omitDefaults=True,             od=1 ):
		if not od:
			omitDefaults = False
		if omitDefaults:
			omitList = [ 'Help', 'Column', 'Sort', 'Debug', 'Errors', 'Timeout', 'GroupBy', 'ShortenColumn', 'Long', 'Length', 'Report', 'Plus', 'Minus', 'PlusOr', 'PlusClose', 'PrintAutoAbbreviations', 'LoadEpoch', 'NoColor', 'Clean', 'NoCount', 'Count' ]
		else:
			omitList = []

		if not  omit is None:
			if type(omit) == str:
				omit = omit.replace(  ' ', '' )
				omit = omit.split(',')
			for x in omit:
				omitList.append( x )


		# appReg values expected: None, 1, true, 'all'
		if appReg is None:
			appReg = __.appReg

		result = []
		for i,row in enumerate(self.switches):
			# pv(row)
			if not row.name in omitList:
				if row.active:
					shouldAdd = True
					if app:
						if type( appReg ) == str:
							if not appReg == 'all':
								if not row.appReg == appReg:
									shouldAdd = False

					if shouldAdd:
						if not row.values:
							for ii,rec in enumerate(self.switches):
								if not i == ii and rec.name == row.name and rec.values: shouldAdd = False
					if shouldAdd:
						result.append({
											'active': row.active,
											'name': row.name,
											'value': row.value,
											'values': row.values,
											'appReg': row.appReg,
						})
		# _result=[]
		# _spent=[]
		# for i, rec in result:
		#   cnt=0
		#   for i, rec in result:



		return result




	def records( self, formating=None, appReg=None ):
	# def records( self, formating=None, appReg=None, empty=True, v=None ):
		# if not v is None and v: empty=False
		# elif not v is None and v: empty=True
		if formating is None:
			colorThis( 'formating options:', 'bold' )
			colorThis( [ '\t', 'list' ], 'yellow' )
			colorThis( [ '\t', 'dic_a-v', '\t', "{ 'isActive': {}, 'values': {} }" ], 'yellow' )
			colorThis( [ '\t', 'dic_on-off-v', '\t', "{ 'on': [], 'off': [], 'values': {} }" ], 'yellow' )
			colorThis( [ '\t', 'dump' ], 'yellow' )
			colorThis( [ '\t', 'relevant' ], 'yellow' )
			colorThis( [ '\t', 'dump2' ], 'yellow' )
			sys.exit()

			colorThis(  )
		if appReg is None:
			appReg = __.appReg


		records = {
						'list': [],
						'dic_a-v': { 'active': self.active(), 'isActive': {}, 'values': {} },
						'dic_on-off-v': { 'on': [], 'off': [], 'values': {} },
						'dump': [],
						'dump2': {},
		}


		for i,switch in enumerate(self.switches):

			#b)--> dump2
			if not switch.appReg in records['dump2']: records['dump2'][switch.appReg]={}
			if not 'on' in records['dump2'][switch.appReg]:
				records['dump2'][switch.appReg]['on']={}
				records['dump2'][switch.appReg]['off']={}

			if switch.active:
				if switch.name in records['dump2'][switch.appReg]['on'] and switch.values:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
				else:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
			else: records['dump2'][switch.appReg]['off'][switch.name] = switch.values
			#e)--> dump2



			#b)--> duplicate fix
			##### #timestamp)--> 2022-07-26T17:09:11-0400
			shouldAdd = True
			for ii,rec in enumerate(self.switches):
				if not i == ii and rec.name == switch.name and rec.values: shouldAdd = False
			if shouldAdd:
			#e)--> duplicate fix

				if self.switches[i].appReg == appReg:
					records['list'].append({ 'name': switch.name, 'values': switch.values })


					records['dic_a-v']['isActive'][switch.name] = switch.active
					records['dic_a-v']['values'][switch.name] = switch.values


					records['dump'] = dict((name, getattr(switch, name)) for name in dir(switch) if not name.startswith('__'))
					records['dic_on-off-v']['values'][switch.name] = switch.values


					if switch.active:
						records['dic_on-off-v']['on'].append( switch.name )
					else:
						records['dic_on-off-v']['off'].append( switch.name )

		#b)--> relevant
		records['relevant']={}
		for on in records['dic_on-off-v']['on']:
			records['relevant'][on] = records['dic_on-off-v']['values'][on]
		if formating.startswith('r'): formating = 'relevant'
		#e)--> relevant
		return records[ formating ]
	def documentation( self, name, data ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if row.name == name:
					# print_( 'SET' )
					if self.switches[i].appReg == __.appReg:

						try:
							if len( data['description'] ):
								self.switches[i].documentation['description'] = data['description']
						except Exception as e:
							pass

						try:
							if len( data['examples'] ):
								self.switches[i].documentation['examples'] = data['examples']
						except Exception as e:
							pass

						try:
							if len( data['required'] ):
								self.switches[i].documentation['required'] = []
								self.switches[i].documentation['related'] = []
								for record in data['required']:
									if record == 'Pipe':
										__.isRequired_Pipe = True
									else:
										self.switches[i].documentation['required'].append( record )
										self.switches[i].documentation['related'].append( record )
										if not name in self.hasRequired:
											self.hasRequired.append( name )


						except Exception as e:
							pass

						try:
							if len( data['related'] ):
								for record in data['related']:
									self.switches[i].documentation['related'].append( record )
						except Exception as e:
							pass

						try:
							if type( data['isRequired'] ) == bool:
								if data['isRequired']:
									if not name in self.isRequired[__.appReg]:
										self.isRequired[__.appReg].append( name )
						except Exception as e:
							pass



		except Exception as e:
			result = False
		return result


	def record( self, name ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						return i
		except Exception as e:
			result = False
		return result

	def dumpSwitches(self,includeBlank=False):
		self.fieldSet('Long','active',True)
		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if includeBlank:
				data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			else:
				if not row.value is None or row.active:
					data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			# print_(row.name,'\t',row.value,'\t',row.appReg)
		tables.register('data',data)
		tables.print('data','appreg,name,value')

	def register(self, name, switch, example_or_notes = None, isRequired=False, isPipe=None, isData=None, description='', space=False, default=False, group=None, g=None):
		if not g is None:
			group = g

		if not isPipe is None:
			__.trigger_isPipe = isPipe

		if not isData is None:
			__.trigger_isPipe = isData
			isPipe=isData
		i=len(self.switches)

		if not __.appReg in self.dex:
			self.dex[__.appReg]={}
		self.dex[__.appReg][name]=i

		self.switches.append(Switch(name, switch, example_or_notes, description, space, default, group))

		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []



		switch = switch.replace( ' ', '' )


		if not isPipe is None:
			__.isData_Switches[name]=isPipe
			if type(isPipe) == bool and isPipe:
				isPipe = 'data'
			vv.isData[name]=isPipe
			isPipe=isPipe.replace('raw','name')
			if 'name' in isPipe and ( 'data' in isPipe or 'clean' in isPipe ):
				pass
			elif 'name' in isPipe:
				__.trigger_isPipe = 'name'
			elif 'data' in isPipe or 'clean' in isPipe:
				if 'clean' in isPipe:
					__.trigger_isPipe = 'data,clean'
				else:
					__.trigger_isPipe = 'data'
		elif isPipe:
			__.trigger_isPipe = 'data'

		if isRequired:
			__.isRequired_index[__.appReg].append( name )
			if not name in self.isRequired[__.appReg]:
				self.isRequired[__.appReg].append( name )



	def fieldSet2( self, name, column, value, theFocus=False, runTrigger=True ):
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value
					elif column == 'values':
						self.switches[i].values = values
						self.switches[i].value = ','.join(valuesV)
	def fieldSet( self, name, column, value, theFocus=False, runTrigger=True ):
		if name == 'Sort':
			if column == 'value':
				if type(value) == str:
					if value.startswith('a.'):
						value = 'a:' + value[2:]
					if ',a.' in value:
						value = value.replace( ',a.', ',a:' )

					if value.startswith('d.'):
						value = 'd:' + value[2:]
					if ',d.' in value:
						value = value.replace( ',d.', ',d:' )
			if column == 'values':
				if type(value) == list:
					for i,asdf in enumerate(value):
						if value[i].startswith('a.'):
							value[i] = 'a:' + value[i][2:]
						if value[i].startswith('d.'):
							value[i] = 'd:' + value[i][2:]


		if type( theFocus ) == bool:
			theFocus = __.appReg

		if column == 'values':
			if type(value) == str:
				value = [value]
			values = []
			valuesV = []
			if not runTrigger:
				for x in value:
					values.append( x )
			elif runTrigger:
				if self.fieldExists( name, 'script_trigger', theFocus ):
					for x in value:
						values.append( self.scriptTrigger( name, x, theFocus  ) )

				elif self.fieldExists( name, 'script_trigger', theFocus ) == True:
					for x in value:
						script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,x)# script_trigger_external
						values.append( eval(script) )
				else:
					for x in value:
						values.append( x )
			for x in values:
				if type(x) == str:
					valuesV.append( x.replace(',',';;') )
		if column == 'value':
			if runTrigger:
				if self.fieldExists( name, 'script_trigger', theFocus ):
					value = self.scriptTrigger( name, value, theFocus  )
					# self.fieldGet(name,'script_trigger')(value)
				elif self.fieldExists( name, 'script_trigger', theFocus ) == True:
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)# script_trigger_external
					value = eval(script)
		# print_( name, column, value )
		# sys.exit()
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value
					elif column == 'values':
						self.switches[i].values = values
						self.switches[i].value = ','.join(valuesV)

					else:
						# self.switches[i][column] = value
						exec('self.switches[i].' + column + '= value')
						# value = str(value)
						# try:
						#   exec('self.switches[i].' + column + '=str(\'' + value + '\')')
						# except Exception as e:
						#   exec('self.switches[i].' + column + '=\'' + value + '\'')

		return ''



	def fieldExists( self, name, column, theFocus=False ):# doesFieldExist
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger( self, name, value, theFocus=False, cc=False ):# externalScriptTrigger
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					if not cc:
						value = self.switches[i].script_trigger(value)# script_trigger_external
					elif cc:
						if not self.switches[i].vs:
							value = self.switches[i].script_trigger(value)# script_trigger_external
						elif not self.switches[i].script_trigger_alt is None:
							value = self.switches[i].script_trigger_alt(value)# script_trigger_external



		return value

	def fieldGet2(self,name,column):# getSwitchField
		# print_(name,column)
		result = ''
		for i,row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result

	def fieldGet( self, name, column, theFocus=False ):# getSwitchField
		# print_(name,column)
		result = ''
		if not column == 'pos':

			if name == 'NoColor' and column == 'active':

				found = False

				for i,row in enumerate(self.switches):
					if row.name == name:
						# print_( row.name, row.active )
						if row.active:
							found = True

				result = found

				# print_( 'here', name, found )
				# sys.exit()


			else:


				i = self.searchIndex( name, theFocus )
				if i is None:

					if column == 'active':
						return False

					if column == 'value':
						return ''

					if column == 'values':
						return []

					printBold( 'Error: Nonexistent Switch', 'red' )
					print_( name, column, theFocus )
					printVar( self.index )
					sys.exit()
				row = self.switches[i]
				result = eval('row.' + column)

		else:
			if type( theFocus ) == bool:
				theFocus = __.appReg
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == theFocus:
					if row.name == name:
						result = eval('row.' + column)
		return result

	def isActive2( self, name, theFocus=False ):
		for i,row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active: return True
		return False


	def isActive( self, name, theFocus=False ):# isSwitchActive
		if not theFocus: theFocus = __.appReg
		if theFocus in self.dex and name in self.dex[theFocus]:
			# print('from index')
			return self.switches[self.dex[theFocus][name]].active
		return self.fieldGet( name, 'active', theFocus )

	def getField( self, name, field, theFocus=False ):
		return self.fieldGet( name, field, theFocus )

	def value( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'value', theFocus )
		if result is None:
			result = ''
		return result

	def values2( self, name, theFocus=False ):# getSwitchValue
		for i,row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet( name, 'values', theFocus )
		return []

	def value2( self, name, theFocus=False ):# getSwitchValue
		for i,row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet( name, 'value', theFocus )
		return ''

	def isActive2( self, name, theFocus=False ):
			for i,row in enumerate(self.switches):
				if self.switches[i].name == name and self.switches[i].active: return True
			return False

	def values( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'values', theFocus )
		if result is None:
			result = []
		return result

	def trigger( self, name, script, vs=False, alt=None ):
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script,vs,alt)

	def simpleTrigger( self, name, value ):
		return self.switches[self.dex[__.appReg][name]].script(value)


	def value2(self,name):
		# return ','.join( self.value3(name) )
		# return ','.join(  self.value3(name)  )


		switchInput = sys.argv
		for i,a in enumerate(switchInput): switchInput[i]=a.replace('↔',' ')
		# print(switchInput)
		# sys.exit()

		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:
						if not name in __.switch_raw:
							if switchInput[i] == ':': switchInput[i] = switchInput[i].replace(':','_;192B;_')
							if switchInput[i] == ',':
								switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			if not name in __.switch_raw:
				result = _str.cleanAll(result,'"','')
				result = _str.cleanAll(result,':,',':')
				result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = ''
		if not name in __.switch_raw:
			return result
			# return _str.cleanBE( result, ' ' )
		else:
			return result

	def value3(self,name):
		switchInput = sys.argv
		for i,a in enumerate(switchInput): switchInput[i]=a.replace('↔',' ')
		data = []
		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			for i,a in enumerate(switchInput):
				# a=self.simpleTrigger(name,a)
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:
						if not a == ' ':
							if not name in __.switch_raw:
								data.append(a)
								# data.append( _str.cleanBE( a, ' ' ) )
							else:
								data.append( a )
						else:
							data.append( a )


		except Exception as e:
			data = []
		return data

	def isSwitch(self,string):# checkIfSwitch
		result = False
		for i,a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
					# print_(b,result)
		return result

	def format(self,name):# processSwitchFormatting
		value = self.value2(name)
		if self.fieldExists(name,'script_trigger'):
			value = self.scriptTrigger(name,value,cc=True)
		elif self.fieldExists(name,'script_trigger'):
			script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def format2( self, name ):
		values = self.value3(name)
		# if name =='Plus':
		#     print_(values)
		if values is None:
			values = []
		else:
			for i,value in enumerate(values):
				if self.fieldExists(name,'script_trigger'):
					values[i] = self.scriptTrigger(name,value)
				elif self.fieldExists(name,'script_trigger'):
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
					values[i] = eval(script)
		return values

	def exists(self,name):# checkSwitchExist
		result = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result
	def help(self,justAppNotFullHelp=False):
		
		# Help Menu Color Scheme
		## Unused colors commented for navigation
		helpColorScheme.labels = 'ColorBold.white'
		helpColorScheme.tableSwitchGroupsLine = 'blue'
		helpColorScheme.tableSwitchGroupsPostLabel = 'yellow'
		helpColorScheme.file = 'Background.light_blue'
		helpColorScheme.description = 'Background.green'
		helpColorScheme.tags = 'green'
		helpColorScheme.prerequisite = 'ColorBold.blue'
		helpColorScheme.relatedapps = 'ColorBold.blue'
		helpColorScheme.examples = 'purple' # handled differently
		helpColorScheme.ask_example_id = 'yellow'
		helpColorScheme.abbreviations = 'purple' # is colorizeRow
		helpColorScheme.line = 'yellow'
		helpColorScheme.requiredLabel = 'red'
		helpColorScheme.required = 'Background.red'
		helpColorScheme.switchRequredLabel = 'ColorBold.white'
		helpColorScheme.switchRequred = 'yellow'
		helpColorScheme.noRequirements = 'green' # cyan
		helpColorScheme.notes = 'purple' # handled differently
		self.justAppNotFullHelp = justAppNotFullHelp
		if self.value('Help') == 'x' or self.value('Help') == 'cls' or self.value('Help') == 'clear' or 'fn' in self.value('Help'):


			if 'fn' in self.values('Help'):
				info = self.values('Help')
				info.pop(0)
				if not info:
					pr('Usage:',c='yellow')
					for li in ['']: pr('\t- '+li,c='cyan')
					sys.exit()

				import inspect
				fn = info[0]
				info.pop(0)
				pr('Function:',fn,c='yellow')
				if not info or (info[0] == 'arg' or info[0] == 'args'):
					argspec = list(inspect.getfullargspec(eval(fn)))
					pr('\t',argspec[0])
					# for spec in argspec: pr('\t-',spec )

				sys.exit()


			if __.isWin:
				os.system('cls')
			else:
				os.system('clear')
		# print_(__.registeredApps)
		# print_(__.appReg)
		# sys.exit()
		if len(__.registeredApps) > 1:
			# print_(__.appReg)
			if __.appReg == '__init__' or __.appReg == 'cryptFile':
				return None
		if __.appInfoScan:
			return None
		# self.help()
		global appInfo
		global fields
		self.fieldSet('Long','active',True)
		if __.cls_process_switches_help or 'cls' in self.value('Help'):
			os.system('cls')
		# os.system('cls')
		print_()
		print_()

		filename = colorThis(  [ 'Program:  \t' ], helpColorScheme.labels, p=0  )
		try:
			if not appInfo[__.appReg]['file'] == 'thisApp.py' and appInfo[__.appReg]['liveAppName'] == '__init__':
				filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
				sys.exit()
			else:
				try:
					if not appInfo[__.appReg]['file'] == 'thisApp.py' and not appInfo[__.appReg]['liveAppName'] == '__init__':
						filename += colorThis(  [ appInfo[__.appReg]['liveAppName'] ], helpColorScheme.file, p=0  )
					else:
						filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
				except Exception as e:
					filename += colorThis(  [ appInfo[__.appReg]['file'].replace('.py','') ], helpColorScheme.file, p=0  )
		except: pass

		print_()
		print_( filename )
		print_()

		try:
			if type( appInfo[__.appReg]['description'] ) == list:
				print_( pr('Description:   ',c=helpColorScheme.labels,p=0))
				for x in appInfo[__.appReg]['description']:
					print_( '                 - ', pr(x,c=helpColorScheme.description,p=0) )
				print_()
			else:
				print_( inlineBold('Description:   '), pr(appInfo[__.appReg]['description'],c=helpColorScheme.description,p=0) + '\n')
			configured = True
		except Exception as e:
			configured = False

		try:
			# print_( inlineBold('Categories:    '), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			print_( inlineBold('Tags:          '), '(',    pr(', '.join( appInfo[__.appReg]['categories'] ),c=helpColorScheme.tags,p=0)   , ')' + '\n')
			# print_( inlineBold('Tags:          '), '(',    ', '.join( appInfo[__.appReg]['categories'] )   , ')' + '\n')
			# print_( inlineBold('          Tags:'), ', '.join( appInfo[__.appReg]['categories'] ) + '\n')
			pass
		except Exception as e:
			pass

		try:
			if len(appInfo[__.appReg]['prerequisite']) > 0:
				pr('Prerequisite:',c=helpColorScheme.labels)
				for docItem in appInfo[__.appReg]['prerequisite']:
					if type(docItem) == list:
						# colorThis( '\t\t'+docItem[0], docItem[1]  )
						pr('\t\t'+docItem[0],c=helpColorScheme.prerequisite)
					else:
						pr('\t\t'+docItem,c=helpColorScheme.prerequisite)
						# colorizeRow( '\t\t'+ docItem , 2)
					# colorizeRow('\t' + prereq,2)
				print_('\n')
		except Exception as e:
			pass
		try:
			if len(appInfo[__.appReg]['relatedapps']) > 0:
				# printBold('Related Apps:')
				pr('Related Apps:',c=helpColorScheme.labels)
				
				for docItem in appInfo[__.appReg]['relatedapps']:
					if type(docItem) == list:
						pr('\t\t'+docItem[0],c=helpColorScheme.relatedapps)
					else:
						pr('\t\t'+docItem,c=helpColorScheme.relatedapps)
				print_('\n')
		except Exception as e:
			pass
		if configured:
			quit_early = False
			if len(appInfo[__.appReg]['examples']) > 0:
				# printBold('Examples:')
				pr('Examples:',c=helpColorScheme.labels)
				IDs = {}
				ei = 1
				for docItem in appInfo[__.appReg]['examples']:
					if not docItem is None:
						prei = str(ei)
						if len(self.value('Help')) and self.value('Help') == prei:
							prei = '*'
						elif not 'id' in self.value('Help') and not 'c' in self.value('Help') and not 'i' in self.value('Help') :
							prei = ''
						else:
							quit_early = True
						if type(docItem) == list:
							if not len(docItem[0]):
								prei = ''
							else:
								ei+=1
							if prei == '*':
								setClip(docItem[0])
								quit_early= True
							if len(prei):
								IDs[prei] = docItem[0]
							# colorThis( '\t'+prei+'\t'+docItem[0], docItem[1]  )
							pr('\t'+prei+'\t'+docItem[0],c=helpColorScheme.examples)
						else:
							if not len(docItem):
								prei = ''
							else:
								ei+=1

							if len(prei):
								IDs[prei] = docItem
							if prei == '*':
								setClip(docItem)
								quit_early = True
							colorizeRow( '\t'+prei+'\t'+ docItem , 2)
							# pr('\t'+prei+'\t'+ docItem ,c=helpColorScheme.examples)
			if 'id' in self.value('Help') or 'c' in self.value('Help') or 'ask' in self.value('Help') or 'i' in self.value('Help'):
				askID = input( '?> : ' )
				if askID in IDs:
					setClip(IDs[askID])
					cp(  [ '\n\nCopied:\n\t', IDs[askID], '\n\n' ], helpColorScheme.ask_example_id  )
			if quit_early:
				sys.exit()
					# colorizeRow('\t' + ex,2)
				print_('\n')
			if len(appInfo[__.appReg]['columns']) > 0:
				printBold('Columns and abbreviations:')
				result = ''
				if len( appInfo[__.appReg]['columns'] ):
					# fields.register( 'columns', 'name,abbreviation', script=__.triggerTest )
					fields.asset( 'columns', appInfo[__.appReg]['columns'] )
					print_()

				if __.columnAbbreviations == 0:
					for col in appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					colorizeRow('\t' + result + '\n',2)
					# helpColorScheme.abbreviations

				if __.columnAbbreviations == 1:
					for col in appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							abbreviation =  fields.value( 'columns', 'abbreviation', col['abbreviation'] )
							name =          fields.value( 'columns', 'name', col['name'] )
							colorizeRow( '\t' + abbreviation + '\t' + name )
							# helpColorScheme.abbreviations
						# print_( '\t', col['abbreviation'], '\t', col['name']  )

				if len( appInfo[__.appReg]['columns'] ):
					print_()
					print_()
				# print_('\n')
		pass
		print_()
		print_()
		# def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2, c='', half=False, h=None )
		linePrint(txt='+',c=helpColorScheme.line,x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		# printBold( 'Requirements:' )
		pr('Requirements:',c=helpColorScheme.labels)
		print_()
		hasRequirements = False
		# if __.isRequired_Pipe_or_File:
		#     hasRequirements = True
		#     colorThis(  [  '  !! Required Pipe or Files'  ]  , 'red' )

		# if len( self.isRequired[__.appReg] ):
		#     for x in self.isRequired[__.appReg]:
		#         hasRequirements = True
		#         colorThis(  [  '  !! Required Switch:', x  ]  , 'red' )

		if __.isRequired_Pipe:
			hasRequirements = True
			colorThis(  [  '  !! Required Pipe data' ]  , helpColorScheme.requiredLabel )

		if __.isRequired_Pipe_or_File:
			hasRequirements = True
			colorThis(  [  '  !! Required Pipe data or Files switch' ]  , helpColorScheme.requiredLabel )

		if len(self.isRequired[__.appReg]):
			hasRequirements = True
			colorThis(  [  '  !! Required ' + ' and '.join(self.isRequired[__.appReg])  ]  , helpColorScheme.requiredLabel )


		if not __.isRequired_or_List is None:
			# for x in __.isRequired_or_List:
			hasRequirements = True
			isRequired_or_List1 = pr('  !! Required   ',c=helpColorScheme.requiredLabel,p=0)
			isRequired_or_List2 = pr(' or '.join(__.isRequired_or_List),c=helpColorScheme.required,p=0)
			print_(isRequired_or_List1 +':   '+ isRequired_or_List2)
			# colorThis(  [  '  !! Required ' + ' or '.join(__.isRequired_or_List)  ]  , 'red' )

		lastGroup = -1
		for switch in self.switches:
			# print_( dir(switch) )
			# print_( switch.__dict__ )
			if len(switch.documentation['required']) :
				print_()
				print_()
				print_( colorThis( '  !! If using switch:' , helpColorScheme.switchRequredLabel, p=0 ), colorThis( switch.name , helpColorScheme.switchRequred, p=0 ), colorThis( 'the following is required:' , helpColorScheme.switchRequredLabel, p=0 ) )

				for x in switch.documentation['required']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'red' )


			if len(switch.documentation['related']) :
				print_()
				print_()
				print_( colorThis( '  If using switch:' , helpColorScheme.switchRequredLabel, p=0 ), colorThis( switch.name , helpColorScheme.switchRequred, p=0 ), colorThis( 'the following is related:' , helpColorScheme.switchRequredLabel, p=0 ) )
				for x in switch.documentation['related']:
					hasRequirements = True
					colorThis(  [ '\t', x  ]  , 'yellow' )

				# del switch.script_trigger
				# del switch.__dict__.script_trigger
				# print_( dict( str(switch.__dict__) ) )
				# printVar( dict(switch.__dict__) )
			# sys.exit()
		if not hasRequirements:
			colorThis( [ '\t', 'No requirements' ], helpColorScheme.noRequirements )
		print_()
		linePrint(txt='+',c=helpColorScheme.line,x=.5)
		# colorThis('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++','yellow')
		print_()
		print_()
		self.print()
		if 'notes' in appInfo[__.appReg]:
			if len( appInfo[__.appReg]['notes'] ):
				print_()
				print_()
				# printBold( 'Notes:' )
				pr('Notes:',c=helpColorScheme.labels)
				for col in appInfo[__.appReg]['notes']:
					print_()
					printVarSimple( col, prefix='                ', remove='"' )
					# helpColorScheme.notes
					print_()

		# for x in sys.modules:
		#     print_(x)
		sys.exit()
		raise SystemExit
		os._exit(0)
		sys.exit(1)
		os._exit(os.EX_OK)




	def process( self, helpx=False ):
		load()
		global customHelp
		global argvProcess
		global printAutoAbbreviations_scheduled
		for ii,sw in enumerate(self.switches):
			if self.switches[ii].appReg == __.appReg:
				self.switches[ii].pos = None
				self.switches[ii].active = False
				self.switches[ii].value = None
				try:
					__.trigger_isPipe = self.switches[ii].isData
				except Exception as e:
					pass

		switchHelp = []
		isActiveList = []
		hasActiveRequireList = []
		isActiveRequireList = []

		if argvProcess:
			for i,a in enumerate(sys.argv):
				a=a.replace('↔',' ')
				if a in __.switch_skimmer.scan:
					__.switch_skimmer.active.append( a )
				a = a.replace(':','')
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)

								isActiveList.append( ii )
								if self.switches[ii].name in self.hasRequired:
									hasActiveRequireList.append( ii )
								if self.switches[ii].name in self.isRequired[__.appReg]:
									isActiveRequireList.append( ii )

								if type( self.switches[ii].value ) == str:
									if '-??' in self.switches[ii].value:
										switchHelp.append(ii)

		if self.exists('_Raw') == True:
			# print_('test')
			self.fieldSet('_Raw','pos',1)
			self.fieldSet('_Raw','active',True)
			self.fieldSet('_Raw','value',self.format('_Raw'))


		for i,record in enumerate(self.switches):
			if self.appRegDefault is None:
				self.appRegDefault = self.switches[i].appReg
			self.index[ self.switches[i].appReg ] = {}
		for i,record in enumerate(self.switches):
			self.index[ self.switches[i].appReg ][self.switches[i].name] = i



		if len( switchHelp ):
			if __.cls_process_switches_help:
				os.system('cls')

			somethingPrinted = False
			for i in switchHelp:
				if len( self.switches[i].documentation['description'] ):
					somethingPrinted = True
					print_()
					print_( inlineBold('Description:\t'), self.switches[i].documentation['description'] )
					print_()
				if len( self.switches[i].documentation['examples'] ):
					printBold( 'Examples:' )
					for example in self.switches[i].documentation['examples']:
						if type(example) == list:
							colorThis( '\t\t'+example[0], example[1]  )
						else:
							colorizeRow( '\t\t'+ example , 2)



			if somethingPrinted:
				sys.exit()

		if self.isActive('PlusCode'):
			__.sw.PlusCode.append('0a72b2d27816')
			for xCode in self.values('PlusCode'):
				if len(xCode) > 1:
					if xCode.startswith('*'): __.sw.PlusCode.append('*x')
					elif xCode.endswith('*'): __.sw.PlusCode.append('x*')
				else:
					if xCode == '=': __.sw.PlusCode.append('=')
					elif xCode == '!': __.sw.PlusCode.append('=')


		if self.isActive('Help') or helpx:
			self.help()

		# if self.isActive(''):

		if not __.appReg in self.isRequired:
			for key in self.isRequired:
				__.appReg = key
		if len( self.isRequired[__.appReg] ):
			allSatisfied = True

			for req in self.isRequired[__.appReg]:
				satisfied = False
				for i in isActiveRequireList:
					if self.switches[i].name.lower() == req.lower():
						satisfied = True

				try:
					__.appInfoScan
				except Exception as e:
					if not satisfied:
						allSatisfied = False
						print_()
						print_( colorThis( 'Error:', 'red', p=0 ) + ' missing required switch:', req )
						sys.exit()


		if len( hasActiveRequireList ):
			allSatisfied = True
			for i in hasActiveRequireList:
				satisfied = False
				for r in self.switches[i].documentation['required']:
					for ia in isActiveList:
						if self.switches[i].name.lower() == r.lower():
							satisfied = True
				if not satisfied:
					if not i in switchHelp:
						switchHelp.append( i )
						print_()
						print_( 'Error:\t\t missing required switch' )
					allSatisfied = False



		if self.isActive('DumpSwitches'):
			if self.value('DumpSwitches'):
				pv(self.all())
			else:
				self.dumpSwitches()
			sys.exit()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			# self.print()
			self.printStatus()
			sys.exit()

		if printAutoAbbreviations_scheduled:
			printAutoAbbreviations()

		if self.isActive('TableProfile') and len(self.value('TableProfile')):
			global TableProfile_Config

			TableProfile_Config = {}

			values = self.values('TableProfile')
			value  = self.value('TableProfile')

			if not ',' in value and not ';' in value:
				tpv = value


				if tpv == 'gs' or tpv == 'groupspaces' or tpv == 'groupspace':
					try:
						TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
					except Exception as e:
						TableProfile_Config['ALLTABLES'] = {}
						TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
				elif tpv == 'hl':
					try:
						TableProfile_Config['_header_']['alignment'] = 'left'
					except Exception as e:
						TableProfile_Config['_header_'] = {}
						TableProfile_Config['_header_']['alignment'] = 'left'



			else:
				for tpv in value.split(','):
					if not ';' in tpv:



						if tpv == 'gs' or tpv == 'groupspaces' or tpv == 'groupspace':
							try:
								TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
							except Exception as e:
								TableProfile_Config['ALLTABLES'] = {}
								TableProfile_Config['ALLTABLES']['GroupSpaces'] = True
						elif tpv == 'hl':
							try:
								TableProfile_Config['_header_']['alignment'] = 'left'
							except Exception as e:
								TableProfile_Config['_header_'] = {}
								TableProfile_Config['_header_']['alignment'] = 'left'


					elif ';' in tpv and tpv.count(';') == 1:


						tpvX = tpv.split(';')
						if tpvX[1] == 'l' or tpvX[1] == 'left' or tpvX[1] == 'r' or tpvX[1] == 'right' or tpvX[1] == 'c' or tpvX[1] == 'center':
							if tpvX[0] == 'header' or tpvX[0] == 'h':
								tpvX[0] = '_header_'
							if tpvX[1] == 'l': tpvX[1] = 'left';
							if tpvX[1] == 'r': tpvX[1] = 'right';
							if tpvX[1] == 'c': tpvX[1] = 'center';
							try:
								TableProfile_Config[  tpvX[0]  ]['alignment'] = tpvX[1]
							except Exception as e:
								TableProfile_Config[  tpvX[0]  ] = {}
								TableProfile_Config[  tpvX[0]  ]['alignment'] = tpvX[1]

							# printVarSimple( TableProfile_Config )

		# theErrors()
		pass
		pass
		# for i,record in enumerate(self.switches):
		#   self.index[ self.switches[i].name +'._.'+ self.switches[i].appReg ] = i

		if len( self.postScripts ):
			for childScript in self.postScripts:
				if 'function' in str(type(childScript)):
					childScript()


	def searchIndex( self, name, appReg ):
		if type(appReg) == bool or appReg is None:
			appReg = __.appReg
		try:
			result = self.index[ appReg ][ name ]

			# result = self.index[ name +'._.'+ appReg ]
		except Exception as e:
			try:
				result = self.index[ self.appRegDefault ][ name ]
			except Exception as e:
				# print_( name, appReg, self.appRegDefault )
				result = None

		return result


	def print(self):
		switch = []
		global tables
		lastGroup = -1
		swLen = {
			'n':0,
			's':0,
			'e':0,
		}
		sgLe = {}
		lastGroup = -1
		sgLm = 0
		for i,sw in enumerate(self.switches):
			n = len(sw.name)
			s = len(sw.switch)
			try:
				e = len(sw.example_or_notes)
			except: e=0
			if n > swLen['n']: swLen['n'] = n
			if s > swLen['s']: swLen['s'] = s
			if e > swLen['e']: swLen['e'] = e
			if not sw.group is None:
				valid = True
				if type(sw.group) == str:
					swgroupID = sw.group
					swgroupLabel = sw.group
				else:
					if len(sw.group) > 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[1]
					elif len(sw.group) == 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[0]
			# try:
			# 	sw.group[0]
			# 	valid = True
			# except Exception as e:
			# 	valid = False
			# if valid:
			# 	if not lastGroup == sw.group[0]:
			# 		if sgLm > len(sw.group[1]): sgLm = len(sw.group[1])
			# 		sgLe[sw.group[0]] = len(sw.group[1])
			# 	lastGroup = sw.group[0]

		if sgLm > swLen['e']: swLen['e'] = sgLm
		
		
		sgSe = {}
		import math
		for i,L in enumerate(sgLe):
			l = swLen['e'] - sgLe[L]
			sp = math.floor(l / 4)
			sgSe[L] = ''
			for i in range( sp+1 ): sgSe[L] += ' '

		spaces = {
			'n':'',
			's':'',
		}
		sg = len('Switch Group: 1')
		if sg > swLen['n']: swLen['n'] = sg
		# for k in swLen:
		if not swLen['n'] == sg:
			for i in range( math.floor(swLen['n'] / 4) ): spaces['n'] += ' '
		
		for i in range( math.floor(swLen['s'] / 2) ): spaces['s'] += '-'
		# for i in range( swLen['s']-1 ): spaces['s'] += '-'
		spaces['s'] = '  <'+spaces['s']+'>'
		# pv(sgSe)
		lastGroup = -1
		lastLabel = ''

		# Start: SwitchSubGroup check
		SwitchGroup = False
		SwitchSubGroup = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				valid = False
				if not sw.group is None:
					valid = True
					if type(sw.group) == str:
						swgroupID = sw.group
						swgroupLabel = sw.group
					else:
						if len(sw.group) > 1:
							swgroupID = sw.group[0]
							swgroupLabel = sw.group[1]
						elif len(sw.group) == 1:
							swgroupID = sw.group[0]
							swgroupLabel = sw.group[0]
							
				if valid:
					SwitchGroup = True
					if not lastGroup == swgroupID:
						pass
					elif not swgroupID == swgroupLabel and not lastLabel == swgroupLabel:
						SwitchSubGroup = True
						# sys.exit()

				if __.switch_skimmer.active and not self.switches[i].default:
					pass
				elif not __.switch_skimmer.active:
					pass
				# try:
				# 	lastGroup = swgroupID
				# 	lastLabel = swgroupLabel
				# except: pass 
		# End: SwitchSubGroup check


		for i,sw in enumerate(self.switches):
			if self.switches[i].default and self.justAppNotFullHelp: continue
			if self.switches[i].appReg == __.appReg:
				valid = False
				if not sw.group is None:
					valid = True
					if type(sw.group) == str:
						swgroupID = sw.group
						swgroupLabel = sw.group
					else:
						if len(sw.group) > 1:
							swgroupID = sw.group[0]
							swgroupLabel = sw.group[1]
						elif len(sw.group) == 1:
							swgroupID = sw.group[0]
							swgroupLabel = sw.group[0]
							
				if valid:
					# print('valid',sw.name)
					if False:
						pass
					elif not lastGroup == swgroupID:
						if SwitchSubGroup:
							pass
							switch.append({ 'HasSwitchSubGroup': '', 'SwitchGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
							
						else:
							pass
							# sys.exit()
							# pr(swgroupLabel,c='BackgroundGreyBold.green')
							if len(sw.group) > 3 and sw.group[2] == 0:
								# switch.append({ 'SwitchGroupPostLabel': sw.group[3].strip(), 'name': '','switch': '','example_or_notes': ''})
								switch.append({ 'SwitchGroup': swgroupLabel.strip(), 'SwitchGroupPostLabel': sw.group[3].strip(),'name': '','switch': '','example_or_notes': ''})
							else:
								switch.append({ 'SwitchGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
						# switch.append({'name':'' ,'switch':'','example_or_notes': '>>'})
					elif not swgroupID == swgroupLabel and not lastLabel == swgroupLabel:
						if len(sw.group) > 2:
							switch.append({ 'SwitchGroupDepth': sw.group[2], 'SwitchSubGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
						else:
							switch.append({ 'SwitchSubGroup': swgroupLabel.strip(), 'name': '','switch': '','example_or_notes': ''})
					# continue
					# SwitchGroup
				if __.switch_skimmer.active and not self.switches[i].default:
					if SwitchGroup:
						if valid:
							key = 'valid'
						else:
							key = 'SwitchGroup'

						switch.append({key:'','name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
					else:
						switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
				elif not __.switch_skimmer.active:
					if SwitchGroup:
						if valid:
							key = 'valid'
						else:
							key = 'SwitchGroup'

						switch.append({key:'','name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
					else:
						switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
					# switch.append({'name':sw.name ,'switch':sw.switch,'example_or_notes': sw.example_or_notes})
				try:
					lastGroup = swgroupID
					lastLabel = swgroupLabel
				except: pass


		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,example_or_notes')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = ''
				v=[]
				for x in sw.values: v.append(str(x))
				value = ' | '.join(v)

				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = ''

				switch.append({'name':sw.name ,'active':active,'value': value})
		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,active,value')
	def active(self,theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		table = []
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				# print_( type(sw.active), sw.active )
				if sw.active:
					table.append(sw.name)
		return table


	def length(self,theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		ii = 0
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				ii += 1
		return ii

	def rebuild( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if row.appReg == appReg:
				if row.active:
					sX = row.switch.split(',')
					if row.value is None:
						r = sX[0]
					else:
						r = sX[0] + ' ' + str(row.value)
					data.append( r )
			# print_(row.name,'\t',row.value,'\t',row.appReg)
		return ' '.join( data )
	def getTable( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:

					info = {
								'name': row.name,
								'value': row.value,
								'values': row.values,
					}

					data.append( info )
		return data


	def loadTable( self, data, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			for info in data:
				if row.appReg == appReg:
					if row.name == info['name']:

						self.switches[i].value = info['value']
						self.switches[i].values = info['values']
						self.switches[i].active = True

	def onlyLoadEpoch( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active and not row.name == 'LoadEpoch':
					return False


		return True

