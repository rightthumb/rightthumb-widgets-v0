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

import time

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.auto = None
		self.description = ''
		self.add( theID, registration )



	def add( self, theID, registration ):
		__.app.algorithmRegister( 'process', 'add' )
		self.ids.append( theID )
		self.description = registration['description']
		self.focus = registration['focus']


		if registration['isIF']:
			self.auto = __.app.ifSet

		if 'activity' in registration.keys():
			try:
				self.auto = __.app.ifSetAction[  registration['activity']  ]
			except Exception as e:
				pass

		if registration['isIF']:
			print()
			for x in self.auto:
				print( x )
			print()
			return True

