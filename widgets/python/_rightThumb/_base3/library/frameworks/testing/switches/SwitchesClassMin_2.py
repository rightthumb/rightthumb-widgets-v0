import sys
import _rightThumb._string as _str








class Tables:

	def __init__(self, name):
		self.name
		self.fields = []

	def trigger(self,field,script):
		self.fields.append({'name': field, 'script_trigger_external': script })


class Switch:

	def __init__(self, name, switch, expected_input_example = None):
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = None
		self.expected_input_example = expected_input_example

	def trigger(self,script):
		self.script_trigger_external = script




class Switches:

	def __init__(self):
		self.switches = []

	def register(self, name, switch, expected_input_example = None):
		self.switches.append(Switch(name, switch, expected_input_example))

	def updateSwitchField(self,name,column,value):
		if column == 'value':
			if self.doesFieldExist(name,'script_trigger_external') == True:
				value = self.externalScriptTrigger(name,value)
				# self.getSwitchField(name,'script_trigger')(value)
			elif self.doesFieldExist(name,'script_trigger') == True:
				script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value)
				value = eval(script)
		i = 0
		for row in self.switches:
			if row.name == name:
				exec('self.switches[i].' + column + '=str(\'' + value + '\')')
			i += 1
		return ''



	def doesFieldExist(self,name,column):
		try:
			for row in self.switches:
				if row.name == name:
					eval('row.' + column)
					result = True
		except Exception as e:
			result = False
		return result
	def externalScriptTrigger(self,name,value):
		i = 0
		for s in self.switches:
			if name == self.switches[i].name:
				value = self.switches[i].script_trigger_external(value)
			i += 1
		return value


	def getSwitchField(self,name,column):
		switch = self.switches
		result = ''
		for row in switch:
			if row.name == name:
				result = eval('row.' + column)
		return result

	def isSwitchActive(self,name):
		return self.getSwitchField(name,'active')

	def getSwitchValue(self,name):
		result = self.getSwitchField(name,'value')
		if result is None:
			result = ''
		return result

	def setExternalScriptTrigger(self,name,script):
		i = 0
		for s in self.switches:
			
			if name == self.switches[i].name:
				self.switches[i].trigger(script)
			i += 1


	def getSwitchValue2(self,name):
		switchInput = sys.argv

		try:
			switchInput[self.getSwitchField(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.getSwitchField(name,'pos'):
					if self.checkIfSwitch(switchInput[i]) == True:
						break
					else:

						if switchInput[i] == ':':
							switchInput[i] = switchInput[i].replace(':','_;192B;_')
						if switchInput[i] == ',':
							switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			result = _str.cleanAll(result,'"','')
			result = _str.cleanAll(result,':,',':')
			result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = None
		return result
	def checkIfSwitch(self,string):
		result = False
		for a in self.switches:
			for b in a.switch.split(','):
				if b == string:
					result = True
					# print(b,result)
		return result
	# def process(self):
	# 	i = 0
	# 	for a in sys.argv:
	# 		a = a.replace(':','')
	# 		ii = 0
	# 		for sw in self.switches:
	# 			# print(sw['name'])
	# 			for s in self.switches[ii].switch.split(','):
	# 				# print(s)
	# 				if s.lower() == a.lower():
	# 					self.switches[ii].pos = i
	# 					self.switches[ii].active = True
	# 					self.switches[ii].value = self.getSwitchValue2(self.switches[ii].name)
	# 			ii += 1
	# 		i += 1
	def processSwitchFormatting(self,name):
		value = self.getSwitchValue2(name)
		if self.doesFieldExist(name,'script_trigger_external') == True:
			value = self.externalScriptTrigger(name,value)
		elif self.doesFieldExist(name,'script_trigger') == True:
			script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def checkSwitchExist(self,name):
		result = False
		for sw in self.switches:
			if sw.name == name:
				result = True
		return result

	def process(self):
		# print(inList)
		global customHelp

		switchInput = sys.argv
		ii = 0
		for sw in self.switches:
			self.switches[ii].pos = None
			self.switches[ii].active = False
			self.switches[ii].value = None
			ii += 1
		i = 0
		for a in switchInput:
			a = a.replace(':','')
			ii = 0
			for sw in self.switches:
				# print(sw['name'])
				for s in sw.switch.split(','):
					# print(s)
					if s.lower() == a.lower():
						self.switches[ii].pos = i
						self.switches[ii].active = True
						self.switches[ii].value = self.processSwitchFormatting(self.switches[ii].name)
				ii += 1
			i += 1
		if self.checkSwitchExist('_Raw') == True:
			# print('test')
			self.updateSwitchField('_Raw','pos',1)
			self.updateSwitchField('_Raw','active',True)
			self.updateSwitchField('_Raw','value',self.processSwitchFormatting('_Raw'))
			# i = 0
			# for a in switchInput:
			# 	print(i,a)
			# 	i += 1
		if self.isSwitchActive('Help') == True:
			global appInfo
			# os.system('cls')
			print('')
			try:
				print('Description: \t', appInfo['description'] + '\n')
				configured = True
			except Exception as e:
				configured = False
			try:
				if len(appInfo['prerequisite']) > 0:
					print('Prerequisite:')
					for prereq in appInfo['prerequisite']:
						print('\t' + prereq)
					print('\n')
			except Exception as e:
				pass


			if configured:
				if len(appInfo['examples']) > 0:
					print('Examples:')
					for ex in appInfo['examples']:
						print('\t' + ex)
					print('\n')
				if len(appInfo['columns']) > 0:
					print('Columns and abbreviations:')
					result = ''
					for col in appInfo['columns']:
						result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					print('\t' + result + '\n')
					# print('\n')
			self.print()
			sys.exit()
		if self.isSwitchActive('Debug') == True or self.isSwitchActive('Errors') == True:
			self.print()
			sys.exit()

		# theErrors()
	def print():
		switch = []
		for sw in self.switches:
			switch.append({'name':sw.name ,'switch':sw.switch,'expected_input_example': sw.expected_input_example})
		printColumns(switch,'name,switch,expected_input_example')
# 	def getSelf(self,name):
# 		result = ''
# 		for sw in self.switches:
# 			if sw.name == name:
# 				result = sw
# 		return result
# def getSwitchSelf(name):
# 	global switches
# 	return switches.getSelf(name)




switches = Switches()
switches.register('Help','?,/?,-?,/h,help,/help,-help,--help')
switches.register('Column','-c,-column')
appInfo=	{
	'file': 'drive.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}
appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
appInfo['columns'].append({'name': 'initiated', 'abbreviation': 'i'})
appInfo['columns'].append({'name': 'type', 'abbreviation': 't'})
appInfo['columns'].append({'name': 'priority', 'abbreviation': 'p'})
appInfo['columns'].append({'name': 'drive', 'abbreviation': 'd,l,dr'})
appInfo['columns'].append({'name': 'machineID', 'abbreviation': 'm'})
appInfo['columns'].append({'name': 'timestamp', 'abbreviation': 'ts,time,date'})
def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

switches.setExternalScriptTrigger('Column',formatColumns)


switches.process()

print(switches.getSwitchField('Column','pos'))
print(switches.getSwitchValue('Column'))
switches.updateSwitchField('Column','value','fish')
print(switches.getSwitchValue('Column'))
print(switches.getSwitchField('Column','value'))
print(switches.isSwitchActive('Column'))
print(switches.isSwitchActive('Help'))
print(switches.isSwitchActive('Test'))

if switches.isSwitchActive('Help'):
	print('Help is active')
else:
	print('Help is NOT active')

if switches.isSwitchActive('Column'):
	print('Column is active')
else:
	print('Column is NOT active')

# _.tableProfile.append({
# 	'field': 'timestamp', 
# 	'script_trigger_external': _.float2Date
# 	})

sys.argv


