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

import sys
from _rightThumb._hub import app

argvProcess=False
printAutoAbbreviations_scheduled=False



############################################################## copy-fn-class


class Switch:
	def __init__( self, name, switch, expected_input_example = None ):
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = []
		self.expected_input_example = expected_input_example
		self.script_trigger_external = None

	def trigger( self, script ):
		self.script_trigger_external = script


class Subject:
	def __init__( self ):
		self.switches = {}
 
 
	def statuses( self ):
		sws = dot()
		sws.status = {}
		sws.active = {}
		for name in self.switches:
			if self.switches[name].active:
				sws.active[name] = 1
				sws.status[name] = 1
			else:
				sws.status[name] = 0
		return sws

 
	def reg( self, name, switch, expected_input_example = None ):
 
 
 
		self.switches[name] = Switch(name, switch, expected_input_example)
	def updateSwitchField( self, name, column, value ):
 
 
 
		if column == 'value':
			if not type(value) is list:
				value = [value]
			for i,vv in enumerate(value):
				if self.doesFieldExist(name,'script_trigger_external') == True:
					value[i] = self.externalScriptTrigger(name,value[i])
					# self.getSwitchField(name,'script_trigger')(value)
				elif self.doesFieldExist(name,'script_trigger') == True:
					script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
					value[i] = eval(script)
		if name in self.switches:
			exec('self.switches[\''+name+'\'].' + column + '=value')
	def doesFieldExist( self, name, column ):
 
 
 
		if name in self.switches:
			if column in self.switches[name].__dict__:
				return True
		return False
		return None
	def externalScriptTrigger( self, name, value ):
 
 
 
		if name in self.switches:
			try:
				return self.switches[name].script_trigger_external(value)
			except Exception as e:
				return value
				
	def getSwitchField( self, name, column ):
 
 
 
		if name in self.switches:
			return eval("self.switches['"+name+"']." + column )
	def isActive( self, name ):
 
 
 
		return self.getSwitchField(name,'active')
	def values( self, name ):
 
 
 
		return self.value(name)
	def value( self, name ):
 
 
 
		if name in self.switches:
			return self.switches[name].value
		return []
	def trigger( self, name, script ):
 
 
 
		if name in self.switches:
			return self.switches[name].trigger(script)
			# return script( self.switches[name].value )
	def getSwitchValue2( self, name ):
 
 
 
		switchInput = sys.argv
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
	def checkIfSwitch( self, string ):
 
 
 
		result = False
		
		for key in self.switches:
			for b in self.switches[key].switch.split(','):
				if b == string:
					result = True
					# print(b,result)
		return result
	def processSwitchFormatting( self, name ):
 
 
 
		value = self.getSwitchValue2(name)
		# print('value',value)
		for i,vv in enumerate(value):
			if self.doesFieldExist(name,'script_trigger_external') == True:
				value[i] = self.externalScriptTrigger(name,value[i])
			elif self.doesFieldExist(name,'script_trigger') == True:
				script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
				value[i] = eval(script)
		return value
	def checkSwitchExist( self, name ):
 
 
 
		if name in self.switches:
			return True
		return False
	def process( self, arg=True ):
 
 
 
		# print(inList)
		global customHelp
		switchInput = sys.argv
		for sw in self.switches:
			self.switches[sw].pos = None
			self.switches[sw].active = False
			self.switches[sw].value = []
		for i,a in enumerate(sys.argv):
			for sw in self.switches:
				for s in self.switches[sw].switch.split(','):
					if s.lower() == a.lower():
						self.switches[sw].pos = i
						self.switches[sw].active = True
						self.switches[sw].value = self.processSwitchFormatting(self.switches[sw].name)
		if self.isActive('Help'):
			print_help()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			self.print()
			sys.exit()
		# theErrors()
	def print( self ):
 
 
 
		p = 'FB2DEDECEA7E'
		return None
		print( 'print aborted' )





