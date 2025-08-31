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

import sys
import time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._md5 as _md5
##################################################
import pickle
##################################################

def appSwitches():
	pass
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '_rightThumb._auditCodeBase',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Audit code in multiple languates',
	'categories': [
						'audit',
						'code',
						'validator',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'import this',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],

	}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
				'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
				'table': {'sent': [], 'received': [] }, 
	},
	}

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
	_.defaultScriptTriggers()
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# START

class Validator:

	def __init__( self ):
		pass

	def register( self, asset, language, project=None ):
		if not project is None:
			__.objectPath = project
		self.logistics = _.getTable( 'auditCodeBase.json' )

		self.asset = asset

		self.language = language
		self.stringDelim = '-B248-'

		self.inlineComments = []
		self.multilineComments = []
		self.locationTable = []
		self.relevantTable = { 'char': [], 'multi': [], 'records': [] }
		self.tickets = {}
		self.omitRanges  = []
		self.idCache = []
		self.idOmitCache = []



	def dump(self):
		self.projectFile
		with open( objFile()  , 'wb') as objSelf:
			pickle.dump(self, objSelf, pickle.HIGHEST_PROTOCOL )
		_.printBold( 'Saved: ' + objFile(), 'green' )


	def auditOmit( self ):
		result = ''
		for i in self.idOmitCache:
			char = self.asset[i]
			result += char
		_.pr( result )



	def printPos( self, start, end, p=True ):
		if p:
			_.pr( 'diff:', end-start )
			_.pr( '__________________________' )
		theEnd = len(self.asset) - (  end )
		payload = self.asset[ start :-theEnd ]
		if p:
			_.pr( 'payload:' )
			_.printBold( payload )
			_.pr( '__________________________' )
		return payload
	def process( self ):

		self.idCache = []
		a = len(self.asset)
		i = 0
		while not a == len(self.idCache):
			self.idCache.append( i )
			i+=1
		

		self.buildRelevantTable( comment=True )
		self.buildLocationTable()
		self.omitTickets()
		self.buildIDCache()

		self.buildRelevantTable( quote=True )
		self.buildLocationTable()        
		self.omitTickets()
		self.buildIDCache()

		self.buildRelevantTable()
		self.buildLocationTable()
		_.pr( 'closed:', len(self.locationTable) )
		_.saveTable( self.tickets, 'auditCodeBase_errors.json' )
		self.dump()



	def createIndex( self, asset, language='global', skipLoad=False, simple=False, A=None, B=None ):

		if A is None and B is None:
			self.index_process = 'A'
		elif not A is None:
			self.index_process = 'A'
		elif not B is None:
			self.index_process = 'B'



		self.isSimple = simple
		self.logistics = _.getTable( 'auditCodeBase.json' )
		self.backupLoaded = { 'attempted': False, 'indexes': False, 'validation': False, 'profile': False }



		if not len( asset ):
			_.pr( 'No Data' )
			return []

		self.asset = asset
		self.language = language
		self.skipLoad = skipLoad

		self.individualIndexes  = []
		self.flat = {}
		self.omitIndex  = []
		self.indexes = { 'char': [], 'group': [], }
		self.validation = {}
		self.profile = {}

		self.MD5 = _md5.md5( self.asset )
		self.projectFile = 'auditCodeBase_MD5_' + self.MD5 + '_PROJECT.json'
		__.validator_Project = self.MD5

		try:
			self.rlID
		except Exception as e:
			self.rls = {}
			self.rlID = 0
			# _.colorThis( [ 'self.rlID: set to 0' ], 'red' )



		# _.colorThis( [  'Project:', self.projectFile.replace( 'PROJECT', 'indexes' ) ], 'green' )


		# _.pr( self.asset )
		# sys.exit()\

		
		if not self.skipLoad:
			self.loadProject()
			# loadProject()
			# self.lookupChars()
		


		if not self.backupLoaded['indexes']:
			self.buildIndexes()
			self.saveProject()


		# _.printVar( self.indexes['totals'] )

		return self.indexes

	def filePath( self ):
		_.pr( self.projectFile.replace( 'PROJECT', 'indexes' ) )
		_.pr( self.projectFile.replace( 'PROJECT', 'validation' ) )

	def lookupChars( self ):

		_.pr( '"', ord('"') )
		_.pr()

		for i,char in enumerate(self.asset):
			_.pr( char, ord( char ) )


		sys.exit()

	def colorPrint( self ):
		# {6402B9BC-FF5C-4B6F-B8B4-CB1EFADDF405}

		# index = self.query( "'", justIndex=False, isGroup=True )
		# _.pr( index )
		# sys.exit()
		pass
		indexes = {}
		colors = [
					[ '//', 'blue,darkcyan' ],

					[ '/*', 'blue,darkcyan' ],
					[ '*/', 'blue,darkcyan' ],

					[ '{', 'green' ],
					[ '}', 'green' ],

					[ '[', 'yellow' ],
					[ ']', 'yellow' ],

					[ '"', 'cyan,darkcyan' ],
					[ "'", 'cyan,darkcyan' ],
					# [ '"', 'cyan,BackgroundGreyBold.red' ],
					# [ "'", 'cyan,BackgroundGreyBold.red' ],

					[ ":", 'red' ],
					[ "=", 'red' ],

					[ ",", 'purple' ],
					[ ";", 'darkcyan' ],

					[ "(", 'Background.red' ],
					[ ")", 'Background.red' ],


				]
		pass

		for color in colors:
			theColors = []
			if ',' in color[1]:
				theColors = color[1].split(',')
			else:
				theColors.append( color[1] )

			cID = self.query( color[0], justIDs=True, isChar=True )
			gID = self.query( color[0], justIDs=True, isGroup=True )
			self.indexes['char'][ cID ]['color'] = theColors[0]
			if not gID is None:
				if ',' in color[1]:
					self.indexes['group'][ gID ]['color'] = theColors[1]
				else:
					self.indexes['group'][ gID ]['color'] = theColors[0]


		# _.printTest( self.indexes['group'], line=409, shouldExit=True )

		posColor = []
		for i,char in enumerate(self.asset):
			setColor = None
			for color in colors:
				# _.pr( i, color, self.query( color[0], justIndex=True, isChar=True ) )
				# sys.exit()
				cIndexes = self.query( color[0], justIndex=False, isChar=True )
				gIndexes = self.query( color[0], justIndex=False, isGroup=True )
				

				# if not gIndexes is None and not gIndexes['nestable']:
				#     _.printTest( gIndexes, line=436 )
				if not gIndexes is None and not gIndexes['nestable']:
					# _.printTest( gIndexes, line=423 )
					if i in gIndexes['inner']:
						setColor = gIndexes['color']
				if setColor is None and i in cIndexes['index']:
					setColor = cIndexes['color']

			# posColor.append({ 'pos': i, 'char': char, 'color': setColor })
			if setColor is None:
				pass
				_.pr( char, end ='' )
			else:
				# _.pr( char, end='' )
				# _.colorThis( color='help', shouldPrint=False )
				# _.pr( _.inlineBold( char, setColor ), end ='' )
				_.pr( _.colorThis( char, color=setColor, shouldPrint=False ), end ='' )
				

		pass
		# _.printBold( 'test', 'red' )



	def query( self, label=None, special=None, iID=None, gID=None, cID=None, rID=None, pID=None, oc='open,close', tag=None, pos=None, justIDs=None, isOpen=None, justIndex=False, isChar=False, isGroup=False, quoteComment=False ):

# self.query( tag='carriage', justIDs=True )
# self.query( tag='inline comment', justIDs=True )
# self.query( tag='comment', justIDs=True )
# self.query( label='\n', justIDs=True )


		# query( '{', justIndex=True, isChar=True )
		locationLabel = None

		if quoteComment:

			records = []
			for i,item in enumerate(self.indexes['group']):
				add = False
				for t in item['tags']:
					if 'quote' in t:
						add = True
					if 'comment' in t:
						add = True
				if add:
					records.append( i )
			return records


		elif not label is None and not justIndex and isChar and not isGroup and justIDs:
			locationLabel = '01'
			theID = self.itemLabel( label, 'char' )
			if theID is None:
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return theID

		elif not label is None and not justIndex and not isChar and isGroup and justIDs:
			locationLabel = '02'

			theID = self.itemLabel( label, 'group' )
			if theID is None:
				return None
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return theID

		elif not label is None and justIndex and isChar and not isGroup:
			locationLabel = '03'
			# _.pr( 'HERE' )

			theID = self.itemLabel( label, 'char' )

			if theID is None:
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()

			result = self.indexes['char'][ theID ]['index']

			# _.pr( result )

			if result is None:
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return result

		elif not label is None and not justIndex and isChar and not isGroup:
			locationLabel = '04'

			theID = self.itemLabel( label, 'char' )

			if theID is None:
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()

			result = self.indexes['char'][ theID ]

			# _.pr( result )

			if result is None:
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return result

		elif not label is None and not justIndex and not isChar and isGroup:
			locationLabel = '05'

			theID = self.itemLabel( label, 'group' )

			if theID is None:
				return None
				_.colorThis( [ 'Query Error:', locationLabel, label ] )
				sys.exit()

			result = self.indexes['group'][ theID ]

			# _.pr( result )

			if result is None:
				_.printBold( label, 'red' )
				sys.exit()
			return result

		elif not justIDs is None:

			if not label is None and special is None:

				info = { 'gID': None, 'iID': None }
				for i,item in enumerate(self.indexes['group']):
					if item['label'] == label:
						info['gID'] = i
				for i,item in enumerate(self.indexes['char']):
					if item['label'] == label:
						info['iID'] = i
				return info

			elif not tag is None and special is None and ',' in tag:
				# _.pr( 'here' )
				records = []
				for i,item in enumerate(self.indexes['group']):
					add = False
					for t in item['tags']:
						found = 0
						for test in tag.split( ',' ):
							if test in t:
								found += 1
						if found == len( tag.split( ',' ) ):
							add = True
					if add:
						records.append( i )
				return records



			elif not tag is None and not special is None and ',' in tag and 'all' in special:
				# _.pr( 'here' )
				records = []
				for i,item in enumerate(self.indexes['group']):
					add = False
					for t in item['tags']:
						found = 0
						for test in tag.split( ',' ):
							if test in t:
								add = True
					if add:
						records.append( i )
				return records



			elif not tag is None and special is None:
				records = []
				for i,item in enumerate(self.indexes['group']):
					for t in item['tags']:
						if t == tag:
							records.append( i )
				return records

			elif not tag is None and not special is None and type(special) == str and 'includes' in special and not ':' in special:

				records = []
				for i,item in enumerate(self.indexes['group']):
					if tag in item['tags']:
						records.append( i )
				return records

			elif not tag is None and not special is None and type(special) == str and 'exclude' in special and not ':' in special:
				records = []
				for i,item in enumerate(self.indexes['group']):
					added = False
					for tagX in item['tags']:
						for exclude in tag.split(','):
							if not exclude in tagX:
								if not added:
									added = True
									records.append( i )
				return records


		return None



		# if not iID is None:
		# elif not cID is None and not rID is None and not gID is None:
		# if not self.inIndex(gID):
		# if 'open' in oc:
		# if self.indexes['group'][gID]['open']['cID'] == cID and self.indexes['group'][gID]['open']['rID'] == rID:
		# if 'close' in oc:
		# if self.indexes['group'][gID]['close']['cID'] == cID and self.indexes['group'][gID]['close']['rID'] == rID:
		# elif not cID is None and not rID is None:
		# if 'open' in oc:
		# if char['open']['cID'] == cID and char['open']['rID'] == rID:
		# if 'close' in oc:
		# if char['close']['cID'] == cID and char['close']['rID'] == rID:
		# elif not cID is None:
		# if 'open' in oc:
		# if char['open']['cID'] == cID:
		# if 'close' in oc:
		# if char['close']['cID'] == cID:
		# elif not gID is None:
		# elif not label is None:
		# if char['label'] == label:
		# elif not tag is None:
		# if char['label'] == label:
		# if tag in char['tags']:



		# inIndex( self, label=None, iID=None, gID=None, cID=None, rID=None, tag=None, oc='open,close')


		# examples:
					# query()
					# query('\n')
					# query('[]' )
					# query('[]', 'inner' )
					# query('functions')
					# query('variables')
					# query('parameters')
					# query('delimiters')
					# query(':')
					# query(':')
					# query( 'whitespace' )
					# self.query( 'carriage', justIDs=True )

						# carriage


# do this first for everything
#                                 if not self.inIndex( iID=iID ):

		############################################################################ 
		# self.logistics[cID][rID]
		# self.indexes['char'][iID]
		# self.indexes['group'][gID]
		############################################################################
		# if not len(label):
		#     return self.indexes

		# if special is None:

		#     for char in self.indexes['char']:
		#         if char['label'] == label:
		#             return char['index']


	# def isCarriage( self, label=None, iID=None, charID=None, tag=None ):
		

	#     if not label is None:

	#         for char in self.indexes['group']:
	#             if char['label'] == label:
	#                 if 'carriage' in char['tags']:
	#                     return True

	#     elif not iID is None:
	#         for char in self.indexes['group']:

	#         else:


	#         else:



	def loadProject( self ):

		self.backupLoaded['attempted'] = True
		self.backupLoaded['validation']

		if not self.skipLoad:
			projectFile_indexes = _.getTable( self.projectFile.replace( 'PROJECT', 'indexes' ) )
			projectFile_validation = _.getTable( self.projectFile.replace( 'PROJECT', 'validation' ) )
			projectFile_profile = _.getTable( self.projectFile.replace( 'PROJECT', 'profile' ) )
			self.identity = _.getTable( self.projectFile.replace( 'PROJECT', 'identity' ) )



			if not len(projectFile_indexes):
				self.backupLoaded['indexes'] = False

			else:
				self.backupLoaded['indexes'] = True
				self.indexes = projectFile_indexes

			if not len(projectFile_validation):
				self.backupLoaded['validation'] = False
			else:
				self.backupLoaded['validation'] = True
				self.validation = projectFile_validation

			if not len(projectFile_profile):
				self.backupLoaded['profile'] = False
			else:
				self.backupLoaded['profile'] = True
				self.profile = projectFile_profile



	def saveProject( self ):
		_.saveTable( self.indexes, self.projectFile.replace( 'PROJECT', 'indexes' ), printThis=False )
		if self.profile:
			_.saveTable( self.profile, self.projectFile.replace( 'PROJECT', 'profile' ), printThis=False )
		
		try:
			_.saveTable( self.identity, self.projectFile.replace( 'PROJECT', 'identity' ), printThis=False )
		except Exception as e:
			pass

		# self.dump()



	def buildActionQueue( self, xID ):

		# x = self.indexes['group'][xID]['label']
		# _.pr( x )

		if not xID in self.buildActionQueueSpent:

			self.buildActionQueueSpent.append( xID )

			self.action[ self.action_queue ] = self.indexes['group'][xID]
			self.action[ self.action_queue ]['scanID'] = 0
			# self.table[ self.action[ self.action_queue ]['label'] ] = []
			self.posTable[ self.action[ self.action_queue ]['open']['label'] ] = []
			self.scanID[ str(self.action_queue)+'escape' ] = 0
			self.scanID[ self.action_queue ] = 0
			self.scanID[ str(self.action_queue) + 'open'] = 0
			self.scanID[ str(self.action_queue) + 'close'] = 0
			self.theNestID[ self.action_queue ] = 0


			self.scanEscapeActive[ self.action_queue ] = None

			# self.table[ self.action_queue ] = []

			self.scanIsOpen[ self.action_queue ] = False

			self.action_queue += 1
		else:
			_.pr( 'Omited Dupicate', xID )

		# _.pr( str(self.action_queue)+'escape' )


	def buildCarriageIndex( self ):
		# self.indexes = { 'char': [], 'group': [], }

		self.carriageIndex = {
						'index': [],
						'line': [],
						'label': ''
		}

		line = 0
		self.carriageIndex['index'].append( 0 )
		for i,char in enumerate(self.asset):
			self.carriageIndex['line'].append( line )

			if char == '\n':
				line += 1
				self.carriageIndex['index'].append( i )



	def getLine( self, pos ):
		# _.pr( 'pos', pos )
		# _.pr( 'line', self.carriageIndex['line'][pos] )
		# _.pr( self.carriageIndex['index'][ self.carriageIndex['line'][pos] ] )
		# sys.exit()
		try:
			return self.carriageIndex['line'][pos]
		except Exception as e:
			return self.indexes['carriageIndex']['line'][pos]

	# {4B2E8584-8EF6-4AA3-BBC0-4F89160AF12B}

	def getLinePos( self, line ):

		return self.indexes['carriageIndex']['index'][line]


	def getLineStartEnd( self, line ):

		pos = self.getLinePos( line )


		try:
			end = self.getLinePos( line+1 )
		except Exception as e:
			end = len( self.asset )-1
		return { 'start': pos, 'end': end }

	def buildIndividualIndexes( self, char ):

		shouldAdd = True

		for x in self.indexes['char']:
			if x['label'] == char:
				shouldAdd = False

		if shouldAdd:

			self.flat[char] = []



			# self.individualIndexes.append( len( self.indexes['char'] ) )

			# charIndexes = {
			#                 'total': 0,
			#                 'index': [],
			#                 'start': [],
			#                 'end': 1,
			#                 'line': [],
			#                 'label': ''
			# }

			# charIndexes['label'] = char

			# self.indexes['char'].append( charIndexes )



	def buildIndexes( self ):
		# os.system('cls')
		self.buildIndexStructure()
		self.buildCarriageIndex()
		self.action_queue = 0
		self.action = {}
		self.table = {}
		self.tableID = {}
		self.posTable = {}
		self.scanID = {}
		self.theNestID = {}
		self.scanIsOpen = {}
		self.scanEscapeActive = {}
		self.buildActionQueueSpent = []


			# self.flat[':'] = []
			# self.flat[','] = []
			# self.flat['='] = []
			# self.flat[';'] = []
			# self.flat[_v.slash] = []

		self.buildIndividualIndexes( ':' )
		self.buildIndividualIndexes( ',' )
		self.buildIndividualIndexes( '=' )
		self.buildIndividualIndexes( ';' )
		self.buildIndividualIndexes( _v.slash )

		self.indexes['individual'] = list( self.flat.keys() )



		# _.printVar2( self.indexes['char'] )
		# sys.exit()


