import sys
import os
import importlib.util
current_file = os.path.abspath(__file__)
# base_path = os.path.normpath(os.path.join(current_file, f'..{os.sep}..{os.sep}..{os.sep}..{os.sep}'))
base_path = os.path.normpath(os.path.join(current_file, '..', '..', '..', '..'))
base_path = os.path.normpath(os.path.join(current_file, '..', '..', '..', '..', '..'))
if base_path not in sys.path:
	sys.path.insert(0,base_path)

_rt = sys.path.insert(0,os.path.normpath(os.path.join(base_path, '_rightThumb')))
if _rt not in sys.path:
	sys.path.insert(0,_rt)
# print(sys.path)

import _rightThumb._base3 as _
import _rightThumb._construct as __
# print(__)
# try:
#     _ = import_something(os.path.join('_rightThumb', '_base3', '__init__.py'), '_')
# except: print('taco')
# try:
#     __ = import_something(os.path.join('_rightThumb', '_construct', '__init__.py'), '__')
# except: print('burrito')
# import fields
# import os
# import row
# import sw
# import sys

errors = []
appInfo = {}
appData = {}
# argvProcess = True
# printAutoAbbreviations_scheduled = False
def blank_script_trigger(data):
	return data
class Switch:
	global __
	global _
	def __init__(self, name, switch='', example_or_notes=None, description='', space=False, default=False, group=None):
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
		self.documentation = {'description': description, 'examples': [], 'required': [], 'related': []}
		self.space = space
		self.vs = False
		self.script_trigger_alt = None
		self.script = blank_script_trigger
	def trigger(self, script, vs=False, alt=None):
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
	def all(self, app=True, appReg=None, omit=None, omitDefaults=True, od=1):
		if not od:
			omitDefaults = False
		if omitDefaults:
			omitList = ['Help', 'Column', 'Sort', 'Debug', 'Errors', 'Timeout', 'GroupBy', 'ShortenColumn', 'Long', 'Length', 'Report', 'Plus', 'Minus', 'PlusOr', 'PlusClose', 'PrintAutoAbbreviations', 'LoadEpoch', 'NoColor', 'Clean', 'NoCount', 'Count']
		else:
			omitList = []
		if not omit is None:
			if type(omit) == str:
				omit = omit.replace(' ', '')
				omit = omit.split(',')
			for x in omit:
				omitList.append(x)
		if appReg is None:
			appReg = __.appReg
		# print('appReg', appReg)
		result = []
		for i, row in enumerate(self.switches):
			if appReg == '__init__':
				appReg = row.appReg
			if not row.name in omitList:
				if row.active:
					shouldAdd = True
					if app:
						if type(appReg) == str:
							if not appReg == 'all':
								if not row.appReg == appReg:
									shouldAdd = False
					if shouldAdd:
						if not row.values:
							for ii, rec in enumerate(self.switches):
								if not i == ii and rec.name == row.name and rec.values:
									shouldAdd = False
					if shouldAdd:
						result.append({'active': row.active, 'name': row.name, 'value': row.value, 'values': row.values, 'appReg': row.appReg})
		return result
	def records(self, formating=None, appReg=None):
		if formating is None:
			_.colorThis('formating options:', 'bold')
			_.colorThis(['\t', 'list'], 'yellow')
			_.colorThis(['\t', 'dic_a-v', '\t', "{ 'isActive': {}, 'values': {} }"], 'yellow')
			_.colorThis(['\t', 'dic_on-off-v', '\t', "{ 'on': [], 'off': [], 'values': {} }"], 'yellow')
			_.colorThis(['\t', 'dump'], 'yellow')
			_.colorThis(['\t', 'relevant'], 'yellow')
			_.colorThis(['\t', 'dump2'], 'yellow')
			sys.exit()
			_.colorThis()
		if appReg is None:
			appReg = __.appReg
		records = {'list': [], 'dic_a-v': {'active': self.active(), 'isActive': {}, 'values': {}}, 'dic_on-off-v': {'on': [], 'off': [], 'values': {}}, 'dump': [], 'dump2': {}}
		for i, switch in enumerate(self.switches):
			if not switch.appReg in records['dump2']:
				records['dump2'][switch.appReg] = {}
			if not 'on' in records['dump2'][switch.appReg]:
				records['dump2'][switch.appReg]['on'] = {}
				records['dump2'][switch.appReg]['off'] = {}
			if switch.active:
				if switch.name in records['dump2'][switch.appReg]['on'] and switch.values:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
				else:
					records['dump2'][switch.appReg]['on'][switch.name] = switch.values
			else:
				records['dump2'][switch.appReg]['off'][switch.name] = switch.values
			shouldAdd = True
			for ii, rec in enumerate(self.switches):
				if not i == ii and rec.name == switch.name and rec.values:
					shouldAdd = False
			if shouldAdd:
				if self.switches[i].appReg == appReg:
					records['list'].append({'name': switch.name, 'values': switch.values})
					records['dic_a-v']['isActive'][switch.name] = switch.active
					records['dic_a-v']['values'][switch.name] = switch.values
					records['dump'] = dict(((name, getattr(switch, name)) for name in dir(switch) if not name.startswith('__')))
					records['dic_on-off-v']['values'][switch.name] = switch.values
					if switch.active:
						records['dic_on-off-v']['on'].append(switch.name)
					else:
						records['dic_on-off-v']['off'].append(switch.name)
		records['relevant'] = {}
		for on in records['dic_on-off-v']['on']:
			records['relevant'][on] = records['dic_on-off-v']['values'][on]
		if formating.startswith('r'):
			formating = 'relevant'
		return records[formating]
	def documentation(self, name, data):
		result = False
		try:
			for i, row in enumerate(self.switches):
				if row.name == name:
					if self.switches[i].appReg == __.appReg:
						try:
							if len(data['description']):
								self.switches[i].documentation['description'] = data['description']
						except Exception as e:
							pass
						try:
							if len(data['examples']):
								self.switches[i].documentation['examples'] = data['examples']
						except Exception as e:
							pass
						try:
							if len(data['required']):
								self.switches[i].documentation['required'] = []
								self.switches[i].documentation['related'] = []
								for record in data['required']:
									if record == 'Pipe':
										__.isRequired_Pipe = True
									else:
										self.switches[i].documentation['required'].append(record)
										self.switches[i].documentation['related'].append(record)
										if not name in self.hasRequired:
											self.hasRequired.append(name)
						except Exception as e:
							pass
						try:
							if len(data['related']):
								for record in data['related']:
									self.switches[i].documentation['related'].append(record)
						except Exception as e:
							pass
						try:
							if type(data['isRequired']) == bool:
								if data['isRequired']:
									if not name in self.isRequired[__.appReg]:
										self.isRequired[__.appReg].append(name)
						except Exception as e:
							pass
		except Exception as e:
			result = False
		return result
	def record(self, name):
		result = False
		try:
			for i, row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						return i
		except Exception as e:
			result = False
		return result
	def dumpSwitches(self, includeBlank=False):
		_.tables = _.Tables()
		self.fieldSet('Long', 'active', True)
		data = []
		for i, row in enumerate(self.switches):
			if includeBlank:
				data.append({'name': row.name, 'value': row.value, 'appreg': row.appReg})
			elif not row.value is None or row.active:
				data.append({'name': row.name, 'value': row.value, 'appreg': row.appReg})
		_.tables = _.Tables()
		_.tables.register('data', data)
		_.tables.print('data', 'appreg,name,value')
	def items(self): return self.switches
	def pr(self,name,switch,trigger=None): self.postRegister(name,switch,trigger)
	def pReg(self,name,switch,trigger=None): self.postRegister(name,switch,trigger)
	def postRegister(self,name,switch,trigger=None):
		if trigger:
			__.SwitchesModifier.Trigger[name] = trigger
		self.switches.append(Switch(name,switch))
		if _.argvProcess:
			for i, a in enumerate(sys.argv):
				a = a.replace('↔', ' ')
				if a in __.switch_skimmer.scan:
					__.switch_skimmer.active.append(a)
				a = a.replace(':', '')
				__.switches_values = {}

				for ii, sw in enumerate(self.switches):
					if not sw.name == name:
						continue
					if a.lower() in sw.switch.lower().split(','):
						__.switches_values[self.switches[ii].name] = []
						self.index[__.appReg][self.switches[ii].name] = ii
						self.switches[ii].pos = i
						self.switches[ii].active = True
						self.switches[ii].value = self.format(self.switches[ii].name)
						self.switches[ii].values = self.format2(self.switches[ii].name)



						if self.switches[ii].name in __.SwitchesModifier.Trigger:
							self.switches[ii].script_trigger = __.SwitchesModifier.Trigger[self.switches[ii].name]
						

						try:
							self.switches[ii].value = self.switches[ii].script_trigger(self.switches[ii].value)
							for i,value in enumerate(self.switches[ii].values):
								self.switches[ii].values[i] = self.switches[ii].script_trigger(value)
							self.switches[ii].valuesBK = self.switches[ii].values
						except: pass



									




	def register(self, name, switch, example_or_notes=None, isRequired=False, isPipe=None, isData=None, description='', space=False, default=False, group=None, g=None, trigger=None, t=None):
		if not t is None: trigger = t
		if not trigger is None: __.SwitchesModifier.Trigger[name] = trigger
		if not g is None:
			group = g
		if not isPipe is None:
			__.trigger_isPipe = isPipe
		if not isData is None:
			__.trigger_isPipe = isData
			isPipe = isData
		i = len(self.switches)
		if not __.appReg in self.dex:
			self.dex[__.appReg] = {}
		self.dex[__.appReg][name] = i
		self.switches.append(Switch(name, switch, example_or_notes, description, space, default, group))
		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []
		switch = switch.replace(' ', '')
		if not isPipe is None:
			__.isData_Switches[name] = isPipe
			if type(isPipe) == bool and isPipe:
				isPipe = 'data'
			_.vv.isData[name] = isPipe
			isPipe = isPipe.replace('raw', 'name')
			if 'name' in isPipe and ('data' in isPipe or 'clean' in isPipe):
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
			if not __.appReg in __.isRequired_index:
				__.isRequired_index[__.appReg] = []
			__.isRequired_index[__.appReg].append(name)
			if not name in self.isRequired[__.appReg]:
				self.isRequired[__.appReg].append(name)
	def fieldSet2(self, name, column, value, theFocus=False, runTrigger=True):
		for i, row in enumerate(self.switches):
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
	def val(self, name, column, value, theFocus=False, runTrigger=True):
		return self.fieldSet(name, column, value, theFocus, runTrigger)
	def fieldSet(self, name, column, value, theFocus=False, runTrigger=True):
		if name == 'Sort':
			if column == 'value':
				if type(value) == str:
					if value.startswith('a.'):
						value = 'a:' + value[2:]
					if ',a.' in value:
						value = value.replace(',a.', ',a:')
					if value.startswith('d.'):
						value = 'd:' + value[2:]
					if ',d.' in value:
						value = value.replace(',d.', ',d:')
			if column == 'values':
				if type(value) == list:
					for i, asdf in enumerate(value):
						if value[i].startswith('a.'):
							value[i] = 'a:' + value[i][2:]
						if value[i].startswith('d.'):
							value[i] = 'd:' + value[i][2:]
		if type(theFocus) == bool:
			theFocus = __.appReg
		if column == 'values':
			if type(value) == str:
				value = [value]
			values = []
			valuesV = []
			if not runTrigger:
				for x in value:
					values.append(x)
			elif runTrigger:
				if self.fieldExists(name, 'script_trigger', theFocus):
					for x in value:
						values.append(self.scriptTrigger(name, x, theFocus))
				elif self.fieldExists(name, 'script_trigger', theFocus) == True:
					for x in value:
						script = "{}('{}','{}')".format(self.fieldGet(name, 'script_trigger'), name, x)
						values.append(eval(script))
				else:
					for x in value:
						values.append(x)
			for x in values:
				if type(x) == str:
					valuesV.append(x.replace(',', ';;'))
		if column == 'value':
			if runTrigger:
				if self.fieldExists(name, 'script_trigger', theFocus):
					value = self.scriptTrigger(name, value, theFocus)
				elif self.fieldExists(name, 'script_trigger', theFocus) == True:
					script = "{}('{}','{}')".format(self.fieldGet(name, 'script_trigger'), name, value)
					value = eval(script)
		for i, row in enumerate(self.switches):
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
						exec('self.switches[i].' + column + '= value')
		return ''
	def fieldExists(self, name, column, theFocus=False):
		result = False
		try:
			for i, row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger(self, name, value, theFocus=False, cc=False):
		for i, s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					if not cc:
						value = self.switches[i].script_trigger(value)
					elif cc:
						if not self.switches[i].vs:
							value = self.switches[i].script_trigger(value)
						elif not self.switches[i].script_trigger_alt is None:
							value = self.switches[i].script_trigger_alt(value)
		return value
	def fieldGet2(self, name, column):
		result = ''
		for i, row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result
	def fieldGet(self, name, column, theFocus=False):
		if theFocus == False:
			theFocus = __.appReg
		result = ''
		if not column == 'pos':
			if name == 'NoColor' and column == 'active':
				found = False
				for i, row in enumerate(self.switches):
					if row.name == name:
						if row.active:
							found = True
				result = found
			else:
				i = self.searchIndex(name, theFocus)
				if i is None:
					if column == 'active':
						return False
					if column == 'value':
						return ''
					if column == 'values':
						return []
					_.printBold('Error: Nonexistent Switch', 'red')
					_.print_(name, column, theFocus)
					_.printVar(self.index)
					sys.exit()
				row = self.switches[i]
				result = eval('row.' + column)
		else:
			if type(theFocus) == bool:
				theFocus = __.appReg
			for i, row in enumerate(self.switches):
				if self.switches[i].appReg == theFocus:
					if row.name == name:
						result = eval('row.' + column)
		return result
	def isActive2(self, name, theFocus=False):
		for i, row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return True
		return False
	def isActive(self, name, theFocus=False):
		if not theFocus:
			theFocus = __.appReg
		if theFocus in self.dex and name in self.dex[theFocus]:
			return self.switches[self.dex[theFocus][name]].active
		return self.fieldGet(name, 'active', theFocus)
	def getField(self, name, field, theFocus=False):
		return self.fieldGet(name, field, theFocus)
	def value(self, name, theFocus=False):
		result = self.fieldGet(name, 'value', theFocus)
		if result is None:
			result = ''
		return result
	def values2(self, name, theFocus=False):
		for i, row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet(name, 'values', theFocus)
		return []
	def value2(self, name, theFocus=False):
		for i, row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return self.fieldGet(name, 'value', theFocus)
		return ''
	def isActive2(self, name, theFocus=False):
		for i, row in enumerate(self.switches):
			if self.switches[i].name == name and self.switches[i].active:
				return True
		return False
	def values(self, name, theFocus=False):
		if theFocus==False: theFocus=__.appReg
		# valuesBK
		result = self.fieldGet(name, 'values', theFocus)
		if result is None:
			result = []
		return result
	def trigger(self, name, script, vs=False, alt=None):
		for i, s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script, vs, alt)
	def simpleTrigger(self, name, value):
		return self.switches[self.dex[__.appReg][name]].script(value)
	def value2(self, name):
		switchInput = sys.argv
		values = []
		for i, a in enumerate(switchInput):
			switchInput[i] = a.replace('↔', ' ')
		try:
			switchInput[self.fieldGet(name, 'pos') + 1]
			result = ''
			i = 0
			for a in switchInput:
				if i > self.fieldGet(name, 'pos'):
					if self.isSwitch(switchInput[i]) == True:
						# _.pr('break',c='red')
						break
					else:
						if not name in __.switch_raw:
							if switchInput[i] == ':':
								switchInput[i] = switchInput[i].replace(':', '_;192B;_')
							if switchInput[i] == ',':
								switchInput[i] = switchInput[i].replace(',', '_;192A;_')
						result += str(switchInput[i]) + ','
						if not name in __.switches_values:
							__.switches_values[name] = []
						__.switches_values[name].append(switchInput[i])
						
				i += 1
			result = result[:-1]
			if not name in __.switch_raw:
				result = _str.cleanAll(result, '"', '')
				result = _str.cleanAll(result, ':,', ':')
				result = _str.cleanAll(result, ',,', ',')
		except Exception as e:
			result = ''
		if not name in __.switch_raw:
			return result
		else:
			return result
	def value3(self, name):
		if name in __.switches_values:
			return __.switches_values[name]
		else:
			return None
		switchInput = sys.argv
		for i, a in enumerate(switchInput):
			switchInput[i] = a.replace('↔', ' ')
		data = []
		try:
			switchInput[self.fieldGet(name, 'pos') + 1]
			result = ''
			for i, a in enumerate(switchInput):
				if i > self.fieldGet(name, 'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					elif not a == ' ':
						if not name in __.switch_raw:
							data.append(a)
						else:
							data.append(a)
					else:
						data.append(a)
		except Exception as e:
			data = []
		return data
	def isSwitch(self, string):
		result = False
		for i, a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
		return result
	def format(self, name):
		value = self.value2(name)
		if self.fieldExists(name, 'script_trigger'):
			value = self.scriptTrigger(name, value, cc=True)
		elif self.fieldExists(name, 'script_trigger'):
			script = "{}('{}','{}')".format(self.fieldGet(name, 'script_trigger'), name, value)
			value = eval(script)
		return value
	def format2(self, name):
		# valuesBK
		values = self.value3(name)
		if values is None:
			values = []
		else:
			for i, value in enumerate(values):
				if self.fieldExists(name, 'script_trigger'):
					values[i] = self.scriptTrigger(name, value, cc=True)
				elif self.fieldExists(name, 'script_trigger'):
					script = "{}('{}','{}')".format(self.fieldGet(name, 'script_trigger'), name, value)
					values[i] = eval(script)
		return values
	def exists(self, name):
		result = False
		for i, sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result
	def help(self, justAppNotFullHelp=False):
		_.helpColorScheme.labels = 'ColorBold.white'
		_.helpColorScheme.tableSwitchGroupsLine = 'blue'
		_.helpColorScheme.tableSwitchGroupsPostLabel = 'yellow'
		_.helpColorScheme.file = 'Background.light_blue'
		_.helpColorScheme.description = 'Background.green'
		_.helpColorScheme.tags = 'green'
		_.helpColorScheme.prerequisite = 'ColorBold.blue'
		_.helpColorScheme.relatedapps = 'ColorBold.blue'
		_.helpColorScheme.examples = 'purple'
		_.helpColorScheme.ask_example_id = 'yellow'
		_.helpColorScheme.abbreviations = 'purple'
		_.helpColorScheme.line = 'yellow'
		_.helpColorScheme.requiredLabel = 'red'
		_.helpColorScheme.required = 'Background.red'
		_.helpColorScheme.switchRequredLabel = 'ColorBold.white'
		_.helpColorScheme.switchRequred = 'yellow'
		_.helpColorScheme.noRequirements = 'green'
		_.helpColorScheme.notes = 'purple'
		self.justAppNotFullHelp = justAppNotFullHelp
		if self.value('Help') == 'x' or self.value('Help') == 'cls' or self.value('Help') == 'clear' or ('fn' in self.value('Help')):
			if 'fn' in self.values('Help'):
				info = self.values('Help')
				info.pop(0)
				if not info:
					_.pr('Usage:', c='yellow')
					for li in ['']:
						_.pr('\t- ' + li, c='cyan')
					sys.exit()
				import inspect
				fn = info[0]
				info.pop(0)
				_.pr('Function:', fn, c='yellow')
				if not info or (info[0] == 'arg' or info[0] == 'args'):
					argspec = list(inspect.getfullargspec(eval(fn)))
					_.pr('\t', argspec[0])
				sys.exit()
			if __.isWin:
				os.system('cls')
			else:
				os.system('clear')
		if len(__.registeredApps) > 1:
			if __.appReg == '__init__' or __.appReg == 'cryptFile':
				return None
		if __.appInfoScan:
			return None
		global appInfo
		global fields
		self.fieldSet('Long', 'active', True)
		if __.cls_process_switches_help or 'cls' in self.value('Help'):
			os.system('cls')
		_.print_()
		_.print_()
		filename = _.colorThis(['Program:  \t'], _.helpColorScheme.labels, p=0)
		try:
			if not _.appInfo[__.appReg]['file'] == 'thisApp.py' and _.appInfo[__.appReg]['liveAppName'] == '__init__':
				filename += _.colorThis([_.appInfo[__.appReg]['file'].replace('.py', '')], _.helpColorScheme.file, p=0)
				sys.exit()
			else:
				try:
					if not _.appInfo[__.appReg]['file'] == 'thisApp.py' and (not _.appInfo[__.appReg]['liveAppName'] == '__init__'):
						filename += _.colorThis([_.appInfo[__.appReg]['liveAppName']], _.helpColorScheme.file, p=0)
					else:
						filename += _.colorThis([_.appInfo[__.appReg]['file'].replace('.py', '')], _.helpColorScheme.file, p=0)
				except Exception as e:
					filename += _.colorThis([_.appInfo[__.appReg]['file'].replace('.py', '')], _.helpColorScheme.file, p=0)
		except:
			pass
		_.print_()
		_.print_(filename)
		_.print_()
		try:
			if type(_.appInfo[__.appReg]['description']) == list:
				_.print_(_.pr('Description:   ', c=_.helpColorScheme.labels, p=0))
				for x in _.appInfo[__.appReg]['description']:
					_.print_('                 - ', _.pr(x, c=_.helpColorScheme.description, p=0))
				_.print_()
			else:
				_.print_(_.inlineBold('Description:   '), _.pr(_.appInfo[__.appReg]['description'], c=_.helpColorScheme.description, p=0) + '\n')
			configured = True
		except Exception as e:
			configured = False
		try:
			_.print_(_.inlineBold('Tags:          '), '(', _.pr(', '.join(_.appInfo[__.appReg]['categories']), c=_.helpColorScheme.tags, p=0), ')' + '\n')
			pass
		except Exception as e:
			pass
		try:
			if len(_.appInfo[__.appReg]['prerequisite']) > 0:
				_.pr('Prerequisite:', c=_.helpColorScheme.labels)
				for docItem in _.appInfo[__.appReg]['prerequisite']:
					if type(docItem) == list:
						_.pr('\t\t' + docItem[0], c=_.helpColorScheme.prerequisite)
					else:
						_.pr('\t\t' + docItem, c=_.helpColorScheme.prerequisite)
				_.print_('\n')
		except Exception as e:
			pass
		try:
			if len(_.appInfo[__.appReg]['relatedapps']) > 0:
				_.pr('Related Apps:', c=_.helpColorScheme.labels)
				for docItem in _.appInfo[__.appReg]['relatedapps']:
					if type(docItem) == list:
						_.pr('\t\t' + docItem[0], c=_.helpColorScheme.relatedapps)
					else:
						_.pr('\t\t' + docItem, c=_.helpColorScheme.relatedapps)
				_.print_('\n')
		except Exception as e:
			pass
		if configured:
			quit_early = False
			if len(_.appInfo[__.appReg]['examples']) > 0:
				_.pr('Examples:', c=_.helpColorScheme.labels)
				IDs = {}
				ei = 1
				for docItem in _.appInfo[__.appReg]['examples']:
					if not docItem is None:
						prei = str(ei)
						if len(self.value('Help')) and self.value('Help') == prei:
							prei = '*'
						elif not 'id' in self.value('Help') and (not 'c' in self.value('Help')) and (not 'i' in self.value('Help')):
							prei = ''
						else:
							quit_early = True
						if type(docItem) == list:
							if not len(docItem[0]):
								prei = ''
							else:
								ei += 1
							if prei == '*':
								_.setClip(docItem[0])
								quit_early = True
							if len(prei):
								IDs[prei] = docItem[0]
							_.pr('\t' + prei + '\t' + docItem[0], c=_.helpColorScheme.examples)
						else:
							if not len(docItem):
								prei = ''
							else:
								ei += 1
							if len(prei):
								IDs[prei] = docItem
							if prei == '*':
								_.setClip(docItem)
								quit_early = True
							_.colorizeRow('\t' + prei + '\t' + docItem, 2)
			if 'id' in self.value('Help') or 'c' in self.value('Help') or 'ask' in self.value('Help') or ('i' in self.value('Help')):
				askID = input('?> : ')
				if askID in IDs:
					_.setClip(IDs[askID])
					cp(['\n\nCopied:\n\t', IDs[askID], '\n\n'], _.helpColorScheme.ask_example_id)
			if quit_early:
				sys.exit()
				_.print_('\n')
			if len(_.appInfo[__.appReg]['columns']) > 0:
				_.printBold('Columns and abbreviations:')
				result = ''
				if len(_.appInfo[__.appReg]['columns']):
					fields.asset('columns', _.appInfo[__.appReg]['columns'])
					_.print_()
				if __.columnAbbreviations == 0:
					for col in _.appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					_.colorizeRow('\t' + result + '\n', 2)
				if __.columnAbbreviations == 1:
					for col in _.appInfo[__.appReg]['columns']:
						if not col['name'] == col['abbreviation']:
							abbreviation = fields.value('columns', 'abbreviation', col['abbreviation'])
							name = fields.value('columns', 'name', col['name'])
							_.colorizeRow('\t' + abbreviation + '\t' + name)
				if len(_.appInfo[__.appReg]['columns']):
					_.print_()
					_.print_()
		pass
		_.print_()
		_.print_()
		_.linePrint(txt='+', c=_.helpColorScheme.line, x=0.5)
		_.pr('Requirements:', c=_.helpColorScheme.labels)
		_.print_()
		hasRequirements = False
		if __.isRequired_Pipe:
			hasRequirements = True
			_.colorThis(['  !! Required Pipe data'], _.helpColorScheme.requiredLabel)
		if __.isRequired_Pipe_or_File:
			hasRequirements = True
			_.colorThis(['  !! Required Pipe data or Files switch'], _.helpColorScheme.requiredLabel)
		if len(self.isRequired[__.appReg]):
			hasRequirements = True
			_.colorThis(['  !! Required ' + ' and '.join(self.isRequired[__.appReg])], _.helpColorScheme.requiredLabel)
		if not __.isRequired_or_List is None:
			hasRequirements = True
			isRequired_or_List1 = _.pr('  !! Required   ', c=_.helpColorScheme.requiredLabel, p=0)
			isRequired_or_List2 = _.pr(' or '.join(__.isRequired_or_List), c=_.helpColorScheme.required, p=0)
			_.print_(isRequired_or_List1 + ':   ' + isRequired_or_List2)
		lastGroup = -1
		for switch in self.switches:
			if len(switch.documentation['required']):
				_.print_()
				_.print_()
				_.print_(_.colorThis('  !! If using switch:', _.helpColorScheme.switchRequredLabel, p=0), _.colorThis(switch.name, _.helpColorScheme.switchRequred, p=0), _.colorThis('the following is required:', _.helpColorScheme.switchRequredLabel, p=0))
				for x in switch.documentation['required']:
					hasRequirements = True
					_.colorThis(['\t', x], 'red')
			if len(switch.documentation['related']):
				_.print_()
				_.print_()
				_.print_(_.colorThis('  If using switch:', _.helpColorScheme.switchRequredLabel, p=0), _.colorThis(switch.name, _.helpColorScheme.switchRequred, p=0), _.colorThis('the following is related:', _.helpColorScheme.switchRequredLabel, p=0))
				for x in switch.documentation['related']:
					hasRequirements = True
					_.colorThis(['\t', x], 'yellow')
		if not hasRequirements:
			_.colorThis(['\t', 'No requirements'], _.helpColorScheme.noRequirements)
		_.print_()
		_.linePrint(txt='+', c=_.helpColorScheme.line, x=0.5)
		_.print_()
		_.print_()
		self.print()
		if 'notes' in _.appInfo[__.appReg]:
			if len(_.appInfo[__.appReg]['notes']):
				_.print_()
				_.print_()
				_.pr('Notes:', c=_.helpColorScheme.labels)
				for col in _.appInfo[__.appReg]['notes']:
					_.print_()
					_.printVarSimple(col, prefix='                ', remove='"')
					_.print_()
		sys.exit()
		raise SystemExit
		os._exit(0)
		sys.exit(1)
		os._exit(os.EX_OK)
	def process(self, helpx=False):
		_.load()
		global customHelp
		# global argvProcess
		
		for ii, sw in enumerate(self.switches):
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
		if _.argvProcess:
			for i, a in enumerate(sys.argv):
				a = a.replace('↔', ' ')
				if a in __.switch_skimmer.scan:
					__.switch_skimmer.active.append(a)
				a = a.replace(':', '')
				__.switches_values = {}
				for ii, sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								__.switches_values[self.switches[ii].name] = []
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)



								if self.switches[ii].name in __.SwitchesModifier.Trigger:
									self.switches[ii].script_trigger = __.SwitchesModifier.Trigger[self.switches[ii].name]
								

								try:
									self.switches[ii].value = self.switches[ii].script_trigger(self.switches[ii].value)
									for i,value in enumerate(self.switches[ii].values):
										self.switches[ii].values[i] = self.switches[ii].script_trigger(value)
									self.switches[ii].valuesBK = self.switches[ii].values
								except: pass



									



								isActiveList.append(ii)
								if self.switches[ii].name in self.hasRequired:
									hasActiveRequireList.append(ii)
								if self.switches[ii].name in self.isRequired[__.appReg]:
									isActiveRequireList.append(ii)
								if type(self.switches[ii].value) == str:
									if '-??' in self.switches[ii].value:
										switchHelp.append(ii)
		if self.exists('_Raw') == True:
			self.fieldSet('_Raw', 'pos', 1)
			self.fieldSet('_Raw', 'active', True)
			self.fieldSet('_Raw', 'value', self.format('_Raw'))
		for i, record in enumerate(self.switches):
			if self.appRegDefault is None:
				self.appRegDefault = self.switches[i].appReg
			self.index[self.switches[i].appReg] = {}
		for i, record in enumerate(self.switches):
			self.index[self.switches[i].appReg][self.switches[i].name] = i
		if len(switchHelp):
			if __.cls_process_switches_help:
				os.system('cls')
			somethingPrinted = False
			for i in switchHelp:
				if len(self.switches[i].documentation['description']):
					somethingPrinted = True
					_.print_()
					_.print_(_.inlineBold('Description:\t'), self.switches[i].documentation['description'])
					_.print_()
				if len(self.switches[i].documentation['examples']):
					_.printBold('Examples:')
					for example in self.switches[i].documentation['examples']:
						if type(example) == list:
							_.colorThis('\t\t' + example[0], example[1])
						else:
							_.colorizeRow('\t\t' + example, 2)
			if somethingPrinted:
				sys.exit()
		if self.isActive('PlusCode'):
			__.sw.PlusCode.append('0a72b2d27816')
			for xCode in self.values('PlusCode'):
				if len(xCode) > 1:
					if xCode.startswith('*'):
						__.sw.PlusCode.append('*x')
					elif xCode.endswith('*'):
						__.sw.PlusCode.append('x*')
				elif xCode == '=':
					__.sw.PlusCode.append('=')
				elif xCode == '!':
					__.sw.PlusCode.append('=')
		if self.isActive('Help') or helpx:
			self.help()
		if not __.appReg in self.isRequired:
			for key in self.isRequired:
				##change
				if key:
					__.appReg = key

		if len(self.isRequired[__.appReg]):
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
						_.print_()
						_.print_(_.colorThis('Error:', 'red', p=0) + ' missing required switch:', req)
						sys.exit()
		if len(hasActiveRequireList):
			allSatisfied = True
			for i in hasActiveRequireList:
				satisfied = False
				for r in self.switches[i].documentation['required']:
					for ia in isActiveList:
						if self.switches[i].name.lower() == r.lower():
							satisfied = True
				if not satisfied:
					if not i in switchHelp:
						switchHelp.append(i)
						_.print_()
						_.print_('Error:\t\t missing required switch')
					allSatisfied = False
		if self.isActive('DumpSwitches'):
			if self.value('DumpSwitches'):
				pv(self.all())
			else:
				self.dumpSwitches()
			sys.exit()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			self.printStatus()
			sys.exit()
		if _.printAutoAbbreviations_scheduled:
			_.printAutoAbbreviations()
		if self.isActive('TableProfile') and len(self.value('TableProfile')):
			global TableProfile_Config
			TableProfile_Config = {}
			values = self.values('TableProfile')
			value = self.value('TableProfile')
			if not ',' in value and (not ';' in value):
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
						if tpvX[1] == 'l' or tpvX[1] == 'left' or tpvX[1] == 'r' or (tpvX[1] == 'right') or (tpvX[1] == 'c') or (tpvX[1] == 'center'):
							if tpvX[0] == 'header' or tpvX[0] == 'h':
								tpvX[0] = '_header_'
							if tpvX[1] == 'l':
								tpvX[1] = 'left'
							if tpvX[1] == 'r':
								tpvX[1] = 'right'
							if tpvX[1] == 'c':
								tpvX[1] = 'center'
							try:
								TableProfile_Config[tpvX[0]]['alignment'] = tpvX[1]
							except Exception as e:
								TableProfile_Config[tpvX[0]] = {}
								TableProfile_Config[tpvX[0]]['alignment'] = tpvX[1]
		pass
		pass
		if len(self.postScripts):
			for childScript in self.postScripts:
				if 'function' in str(type(childScript)):
					childScript()
	def searchIndex(self, name, appReg):
		if type(appReg) == bool or appReg is None:
			appReg = __.appReg
		try:
			result = self.index[appReg][name]
		except Exception as e:
			try:
				result = self.index[self.appRegDefault][name]
			except Exception as e:
				result = None
		return result
	def print(self):
		switch = []
		lastGroup = -1
		swLen = {'n': 0, 's': 0, 'e': 0}
		sgLe = {}
		lastGroup = -1
		sgLm = 0
		for i, sw in enumerate(self.switches):
			n = len(sw.name)
			s = len(sw.switch)
			try:
				e = len(sw.example_or_notes)
			except:
				e = 0
			if n > swLen['n']:
				swLen['n'] = n
			if s > swLen['s']:
				swLen['s'] = s
			if e > swLen['e']:
				swLen['e'] = e
			if not sw.group is None:
				valid = True
				if type(sw.group) == str:
					swgroupID = sw.group
					swgroupLabel = sw.group
				elif len(sw.group) > 1:
					swgroupID = sw.group[0]
					swgroupLabel = sw.group[1]
				elif len(sw.group) == 1:
					swgroupID = sw.group[0]
					swgroupLabel = sw.group[0]
		if sgLm > swLen['e']:
			swLen['e'] = sgLm
		sgSe = {}
		import math
		for i, L in enumerate(sgLe):
			l = swLen['e'] - sgLe[L]
			sp = math.floor(l / 4)
			sgSe[L] = ''
			for i in range(sp + 1):
				sgSe[L] += ' '
		spaces = {'n': '', 's': ''}
		sg = len('Switch Group: 1')
		if sg > swLen['n']:
			swLen['n'] = sg
		if not swLen['n'] == sg:
			for i in range(math.floor(swLen['n'] / 4)):
				spaces['n'] += ' '
		for i in range(math.floor(swLen['s'] / 2)):
			spaces['s'] += '-'
		spaces['s'] = '  <' + spaces['s'] + '>'
		lastGroup = -1
		lastLabel = ''
		SwitchGroup = False
		SwitchSubGroup = False
		for i, sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				valid = False
				if not sw.group is None:
					valid = True
					if type(sw.group) == str:
						swgroupID = sw.group
						swgroupLabel = sw.group
					elif len(sw.group) > 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[1]
					elif len(sw.group) == 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[0]
				if valid:
					SwitchGroup = True
					if not lastGroup == swgroupID:
						pass
					elif not swgroupID == swgroupLabel and (not lastLabel == swgroupLabel):
						SwitchSubGroup = True
				if __.switch_skimmer.active and (not self.switches[i].default):
					pass
				elif not __.switch_skimmer.active:
					pass
		for i, sw in enumerate(self.switches):
			if self.switches[i].default and self.justAppNotFullHelp:
				continue
			if self.switches[i].appReg == __.appReg:
				valid = False
				if not sw.group is None:
					valid = True
					if type(sw.group) == str:
						swgroupID = sw.group
						swgroupLabel = sw.group
					elif len(sw.group) > 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[1]
					elif len(sw.group) == 1:
						swgroupID = sw.group[0]
						swgroupLabel = sw.group[0]
				if valid:
					if False:
						pass
					elif not lastGroup == swgroupID:
						if SwitchSubGroup:
							pass
							switch.append({'HasSwitchSubGroup': '', 'SwitchGroup': swgroupLabel.strip(), 'name': '', 'switch': '', 'example_or_notes': ''})
						else:
							pass
							if len(sw.group) > 3 and sw.group[2] == 0:
								switch.append({'SwitchGroup': swgroupLabel.strip(), 'SwitchGroupPostLabel': sw.group[3].strip(), 'name': '', 'switch': '', 'example_or_notes': ''})
							else:
								switch.append({'SwitchGroup': swgroupLabel.strip(), 'name': '', 'switch': '', 'example_or_notes': ''})
					elif not swgroupID == swgroupLabel and (not lastLabel == swgroupLabel):
						if len(sw.group) > 2:
							switch.append({'SwitchGroupDepth': sw.group[2], 'SwitchSubGroup': swgroupLabel.strip(), 'name': '', 'switch': '', 'example_or_notes': ''})
						else:
							switch.append({'SwitchSubGroup': swgroupLabel.strip(), 'name': '', 'switch': '', 'example_or_notes': ''})
				if __.switch_skimmer.active and (not self.switches[i].default):
					if SwitchGroup:
						if valid:
							key = 'valid'
						else:
							key = 'SwitchGroup'
						switch.append({key: '', 'name': sw.name, 'switch': sw.switch, 'example_or_notes': sw.example_or_notes})
					else:
						switch.append({'name': sw.name, 'switch': sw.switch, 'example_or_notes': sw.example_or_notes})
				elif not __.switch_skimmer.active:
					if SwitchGroup:
						if valid:
							key = 'valid'
						else:
							key = 'SwitchGroup'
						switch.append({key: '', 'name': sw.name, 'switch': sw.switch, 'example_or_notes': sw.example_or_notes})
					else:
						switch.append({'name': sw.name, 'switch': sw.switch, 'example_or_notes': sw.example_or_notes})
				try:
					lastGroup = swgroupID
					lastLabel = swgroupLabel
				except:
					pass
		_.tables = _.Tables()
		_.tables.register('switches', switch)
		_.tables.print('switches', 'name,switch,example_or_notes')
	def printStatus(self):
		switch = []
		for i, sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = ''
				v = []
				for x in sw.values:
					v.append(str(x))
				value = ' | '.join(v)
				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = ''
				switch.append({'name': sw.name, 'active': active, 'value': value})
		_.tables = _.Tables()
		_.tables.register('switches', switch)
		_.tables.print('switches', 'name,active,value')
	def active(self, theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		table = []
		for i, sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if sw.active:
					table.append(sw.name)
		return table
	def length(self, theFocus=None):
		if theFocus is None:
			theFocus = __.appReg
		ii = 0
		for i, sw in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				ii += 1
		return ii
	def rebuild(self, theFocus=False):
		if not type(theFocus) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg
		data = []
		for i, row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:
					sX = row.switch.split(',')
					if row.value is None:
						r = sX[0]
					else:
						r = sX[0] + ' ' + str(row.value)
					data.append(r)
		return ' '.join(data)
	def getTable(self, theFocus=False):
		if not type(theFocus) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg
		data = []
		for i, row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:
					info = {'name': row.name, 'value': row.value, 'values': row.values}
					data.append(info)
		return data
	def loadTable(self, data, theFocus=False):
		if not type(theFocus) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg
		for i, row in enumerate(self.switches):
			for info in data:
				if row.appReg == appReg:
					if row.name == info['name']:
						self.switches[i].value = info['value']
						self.switches[i].values = info['values']
						self.switches[i].active = True
	def onlyLoadEpoch(self, theFocus=False):
		if not type(theFocus) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg
		for i, row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active and (not row.name == 'LoadEpoch'):
					return False
		return True
