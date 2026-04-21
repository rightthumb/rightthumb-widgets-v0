import sys

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
import time
import _rightThumb._construct as __
import _rightThumb._vars as _v
try:
	import simplejson
	json = simplejson
except:
	pass
try:
	import json
except ImportError:
	print('no json')

__.dictProfile_fields = []

class Profile:

	def __init__( self, name, asset, appReg ):
		self.appReg = appReg
		self.name = name
		self.asset = asset
		self.profile = {}

		self.multiType = False
		self.samples = 1
		self.type = False
		self.types = []

		self.dictProfile = False
		self.dictProfiles = []

		self.length = False
		self.lengths = []

		self.mem = False
		self.mems = []

		self.dKey = False
		self.dKeys = []

		self.first = True


	def audit( self ):
		profile = self.initialize()
		length = 0
		mem = 1



		if 'socket' in str(type( self.asset )).lower() and 'ssl' in str(type( self.asset )).lower()  :
			thisType = 'SSL_Socket'
		elif 'socket' in str(type( self.asset )).lower():
			thisType = 'Socket'
		elif type( self.asset ) == bool:
			thisType = 'bool'
		elif type( self.asset ) == tuple:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'tuple'
			length = len( self.asset )
		elif type( self.asset ) == list:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'list'
			length = len( self.asset )
			if length:
				if type( self.asset[0] ) == dict:
					thisType = 'list_dics'



		elif type( self.asset ) == int:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'int'
			length = len( str(self.asset) )
		elif type( self.asset ) == float:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'float'
			length = len( str(self.asset) )
		elif type( self.asset ) == str:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'str'
			length = len( self.asset )
		elif type( self.asset ) == complex:
			thisType = 'complex'
		elif type( self.asset ) == dict:
			mem = sys.getsizeof( str( self.asset ) )
			thisType = 'dict'
		elif self.asset is None:
			thisType = 'None'

		elif 'class' in str(type( self.asset )):
			saveTable( self.asset.__dict__, 'profileVariables_temp.json' )
			newData = getTable( 'profileVariables_temp.json' )
			self.asset = newData
			return self.audit()



		# print( type( self.asset ) )


		self.addType( thisType )
		dictProfile = False
		if thisType == 'dict' or thisType == 'list_dics' :
			if thisType == 'dict':
				if self.hasKeys( self.asset ):
					try:
						dictProfile = processRows( [ self.asset ] )
					except Exception as e:
						dictProfile = False
				else:
					dictProfile = False
			else:
				if self.hasKeys( self.asset[0] ):
					try:
						dictProfile = processRows( self.asset )
					except Exception as e:
						dictProfile = False
				else:
					dictProfile = False
		
		

		if len( __.dictProfile_fields ):
			self.addKeys( __.dictProfile_fields )
			if thisType == 'dict':
				length = len( __.dictProfile_fields )
			else:
				length = [ length, len( __.dictProfile_fields ) ]
			self.addDictProfile( dictProfile )


		self.addLength( length )
		self.addMem( mem )


		# self.asset = None
		
		self.profile = self.initialize()
		return self.profile

	def addKeys( self, data ):
		if type( self.dKey ) == bool:
			self.dKey = data
		elif not len(self.dKeys):
			if not self.dKey == data:
				self.dKeys.append( self.dKey )
				self.dKeys.append( data )
				self.dKey = data
		else:
			self.dKeys.append( data )
			self.dKey = data

	def addMem( self, data ):
		if type( self.mem ) == bool:
			self.mem = data
		elif not len(self.mems):
			self.mems.append( self.mem )
			self.mems.append( data )
		else:
			self.mems.append( self.mem )


	def addLength( self, data ):
		if type( self.length ) == bool:
			self.length = data
		elif not len(self.lengths):
			self.lengths.append( self.length )
			self.lengths.append( data )
		else:
			self.lengths.append( self.length )

	def addDictProfile( self, data ):
		if self.hasKeys( self.dictProfile ):
			self.first = False

		if not self.hasKeys( self.dictProfile ):
			self.dictProfile = data
		else:
			found = False
			for row in self.dictProfiles:
				if row == data:
					found = True
			if not found:
				self.dictProfiles.append( data )
			self.dictProfile = data




	def addType( self, thisType ):
		
		if type( self.type ) == bool:
			self.type = thisType
		else:
			if len( self.types ):
				same = True
				for row in self.types:
					if not row == thisType:
						same = False
						self.multiType = True
				if not same:
					self.types.append( thisType )
					self.type = thisType
			else:
				if not self.type == thisType:
					self.types.append( self.type )
					self.types.append( thisType )
					self.type = thisType





	def prep( self ):
		if not self.hasKeys( self.profile ):
			self.profile = self.initialize()


	def initialize( self ):
		profile = {
							'name': self.name,
							'epoch': time.time(),
							'type': self.type,
							'types': self.types,
							'multi': self.multiType,
							'mem': self.mem,
							'mems': self.mems,
							'length': self.length,
							'lengths': self.lengths,
							'dKey': self.dKey,
							'dKeys': self.dKeys,
							'dicProfiles': self.dictProfiles,
							'dicProfile': self.dictProfile,
		}

		return profile


	def hasKeys( self, data ):
		if not type(data) == dict:
			return False
			
		if len( data.keys() ):
			return True
		else:
			return False





