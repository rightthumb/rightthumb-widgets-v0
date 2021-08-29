class srv():
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


