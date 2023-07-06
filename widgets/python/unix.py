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

import os
import sys
import time
import _rightThumb._vars as _v
# from shutil import copyfile

def getText( theFile ):
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	result = ''
	if type(lines) == list:
		for x in lines:
			result += x
	elif type(lines) == str:
		result = lines

	return result



def saveText( rows, theFile, errors=True ):
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
  

		if type(rows) == str:
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		open(theFile, 'wb').write(rows)
		if errors:
			print( 'Auto correction when saving text' )
if os.name == 'nt':
	slash = _v.slash
else:
	slash = '/'
from pathlib import Path
import _rightThumb._string as _str
home = str(Path.home())
fileName = home + slash+'.tk421'
if os.name == 'nt':
	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write('C')

	techDrive = open( fileName, 'r' ).read()
	techDrive = _str.totalStrip(techDrive)

elif os.name == 'posix':
	fileName = fileName.replace( _v.slash, slash )

	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write(home)

	techDrive = open( fileName, 'r' ).read()


# print(srcfolder)
# sys.exit()
def buildFolders( path ):
	global slash
	folder = path
	parts = folder.split( slash )
	parts.pop()

	newParts = []

	for p in parts:

		newParts.append( p )
		f = slash.join( newParts )

		if os.name == 'posix':
			if not f.startswith(slash):
				f = slash+f
		# print(f)
		exist = os.path.isdir( f )
		if not exist:
			try:
				# print(f)
				os.mkdir( f )
			except Exception as e:
				pass


def process( path ):
	global srcfolder
	global slash
	# if 'dirX' in path:
	data = getText( path )
	data = data.replace( _v.slash+_v.slash, '/' )
	data = data.replace( '4FD4030911', _v.slash+_v.slash )
	# data = data.replace( "/'", "'+_v.slash" )
	# data = data.replace( "'/'+_v.slash", "'/'" )
	# data = data.replace( '/'+_v.slash, '/' )

	path2 = path.replace( _v.python['src']['windows'],  _v.python['src']['unix'] )
	buildFolders( path2 )
	saveText( data, path2 )
	print(path)
	# print(data)
	# print(path2)




def getFolder(folder):
	global slash
	try:
		dirList = os.listdir(folder)
		takeAction = True
	except Exception as e:
		takeAction = False
	if takeAction:
		if os.path.isdir(folder):
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + slash + item
			path = path.replace(slash+slash,slash)
			if os.path.isfile(path):
				# print(path)
				if path.endswith('.py'):
					process( path )

			if os.path.isdir(path):
				newFolder = folder + slash + item
				if os.path.isdir(newFolder):
					try:
						getFolder(newFolder)
					except Exception as e:
						pass

def action():
	global srcfolder
	global slash


	print(srcfolder)
	getFolder(srcfolder)

			# copyfile(path, folder+'_unix')

techDrive = techDrive.replace('\n','').replace('\r','')
srcfolder = _v.python['src']['windows']

if __name__ == '__main__':
	action()