class Variable_Profiles:

	def __init__( self ):
		self.profiles = []
		self.appReg = __.appReg

	def audit( self, name, asset, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		found = False
		thisID = False
		for i,t in enumerate(self.profiles):
			if self.profiles[i].name == name and self.profiles[i].appReg == appReg:
				found = True
				if len(asset) > 0:
					self.profiles[i].asset = asset
					return self.profiles[i].profile()
		if not found:
			i = len(self.profiles)
			self.profiles.append(Profile( name, asset, appReg ))
			return self.profiles[i].audit()

	def getAsset( self, name, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		for i,t in enumerate(self.profiles):
			print( self.profiles[i].name, name )
			if self.profiles[i].name == name:
			# if self.profiles[i].name == name and self.profiles[i].appReg == appReg:
				return self.profiles[i].asset

		return None


records = Variable_Profiles()


def processDic( rows, thisDic, parent=[]):
	
	

	fields = []
	for tK in thisDic.keys():

		if thisDic[tK] == 'dic':
			__.dictProfile_fields.append({ 'type': thisDic[tK], 'field': tK, 'parent': parent })
			# newParent = list(tuple(parent))
			try:
				if type(rows[tK]) == dict:
					dicRow = []
					dicRow.append(rows[tK])
				newParent = list(tuple(parent))
				newParent.append( str(tK) )
				fields.append({'type': thisDic[tK], 'field': tK, 'parent': parent, 'zChildren': processRows(dicRow, newParent)})
			except Exception as e:
				try:
					newParent = list(tuple(parent))
					newParent.append( str(tK) )
					fields.append({'type': thisDic[tK], 'field': tK, 'parent': parent, 'zChildren': processRows(rows[0][tK], newParent)})
				except Exception as e:
					fields.append({'type': thisDic[tK], 'field': tK, 'parent': parent })
		elif thisDic[tK] == 'multidimensional' or thisDic[tK] == 'list':
			__.dictProfile_fields.append({ 'type': thisDic[tK], 'field': tK, 'parent': parent })
			try:
				try:
					newParent = list(tuple(parent))
					newParent.append( str(tK) )
					fields.append({'type': thisDic[tK]+'1', 'field': tK, 'parent': parent, 'zChildren': processRows(rows[0][tK], newParent)})
				except Exception as e:
					# print('dic')
					newParent = list(tuple(parent))
					newParent.append( str(tK) )
					fields.append({'type': thisDic[tK]+'2', 'field': tK, 'parent': parent, 'zChildren': processRows(rows[tK], newParent)})
					# print('dic')
			except Exception as e:
				# try:
				#     print(rows[0][tK])
				# except Exception as e:
				#     pass
				# print(rows[0][tK])
				# print(tK)


				
				# if 'date_test' in tK:
				#     print("'"+tK+"'")
				#     print('it was found')
				#     print(rows)
				#     # fields.append({'type': thisDic[tK]+'3', 'field': tK, 'zChildren': processRows2(rows[0][tK])})
				#     print('done')
				#     sys.exit()
				# else:
				#     fields.append({'type': thisDic[tK]+'3', 'field': tK})
				fields.append({'type': thisDic[tK]+'3', 'field': tK, 'parent': parent })
		else:
			__.dictProfile_fields.append({ 'type': thisDic[tK], 'field': tK, 'parent': parent })
			fields.append({'type': thisDic[tK], 'field': tK, 'parent': parent })
	# print(fields)
	return fields



def processRows( rows, parent=[] ):
	jsonKeys = {}
	# print('yes')
	# if type(rows) == list:
		# rows = rows[0]
	# print(type(rows))
	if type(rows) == dict:
		# print(rows)
		# print('dic')
		# print(rows)
		# print('dic')
		for i,kS in enumerate(rows.keys()):
			if i == 0:
				pass
				# print(kS,type(rows[kS]))
			try:
				try:
					float(rows[kS])
				except Exception as e:
					int(rows[kS])
				if i == 0:
					jsonKeys[kS] = 'int'
			except Exception as e:
				if len(kS) > 0:
					jsonKeys[kS] = variableType(rows[kS])
			if jsonKeys[kS] == 'int' and isDate(rows[kS]):
				jsonKeys[kS] = 'date'
			if type(rows[kS]) == list:
				try:
					if len(jsonKeys[kS][0].keys()) > 0:
						jsonKeys[kS] = 'multidimensional'
					else:
						jsonKeys[kS] = 'list'
				except Exception as e:
					jsonKeys[kS] = 'list'
	else:
		for  i,jN in enumerate(rows):
			# print(jN)

			try:
				for kS in jN.keys():
					if i == 0:
						pass
						# print(kS,type(jN[kS]))
					try:
						int(jN[kS])
						if i == 0:
							jsonKeys[kS] = 'int'
					except Exception as e:
						if len(kS) > 0:
							jsonKeys[kS] = variableType(jN[kS])
					if jsonKeys[kS] == 'int' and isDate(jN[kS]):
						jsonKeys[kS] = 'date'
					if type(jN[kS]) == list:
						try:
							if len(jsonKeys[kS][0].keys()) > 0:
								jsonKeys[kS] = 'multidimensional'
							else:
								jsonKeys[kS] = 'list'
						except Exception as e:
							jsonKeys[kS] = 'list'
					if type(jN[kS]) == dict:
						jsonKeys[kS] = 'dic'
						# print(jN[kS])
				pass
			except Exception as e:
				# print(rows)
				try:
					try:
						float(jN[i])
					except Exception as e:
						int(jN[i])
					jsonKeys[i] = 'int'
				except Exception as e:
					try:
						jN[i]
						jsonKeys[i] = variableType(jN[i])
					except Exception as e:
						pass
				try: ###
					if jsonKeys[i] == 'int' and isDate(jN[i]):
						jsonKeys[i] = 'date'
				except Exception as e:
					pass
	return processDic( rows, jsonKeys, parent )

def isDate(n):
	try:
		try:
			n = int(n)
		except Exception as e:
			n = float(n)
		test = cal_days_diff(n)
		if test < 7000:
			result = True
		else:
			result = False
	except Exception as e:
		result = False
	return result



def getTable( theFile, tableTemp=False, printThis=False ):
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
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
	else:
		json_data = []
	return json_data


def saveTable( rows, theFile, tableTemp=False, printThis=False, indentCode=True, sort_keys=False ):
	# defaults to myTables
	p = ''
	if not tableTemp:
		file0 = _v.myTables + _v.slash + theFile
		p = theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
		p = file0
	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = json.dumps(rows)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + p, 'blue')
	return file0


def variableType( asset ):
	if 'socket' in str(type( asset )).lower() and 'ssl' in str(type( asset )).lower()  :
		thisType = 'SSL_Socket'
	elif 'socket' in str(type( asset )).lower():
		thisType = 'Socket'
	elif type( asset ) == bool:
		thisType = 'bool'
	elif type( asset ) == tuple:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'tuple'
		length = len( asset )
	elif type( asset ) == list:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'list'
		length = len( asset )
		if length:
			if type( asset[0] ) == dict:
				thisType = 'list_dics'



	elif type( asset ) == int:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'int'
		length = len( str(asset) )
	elif type( asset ) == float:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'float'
		length = len( str(asset) )
	elif type( asset ) == str:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'str'
		length = len( asset )
	elif type( asset ) == complex:
		thisType = 'complex'
	elif type( asset ) == dict:
		mem = sys.getsizeof( str( asset ) )
		thisType = 'dict'
	elif asset is None:
		thisType = 'None'

	elif 'class' in str(type( asset )):
		thisType = 'class'

	return thisType



