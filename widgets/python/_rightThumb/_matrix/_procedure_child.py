import _rightThumb._matrix as _matrix
import _rightThumb._base3 as _
import time

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );


	def add( self, theID, registration ):
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']

		_matrix.app.algorithmResult( algorithm, result=None )

