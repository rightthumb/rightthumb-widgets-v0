import _rightThumb._matrix as _matrix
import time

thisChildApp = _matrix.GenChildLabel.gen( __file__ )

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.auto = None
		self.description = ''
		self.add( theID, registration )

	def callers( self, trackingID=None ):_.printVar( _matrix.app.algorithmRegister(trackingID=trackingID) );

	def add( self, theID, registration ):
		algorithm = _matrix.app.algorithmRegister(trackingID=registration['trackingID'])
		self.ids.append( theID )
		self.focus = registration['focus']
		self.name = registration['name']
		self.hashID = registration['hashID']

		self.description = registration['description']


		if registration['isIF']:
			self.auto = _matrix.app.ifSet

		if 'activity' in registration.keys():
			try:
				self.auto = _matrix.app.ifSetAction[  registration['activity']  ]
			except Exception as e:
				pass

		# if registration['isIF']:
		# 	print()
		# 	for x in self.auto:
		# 		print( x )
		# 	print()
		# 	return True
		_matrix.app.algorithmResult( algorithm, result=None )



		