#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import _rightThumb._construct as __
import _rightThumb._base3 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import os, sys, time, random

class dot:
	def __init__( self ):
		pass





class FILES:
	def __init__( self ):
		self.records = None
		self.statusCache = None
		self.statusCacheChanged = False
		self.recordsChanged = False
	
	def load( self ):
		if self.records is None:
			self.records = _.getTableDB( 'meta-files.hash' )


	def save( self ):
		if self.recordsChanged:
			_.saveTableDB( self.records, 'meta-files.hash' )
		if self.statusCacheChanged:
			_.saveTable( self.statusCache, 'meta-files-status.hash' )

	def register( self, path,  ):

	def path( self, path, s=False, p=False ):
		if not p and not s:
			if os.path.isfile(path):
				return _v.sanitizeFolder(path)
			else:
				return _v.resolveFolderIDs(path)
		elif p:
			return _v.resolveFolderIDs(path)
		elif s:
			return _v.sanitizeFolder(path)

	def open( self, path ):
		path = self.path(path,p=1)
		san = self.path(path,s=1)
		meA = os.path.getmtime( path )
		if _.isCrypt(path):
			_vault.f.de( path )
		if _.isTar.bz2( path ):
			_tar.untar( [path] )
		if _.isCrypt(path):
			_vault.f.de( path )
		if _.isTar.bz2( path ):
			_tar.untar( [path] )
		
		meB = os.path.getmtime( path )
		if not maA == meB:
			_.changeM(meA)
		md5 = _hash.file( file )
		if not san in self.records:
			self.recordsChanged = True
		if not self.records[san]['md5'] == md5:
			self.recordsChanged = True


	def close( self, path ):
		path = self.path(path,p=1)
		san = self.path(path,s=1)
		meA = os.path.getmtime( path )
		if not san in self.records:
			return None
		




		if 'crypt' in self.records[san]:
			crypt = True
			isCrypt = _.isCrypt(path)
		
		if crypt and isCrypt:
			return None


		zipp = False
		if 'zip' in self.records[san]:
			if self.records[san]['zip']:
				zipp = True

		if not zipp and 'zip-size' in self.records[san]:
			b = os.stat( path ).st_size
			if b >= self.records[san]['zip-size']:
				zipp = True
		
		if zipp:
			isZip = _.isTar.bz2(path)

		crypt = False




		meB = os.path.getmtime( path )
		if not maA == meB:
			_.changeM(meA)

	def status( self, path ):
		if self.statusCache is None:
			self.statusCache = _.getTable( 'meta-status.hash' )
		if __.path(path) in self.statusCache:
			if self.statusCache[__.path(path)]:
				return True
			else:
				return False
		try:
			" ".join(['{:02X}'.format(byte) for byte in     open( path , 'rb' ).read(32)    ])
		except Exception as e:
			self.statusCacheChanged = True
			self.statusCache[ __.path(path) ] = 0
			_.saveTable( self.statusCache, 'meta-files-status.hash' )
			return False
		self.statusCache[ __.path(path) ] = 1
		self.statusCacheChanged = True
		return True



		
files = FILES()
def done():
	global files
	files.save()

__.onExit(done)

appReg = __.appReg
import _rightThumb._vault as _vault
import _rightThumb._tar as _tar
import _rightThumb._md5 as _hash
__.appReg = appReg
del appReg



