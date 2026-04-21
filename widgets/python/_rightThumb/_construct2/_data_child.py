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
import sys

class TheChild:
	def __init__( self, theID, registration ):
		self.id = theID
		self.ids = []
		self.registration = registration
		self.name = None
		self.value = None
		self.status = True
		self.add( theID, registration )
		self.size = 0
		self.singeSet = False

	def add( self, theID, registration ):
		__.app.algorithmRegister( 'data', 'add' )
		self.ids.append( theID )
		self.name = registration['name']
		# _.colorThis(  [ self.name ], 'yellow'  )
		self.value = registration['value']
		self.focus = registration['focus']
		self.size = _.get_size(self.value)
		__.app.memory += self.size
		

	def unregister( self ):
		_.colorThis(  [ 'unregister:', self.name, self.size, __.app.memory-self.size ], 'yellow'  )
		self.status = False
		self.value = None
		__.app.memory -= self.size

	def clear( self ):
		self.set( None )
		self.status = False
		self.singeSet = False


	def set( self, data ):
		self.status = True
		self.value = data
		__.app.memory -= self.size
		self.size = _.get_size(self.value)
		__.app.memory += self.size

		# _.pr('set',self.value)

	def get( self ):
		# _.pr('get')
		return self.value

	def clean( self, data ):
		newData = []
		for x in data:
			x = x.replace( '\n', '' )
			x = x.replace( '\r', '' )
			newData.append( x )
		return newData


	def pipe( self ):
		if not sys.stdin.isatty():
			self.value = self.clean( sys.stdin.readlines() )
			self.size = _.get_size(self.value)
			__.app.memory += self.size
		else:
			self.value = None

	def single( self ):
		self.clear()
		self.status = True
		return self.id



	def singleSet( self, data ):
		self.status = True
		self.set( data )
		self.singeSet = True

	def singleGet( self ):
		if self.singeSet:
			self.singeSet = False
			val = self.value

			if not val is None:
				self.clear()

			return val

		elif not self.singeSet:
			return None

	def singleGetWait( self ):

		while not self.singeSet:
			pass
		val = self.value
		self.singeSet = False
		self.clear()
		return val