# self.scanIsOpen[ self.action[ self.action_queue ]['open']['label'] ] = False
		# _.printVar( self.indexes )
		# sys.exit()
		# test = _.inlineBold( '[', 'green' )
		# _.pr( _.inlineBold( '{', 'green' ) )
		# _.pr( test )

		# # _.pr( self.indexes )
		# _.printVar( self.indexes )
		# sys.exit()

		# _.printVar( self.query( tag='inline,comment', justIDs=True ) )

		for xID in self.query( tag='inline,comment', justIDs=True ):
			# _.pr( xID )
			self.buildActionQueue( xID )



		# _.printVar( self.action )
		# sys.exit()

		for xID in self.query( tag='comment', justIDs=True ):
			self.buildActionQueue( xID )

		for xID in self.query( tag='comment', justIDs=True, special='exclude' ):
			self.buildActionQueue( xID )


		# for key in self.action:
		#     x = self.action[key]['label']
		#     _.pr( key, x )


		# # self.action[ self.action_queue ]
		# _.printVar( self.action )

		# sys.exit()
		# _.printVar( self.action )
		# sys.exit()

		self.allClosed = []

		self.identity = {
								'location': {
												'open': {},
												'close': {},
								},
								'identity': {},
								'validation': {},

		}

		if self.index_process == 'A':
			self.buildIndexes_Process_A()
		elif self.index_process == 'B':
			self.buildIndexes_Process_B()

	def buildIndexes_Process_A( self ):


		isSimple = self.isSimple
		nestable = {
					'status': False,
					'close': None,
		}
		# nestable['status'] = True
		# nestable['close'] = None

		nestTickets = {}

		auditIsClose = {}

		loopCheck = 0

		testA = 0
		testB = 0
		testC = 0
		testD = 0
		testE = 0

		loopLen = len( self.action.keys() ) 



		savedIn = []
		nestAudit = {
						'firstRun': True,
						'id': 0,
						'spent': [],
		}

		

		# _.printTest( self.action, line=862 )

		

		scanChars = []

		scanChars.append( ' ' )
		scanChars.append( '\n' )
		scanChars.append( '\t' )


		"""
		if self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ] == i: identification['all'] scan label id active start
		
		"""

		identification = {

							'all': '-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							'notFirst': '-:',
							'scan': [
											'0123456789',
											'.0123456789',
											'abcdefghijklmnopqrstuvwxyz',
											'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							],
							'label': [
											'number',
											'float',
											'alphaLower',
											'alphaUpper',
											'alpha',
											'alphaNumeric',
							],
							'id': None,
							'active': False,
							'start': None,
							'max': None,
		}
		
		identification['max'] = len( identification['scan'] )-1

		# idTable = {
		#                 'open': {},
		#                 'close': {},
		#                 'list': [],
		# }

		# idOC = {
		#                 'open': {},
		#                 'close': {},

		# }
		


		def genLabel( aID ):
			# _.printVarSimple( self.action[ aID ] )
			# sys.exit()
			tempLabel = '_'.join(  self.action[ aID ]['tags']  )
			return tempLabel


			tempLabel = self.action[ aID ]['open']['label']
			if not self.action[ aID ]['close']['label'] is None:
				tempLabel+=self.stringDelim+self.action[ aID ]['close']['label']
			return tempLabel


		for record in self.logistics['characters']:
			scanChars.append( record['char'] )


		scanChars = set(scanChars)

		for i,char in enumerate(self.asset):

			loopCheck += 1
			aID = 0
			saved = False
			nestAudit['firstRun'] = True
			allClosed = True
			factor = False
			if True:
				while not aID == ( loopLen ):



					if not saved or False:


						if self.action[ aID ]['close']['label'] is None:
							pass


						aIDxx = str(aID) + 'escape'


						if not self.scanEscapeActive[ aID ] is None and not self.scanEscapeActive[ aID ] == i:
							self.scanEscapeActive[ aID ] = None



						if len( self.action[ aID ]['escape'] ):

							if self.action[ aID ]['escape'][ self.scanID[ aIDxx ] ] == char:
								self.scanID[ aIDxx ] += 1
							else:
								self.scanID[ aIDxx ]  = 0
							if self.scanID[ aIDxx ] == len(self.action[ aID ]['escape']):
								self.scanEscapeActive[ aID ] = i+1
								factor = True

								self.scanID[ aIDxx ] = 0


						if self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ] == i:

							if self.action[ aID ]['close']['label'] is None:



								if self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] == char:

									self.scanID[ str(aID)+'open' ] += 1
								else:
									self.scanID[ str(aID)+'open' ] = 0
									if False and aID == 1:
										_.printBold( '00 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
								
								if self.scanID[ str(aID)+'open' ] == len(self.action[ aID ]['open']['label']):
									self.scanID[ str(aID)+'open' ] = 0
									factor = True
									if False and aID == 1:
										_.printBold( '01 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )



									if not nestable['status'] or (not nestable['close'] is None and nestable['close'] == self.action[ aID ]['open']['label'] and nestable['close'] == char):

										

	#####################################################       SAME OPEN AS CLOSE 
	# {6402B9BC-FF5C-4B6F-B8B4-CB1EFADDF405}



										if not self.scanIsOpen[ aID ] and not nestable['status']:
											if not self.action[ aID ]['nestable']:
												nestable['status'] = True
												nestAudit['id']+=1
												nestable['close'] = self.action[ aID ]['open']['label']
											self.theNestID[ aID ] += 1
											saved = True
											if self.theNestID[ aID ] > 1:
												_.printBold( 'error', 'red' )
											nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = True
											self.scanIsOpen[ aID ] = True
											if not isSimple:
												try:
													# self.identity['location']['close'][ i ] = self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]
													# self.identity['location']['open'][  self.identity['location']['close'][ i ]  ] =  i
													# self.identity['identity'][  self.identity['location']['close'][ i ] ] =  genLabel(aID)
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 0 )
												except Exception as e:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = []
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 1 )
											self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = i
										
										elif self.scanIsOpen[ aID ]:
											self.identity['location']['close'][ i ] = self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
											self.identity['location']['open'][  self.identity['location']['close'][ i ]  ] =  i
											self.identity['identity'][  self.identity['location']['close'][ i ] ] =  genLabel(aID)
											if not isSimple:
												if not self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ][0]['start'] == i-len(self.action[ aID ]['open']['label'])+1:

													nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = False
													saved = True
													nestable['status'] = False
													nestable['close'] = None
													self.scanIsOpen[ aID ] = False
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 2 )
													self.theNestID[ aID ] -= 1



							else:
	#####################################################       OPEN

								if not nestable['status']:
									if False and i == 5:
										sys.exit()
									if False and aID == 1:
										_.pr( '\t', i, aID, self.scanID[ str(aID)+'open' ], self.action[ aID ]['open']['label'] )
									if self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] == char:
										self.scanID[ str(aID)+'open' ] += 1
										if False and aID == 1:
											_.pr( i, aID, 'Found:', self.action[ aID ]['open']['label'], self.scanID[ str(aID)+'open' ], self.asset[i+1] )
									else:
										if False and aID == 1:
											_.pr( i, aID, 'Not Found:', self.action[ aID ]['open']['label'], self.scanID[ str(aID)+'open' ], self.asset[i], self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ]-1 ],self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] )
											_.pr(  self.asset[i], self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] )
											_.pr(  "'"+self.asset[i]+"'", "'"+self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] +"'" )

										self.scanID[ str(aID)+'open' ] = 0
										if False and aID == 1:
											_.printBold( '02 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )

									if self.scanID[ str(aID)+'open' ] == len(self.action[ aID ]['open']['label']):
										self.scanID[ str(aID)+'open' ] = 0
										factor = True
										if False and aID == 1:
											_.printBold( '03 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )

										if not nestable['status'] :
											self.theNestID[ aID ] += 1
											self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = i
											saved = True
											nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = True


											if not self.action[ aID ]['nestable']:
												nestable['status'] = True
												nestAudit['id']+=1
												nestable['close'] = self.action[ aID ]['open']['label']

											self.identity['location']['close'][ i ] = self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
											self.identity['location']['open'][  self.identity['location']['close'][ i ]  ] =  i
											self.identity['identity'][  self.identity['location']['close'][ i ] ] =  genLabel(aID)

											if not isSimple:
												try:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 3 )
												except Exception as e:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = []
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 4 )
											
											if not self.action[ aID ]['nestable']:
												nestable['status'] = True
												nestAudit['id']+=1
												nestable['close'] = self.action[ aID ]['close']['label']



									pass



	#####################################################       CLOSE


								pass
								if '\n' == self.action[ aID ]['close']['label'] :
									if char  == self.action[ aID ]['close']['label']:
										if not nestable['status'] or (not nestable['close'] is None and nestable['close'] == self.action[ aID ]['close']['label']):



											try:
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ]-1 ) ]
											except Exception as e:
												isClose = False
												
											else:
												if nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ]-1 ) ]:
													isClose = True
												else:
													isClose = False

											if isClose or True:
												
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = False
												try:
													if not isSimple:
														self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['close']['label'] , 'start': i-len(self.action[ aID ]['close']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 5 )
													self.identity['location']['close'][ i ] = self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
													self.identity['location']['open'][  self.identity['location']['close'][ i ] ] =  i
													self.identity['identity'][  self.identity['location']['close'][ i ] ] =  genLabel(aID)
												except Exception as e:
													pass
												else:
													saved = True
													self.theNestID[ aID ] -= 1
													nestable['status'] = False
													nestable['close'] = None



								else:



									if self.action[ aID ]['close']['label'][ self.scanID[ str(aID)+'close' ] ] == char:
										# _.pr( i, self.scanID[ str(aID)+'close' ], char, 'close' )
										self.scanID[ str(aID)+'close' ] += 1
									else:
										self.scanID[ str(aID)+'close' ] = 0
										if False and aID == 1:
											_.printBold( '04 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
									if self.scanID[ str(aID)+'close' ] == len(self.action[ aID ]['close']['label']):
										self.scanID[ str(aID)+'close' ] = 0
										factor = True
										if False and aID == 1:
											_.printBold( '05 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )



										if not nestable['status'] or (not nestable['close'] is None and nestable['close'] == self.action[ aID ]['close']['label']):



											try:
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]
											except Exception as e:
												isClose = False
												
											else:
												if nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]:
													isClose = True
												else:
													isClose = False



												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ] = False

												try:
													if not isSimple:
														if not self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ][0]['start'] == i-len(self.action[ aID ]['close']['label'])+1:
															self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['close']['label'] , 'start': i-len(self.action[ aID ]['close']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													self.identity['location']['close'][ i ] = self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
													self.identity['location']['open'][  self.identity['location']['close'][ i ] ] =  i
													self.identity['identity'][  self.identity['location']['close'][ i ] ] =  genLabel(aID)
												except Exception as e:
													pass
												else:
													savedIn.append( 6 )
													saved = True
													self.theNestID[ aID ] -= 1
													nestable['status'] = False
													nestable['close'] = None

										else:
											pass



						pass
						if not nestable['status']:
							for key in self.flat.keys():
								if key == char:
									self.flat[key].append( i )
						pass
						if not nestable['status']:
							for iiChar in self.individualIndexes:
								if char == self.indexes['char'][iiChar]['label']:

									self.indexes['char'][iiChar]['total']+=1
									self.indexes['char'][iiChar]['index'].append( i )
									self.indexes['char'][iiChar]['line'].append( self.getLine(i) )

# {
#     'total': 0,
#     'index': [],
#     'start': [],
#     'end': 1,
#     'line': [],
#     'label': ''
# }



					pass
					if self.theNestID[ aID ]:
						allClosed = False


					
					aID += 1





				pass
				if not nestable['status']:

					pass
					if not char in identification['all'] and identification['active']:
						# _.pr('HERE')
						thisLabel = identification['label'][  identification['id']  ]
						txx = i-1-identification['start']
						if txx == 4 or txx == 3:
							sample = self.assetSnipet( identification['start'], i-1 )
							# _.pr(sample)
							if sample == 'true' or sample == 'True' or sample == 'false' or sample == 'False' or sample == 'TRUE' or sample == 'FALSE':
								thisLabel = 'bool'

						# rxz = { 'label': thisLabel , 'start': identification['start'], 'end': i-1,  'line': self.getLine(i) }
						# idTable['list'].append( rxz )
						# idTable['open'][  identification['start']  ] = i
						# idTable['close'][  i  ] = identification['start']


						self.identity['location']['close'][ i-1 ] = identification['start']
						self.identity['location']['open'][  self.identity['location']['close'][ i-1 ] ] =  i-1
						self.identity['identity'][  self.identity['location']['close'][ i-1 ] ] =  thisLabel



						identification['active'] = False
						identification['id'] = None
						identification['start'] = None

					
					elif char in identification['all'] and not identification['active']:
						if not char in identification['notFirst']:
							identification['start'] = i
							identification['id'] = 0
							identification['active'] = True
							
							while not char in identification['scan'][  identification['id']  ]:
								identification['id']+=1

					elif char in identification['all'] and identification['active']:
						while not char in identification['scan'][  identification['id']  ]:
							identification['id']+=1

					# identification['all'] scan label id active start
					# identification['max']
					# idTable['open'] close list

					pass
				pass






					# self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ] == i: 

			pass
			if allClosed:
				self.allClosed.append( i )


		# self.thisTest = self.asset
		# self.thisTest = idTable
		if not isSimple:
			self.dataRestructure()









































	def buildIndexes_Process_B( self ):



		"""
		if self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ] == i: identification['all'] scan label id active start
		
		"""

		identification = {

							'all': '-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							'notFirst': '-:',
							'scan': [
											'0123456789',
											'.0123456789',
											'abcdefghijklmnopqrstuvwxyz',
											'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							],
							'label': [
											'number',
											'float',
											'alphaLower',
											'alphaUpper',
											'alpha',
											'alphaNumeric',
							],
							'id': None,
							'active': False,
							'start': None,
							'max': None,
		}
		
		identification['max'] = len( identification['scan'] )-1

		# idTable = {
		#                 'open': {},
		#                 'close': {},
		#                 'list': [],
		# }

		# idOC = {
		#                 'open': {},
		#                 'close': {},

		# }
		


		def genLabel( aID ):
			# _.printVarSimple( self.action[ aID ] )
			# sys.exit()
			tempLabel = '_'.join(  self.action[ aID ]['tags']  )
			return tempLabel


			tempLabel = self.action[ aID ]['open']['label']
			if not self.action[ aID ]['close']['label'] is None:
				tempLabel+=self.stringDelim+self.action[ aID ]['close']['label']
			return tempLabel


		# for record in self.logistics['characters']:
		#     scanChars.append( record['char'] )

		self.characters_max_length = 0

		action_count_temp = {}
		self.action_index = {}

		for aID in self.action:
			self.action[aID]['open']['not'] = None
			self.action[aID]['close']['not'] = None

		for aID in self.action:
			o = self.action[aID]['open']['label']
			c = self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ] = {}
				action_count_temp[  o[0]  ] = { 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }
			if not c is None:
				self.action_index[  c[0]  ] = {}
				action_count_temp[  c[0]  ] = { 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }

		for i,aID in enumerate(self.action):
			o = self.action[aID]['open']['label']
			c = self.action[aID]['close']['label']
			if not o is None:
				if len(o) > self.characters_max_length:
					self.characters_max_length = len(o)
				self.action_index[  o[0]  ][ len(o) ] = {}
			if not c is None:
				if len(c) > self.characters_max_length:
					self.characters_max_length = len(c)
				self.action_index[  c[0]  ][ len(c) ] = {}

		for i,aID in enumerate(self.action):
			o = self.action[aID]['open']['label']
			c = self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ][ len(o) ][ o ] = i
			if not c is None:
				self.action_index[  c[0]  ][ len(c) ][ c ] = i




		for i,aID in enumerate(self.action):
			o = self.action[aID]['open']['label']
			c = self.action[aID]['close']['label']
			if not o is None:
				action_count_temp[  o[0]  ]['cnt']+=1
				if len(o) > action_count_temp[  o[0]  ]['max']:
					action_count_temp[  o[0]  ]['max'] = len(o)
				action_count_temp[  o[0]  ]['chars']['start'][o] = {}
			if not c is None:
				action_count_temp[  c[0]  ]['cnt']+=1
				if len(c) > action_count_temp[  c[0]  ]['max']:
					action_count_temp[  c[0]  ]['max'] = len(c)
				action_count_temp[  c[0]  ]['chars']['start'][c] = {}

		self.action_multi = { 'cnt': {}, 'max': {} }


		for x in action_count_temp:
			if action_count_temp[x]['max'] > 1:
				self.action_multi['max'][x] = action_count_temp[x]
			if action_count_temp[x]['cnt'] > 1:
				self.action_multi['cnt'][x] = action_count_temp[x]
		
		# for aID in self.action:
		#     o = self.action[aID]['open']['label']
		#     c = self.action[aID]['close']['label']
		#     if o in self.action_multi['cnt']:
		#         for x in self.action_multi['cnt'][o]['chars']['start']:
		#             if not x == o:
		#                 if self.action[aID]['open']['not'] is None:
		#                     self.action[aID]['open']['not'] = {'start':{},'end':{},'middle':{}}
		#                 if not len(x) in self.action[aID]['open']['not']:
		#                     self.action[aID]['open']['not']['start'][len(x)] = {}
		#                 self.action[aID]['open']['not']['start'][len(x)][x] = {}
						
		#                 # _.pr( 'not:', o, x )

		#     if c in self.action_multi['cnt']:
		#         for x in self.action_multi['cnt'][c]['chars']['start']:
		#             if not x == c:
		#                 if self.action[aID]['close']['not'] is None:
		#                     self.action[aID]['close']['not'] = {'start':{},'end':{},'middle':{}}
		#                 if not len(x) in self.action[aID]['close']['not']:
		#                     self.action[aID]['close']['not']['start'][len(x)] = {}
		#                 self.action[aID]['close']['not']['start'][len(x)][x] = {}
		#                 # _.pr( 'not:', c, x )

		for i,aID in enumerate(self.action):
			for ix,aIDx in enumerate(self.action):
				if not aID == aIDx:
					if self.action[aID]['open']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not'] = {'beg':None,'end':None,'mid':None }
						a = self.action[aID]['open']['label']
						b = self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg'] = {}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)] = {}
							self.action[aID]['open']['not']['beg'][len(b)][b] = {}

						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end'] = {}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)] = {}
							self.action[aID]['open']['not']['end'][len(b)][b] = {}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid'] = {}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)] = {}
							self.action[aID]['open']['not']['mid'][len(b)][b] = {}

					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not'] = {'beg':None,'end':None,'mid':None }
						a = self.action[aID]['close']['label']
						b = self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg'] = {}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)] = {}
							self.action[aID]['close']['not']['beg'][len(b)][b] = {}

						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end'] = {}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)] = {}
							self.action[aID]['close']['not']['end'][len(b)][b] = {}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid'] = {}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)] = {}
							self.action[aID]['close']['not']['mid'][len(b)][b] = {}
		



					if not self.action[aID]['open']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['open']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not'] = {'beg':None,'end':None,'mid':None }
						a = self.action[aID]['open']['label']
						b = self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg'] = {}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)] = {}
							self.action[aID]['open']['not']['beg'][len(b)][b] = {}

						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end'] = {}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)] = {}
							self.action[aID]['open']['not']['end'][len(b)][b] = {}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid'] = {}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)] = {}
							self.action[aID]['open']['not']['mid'][len(b)][b] = {}



					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['open']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not'] = {'beg':None,'end':None,'mid':None }
						a = self.action[aID]['close']['label']
						b = self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg'] = {}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)] = {}
							self.action[aID]['close']['not']['beg'][len(b)][b] = {}

						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end'] = {}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)] = {}
							self.action[aID]['close']['not']['end'][len(b)][b] = {}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid'] = {}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)] = {}
							self.action[aID]['close']['not']['mid'][len(b)][b] = {}



		def d4_peek( ix, length ):
			txt = ''
			while not len(txt) == length:
				try:
					txt += self.asset[ix]
				except Exception as e:
					txt += ' '
				ix+=1
			return txt

		def d4_peek( ix, length ):
			txt = ''
			while not len(txt) == length:
				try:
					txt += self.asset[ix]
				except Exception as e:
					txt += ' '
				ix+=1
			return txt



		def d4_peekB( ix, length, char ):
			txt = []
			for x in char:
				txt.append(x)
			txt.reverse()
			ix-=1

			while not len(txt) == length:
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix-=1
			txt.reverse()
			return ''.join(txt)

		def d8_peek_in(  ix, char, charX, sject  ):
			
			x = charX.index(char)
			txt = []
			yx = 0
			bix = ix
			while not yx == x:
				yx+=1
				try:
					txt.append( self.asset[ bix-yx ] )
				except Exception as e:
					txt.append( ' ' )
				
			txt.reverse()
			yy = x+len(char)-1
			xy = len(charX)-1

			for y in char:
				ix+=1
				txt.append(y)

			while not len(txt) >= len(charX):
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix+=1
			return ''.join(txt)

		def escapeIsActive(i,escape):
			txt = ''
			bix = i-1
			while self.asset[bix] == escape:
				txt+=self.asset[bix]
				bix-=1
			if len(txt) % 2 == 0:
				return False
			else:
				return True
		def d20( i, char  ):
			aID = None

			if char in self.action_index:
				# _.pr( char )
				ai = self.action_index[char]
				if len( ai ) == 1 and 1 in ai:
					aID = ai[1][char]
				else:
					mx = self.characters_max_length
					while mx > 0 and aID is None:
						if aID is None:
							if mx in ai:
								char = d4_peek( i, mx )
								if char in ai[mx]:
									aID = ai[mx][char]
									checkValid = True

									# for item in ['open','close']:
									for item in ['open']:
										if not self.action[aID][item]['label'] is None:
											if self.action[aID][item]['label'] == char:
												if not self.action[aID][item]['not'] is None:
													for sject in self.action[aID][item]['not']:
														if not self.action[aID][item]['not'][sject] is None:
															# _.colorThis([ sject.upper(), char ])
															mxNOT = self.characters_max_length
															while mxNOT > 0:
																if mxNOT in self.action[aID][item]['not'][sject]:
																	
																	if sject == 'beg':
																		if d4_peek( i, mxNOT ) in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid = False
																		if d4_peekB( i, mxNOT, char ) in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid = False
																	elif sject == 'end':
																		charX = d4_peekB( i, mxNOT, char )
																		if charX in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid = False
																	elif sject == 'mid':
																		for charX in self.action[aID][item]['not'][sject][mxNOT]:
																			if not d8_peek_in( i, char, charX, sject ):
																				checkValid = False

																mxNOT-=1







									# {B0B402BE-6121-47BA-9299-11C52E13CE87}
									if checkValid:
										break
									else:
										if not self.nestable['status']:
											aID = None
										else:
											break
						mx-=1
			
			if not aID is None:
				if not self.nestable['status']:
					isValid = True
				elif self.nestable['close'] == aID:
					isValid = True
				else:
					isValid = False

				if isValid:
					if 'regex' in self.action[aID]['tags']:
						if not self.nestable['status']:
							the_last_char = [
										'(',
										'=',
										':',
										'[',
									]
							if not self.the_last_char in the_last_char:
								isValid = False

				if isValid:
						escape = self.action[aID]['escape']
						if escape:
							if not i == 0:
								if self.asset[i-1] == escape:
									if escapeIsActive(i,escape):
										isValid = False

						# sys.exit()

				# if not isValid:
				#     _.pr(char)
				if isValid:
					if self.nestable['close'] == aID or char == self.action[aID]['close']['label']:
						if self.theNestID[ aID ] > 0:

							thisItem = str(aID) +'X'+ str( self.theNestID[ aID ] )

							theEnd = i-len(self.action[ aID ]['open']['label'])+1+len(self.action[ aID ]['open']['label'])-1
							theStart = self.table[ thisItem ]
							self.identity['location']['close'][ theEnd ] = theStart
							self.identity['location']['open'][  self.identity['location']['close'][ theEnd ] ] =  theEnd
							self.identity['identity'][  self.identity['location']['close'][ theEnd ] ] =  genLabel(aID)
							d10_close( char, theStart, theEnd, thisItem )
							self.theNestID[ aID ]-=1
							self.nestable['close'] = None
							self.nestable['status'] = False


					else:
						self.theNestID[ aID ]+=1
						thisItem = str(aID) +'X'+ str( self.theNestID[ aID ] )
						self.table[ thisItem ] = i
						if not self.action[aID]['nestable']:
							self.nestable['close'] = aID
							self.nestable['status'] = True
						
						d10_open( i, char, thisItem )
						

						# _.printVarSimple( self.action[aID] )
						# sys.exit()

		#     self.action[aID]['close']['not'][len(x)][x] = {}
		#     self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]
		#     self.action_index[  o[0]  ][ len(o) ][ o ] = i
		#     self.characters_max_length




		#     if not self.asset[i] in self.action_multi['max']:
		#         if self.action[aID][theOC]['label'] == self.asset[i]:
		self.relevant_OC = ['(', '{','[']

		def d10_open( i, char, thisItem ):

			
			self.components['preLast'][thisItem] = self.components['last']
			self.components['last'] = thisItem
			self.components['char'][thisItem] = char
			self.components['hasLabel'][thisItem] = False
			self.components['builder'][thisItem] = []
			self.components['sub'][thisItem] = []
			self.components['sub'][ thisItem  ]
			self.components['lastLabel'][ thisItem ] = []
			# self.components['lastLabel'][thisItem] = []
			# if char in self.relevant_OC:
		def d10_close( char, theStart, theEnd, thisItem=None ):
			if thisItem is None:
				thisItem = self.components['last']

				if not thisItem in self.components['sub']:
					self.components['sub'][ thisItem ] = []
				self.components['sub'][ thisItem  ].append(theStart)
			else:
				if char in '}':
					d10_softClose( thisItem )
				# _.pr(  char, self.components['last'], self.components['preLast'][thisItem]  )
				self.components['last'] = self.components['preLast'][thisItem]
			# _.pr( thisItem, self.components['preLast'][thisItem] )

				if not self.components['last'] in self.components['sub']:
					self.components['sub'][ self.components['last'] ] = []
				self.components['sub'][ self.components['last']  ].append(theStart)

			# self.components['sub'][ thisItem  ] = []
			# _.pr(theStart,self.components['char'][thisItem],self.components['char'][self.components['preLast'][thisItem]])


			# self.components['sub'].append( theStart )
				# if self.components['char'][self.components['last']] in self.relevant_OC:
					# d10_softClose( self.components['last'] )
					# try:
					# except Exception as e:
					#     pass
			
					# self.components['sub'][ self.components['last']  ] = []
					# self.components['builder'][ self.components['last'] ] = []



			self.identity['validation'][theStart] = self.components['builder'][thisItem]
			self.components['builder'][thisItem] = []
			# self.components['last'] = self.components['preLast'][thisItem]
		def d10_build_part():
			pass
		def d10_build_close():
			pass

		def d10_char(i,char):
			thisItemP = self.components['preLast'][self.components['last']]
			thisItem = self.components['last']
			if self.components['char'][ thisItem ] == '{':
				if char == self.breaks['label']:
					self.components['lastLabel'][ thisItem ] = self.components['sub'][ thisItem ]
					self.components['hasLabel'][ thisItem ] = True
					self.components['sub'][ thisItem  ] = []
				elif char == self.breaks['mini']:
					d10_softClose( thisItem )
			
		def d10_softClose( thisItem ):
			# _.pr(txt)

			try:
				vbs = { 'label': self.components['lastLabel'][ thisItem ], 'values': self.components['sub'][ thisItem  ] }
			except Exception as e:
				_.pr( thisItem, self.components['char'][thisItem] )
				sys.exit()
			asdf = False
			if asdf:
				_.pr()
				_.pr(thisItem, vbs)
			for x in self.components['lastLabel'][ thisItem ]:
				if x in self.identity['location']['open']:
					txt = self.assetSnipet( x, self.identity['location']['open'][x] )
				else:
					txt = self.asset[x]
				if asdf:
					_.pr( '\t LABEL', txt )
			for x in self.components['sub'][ thisItem  ]:
				if x in self.identity['location']['open']:
					txt = self.assetSnipet( x, self.identity['location']['open'][x] )
				else:
					txt = self.asset[x]
				if asdf:
					_.pr( '\t VALUE', txt )
			self.components['sub'][ thisItem  ] = []

			self.components['builder'][ thisItem ].append(vbs)

		self.breaks = {
								'label': ':',
								'mini': ',',
								'hard': ';',
								'soft': '\n',
		}
		relevantChars = []
		for x in self.breaks:
			relevantChars.append( self.breaks[x] )

		# self.components['builder']
		self.components = {
								'sub': {},
								'builder': {},

								'group': {},
								'char': {},
								'variable': {},

								'preLast': {},
								'last': 0,

								'hasLabel': {},
								'lastLabel': {},
		}
		self.components['sub'][0]=[]
		self.components['char'][0] = None
		self.components['preLast'][0] = 0
		self.components['preLast']['None'] = 0
		self.components['char']['None'] = ''
		self.components['builder'][0] = []
		self.nestable = {
							'status': False,
							'close': None,
		}

		# 
		start = time.time()
		self.the_last_char = ''
		for i,char in enumerate(self.asset):

			x = d20( i, char )
			if not char == ' ' and not char == '\t' and not char == '\n':
				self.the_last_char = char
				
			if not self.nestable['status']:

				pass
				if not char in identification['all'] and identification['active']:
					# _.pr('HERE')
					thisLabel = identification['label'][  identification['id']  ]
					txx = i-1-identification['start']
					if txx == 4 or txx == 3:
						sample = self.assetSnipet( identification['start'], i-1 )
						# if sample == '9999':
						#     _.pr( sample, self.components['last'] )
						# _.pr(sample)
						if sample == 'true' or sample == 'True' or sample == 'false' or sample == 'False' or sample == 'TRUE' or sample == 'FALSE':
							thisLabel = 'bool'

					# rxz = { 'label': thisLabel , 'start': identification['start'], 'end': i-1,  'line': self.getLine(i) }
					# idTable['list'].append( rxz )
					# idTable['open'][  identification['start']  ] = i
					# idTable['close'][  i  ] = identification['start']


					self.identity['location']['close'][ i-1 ] = identification['start']
					self.identity['location']['open'][  self.identity['location']['close'][ i-1 ] ] =  i-1
					self.identity['identity'][  self.identity['location']['close'][ i-1 ] ] =  thisLabel

					d10_close( char, identification['start'], i-1 )

					identification['active'] = False
					identification['id'] = None
					identification['start'] = None

				
				elif char in identification['all'] and not identification['active']:
					if not char in identification['notFirst']:
						identification['start'] = i
						identification['id'] = 0
						identification['active'] = True
						
						while not char in identification['scan'][  identification['id']  ]:
							identification['id']+=1

				elif char in identification['all'] and identification['active']:
					while not char in identification['scan'][  identification['id']  ]:
						identification['id']+=1

				# identification['all'] scan label id active start
				# identification['max']
				# idTable['open'] close list

				pass
			pass

			if not self.nestable['status']:
				if char in relevantChars:
					d10_char( i, char )
				elif not char in self.action_index and not char in identification['all'] and not char == ' ' and not char == '\t' and not char == '\n':
					if not self.components['last'] in self.components['sub']:
						self.components['sub'][ self.components['last']  ] = []
					self.components['sub'][ self.components['last']  ].append(i)



			




		# _.printVarSimple(self.theNestID)
		self.duration = time.time()-start
		errors = []
		for x in self.theNestID:
			if self.theNestID[x] > 0:
				yyy = self.table[ str(x) +'X'+ str( self.theNestID[ x ] ) ]
				
				errors.append( yyy )
		
		if errors:
			_.pr()
			_.pr()
			_.pr()
			_.colorThis( [  'FILE NOT VALID:'  ] )
			_.colorThis( [  '\tfound', len(errors), 'errors'  ], 'yellow' )
			for x in errors:
				y = {  'char': self.asset[x], 'line': self.getLine(x) }
				_.color( [  '\t\t\t', y  ], 'yellow' )
			_.pr()
			_.pr()
			_.pr()
			return None
			sys.exit()


		# _.pr( self.identity )

		del self.nestable
























	def getLabel( self, subject, string=False ):
		if type(subject) == str:
			r = subject.split(self.stringDelim)
			if string:
				return ''.join(r)
			return r
		elif type(subject) == int:
			return self.getLabel(  self.identity['identity'][subject], string  )
	def preValidate( self, start=None, end=None ):
		special = {
						'\n': { 'tags': ['close'] },
						';': { 'tags': ['close'] },
						'=': { 'tags': ['eq'] },
						',': { 'tags': ['delimiter'] },
						'-': { 'tags': ['math'] },
						'+': { 'tags': ['math','add'] },
						'/': { 'tags': ['math'] },
						'*': { 'tags': ['math'] },
		}

		whitespace = [ ' ', '\t', '\n' ]
		if start is None:
			i = -1
		else:
			i = start
		if end is None:
			end = len(self.asset)
		end-=1

		done = False
		result = []
		last = None
		lastSet = []
		var = None
		isEqual = False
		label = None
		delimiters = 0
		variables = {}
		while not  done:
			i+=1
			if i == end:
				done=True
			if not done:
				try:
					char = self.asset[i]
				except Exception as e:
					done=True
			if not done:
				
				if not i in self.identity['identity']:
					# _.pr('char',char)
					if char in special:
						# _.pr('SPECIAL', char, special[char])
						# sys.exit()
						if 'close' in special[char]['tags']:
							if not label is None:
								y = []
								for x in lastSet:
									y.append(str(x))
								variables[ ','.join(y) ] = lastSet
								result.append( { 'label': label, 'values': lastSet } )
							elif len(lastSet):
								result.append( lastSet )
							lastSet = []
							label = None
						elif 'eq' in special[char]['tags']:
							# _.pr('HERE')
							# sys.exit()
							label = lastSet
							
							lastSet = []
						else:
							lastSet.append( i )
					elif char in whitespace:
						pass
					else:
						lastSet.append(i)


				else:
					o = i
					c = self.identity['location']['open'][o]
					lastSet.append(i)
					i=c

		if len(lastSet):
			if not label is None:
				result.append( { 'label': label, 'values': lastSet } )
				label = None
			else:
				result.append(lastSet)

		return result

	def sudoValidate( self, start=None, end=None ):
		result = self.preValidate()
		# return result
		_.pr(  )
		_.pr( '____' )
		_.pr(  )
		for group in result:
			_.pr(  )
			if type(group) == dict:
				_.pr( group )
				o = group['values'][0]
				c = self.identity['location']['open'][o]
				test = self.validateDic(o,c)
				_.pr( test )

				for rec in test:
					o = rec[0]
					c = self.identity['location']['open'][o]
					txt = self.assetSnipet( o, c )
					_.pr( '\t', txt )
					for val in rec[1]:
						o = val
						if o in self.identity['location']['open']:
							c = self.identity['location']['open'][o]
							l = self.identity['identity'][o]
							txt = self.assetSnipet( o, c )
						else:
							txt = self.asset[o]
							l=''
						_.pr( '\t\t', txt, l )


			elif type(group) == list:
				for i in group:
					if type(i) == int:
						o=i
						if o in self.identity['location']['open']:
							c = self.identity['location']['open'][o]
							l = self.identity['identity'][o]
							txt = self.assetSnipet( o, c )
						else:
							l = ''
							txt = ''
						_.pr( i, txt, l )
					else:
						_.pr( type(i) )
						_.pr( str(i) )





		# for i,char in enumerate(self.asset):
		#     if i in self.identity['identity']:
		#         pass
		#         sv = self.getLabel(  i  )
		#         o = i
		#         c = self.identity['location']['open'][i]
		#         if sv[0] == '{':
		#             _.pr( 'sv\t', sv )
		#             _.pr( self.assetSnipet( o, c ) )
		#             test = self.validateDic( o, c )
		#             _.pr( test )

		#             for rec in test:
		#                 o = rec[0]
		#                 c = self.identity['location']['open'][o]
		#                 txt = self.assetSnipet( o, c )
		#                 _.pr( '\t', txt )
		#                 for val in rec[1]:
		#                     o = val
		#                     if o in self.identity['location']['open']:
		#                         c = self.identity['location']['open'][o]
		#                         txt = self.assetSnipet( o, c )
		#                     else:
		#                         txt = self.asset[o]
		#                     _.pr( '\t\t', txt )

	def validateDic( self, o, c ):
		field=':'
		each=','
		i = o
		done = False
		result = []
		lastField = None
		lastValue = []
		pastField=False
		while not  done:
			i+=1
			if i == c:
				done=True
			if not done:
				try:
					char = self.asset[i]
				except Exception as e:
					done=True
			if not done:
				
				if not i in self.identity['identity']:
					# _.pr('char',char)
					if char == field and pastField:
						_.colorThis( 'Error' )
					if char == field:
						pastField = True
					elif char == each:
						result.append( [lastField, lastValue] )
						lastField = None
						lastValue = []
						pastField = False
					elif char == ' ' or char == '\t' or char == '\n':
						pass
					else:
						lastValue.append(i)


				else:
					if lastField is None:
						lastField = i
					elif pastField:
						lastValue.append(i)
					else:
						_.colorThis( 'Error' )

					# sv = self.splitOpenClose(  self.identity['identity'][i]  )
					o = i
					c = self.identity['location']['open'][i]
					i=c
					# if sv[0] == '{':
		if len(lastValue):
			result.append( [lastField, lastValue] )
		
		return result



	def dataRestructure( self ):

		self.indexes['allClosed'] = self.allClosed
		self.indexes['carriageIndex'] = self.carriageIndex

		actionIndex = {}
		loopLen = len( self.action.keys() ) 
		aID = 0
		while not aID == ( loopLen ):
			actionIndex[ self.action[ aID ]['open']['label'] ] = aID
			
			if not self.action[ aID ]['close']['label'] is None:
				actionIndex[ self.action[ aID ]['close']['label'] ] = aID

			aID+=1


		
		for key in self.flat.keys():
			charIndexes = {
							'total': len(self.flat[key]),
							'index': self.flat[key],
							'start': self.flat[key],
							'end': 1,
							'line': [],
							'label': key
			}
			for i in self.flat[key]:
				charIndexes['line'].append( self.getLine(i) )

			self.indexes['char'].append( charIndexes )


		cleanKeys = {}
		for key in self.table.keys():
			for x in self.table[ key ]:
				try:
					cleanKeys[x['id']].append( x )
				except Exception as e:
					cleanKeys[x['id']] = []
					cleanKeys[x['id']].append( x )
				# _.printVar( x )
				# sys.exit()

		pass
		for key in cleanKeys.keys():
			if not len( cleanKeys[key] ) == 2:
				_.printBold( 'Validation Fail: ' + str(cleanKeys[key]), 'red' )
				sys.exit()


		# for key in cleanKeys.keys():
		#     _.pr( 'line: 1377', cleanKeys[key] )



		omit = [
					'[',
					"'",
					'(',
					'//',
					'"',
					'{',
				]

		# for i,key in enumerate(cleanKeys.keys()):
		#     if not cleanKeys[key][0]['label'] in omit:
		#         _.pr( cleanKeys[key][0]['label'], cleanKeys[key][1]['label'] )


		# for i,key in enumerate(cleanKeys.keys()):
		#     if i == 0:
		#         _.pr( cleanKeys[key] )

		# _.printVar( self.indexes )
		# sys.exit()

		self.noIndex = []


		self.genitemLabelIndexes()



		# _.printVar( self.indexes )
		# _.printVarSimple( self.indexes['IDs'] )

		for i,key in enumerate(cleanKeys.keys()):
			if True:
			# if i == 0:

				theChar = cleanKeys[key][0]['label']
				char0ID = self.itemLabel( cleanKeys[key][0]['label'], 'char' )
				char1ID = self.itemLabel( cleanKeys[key][1]['label'], 'char' )

				groupID = self.itemLabel( cleanKeys[key][0]['label']+cleanKeys[key][1]['label'], 'group' )
				if groupID is None:
					groupID = self.itemLabel( cleanKeys[key][0]['label'], 'group' )

				if char0ID is None:
					_.printVar( cleanKeys[key] )
					_.printBold( 'Error: char0ID is None', 'red' )

				if char1ID is None:
					_.printVar( cleanKeys[key] )
					_.printBold( 'Error: char1ID is None', 'red' )

				if groupID is None:
					_.printVar( cleanKeys[key] )
					_.printBold( 'Error: groupID is None', 'red' )


				# _.printVar( cleanKeys[key] )
				# sys.exit()

				# CHAR - aquire data from 0 

				start = cleanKeys[key][0]['start']
				xLen = 1
				try:
					xLen = len( cleanKeys[key][0]['label'] )
				except Exception as e:
					pass
				end = cleanKeys[key][0]['start'] + xLen
				
				xPos = []
				x = start
				if start == end:
					xPos.append( start )
				else:
					while not x == end:
						xPos.append( x )
						x+=1
				aStart = start
				aEnd = end
				aLen = xLen
				aPos = xPos
				
				# CHAR - aquire data from 1

				start = cleanKeys[key][1]['start']
				xLen = 1
				try:
					xLen = len( cleanKeys[key][1]['label'] )
				except Exception as e:
					pass
				end = cleanKeys[key][1]['start'] + xLen
				
				xPos = []
				x = start
				if start == end:
					xPos.append( start )
				else:
					while not x == end:
						xPos.append( x )
						x+=1
				bStart = start
				bEnd = end
				bLen = xLen
				bPos = xPos

				# GROUP - aquire data

				outer = []
				inner = []

				x = aStart
				while not x == bEnd:
					outer.append( x )
					x+=1
				# if not x >= aEnd+1:
				x = aEnd
				# _.pr( x, bStart-1 )

				if x < bStart:
					while not x == bStart:
						inner.append( x )
						x+=1
				# else:
				#     _.pr( x , bEnd, cleanKeys[key] )


				pass


				# {71FE9636-7C0C-440F-86D9-CDBAF1F51155}
				# {6402B9BC-FF5C-4B6F-B8B4-CB1EFADDF405}

				# CHAR - save index set 0
				self.indexes['char'][char0ID]['total']+=1
				self.indexes['char'][char0ID]['line'].append( cleanKeys[key][0]['line'] )
				self.indexes['char'][char0ID]['end'] = aLen
				self.indexes['char'][char0ID]['start'].append( aStart )
				for x in aPos:
					self.indexes['char'][char0ID]['index'].append( x )

				# CHAR - save index set 1
				self.indexes['char'][char1ID]['total']+=1
				self.indexes['char'][char1ID]['line'].append( cleanKeys[key][1]['line'] )
				self.indexes['char'][char1ID]['end'] = bLen
				self.indexes['char'][char1ID]['start'].append( bStart )
				# if not self.action[ actionIndex[theChar] ]['close']['label'] is None:
				for x in bPos:
					self.indexes['char'][char1ID]['index'].append( x )

				# GROUP - save index
				self.indexes['group'][groupID]['total']+=1

				self.indexes['group'][groupID]['oc'].append({ 'open': aStart, 'close': bStart })

				for x in inner:
					self.indexes['group'][groupID]['inner'].append( x )
				try:
					for x in outer:
						self.indexes['group'][groupID]['index'].append( x )
				except Exception as e:
					_.pr( outer, self.indexes['group'][groupID]['index'] )
				# self.indexes['group'][groupID]['inner'] = bLen


				pass
				# if self.action[ actionIndex[theChar] ]['close']['label'] is None:
				#     _.printVarSimple( cleanKeys[key] )
					


				# _.pr( char0ID, char1ID, groupID )
		# _.printVar( self.indexes )


