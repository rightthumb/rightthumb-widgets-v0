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
import _rightThumb._string as _str
import sys

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.value = None
		self.status = True
		self.size = 0
		self.singeSet = False
		self.live = ''
		self.memoryHistory = []
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );

	def add( self, theID, registration ):
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']

		# _.colorThis(  [ self.name ], 'yellow'  )
		self.value = registration['value']
		self.size = _.get_size(self.value)
		self.memoryHistory.append( self.size )
		_matrix.app.totalMemory()
		_matrix.app.algorithmResult( algorithm, result=None )
		

	def unregister( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.status = False
		self.value = None
		# _.colorThis(  [ 'unregister:', self.name, self.size, _matrix.app.totalMemory() ], 'yellow'  )
		_matrix.app.totalMemory()
		_matrix.app.algorithmResult( algorithm, result=None )
		# return _matrix.app.memory

	def clear( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.set( None )
		self.status = False
		self.singeSet = False
		_matrix.app.algorithmResult( algorithm, result=None )


	def set( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.live = _matrix.app.callers()[0]['file']
		# _.pr('self.live',self.live)
		# _.printVarSimple(  )

		self.status = True
		self.value = data
		_matrix.app.totalMemory()
		self.size = _.get_size(self.value)
		self.memoryHistory.append( self.size )
		_matrix.app.algorithmResult( algorithm, result=None )
		return data

		# _.pr('set',self.value)

	def get( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		
		# _.pr('get')
		return _matrix.app.algorithmResult( algorithm, result=self.value )

	def clean( self, data, clean=0, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)

		if type(data) == list:
			newData = []
			for row in data:
				row = row.replace( '\n', '' )
				row = row.replace( '\r', '' )
				if clean == 2:
					row = _str.replaceDuplicate( row, ' ' )
					row = _str.cleanBE( row, ' ' )
				shouldAdd = True
				if clean > 0:
					if not len(row):
						shouldAdd = False
				if shouldAdd:
					newData.append( row )
		elif type(data) == str:
			if clean > 0:
				if not len( data[0].replace( '\f', '' ) ):
					data = data[1:]
			if clean >= 2:
				data = data.replace( '\r', '' )
				data = _str.replaceDuplicate( row, '\n' )
			if clean >= 3:
				data = _str.replaceDuplicate( row, '  ' )
			newData = data
		
		return _matrix.app.algorithmResult( algorithm, result=newData )

	def stdin( self, isList=None, isText=None, trackingID=None ):
		return self.pipe( isList=isList, isText=isText, trackingID=trackingID )

	def pipe( self, isList=None, isText=None, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		if isList is None and isText is None:
			isList = True
		if not sys.stdin.isatty():
			if isText:
				self.value = ''
				for x in sys.stdin.readlines():
					self.value+=x
				if not type(isText) is bool:
					self.value = self.clean( self.value )

			elif isList:
				if type(isList) == str and isList == 'raw':
					self.value = sys.stdin.readlines()
				else:
					self.value = self.clean( sys.stdin.readlines(), clean=isList )

		else:
			self.value = None

		self.size = _.get_size(self.value)
		_matrix.app.totalMemory()
		return _matrix.app.algorithmResult( algorithm, result=self.value )

	def single( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.clear()
		self.status = True
		
		return _matrix.app.algorithmResult( algorithm, result=self.id )




	def singleSet( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.status = True
		self.set( data )
		self.singeSet = True
		_matrix.app.algorithmResult( algorithm, result=None )

	def singleGet( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		
		if self.singeSet:
			self.singeSet = False
			val = self.value

			if not val is None:
				self.clear()

			return _matrix.app.algorithmResult( algorithm, result=val )

		elif not self.singeSet:
			return _matrix.app.algorithmResult( algorithm, result=None )

	def singleGetWait( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		while not self.singeSet:
			pass
		val = self.value
		self.singeSet = False
		self.clear()
		
		return _matrix.app.algorithmResult( algorithm, result=val )





