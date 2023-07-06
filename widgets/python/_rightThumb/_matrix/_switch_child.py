import _rightThumb._matrix as _matrix

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

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.triggerDefault = None
		self.registration = registration
		self.switchDelim = _matrix.switchDelim
		self.switchDelimReplace = _matrix.switchDelimReplace
		_matrix.app.sequences['switch']['algorithm'] = {}
		self.key = None
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );


	def add( self, theID, registration ):
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']

		self.required = False
		self.pipe = False
		self.documentation = {}
		
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
		_matrix.app.algorithmResult( algorithm, result=None )
		
	def hasVal( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		
		if len(self.value):
			return _matrix.app.algorithmResult( algorithm, result=True )
		else:
			return _matrix.app.algorithmResult( algorithm, result=False )
	def hv( self, trackingID=None ):
		return self.hasVal( trackingID=trackingID )

	def l( self, trackingID=None ):
		return self.hasVal( trackingID=trackingID )


	def inV( self, search, trackingID=None ):
		return self.inVal( search, trackingID=trackingID )
	def inVal( self, search, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID, note=search)
		
		result = False
		for val in self.values:
			if search in val:
				result = True
		return _matrix.app.algorithmResult( algorithm, result=result )

	def isV( self, search, trackingID=None ):
		return self.isVal( search, trackingID=trackingID )
	def isVal( self, search, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID,note=search)
		
		result = False
		for val in self.values:
			if search.lower() == val.lower():
				result = True

		return _matrix.app.algorithmResult( algorithm, result=result )
	def about( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		result = {
					'active': self.active,
					'values': self.values,
					'value': self.value,
		}        
		return _matrix.app.algorithmResult( algorithm, result=result )


	def isActive( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		return _matrix.app.algorithmResult( algorithm, result=self.active )

	def ia( self, trackingID=None ):
		return self.isActive( trackingID=trackingID )

	def a( self, trackingID=None ):
		return self.isActive( trackingID=trackingID )



	def setActive( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.active = True
		_matrix.app.algorithmResult( algorithm, result=None )

	def setNotActive( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.active = False
		_matrix.app.algorithmResult( algorithm, result=None )



	def v( self, data=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		
		if not data is None:
			self.value = self.format(data)
			self.values = [self.value]
		


	def vs( self, data=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		_matrix.app.algorithmResult( algorithm, result=None )


		if not data is None:
			for i,d in enumerate(data):
				data[i] = self.format(d)
			self.values = data
			for i,v in data:
				data[i] = data[i].replace( self.switchDelim, self.switchDelimReplace )
			self.value = self.switchDelim.join( data )
		


	def getValue( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		return _matrix.app.algorithmResult( algorithm, result=self.value )

	def getValues( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		return _matrix.app.algorithmResult( algorithm, result=self.values )


	def setValue( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.value = self.format(data)
		_matrix.app.algorithmResult( algorithm, result=None )

	def setValues( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)

		for i,d in enumerate(data):
			data[i] = self.format(d)
		self.values = data
		for i,v in data:
			data[i] = data[i].replace( self.switchDelim, self.switchDelimReplace )
		self.value = self.switchDelim.join( data )

		_matrix.app.algorithmResult( algorithm, result=None )

	def trigger( self, script, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.script = script
		_matrix.app.algorithmResult( algorithm, result=None )

	def format( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		
		if self.script is None:
			return _matrix.app.algorithmResult( algorithm, result=data )
		else:
			result = self.script( data )
			return _matrix.app.algorithmResult( algorithm, result=result )

	def triggerColumns( self ):
		algorithm = _matrix.app.algorithmRegister()
		_matrix.app.algorithmResult( algorithm, result=None )
		self.triggerDefault = 'Columns'
		pass

	def triggerColumnsSort( self ):
		algorithm = _matrix.app.algorithmRegister()
		_matrix.app.algorithmResult( algorithm, result=None )
		self.triggerDefault = 'ColumnsSort'
		pass

	def triggerAgo( self ):
		algorithm = _matrix.app.algorithmRegister()
		_matrix.app.algorithmResult( algorithm, result=None )
		self.triggerDefault = 'triggerAgo'
		pass

	def dump( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		for i, key in enumerate(_matrix.app.records['switch']):
			record = _matrix.app.records['switch'][key]
			_.pr(  record.focus,  record.name, record.active )
		_matrix.app.algorithmResult( algorithm, result=None )


	def audit( self, ):
		return _matrix.app.callers()


# p file + _child --c | p line --c -make " n {} "


		



