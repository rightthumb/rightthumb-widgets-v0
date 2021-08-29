import os, sys
import _rightThumb._base3 as _
import xtarfile

class dot:
	def __init__(self):
		pass

def isGz(filepath):
	if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '1F 8B 08 08' ):
		return True
	else:
		return False

def isBz2(filepath):
	if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '42 5A 68' ):
		return True
	else:
		return False


isTar = dot()
isTar.gz = isGz
isTar.bz2 = isBz2
def tar( files, tarball=None, gz=False, ext=None  ):
	# print(type(files),files)
	if type(files) is str:
		# print('here')
		files = [files]
	if gz:
		ext = '.tar.gz'
		w = 'gz'
	else:
		ext = '.tar.bz2'
		w = 'bz2'
	# if _.switches.isActive('NoExt'):
	# 	ext = ''
	# 	w = 'bz2'
	tarball = None
	if not tarball is None:
		tarball = tarball
	once=False
	hasAction = False
	# print(files)
	for i,path in enumerate( files ):
		if not type(path) == str:
			path = path[0]
			files[i] = path
		# if type(path) == list:
		# 	path = path[0]
		# 	files[i] = path
		# print(type(path), path)
		# sys.exit()
		if not os.path.isdir(path) and not _.isTar.gz(path) and not _.isTar.bz2(path):
			hasAction = True

	if hasAction and not tarball is None:
		tar = xtarfile.open( tarball, 'w:'+w )

	for i,path in enumerate( files ):
		aa = os.stat( path ).st_size
		print( _.formatSize( aa ) )
		# print('here')
		# print(path)
		if os.path.isdir(path):

			# print('here')
			if tarball:
				folder( path, tarball )
			else:
				folder( path )
		else:
			if not once:
				once = True
				if tarball:
					tar = xtarfile.open( tarball, 'w:'+w )

			if tarball:
				tar.add(path)
			else:
				tar = xtarfile.open( path+ext, 'w:'+w )
				tar.add(path)
				tar.close()
				bb = os.stat( path+ext ).st_size
				print( _.formatSize( bb ) )
				print( str(_.percentageDiffCalc( aa, bb ))+'%' )
				print( _.formatSize(aa-bb) )
				if _.switches.isActive('NoExt'):
					os.unlink( path )
					os.rename( path+ext, path )

	if once and len(_.switches.value('Compress')):
		tar.close()
		bb = os.stat( _.switches.values('Compress')[0] ).st_size
		print( _.formatSize( bb ) )
		print( str(_.percentageDiffCalc( aa, bb ))+'%' )
		print( _.formatSize(aa-bb) )


def untar( files ):
	for i,path in enumerate( files ):
		if path.endswith('.bz2'):
			ext = 'bz2'
		elif path.endswith('.gz'):
			ext = 'gz'
		else:
			ext = 'bz2'
		try:
			tar = xtarfile.open( path , 'r:'+ext )
			tar.extractall()
			tar.close()

		except Exception as e:
			uncompress_folder(path)

def uncompress_folder(path):
	tar = xtarfile.open(path)
	for member in tar.getmembers():
		print( "Extracting %s" % member.name )
		tar.extract(member, path=path.replace('.tar.bz2',''))




def folder( fromPath, toPath=None, gz=False ):
	if gz:
		ext = '.tar.gz'
		w = 'gz'
	else:
		ext = '.tar.bz2'
		w = 'bz2'
	if toPath is None:
		toPath = fromPath+ext
	with xtarfile.open( toPath, 'w:'+w ) as tar:
		tar.add(fromPath, arcname=os.path.basename(fromPath))


def list(files):
	for path in files:
		tar = xtarfile.open(path,'r:bz2')
		print( tar.list() )
		tar.close()