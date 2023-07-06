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
# import uuid
# from operator import itemgetter
# from datetime import datetime as dt, timedelta
# import datetime
import time
# from threading import Timer
# from datetime import date
import simplejson as json
# import sqlite3

# import pyperclip

import colorama
colorama.init()

# from threading import Thread
# import threading
# import ctypes

import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._profileVariables as _profile

# _.colorThis( [ '\t', part_profile  ], 'yellow', simpleDic=True, colorProfile=[ { 't': 'i/dict', 'color': 'red', 'field': 'match'  } ] )


def simpleDic( dic ):
	txt = str(dic)
	txt = txt.replace( '{', '' )
	txt = txt.replace( '}', '' )
	txt = txt.replace( '"', '' )
	txt = txt.replace( "'", '' )
	txt = txt.replace( '_', ' ' )
	txt = txt.title()
	return txt

def lastBackup( file, backup=0 ):
	backupLog = tables.returnSorted( 'backupLog', 'd.timestamp', getTable('fileBackup.json') )
	path = os.path.abspath(file)
	# print( 'path:', path )
	if backup == '?':

		i = 0
		for record in backupLog:
			if record['file'] == path:
				i+=1
		part = path.split( _v.slash )
		part.reverse()
		label = part[0]
		colorThis( [ '\n\ttotol of', i , 'backups for ', label ], 'yellow' )
		sys.exit()

	else:
		i = 0
		for record in backupLog:
			if record['file'] == path:
				# printTest( record )
				# print( friendlyDate(record['timestamp']) )
				if i == backup:
					return record['backup']
				i+=1


		i = 0
		for record in backupLog:
			if record['file'] == path:
				i+=1
		part = path.split( _v.slash )
		part.reverse()
		label = part[0]
		colorThis( [ '\n\ttotol of', i , 'backups for ', label ], 'yellow' )
		sys.exit()

		# id timestamp file backup status version flag


	return None

def textClean( txt ):
	clean = 2
	
	if clean:
		txt = _str.replaceDuplicate( txt, '\n' )
		txt = _str.cleanBE( txt, '\n' )
	if clean == 2:
		txt = txt.replace( '\t', ' ' )
		txt = _str.replaceDuplicate( txt, ' ' )
		while '\n \n' in txt:
			txt = txt.replace( '\n \n', '\n' )
		txt = _str.replaceDuplicate( txt, '\n' )
		txt = _str.cleanBE( txt, '\n' )
	return txt

def get_size(obj, seen=None):
	
	# function source documentation:
	#   searched for: python how much memory usage of list of dict
	#   https://goshippo.com/blog/measure-real-size-any-python-object/

	"""Recursively finds size of objects"""
	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0
	# Important mark as seen *before* entering recursion to gracefully handle
	# self-referential objects
	seen.add(obj_id)
	if isinstance(obj, dict):
		size += sum([get_size(v, seen) for v in obj.values()])
		size += sum([get_size(k, seen) for k in obj.keys()])
	elif hasattr(obj, '__dict__'):
		size += get_size(obj.__dict__, seen)
	elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
		size += sum([get_size(i, seen) for i in obj])
	return size


bmIndex = []
processWordStem = None


class CacheManager:
# get_size()

	def __init__( self ):
		pass

	def load( self, config ):
		return None

	def save( self, data, config ):
		return data

	# def 



__.app = CacheManager()

class DataBank:

	def __init__( self, table_tags=None, search_tags=None, subject_trigger=None, description_trigger=None,           table=None, search=None,  t=None, s=None, st=None, dt=None  ):

		if not table is None:
			table_tags = table
		if not search is None:
			search_tags = search_tags

		if not t is None:
			table_tags = t
		if not s is None:
			search_tags = s
		if not st is None:
			subject_trigger = st
		if not dt is None:
			description_trigger=dt


		cache = __.app.get({ 'algorithm': ['DataBank'], 'usage': 'return/app', 'tags': table_tag, 'search': search_tags  })
		if not cache is None:
			return cache



		if not type(table_tags) == list:
			table_tags = table_tags.split(',')
		if not type(search_tags) == list:
			search_tags = search_tags.split(',')

		self.table_tags = table_tags
		self.search_tags = search_tags
		self.subject_trigger = subject_trigger
		self.description_trigger = description_trigger
		self.pathIndexDatabases = _v.databank+_v.slash+'indexes\\databases'
		self.pathIndexStems = _v.databank+_v.slash+'indexes\\tag_stems'

		self.table_tag_stems = []
		for tag in self.table_tags:
			self.table_tag_stems.append( wordStem(tag) )

		self.search_tag_stems = []
		for tag in self.search_tags:
			self.search_tag_stems.append( wordStem(tag) )

		self.indexFilesNames = os.listdir(  self.pathIndexDatabases  )
		self.records = []
		for files in self.indexFilesNames:

			# print( self.pathIndexDatabases+_v.slash+files )
			index = getTable2( self.pathIndexDatabases+_v.slash+files )


			cnt = 0
			tags = index['tag_stems']
			for search in self.table_tag_stems:
				if search in tags:
					cnt+=1
			# print( 'test:', cnt, len(self.table_tag_stems) )
			if cnt == len(self.table_tag_stems):

				print(index['tags'])

				self.search_tag_stems.sort()
				if '_'.join(self.search_tag_stems) in list(index['stem_index']):
					# print( 'in index' )
					for i in index['stem_index'][  '_'.join(self.search_tag_stems)  ]:
						data = index['records'][i]['data']
						if not self.subject_trigger is None:
							data = self.subject_trigger(data)
						self.records.append(data)
					# print( len(self.records) )
				else:

					records = []

					# print( 'found table' )

				
					tables = []
					for i,table in enumerate(index['tables']):
						# print( table['indexes'].keys() )
						cnt = 0
						stems = list(  table['indexes']['stems'].keys()  )
						for search in self.search_tag_stems:
							if search in stems:
								cnt+=1
						if cnt == len(self.search_tag_stems):
							tables.append(table['tableID'])
							# print(table['tableID'])
						# table['tableID']
						# table['data']
						# table['indexes']
					pass

					
					for i,record in enumerate(index['records']):
						if record['tableID'] in tables:
							records.append(i)
						else:
							stems = list(  record['indexes']['stems'].keys()  )
							cnt = 0

							for search in self.search_tag_stems:
								if search in stems:
									cnt+=1
							if cnt == len(self.search_tag_stems):
								records.append(i)

					pass
					print( len(records) )

					self.search_tag_stems.sort()
					index['stem_index'][  '_'.join(self.search_tag_stems)  ] = records
					saveTable2(  index,  self.pathIndexDatabases+_v.slash+files  )
					for i in records:
						data = index['records'][i]['data']
						if not self.subject_trigger is None:
							data = self.subject_trigger(data)
						self.records.append(data)

	def data( self ):
		return __.app.save( data, { 'algorithm': ['DataBank'], 'usage': 'return/app', 'tags': table_tag, 'search': search_tags  } )
		# return list(set(self.records))


		"""
				index fields
							words
							stems
							speech
							parts
							words_cnt
							words_cnt_unique
							percentage
		"""

		# wordStem(word)

def genSerial( subject ):
	serial_no = getText( _v.myVars + _v.slash+'sequence-'+subject+'.serial', clean=2, raw=1 )
	if serial_no is None:
		serial_no = 12345
	else:
		serial_no = int(serial_no)+1
	saveText( str(serial_no), _v.myVars + _v.slash+'sequence-'+subject+'.serial' )
	return serial_no


def extTrigger__File_TYPE__( data ):
	data = data.lower()
	archive = [
				'*.7z',
				'*.s7z',
				'*.ace',
				'*.afa',
				'*.alz',
				'*.apk',
				'*.arc',
				'*.ark',
				'*.cdx',
				'*.arj',
				'*.b1',
				'*.b6z',
				'*.ba',
				'*.bh',
				'*.cab',
				'*.car',
				'*.cfs',
				'*.cpt',
				'*.dar',
				'*.dd',
				'*.dgc',
				'*.dmg',
				'*.ear',
				'*.gca',
				'*.ha',
				'*.hki',
				'*.ice',
				'*.jar',
				'*.kgb',
				'*.lzh',
				'*.lha',
				'*.lzx',
				'*.pak',
				'*.partimg',
				'*.paq6',
				'*.paq7',
				'*.paq8',
				'*.pea',
				'*.pim',
				'*.pit',
				'*.qda',
				'*.rar',
				'*.rk',
				'*.sda',
				'*.sea',
				'*.sen',
				'*.sfx',
				'*.shk',
				'*.sit',
				'*.sitx',
				'*.sqx',
				'*.tar',
				'*.tar.gz',
				'*.tgz',
				'*.tar.Z',
				'*.tar.bz2',
				'*.tbz2',
				'*.tar.lzma',
				'*.tlz.',
				'*.tar.xz',
				'*.txz',
				'*.uc',
				'*.uc0',
				'*.uc2',
				'*.ucn',
				'*.ur2',
				'*.ue2',
				'*.uca',
				'*.uha',
				'*.war',
				'*.wim',
				'*.xar',
				'*.xp3',
				'*.yz1',
				'*.zip',
				'*.zipx',
				'*.zoo',
				'*.zpaq',
				'*.zz'
			]

	office = [
				'*.doc',
				'*.dot',
				'*.wbk',
				'*.docx',
				'*.docm',
				'*.dotx',
				'*.dotm',
				'*.docb',
				'*.xls',
				'*.xlt',
				'*.xlm',
				'*.xlsx',
				'*.xlsm',
				'*.xltx',
				'*.xltm',
				'*.xlsb',
				'*.xla',
				'*.xlam',
				'*.xll',
				'*.xlw',
				'*.ppt',
				'*.pot',
				'*.pps',
				'*.pptx',
				'*.pptm',
				'*.potx',
				'*.potm',
				'*.ppam',
				'*.ppsx',
				'*.ppsm',
				'*.sldx',
				'*.sldm',
				'*.pub',
				'*.xps'
			]
	pass
	# archive
	# office
	


def urlTrigger(url):
	if not '.' in url:
		url = 'http://' + url + '.com'
	elif not url.startswith('http'):
		url = 'http://' + url
	return url

def myFolderLocations( data ):
	if os.path.isdir(data):
		return data
	

	global bmIndex
	
	if not len(bmIndex):
		bmIndex = getTable( 'bookmarks_index.json' )

	try:
		return bmIndex['labels'][data]
	except Exception as e:
		pass

	return data

def mod(path):
	return os.path.getmtime(path)

def miniUUID(): 
	u = genUUID()
	u = u.replace( '{','' ).replace( '-','' )
	return '{' + u[:12] + '}'


def colorPlus( data, color='green' ):
	for search in switches.values('Plus'):
		for subject in caseUnspecific( data, search, isPlus=True ):

			if type( subject ) == str:
				data = data.replace( subject, colorThis( subject, color, p=0 ) )
			else:
				if subject['pos'] == 'first':
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), 1)
				else:
					cx = data.count( subject['data'] )
					data = nth_repl(data, subject['data'], colorThis( subject['data'], color, p=0 ), cx)
	return data

def plusColor( row, color='green' ):
	# row = thePrintLine

	if switches.isActive('Plus'):
		thePrintLine = row
		for plusSearchX in switches.values('Plus'):
			plusSearchX = ci( plusSearchX )

			for subject in caseUnspecific( row, plusSearchX ):
				row = thePrintLine.replace( subject, colorThis( subject, color , p=0 ) )

	return row

def caseUnspecific( data, subject, isPlus=False ):
	results = []
	subject = subject.lower()
	if isPlus:
		if '*' in subject and len(subject) > 1:
			if subject.startswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().endswith( subject ):
					return [{ 'data': data[-len(subject):], 'pos': 'last' }]
				return []
			if subject.endswith('*'):
				subject = subject.replace( '*', '' )
				subject = ci(subject)
				if data.lower().startswith( subject ):
					return [{ 'data': data[:len(subject)], 'pos': 'first' }]
				return []
		subject = ci(subject)
			

	while data.lower().find( subject ) > -1:
		scanning = data.lower().find( subject )
		subjectY = ''
		scanComplete = False
		while not scanComplete:
			if len(subjectY) == len(subject):
				scanComplete = True
			elif scanning > len(data)-1:
				scanComplete = True
			else:
				subjectY += data[ scanning ]
			scanning += 1
		if not subjectY in results:
			results.append( subjectY )
		data = data.replace( subjectY, '' )
	return results

def nth_repl(s, sub, repl, nth):

	# first and only thing a got online

	find = s.find(sub)
	# if find is not p1 we have found at least one match for the substring
	i = find != -1
	# loop util we find the nth or we find no match
	while find != -1 and i != nth:
		# find + 1 means we start at the last match start index + 1
		find = s.find(sub, find + 1)
		i += 1
	# if i  is equal to nth we found nth matches so replace
	if i == nth:
		return s[:find]+repl+s[find + len(sub):]
	return s


def shuffle( myList ):
	result = []
	data = []
	for x in myList:
		data.append({ 'data': x, 'sortBy': genUUID() })

	for record in tables.returnSorted( genUUID(), 'd.sortBy', data ):
		result.append( record['data'] )
	return result



# oc = list(filter(lambda data: data['open'] == pos, record['oc']))
__.loadingVar = {
					'hasLoaded': False,
					'hasCleared': False,
					'isRunning': False,
					'done': False,
}


__.loadingVar['hasLoaded'] = False
__.loadingVar['hasCleared'] = False
__.loadingVar['isRunning'] = False

def listColor( text, rows, color='green' ):
	return text
	r = text

	# print( 'HERE', r )
	txtCNT = text.lower()
	for row in rows:

		loc = txtCNT.find( row )
		if row in txtCNT:
			print( 'loc:', loc )
			if loc:
				r = ''
				for i,char in enumerate(text):
					if i >= loc and i <= len(row)-1:
						print( char )
						r += colorThis( char, color, p=0 )
					else:
						r+=char
	return r



def LoadingDone(done=None):
	if not done is None:
		__.loadingVar['done'] = done
	__.loadingVar['hasLoaded'] = True
	
	global threads
	while not __.loadingVar['hasCleared']:
		time.sleep( .2 )
	time.sleep( .7 )
	print( '                                                        ', end='\r' )
	time.sleep( 2 )
	__.loadingVar['hasCleared'] = False
	__.loadingVar['hasLoaded'] = False
	__.loadingVar['isRunning'] = False
	del threads
	threads = Queue()

def loadingAnimation(loading='Searching',done='Found' ):
	__.loadingVar['done'] = done
	if not __.loadingVar['isRunning']:
		__.loadingVar['isRunning'] = True
		global threads
		theID = 'loadingAnimation_'+loading+'_' + genUUID()
		threads.add( theID ) # kwargs 
		threads.maxThreadsSafe = 225
		threads.autoLoadedAfter = .1
		threads.scheduleLoop = .01
		threads.auditLoop = .1
		threads.projectDataMaxLen = 500
		threads.report = False
		threads.auditPrint = False
		threads.add( theID, loadingGif, [loading] )


