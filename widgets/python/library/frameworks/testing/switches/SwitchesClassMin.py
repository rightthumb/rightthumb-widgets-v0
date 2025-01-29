import base as _


class Switch:

	def __init__(self, name, switch, expected_input_example = None):
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = []
		self.expected_input_example = expected_input_example
		self.script_trigger_external = null

	def trigger(self,script):
		self.script_trigger_external = script




class Switches:

	def __init__(self):
		self.switches = {}

	def register(self, name, switch, expected_input_example = None):
		self.switches[name] = Switch(name, switch, expected_input_example)

	def updateSwitchField(self,name,column,value):
		if column == 'value':
			if not type(value) is list:
				value = [value]
			for i,v in enumerate(value):
				if self.doesFieldExist(name,'script_trigger_external') == True:
					value[i] = self.externalScriptTrigger(name,value[i])
					# self.getSwitchField(name,'script_trigger')(value)
				elif self.doesFieldExist(name,'script_trigger') == True:
					script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
					value[i] = eval(script)
		if name in self.switches:
			exec('self.switches[\''+name+'\'].' + column + '=value')



	def doesFieldExist(self,name,column):
		if name in self.switches:
			if column in self.switches[name].__dict__:
				return True
		return False

		return None
	def externalScriptTrigger(self,name,value):
		if name in self.switches:
			return self.switches[name].script_trigger_external(value)


	def getSwitchField(self,name,column):
		if name in self.switches:
			return eval("self.switches['"+name+"']." + column )

	def isActive(self,name):
		return self.getSwitchField(name,'active')

	def values(self,name):
		return self.value(name)
	def value(self,name):
		if name in self.switches:
			return self.switches[name].value
		return []
	def trigger(self,name,script):

		if name in self.switches:
			return self.switches[name].trigger(script)
			# return script( self.switches[name].value )



	def getSwitchValue2(self,name):
		switchInput = sys.argv.copy()

		try:
			switchInput[self.getSwitchField(name,'pos') + 1]
			result = []

			i = 0
			for a in switchInput:
				if i > self.getSwitchField(name,'pos'):
					if self.checkIfSwitch(switchInput[i]) == True:
						break
					else:
						result.append(switchInput[i])
				i += 1


		except Exception as e:
			result = []
		return result
	def checkIfSwitch(self,string):
		result = False

		for key in self.switches:
			for b in self.switches[key].switch.split(','):
				if b == string:
					result = True
					# print(b,result)
		return result

	def processSwitchFormatting(self,name):
		value = self.getSwitchValue2(name)
		# print('value',value)
		for i,v in enumerate(value):
			if self.doesFieldExist(name,'script_trigger_external') == True:
				value[i] = self.externalScriptTrigger(name,value[i])
			elif self.doesFieldExist(name,'script_trigger') == True:
				script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
				value[i] = eval(script)
		return value

	def checkSwitchExist(self,name):
		if name in self.switches:
			return True
		return False


	def process(self):
		# print(inList)
		global customHelp

		switchInput = sys.argv.copy()
		for sw in self.switches:
			self.switches[sw].pos = None
			self.switches[sw].active = False
			self.switches[sw].value = []
		for i,a in enumerate(sys.argv.copy()):
			# a = a.replace(':','')
			# print('a',a)
			for sw in self.switches:
				# print(sw['name'])
				for s in self.switches[sw].switch.split(','):
					# print(s)
					# print( s,a )
					if s.lower() == a.lower():
						self.switches[sw].pos = i
						self.switches[sw].active = True
						self.switches[sw].value = self.processSwitchFormatting(self.switches[sw].name)

		if self.isActive('Help') == True:
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
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			self.print()
			sys.exit()

		# theErrors()
	def print(self):
		return None
		print( 'print aborted' )

########################################################################################


# # Create an instance of the Switches class
# switches = Switches()

# # Register switches
# switches.register('Name', '-name', 'John Doe')
# switches.register('Age', '-age', '30')

# # Process the switches based on sys.argv
# switches.process()

# # Access switch values
# name = switches.value('Name')
# age = switches.value('Age')
