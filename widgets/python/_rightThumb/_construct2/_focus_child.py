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

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.record = None
		self.add( theID, registration )


	def add( self, theID, registration ):
		__.app.algorithmRegister( 'ext', 'add' )
		self.ids.append( theID )
		self.name = registration['name']
		self.focus = registration['focus']

	def unregister( self ):
		__.app.algorithmRegister( 'ext', 'unregister' )
		for key in __.app.records['data'].keys():
			if self.name in __.app.records['data'][key].focus:
				__.app.records['data'][key].unregister()
	
	def register( self, data ):
		__.app.algorithmRegister( 'ext', 'register' )
		self.record = data
		return self.id

	def profile( self ):
		if not self.record is None and type(self.record) == dict:
			__.app.algorithmRegister( 'ext', 'profile', result=True )
			return self.record
		else:
			__.app.algorithmRegister( 'ext', 'profile', result=False )
			return None
	
	def columns( self ):
		if not self.record is None and type(self.record) == dict and 'columns' in self.record.keys():
			__.app.algorithmRegister( 'ext', 'columns', result=True )
			return self.record['columns']
		else:
			__.app.algorithmRegister( 'ext', 'columns', result=False )
			return None