def loadingGif(loading, qID=False):
	
	gif = [
			'       *',
			'      **',
			'     ***',
			'    *** ',
			'   ***  ',
			'  ***   ',
			' ***    ',
			'***     ',
			'**      ',
			'*       ',
			'**      ',
			'***     ',
			' ***    ',
			'  ***   ',
			'   ***  ',
			'    *** ',
			'     ***',
			'      **',
	]
	while not __.loadingVar['hasLoaded']:
		print( '                                                                                                   ', end='\r' )
		for x in gif:
			animate = colorThis( x, 'red', p=0 )
			print( '\t\t{' + animate + '} '+loading+'...', end='\r' )
			time.sleep( .4 )
		print( '                                                                                                   ', end='\r' )
	print( '                                                                                                   ', end='\r' )
	print( '\t\t'+colorThis( __.loadingVar['done'], 'green', p=0 ), end='\r' )
	if not type(qID) == bool:
		global threads
		threads.spent( qID, sys.getsizeof( 'obj') )
	__.loadingVar['hasCleared'] = True

		
def loadingGifX(loading):
	
	gif = [
			'       *',
			'      **',
			'     ***',
			'    *** ',
			'   ***  ',
			'  ***   ',
			' ***    ',
			'***     ',
			'**      ',
			'*       ',
			'**      ',
			'***     ',
			' ***    ',
			'  ***   ',
			'   ***  ',
			'    *** ',
			'     ***',
			'      **',
	]
	while not __.loadingVar['hasLoaded']:
		print( '                                                                                                   ', end='\r' )
		for x in gif:
			animate = colorThis( x, 'red', p=0 )
			print( '\t\t{' + animate + '} '+loading+'...', end='\r' )
			time.sleep( .4 )
		print( '                                                                                                   ', end='\r' )
	print( '                                                                                                   ', end='\r' )
	print( '\t\t'+colorThis( __.loadingVar['done'], 'green', p=0 ), end='\r' )

	__.loadingVar['hasLoaded'] = False



server_proxy = []
server_proxy.append( '' )
server_proxy.append( 'http://www.rightthumb.com/projects/widget/proxy.php?p=' )
server_proxy.append( 'http://rephrecruiting.com/proxy.php?p=' )
server_proxy.append( 'http://www.pillerbeauty.com/proxy.php?p=' )
server_proxy.append( 'http://signaturemassageandfacialspa.com/p.php?p=' )
server_proxy.append( 'https://signaturemassagetampa.com/payroll/p.php?p=' )

appProxy = 'appProxy.json'

