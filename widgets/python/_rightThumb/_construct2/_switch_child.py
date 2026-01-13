import _rightThumb._construct2 as __

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import _rightThumb._base3 as _
import time


class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.triggerDefault = None
		self.registration = registration
		self.switchDelim = __.switchDelim
		self.switchDelimReplace = __.switchDelimReplace
		__.app.sequences['switch']['algorithm'] = {}
		self.key = None
		self.add( theID, registration )



	def add( self, theID, registration ):
		__.app.algorithmRegister( 'switch', 'add' )
		self.ids.append( theID )
		self.required = False
		self.pipe = False
		self.documentation = {}
		self.focus = registration['focus']
		
		self.isDefault = registration['isDefault']
		if 'isRequired' in registration.keys():
			self.required = registration['isRequired']
		
		if 'isPipe' in registration.keys():
			self.required = registration['isPipe']

		if 'example' in registration.keys():
			self.example = registration['example']
		else:
			self.example = None


		if 'expected_input_example' in registration.keys():
			self.expected_input_example = registration['expected_input_example']
		else:
			self.expected_input_example = None


		if 'examples' in registration.keys():
			self.documentation['examples'] = registration['examples']

		if 'required' in registration.keys():
			self.documentation['required'] = registration['required']

		if 'related' in registration.keys():
			self.documentation['related'] = registration['related']

		if 'description' in registration.keys():
			self.documentation['description'] = registration['description']
		else:
			self.documentation = None

		self.name = None
		self.switches = None

		if 'name' in registration.keys():
			self.name = registration['name']
		if 'n' in registration.keys():
			self.name = registration['n']

		if 'switches' in registration.keys():
			self.switches = registration['switches']
		if 's' in registration.keys():
			self.switches = registration['s']

		self.appReg = registration['focus']


		self.id = theID
		self.pos = 0
		self.active = False
		self.value = ''
		self.values = []
		self.script = None
		
	def hasVal( self, activity=None ):
		if len(self.value):
			__.app.algorithmRegister( 'switch', 'hasVal', activity, True )
			return True
		else:
			__.app.algorithmRegister( 'switch', 'hasVal', activity, False )
			return False
	def hv( self, activity=None ):
		return self.hasVal( activity )

	def l( self, activity=None ):
		return self.hasVal( activity )


	def inV( self, search, activity=None ):
		return self.inVal( search, activity )
	def inVal( self, search, activity=None ):
		result = False
		for val in self.values:
			if search in val:
				result = True
		if result:
			__.app.algorithmRegister( 'switch', 'inVal', activity, True, search )
		else:
			__.app.algorithmRegister( 'switch', 'inVal', activity, False, search )
		return result

	def isV( self, search, activity=None ):
		return self.isVal( search, activity )
	def isVal( self, search, activity=None ):
		result = False
		for val in self.values:
			if search.lower() == val.lower():
				result = True
		if result:
			__.app.algorithmRegister( 'switch', 'isVal', activity, True, search )
		else:
			__.app.algorithmRegister( 'switch', 'isVal', activity, False, search )
		return result
	def about( self, activity=None ):
		__.app.algorithmRegister( 'switch', 'about', activity )
		return {
					'active': self.active,
					'values': self.values,
					'value': self.value,
		}


	def isActive( self, activity=True, isIF=True ):
		__.app.algorithmRegister( 'switch', 'isActive', activity )
		return self.active

	def ia( self, activity=None, isIF=True ):
		return self.isActive( activity )

	def a( self, activity=None, isIF=True ):
		return self.isActive( activity )



	def setActive( self, activity=None ):
		__.app.algorithmRegister( 'switch', 'setActive', activity )
		self.active = True

	def setNotActive( self, activity=None ):
		__.app.algorithmRegister( 'switch', 'setNotActive', activity )
		self.active = False



	def v( self, data=None, activity=None ):
		__.app.algorithmRegister( 'switch', 'v', activity )
		if not data is None:
			self.value = self.format(data)
			self.values = [self.value]
		return self.value

	def vs( self, data=None, activity=None ):
		__.app.algorithmRegister( 'switch', 'vs', activity )
		if not data is None:
			for i,d in enumerate(data):
				data[i] = self.format(d)
			self.values = data
			for i,v in data:
				data[i] = data[i].replace( self.switchDelim, self.switchDelimReplace )
			self.value = self.switchDelim.join( data )
		return self.values

	def getValue( self, activity=None ):
		__.app.algorithmRegister( 'switch', 'getValue', activity )
		return self.value

	def getValues( self, activity=None ):
		__.app.algorithmRegister( 'switch', 'getValues', activity )
		return self.values

	def setValue( self, data, activity=None ):
		__.app.algorithmRegister( 'switch', 'setValue', activity )
		self.value = self.format(data)

	def setValues( self, data, activity=None ):
		__.app.algorithmRegister( 'switch', 'setValues', activity )
		for i,d in enumerate(data):
			data[i] = self.format(d)
		self.values = data
		for i,v in data:
			data[i] = data[i].replace( self.switchDelim, self.switchDelimReplace )
		self.value = self.switchDelim.join( data )

	def trigger( self, script, activity=None ):
		__.app.algorithmRegister( 'switch', 'trigger', activity )
		self.script = script

	def format( self, data, activity=None ):
		__.app.algorithmRegister( 'switch', 'format', activity )
		if self.script is None:
			return data
		else:
			return self.script( data )

	def triggerColumns( self ):
		self.triggerDefault = 'Columns'
		pass

	def triggerColumnsSort( self ):
		self.triggerDefault = 'ColumnsSort'
		pass

	def triggerAgo( self ):
		self.triggerDefault = 'triggerAgo'
		pass

	def dump( self ):
		for i, key in enumerate(__.app.records['switch']):
			record = __.app.records['switch'][key]
			_.pr(  record.focus,  record.name, record.active )

	def setKeys( self ):
		for i, key in enumerate(__.app.records['switch']):
			__.app.records['switch'][key].key = key
			

	def call( self ):
		audit = __.app.algorithmRegister( 'switch', 'call' )
		_.printVar( audit )



		


