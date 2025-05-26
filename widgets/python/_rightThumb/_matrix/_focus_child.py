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

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.record = None
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );

	def add( self, theID, registration ):
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		_matrix.app.algorithmRegister()
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']
		_matrix.app.algorithmResult( algorithm, result=None )

	def unregister( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		# _.pr('self.name',self.name)
		for key in _matrix.app.records['data'].keys():
			if self.name in _matrix.app.records['data'][key].focus:
				# _.pr(' found  found  found  found  found  found  found  found  found  found  found  found  found ')
				_matrix.app.records['data'][key].unregister()
			if self.name in _matrix.app.records['data'][key].live:
				# _.pr(' found  found  found  found  found  found  found  found  found  found  found  found  found ')
				_matrix.app.records['data'][key].unregister()
		try:
			for key in _matrix.app.records['ext'].keys():
				# _.pr( "_matrix.app.records['ext'][key].app", _matrix.app.records['ext'][key].app, self.name )
				if self.name in _matrix.app.records['ext'][key].app:
					_matrix.app.records['ext'][key].unregister()
		except Exception as e:
			pass


		# _.colorThis( [ self.name, '_matrix.app.memory_max', _.formatSize(_matrix.app.memory_max) ], 'yellow' )
		_matrix.app.algorithmResult( algorithm, result=None )
	
	def register( self, data, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		self.record = data
		return _matrix.app.algorithmResult( algorithm, result=self.id )

	def profile( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		if not self.record is None and type(self.record) == dict:
			return _matrix.app.algorithmResult( algorithm, result=self.record )
		else:

			return _matrix.app.algorithmResult( algorithm, result=None )
	
	def columns( self, trackingID=None ):
		algorithm = _matrix.app.algorithmRegister(trackingID=trackingID)
		

		if not self.record is None and type(self.record) == dict and 'columns' in self.record.keys():
			_matrix.app.algorithmRegister( result=True )
			return _matrix.app.algorithmResult( algorithm, result=self.record['columns'] )
		else:
			_matrix.app.algorithmRegister( result=False )
			return _matrix.app.algorithmResult( algorithm, result=None )