ipsum = None
def ipsumSentence():
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	ipsum = ipsum.replace( '\n', ' ' )
	sentences = []
	for sentence in ipsum.split('.'):
		sentence = _str.replaceDuplicate( sentence, ' ' )
		sentence = _str.cleanBE( sentence, ' ' )
		sentence = sentence + '.'
		sentences.append({ 'sentence': sentence, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', sentences )
	return randomized[0]['sentence']

def ipsumParagraph( count=1, shouldPrint=False, returnList=False, lorem=True ):
	global ipsum
	if ipsum is None:
		ipsum = getText( _v.ipsum, raw=True, clean=2 )
	paragraphs = []
	for item in ipsum.split('\n'):
		item = _str.replaceDuplicate( item, ' ' )
		item = _str.cleanBE( item, ' ' )
		item = item + '.'
		item = _str.replaceDuplicate( item, '.' )
		paragraphs.append({ 'paragraph': item, 'sortBy': genUUID() })

	randomized = tables.returnSorted( 'data', 'd.sortBy', paragraphs )

	result = []

	i=0
	while not i == count:
		result.append( randomized[i]['paragraph'] )
		i+=1

	if lorem:
		result[0] = 'Lorem ipsum ' + result[0][0].lower() + result[0][1:]

	

	if shouldPrint:
		data = '\n\n'.join( result )
		print( data )

	if returnList:
		return result
	else:
		return '\n\n'.join( result )


def convertTimestamp( data ):
	if not len( data ):
		return data
	if not 'timestamp' in data[0].keys():
		return data
	if 'datetime' in data[0].keys():
		hasDateTime = True
	else:
		hasDateTime = False
	for i,record in enumerate(data):
		try:
			if len( record['timestamp'] ):
				if isFloat( str(record['timestamp']) ):
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
					else:
						return data
				else:
					data[i]['timestamp'] = autoDate( record['timestamp'] )
					if not hasDateTime:
						data[i]['datetime'] = resolveEpoch( data[i]['timestamp'] )
		except Exception as e:
			return data
	return data

def changeExtension( file, ext ):
	f = removeExtension( file )
	if not '.' in ext:
		return f + '.' + ext
	else:
		return f + ext

def getExtension(string):

	ext0 = string.split('.')
	extId = len(ext0) - 1
	if extId > 0:
		ext = ext0[extId]
	else:
		ext = ''
	return ext
def removeExtension(string):
	if not '.' in string:
		return string
	ext = getExtension(string)
	sl = len(string)
	el = len(ext)
	dl = (sl - el) - 1
	file = ''
	for i,n in enumerate(string):
		if i < dl:
			file += n

	return file


def registerSpent( app, spentID ):
	global appProxy
	data = getTable( appProxy )
	for i,record in enumerate(data):
		if record['app'] == app:
			pass
	saveTable( appProxy )

# colorizeRow
# printBold

__.color_palette = 0

# from timeout import timeout
plusClose = 70
autoBackupData = False
autoLoadData = False

idResolution = []

theExtensionsList = []
relevantFolders = []
setPipeDataRan = False

__.columnAbbreviations = 1

# print( 'make pattern algorithm for pattern IDs' )

# def testPatterns( two, one ):

def saveData( rows, theFile, printThis=True ):

	if theFile.lower().endswith( '.json' ):
		if _v.slash in theFile:
			saveTable2( rows, theFile, printThis )
			if printThis:
				print( 'Saved: ', theFile )
		else:
			saveTable( rows, theFile, printThis )
		return True

	if theFile.lower().endswith( '.txt' ):
		if _v.slash in theFile:
			saveText( rows, theFile )
			if printThis:
				print( 'Saved: ', theFile )
		else:
			if os.path.isfile( _v.myTables + _v.slash + theFile ):
				saveText( rows, _v.myTables + _v.slash + theFile )
			else:
				saveText( rows, _v.myTables + _v.slash + theFile )
			if printThis:
				print( 'Saved: ', _v.myTables + _v.slash + theFile )
		return True

	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile


	if found:
		if location.lower().endswith( '.json' ):
			saveTable2( rows, location, printThis )
			if printThis:
				print( 'Saved: ', location )
			return True

		if location.lower().endswith( '.txt' ):
			saveText( rows, location )
			if printThis:
				print( 'Saved: ', location )
			return True


	t = type( rows )
	if t == str:
		location = _v.myTables + _v.slash + theFile + '.txt'
		saveText( rows, location )
		if printThis:
			print( 'Saved: ', location )
		return True

	if t == dict:
		saveTable( rows, theFile+'.json', printThis )
		return True
	if t == list:
		if len(rows) == 0:
			print( 'Error: no data to save' )
			return False

		t = type( rows[0] )
		if t == dict:
			saveTable( rows, theFile+'.json', printThis )
			return True
		pass
		if t == str:
			location = _v.myTables + _v.slash + theFile + '.txt'
			saveText( rows, location )
			if printThis:
				print( 'Saved: ', location )
			return True

	print( 'Error: unable to save file' )
	return False



def getData( theFile, exitOnError=False ):
	location = theFile
	if os.path.isfile( theFile ):
		found = True
	
	if not os.path.isfile( theFile ):
		found = False
		if not _v.slash in theFile:
			if not '.' in theFile:
				if os.path.isfile( _v.myTables + _v.slash + theFile + '.json' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.json'
				elif os.path.isfile( _v.myTXT + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTXT + _v.slash + theFile + '.txt'
				elif os.path.isfile( _v.myTables + _v.slash + theFile + '.txt' ):
					found = True
					location = _v.myTables + _v.slash + theFile + '.txt'
			else:
				if os.path.isfile( _v.myTables + _v.slash + theFile ):
					found = True
					location = _v.myTables + _v.slash + theFile
				elif os.path.isfile( _v.myTXT + _v.slash + theFile ):
					found = True
					location = _v.myTXT + _v.slash + theFile

		if not found:
			print( 'Error: unable to locate file' )
			if exitOnError:
				sys.exit()
			return []



	if not os.path.isfile( theFile ):
		if location.lower().endswith( '.json' ):
			return getTable2( location )



	file = getText( location, raw=True, clean=1 )
	textList = file.split('\n')
	if '[' in textList or '{' in textList:
		data = eval( file )
	else:
		data = textList
	return data



class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'


class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


class Background:
	red = '\033[1;37;41m'
	green = '\033[1;37;42m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;37;44m'
	purple = '\033[1;37;45m'
	light_blue = '\033[1;37;46m'
	grey = '\033[1;37;47m'
	black = '\033[1;37;48m'
	end = '\033[0m'

class BackgroundGrey:
	black = '\033[0;30;47m'
	red = '\033[0;31;47m'
	green = '\033[0;32;47m'
	brown = '\033[0;33;47m'
	blue = '\033[0;34;47m'
	magenta = '\033[0;35;47m'
	cyan = '\033[0;36;47m'
	gray = '\033[0;37;40m'
	end = '\033[0m'
	
class BackgroundGreyBold:
	black = '\033[1;30;47m'
	red = '\033[1;31;47m'
	green = '\033[1;32;47m'
	brown = '\033[1;33;47m'
	blue = '\033[1;34;47m'
	magenta = '\033[1;35;47m'
	cyan = '\033[1;36;47m'
	gray = '\033[1;37;40m'
	end = '\033[0m'
	


row_colors = []

row_colors.append([ 0, Background.blue ])
row_colors.append([ 0, Background.light_blue ])
row_colors.append([ 0, Background.purple ])

row_colors.append([ 1, BackgroundGrey.red ])
row_colors.append([ 1, BackgroundGrey.brown ])
row_colors.append([ 1, BackgroundGrey.blue ])

row_colors.append([ 2, Color.cyan ])
row_colors.append([ 2, Color.green ])

row_colors_ID = 0

colorHelp_colorList = [
	"ColorBold.gray",
	"ColorBold.red",
	"ColorBold.green",
	"ColorBold.yellow",
	"ColorBold.blue",
	"ColorBold.magenta",
	"ColorBold.cyan",
	"ColorBold.white",

	"",

	"Color.purple",
	"Color.cyan",
	"Color.darkcyan",
	"Color.blue",
	"Color.green",
	"Color.yellow",
	"Color.red",
	"Color.bold",
	
	"",

	"Background.red",
	"Background.green",
	"Background.yellow",
	"Background.blue",
	"Background.purple",
	"Background.light_blue",
	"Background.grey",
	"Background.black",

	"",

	"BackgroundGrey.black",
	"BackgroundGrey.red",
	"BackgroundGrey.green",
	"BackgroundGrey.brown",
	"BackgroundGrey.blue",
	"BackgroundGrey.magenta",
	"BackgroundGrey.cyan",
	"BackgroundGrey.gray",

	"",

	"BackgroundGreyBold.black",
	"BackgroundGreyBold.red",
	"BackgroundGreyBold.green",
	"BackgroundGreyBold.blue",
	"BackgroundGreyBold.magenta",
	"BackgroundGreyBold.cyan",
	"BackgroundGreyBold.gray"
]

def colorHelp( ipsum=False ):
	global colorHelp_colorList
	for sample in colorHelp_colorList:
		if not len( sample ):
			print()
		else:
			result = eval( sample + '+ "THE_TEXT" + Color.end' )
			if ipsum:
				result = result.replace( 'THE_TEXT', ipsumSentence() )
			else:
				result = result.replace( 'THE_TEXT', sample )
			
			print( result )
	sys.exit()


def buldColorTable( tableID ):
	global row_colors
	newColorTable = []
	for row in row_colors:
		if row[0] == tableID:
			newColorTable.append( row[1] )
	return newColorTable

def colorNext( tableID ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	row_colors_ID += 1
	# if row_colors_ID == len(row_colors):
	if row_colors_ID % len(row_colors) == 0:
		row_colors_ID = 0

def colorID( tableID, up=True ):
	row_colors = buldColorTable( tableID )
	global row_colors_ID
	result = row_colors[row_colors_ID]
	if up:
		colorNext( tableID )
	return result

def colorizeRow( row, tableID=False ):

	global switches
	if switches.isActive( 'NoColor' ):
		print( row )
		return False

	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print( row )
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		# print( str(len(row))+colorID( tableID, up ) + row + Background.end )
		print( colorID( tableID, up ) + row + Background.end )



app_full_color_index = None
def generateColorIndex():
	global app_full_color_index
	if not app_full_color_index is None:
		return app_full_color_index
	colorClasses = 'ColorBold Color Background BackgroundGrey BackgroundGreyBold'
	list_of_colors = []
	test = 0
	if test == 0:
		for cc in colorClasses.split(' '):
			for x in dir(  eval(  '_.'+cc  )  ):
				if not x.startswith('_'):
					
					subject = x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )

					subject = cc+'.'+x
					subject = subject.lower()
					if not subject in list_of_colors:
						list_of_colors.append( subject )


	test = 1
	if test == 1:
		for x in _.colorHelp_colorList:
			if '.' in x:
				p = x.split('.')
				a = p[0]+'.'
				aa = a.lower()
				b = p[1]
				bb = b.lower()

				subject = bb
				if not subject in list_of_colors:
					list_of_colors.append( subject )

				subject = x.lower()
				if not subject in list_of_colors:
					list_of_colors.append( subject )


	app_full_color_index = []

	for x in list_of_colors:
		if not '.' in x:
			app_full_color_index.append( x )

	for x in list_of_colors:
		if '.' in x:
			app_full_color_index.append( x )

	return app_full_color_index



# _.colorThis( [ '\t', part_profile  ], 'yellow', simpleDic=True, colorProfile=[  ] )

# simpleDic=True, simpleDicColor=[ [ 'match', 'red' ] ]
def colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False, simpleDic=False, colorProfile=None,      p=True ):

# [ { 'color': 'red', 'field': 'match', 'i': 0  } ]
# [ { 'color': 'red', 'field': 'match' } ]
# [ { 'color': 'red', 'i': 0  } ]
# { 'color': 'red', 'i': 0  }
# ['red',1]
# [2,'red']
# ['name','yellow']
# 'red,green'
# 'red,green:*'
# '*red,green'
# 'green,red,green:*'
# 'green:2,red:*,green'

# topic_index
#   'float,2'


# ColorBold Color Background BackgroundGrey BackgroundGreyBold

	
	# color_index = generateColorIndex()
	# colorProfileTmp = []
	# index = {
	#             'i': [],
	#             'keys': [],
	#             'data': {},
	# }
	# if not colorProfile is None:
	#     if type(colorProfile) == str:
	#         if type(strings) == list and ',' in colorProfile:
	#             if colorProfile.count('*') > 1:
	#                 print( ' only 1 * ' )
	#             new_CP = []
	#             cp = colorProfile.split(',')
	#             end = len(strings)-1
	#             leftC = len(cp)-1
	#             leftL = end


	#             for i,xx in enumerate(strings):



	#     if type(colorProfile) == list:
	#         for i,record in enumerate(colorProfile):
	#             if type(record) == dict:
	#                 record['id'] = i
	#                 if 'c' in record.keys():
	#                     record['color'] = record['c']
	#                     del record['c']

	#                 if 'f' in record.keys():
	#                     record['field'] = record['f']
	#                     del record['f']

	#                 if 'column' in record.keys():
	#                     record['field'] = record['column']
	#                     del record['column']


	#                 if 'i' in record.keys():
	#                     index['i'].append( record['i'] )
	#                     index['data'][i] = record
					
	#                 if 'field' in record.keys():
	#                     if ',' in record['field']:
	#                         for ef in record['field'].split(','):
	#                             index['keys'].append( ef )
	#                             index['data'][ ef ] = record
	#                     else:
	#                         index['keys'].append( record['field'] )
	#                         index['data'][record['field']] = record
	#                 colorProfileTmp.append( record )
					
	#             if type(record) == list:
	#                 if len(record) == 2:
	#                     newRecord = { 'id': i }


	#                     if type( record[0] ) == int:
	#                         newRecord['i'] = record[0]
	#                         newRecord['color'] = record[1]

	#                     elif type( record[1] ) == int:
	#                         newRecord['i'] = record[1]
	#                         newRecord['color'] = record[0]
	#                     else:
	#                         if record[0].lower() in color_index:
	#                             newRecord['field'] = record[0]
	#                             newRecord['color'] = record[1]
	#                         if record[1].lower() in color_index:
	#                             newRecord['field'] = record[1]
	#                             newRecord['color'] = record[0]

	#                     if 'color' in newnewRecord.keys():

	#                         if 'i' in newRecord.keys():
	#                             index['i'].append( newRecord['i'] )
	#                             index['data'][i] = newRecord
							
	#                         if 'field' in newRecord.keys():
	#                             if ',' in newRecord['field']:
	#                                 for ef in newRecord['field'].split(','):
	#                                     index['keys'].append( ef )
	#                                     index['data'][ ef ] = newRecord
	#                             else:
	#                                 index['keys'].append( newRecord['field'] )
	#                                 index['data'][newRecord['field']] = newRecord
	#                         colorProfileTmp.append( newRecord )



	#     if type(colorProfile) == dict:
	#         record = colorProfile
	#         if 'c' in record.keys():
	#             colorProfile[i]['color'] = record['c']
	#             record['color'] = record['c']
	#         if 'f' in record.keys():
	#             colorProfile[i]['field'] = record['f']
	#             record['field'] = record['f']
	#         if 'column' in record.keys():
	#             colorProfile[i]['field'] = record['column']
	#             record['field'] = record['column']


	#         if 'i' in record.keys():
	#             index['i'].append( record['i'] )
			
	#         if 'field' in record.keys():
	#             index['keys'].append( record['field'] )
	#         colorProfile = [record]


	if not p:
		shouldPrint = False

	if type(strings) == list:

		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	if ipsum:
		string = ipsumSentence()

	found = False

	if color == 'help':
		print()
		print()
		print( "_.colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print()
		print()
		colorHelp( ipsum )


	if '.' in color:

		try:
			result = eval( color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True

	else:
		color = color.lower()


	if not found and notBold:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'ColorBold.' + color + '+ string + ColorBold.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'Background.' + color + '+ string + Background.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGrey.' + color + '+ string + BackgroundGrey.end')
		except Exception as e:
			pass
		else:
			found = True


	if not found:
		try:
			result = eval( 'BackgroundGreyBold.' + color + '+ string + BackgroundGreyBold.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		printBold( 'Error: _.colorThis: color not found ' + str(color), 'red' )
		colorHelp( ipsum )

		sys.exit()

	if shouldPrint:
		try:
			print( result )
		except Exception as e:

			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')



	return result



def inlineColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
		return string

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		return Color.red + string + Color.end
	elif color == 'cyan':
		return Color.cyan + string + Color.end
	elif color == 'darkcyan' or color == 'grey':
		return Color.darkcyan + string + Color.end
	elif color == 'blue':
		return Color.blue + string + Color.end
	elif color == 'green':
		return Color.green + string + Color.end
	elif color == 'yellow':
		return Color.yellow + string + Color.end
	elif color == 'underline':
		return Color.underline + string + Color.end


def printColor( string, color='red' ):

	global switches
	if switches.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		print( Color.red + string + Color.end )
	elif color == 'cyan':
		print( Color.cyan + string + Color.end )
	elif color == 'darkcyan' or color == 'grey':
		print( Color.darkcyan + string + Color.end )
	elif color == 'blue':
		print( Color.blue + string + Color.end )
	elif color == 'green':
		print( Color.green + string + Color.end )
	elif color == 'yellow':
		print( Color.yellow + string + Color.end )
	elif color == 'underline':
		print( Color.underline + string + Color.end )


def printBold( string, color='white' ):

	global switches
	if switches.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print( ColorBold.white + string + ColorBold.end )
	elif color == 'red':
		print( ColorBold.red + string + ColorBold.end )
	elif color == 'gray' or color == 'grey':
		print( ColorBold.gray + string + ColorBold.end )
	elif color == 'green':
		print( ColorBold.green + string + ColorBold.end )
	elif color == 'yellow':
		print( ColorBold.yellow + string + ColorBold.end )
	elif color == 'blue':
		print( ColorBold.blue + string + ColorBold.end )
	elif color == 'magenta':
		print( ColorBold.magenta + string + ColorBold.end )
	elif color == 'cyan':
		print( ColorBold.cyan + string + ColorBold.end )


def inlineColorGroup( row, tableID=False ):

	global switches
	if switches.isActive( 'NoColor' ):
		return row

	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		tableID = __.color_palette
	if not type(row) == str:
		row = str(row)
	if type(tableID) == bool:
		print( row )
	else:
		if _str.hasVisible(row):
			up =True
		else:
			up =False
		# print( 'tableID:', tableID, colorID( tableID ) )
		return colorID( tableID, up ) + row + Background.end


def inlineBold( string, color='white' ):
	global switches
	if switches.isActive( 'NoColor' ):
		return string
	
	string = str(string)
	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		return ColorBold.white + string + ColorBold.end 
	elif color == 'red':
		return ColorBold.red + string + ColorBold.end 
	elif color == 'gray' or color == 'grey':
		return ColorBold.gray + string + ColorBold.end 
	elif color == 'green':
		return ColorBold.green + string + ColorBold.end 
	elif color == 'yellow':
		return ColorBold.yellow + string + ColorBold.end 
	elif color == 'blue':
		return ColorBold.blue + string + ColorBold.end 
	elif color == 'magenta':
		return ColorBold.magenta + string + ColorBold.end 
	elif color == 'cyan':
		return ColorBold.cyan + string + ColorBold.end
	elif color == 'underline':
		return ColorBold.underline + string + ColorBold.end

def patternMatch( one, two, best=True, simple=True, both=False, unsorted=False ):
	# simple=True
	result = []
	result.append( testPatterns( one, two, simple ) )
	result.append( testPatterns( two, one, simple ) )
	if not both:
		if best:
			return max(result)
		else:
			return min(result)
	else:
		if unsorted:
			return result

		if not simple:
			if result[0][0] > result[1][0]:
				return result[0],result[1]
			else:
				return result[1],result[0]
		else:
			if result[0] > result[1]:
				return result[0],result[1]
			else:
				return result[1],result[0]
		
def testPatterns( one, two, simple=True ):

	test = False
	spent = []
	patterns = []
	matches = []
	def tempDataset( datasetX ):
		newDataset = []
		for dat in datasetX:
			newDataset.append( dat )
		return newDataset
	def genChars( datasetY, x=False ):
		chars = []
		for d in datasetY:
			chars.append( one[d] )
			if x:
				print( one[d], d )
		return ''.join( chars )
	def addSpent( datasetY ):
		for d in datasetY:
			spent.append( d )

	def addMatch( datasetY ):
		for d in datasetY:
			if not d in matches:
				matches.append( d )

	def testSpent( datasetX ):
		for d in datasetX:
			if d in spent:
				return False
		return True

	def expandTest( datasetX ):
		if testSpent( datasetX ):
			first = datasetX[0]
			last = datasetX[len(datasetX)-1]
			theLast = len(datasetX)-1
			theMax = len(one)-1

			datasetY = tempDataset( datasetX )
			if not datasetX[0] == 0:
				nextFirst = int(first)
				for x in range(1,100000):
					nextFirst = first - 1
					if nextFirst >= 0:
						datasetY.append( nextFirst )
						datasetY.sort()
						if not genChars( datasetY ) in two:
							datasetY.pop(0)
							break
					else:
						break
			if not datasetY[len(datasetY)-1] == theMax:
				nextLast = int(datasetY[len(datasetY)-1])
				# print()
				# print( 'nextLast:', nextLast )
				for x in range(1,100000):
					# print()
					# print( nextLast, x, nextLast + x )
					nextLast = nextLast + 1
					if nextLast <= theMax:
						datasetY.append( nextLast )
						datasetY.sort()
						if not genChars( datasetY, x=False ) in two:
							datasetY.reverse()
							datasetY.pop(0)
							datasetY.reverse()
							addSpent( datasetY )
							addMatch( datasetY )
							patterns.append( genChars( datasetY ) )
							# print( '\t1' )
							break
					else:
						addSpent( datasetY )
						addMatch( datasetY )
						patterns.append( genChars( datasetY ) )
						# print( '\t2' )
						break
			else:
				addSpent( datasetY )
				addMatch( datasetY )
				patterns.append( genChars( datasetY ) )
				# print( '\t3' )

	def runTest( patternLength ):
		data = generatePatterns( one, 2 )
		# print( len(data) )
		i = 0
		ii = 0
		for dataset in data:
			x = genChars( dataset )
			if x in two:
				addMatch( dataset )
				expandTest( dataset )
				# print( x )
				if test:
					print( x )
				i += 1
			else:
				ii += 1

		result = percentageDiffInt( i, len(data) )
		return result
	resultX = []

	for x in range(2,10):
		if len( one ) > x:
			resultX.append( runTest( x ) )


	newResult = percentageDiffInt( len(matches), len(one) )
	# print( patterns )
	# print( newResult )
	if simple:
		return newResult
	else:
		return newResult, tuple(patterns)



def generatePatterns( string, patternLength ):

	def genP( by ):
		
		offset = 0
		dataset = []
		for offset in range(0,by):
			# print( offset )
			ix = False
			for i,char in enumerate(string):
				if i >= offset:
					ix = ( i + offset )
					
				if not type(ix) == bool:
					# dataset.append( char )
					dataset.append( i )
					if len(dataset) % by == 0:
						if len( dataset ):
							data.append( dataset )
							# print( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data



def stringDiff( one, two ):
	one = one.lower()
	two = two.lower()
	appropriate = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if len(one) > len(two):
		a = len(one)
		b = len(two)
	else:
		b = len(one)
		a = len(two)
	d = a - b
	# if d > 2:
	#   return False
	setA = 0
	theTotal_one = 0
	theTotal_two = 0
	for x in appropriate:
		if x in two:
			theTotal_two += 1
		if x in one:
			theTotal_one += 1
		if x in one and x in two:
			setA += 1

	resultX = []
	resultX.append(percentageDiffInt( setA, theTotal_one ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append(percentageDiffInt( theTotal_one, theTotal_two ))
	resultX.append( testPatterns( one, two ) )
	result = max(resultX)
	
	# resultY = []
	# resultY.append(min(resultX))
	# resultY.append(patternMatch( one, two ))
	# result = max(resultY)
	# print()
	# print( setA, theTotal_one )
	# print( resultX, one, two )

	return result



def fromEpoch( epoch ):
	return datetime.datetime.fromtimestamp(epoch).strftime('%c')

def postLoad( file, epoch=0, theFocus=False ):
	global autoLoadData
	global switches
	global appData
	


	try:
		__.appInfoScan
	except Exception as e:
		if not type( theFocus ) == bool:
			theFocus = theFocus
		else:
			theFocus = __.appReg

		# print( 'theFocus:', theFocus )
		# printVar( appData )

		if type( appData[theFocus]['pipe'] ) == bool:
			hasPipeData = False
		else:
			hasPipeData = True



		# print( type( appData[theFocus]['pipe'] ) )


		# print( appData[theFocus]['pipe'] )


		if type( myFileLocation_File ) == bool:
			hasFile = False
		else:
			hasFile = True

		if __.isRequired_Pipe_or_File and not hasFile and not hasPipeData:
			print(  )
			print( inlineBold('Error:','red')+inlineBold(' Pipe')+' data or '+inlineBold('File')+' is required' )
			print(  )
			sys.exit()

		if __.isRequired_Pipe and not hasPipeData:
			print(  )
			print( 'Error: Pipe data is required' )
			print(  )
			sys.exit()

		if not type( __.isRequired_or_List ) == bool and __.registeredApps[0] == __.appReg:
			meetsRequirements = False


			if 'Pipe' in __.isRequired_or_List:
				if hasPipeData:
					meetsRequirements = True
				if not hasFile and not hasPipeData:
					pass
				else:
					meetsRequirements = True
			if not meetsRequirements:
				for check in __.isRequired_or_List:
					if switches.isActive(check):
						meetsRequirements = True
				if not meetsRequirements:
					print(  )
					print( inlineBold( 'Error:', 'red' ) + ' One of the following is required:', ', '.join( __.isRequired_or_List ) )
					print(  )

					# print( __.registeredApps )

					sys.exit()


		
		appDBA = __.thisApp( file )

		if switches.isActive( 'LoadEpoch' ):
			if '.' in switches.value( 'LoadEpoch' ):
				autoLoadData = True
				epoch = float( switches.value( 'LoadEpoch' ) )
		if autoLoadData and epoch == 0:
			if type( autoLoadData ) == str:
				if '.' in autoLoadData:
					epoch = float( autoLoadData )
			if type( autoLoadData ) == float:
				epoch = autoLoadData

			if epoch == 0:
				autoLoadData = False


		if autoLoadData:
			reclaimAcquiredData( appDBA, epoch, theFocus )
		else:
			releaseAcquiredData( appDBA, theFocus )



def releaseAcquiredData( appDBA, theFocus ):
	global autoBackupData
	global switches
	global appData
	global myFileLocation_Files
	global switches
	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( __.startTime ) + '.json'
	rebuiltCommandRaw = theCommand( appDBA, printThis=False, separate=True )
	if len( rebuiltCommandRaw[1] ):
		rebuiltCommand = rebuiltCommandRaw[0] + ' ' + rebuiltCommandRaw[1]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) + ' ' + rebuiltCommandRaw[1]
	else:
		rebuiltCommand = rebuiltCommandRaw[0]
		rebuiltCommandEpoch = rebuiltCommandRaw[0] + ' -loadEpoch ' + str( __.startTime ) 
	# print( log )
	# print( rebuiltCommandRaw )


	# autoBackupData = True



	info = {
				'epoch': __.startTime,
				'app': appDBA,
				'rebuiltCommand': rebuiltCommand,
				'rebuiltCommandEpoch': rebuiltCommandEpoch,
				'files': [],
				'switches': switches.getTable(),
	}

	if not autoBackupData:
		saveTable2( info, log )

	if autoBackupData:
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				try:
					thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_file' + str(i) + '.cache'
					tmpData = getText( file )
					saveText( tmpData, _v.myAppLogs + _v.slash + thisName )
					info['files'].append( thisName )

				except Exception as e:
					pass

		# print( theFocus, type( appData[theFocus]['pipe'] ) )
		if not type( appData[theFocus]['pipe'] ) == bool:
			thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_pipe' + '.cache'
			saveText( appData[theFocus]['pipe'], _v.myAppLogs + _v.slash + thisName )
			info['files'].append( thisName )
		

		saveTable2( info, log )

		# print()
		# print()
		# printVar( info )

	# 
# _.theCommand( __file__ )
# file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

def reclaimAcquiredData( appDBA, epoch, theFocus=False ):
	global switches
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg

	log = _v.appLogs() + _v.slash+'execution_receipt-' + appDBA + '-' + str( epoch ) + '.json'
	info = getTable2( log )
	# print( log )
	# print( info )
	# printVar( info )

	def pipeFile():
		for file in info['files']:
			if 'pipe' in file:
				return _v.myAppLogs + _v.slash + file
		return False

	def theFiles():
		theFiles = []
		for file in info['files']:
			if not 'pipe' in file:
				theFiles.append( _v.myAppLogs + _v.slash + file )
		return theFiles

	def rebuildSwitches( switchData ):
		# printVar( switchData )
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
		return switchData

	def rebuildFiles( switchData ):
		data = []
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data
	def rebuildFiles( switchData ):
		for i,switch in enumerate(switchData):
			if switch['name'] == 'File' or switch['name'] == 'Files':
				switchData[i]['values'] = []
				for file in info['files']:
					if not 'pipe' in file:
						switchData[i]['values'].append( _v.myAppLogs + _v.slash + file )
				switchData[i]['value'] = ','.join( switchData[i]['values'] )
				data.append( switchData[i] )
		return data


	if switches.onlyLoadEpoch( theFocus=appReg ):
		switchData = rebuildSwitches( info['switches'] )
	else:
		switchData = rebuildFiles( info['switches'] )
	# printVar( switchData )
	switches.loadTable( switchData, theFocus=appReg )
	# print( 'theFocus:', theFocus )

	if not type( pipeFile() ) == bool:
		appData[appReg]['pipe'] = getText( pipeFile() )



def theCommand( file='', theFocus=False, printThis=True, justSwitches=False, separate=False ):
	global switches
	# _.theCommand( __file__, theFocus=False, printThis=True, justSwitches=False  )
	
	if not type( theFocus ) == bool:
		appReg = theFocus
	else:
		appReg = __.appReg
	if len( file ):
		if _v.slash in file or '.py' in file.lower():
			appDBA = __.thisApp( file )
		else:
			appDBA = file
	else:
		appDBA = ''
	theSwitchInfo = switches.rebuild()
	if justSwitches:
		result = theSwitchInfo
	else:
		result = 'p ' + appDBA + ' ' + theSwitchInfo
	if printThis:
		print( result )
	if separate:
		return [ 'p ' + appDBA, theSwitchInfo ]

	return result

def triggerSpace( data ):
	data = data.replace( ',', ' ' )
	return data

def longDashAdd( data ):
	data = _str.clean_latin1( data )
	data = data.replace( ' :', ':' )
	data = data.replace( '-', '—' )
	return data

def longDashRemove( data ):
	data = data.replace( '—', '-' )
	return data


def inRelevantFolder( file ):
	found = inRelevantFolderSearch( file )
	if type( found ) == bool:
		return file
	if os.path.isfile( found ):
		myFileLocation_Files.append( found )
	return found
def inRelevantFolderSearch( file ):
	if os.path.isfile( file ):
		return os.getcwd() +_v.slash+ file

	probableLocations = [
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Downloads'+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'\\powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\vbs'+_v.slash + '*THEFILENAME*'",
	]

	for test in probableLocations:
		f = test.replace( '*THEFILENAME*', file )
		if os.path.isfile( f ):
			return f



	global relevantFolders
	if not len( relevantFolders ):
		rf = getText( _v.relevant_folders, raw=True, clean=2 )
		relevantFolders = rf.split('\n')
	# 

	for folder in relevantFolders:
		f = folder +_v.slash+ file
		if os.path.isfile( f ):
			return f
	return False


def hasExtion( data, wild=False, free=False ):
	global theExtensionsList
	if not len( theExtensionsList ):
		if not wild and not free:
			ext = getText( _v.myTables + _v.slash+'extensions.txt', raw=True, clean=2 )
		elif free:
			ext = getText( _v.myTables + _v.slash+'extensions_free.txt', raw=True, clean=2 )
		else:
			ext = getText( _v.myTables + _v.slash+'extensions_wild.txt', raw=True, clean=2 )
		theExtensionsList = ext.split('\n')
	if not free:
		if '.' in data:
			end0 = data[(-4):]
			end1 = data[(-5):]
			if '.' == end0[0] or '.' == end1[0]:
				testX = data.split('.')
				test = testX[len(testX)-1].lower()
				if test in theExtensionsList:
					return True
	else:
		for ext in theExtensionsList:
			if data.lower().endswith( '.'+ext ):
				return True

	return False



def popDelim( data, delim, pop=1 ):
	data = str( data )
	dataX = data.split( delim )
	i = 0
	while not i == pop:
		dataX.pop()
		i+=1
	return delim.join( dataX )


def addComma( data ):
	txt = str( data )
	if '.' in txt:
		txt = txt.split( '.' )[0]
	n = []
	for x in txt:
		n.append( x )
	n.reverse()
	y = []
	for i,x in enumerate(n):
		y.append( x )
		if ((i+1)%3==0):
			y.append( ',' )
	y.reverse()
	result = ''.join( y )
	result = _str.cleanBE( result, ',' )
	return result



def genAppName( file ):
	if file.lower().endswith( '.py' ):
		x = file.split( '.' )
		x.pop( len(x)-1 )
		result = '.'.join( x )
	else:
		result = file
	return result

def printFields( data, depth=1 ):
	if depth == 1:
		print()
	def tabLoop( depth ):
		result = ''
		i=0
		while not i == depth:
			i+=1
			result += '\t'
		return result
	if type( data ) == list:

		if len(data) and type(data[0]) == dict:
			for row in data[0].keys():
				print( tabLoop( depth ), row )
				printFields( data[0][row], depth+1 )
	elif type( data ) == dict:
		for row in data.keys():
			print( tabLoop( depth ), row )
			printFields( data[row], depth+1 )

def removeReturn( data ):
	for i,row in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

def flattenList( data ):
	result = ''
	for row in data:
		row = row.replace( '\n', '' )
		result += row + '\n'
	result = _str.cleanBE( result, '\n' )
	return result

def resolveIDs( data ):
	global idResolution
	data = str(data)
	# if len( idResolution ) == 0:
	if not len( idResolution ):
		idResolution = getTable('idResolution.json')
	# idResolution = getTable('idResolution.json')
	for idx in idResolution:
		if data in idx['id']:
			return ' ** ' + idx['name'] + ' ** '
	return data

def printSafe( data ):
	data = str( data )
	result = ''
	for ch in data:
		if ch in _v.safeChar:
			result += ch
	return result


def setPipeData( data, theFocus=False, clean=True ):
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		appData[theFocus]['pipe'] = []
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd)
		setPipeDataRan = True

def pipeCleaner(clean=0):
	global appData
	try:
		if not appData[__.appReg]['pipe'][0][0] in _str.safeChar:
			appData[__.appReg]['pipe'][0] = appData[__.appReg]['pipe'][0][1:]
	except Exception as e:
		pass
	try:
		for i,pipeData in enumerate(appData[__.appReg]['pipe']):
			p = appData[__.appReg]['pipe'][i].replace('\n','')
			if clean:
				while p.startswith(' '):
					p = p[1:]

				while p.endswith(' '):
					p = p[:-1]


			appData[__.appReg]['pipe'][i] = p
	except Exception as e:
		pass
	return appData[__.appReg]['pipe']


def copyVar( data ):
	return pyperclip.copy( str(data) )



def cleanDic( data ):
	nowJSON_TXT = d2json( data )
	nowDic = json2d( nowJSON_TXT, True )


def d2json( data, sort_keys=False ):
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return json.dumps(data, indent=4, sort_keys=sort_keys)

def printVar1( data ):
	print( d2json( data ) )


def printVar( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	# saveTable2( data, _v.json_temp )
	# result = getText( _v.json_temp, raw=True )
	# result = type( result )
	result = printVarColor( result )
	print(  )

def printTest( data, color='white', line=None, isPrint=1, shouldExit=1, validate=1, raw=0, profile=False, sort_keys=False,     r=0, v=1, val=1, l=None, x=1, s=False, sk=False ):

	if s or sk:
		sort_keys = True

	if not x:
		shouldExit = 0


	if r:
		raw = True
	if not l is None:
		line = l
	if not v or not val:
		validate = False
	if raw:
		validate = False
	isCode = False



	if not line is None:
		colorThis( [ 'Line:', line ], 'green' )
	if type( data ) == dict:
		isCode = True
	elif type( data ) == list and len(data) and type( data[0] ) == dict:
		isCode = True
	elif type( data ) == list and not isPrint:
		isCode = True
	elif type( data ) == list and isPrint:
		isCode = False
	else:
		isCode = False

	if not validate:
		isCode = False

	if profile:
		# import _rightThumb._profileVariables as _profile
		profile = _profile.records.audit( 'printTest_profile', data )
		data = profile
		isCode = True
	


	if isCode:
		if validate:
			printVar( data, sort_keys )
		else:
			printVarSimple( data, sort_keys )
	else:
		if raw:
			colorThis( str(data), color )
		else:
			colorThis( data, color )

	if shouldExit:
		sys.exit()

def printVar2( data, sort_keys=False ):
	printVarOld( data, sort_keys )
	
def printVarSimple( data, sort_keys=False ):
	printVarOld( data, sort_keys )

def printVarOld( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	print( result )

def printVarSimplePostReplace( data, string, newString, sort_keys=False ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	result = result.replace( string, newString )
	print( result )


def printVar2( data, sort_keys=False ):
	result = d2json( data, sort_keys )
	result = printVarColor_OLD( result )
	print( result )


def printVarColor( data ):
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()
	index = validator.createIndex( data, 'javascript' )
	validator.colorPrint()
	


def printVarColor_OLD( data ):
	result = ''
	for char in data:
		result += printVarColorChar( char )
	return result


	# Gray = '\033[1;30;40m'
	# Red = '\033[1;31;40m'
	# Green = '\033[1;32;40m'
	# Yellow = '\033[1;33;40m'
	# Blue = '\033[1;34;40m'
	# Magenta = '\033[1;35;40m'
	# Cyan = '\033[1;36;40m'
	# White = '\033[1;37;40m'
	# END = '\033[0m'


# def inlineColor( string, color='RED' ):
#   color = color.upper()
#   if not type(string) == str:
#       string = str(string)
#   if color == 'RED':
#       return Color.RED + string + Color.END
#   elif color == 'CYAN':
#       return Color.CYAN + string + Color.END
#   elif color == 'DARKCYAN' or color == 'grey':
#       return Color.DARKCYAN + string + Color.END
#   elif color == 'BLUE':
#       return Color.BLUE + string + Color.END
#   elif color == 'GREEN':
#       return Color.GREEN + string + Color.END
#   elif color == 'YELLOW':
#       return Color.YELLOW + string + Color.END
#   elif color == 'UNDERLINE':
#       return Color.UNDERLINE + string + Color.END


def printVarColorChar( data ):


	what = '('
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )

	what = ')'
	color = 'Background.red'
	if data == what:
		return data.replace( what, colorThis( what, color, shouldPrint=False ) )


	what = '{'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '}'
	color = 'green'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )
	
	what = '['
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineColor( what, color ) )

	what = ']'
	color = 'YELLOW'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '"'
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = "'"
	color = 'white'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ':'
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = ','
	color = 'Magenta'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	what = '='
	color = 'red'
	if data == what:
		return data.replace( what, inlineBold( what, color ) )

	return data



def class2Dic( data ):
	saveTable2( data, _v.json_temp )
	txt = getTable2( _v.json_temp )
	return txt



myFileLocation_Print = True
myFileLocation_File = False
myFileLocation_Files = []
myFileLocation_Pipe = []
def myFileLocations( file, silent=False, currentBaseVersion=3 ):
	global myFileLocation_File
	# if ',' in file and not os.path.isfile( file ):
	#   nFiles = []
	#   for f in file.split(','):
	#       nFiles.append( myFileLocations2( f, silent, currentBaseVersion ) )
	#   file = ','.join( nFiles )
		
	# else:
	#   myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )

	myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )
	if os.path.isfile( myFileLocation_File ) and not myFileLocation_File in myFileLocation_Files:
		myFileLocation_Files.append( myFileLocation_File )
	try:
		autoAbbreviations()
	except Exception as e:
		pass
	if len( myFileLocation_Files ):
	# if len( myFileLocation_Files ) and type( appData[__.appReg]['pipe'] ) == bool:
		if not type( __.trigger_isPipe ) == bool:
			# print( 'HERE', myFileLocation_Files )
			__.appRegPipe = __.appReg

			if 'name' in __.trigger_isPipe:
				justNames = True
			else:
				justNames = False

			tmpFiles = []
			hasFiles = False
			if justNames:
				# print( 'HERE' )
				# setPipeData( myFileLocation_Files, __.appReg )
				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
				for thisFile in myFileLocation_Files:
					if os.path.isfile( thisFile ):
						if not thisFile in myFileLocation_Pipe:
							myFileLocation_Pipe.append( thisFile )
							appData[__.appReg]['pipe'].append( thisFile )
			else:
				for thisFile in myFileLocation_Files:
					if os.path.isfile( thisFile ):
						hasFiles = True
						if not thisFile in myFileLocation_Pipe:
							myFileLocation_Pipe.append( thisFile )
							if type( appData[__.appReg]['pipe'] ) == bool:
								appData[__.appReg]['pipe'] = []
							if 'clean' in __.trigger_isPipe:
								for row in getText( thisFile, raw=True, clean=True ).split('\n'):
									appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
							else:
								for row in getText( thisFile, raw=True ).split('\n'):
									appData[__.appReg]['pipe'].append( row )
									# tmpFiles.append( row )
			# if hasFiles:
			#   if 'clean' in __.trigger_isPipe:
			#       setPipeData( tmpFiles, __.appReg, clean=True )
			#   else:
			#       setPipeData( tmpFiles, __.appReg, clean=False )
			if not hasFiles:
				if type( appData[__.appReg]['pipe'] ) == bool:
					appData[__.appReg]['pipe'] = []
					for row in myFileLocation_Files:
						appData[__.appReg]['pipe'].append( row )



	return myFileLocation_File
def myFileLocations2( file, silent=False, currentBaseVersion=3 ):
	global myFileLocation_Print
	silentSetTo = myFileLocation_Print
	if silent:
		silentSetTo = silent

	if os.path.isfile( file ):
		return file

	if 'tmpf' in file.lower():
		fx = file.lower()
		if 'tmpf' == fx:
			return _v.tmpf
		elif 'tmpf0' == fx:
			return _v.tmpf0
		elif 'tmpf1' == fx:
			return _v.tmpf1
		elif 'tmpf2' == fx:
			return _v.tmpf2
		elif 'tmpf3' == fx:
			return _v.tmpf3
		elif 'tmpf4' == fx:
			return _v.tmpf4
		elif 'tmpf5' == fx:
			return _v.tmpf5
		elif 'tmpf6' == fx:
			return _v.tmpf6
		elif 'tmpf7' == fx:
			return _v.tmpf7
		elif 'tmpf8' == fx:
			return _v.tmpf8
		elif 'tmpf9' == fx:
			return _v.tmpf9

	probableLocations = [
		"_v.myAppsPy + _v.slash+'\\_rightThumb\\\\_' + '*THEFILENAME*' + _v.slash+'\\__init__.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'\\Downloads'+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'\\powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'\\vbs'+_v.slash + '*THEFILENAME*'",
	]

	if file == 'base':
		file = 'base' + str( currentBaseVersion )

	for testThis in probableLocations:
		theTest = eval( testThis )
		theTest = theTest.replace( '*THEFILENAME*', file )
		if os.path.isfile( theTest ):
			if silentSetTo:
				
				print()
				print( 'File not here but in:', theTest )
				print()

			return theTest
	return file



def cleanList( data ):
	for i,d in enumerate(data):
		data[i] = data[i].replace( '\n', '' )
	return data

adminStatus = ''
def isAdmin():
	global adminStatus
	if type(adminStatus) == str:
		tempFile = _v.stmp + _v.slash + genUUID()
		do = 'echo %isAdmin%>'+tempFile
		test = os.system('"' + do + '"')
		isAdmin0 = getText(tempFile)
		isAdmin1 = isAdmin0[0].replace('\n','')
		os.remove(tempFile)
		if 'True' in isAdmin1:
			adminStatus = True
		else:
			adminStatus = False
	return adminStatus

def autoDate( theDate ):
	import _rightThumb._date as _date
	return _date.autoDate( theDate )

def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )

def resolveEpoch( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	return resolveEpochTest( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )

def resolveEpochTest( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	import _rightThumb._date as _date
	return _date.resolveEpoch( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )

def fileDate( theDate ):
	friendly = friendlyDate( theDate )
	friendly = friendly.replace( ' ', '_' )
	friendly = friendly.replace( ':', '-' )
	return friendly

def dateAdd2( theDate, addDays, delim='-' ):
	
	theDate = str( theDate )

	if not delim in theDate:
		try:
			float( theDate )
			theDate = resolveEpochTest( theDate, onlyEpoch='day', delim=delim )
			if type(theDate) == bool:
				print( 'Error:', theDate )
				sys.exit()
		except Exception as e:
			printBold( 'Error: '+ theDate, 'red' )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def txt2Date(text):
	# _.switches.trigger('Watched', _.txt2Date)

	try:
		if not type(text) == str:
			text = ''
	except Exception as e:
		text = ''

	if text == '':
		theDate = datetime.date.today()
		result = str( theDate ).split()[0]
	elif '-' in text:
		if text.count('-') == 2:
			try:
				textSplit = text.split('-')
				# print(textSplit)
				theDate = datetime.datetime( int(textSplit[0]), int(textSplit[1]), int(textSplit[2]), 0, 0 )
				result = str( theDate ).split()[0]
			except Exception as e:
				printBold('Date error: using today\'s date','red')
				theDate = datetime.date.today()
				result = str( theDate ).split()[0]
		else:
			print('Date error: using today\'s date')
			theDate = datetime.date.today()
			result = str( theDate ).split()[0]
	else:
		fnd = 'ymwd'
		do = text.lower().replace(' ','')
		nmb = do
		for t in fnd:
			nmb = nmb.replace(t,'')
		if len(nmb) == 0:
			nmb = 1
		try:
			nmb = int(nmb)
		except Exception as e:
			nmb = 1
		if 'y' in do:
			theDate = datetime.date.today() + datetime.timedelta(-365 * nmb)
		if 'm' in do:
			theDate = datetime.date.today() + datetime.timedelta(-30 * nmb)
		if 'w' in do:
			theDate = datetime.date.today() + datetime.timedelta(-7 * nmb)
		if 'd' in do:
			theDate = datetime.date.today() + datetime.timedelta(-1 * nmb)
		result = str( theDate ).split()[0]
	return result

def genUUID( project='', label='', uniqueTimestamp=False ):
	global appData
	global appInfo
	
	# string = str(uuid.uuid4())
	# string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	try:
		type(appData[__.appReg]['uuid'])
		good = True
	except Exception as e:
		good = False
	if good:

		try:
			timestamp = appData[__.appReg]['start']
		except Exception as e:
			timestamp = time.time()

		if not project == '' or not label == '':
			if type(appData[__.appReg]['uuid']) == str:
				# print()
				# print( '__.appReg', __.appReg )
				# print()
				# print(d2json( appData ))
				# print()
				appData[__.appReg]['uuid'] = {}
				# print(appInfo[__.appReg]['file'])
				# sys.exit()
				appData[__.appReg]['uuid']['app'] = appInfo[__.appReg]['file']

			if not type(appData[__.appReg]['uuid']) == str:
				
				appData[__.appReg]['uuid']['uuid'] = string
				appData[__.appReg]['uuid']['timestamp'] = timestamp
				appData[__.appReg]['uuid']['project'] = ''
				appData[__.appReg]['uuid']['label'] = ''

				if uniqueTimestamp:
					appData[__.appReg]['uuid']['timestamp'] = time.time()

				if not project == '':
					appData[__.appReg]['uuid']['project'] = project

				if not label == '':
					appData[__.appReg]['uuid']['label'] = label
					
				uuidLog = getTable('uuid_log.json')
				uuidLog.append(appData[__.appReg]['uuid'])
				saveTable(uuidLog,'uuid_log.json',printThis=False)
			# appData[__.appReg]['uuid'] = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string

def saveText( rows, theFile, errors=True ):
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print(type(rows))
		if type(rows) == str:
			# print(rows)
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
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
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		open(theFile, 'wb').write(rows)
		if errors:
			print( 'Auto correction when saving text' )

def getText( theFile, raw=False, clean=False,  e=0 ):
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
	else:
		if not e:
			return None
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines

def getSize(fileobject):
	fileobject.seek(0,2) # move the cursor to the end of the file
	size = fileobject.tell()
	return size

# def formatSize(size):
#   result = ''
#   if size == None:
#       result = ''
#   elif size < 1024:
#       result = str(size) + ' B'
#   elif size > 1024 and size < 1048576:
#       num = round(size / 1024, 2)
#       result = str(num) + ' KB'
#   elif size > 1048576 and size < 1073741824:
#       num = round(size / 1048576, 2)
#       result = str(num) + ' MB'
#   elif size > 1073741824 and size < 137438953472:
#       num = round(size / 1073741824, 2)
#       result = str(num) + ' GB'
#   # if size < 1:
#   #   result = ''
#   return result

def monthByNumber(month):
	result = ''
	if str(month) == '01':
		result = 'Jan'
	if str(month) == '02':
		result = 'Feb'
	if str(month) == '03':
		result = 'Mar'
	if str(month) == '04':
		result = 'Apr'
	if str(month) == '05':
		result = 'May'
	if str(month) == '06':
		result = 'Jun'
	if str(month) == '07':
		result = 'Jul'
	if str(month) == '08':
		result = 'Aug'
	if str(month) == '09':
		result = 'Sep'
	if str(month) == '10':
		result = 'Oct'
	if str(month) == '11':
		result = 'Nov'
	if str(month) == '12':
		result = 'Dec'
	return result


def months_between(start_date, end_date):
	# start_date = int(start_date)
	# end_date = int(end_date)
	# st = str(formatDateYear(start_date)) + '-' + str(formatDateMonth(start_date)) + '-' +  str(formatDateDay(start_date)) 
	# en = str(formatDateYear(end_date)) + '-' + str(formatDateMonth(end_date)) + '-' +  str(formatDateDay(end_date))
	start = datetime.date(int(formatDateYear(start_date)), int(formatDateMonth(start_date)), int(formatDateDay(start_date)) )
	end = datetime.date(int(formatDateYear(end_date)), int(formatDateMonth(end_date)), int(formatDateDay(end_date)) )
	months = calculate_monthdelta(start, end)
	return months


# def timeout(start,t):

#     # os._exit(0)
#     # print('loop')
#     global completed
#     global killTime
#     global timeoutKill
#     ts = dt.now()

#     if start == 'start':
#         timeoutKill = False
#         completed = False
#         killTime = ts + timedelta(seconds=int(t))

#     if completed == False and ts < killTime:
#         x = Timer(0.0, timeout, ('loop',t))
#         x.start()
#     elif completed == False:
#         timeoutKill = True
#         completed = True
#         print('\n*** Timeout ***()')
#         # os._exit(0)

# def processTimeout():
#     global switches
#     global defaultTimeout
#     if switches.isActive('Timeout') == True:
#         try:
#             defaultTimeout = int(switches.value('Timeout'))
#         except Exception as e:
#             errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(switches.value('Timeout'))", 'vars': [{'name': 'timeout', 'value': switches.value('Timeout')}], 'error': e})
#             printBold('Error:','red')
#             print('\tBad timeout value.')
#             os._exit(0)

#     # print(defaultTimeout)
#     x = Timer(0.0, timeout, ('start',defaultTimeout))
#     x.start()


def showLine( string, plus = '', minus = '', plusOr = False ):
	# print(plus)
	# print(string)
	
	global switches
	if switches.isActive('Plus') or not plus == '':
		# print('asdf')
		result = positiveResults(string,plus,plusOr)
		if not result and switches.isActive('PlusClose'):
			result = closeResults( string )

	else:
		result = True
	if result == True and  (switches.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print(result)
	return result
def closeResults( string ):
	global switches
	global plusClose
	
	if len( switches.value('PlusClose') ):
		try:
			plusClose = float( switches.value('PlusClose') )
		except Exception as e:
			pass

	test = patternMatch( string, switches.value('Plus') )
	if test >= plusClose:
		# print( test, string )
		return True
	else:
		return False



def positiveResults(string,plus='',plusOr=False):
	global switches
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus')
	if type( plusInput ) == str:
		plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	string = string.lower()
	# print( plusList )
	# sys.exit()
	for s in plusList:
		s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not string.find(ci(s)) == -1 or s in string:
			cnt += 1


		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result

def minusResults(string,minus=''):
	global switches
	string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switches.values('Minus')
	if type( minusInput ) == str:
		minusInput = minusInput.lower()
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			minusInput[i] = minusInput[i].lower()
		minusList = minusInput

	try:
		for s in minusList:
			s = s.lower()
			if len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					result = False
					break
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					result = False
					break
			if not string.find(ci(s)) == -1 or s in string:
				result = False
				break
	except Exception as e:
		pass
	return result

def saveLog( logname, rows=[], focus=True, printThis=True ):
	global appInfo
	global appData
	
	indentCode = True
	log = 'app_audit_log_TIMESTAMP__FILENAME__LOGNAME__INSTANCE.json'

	if type(focus) == bool:
		focus = __.appReg
		
	if not len(rows) and logname == 'threads':
		global threads
		rows = threads.log()
		# print( rows )
		# sys.exit()
	if not len(rows) and logname == 'audit':
		for ad in __.structure():
			if len(appData[ad]['audit']) > 0:
				rows.append( { 'app': appInfo[ad]['file'], 'focus': ad, 'records': appData[ad]['audit'] } )
	try:
		if len(appInfo[focus]['instance']) > 0:
			log = log.replace('INSTANCE',appInfo[focus]['instance'])
		else:
			log = log.replace('__INSTANCE','')
	except Exception as e:
		log = log.replace('__INSTANCE','')
	
	log = log.replace('TIMESTAMP',str(appData[focus]['start']))
	log = log.replace('FILENAME',appInfo[focus]['file'])
	log = log.replace('LOGNAME',logname)
	
	file0 = _v.myTables + _v.slash+'applogs'+_v.slash + log

	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=True)
	else:
		dataDump = json.dumps(rows)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + file0)

def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,    p=1   ):

	if k or s:
		sort_keys = True

	if not p:
		printThis = False


	# defaults to myTables
	px = ''
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
		# import _rightThumb._md5 as _md5

		theFileLabel = theFile
		if _v.slash in theFileLabel:
			global appInfo
			tfl = theFileLabel.split(_v.slash)
			tfl.reverse()
			theFileLabel = str(appInfo[__.appReg]['liveAppName']) + '__' + tfl[0]
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


def getTable( theFile, tableTemp=False, printThis=False,     isDic=None, isList=None ):
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
		if isDic is None and isList is None:
			json_data = []
		if isDic:
			json_data = {}
		if isList:
			json_data = []
	return json_data

def getTable3(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r') as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data

def getTable2( theFile,     isDic=None, isList=None ):
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
			
def saveTable2( rows, theFile, printThis=False, sort_keys=False, indentCode=True ):
	# print('*******************',theFile)

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

def saveTable3( rows, theFile, printThis=False ):
	# print('*******************',theFile)
	dataDump = json.dumps(rows)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)


def tempFile(rows,theFile):
	file0 = _v.stmp + _v.slash + theFile
	file = open(file0,'w')
	for r in rows:
		file.write(r)                
	file.close()

def stamp2Date(ts):
	# print(ts)
	# print(datetime.datetime.fromtimestamp(int(ts) / 1e3))
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)
def float2Date(ts):
	import _rightThumb._date as _date
	auto = _date.autoDate( ts )
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
		# print( stamp2Date(ts) )
	return stamp2Date(ts)
def float2Date2(ts):
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
	return str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
	# return str(datetime.datetime.fromtimestamp(ts / 1e3))
	# return str(ts)
	# return str(datetime.datetime.fromtimestamp(ts)).split('.')[0] + '\t' + str(ts)
	# return str(ts).split('.')[0] + '\t' + str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
def float2Date3(ts):
	return str(datetime.datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))
def float2Date3B(ts,isJson = True):
	stmp = float2Date3(ts)
	dt = stmp.split(' ')[0]
	preResult = {'year': dt.split('-')[0],'month': dt.split('-')[1],'day': dt.split('-')[2]}
	if isJson:
		result = preResult
	else:
		result = str(preResult['year']) + '-' + str(preResult['month']) + '-' + str(preResult['day'])

	return result

def expireCheck(theDate,delim):
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	fdtl = theDate.split(delim)
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate
	return int(diff.days)

def dateDiff( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		try:
			theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )
			if type(theDate0) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
			sys.exit()


	if not delim in theDate1:
		try:
			theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )
			if type(theDate1) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
			sys.exit()

	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))
	
