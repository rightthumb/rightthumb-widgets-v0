class srv():

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

	def __init__( self, server, username, password, folder=None ):
		self.ftp = FTP( server, username, password )
		if not folder is None:
			self.dir( folder )
	
	def dir( folder ):
		self.ftp.cwd( folder )

	def up( file, folder ):
		pass

	def down( file, folder ):
		pass

	def ls():
		pass