# [{'label': '{', 'start': 56, 'end': 56, 'id': 56, 'n': 1, 'line': 2}, {'label': '}', 'start': 13729, 'end': 13729, 'id': 56, 'n': 1, 'line': 347}]

# self.indexes = { 'char': [], 'group': [], }

		pass

		self.indexes['totals'] = {}
		self.indexes['totals']['total'] = len( cleanKeys.keys() )

		self.indexes['totals']['group'] = {}
		self.indexes['totals']['char'] = {}

		for record in self.indexes['group']:
			self.indexes['totals']['group'][ record['label'] ] = record['total']

		for record in self.indexes['char']:
			self.indexes['totals']['char'][ record['label'] ] = record['total']

		pass
		self.indexes['language'] = self.language

		self.genitemLabelIndexes()
		# self.testIndexs()



	def genitemLabelIndexes( self ):

		self.indexes['IDs'] = {}
		self.indexes['IDs']['char'] = {}
		self.indexes['IDs']['group'] = {}

		

		for i,record in enumerate(self.indexes['char']):
			self.indexes['IDs']['char'][ self.genLabel( i, 'char' ) ] = i

		for i,record in enumerate(self.indexes['group']):
			self.indexes['group'][i]['open']['iID'] = self.itemLabel( self.indexes['group'][i]['open']['label'], 'char' )
			self.indexes['IDs']['group'][ self.genLabel( i, 'group' ) ] = i
			
			openID = self.genLabel( i, 'group', 'open' )
			if not openID is None:
				self.indexes['IDs']['group'][ openID ] = i

			closeID = self.genLabel( i, 'group', 'close' )
			if not closeID is None:
				self.indexes['IDs']['group'][ closeID ] = i
				self.indexes['group'][i]['close']['iID'] = self.itemLabel( self.indexes['group'][i]['close']['label'], 'char' )



	def testIndexs( self ):
		# return None
		# 875
		# {6402B9BC-FF5C-4B6F-B8B4-CB1EFADDF405}
		for record in self.indexes['char']:
			_.pr()
			_.pr()
			_.colorThis( record['label'] )
			_.colorThis( len(record['index']), 'green' )
			chars = []
			for x in record['index']:
				chars.append( self.asset[x] )
			_.colorThis( ''.join(chars), 'cyan' )


	def buildValidationActionQueue( self, xID ):

		self.action[ self.action_queue ] = self.logistics['action'][xID]

		for i,record in enumerate(self.action[ self.action_queue ]['test']):

			if record['type'] == 'text' and record['strict'] == 1:
				self.action[ self.action_queue ]['test'][i]['data'] = record['data'].lower()

		self.action[ self.action_queue ]['active'] = True
		self.action[ self.action_queue ]['testLen'] = len( self.action[ self.action_queue ]['test'] )
		
		self.scanID[ self.action_queue ] = 0
		self.testID[ self.action_queue ] = 0

		self.action_queue += 1



	def multiLanguageValidation( self ):
		if self.backupLoaded['validation']:
			_.pr( 'Validation Loaded' )
			sys.exit()

		self.scanID = {}
		self.testID = {}
		self.action = {}
		self.action_queue = 0
		self.table = {}


		quoteComment = self.query( quoteComment=True )

		omitIndex = []

		for x in quoteComment:
			for i in self.indexes['group'][x]['index']:
				omitIndex.append( i )


		for xID,record in enumerate(self.logistics['action']):
			if record['language'] == 'global' or record['language'] == self.language:
				self.buildValidationActionQueue( xID )
				# _.printTest( record )



		assetLen = len(self.asset)-1

		whitespace = []
		whitespace.append( ' ' )
		# whitespace.append( '\n' )



		for i,char in enumerate(self.asset):

			if not i in omitIndex:

				aID = 0
				while not aID == ( loopLen ):

					self.action

					if self.action[ aID ]['active']:
						testPass = False
						rulePass = False



						if char in whitespace:
							isWhitespace = True
						else:
							isWhitespace = False

						if self.action[ aID ]['active'][self.testID]['type'] == 'text':
							if self.action[ aID ]['active'][self.testID]['strict']:

								if self.action[ aID ]['active'][self.testID]['strict'] == 1:
									theChar = char.lower()
								else:
									theChar = char

								if self.action[ aID ]['active'][self.testID]['data'][ self.scanID[ str(aID) ] ] == theChar:

									self.scanID[ str(aID) ] += 1
								else:
									self.scanID[ str(aID) ] = 0

								if self.scanID[ str(aID) ] == len(self.action[ aID ]['active'][self.testID]['data']):
									self.scanID[ str(aID) ] = 0
									testPass = True
							else:
								pass



						if testPass:
							self.action[ self.action_queue ]['testLen']
							rulePass = True



					aID+=1

	# def reactivateActionItems( self ):



	def reactivateActionItems( self ):
		aID = 0
		while not aID == ( loopLen ):
			self.action[aID]['active'] = True
			aID+=1

	def javascriptNamespace( self ):
		# for record in self.indexes['group']:
		#     _.pr( record['label'] )
		# return None

		#############
		# validation = self.runRules( self.asset, 'scan', shouldLoop=True )
		# return None
		#############




		
		# if self.backupLoaded['validation']:
		#     _.pr( 'Validation Loaded' )
		#     sys.exit()

		# self.multiLanguageValidation()

		# _.pr( self.indexes['carriageIndex'].keys() )

		# _.pr( self.indexes['carriageIndex'] )



		# notFound = []
		# allIndexes = []
		# for record in self.indexes['char']:
		#     for i in record['index']:
		#         allIndexes.append( i )

		# for i in self.relevantPos:
		#     if not i in allIndexes:
		#         notFound.append( i )
		# _.pr( notFound )
		# for i in notFound:
		#     _.pr( self.asset[i] )



		# return None


		commentIndex = []

		xIDs = self.query( tag='comment,inline comment', justIDs=True, special='all' )



		for x in xIDs:
			for i in self.indexes['group'][x]['index']:
				commentIndex.append( i )



		equal = self.indexes['char'][ self.query( '=', justIDs=True, isChar=True ) ]
		braces = self.indexes['char'][ self.query( '{', justIDs=True, isChar=True ) ]
		

		items = set(equal['index']) & set(self.indexes['allClosed'])

		lines = []

		for x in items:
			lines.append( self.getLine( x ) )


		flaggedLines = set(lines) & set( braces['line'] )

		# {4B2E8584-8EF6-4AA3-BBC0-4F89160AF12B}


		namespaceRecords = []

		x = self.indexes['carriageIndex'].keys()


		car = []
		# car.append( 0 )
		for x in self.indexes['carriageIndex']['index']:
			car.append( x )



		self.genitemLabelIndexes()

		for line in flaggedLines:
			data = self.assetSnipetLine( line )

			pos = data['text'].index( '{' )+data['start']

			groupID = self.itemLabel( '{}', 'group' )

			record = self.indexes['group'][groupID]

			oc = list(filter(lambda data: data['open'] == pos, record['oc']))

			ns = data['text'].split('=')[0]
			ns = ns.replace( ' ', '' ).replace( '\n', '' )

			namespaceRecords.append({ 'ns': ns, 'open': oc[0]['open'], 'close': oc[0]['close'] })



		for i,ns in enumerate(namespaceRecords):
			if not i:
				
				validation = self.runRules( {'open': ns['open']+1, "close": ns['close']-1}, 'validate namespace' )
				_.pr( text )

				
		# _.printTest( namespaceRecords )



	def runRules( self, on, run, returnFirst=False, shouldLoop=False, scanStart=None, scanEnd=None ):
		self.rlID += 1
		rID = self.rlID
		startOn = 0
		self.rls[rID] = {
							'action': {},
							'scanID': {},
							'testID': {},
							'rulePass': {},
							'pattern': {},
							'data': {},
		}


		if type( on ) == dict:
			asset = self.assetSnipet( on['open'], on['close'] )
			startOn = on['open']
		elif type( on ) == str:
			asset = on
		elif type( on ) == list:
			startOn = on[0]['open']
			asset = self.assetSnipet( on[0]['open']+1, on[0]['close']-1 )


		# _.pr( asset )

		rulesIDs = []
		if type( run ) == str:

			for i,record in enumerate(self.logistics['rules']):
				if record['description'] == run:
					if record['language'] == 'global' or record['language'] == self.language:
						rulesIDs.append( i )

		elif type( run ) == list:

			for rl in run:
				if type( rl ) == int:

					for i,record in enumerate(self.logistics['rules']):
						if record['id'] == rl:
							if record['language'] == 'global' or record['language'] == self.language:
								rulesIDs.append( i )


				elif type( rl ) == str:

					for i,record in enumerate(self.logistics['rules']):
						if record['description'] == rl:
							if record['language'] == 'global' or record['language'] == self.language:
								rulesIDs.append( i )

		elif type( run ) == int:
			for i,record in enumerate(self.logistics['rules']):
				if record['id'] == run:
					if record['language'] == 'global' or record['language'] == self.language:
						rulesIDs.append( i )



		def buildRuleActionQueue( self, i, rID, theRule ):

			# _.colorThis( [ rID, self.rlID ], 'red' )

			self.rls[rID]['action'][ i ] = theRule

			for ii,record in enumerate(self.rls[rID]['action'][ i ]['patterns']):

				if record['type'] == 'text' and record['strict'] == 1:
					self.rls[rID]['action'][ i ]['patterns'][ii]['test'] = record['test'].lower()

			self.rls[rID]['action'][ i ]['active'] = True
			self.rls[rID]['action'][ i ]['testLen'] = len( self.rls[rID]['action'][ i ]['patterns'] )
			
			self.rls[rID]['scanID'][ i ] = 0
			self.rls[rID]['testID'][ i ] = 0
			self.rls[rID]['rulePass'][ i ] = False
			self.rls[rID]['pattern'][ i ] = False
			self.rls[rID]['data'][ i ] = []



		omitIndex = []
		for xID in self.query( tag='comment,inline comment', justIDs=True, special='all' ):
			for x in self.indexes['group'][xID]['index']:
				omitIndex.append( x )
			


		scanID = {}
		testID = {}
		action = {}
		action_queue = 0
		table = {}
		for i,iX in enumerate(rulesIDs):
			buildRuleActionQueue( self, i, rID, self.logistics['rules'][iX] )


		# _.pr( type(self.rls[rID]['action']) )
		# _.printTest( self.rls[rID]['action'], x=0 )
		# _.pr( type(self.rls[rID]['action']) )

		loopLen = len( self.rls[rID]['action'].keys() )
		# _.pr( loopLen )


		assetLen = len(asset)-1

		ws = []
		ws.append( ' ' )
		ws.append( '\n' )
		# whitespace.append( '\n' )
		# for i,char in enumerate(asset):

		# {C82DBFC2-BCD5-4885-88B7-90604D69CDDB}
		skippedWS = False
		records = []
		loopCount=0
		loopICount=0
		data = {}
		i=0
		if not scanStart is None:
			i=scanStart
			startOn = scanStart
		if not scanEnd is None:
			assetLen = scanEnd

		text = self.assetSnipet( startOn, assetLen, asset )
		_.colorThis( text, 'purple' )

		while not i == assetLen:
			# _.pr( i, asset[i] )
			loopICount+=1

			ii=i


			if not startOn+i in omitIndex:

				if asset[i] in ws:
					skippedWS = True
				else:
					# _.pr( asset[i], end='' )
					# _.pr( aID ,loopLen )
					aID = 0
					allFail = True
					while not aID == loopLen:

						# 6
						
						_.colorThis( self.rls[rID]['action'][aID], 'Color.yellow' )
						# _.printTest( self.rls[rID]['action'][aID], x=0 )
						pass

						if self.rls[rID]['action'][aID]['active']:



							loopCount+=1
							
							testID = self.rls[rID]['testID'][aID]

							# _.colorThis( [ self.rls[rID]['description'], testID ], 'Color.yellow' )
							if self.rls[rID]['action'][aID]['patterns'][testID]['strict'] == 1:
								theChar = asset[i].lower()
							else:
								theChar = asset[i]

							# {20E19A90-3070-4181-A3AC-591C186977EF}
							_.pr( '___ A', self.rls[rID]['action'][aID]['patterns'][testID]['type'], aID, testID, loopCount, loopICount, i, asset[i] )
							


							if self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'text':

								# _.printTest( 'here', l=2029 )
								if self.rls[rID]['action'][aID]['patterns'][testID]['strict']:



									if self.rls[rID]['action'][aID]['patterns'][testID]['test'][ self.rls[rID]['scanID'][aID] ] == theChar:

										self.rls[rID]['scanID'][aID] += 1
									else:
										self.rls[rID]['scanID'][aID] = 0
										self.rls[rID]['action'][aID]['active'] = False
										_.pr( 'Fail 01', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
										# _.printTest( self.rls[rID]['action'][aID]['patterns'][testID] )
										self.rls[rID]['data'][aID] = []

									if self.rls[rID]['scanID'][aID] == len(self.rls[rID]['action'][aID]['patterns'][testID]['test']):
										
										self.rls[rID]['pattern'][aID] = True
										
								else:
									# _.pr( 'pre' )
									if asset[i] in self.rls[rID]['action'][aID]['patterns'][testID]['test']:

										self.rls[rID]['scanID'][aID] += 1
										# _.pr( 'post', self.rls[rID]['scanID'][aID] )
									elif self.rls[rID]['scanID'][aID]:
										# _.pr()
										# self.rls[rID]['scanID'][aID] -= 1
										if self.rls[rID]['scanID'][aID]:


											self.rls[rID]['pattern'][aID] = True
											i-=1
											_.colorThis( 'back', 'red' )
										else:
											self.rls[rID]['scanID'][aID] = 0
											self.rls[rID]['action'][aID]['active'] = False
											_.pr( 'Fail 02', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
											# _.printTest( self.rls[rID]['action'][aID]['patterns'][testID] )
											self.rls[rID]['data'][aID] = []

									else:
										_.pr( 'asdf test' )
							elif self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'index':
								_.pr( 'index HERE' )

								if self.rls[rID]['action'][aID]['patterns'][testID]['test'][ self.rls[rID]['scanID'][aID] ] == theChar:
									self.rls[rID]['scanID'][aID] += 1
								else:
									self.rls[rID]['scanID'][aID] = 0
									self.rls[rID]['action'][aID]['active'] = False
									_.pr( 'Fail 03', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
									# _.printTest( self.rls[rID]['action'] )
									# _.printTest( self.rls[rID]['action'][aID]['patterns'][testID] )
									self.rls[rID]['data'][aID] = []

								if self.rls[rID]['scanID'][aID] == len(self.rls[rID]['action'][aID]['patterns'][testID]['test']):
									_.pr( 'works' )
									self.rls[rID]['pattern'][aID] = True

									
							elif self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'scan':

								# {7F41946A-F2F2-4D71-B7E0-765D3109BC86}

								_.colorThis( '\nSTARTING SCAN\n', 'cyan' )
								_.pr( i+1, asset[i], startOn, asset[ i+startOn ] )
								scan =self.runRules( self.asset, self.rls[rID]['action'][aID]['patterns'][testID]['test'], returnFirst=True, scanStart=i+startOn, scanEnd=None )

								_.colorThis( '\nSCAN COMPLETE\n', 'darkcyan' )

								_.pr( scan )

								self.rls[rID]['pattern'][aID] = True



							if self.rls[rID]['pattern'][aID]:
								# _.printTest( self.rls[rID] )
								_.colorThis( [ self.rls[rID]['action'][aID]['tags'], testID ], 'white' )
								_.colorThis( [ 'pattern', asset[ii] ], 'green' )


								if self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'text':
									_.pr( 'pattern text' )
									text = self.assetSnipet( i-self.rls[rID]['scanID'][aID], i, asset )
									_.colorThis( [ 'text:', text ], 'cyan' )
									self.rls[rID]['data'][aID].append({ 'id': self.rls[rID]['action'][aID]['id'], 'pattern': testID, 'data': text })
								
								elif False and self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'index':
									_.pr( 'pattern index' )
									# i+startOn


									oc = list(filter(lambda data: data['open'] == startOn+i, self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc']))
									try:
										pass
									except Exception as e:
										_.printVarSimple( self.rls[rID]['action'][aID] )



										# data = self.assetSnipetLine( line )
										# oc = list(filter(lambda data: data['open'] == startOn+i, self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc']))
									# try:
									#     # oc = list(filter(lambda data: data['open'] == startOn+i, self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc']))
									# except Exception as e:
									#     _.pr('\n\n\n')
									#     _.pr( "data['open']", data['open'] )
									#     _.pr( "self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc']", self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc'] )
									#     sys.exit()
									#     pass
									self.rls[rID]['data'][aID].append({ 'id': self.rls[rID]['action'][aID]['id'], 'pattern': testID, 'data': oc })
									# text = self.assetSnipet( 0, startOn+i, self.asset )
									text = self.assetSnipet( oc[0]['open'], oc[0]['close'], asset )
									_.colorThis( [ 'text:', text ], 'cyan' )
									_.pr( text )
									_.pr( rID, self.rlID, i, startOn+i, asset[i], oc, self.itemLabel( asset[i], 'group' ), self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc'] )
									_.pr( oc[0]['close'] )
									i = oc[0]['close'] + 1
								elif self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'scan':
									text = self.assetSnipet( oc[0]['open'], oc[0]['close'], self.asset )
									_.colorThis( [ 'text:', text ], 'cyan' )
									pass

									

								if len( self.rls[rID]['action'][aID]['patterns'][testID]['rules'] ) and not self.rls[rID]['action'][aID]['patterns'][testID]['type'] == 'scan':

									# text = self.assetSnipet( oc[0]['open'], oc[0]['close'], asset )
									# _.pr( text )
									_.colorThis( '\nSTARTING RULES\n', 'cyan' )
									scan =self.runRules( self.asset, self.rls[rID]['action'][aID]['patterns'][testID]['rules'], returnFirst=True, scanStart=oc[0]['open'], scanEnd=oc[0]['close'] )
									# self.runRules( oc, self.rls[rID]['action'][aID]['patterns'][testID]['rules'] )

								if returnFirst:
									records.append( self.rls[rID]['data'][aID] )
									return records

								# _.printTest( text )
								self.rls[rID]['scanID'][aID] = 0
								# _.printTest( 'pattern', l=2061 )
								if self.rls[rID]['testID'][aID] == len(self.rls[rID]['action'][aID]['patterns'])-1:
									self.rls[rID]['testID'][aID] = 0
									_.colorThis( 'Zero Test', 'green' )
									self.rls[rID]['rulePass'][aID] = True
								else:
									self.rls[rID]['testID'][aID]+=1
									testID = self.rls[rID]['testID'][aID]
									# _.pr( 'testID +', self.rls[rID]['testID'][aID], aID )



							if self.rls[rID]['action'][aID]['loop']:
								self.rls[rID]['action'][aID]['active'] = True

							elif self.rls[rID]['rulePass'][aID]:
								records.append( self.rls[rID]['data'][aID] )

								# _.printTest( records )

								if returnFirst:
									return records

								self.rls[rID]['data'][aID] = []


								if shouldLoop:
									aIDx = 0
									while not aIDx == loopLen:
										self.rls[rID]['action'][aIDx]['active'] = True
										aIDx+=1


								# _.printTest( 'rulePass', l=2061 )

							# {20E19A90-3070-4181-A3AC-591C186977EF}
							_.pr( '___ B', self.rls[rID]['action'][aID]['patterns'][testID]['type'], aID, testID, loopCount, loopICount, i, asset[i] )
							# _.printTest( self.rls[rID]['action'], x=0 )
						pass
						# _.pr( rID, self.rlID )
						# _.pr( aID )
						# _.colorThis( [ rID, self.rlID ], 'red' )
						# _.colorThis( [ rID, self.rlID ], 'red' )
						# _.printTest( self.rls[rID] )
						# if self.rls[rID]['action'][aID]['active']:
						if self.rls[rID]['action'][aID]['active']:
							allFail = False

						aID+=1
						pass
						# 6
					pass
					skippedWS = False
					if allFail:
						_.pr( testID )
						_.colorThis( [ 'All Fail', scanStart ], 'red' )
						return records
			pass
			i+=1
		_.colorThis( 'All Pass', 'green' )
		return records



	def assetSnipetLine( self, line ):

		pos = self.getLineStartEnd( line )
		snippet = self.assetSnipet( pos['start'], pos['end'] )
		return { 'start': pos['start'], 'end': pos['end'], 'text': snippet }

	def assetSnipet( self, start, end, asset='' ):
		end+=1
		if not asset:
			asset = self.asset
		result = ''

		x = start

		while not x == end:
			try:
				result += asset[x]
			except Exception as e:
				_.pr( asset )
				_.colorThis( [ len(asset), start, end, 'self.assetSnipet' ], 'red' )
				return None
				
				# result += asset[len(asset)-1]
			x+=1

		return result

	def assetSnipetClean( self, start, end, asset='' ):
		if not len( self.omitIndex ):
			self.genOmit()
		end+=1
		if not asset:
			asset = self.asset
		result = ''

		x = start

		while not x == end:
			if not x in self.omitIndex:
				result += asset[x]
			x+=1

		return result

	def genOmit( self ):

		if not len( self.omitIndex ):

			self.omitIndex = []
			# _.pr( self.indexes['group'][0].keys() )
			# sys.exit()
			for i,record in enumerate(self.indexes['group']):
				should = 0
				for tag in record['tags']:
					if 'comment' in tag or 'quote' in tag:
						should = 1
				if should:
					for ix in record['index']:
						self.omitIndex.append( ix )



	def itemLabel( self, index, what ):
		try:
			return self.indexes['IDs'][what][index]
		except Exception as e:
			pass
			# _.colorThis( 'Error: noIndex', 'red' )
			# sys.exit()
			# for record in self.noIndex:
			#     if what == record['label']:
			#         return record['index']
		# _.printBold( 'Error: itemLabel: ' + str(index) +' '+ str(what), 'red' )
		return None


			
	def genLabel( self, i, what, oc=None ):
		test = {}
		label = None

		if oc is None:
			try:
				test[ self.indexes[what][i]['label'] ] = None
				label = self.indexes[what][i]['label']
			except Exception as e:
				label = i
				self.noIndex.append({ 'index': i, 'label': self.indexes[what][i]['label'] })
			return label
		else:

			try:
				if 'open' in oc:
					label = self.indexes[what][i]['open']['label']
				else:
					if self.indexes[what][i]['close']['label'] is None:
						label = None
					else:
						label = self.indexes[what][i]['close']['label']
			except Exception as e:
				_.colorThis( 'Error: noIndex', 'red' )
				sys.exit()
				# label = i
				# self.noIndex.append({ 'index': i, 'label': self.indexes[what][i]['label'] })
				# _.pr( 'line: 1686, self.noIndex' )
			# _.pr( 'genLabel:', i, label, self.indexes[what][i]['label'] )
			return label

	def auditTable( self ):
		

		try:
			self.table.keys()
		except Exception as e:
			# _.printBold( 'Error auditTable: Loaded from backup', 'red' )
			return False


		cleanKeys = {}
		for key in self.table.keys():
			for x in self.table[ key ]:
				try:
					cleanKeys[x['id']].append( x )
				except Exception as e:
					cleanKeys[x['id']] = []
					cleanKeys[x['id']].append( x )
				# _.printVar( x )
				# sys.exit()


		test = [0,1]
		if 0 in test:
			theTotals = {}
			for key in cleanKeys.keys():

				try:
					theTotals[ str(len(cleanKeys[key])) ] += 1
				except Exception as e:
					theTotals[ str(len(cleanKeys[key])) ] = 1


			for key in theTotals.keys():
				_.pr( key, theTotals[key] )


		if 1 in test:


			for key in cleanKeys.keys():
				if not len( cleanKeys[key] ) == 2:
					_.printBold( '_________________________________________', 'red' )
					_.pr( 'line:', _.inlineBold(str(cleanKeys[key][0]['line']), 'green')  )
					_.pr( len( cleanKeys[key] ), cleanKeys[key] )
					self.printPos( cleanKeys[key][0]['start']-20, cleanKeys[key][0]['start']+20 )
		
		if 2 in test:

			for key in cleanKeys.keys():
				if len( cleanKeys[key] ) == 2 and cleanKeys[key][0]['label'] == "'":
					_.pr( 'line:', _.inlineBold(str(cleanKeys[key][0]['line']), 'green')  )
					self.printPos( cleanKeys[key][0]['start'], cleanKeys[key][1]['end'] )



	def buildIndexes2( self ):
# *******************************************************************************************************
#         solution

#         self.findStringInAsset()


#         do inline comment and quote at the same time 
#         just do the if statements in the right order
#         collent non-omit ids in process
# *******************************************************************************************************



		self.index_structure = { 
									'char': { 
												'line': [],
												'index': [],
												'end': [],
												'label': '',
											},
									'group': { 
												'open': {
															'label': '',
															'rID': None,
															'iID': None,
															'pIDs': [],
												},
												'close': {
															'label': '',
															'rID': None,
															'iID': None,
															'pIDs': [],
												},
												'tags': [],
												'index': [],
												'inner': [],
												'groups': [],
												'nestable': None,
												'escape': None,
												'label': '',
											}
							}



		self.indexes = { 'char': [], 'group': [], }

		carriage = {
						'index': [],
						'line': [],
						'label': ''
		}

		line = 0
		for i,char in enumerate(self.asset):
			carriage['line'].append( line )

			if char == '\n':
				line += 1
				carriage['index'].append( i )


		# self.indexes['char'].append( carriage )
		self.buildIndexStructure()

		lookForSingle = []
		lookForMulti = []
		who = {}
		end = {}
		table = {}
		scan = {}
		i = {}
		for i,record in enumerate(self.indexes['char']):
			scan[record['label']] = 0
			table[record['label']] = []
			end[record['label']] = []
			if len( record['label'] ) == 1:
				lookForSingle.append( record['label'] )
			else:
				lookForMulti.append( record['label'] )


		
		for i,char in enumerate(self.asset):
			for single in lookForSingle:
				table[single].append( i )

			for multi in lookForMulti:


				if multi[ scan[multi] ] == char:
					scan[multi] += 1
				else:
					scan[multi] = 0
				if scan[multi] == len(multi):
					end[multi].append( i )
					table[multi].append( i-len(multi)-1 )
					scan[multi] = 0

		# for i,char in enumerate(self.asset):
		#     for key in table.keys():
		#         if i in table[key]:
		#             pass

		# for key in table.keys():
		#     for 

		_.pr( 'done' )
		sys.exit()



		# _.printVar( self.indexes )
		# sys.exit()

		# for i,record in enumerate(self.indexes['group']):
		#     if 'inline comment' in record['tags']:
		#         done = False
		#         i = 0
		#         openID = record['open']['iID']
		#         while not done:
		#             if not openID is None and not self.indexes['char'][ openID ]['index']:
		#                 pos = self.asset.find( record['open']['label'] )
		#                 if not pos == -1:
		#                     self.indexes['char'][ openID ]['index'].append( pos )
		#                     self.indexes['char'][ openID ]['line'].append( carriage['line'][i] )
		#                     x = i
		#                     while not i == carriage['index'][ carriage['line'][i] ]:
		#                         self.indexes['group'][i]['index'].append( x )
		#                         x += 1
		indexes = self.indexes
		for i,record in enumerate(indexes['group']):
			if 'comment' in record['tags']:

				done = False
				i = 0

				endAdd = len( record['open']['label'] )-1
				openID = record['open']['iID']
				try:
					closeID = record['close']['iID']
					pass
				except Exception as e:
					_.printVar( record )
					sys.exit()
				index = []
				end = []
				line = []
				while not done:
					if not openID is None and not indexes['char'][ openID ]['index']:
						pos = self.asset.find( record['open']['label'] )
						posEnd = pos + endAdd
						if not pos == -1:
							index.append( pos )
							end.append( posEnd )
						else:
							done = True
							# line.append( carriage['line'][i] )
				self.indexes['char'][ openID ]['index'] = index
				self.indexes['char'][ openID ]['end'] = end
				# self.indexes['char'][ openID ]['line'] = line
				if not record['close']['label'] is None:
					endAdd = len( record['close']['label'] )-1
					index = []
					end = []
					line = []
					while not done:
						if not closeID is None and not indexes['char'][ closeID ]['index']:
							pos = self.asset.find( record['close']['label'] )
							posEnd = pos + endAdd
							if not pos == -1:
								index.append( pos )
								end.append( posEnd )
							else:
								done = True
								# line.append( carriage['line'][i] )
					self.indexes['char'][ openID ]['index'] = index
					self.indexes['char'][ openID ]['end'] = end
				# self.indexes['char'][ openID ]['line'] = line
				# pass

				# group = []
				# for ia,char in enumerate(self.asset):
				#     if group and ia in self.indexes['char'][ closeID ]['end']:
				#         group.append( ia )
				#         self.indexes['group'][i]['groups'].append( group )
				#         group = []
				#     if not group and ia in self.indexes['char'][ openID ]['index']:
				#         group.append( ia )



# inner
						


		_.printVar( self.indexes )


# in future be mindful of order example """ should be run befor "


# self.query( tag='carriage', justIDs=True )
# self.query( tag='inline comment', justIDs=True )
# self.query( tag='comment', justIDs=True )
# self.query( label='\n', justIDs=True )

		# order:
		#         self.query( 'carriage', justIDs )


	def inIndex( self, label=None, iID=None, gID=None, rID=None, pID=None, tag=None, oc='open,close', cg='char,group' ):


		oc = oc.lower()
		if not iID is None:

			try:
				self.indexes['char'][iID]
			except NameError:
				return False
			else:
				return True

		if not label is None and not pID is None and not gID is None:

			if not self.inIndex( label=label ):
				_.pr( 'Error: test for label first' )
				sys.exit()
			if not self.inIndex( gID=gID ):
				_.pr( 'Error: test for gID first' )
				sys.exit()

				if pID in self.indexes['group'][gID]['open']['pIDs']:
					return True

		if not label is None and not pID is None:

			if not self.inIndex( label=label ):
				_.pr( 'Error: test for label first' )
				sys.exit()

				for item in self.indexes['group']:
					if item['label'] == label:
						if 'open' in oc:
							if pID in item['open']['profiles']:
								return True
						if 'close' in oc:
							if pID in item['close']['profiles']:
								return True

		elif not rID is None and not gID is None:

			if not self.inIndex( gID=gID ):
				_.pr( 'Error: test for gID first' )
				sys.exit()
			if 'open' in oc:
				if self.indexes['group'][gID]['open']['rID'] == rID:
					return True
			if 'close' in oc:
				if self.indexes['group'][gID]['close']['rID'] == rID:
					return True

		elif not rID is None:

			for char in self.indexes['group']:
				if 'open' in oc:
					if char['open']['rID'] == rID:
						return True
				if 'close' in oc:
					if char['close']['rID'] == rID:
						return True

		elif not gID is None:

			try:
				self.indexes['group'][gID]
			except NameError:
				return False
			else:
				return True

		elif not label is None:

			if 'group' in cg:
				for item in self.indexes['group']:
					if item['label'] == label:
						return True
			if 'char' in cg:
				for item in self.indexes['char']:
					if item['label'] == label:
						return True

		elif not tag is None:

			for char in self.indexes['group']:
				if char['label'] == label:
					if tag in char['tags']:
						return True
		return False
	def buildIndexStructure( self, comment=False, quote=False ):

	
		for rID,record in enumerate(self.logistics['characters']):
			for pID,profile in enumerate(record['profiles']):
				if profile['language'] == self.language or profile['language'] == 'global':
					if profile['isOpen']:
						indexes = { 
										'open': {
													'label': '',
													'rID': None,
													'iID': None,
													'pIDs': [],
										},
										'close': {
													'label': '',
													'rID': None,
													'iID': None,
													'pIDs': [],
										},
										'total': 0,
										'tags': [],
										'oc': [],
										'index': [],
										'inner': [],
										'groups': [],
										'nestable': None,
										'escape': None,
										'label': '',
						}
						charIndexes = {
										'total': 0,
										'index': [],
										'start': [],
										'end': 1,
										'line': [],
										'label': ''
						}
						charIndexesC = {
										'total': 0,
										'index': [],
										'start': [],
										'end': 1,
										'line': [],
										'label': ''
						}
						indexes['open'] = {}
						indexes['close'] = {}
						indexes['open']['pIDs'] = []
						indexes['close']['pIDs'] = []
						indexes['close']['label'] = None

						charIndexes['label'] = record['char']
						indexes['label'] = record['char']
						indexes['open']['label'] = record['char']
						indexes['open']['rID'] = rID
						indexes['open']['pIDs'].append( pID )
						indexes['tags'] = profile['tags']
						indexes['nestable'] = profile['nest']
						indexes['escape'] = ''
						for charID in profile['escape']:
							indexes['escape'] +=self.charById( charID )['char']
							


						for charID in profile['set']:
							char = self.charById( charID )['char']
							charIndexes['label'] += char
							indexes['label'] += char
							indexes['open']['label'] += char

						if not type(profile['groupID']) == bool:

							pass
							for rIDc,recordC in enumerate(self.logistics['characters']):
								for pIDc,profileC in enumerate(recordC['profiles']):
									if not type(profileC['groupID']) == bool and profileC['groupID'] == profile['groupID'] and not profileC['isOpen']:
										charIndexesC['label'] = recordC['char']
										indexes['label'] += recordC['char']
										indexes['close']['label'] = recordC['char']
										indexes['close']['rID'] = rIDc
										indexes['close']['pIDs'].append( pIDc )
										# _.pr( pIDc )

										for charID in profileC['set']:
											char = self.charById( charID )['char']
											charIndexesC['label'] += char
											indexes['label'] += char
											indexes['close']['label'] += char
						

						pass
						self.addRecords( indexes, charIndexes, charIndexesC )


	
							# _.printVar( self.indexes )
							# sys.exit()

 # or lan['language'] == 'global':

	def addRecords( self, indexes, charIndexes, charIndexesC ):
		if not self.inIndex( label=indexes['open']['label'] ):
			# _.pr( indexes['label'],charIndexes['label'] )
			# _.printVar( charIndexes )
			# pause=input('pause')
			self.indexes['char'].append( charIndexes )
			xID = self.query( label=indexes['open']['label'], justIDs=True )
			indexes['open']['iID'] = xID['iID']
			if not indexes['close']['label'] is None:
				if not self.inIndex( label=indexes['close']['label'] ):
					self.indexes['char'].append( charIndexesC )

				xID = self.query( label=indexes['close']['label'], justIDs=True )
				indexes['close']['iID'] = xID['iID']
			self.indexes['group'].append( indexes )
		else:
			xID = self.query( label=indexes['label'], justIDs=True )
			if not xID['gID'] is None and not self.inIndex( gID=xID['gID'], pID=pID, oc='open' ):
				self.indexes['group'][xID['gID']]['open']['pIDs'].append( pID )
				for tag in indexes['tags']:
					self.indexes['goup'][xID['gID']]['tags'].append( tag )

			if not self.inIndex( gID=xID['gID'], pID=pIDc, oc='close' ):
				self.indexes['goup'][xID['gID']]['close']['pIDs'].append( pIDc )

			if not self.inIndex( label=indexes['close']['label'] ):
				pass
		pass
		# _.pr( x )
		# sys.exit()
		if not indexes['close']['label'] is None:
			if not self.inIndex( label=indexes['close']['label'] ):
				self.indexes['char'].append( charIndexesC )
		if not self.inIndex( label=indexes['open']['label'] ):
			self.indexes['char'].append( charIndexes )
		pass



	def omitTickets( self ):
		self.omitRanges = []
		closed = 0
		for i,ticket in enumerate(self.locationTable):
			if not ticket['isOpen']:
				self.omitRanges.append({ 'start': ticket['start'], 'end': ticket['end'], })
				closed+=1
		_.pr( 'closed:', closed )



	def buildLocationTable( self ):
		relevantTable = self.relevantTable
		end = len(self.asset)-1

		self.tickets = {
							'open': {},
							'closeOn': {},
							'scanningFor': { 'char': [], 'multi': [] },
							'records': [],
							'closed': 0,
		}
		zNoNestActive = ''
		for relevant in self.relevantTable['char']:
			self.tickets['open'][relevant] = 0


		for i in self.idCache:
			char = self.asset[i]
			if True:
				if not len(zNoNestActive) and char in self.relevantTable['char']:
					shouldProcess = False
					record = False
					for check in self.relevantTable['records']:
						if check['char']  == char:
							hasSet = False
							for lan in check['profiles']:
								if len(lan['set']):
									xx=i
									for theID in lan['set']:
										xx+=1
										if not xx > end:
											if self.asset[xx] == self.charById( theID )['char']:
												hasSet = True
												recordSet = lan
												shouldProcess = True
												break
								else:
									record = lan
									shouldProcess = True
							if hasSet:
								record = recordSet
							break


					if shouldProcess:
						if len( record['escape'] ):
							xx=i
							record['escape'].reverse()
							for eID in record['escape']:
								xx-=1
								if xx > 0:
									if self.asset[xx] == self.charById( eID )['char']:
										shouldProcess = False


					if shouldProcess:
						lan = record
						if type(lan['groupID']) == bool:
							close = { 'char': char , 'lan': lan }
						else:
							close = self.charByGroupIdClose( lan['groupID'] )



						if type(close) == bool:
							_.pr( 'Error: line 292... ish' )
							sys.exit()
						if not close['char'] in self.tickets['scanningFor']['char']:
							self.tickets['scanningFor']['char'].append( close['char'] )
						if len(close['lan']['set']):
							if not close['char'] == self.tickets['scanningFor']['multi']:
								self.tickets['scanningFor']['multi'].append( close['char'] )
						self.tickets['records'].append({  
															'start': i,
															'end': False,
															'isOpen': True,
															'closeOn': self.tickets['open'][char],
															'char': char,
															'lan': close['lan'],
															'closeChar': close['char']
														})
						pass
						self.tickets['open'][char] += 1


						if not record['nest']:
							zNoNestActive = close['char']



################################################################################################
				if char in self.tickets['scanningFor']['char']:

					shouldProcess = True
					cID = None
					for ic,check in enumerate(self.tickets['records']):
						if check['isOpen'] and check['start'] < i  and check['closeChar']  == char and check['closeOn'] == (self.tickets['open'][ check['char'] ]-1):
						# if check['isOpen'] and check['start'] < i  and check['closeChar']  == char :
						# if check['isOpen'] and check['closeChar']  == char:
							cID = ic
							if len( check['lan']['escape'] ):
								xx=i
								check['lan']['escape'].reverse()
								for eID in check['lan']['escape']:
									xx-=1
									if xx > 0:
										if self.asset[xx] == self.charById( eID )['char']:
											shouldProcess = False



					if not cID is None:
						groupLength = 1
						if char in self.tickets['scanningFor']['multi']:
							found = False
							if self.tickets['records'][cID]['closeChar']  == char:
								xx=i

								for theID in self.tickets['records'][cID]['lan']['set']:
									xx+=1
									if not xx > end:
										if self.asset[xx] == self.charById( theID )['char']:
											groupLength+=1
											found = True

							if not found:
								shouldProcess = False
					if shouldProcess and not cID is None:

						zNoNestActive = ''

						self.tickets['open'][self.tickets['records'][cID]['char']] -= 1

						self.tickets['closed']+=1


						self.tickets['records'][cID]['end'] = i
						self.tickets['records'][cID]['isOpen'] = False

						self.locationTable.append( self.tickets['records'][cID] )
						self.tickets['records'].pop( cID )


	def findCloseByChar( self, char ):
		
		for record in self.logistics['characters']:
			if record['char'] == char:
				for lan in record['profiles']:
					if lan['language'] == self.language or lan['language'] == 'global':
						if lan['isOpen']:
							if not type(lan['groupID']) == bool:
								return self.charByGroupIdClose( lan['groupID'] )
							else:
								return { 'char': record['char'] , 'lan': lan }
							
		return False

	def charByGroupIdClose( self, groupID ):
		

		found = False
		for i,record in enumerate(self.logistics['characters']):
			for lan in record['profiles']:
				if lan['groupID'] == groupID and not lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
		return False

	def charByGroupIdOpen( self, groupID ):
		
		for record in self.logistics['characters']:
			for lan in record['profiles']:
				if lan['groupID'] == groupID and lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
					
		return False



	def inCommentRange( self, i ):
		for omit in self.omitRanges:
			if i >= omit['start'] and i <= omit['end']:
				return True
		return False


	def buildRelevantTable( self, comment=False, quote=False ):
		self.relevantTable = { 'char': [], 'multi': [], 'records': [] }
		if not comment and not quote:
			for record in self.logistics['characters']:
				isRelevant = False
				profiles = []
				for lan in record['profiles']:
					if lan['language'] == self.language or lan['language'] == 'global':
						tagList = []
						if lan['isOpen']:
							isRelevant = True
							profiles.append( lan )
							if len(lan['set']):
								pass

				if isRelevant:    
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )

		elif comment:
			for record in self.logistics['characters']:
				isRelevant = False
				profiles = []
				for lan in record['profiles']:
					if lan['language'] == self.language:
						isComment = False
						tagList = []
						for tag in lan['tags']:
							if 'comment' in tag:
								isRelevant = True
								profiles.append( lan )

				if isRelevant:    
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )


		elif quote:
			for record in self.logistics['characters']:
				isRelevant = False
				profiles = []
				for lan in record['profiles']:
					if lan['language'] == self.language or lan['language'] == 'global':
						isComment = False
						tagList = []
						for tag in lan['tags']:
							if 'quote' in tag:
								isRelevant = True
								profiles.append( lan )

				if isRelevant:    
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )


	def shouldScan( self, char ):
		record = charByChar( char )

	def charByChar( self, char ):
		
		for record in self.logistics['characters']:
			if record['char'] == char:
				return record    
		return False

	def buildMultilineComments( self ):
		
		for record in self.logistics['characters']:
			charSet = record['char']
			theOpen = record['char']
			for lan in record['profiles']:
				if lan['language'] == self.language:
					isComment = False
					tagList = []
					if lan['isOpen'] and 'comment' in lan['tags'] :
						_.pr( lan['tags'] )
						tagList.append( 'comment' )
						isComment = True
						theClose = ''
						if type(lan['set']) == list and len( lan['set'] ):
							for setID in lan['set']:
								if type(setID) == int:
									nextChar = self.charById( setID )['char']
									if type( nextChar ) == str:
										theOpen += nextChar
						if not type(lan['groupID']) == bool:
							groupInfo = self.charByGroupIdClose( lan['groupID'] )
							if not type(groupInfo) == bool:
								theClose += groupInfo['char']
								if len( groupInfo['lan']['set'] ):
									for groupSetId in groupInfo['lan']['set']:
										if type(groupSetId) == int:
											nextChar = self.charById( groupSetId )['char']
											if type( nextChar ) == str:
												theClose += nextChar

						if isComment and True:
							self.multilineComments.append({ 'open': theOpen, 'close': theClose })


	def charByGroupId( self, groupID ):
		
		for record in self.logistics['characters']:
			for lan in record['profiles']:
				if lan['groupID'] == groupID and not lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
					
		return False


	def buildInlineComments( self ):
		
		for record in self.logistics['characters']:
			charSet = record['char']
			comment = record['char']
			for lan in record['profiles']:
				if lan['language'] == self.language:
					isComment = False
					tagList = []
					isInline = False
					for tag in lan['tags'] :
						if lan['isOpen'] and 'inline' in tag:
							isInline = True
							tagList.append( tag )
					if isInline:
						isComment = True
						if type(lan['set']) == list and len( lan['set'] ):
							for setID in lan['set']:
								if type(setID) == int:
									nextChar = self.charById( setID )['char']
									if type( nextChar ) == str:
										comment += nextChar

					if isComment and True:
						self.inlineComments.append( comment )

		

	def charById( self, setID ):
		
		for record in self.logistics['characters']:
			if record['id'] == setID:
				return record
		return False

	def cleanInlineComments( self ):
		pass
		# assetRows = []

		# for inline in self.inlineComments:
		#     for line in self.asset.split('\n'):
		#         tmpLine = _str.replaceAll( line, '\t', ' ' )
		#         tmpLine = _str.replaceDuplicate( tmpLine, ' ' )
		#         tmpLine = _str.cleanBE( tmpLine, ' ' )
		#         if len( tmpLine ) and not tmpLine.startswith( inline ):
		#             assetRows.append( line.split(inline)[0] )
		#     self.asset = '\n'.join( assetRows )


	def cleanMultilineComments( self ):
		pass
		# for group in self.multilineComments:
			
		#     done = False
		#     i = 0
		#     pos = 0
		#     openClose = []
		#     payloads = []
		#     while not done:
		#         o = self.asset.find( group['open'], pos )
		#         c = self.asset.find( group['close'], pos )
		#         if o == -1 or c == -1:
		#             done = True
		#         else:
		#             openClose.append({ 'openID': o, 'openLen': len(group['open']), 'closeID': c, 'closeLen': len(group['close']),  })
		#             pos = c+len(group['close'])
		#             theEnd = len(self.asset) - (  pos )
		#             payload = self.asset[o:-theEnd]
		#             payloads.append( payload )
		#     pass
		#     for payload in payloads:
		#         self.asset = self.asset.replace( payload, '' )
		#     self.asset = _str.replaceDuplicate( self.asset , '\n' )
			# _.pr()
			# _.pr()
			# for x in openClose:
			#     _.pr(x)


	def jsNameSpace_2019( self ):

		# if self.backupLoaded['profile']:
		#     return self.profile

		self.namespaceFunctions = []
		gi = None

		for i,record in enumerate(self.indexes['group']):
			if record['label'] == '{}':
				gi = i
				break

		ci = None
		for i,record in enumerate(self.indexes['char']):
			# _.pr( record['label'], len(  record['start']  ) )
			if record['label'] == '{':
				ci = i
				break


		functions = []
		lastNS = ''
		documentation = []
		docIndex = []
		self.genOmit()

		# ToDo:
		#         scan documentation first
		#         docIndex = []
		#         docIndex is starting pos of every doc2b
		#         create global table of context 
		#         load global context table

		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line'] = self.getLine( oc['open'] )
			oc['linePos'] = self.getLinePos( oc['line'] )
			code = self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs = None
			code = code = self.assetSnipet( oc['open'], oc['close'] )
			if 'doc2b' in code:
				thisIs = 'documentation'
				documentation.append( oc )
				docIndex.append( oc['open'] )


		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line'] = self.getLine( oc['open'] )
			oc['linePos'] = self.getLinePos( oc['line'] )
			code = self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs = None
			if '=' in code:
				ns = code.split('=')[0]
				ns = ns.replace( ' ', '' )
				ns = ns.replace( '\t', '' )
				lastNS = ns
				thisIs = 'var'
				# _.pr( lastNS )
			if 'function' in code.lower() and ':' in code.lower() and '(' in code.lower():
				thisIs = 'function'
				ns = code.split(':')[0]
				ns = ns.replace( ' ', '' )
				ns = ns.replace( '\t', '' )
				fullNS = lastNS + '.' + ns
				oc['ns'] = fullNS
				functions.append( oc )
				code = code = self.assetSnipetClean( oc['open'], oc['close'] )
				terms = self.findTerms( code )
				for t in terms:
					pass
					# _.pr( t )
				oc['documentation'] = []
				for doci,doc in enumerate(documentation):
					if doc['open'] > oc['open'] and doc['open'] < oc['close']:
						oc['documentation'].append( doci )


		self.profile['documentation'] = documentation
		self.profile['functions'] = functions
		self.saveProject()

		return self.profile



	def jsNameSpace( self ):

		if self.backupLoaded['profile']:
			return self.profile

		self.namespaceFunctions = []
		gi = None

		for i,record in enumerate(self.indexes['group']):
			if record['label'] == '{}':
				gi = i
				break

		ci = None
		for i,record in enumerate(self.indexes['char']):
			# _.pr( record['label'], len(  record['start']  ) )
			if record['label'] == '{':
				ci = i
				break


		functions = []
		lastNS = ''
		documentation = []
		docIndex = []
		self.genOmit()

		# ToDo:
		#         scan documentation first
		#         docIndex = []
		#         docIndex is starting pos of every doc2b
		#         create global table of context 
		#         load global context table

		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line'] = self.getLine( oc['open'] )
			oc['linePos'] = self.getLinePos( oc['line'] )
			code = self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs = None
			code = code = self.assetSnipet( oc['open'], oc['close'] )
			if 'doc2b' in code:
				thisIs = 'documentation'
				documentation.append( oc )
				docIndex.append( oc['open'] )

		# _.pr( self.indexes['group'][gi].keys() )
		# dict_keys(['open', 'close', 'total', 'tags', 'oc', 'index', 'inner', 'groups', 'nestable', 'escape', 'label', 'scanID'])
		# sys.exit()
		top = []
		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line'] = self.getLine( oc['open'] )
			oc['linePos'] = self.getLinePos( oc['line'] )
			if not oc['open'] in self.indexes['group'][gi]['inner']:
				top.append( oc )

		for oc in top:
			code = self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs = None
			if '=' in code:
				ns = code.split('=')[0]
				ns = ns.replace( ' ', '' )
				ns = ns.replace( '\t', '' )
				lastNS = ns
				thisIs = 'var'
				# _.pr( lastNS )
				# codeX = self.assetSnipet( oc['open'], oc['close'] )
				# _.pr( codeX )
				# sys.exit()
				for i,ocX in enumerate(self.indexes['group'][gi]['oc']):
					if ocX['open'] > oc['open'] and ocX['close'] < oc['close']:
						codeX = self.assetSnipet( ocX['linePos']+1, ocX['open'] )
						if 'function' in codeX.lower() and ':' in codeX.lower() and '(' in codeX.lower():
							thisIs = 'function'
							ns = codeX.split(':')[0]
							ns = ns.replace( ' ', '' )
							ns = ns.replace( '\t', '' )
							fullNS = lastNS + '.' + ns
							ocX['ns'] = fullNS
							functions.append( ocX )
							# code = code = self.assetSnipetClean( oc['open'], oc['close'] )
							# terms = self.findTerms( code )


		# _.pr( top )
		# sys.exit()
		#     code = self.assetSnipet( oc['linePos']+1, oc['open'] )
		#     thisIs = None
		#     if '=' in code:
		#         ns = code.split('=')[0]
		#         ns = ns.replace( ' ', '' )
		#         ns = ns.replace( '\t', '' )
		#         lastNS = ns
		#         thisIs = 'var'
		#         # _.pr( lastNS )
		#     if 'function' in code.lower() and ':' in code.lower() and '(' in code.lower():
		#         thisIs = 'function'
		#         ns = code.split(':')[0]
		#         ns = ns.replace( ' ', '' )
		#         ns = ns.replace( '\t', '' )
		#         fullNS = lastNS + '.' + ns
		#         oc['ns'] = fullNS
		#         functions.append( oc )
		#         code = code = self.assetSnipetClean( oc['open'], oc['close'] )
		#         terms = self.findTerms( code )
		#         for t in terms:
		#             pass
		#             # _.pr( t )
		#         oc['documentation'] = []
		#         for doci,doc in enumerate(documentation):
		#             if doc['open'] > oc['open'] and doc['open'] < oc['close']:
		#                 oc['documentation'].append( doci )


		# self.profile['documentation'] = documentation
		self.profile['functions'] = functions
		self.saveProject()

		return self.profile



	def findTerms( self, code ):
		data = ''
		for char in code:
			if not char in _str.alphaChar+'._-':
				data += ' '
			else:
				data += char
		data = _str.replaceDuplicate( data, ' ' )
		data = _str.cleanBE( data, ' ' )
		return data.split(' ')

	def findTerms_has_issues( self, code ):
		result = []
		for line in code.split('\n'):
			data = ''
			for char in code:
				if not char in _str.alphaChar+'._-':
					data += ' '
				else:
					data += char
			data = _str.replaceDuplicate( data, ' ' )
			data = _str.cleanBE( data, ' ' )
			result.append( data.split(' ') )
		return result


	def jsNameSpace_Old( self ):
		self.namespaceFunctions = []
		theFileRows = []
		lineIDX = []
		for i,line in enumerate(self.asset.split('\n')):
			line = _str.cleanBE( line, ' ' )
			# _.pr( line )
			if len( line ) and not line.startswith('//'):
				if not '//' in line and not '}'in line :
					theFileRows.append( line )
					lineIDX.append( i )
					# _.pr( line )


		namespaceList = []
		lineID = []
		for i,line in enumerate(theFileRows):
			if not 'this.' in line and not 'prototype' in line and not '.v.' in line and '.' in line and '=' in line and '{' in line and not '==' in line and not line.startswith('for ') and not line.startswith('var ') and not line.startswith('$') and not '(' in line and not '[' in line:
				namespaceList.append( line )
				lineID.append( lineIDX[i] )
				# _.pr( line )
				# _.pr( line )
		namespaceFunctions = []
		for i,ns in enumerate(namespaceList):
			# _.pr(ns)
			pos = self.asset.find( ns )
			end = len(self.asset) - ( pos + len(ns)+1 )
			string = self.asset[pos:-end]
				# sys.exit()
			bOpen = 1
			bClose = 0
			closeingChar = False

			nsX = ns.replace( ' ', '' )
			
			namespaceRecord = { 'ns': nsX[:-2],  'raw': ns, 'start': pos }

			self.namespaceFunctions.append( namespaceRecord )

		pass
		ns = self.namespaceFunctions
		idList = []
		for i,record in enumerate(ns):
			ix = self.findStringInAsset( record['ns']+'={' )
			if ix:
				ns[i]['charID'] = ix
				idList.append( ix )
				# _.pr(record['ns'])


		testTable = []
		for record in self.locationTable:
			if record['char'] == '{':
				testTable.append( record )

		relevant = []
		xx = 0
		for test in testTable:
			if test['start'] in idList:
				xx += 1
				relevant.append( test )

		for i,record in enumerate(ns):
			for ticket in relevant:
				try:
					if ns[i]['charID'] == ticket['start']:
						ns[i]['record'] = ticket
				except Exception as e:
					_.printVar( ns[i] )
					# sys.exit()
		self.namespaceFunctions = ns

		return self.namespaceFunctions


	def link_jsNameSpace_to_function_payloads( self ):
		self.jsNameSpace()
		# return False
		fnList = []
		for i,ns in enumerate(self.namespaceFunctions):
			fn = []
			try:
				code = self.findCode( ns['record']['start'], ns['record']['end'] )
				for ln in code.split('\n'):
					if ':' in ln and '(' in ln and ')' in ln and '{' in ln and 'function' in ln and not 'push(' in ln:
						f = ns['ns']+'.'+ln.split(':')[0].replace(' ','')
						fn.append( f )
						fnList.append( f )
						# _.pr( f )
				self.namespaceFunctions[i]['functions'] = fn
			except Exception as e:
				pass
			

		xref = {}
		for i,ns in enumerate(self.namespaceFunctions):
			code = self.findCode( ns['record']['start'], ns['record']['end'] )
			# _.pr( len(code) )
			xref[i] = []
			for fnx in fnList:
				if fnx in code:
					xref[i].append( fnx )

		for i in xref.keys():
			_.printBold( self.namespaceFunctions[i]['ns'] )
			for x in xref[i]:
				_.pr( '\t', x )



	def quickTest( self ):
		dataSample = _.getTable( 'auditCodeBase_js_field_tmp.json' )
		self.tableAudit = _profile.records.audit( 'tableAudit', dataSample )
		# self.tableAudit = _profile.processRows( dataSample )
		_.printVar( self.tableAudit )
		# _.printVar( dataSample )
		# for one in dataSample.items():
		#     _.pr( one.items() )
		# x = findX( dataSample )
	def findX(self, key, dictionary):
		for k, v in dictionary.iteritems():
			if k == key:
				yield v
			elif isinstance(v, dict):
				for result in find(key, v):
					yield result
			elif isinstance(v, list):
				for d in v:
					if isinstance(d, dict):
						for result in find(key, d):
							yield result

	def findStringInAsset( self, string ):
		test = 0
		i=0
		while not i == len(self.asset)-1:
			char = self.asset[i]
			if not char == ' ':
				if string[test] == char:
					test += 1
				else:
					test = 0
				if test == len(string):
					return i
			i+=1
		return False

	def buildIDCache( self ):
		self.idCache = []
		self.idOmitCache = []
		a = len(self.asset)
		i = 0
		while not i == a:
			if not self.inCommentRange( i ):
				self.idCache.append( i )
			else:
				self.idOmitCache.append( i )
			i += 1
		if not ( len(self.idOmitCache) + len(self.idCache) ) == len(self.asset):
			_.pr( 'Error xy' )



	def findCode( self, start, end ):
		return self.asset[ start :-( len(self.asset) - end ) ]



	def buildCarriageReturnTable( self ):
		self.carriageReturnTable = []
		self.carriageReturnTable.append( 0 )
		# for i, char in enumerate(self.asset):
		for i in self.idCache:
			char = self.asset[i]
			if char == '\n':
				# _.pr( i )
				self.carriageReturnTable.append( i )



		# buildIDCache()
		# self.idCache
		# self.idOmitCache
	def noComment( self ):
		commentRecords = self.query( tag='comment', justIDs=True )
		_.pr( commentRecords )
		sys.exit()



def loadProject( project=None ):
	global validator
	result = None
	if not project is None:
		__.validator_Project = project



	try:
		with open( objFile() , 'rb') as objThis:
			result = pickle.load(objThis)
	except Exception as e:
		pass

	if not result is None:
		validator = result
	_.printBold( 'Loaded: ' + objFile(), 'green' )
	return result



def objFile():
	return __.objectPath.replace( 'MD5', __.validator_Project )


def action():
	pass
	# global data
	# load()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner()
	#     # _.printVar(_.appData)
	#     for i,row in enumerate(_.appData[__.appReg]['pipe']):
	#         pass

__.validator_Project = 'test'
validator = Validator()
__.objectPath = _v.myTables + _v.slash+'objects\\auditCodeBase_MD5.object'

# _.pr( objFile() )
# sys.exit()

# for i in self.idCache:
#     char = self.asset[i]
import _rightThumb._profileVariables as _profile
# p inFunc -i D:\tech\programs\python\_rightThumb\_auditCodeBase\__init__.py
# p inFunc -i D:\tech\programs\python\_rightThumb\_auditCodeBase\__init__.py + self.relevantTable
########################################################################################
if __name__ == '__main__':
	action()



# b tt
# del auditCodeBase_MD5_*
# b jjs


# p auditJavascriptFileNamespaceAndProcessManagement -f blank2.js

# p auditJavascriptFileNamespaceAndProcessManagement -f test4.js
# p auditJavascriptFileNamespaceAndProcessManagement -f test4B.js

# p auditJavascriptFileNamespaceAndProcessManagement -f test2.js
# p auditJavascriptFileNamespaceAndProcessManagement -f test.js
# p auditJavascriptFileNamespaceAndProcessManagement -f shared.js



# test4.js    387 B
# test3.js    13.75 KB
# test2.js    16.69 KB
# test.js    184.65 KB

# index = _code.imp.validator.createIndex( allFiles, 'javascript' )
# index = _code.imp.validator.auditTable()
# self.buildIndexes()
# self.buildIndexStructure()
# self.dataRestructure()
# def auditTable( self ):
# {71FE9636-7C0C-440F-86D9-CDBAF1F51155}
# if False and not nestable['status'] and firstRun:

# if self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ] == i: ?????????

# def colorPrint( self ):
# self.testIndexs()
# {6402B9BC-FF5C-4B6F-B8B4-CB1EFADDF405}
# self.javascriptNamespace
# self.backupLoaded['attempted']
# {4B2E8584-8EF6-4AA3-BBC0-4F89160AF12B}
# {C82DBFC2-BCD5-4885-88B7-90604D69CDDB}
# {20E19A90-3070-4181-A3AC-591C186977EF}

# left off
	# {7F41946A-F2F2-4D71-B7E0-765D3109BC86}

# assetSnipetClean

# b jjs
# p jsScan -f newpage2.js

# buildIndexes

# sudoValidate
# epy validate

"""

	_code.imp.validator.register( data, 'javascript' )
	index = _code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False )
	# index = _code.imp.validator.thisTest
	# _.pr( index )
	if False:
		_.pr( _code.imp.validator.asset )
		for x in _code.imp.validator.identity['identity']:
			o = x
			c = _code.imp.validator.identity['location']['open'][o]
			l = _code.imp.validator.getLabel( o, string=True )
			_.pr()
			_.pr()
			_.pr()
			_.pr( o,c,l )
			_.pr(  _code.imp.validator.assetSnipet( o, c )  )

	_code.imp.validator.sudoValidate()

createIndex

"""



# LEFT OFF: FIX     8 /* asdf */ regular_expression
#         {F4CE5BB3-B637-4D70-90F5-0E222630EFC0}

#     self.index_process = 'B'
#     buildIndexes_Process_A
#     buildIndexes_Process_B

# d20(

# {B0B402BE-6121-47BA-9299-11C52E13CE87}
	# possibley needs to be looked at