def dateDiffX( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )



	if not delim in theDate1:
		theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )



	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))

def dateAdd(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def dateSub(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 - datetime.timedelta(days=addDays)

def listAverage(theList):
	total = 0
	for item in theList:
		total += item
	result =  total / len(theList)
	return result 
def date2epoch(theDate,delim='-'):
	theDate = str(theDate)
	if len( theDate ) == 0:
		return ''
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(' ')[0].split('-')
	if ':' in theDate:
		theDate = theDate.replace('.',':')
		if theDate.count(':') == 2:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S')
		elif theDate.count(':') == 1:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M')
		elif theDate.count(':') == 3:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S:%f')
		else:
			print('Error: date2epoch')
			sys.exit()

	else:
		stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
	return float(time.mktime(stmp.timetuple()))

def validateEmail(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip(data)
	good = True
	# if not '@' in data:
	if not data.count('@') == 1:
		good = False
	if good:
		if not '.' in data.split('@')[1]:
			good = False
	# if data.count('@') == 1:
	if not good and len(data) > 0:
		data = ' ___________ * BAD * ___________'
	return data

def figureOutDate(theDate, theFormat):
	theFormat = str(theFormat)
	theFormat = _str.replaceDuplicate(theFormat,' ')
	theFormat = _str.cleanBE(theFormat,' ')
	theFormat = theFormat.lower()

	theFormatExp = 'dmy'
	if not len(theFormat) == 3:
		print('format error, expected: dmy, ymd')
		sys.exit()
	if theFormat[0] in theFormatExp and theFormat[1] in theFormatExp and theFormat[2] in theFormatExp:
		pass
	else:
		print('format error, expected: dmy, ymd')
		sys.exit()
	# theFormat = 'dmy'
	theDate = str(theDate)
	theDate = _str.replaceDuplicate(theDate,' ')
	theDate = _str.cleanBE(theDate,' ')

	
	n = '0123456789'
	a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	autoDelim = ''
	for d in theDate:
		if d in n:
			pass
		elif d in a:
			pass
		else:
			autoDelim = d
			break

	theDateDe = theDate.split(autoDelim)
	info = {}

	info[theFormat[0]] = theDateDe[0]
	info[theFormat[1]] = theDateDe[1]
	info[theFormat[2]] = theDateDe[2]
	if info['m'][0] in a:
		m = info['m']
		m = m.lower()
		found = False
		for monththeDate in getMonthData():
			# print(monththeDate)
			# sys.exit()
			full = monththeDate['month']
			abbrev = monththeDate['abbrev']
			mNumber = monththeDate['number']
			full = full.lower()
			abbrev = abbrev.lower()
			if m == full or m == abbrev:
				found = True
				info['m'] = mNumber
		if not found:
			ans = input('What Month? ')
			if len(ans) == 0:
				print('Month error')
				sys.exit()
			try:
				int(ans)
			except Exception as e:
				printBold('Month error','red')
				sys.exit()
			if len(ans) == 1:
				info['m'] = 0 + ans
			elif len(ans) == 2:
				info['m'] = ans
			else:
				printBold('Month error','red')
				sys.exit()

	ifoy = info['y']
	ifom = info['m']
	ifod = info['d']
	pResult = info['y'] + '-' + info['m'] + '-' + info['d']
	hasDup = False
	if pResult.count(ifoy) > 1:
		hasDup = True
	if pResult.count(ifom) > 1:
		hasDup = True
	if pResult.count(ifod) > 1:
		hasDup = True


	changed = []
	def test(l):
		result = ''
		if int(l) > 1000:
			result = 'y'
		elif int(l) > 12:
			result = 'd'
		return result
	fList = ''
	if test(ifom) == 'y':
		fList += 'y'
		info['y'] = ifom
		# info['m'] = ifoy
	if test(ifod) == 'y':
		fList += 'y'
		info['y'] = ifod
		# info['d'] = ifoy
	if test(ifod) == 'd':
		fList += 'd'
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifom) == 'd':
		fList += 'd'
		info['d'] = ifom
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifod) == '' and 'd' in fList:
		info['m'] = ifod
	# print(test(ifoy))
	# print(fList)

	result = info['y'] + '-' + info['m'] + '-' + info['d']
	# print(result)
	if not hasDup:
		hasDup = False
		if result.count(ifoy) > 1:
			hasDup = True
		if result.count(ifom) > 1:
			hasDup = True
		if result.count(ifod) > 1:
			hasDup = True
		if hasDup:
			print('Error please specify format: ymd')
			sys.exit()
	else:
		if result.count(info['y']) > 1:
			print('Error please specify format: ymd')
			sys.exit()

	print(result)
	sys.exit()
	return result



def getMonthData():
	monthData = getText(_v.myTables + _v.slash+'month.txt')
	monthList = []
	for md in monthData:
		md = md.replace('\n','')
		mds = md.split(',')
		monthList.append({'month': mds[0], 'abbrev': mds[1], 'number': mds[2]})
	return monthList



def formatPhone00(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)
	data = _str.cleanBE(data,'.')
	return data

def formatPhone0(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = '(' + data[0] + data[1] + data[2] + ') ' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone1(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '-' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def formatPhone2(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '.' + data[3] + data[4] + data[5] + '.' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

def updateLine(string):
	# if type(string) == list:
		

	string = str(string)
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(" " * len(string))
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(string)
	sys.stdout.flush()

def getLastTableSplit(theFile,tableTemp = 'split'):
	if tableTemp == 'split':
		basePath = _v.myTables + _v.slash+'tablesets'
	else:
		basePath = _v.stmp
	# print(basePath)
	dirList = os.listdir(basePath)
	fileList = []
	for d in dirList:
		if d.startswith(theFile):
			fileList.append(d)
	# print(fileList)
	fileList.sort()
	# print(fileList)
	# print()
	# print(fileList[len(fileList)-1])
	# print(fileList)
	# file0 = basePath + _v.slash + fileList[len(fileList)-1]
	# print(file0)
	return getTable(fileList[len(fileList)-1],tableTemp)

def saveTableSplitNew( rows,theFile,tableTemp = True,printThis = True, project=False ):
	# defaults to myTables
	print( 'save size:', len(rows))
	if tableTemp:
		file0 = _v.myTables + _v.slash+'tablesets' + _v.slash + theFile
	elif project:
		file0 = _v.myTables + _v.slash+'projects' + _v.slash + theFile

	else:
		file0 = _v.stmp + _v.slash + theFile

	def count(cnt):
		char = 6
		cnt = str(cnt)
		lencnt = len(cnt)
		if lencnt == 1:
			cnt = '00000' + cnt
		if lencnt == 2:
			cnt = '0000' + cnt
		if lencnt == 3:
			cnt = '000' + cnt
		if lencnt == 4:
			cnt = '00' + cnt
		if lencnt == 5:
			cnt = '0' + cnt
		cnt = '_' + cnt
		return cnt

	suffix = '.json'
	cnt = 0
	path = file0 + count(cnt) + suffix
	while os.path.isfile(path) == True:
		cnt += 1
		path = file0 + count(cnt) + suffix

	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(path,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + path)

def sort(rows, name):
	global errors
	tempFields = []
	sortBy = {}
	sortList = name.split(',')
	sortList.reverse()

	### Check for bad sort input
	for item in sortList:
		item = item
		try:
			if item.count(':') > 0:
				sb = item.split(':')[1]
			else:
				sb = item
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})



	for item in sortList:
		try:
			direction = item.split(':')[0]
			sb = item.split(':')[1]
			if direction == 'asc':
			# if direction.find('a') == 0:
				rows = sorted(rows, key=itemgetter(sb))
			else:
				rows = sorted(rows, key=itemgetter(sb), reverse=True)
		except Exception as e:
			try:
				pass
				rows = sorted(rows, key=itemgetter(item))
			except Exception as e:
				errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			

		sortBy[item] = str(uuid.uuid4())
		tempFields.append( sortBy[item] )
		i = 0
		for row in rows:
			rows[i][sortBy[item]] = i
			i += 1

	# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

	sortCode = 'rows = sorted(rows, key=lambda d: ('
	for item in sortList:
		sortCode += "d['" + str(sortBy[item]) + "'],"
	sortCode = sortCode[:-1]
	sortCode += '))'
	exec(sortCode)
	if len( tempFields ):
		# print( tempFields )
		for ix,r in enumerate(rows):
			for tmp in tempFields:
				try:
					del rows[ix][tmp]
				except Exception as e:
					pass

	return rows


class Switch:

	def __init__(self, name, switch, expected_input_example, description):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = None
		self.values = []
		self.expected_input_example = expected_input_example
		self.documentation = { 'description': description, 'examples': [], 'required': [], 'related': [] }

		# print()
		# print()

		# for key in dir(self):
		#   if not key.startswith('_'):
		#       x = 'self.'+key
		#       print( x, eval(x) )

	def trigger(self,script):
		self.script_trigger = script



class Switches:

	def __init__(self):
		self.switches = []
		self.index = {}
		self.appRegDefault = None
		self.appReg = __.appReg
		self.hasRequired = []
		self.isRequired = {}


	def all( self, appReg=None, omit=None, omitDefaults=True,             od=1 ):
		if not od:
			omitDefaults = False
		if omitDefaults:
			omitList = [ 'Help', 'Column', 'Sort', 'Debug', 'Errors', 'Timeout', 'GroupBy', 'ShortenColumn', 'Long', 'Length', 'Report', 'Plus', 'Minus', 'PlusOr', 'PlusClose', 'PrintAutoAbbreviations', 'LoadEpoch', 'NoColor', 'Clean', 'NoCount', 'Count' ]
		else:
			omitList = []

		if not  omit is None:
			if type(omit) == str:
				omit = omit.replace(  ' ', '' )
				omit = omit.split(',')
			for x in omit:
				omitList.append( x )


		# appReg values expected: None, 1, true, 'all'
		if appReg is None:
			appReg = __.appReg

		result = []
		for i,row in enumerate(self.switches):
			if not row.name in omitList:
				if row.active:
					shouldAdd = True
					if type( appReg ) == str:
						if not appReg == 'all':
							if not row.appReg == appReg:
								shouldAdd = False

					if shouldAdd:
						result.append({
											'active': row.active,
											'name': row.name,
											'value': row.value,
											'values': row.values,
											'appReg': row.appReg,
						})
		return result



	def documentation( self, name, data ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if row.name == name:
					# print( 'SET' )
					if self.switches[i].appReg == __.appReg:

						try:
							if len( data['description'] ):
								self.switches[i].documentation['description'] = data['description']
						except Exception as e:
							pass

						try:
							if len( data['examples'] ):
								self.switches[i].documentation['examples'] = data['examples']
						except Exception as e:
							pass

						try:
							if len( data['required'] ):
								self.switches[i].documentation['required'] = []
								self.switches[i].documentation['related'] = []
								for record in data['required']:
									if record == 'Pipe':
										__.isRequired_Pipe = True
									else:
										self.switches[i].documentation['required'].append( record )
										self.switches[i].documentation['related'].append( record )
										if not name in self.hasRequired:
											self.hasRequired.append( name )
								

						except Exception as e:
							pass

						try:
							if len( data['related'] ):
								for record in data['related']:
									self.switches[i].documentation['related'].append( record )
						except Exception as e:
							pass

						try:
							if type( data['isRequired'] ) == bool:
								if data['isRequired']:
									if not name in self.isRequired[__.appReg]:
										self.isRequired[__.appReg].append( name )
						except Exception as e:
							pass



		except Exception as e:
			result = False
		return result


	def record( self, name ):
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						return i
		except Exception as e:
			result = False
		return result
	def dumpSwitches(self,includeBlank=False):
		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if includeBlank:
				data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			else:
				if not row.value is None or row.active:
					data.append({ 'name': row.name, 'value': row.value, 'appreg': row.appReg })
			# print(row.name,'\t',row.value,'\t',row.appReg)
		tables.register('data',data)
		tables.print('data','appreg,name,value')
	def register(self, name, switch, expected_input_example = None, isRequired=False, isPipe=False, description=''):

		self.switches.append(Switch(name, switch, expected_input_example, description))

		try:
			if not type(self.isRequired[__.appReg]) == list:
				self.isRequired[__.appReg] = []
		except Exception as e:
			self.isRequired[__.appReg] = []
		
		

		switch = switch.replace( ' ', '' )

		if not type( isPipe ) == bool:
			if 'name' in isPipe and ( 'data' in isPipe or 'clean' in isPipe ):
				pass
			elif 'name' in isPipe:
				__.trigger_isPipe = 'name'
			elif 'data' in isPipe or 'clean' in isPipe:
				if 'clean' in isPipe:
					__.trigger_isPipe = 'data,clean'
				else:
					__.trigger_isPipe = 'data'
		elif isPipe:
			__.trigger_isPipe = 'data'


		if isRequired:
			if not name in self.isRequired[__.appReg]:
				self.isRequired[__.appReg].append( name )



	def fieldSet( self, name, column, value, theFocus=False ):# updateSwitchField

		if type( theFocus ) == bool:
			theFocus = __.appReg

		if column == 'value':
			if self.fieldExists( name, 'script_trigger', theFocus ):
				value = self.scriptTrigger( name, value, theFocus  )
				# self.fieldGet(name,'script_trigger')(value)
			elif self.fieldExists( name, 'script_trigger', theFocus ) == True:
				script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)# script_trigger_external
				value = eval(script)
		# print( name, column, value )
		# sys.exit()
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == theFocus:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value

					else:
						# self.switches[i][column] = value
						exec('self.switches[i].' + column + '= value')
						# value = str(value)
						# try:
						#   exec('self.switches[i].' + column + '=str(\'' + value + '\')')
						# except Exception as e:
						#   exec('self.switches[i].' + column + '=\'' + value + '\'')
			
		return ''



	def fieldExists( self, name, column, theFocus=False ):# doesFieldExist
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger( self, name, value, theFocus=False ):# externalScriptTrigger
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					value = self.switches[i].script_trigger(value)# script_trigger_external
		return value

	def fieldGet2(self,name,column):# getSwitchField
		# print(name,column)
		result = ''
		for i,row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result

	def fieldGet( self, name, column, theFocus=False ):# getSwitchField
		# print(name,column)
		result = ''
		if not column == 'pos':

			if name == 'NoColor' and column == 'active':

				found = False

				for i,row in enumerate(self.switches):
					if row.name == name:
						# print( row.name, row.active )
						if row.active:
							found = True

				result = found
						
				# print( 'here', name, found )
				# sys.exit()


			else:


				i = self.searchIndex( name, theFocus )
				if i is None:

					if column == 'active':
						return False

					if column == 'value':
						return ''

					if column == 'values':
						return []

					printBold( 'Error: Nonexistent Switch', 'red' )
					print( name, column, theFocus )
					printVar( self.index )
					sys.exit()
				row = self.switches[i]
				result = eval('row.' + column)

		else:
			if type( theFocus ) == bool:
				theFocus = __.appReg
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == theFocus:
					if row.name == name:
						result = eval('row.' + column)
		return result

	def isActive( self, name, theFocus=False ):# isSwitchActive
		return self.fieldGet( name, 'active', theFocus )

	def getField( self, name, field, theFocus=False ):
		return self.fieldGet( name, field, theFocus )

	def value( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'value', theFocus )
		if result is None:
			result = ''
		return result

	def values( self, name, theFocus=False ):# getSwitchValue
		result = self.fieldGet( name, 'values', theFocus )
		if result is None:
			result = []
		return result


	def trigger(self,name,script):
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script)


	def value2(self,name):
		switchInput = sys.argv

		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:

						if switchInput[i] == ':':
							switchInput[i] = switchInput[i].replace(':','_;192B;_')
						if switchInput[i] == ',':
							switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			result = _str.cleanAll(result,'"','')
			result = _str.cleanAll(result,':,',':')
			result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = None
		return result


	def value3(self,name):
		switchInput = sys.argv
		data = []
		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			for i,a in enumerate(switchInput):
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:

						data.append( a )


		except Exception as e:
			data = None
		return data

	def isSwitch(self,string):# checkIfSwitch
		result = False
		for i,a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
					# print(b,result)
		return result

	def format(self,name):# processSwitchFormatting
		value = self.value2(name)
		if self.fieldExists(name,'script_trigger') == True:
			value = self.scriptTrigger(name,value)
		elif self.fieldExists(name,'script_trigger') == True:
			script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def format2( self, name ):

		values = self.value3(name)
		if values is None:
			values = []
		else:
			for i,value in enumerate(values):
				if self.fieldExists(name,'script_trigger') == True:
					values[i] = self.scriptTrigger(name,value)
				elif self.fieldExists(name,'script_trigger') == True:
					script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
					values[i] = eval(script)

		return values

	def exists(self,name):# checkSwitchExist
		result = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result

	def process( self, helpx=False ):
		global customHelp
		global argvProcess
		global printAutoAbbreviations_scheduled
		for ii,sw in enumerate(self.switches):
			if self.switches[ii].appReg == __.appReg:
				self.switches[ii].pos = None
				self.switches[ii].active = False
				self.switches[ii].value = None
		switchHelp = []
		isActiveList = []
		hasActiveRequireList = []
		isActiveRequireList = []

		if argvProcess:
			for i,a in enumerate(sys.argv):
				a = a.replace(':','')
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)
								self.switches[ii].values = self.format2(self.switches[ii].name)

								isActiveList.append( ii )
								if self.switches[ii].name in self.hasRequired:
									hasActiveRequireList.append( ii )
								if self.switches[ii].name in self.isRequired[__.appReg]:
									isActiveRequireList.append( ii )

								if type( self.switches[ii].value ) == str:
									if '-??' in self.switches[ii].value:
										switchHelp.append(ii)

		if self.exists('_Raw') == True:
			# print('test')
			self.fieldSet('_Raw','pos',1)
			self.fieldSet('_Raw','active',True)
			self.fieldSet('_Raw','value',self.format('_Raw'))


		for i,record in enumerate(self.switches):
			if self.appRegDefault is None:
				self.appRegDefault = self.switches[i].appReg
			self.index[ self.switches[i].appReg ] = {}
		for i,record in enumerate(self.switches):
			self.index[ self.switches[i].appReg ][self.switches[i].name] = i



		if len( switchHelp ):
			if __.cls_process_switches_help:
				os.system('cls')

			somethingPrinted = False
			for i in switchHelp:
				if len( self.switches[i].documentation['description'] ):
					somethingPrinted = True
					print()
					print( inlineBold('Description:\t'), self.switches[i].documentation['description'] )
					print()
				if len( self.switches[i].documentation['examples'] ):
					printBold( 'Examples:' )
					for example in self.switches[i].documentation['examples']:
						if type(example) == list:
							_.colorThis( '\t\t'+example[0], example[1]  )
						else:
							colorizeRow( '\t\t'+ example , 2)



			if somethingPrinted:
				sys.exit()

		if self.isActive('Help') or helpx:
			global appInfo
			global fields
			self.fieldSet('Long','active',True)
			if __.cls_process_switches_help:
				os.system('cls')
			# os.system('cls')
			print('')
			try:
				
				print( inlineBold('Description: \t'), appInfo[__.appReg]['description'] + '\n')
				configured = True
			except Exception as e:
				configured = False
			try:
				if len(appInfo[__.appReg]['prerequisite']) > 0:
					printBold('Prerequisite:')
					for docItem in appInfo[__.appReg]['prerequisite']:
						if type(docItem) == list:
							colorThis( '\t\t'+docItem[0], docItem[1]  )
						else:
							colorizeRow( '\t\t'+ docItem , 2)
						colorizeRow('\t' + prereq,2)
					print('\n')
			except Exception as e:
				pass
			try:
				if len(appInfo[__.appReg]['relatedapps']) > 0:
					printBold('Related Apps:')
					for docItem in appInfo[__.appReg]['relatedapps']:
						if type(docItem) == list:
							colorThis( '\t\t'+docItem[0], docItem[1]  )
						else:
							colorizeRow( '\t\t'+ docItem , 2)
					print('\n')
			except Exception as e:
				pass

			if configured:
				if len(appInfo[__.appReg]['examples']) > 0:
					printBold('Examples:')
					for docItem in appInfo[__.appReg]['examples']:

						if type(docItem) == list:
							colorThis( '\t\t'+docItem[0], docItem[1]  )
						else:
							colorizeRow( '\t\t'+ docItem , 2)

						# colorizeRow('\t' + ex,2)
					print('\n')
				if len(appInfo[__.appReg]['columns']) > 0:
					printBold('Columns and abbreviations:')
					result = ''
					if len( appInfo[__.appReg]['columns'] ):
						# fields.register( 'columns', 'name,abbreviation', script=__.triggerTest )
						fields.asset( 'columns', appInfo[__.appReg]['columns'] )
						print()

					if __.columnAbbreviations == 0:
						for col in appInfo[__.appReg]['columns']:
							result += col['name'] + '(' + col['abbreviation'] + '), '
						result = result[:-2]
						colorizeRow('\t' + result + '\n',2)

					if __.columnAbbreviations == 1:
						for col in appInfo[__.appReg]['columns']:
							abbreviation =  fields.value( 'columns', 'abbreviation', col['abbreviation'] )
							name =          fields.value( 'columns', 'name', col['name'] )
							colorizeRow( '\t' + abbreviation + '\t' + name )
							# print( '\t', col['abbreviation'], '\t', col['name']  )

					if len( appInfo[__.appReg]['columns'] ):
						print()
						print()
					# print('\n')
			self.print()
			sys.exit()


		if len( self.isRequired[__.appReg] ):
			allSatisfied = True
			
			for req in self.isRequired[__.appReg]:
				satisfied = False
				for i in isActiveRequireList:
					if self.switches[i].name.lower() == req.lower():
						satisfied = True

				try:
					__.appInfoScan
				except Exception as e:
					if not satisfied:
						allSatisfied = False
						print()
						print( colorThis( 'Error:', 'red', p=0 ) + ' missing required switch:', req )
						sys.exit()


		if len( hasActiveRequireList ):
			allSatisfied = True
			for i in hasActiveRequireList:
				satisfied = False
				for r in self.switches[i].documentation['required']:
					for ia in isActiveList:
						if self.switches[i].name.lower() == r.lower():
							satisfied = True
				if not satisfied:
					if not i in switchHelp:
						switchHelp.append( i )
						print()
						print( 'Error:\t\t missing required switch' )
					allSatisfied = False



		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			# self.print()
			self.printStatus()
			sys.exit()
		
		if printAutoAbbreviations_scheduled:
			printAutoAbbreviations()

		# theErrors()
		pass
		pass
		# for i,record in enumerate(self.switches):
		#   self.index[ self.switches[i].name +'._.'+ self.switches[i].appReg ] = i

		
		
	def searchIndex( self, name, appReg ):
		if type(appReg) == bool or appReg is None:
			appReg = __.appReg
		try:
			result = self.index[ appReg ][ name ]
			
			# result = self.index[ name +'._.'+ appReg ]
		except Exception as e:
			try:
				result = self.index[ self.appRegDefault ][ name ]
			except Exception as e:
				# print( name, appReg, self.appRegDefault )
				result = None

		return result


	def print(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				switch.append({'name':sw.name ,'switch':sw.switch,'expected_input_example': sw.expected_input_example})
		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,expected_input_example')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = 'False'
				value = sw.value
				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = 'False'

				switch.append({'name':sw.name ,'active':active,'value': value})
		# def test(value):
		#   value = value + '_V_'
		#   return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,active,value')
	def length(self):
		ii = 0
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				ii += 1
		return ii

	def rebuild( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			# if not row.value is None:
			if row.appReg == appReg:
				if row.active:
					sX = row.switch.split(',')
					if row.value is None:
						r = sX[0]
					else:
						r = sX[0] + ' ' + str(row.value)
					data.append( r )
			# print(row.name,'\t',row.value,'\t',row.appReg)
		return ' '.join( data )
	def getTable( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		data = []
		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active:

					info = {
								'name': row.name,
								'value': row.value,
								'values': row.values,
					}

					data.append( info )
		return data


	def loadTable( self, data, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			for info in data:
				if row.appReg == appReg:
					if row.name == info['name']:

						self.switches[i].value = info['value']
						self.switches[i].values = info['values']
						self.switches[i].active = True

	def onlyLoadEpoch( self, theFocus=False ):
		if not type( theFocus ) == bool:
			appReg = theFocus
		else:
			appReg = __.appReg


		for i,row in enumerate(self.switches):
			if row.appReg == appReg:
				if row.active and not row.name == 'LoadEpoch':
					return False


		return True



#   def getSelf(self,name):
#       result = ''
#       for sw in self.switches:
#           if sw.name == name:
#               result = sw
#       return result
# def getSwitchSelf(name):
#   global switches
#   return switches.getSelf(name)
def ci2(string):
	string = ci(string)
	string = _str.replaceAll(string,',',' ')
	return string

class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table
		# print(self.name)



class Table:

	def __init__(self,name,asset=[]):
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print()
			# for x in dir(self.views[i]):
			#   print(x)

			if self.views[i].name == name:
				# print('found')
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				# print(switches.value('Sort'))
				# try:
					
				# except Exception as e:
				#   pass
				# print('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#   self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if switches.isActive('Length'):
			result = self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += '  .' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += '  .' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print('*** ' + name)
		size = len(name) + spacer
		
		# print(name,00)
		# rows[0][name]
		try:
			pass
			rows[0][name]
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			print(9)
			print(name)
			print(rows[0])
			os._exit(0)
		# print(name)
		for item in rows:
			shorten = True
			if switches.isActive('Long') == True:
				shorten = False
				if switches.isActive('ShortenColumn') == True:
					shortenColumn = switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
				
			if shorten == True and not switches.isActive('Length'):
				try:
					text = self.nameLength( str(self.scriptTriggerField(name,item[name])) ,'')
				except Exception as e:
					text = self.nameLength(str(item[name]),'')
			else:
				if switches.isActive('Length'):
					# print('asdf')
					# sys.exit()
					try:
						
						text = self.nameLengthFix(  str(self.scriptTriggerField(name,item[name])) ,switches.value('Length'),'')
					except Exception as e:
						text = self.nameLengthFix(str(item[name]),switches.value('Length'),'')
				else:
					# sys.exit()
					try:
						text = str(self.scriptTriggerField(name,item[name]))
					except Exception as e:
						text = str(item[name])
						
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print('ran')
		field = field.lower()
		i = 0
		value = ''
		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1
		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader
		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print(rows)

		columnList = column
		value = self.triggerExecute(column,str(rows[i][column]))
		# value = rows[i][column]
		# print(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if switches.isActive('Long') == True:
			shorten = False
			if switches.isActive('ShortenColumn') == True:
				shortenColumn = switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = switches.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							print(self.groupLine(columnList,columnHeaderLength))
							for g in groupBy.split(','):
								groupByList[g] = ''
						else:
							print('')
						groupByList[gb] = text
					else:
						pass
						text = ''
		alignment = self.fieldProfileGet(column,'alignment')
		# print(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print(column,theLeft,theRight,'0' + result + '0')
			# print(totalSpace,theLeft,theRight)
		#   result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ''
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',True)
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'right'


			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		result += '\n'
		return result

	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower() == column.lower():
				return k

	def print(self,column,fieldLengths=False):
		self.groupByTrigger()
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print(column)
		# print(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()
		global errors
		global switches
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			try:
				column += self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column += cs + ','
				# print( 'Error: print column', cs )
				# sys.exit()
			# print(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								if len(str(dpi[dpic])) > 1:
									hasData = True
								y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print(newData)
			# print('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print('IS')
								# print(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if switches.isActive('PlusOr') == True:
										#   if cnt > 0:
										#       rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(ci(s)) == -1:
												cnt += 1
											# if not string.find(ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print(self.asset)



		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()



		# if not len(groupByList):
		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		# if not column == False:
			# switches.fieldSet('Column','value',column)
			# column = switches.value('Column')
		if switches.isActive('Sort') == True:
			self.asset = self.sort()
		elif switches.isActive('GroupBy') == True:
			
			switches.fieldSet('Sort','active',True)
			switches.fieldSet('Sort','value',switches.value('GroupBy'))
			self.asset = self.sort()
		# print('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		# print(columnHeader)
		printBold(columnHeader)
		i = 0
		# print(self.asset)
		for item in self.asset:
			# print(item)
			result = '' 
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print(result)
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					print(12)
					print(c)
					print(12)
					os._exit(0)
			# print(_str.totalStrip5(result)) #TESTING
			if len(result) > 0:
				# print(result)
				colorizeRow(result)
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:

				print('')
		if len(oldData) > 0:
			self.asset = oldData
	def sort(self,fields=''):# sortThis
		rows = self.asset
		global errors
		global switches
		# self.sort = name
		tempFields = []
		delim = '.'
		if fields == '':
			name = switches.value('Sort')
		else:
			name = fields
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})


		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = self.findColumName(item.split(delim)[1])
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				

			sortBy[item] = str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		if len( tempFields ):
			# print( tempFields )
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True):
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0 = _v.stmp + _v.slash + theFile
		dataDump = json.dumps(self.asset, indent=4, sort_keys=True)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		if printThis:
			print('Saved: ' + file0)
	def get(self,theFile = '',tableTemp = True,printThis = False):
		if theFile == '':
			theFile = self.file
		self.file = theFile
		# defaults to myTables
		if tableTemp == True:
			file0 = _v.myTables + _v.slash + theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
		if printThis:
			print('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = json.load(json_file)
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

	def groupByTrigger( self ):
		try:
			if switches.isActive('GroupBy') and len(self.asset):
				newValues = []
				keys = []
				for key in self.asset[0].keys():
					keys.append( key )
				for val in switches.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower() == val.lower():
							newValues.append( key )
				if len(newValues):
					switches.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass



class Tables:

	def __init__(self):
		self.tables = []

		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'



	def register(self,name,asset = []):
		found = False
		thisID = False
		for i,t in enumerate(self.tables):
			if t.name == name:
				found = True
				self.tables[i].maxNameLength = self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if not found:
			self.tables.append(Table(name,asset))
			self.tables[ len( self.tables )-1 ].maxNameLength = self.maxNameLength

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False):
		# print(name,fields)
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					self.tables[i].print(fields,fieldLengths)
				else:
					print('Table Blank')
			i += 1

	def sort(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def returnSorted(self,name,fields,asset = []):
		if len(asset) > 0:
			self.register(name,asset)

		result = []
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
				result = self.tables[i].asset
			i += 1
		return result
	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#   if spaces > totalColumnWidth:
		#       totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		# for m in self.meta['data']:
		#   genLine(totalColumnWidth,'=')
		#   print('Table:\t',m['table'])
		#   print('Parent:\t',m['parent'])
		#   print('Records:',m['count'])
		#   print()
		#   tables.register(m['table'],m['fields'])
		#   tables.fieldProfileSet(m['table'],'*','alignment','center')
		#   tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#   genLine(totalColumnWidth,'=')
		# print()
		# print('Records:',self.meta['records'])
		# print()
		# print('Errors:')
		# for e in self.meta['errors']:
		#   print('\t',e)

		return result

###########################################################################################

def formatSize(size):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#   result = ''
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776  
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	result = round(size * factor,0)
	return result

def timeAgo(do=''):
	if len(do) == 0:
		do = switches.value('Ago')
	do = do.lower()

	if 't' in do :
		one = resolveEpochTest( time.time() )
		two = autoDate( one.split(' ')[0] )
		return two

	if 'mm' in do :
		each = 60
		units = do
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return time.time() - remove  

	if 'h' in do :
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return time.time() - remove  


	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1
	if 'y' in do:
		start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
	if 'm' in do:
		start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
	if 'w' in do:
		start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
	if 'd' in do:
		start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
	dT = str(start_date)
	# print(dT)
	# print(dT)
	# print(dT)
	# print(dT)
	d = dT.split('-')
	result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# print(start_date)
	# print(result)]
	# print(result)
	return result

###########################################################################################
###########################################################################################


###########################################################################################
###########################################################################################



###########################################################################################
def get_size(obj, seen=None):
	# https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524
	# From https://goshippo.com/blog/measure-real-size-any-python-object/
	# Recursively finds size of objects
	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0


###########################################################################################
def genLine(count,what):
	count = int(count)
	what = str(what)
	cnt = 0
	result = ''
	while cnt < count:
		result += what
		cnt += 1
	print(result)
	return result


def ci(string): 
	#switchValueClean
	global ciData
	# print( ciData )
	# sys.exit()
	for cx in ciData:
		if cx[0] in string:
			# print( 'HERE', cx )
			string = string.replace( cx[0], cx[1] )
	
	string = string.replace( ';d;', __.theDelim )
	string = string.replace( ';delim;', __.theDelim )
	string = string.replace( ';thedelim;', __.theDelim )
	string = string.replace( ';theDelim;', __.theDelim )



	return string



def formatColumns(columns):
	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a == c:
						c = col['name']
			if hasPre:
				c = preData + '.' + c
			result += c + ','
		result = result[:-1]
	return result

def defaultScriptTriggers():
	if len(appInfo[__.appReg]['columns']) > 0:
		switches.trigger('Column',formatColumns)
		switches.trigger('Sort',formatColumns)
		switches.trigger('GroupBy',formatColumns)

printAutoAbbreviations_scheduled = False
def autoAbbreviations():
	global printAutoAbbreviations_scheduled
	# return False
	global myFileLocation_File
	if not type( myFileLocation_File ) == bool:
		if not len( appInfo[__.appReg]['columns'] ) and myFileLocation_File.lower().endswith('.json'):
			
			printAutoAbbreviations_scheduled = True
			data = []
			groups = {}
			myFileLocation_File_Data = getTable2( myFileLocation_File )
			if type( myFileLocation_File_Data ) == dict:
				myFileLocation_File_Data = [myFileLocation_File_Data]
			for i,key in enumerate( myFileLocation_File_Data[0].keys()):
				# print( key )
				record = {}
				record['id'] = i
				record['key'] = key
				record['first'] = key[:1].lower()
				record['second'] = key[:2].lower()
				record['third'] = key[:3].lower()
				wf = ''
				for w in key.replace( '_', ' ' ).split( ' ' ):
					wf += w[:1].lower()
				record['firstofword'] = wf


				for k in record.keys():
					try:
						if not type(groups[ k ]) == dict:
							groups[ k ] = {}
					except Exception as e:
						groups[ k ] = {}

					try:
						if not type(groups[ k ][ record[k] ]) == dict:
							groups[ k ][ record[k] ] = {}
					except Exception as e:
						groups[ k ][ record[k] ] = {}
						groups[ k ][ record[k] ]['ids'] = []


				for k in record.keys():
					groups[ k ][ record[k] ]['ids'].append( i )
				
				data.append( record )


			approvedAbbreviations= []
			flag = False
			flagged= []

			for k in groups['first'].keys():
				approvedAbbreviations.append({ 'key': data[groups['first'][k]['ids'][0]]['key'], 'abbreviations': k })
				if not len(groups['first'][k]['ids']) == 1:
					flag = True
					for i,idx in enumerate(groups['first'][k]['ids']):
						if not i == 0:
							flagged.append({ 'first': k, 'id': idx, 'assigned': False })

			
			if flag:
				flagsResolved = 0
				for k in groups['firstofword'].keys():
					if len(k) > 1:
						for x in groups['firstofword'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['second'].keys():
						for x in groups['second'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })

				if not flagsResolved == len(flagged):
					for k in groups['third'].keys():
						for x in groups['third'][k]['ids']:
							for i,f in enumerate(flagged):
								if not flagged[i]['assigned']:
									if flagged[i]['id'] == x:
										flagsResolved += 1
										flagged[i]['assigned'] = True
										approvedAbbreviations.append({ 'key': data[x]['key'], 'abbreviations': k })         

				if not flagsResolved == len(flagged):
					for i,f in enumerate(flagged):
						if not flagged[i]['assigned']:
							print( 'Error: abbreviation', data[flagged[i]['id']]['key'] )


			# printVar( groups )
			# printVar( data )

			for aa in approvedAbbreviations:
				appInfo[__.appReg]['columns'].append({'name': aa['key'], 'abbreviation': aa['abbreviations']})
			if switches.isActive('PrintAutoAbbreviations'):
				print()
				print('Columns and abbreviations:')
				result = ''
				for col in appInfo[__.appReg]['columns']:
					result += col['name'] + '(' + col['abbreviation'] + '), '
				result = result[:-2]
				print('\t' + result + '\n')
				print()

			defaultScriptTriggers()
			# sys.exit()
			# print(first)


def printAutoAbbreviations():
	global printAutoAbbreviations_scheduled
	if printAutoAbbreviations_scheduled and switches.isActive('PrintAutoAbbreviations'):
		print()
		print('Columns and abbreviations:')
		result = ''
		for col in appInfo[__.appReg]['columns']:
			result += col['name'] + '(' + col['abbreviation'] + '), '
		result = result[:-2]
		print('\t' + result + '\n')
		print()



#########################################################################################################################################################



#########################################################################################################################################################


###################################################################################################################

###################################################################################################################

def isText( data ):
	if type( data ) == str:

		return True
	else:
		return False

def isNum( data ):
	if type( data ) == int:
		return True
	else:
		return False

def isFloat( data ):
	if type( data ) == float:
		return True
	else:
		return False

###################################################################################################################


class Field:

	def __init__( self, project, name, value, appReg, script, maxField ):
		self.appReg = appReg
		self.project = project
		self.name = name
		self.trigger = script
		self.maxField = maxField



		self.registerValue( value )

	def setTrigger( self, script ):
		self.trigger = script

	def addPadding( self, value, extra ):
		value = self.runTrigger( str(value) )
		addPadding = (extra + self.maxField) - len( value )
		while not len(value) == self.maxField+extra:
			value += ' '
		# for x in range(1,addPadding+1):
		#   value += ' '
		# return str(self.maxField)+' '+str(len( value ))+value
		return value

	def addPaddingZeros( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += '0'
			newValue = Zeros + value
		return newValue

	def runTrigger( self, value ):
		if type( self.trigger ) == bool:
			return value

		# print( 'HERE' )
		return self.trigger( value )

	def registerValue( self, value ):
		thisLen = len( self.runTrigger( str(value) ) )

		if thisLen > self.maxField:
			self.maxField = thisLen



class Fields:

	def __init__(self):
		self.fields = []
		self.extra = 0

	def register( self, project='', names='', value='', appReg=False, script=False, maxField=None,        p=None, n=None, v=None, m=None ):



		if not p is None:
			project = p

		if not n is None:
			names = n

		if not v is None:
			value = v

		maxField = 0

		if not maxField is None:
			maxField = maxField
			
		if not m is None:
			maxField = m


		if type(appReg) == bool:
			appReg = __.appReg

		for name in names.split(','):

			shouldAdd = True
			for i,s in enumerate(self.fields):
				if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
					shouldAdd = False
			if shouldAdd:
				self.fields.append( Field( project, name, value, appReg, script, maxField ) )
				if maxField and type(value) == int:
					return self.fields[len(self.fields)-1].addPaddingZeros(value)
				elif maxField and type(value) == str:
					return self.fields[len(self.fields)-1].addPadding(value)
			else:
				self.registerValue( project, name, value, appReg )

	def registerValue( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		
		result = False
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				self.fields[i].registerValue( value )
				result = True
		return result


	def padZeros( self, project, name, value, extra=None, appReg=False ):

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				return self.fields[i].addPaddingZeros( value )
				result = self.fields[i].addPaddingZeros( value )
		return result


	def value( self, project, name, value, extra=None, appReg=False ):

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				result = self.fields[i].addPadding( value, extra )
		return result
	def valuez( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields):
			if self.fields[i].appReg == appReg and project == self.fields[i].project and name == self.fields[i].name:
				result = self.fields[i].addPaddingZeros( value )
		return result

	def asset( self, project, asset, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		if type( asset ) == dict:
			self.registerDic( project, asset, appReg )

		if type( asset ) == list:
			for row in asset:
				if type( row ) == dict:
					self.registerDic( project, row, appReg )


	def registerDic( self, project, asset, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg

		for name in asset.keys():
			self.register( project, name, asset[name], appReg )

# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

###################################################################################################################



thisTest = 'hello'



errors = []
appInfo = {}
appData = {}

argvProcess = True

fields = Fields()

switches = Switches()
tables = Tables()


def appInfoDump():
	global appInfo
	for k in appInfo.keys():
		print()
		print(k,appInfo[k])



def appInfoDump2():
	global appInfo
	for k in appInfo.keys():
		print()
		print(k,appInfo[k])



# def appInfoDump2():
#   global appInfo
#   for k in appInfo.keys():
#       print(k,appInfo[k]['columns'])


def load():
	global switches
	global switchDefault
	# global tables
	switches.register('Help', '?,/?,-?,/h,/help,-help,--help')
	# switches.register('Column', '-c,-column', 'size, name')
	# switches.register('Sort','-s,-sort', 'Asc:type, Desc:ext')
	switches.register('Debug', '-d,-debug')
	# switches.register('Errors', '-e,-Error,-Errors', '8,11 OR hide:8,11')
	# switches.register('Timeout', '-t,-Timeout')
	# switches.register('GroupBy', '-g,-group,-groupby', 'ext, month')
	switches.register('Long', '-l,-long')
	switches.register('Short', '-sc,-short')
	switches.register('Length', '-length','x3')
	# switches.register('Report', '-report')
	switches.register('Plus', '+')
	switches.register('Minus', '-')
	switches.register('PlusOr', '-or')
	switches.register('PlusClose', '+close')
	# switches.register('PrintAutoAbbreviations', ',-printa,-aprint')
	# switches.register('LoadEpoch', '-loadepoch')
	# switches.register('NoColor', '-nocolor')
	switchDefault = switches.length()



###############################################
####### imported into functions as needed
	# math
	# calendar
	# re
	# np
	# random

####### deleted
# glob
# subprocess
# join
# getsize
# splitext
# rrule
# ast
# OrderedDict
###############################################

### NOTES ###
	# types of timestamps:
	#                       1522705321.1137724      file create, modification
	#                       1517338060740           int(round(time.time() * 1000))
	


# _.regImps( focus(), 'app' )
# _.regImps[focus()]['app']

# class Threads
# class Queue
# def add(
# def printReport(
# def checkTimeout(
# def audit

# class regImp:


# 2B-C3P0-AF i: {id} 
# 2B-R2D2-AF
# r: {relatedid}

{ '2B100AF': 0, 'id': 0, 'genfrom': 0,  'created': 1558456773.7885933 }

############################################### ###############################################

ciData = (  [ ';;',         ',' ],
			[ ';c',         ',' ],
			[ '_;192A;_',   ',' ],
			
			[ ';_',         '-' ],
			[ ';-',         '-' ],

			[ ';p',         '%' ],
			[ ';p;',        '%' ],
			[ ';.',         ':' ],
			[ '_;192B;_',   ':' ],
			[ ";;'",        _v.slash+'"' ],

			[ _v.slash+'n',        '\n' ],
			[ ';n',         '\n' ],
			[ ';return',    '\n' ],
			[ ';t',         '\t' ],

			[ ";'",         '"' ],
			[ ';q;',        '"' ],
			[ '"\'"',       "'" ],
			[ 'null00',     '"",' ],
			[ '"\'", "\'"', "','" ],

			[ '[star]',     '*' ],
			[ '[a]',        '*' ],
			[ '[eq]',       '=' ],
			[ ';opar;',     '[' ],
			[ '[pipe]',     '|' ],
			[ '[htmlopen]', '<' ],
			[ '[htmlclose]','>' ],
			[ '[gtr]',      '>' ],
			[ '[lss]',      '<' ],
			[ ';6',         '^' ],
			[ ';+',         '+' ],

			[ '+--+c',          '--c' ],

			[ '[semi]',         ';' ],
			
			[ '[caret]',    '^' ]  )

############################################### ###############################################

# testlist = [1, 2, 3, 5, 3, 1, 2, 1, 6]
# test = [i for i,x in enumerate(testlist) if x == 1]



# _.fields.register( 'project', 'name', script=_.resolveEpochTest )
# _.fields.asset( 'project', {} )
# _.fields.asset( 'project', [{}] )
# _.fields.register( 'project', 'name', value, appReg=focus() )
# _.fields.register( 'project', 'name', value )
# _.fields.value( 'project', 'name', value )

# fields = Fields()





