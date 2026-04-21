import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import simplejson as json

import _rightThumb._construct as __
import _rightThumb._matrix as _matrix
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._profileVariables as _profile

class table:

	def save( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,    p=1   ):

		if k or s:
			sort_keys = True

		if not p:
			printThis = False


		# defaults to myTables
		px = ''
		if theFile.startswith('temp'+_v.slash):
			theFile = theFile.replace( 'temp'+_v.slash, '' )
			file0 = _v.stmp + _v.slash + theFile
			px = file0
		else:
			if not tableTemp:
				file0 = _v.myTables + _v.slash + theFile
				px = theFile
			else:
				file0 = _v.stmp + _v.slash + theFile
				px = file0

		if indentCode:
			dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
		else:
			dataDump = json.dumps(rows)
		
		if archive:
			import _rightThumb._md5 as _md5

			theFileLabel = theFile
			if _v.slash in theFileLabel:
				global appInfo
				tfl = theFileLabel.split(_v.slash)
				tfl.reverse()
				theFileLabel = str(appInfo[_matrix.appReg]['liveAppName']) + '__' + tfl[0]
			theFileLabel = theFileLabel.replace( '.json', '' )
			theFileLabel = theFileLabel.replace( '.JSON', '' )

			lastMD5 = None
			if os.path.isfile( file0 ):
				lastMD5 = _md5.md5File( file0 )

				backupFile = _v.stmp + _v.slash+'__archive_temp__' + theFileLabel + '__' + genUUID() + '.json'
				

		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()

		if archive:
			shouldDocument = False

			if os.path.isfile( file0 ):
				thisMD5 = _md5.md5File( file0 )
			if lastMD5 is None:
				shouldDocument = True
			else:
				if not lastMD5 == thisMD5:
					shouldDocument = True

			if not shouldDocument:
				if os.path.isfile( backupFile ):
					os.remove( backupFile )
			
			if shouldDocument:
				md5Table = getTable( 'table_archive_log.json' )
				found = False
				for i,record in enumerate(md5Table):
					if theFileLabel == record['name']:
						found = True

				theFileLabel
				theFile
				fileDate( theData )


		if printThis:
			printBold('Saved: ' + px, 'blue')
		return file0



	def get( theFile, tableTemp=False, printThis=False,     isDic=None, isList=None ):

		if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
			isDic = True

		# defaults to myTables
		if not type( tableTemp ) == bool:
			if tableTemp == 'split':
				file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
		else:
			if tableTemp == True:
				file0 = _v.stmp + _v.slash + theFile
			else:
				file0 = _v.myTables + _v.slash + theFile

		if printThis:
			print('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			# import bigjson
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = json.load(json_file)
			# with open( file0, 'rb' ) as f:
				# json_data = bigjson.load(f)
				# json_data = bigjson.load(json_file)
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)

		else:
			if isDic is None and isList is None:
				json_data = []
			if isDic:
				json_data = {}
			if isList:
				json_data = []
		return json_data

	def get2( theFile,     isDic=None, isList=None ):
		if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
			isDic = True
		if os.path.isfile(theFile) == True:
			with open(theFile,'r', encoding="latin-1") as json_file:
				json_data = json.load(json_file)
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
			return json_data
		else:
			if isDic is None and isList is None:
				return []
			if isDic:
				return {}
			if isList:
				return []


	def save2( rows, theFile, printThis=False, sort_keys=False, indentCode=True ):
		# print('*******************',theFile)
		if theFile.startswith('temp'+_v.slash):
			theFile = theFile.replace( 'temp'+_v.slash, '' )
			theFile = _v.stmp + _v.slash + theFile

		if indentCode:
			dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
		else:
			dataDump = json.dumps(rows)

		# dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
		f = open(theFile,'w')
		f.write(str(dataDump))
		f.close()
		if printThis:
			print('Saved: ' + theFile)

class tableDB:

	def get( theFile,     isDic=None, isList=None ):

		if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
			isDic = True

		theFile = _v.dbTables + _v.slash + theFile
		if os.path.isfile(theFile) == True:
			with open(theFile,'r', encoding="latin-1") as json_file:
				json_data = json.load(json_file)
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
			return json_data
		else:
			if isDic is None and isList is None:
				return []
			if isDic:
				return {}
			if isList:
				return []

	def save( rows, theFile, printThis=False, sort_keys=False, indentCode=True ):
		# print('*******************',theFile)
		theFile = _v.dbTables + _v.slash + theFile

		if indentCode:
			dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
		else:
			dataDump = json.dumps(rows)

		# dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
		f = open(theFile,'w')
		f.write(str(dataDump))
		f.close()
		if printThis:
			print('Saved: ' + theFile)


