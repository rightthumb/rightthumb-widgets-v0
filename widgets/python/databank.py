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
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register( 'New', '-new' )
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Download', '-download' )
	_.switches.register( 'Tables', '-t,-table,-tables' )
	_.switches.register( 'Pause', '-pause' )
	_.switches.register( 'JustReturn', '-return' )
	_.switches.register( 'Edit', '-edit' )


	_.switches.register( 'isFileExt', '-isext' )

	_.switches.register( 'Manual_Index', '-index', 'D:\\tech\\programs\\databank\\indexes\\queries\\FILE-EXTENS\\label.index' )
	_.switches.register( 'File', '-file', '%tmpf0%' )

	_.switches.register( 'Clean', '-clean', 'image.index' )
	_.switches.register( 'Subject', '-subject', 'graphic.index' )

	_.switches.register( 'Combine_Indexes', '-combine', ' image.index  images.index ' )


	
_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['New','Save']

_.appInfo[focus()] = {
	'file': 'databank.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Structure, index, prep, and query databases acquired from internet',
	'categories': [
						'database',
						'databank',
						'db',
						'data',
						'query',
						'search',
						'index',
						'structure',
						'acquired',
						'internet',
						'import',
						'resource',
						'asset',
						'assets',
						'store',
						'stockpile',
						'goods',
						'riches',
						'equity',
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
						'p databank -download',
						'',
						'p databank -tables file extensions + audio',
						'',
						'p databank -tables file extensions + audio -edit',
						'',
						'p databank -subject graphic.index -clean image.index images.index',
						'',
						'p databank  -file %tmpf4%  -isext   -index db.index',
						'',
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
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
	
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
# __.appRegPipe
########################################################################################
# START



def cleanChars( data, chars=None, startwith=None ):

	data = _str.replaceDuplicate( data, ' ' )
	data = _str.cleanBE( data, ' ' )

	if not startwith is None:
		if not data.startswith(startwith):
			data = startwith + data
		data = _str.replaceDuplicate( data, startwith )

	if chars is None:
		return data
	results = ''
	for x in data:
		if x in chars:
			results += x
	return results



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


		# cache = __.app.get({ 'algorithm': ['DataBank'], 'usage': 'return/app', 'tags': table_tag, 'search': search_tags  })
		# if not cache is None:
		#     return cache



		if not type(table_tags) == list:
			table_tags = table_tags.split(',')
		if not type(search_tags) == list:
			search_tags = search_tags.split(',')

		self.table_tags = table_tags
		self.search_tags = search_tags
		self.subject_trigger = subject_trigger
		self.description_trigger = description_trigger
		self.pathIndexDatabases = _v.databank+_v.slash+'indexes'+_v.slash+'databases'
		self.pathIndexStems = _v.databank+_v.slash+'indexes'+_v.slash+'tag_stems'

		self.table_tag_stems = []
		for tag in self.table_tags:
			self.table_tag_stems.append( wordStem(tag) )

		self.search_tag_stems = []
		for tag in self.search_tags:
			self.search_tag_stems.append( wordStem(tag) )

		self.indexFilesNames = os.listdir(  self.pathIndexDatabases  )
		self.records = []



		for files in self.indexFilesNames:

			# _.pr( self.pathIndexDatabases+_v.slash+files )
			index = _.getTable2( self.pathIndexDatabases+_v.slash+files )


			cnt = 0
			tags = index['tag_stems']
			for search in self.table_tag_stems:
				if search in tags:
					cnt+=1
			# _.pr( 'test:', cnt, len(self.table_tag_stems) )
			if cnt == len(self.table_tag_stems):

				_.pr(index['tags'])

				chars = None
				startwith = None
				
				global formatProfile
				stem_profile = None
				for sKey in formatProfile.keys():
					good = True
					for x in sKey.split('_'):
						if not x in index['tag_stems']:
							good = True
					if good:
						stem_profile = formatProfile[sKey]

				if not stem_profile is None:
					delim = _.genUUID()
					if 'chars' in stem_profile.keys():
						chars = stem_profile['chars']
					if 'startswith' in stem_profile.keys():
						startwith = stem_profile['startswith']


				self.search_tag_stems.sort()
				if '_'.join(self.search_tag_stems) in list(index['stem_index']):
					# _.pr( 'in index' )
					for i in index['stem_index'][  '_'.join(self.search_tag_stems)  ]:
						data = index['records'][i]['data']
						if not self.subject_trigger is None:
							data = self.subject_trigger(data)
						# self.records.append(data)

						if stem_profile is None:
							self.records.append(data)
						else:

							if 'case' in stem_profile.keys() and stem_profile['case'] == 'lower':
								data = data.lower()
							if 'case' in stem_profile.keys() and stem_profile['case'] == 'upper':
								data = data.upper()
							if 'split' in stem_profile.keys():
								for x in stem_profile['split']:
									data = data.replace( x, delim )

								data = _str.replaceDuplicate( data, delim )
								data = _str.cleanBE( data, delim )

								for xx in data.split(delim):
									if not 'lengths' in stem_profile.keys():
										self.records.append(cleanChars(xx,chars,startwith))
									else:
										if len(xx) in stem_profile['lengths']:
											self.records.append(cleanChars(xx,chars,startwith))
							elif not 'split' in stem_profile.keys():
								self.records.append(cleanChars(data,chars,startwith))
							


					# _.pr( len(self.records) )
				else:

					records = []

					# _.pr( 'found table' )

				
					tables = []
					for i,table in enumerate(index['tables']):
						# _.pr( table['indexes'].keys() )
						cnt = 0
						stems = list(  table['indexes']['stems'].keys()  )
						for search in self.search_tag_stems:
							if search in stems:
								cnt+=1
						if cnt == len(self.search_tag_stems):
							tables.append(table['tableID'])
							# _.pr(table['tableID'])
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
					_.pr( len(records) )

					self.search_tag_stems.sort()
					index['stem_index'][  '_'.join(self.search_tag_stems)  ] = records
					_.saveTable2(  index,  self.pathIndexDatabases+_v.slash+files  )
					for i in records:
						data = index['records'][i]['data']
						if not self.subject_trigger is None:
							data = self.subject_trigger(data)
						if stem_profile is None:
							self.records.append(data)
						else:

							if 'case' in stem_profile.keys() and stem_profile['case'] == 'lower':
								data = data.lower()
							if 'case' in stem_profile.keys() and stem_profile['case'] == 'upper':
								data = data.upper()
							if 'split' in stem_profile.keys():
								for x in stem_profile['split']:
									data = data.replace( x, delim )

								data = _str.replaceDuplicate( data, delim )
								data = _str.cleanBE( data, delim )

								for xx in data.split(delim):
									if not 'lengths' in stem_profile.keys():
										self.records.append(cleanChars(xx,chars,startwith))
									else:
										if len(xx) in stem_profile['lengths']:
											self.records.append(cleanChars(xx,chars,startwith))


							elif not 'split' in stem_profile.keys():
								self.records.append(cleanChars(data,chars,startwith))



# {
#     'case': 'lower',
#     '': ',(/&'+_v.slash,
#     'chars': '.-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
#     'startswith': '.',
#     'lengths': [3,4],
# },



	def data( self ):
		return list(set(self.records))
		# return __.app.save( data, { 'algorithm': ['DataBank'], 'usage': 'return/app', 'tags': table_tag, 'search': search_tags  } )
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



processWordStem = None
def wordStem(word):
	global processWordStem
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	return processWordStem.stem(word)



from operator import itemgetter
from lxml import html
import requests
# import webbrowser
# import datetime
# import arrow
# import pickle

_textIndex = _.regImp( __.appReg, 'words' )
_textIndex.switch( 'Alpha' )
_textIndex.switch( 'Unique' )
_textIndex.switch( 'MinLength', 2 )
_textIndex.switch( 'Stemming' )
_textIndex.switch( 'PartsOfSpeech' )
_textIndex.switch( 'Clean' )

def build_Tag_Path_Stems( theList, cacheTables=None ):
	global ps
	added = False
	tag_stem_index_file = _v.databank + _v.slash+'indexes'+_v.slash+'tag_stem_indexes.index'
	tag_stem_index = _.getTable2( tag_stem_index_file )
	result = []
	for tag in theList:
		tag = tag.upper()
		tag = _str.stripNonAlphaNumaric(tag)
		if tag in tag_stem_index.keys():
			result.append( tag_stem_index[tag] )
		else:
			if ps is None:
				import nltk
				from nltk.stem import PorterStemmer
				from nltk.tokenize import word_tokenize
				ps = PorterStemmer()
			pass
			added = True
			ps_stem_x = ps.stem(tag)
			# ps_stem_x = ps_stem_x.upper()
			tag_stem_index[ tag ] = ps_stem_x
			result.append( ps_stem_x )


	if not cacheTables is None:
		for queryTables in cacheTables:
			tableMatch = 0
			tbls = []
			for tbl in queryTables:
				if tbl.lower() in result:
					tableMatch += 1

			if tableMatch == len(queryTables):
				import shutil
				qtx = _v.databank+_v.slash+'indexes'+_v.slash+'queries'+_v.slash+ '-'.join(queryTables)
				if os.path.isdir( qtx ):
					shutil.rmtree(qtx)


	if added:
		_.saveTable2( tag_stem_index, tag_stem_index_file )

	return result



def process( file ):
	global keyOmit
	global cacheTables
	recordID = file.split('__')[0]
	page = requests.get( __.url + file )
	_.saveText( page.content , _v.myTables + _v.slash+'researchData-subject.json' )

	record = _.getTable( 'researchData-subject.json' )
	try:
		_.colorThis(  [ '\t', record['settings']['settings']['label'] ], 'cyan'  )
	except Exception as e:
		_.pr( record['settings']['settings'].keys() )
		sys.exit()
	_.colorThis(  [ '\t\t', record['settings']['settings']['tag_path'] ], 'blue'  )
	
	try:
		dl = _.colorThis(  [ '\t\t\t', record['data']['label'] ], 'cyan', p=0  )
		dl += _.colorThis(  [ 'tables:' ], 'bold', p=0  )
	except Exception as e:
		pass
	for i,dRec in enumerate(record['data']['data']):
		tbl = dRec['label']
		for ko in keyOmit:
			if ko in tbl:
				needsKeyClean = True
			tbl = tbl.replace(ko,'')
		record['data']['data'][i]['label'] = tbl
	try:
		for dRec in record['data']['data']:
			tbl = dRec['label']
			_.colorThis(  [ '\t\t\t\t-', tbl ], 'cyan'  )

	except Exception as e:
		pass
		_.colorThis(  [ 'checkout around line 206 to fix table labels' ], 'red'  )
		# _.printTest(record)



	# pause=input(': ')
	# _.printTest(record)

	if cacheTables is None:
		cacheTables = []
		for fxy in os.listdir( _v.databank+_v.slash+'indexes'+_v.slash+'queries' ):
			if os.path.isdir( _v.databank+_v.slash+'indexes'+_v.slash+'queries'+_v.slash+fxy ):
				rec = []
				for fxyz in fxy.split('-'):
					rec.append( fxyz )
				cacheTables.append( rec )
				



	tags = _str.stripNonAlphaNumaric( record['settings']['settings']['tag_path'] )
	tag_stems = build_Tag_Path_Stems( tags.split(' '), cacheTables )
	global ps

	indexes = {
					'recordID': recordID,
					'id': _.genSerial( 'databank' ),
					'tags': record['settings']['settings']['tag_path'],
					'tag_stems': tag_stems,
					'path': thePath( record['settings']['settings']['tag_path'] )+_v.slash+recordID+'.json',
					'subject': record['settings']['settings']['subject'],
					'description': record['settings']['settings']['description'],
					'database': {},
					'tables': [],
					'records': [],
					'stem_index': {},
	}


	# indexes['records']



	if type( record ) == dict:
		pass

	else:
		_.colorThis( [ 'Error:', 'record blank' ], 'red' )

	if False:
		_textIndex.pipe( str(page.content).split('\n') )
		indexes['database'] = _textIndex.do( 'action' )
		_.pr()
		_.pr()
		_.pr( 'Percentage: > 2' )
		for k in indexes['database']['percentage'].keys():
			if indexes['database']['percentage'][k] > 2:
				_.pr( k, indexes['database']['percentage'][k] )
		_.printVar1( indexes['database'] )
		# sys.exit()



	# _.printVar1( record )

	isTraditional = False
	if len( record['data']['data'][0].keys() ) == 2 and  'label' in record['data']['data'][0].keys() and 'records' in record['data']['data'][0].keys():
		isTraditional = True
		# _.pr( 'isTraditional' )
		# _.pr( record['data']['data'][0]['records'][0].keys() )
		if not len(record['settings']['settings']['description']) and (  'description' in record['data']['data'][0]['records'][0].keys()  or 'Description' in record['data']['data'][0]['records'][0].keys()  or 'DESCRIPTION' in record['data']['data'][0]['records'][0].keys() ):
			
			record['settings']['settings']['description'] = 'description'

			if 'Description' in record['data']['data'][0]['records'][0].keys():
				record['settings']['settings']['description'] = 'Description'

			if 'DESCRIPTION' in record['data']['data'][0]['records'][0].keys():
				record['settings']['settings']['description'] = 'DESCRIPTION'

			if len(record['data']['data'][0]['records'][0].keys()) == 2:
				thisKey = list(record['data']['data'][0]['records'][0].keys())
				if not thisKey[0] == 'description':
					record['settings']['settings']['subject'] = thisKey[0]
				elif not thisKey[1] == 'description':
					record['settings']['settings']['subject'] = thisKey[1]
		if not len(record['settings']['settings']['subject']):
			record['settings']['settings']['subject'] = thisKey[0]



	if not isTraditional:
		_.pr()
		_.pr( '! isTraditional' )
		_.pr()
		for k in record['data']['data'][0].keys():
			_.pr( k )



	record['settings']['settings']['description'] = record['settings']['settings']['description'].split(',')
	record['settings']['isTraditional'] = isTraditional

	# _.printTest( record['settings'] )
	if isTraditional:
		for it, table in enumerate(record['data']['data']):
			_textIndex.pipe( [table['label']] )
			indexes['tables'].append({ 'tableID': it, 'data': table['label'], 'indexes': _textIndex.do( 'action' ) })

			for ir, rec in enumerate(table['records']):
				description = ''
				if len(record['settings']['settings']['description']):
					for d in record['settings']['settings']['description']:

						description_title_method = 3
						try:
							if d.title() in rec.keys():
								description_title_method = 2
						except Exception as e:
							if d in rec.keys():
								description_title_method = 1
						
						pass
						if description_title_method == 1:
							try:
								description += rec[d] + ' '
							except Exception as e:
								
								try:
									description += rec[d.title()] + ' '
								except Exception as e:
									_.colorThis( [ 'Error: record description title', d ] , 'red' )
									_.printVarSimple(rec)
									sys.exit()

						elif description_title_method == 2:
							description += rec[d.title()] + ' '

						elif description_title_method == 3:
							if len( list(rec.keys()) ) > 1:
								description = rec[  list(rec.keys())[1]  ]
							else:
								description = rec[  list(rec.keys())[0]  ]


				if len(description) or len(rec[  record['settings']['settings']['subject']  ]):
					try:
						_textIndex.pipe( [   rec[  record['settings']['settings']['subject']  ]  +' '+  description ] )
					except Exception as e:
						_textIndex.pipe( [   rec[  list(rec.keys())[0]  ]  +' '+  description ] )
					dex = _textIndex.do( 'action' )
				else:
					dex = None
				try:
					indexes['records'].append({ 'tableID': it, 'recordID': ir, 'data': rec[  record['settings']['settings']['subject']  ], 'record': rec, 'indexes': dex })
				except Exception as e:
					indexes['records'].append({ 'tableID': it, 'recordID': ir, 'data': rec[  list(rec.keys())[0]  ], 'record': rec, 'indexes': dex })


		pass
		# _.pr( indexes )
		# sys.exit()
		# _.printTest( indexes )
		_.saveTable2( indexes, _v.data+_v.slash+'indexes'+_v.slash+'databases'+_v.slash+recordID+'.json' )
		_.saveTable2( record, indexes['path'] )


		################################################################################## ##################################################################################
		global delete_after_download
		
		if delete_after_download:
			requests.get( __.url +  'delete.php?record='+recordID )



	# for k in indexes['database']['count'].keys():
	#   if indexes['database']['count'][k] > 5:
	#       _.pr( k, indexes['database']['count'][k], _.percentageDiffInt( indexes['database']['count'][k], indexes['database']['cnt_words'] ) )


	# sys.exit()



def thePath( data ):

	import nltk
	from nltk.stem import PorterStemmer
	from nltk.tokenize import word_tokenize
	ps = PorterStemmer()

	tp = _str.stripNonAlphaNumaric( data ).split(' ')

	newPath = _v.data + _v.slash+'vault'
	for fdr in tp:
		newPath += _v.slash + ps.stem(fdr).upper()
		if not os.path.isdir( newPath ):
			os.mkdir(newPath)
	return newPath

def action():
	if _.switches.isActive('Clean') and _.switches.isActive('Subject'):

		# fileBackup = _.regImp( focus(), 'fileBackup' )
		fileBackup = _.regImp( __.appReg, 'fileBackup' )
		fileBackup.switch( 'Silent' )
		fileBackup.switch( 'Flag', 'imdb' )
		fileBackup.switch( 'isRunOnce' )
		fileBackup.switch( 'DoNotSchedule' )



		subject = _.getTable2(  _.switches.values('Subject')[0]  )

		for filepath in _.switches.values('Clean'):

			fileBackup.switch( 'Input', filepath )
			bk = fileBackup.do( 'action' )
			_.pr( 'backup:', filepath, bk )

			index = []
			for ix in _.getTable2(  filepath  ):
				if not ix in subject and not ix in index:
					index.append( ix )
			_.saveTable2( index, filepath )

		sys.exit()



	if _.switches.isActive('File') and _.switches.isActive('Manual_Index'):
		def manual_clean( data ):
			if not _.switches.isActive('isFileExt'):
				return data
			data = data.replace(' ','')
			data = data.replace('.','')
			data = data.lower()
			return '.'+data

		index = []
		for filepath in _.switches.values('File'):
			manual = _.getText(  filepath, raw=True  )
			if manual.startswith('['):
				for x in eval(manual):
					y = manual_clean(x)
					if not y in index and len(y):
						index.append(  y  )
			else:
				for x in manual.split('\n'):
					y = manual_clean(x)
					if not y in index and len(y):
						index.append(  y  )

		_.saveTable2( index, _.switches.values('Manual_Index')[0] )
		sys.exit()



	if _.switches.isActive('Download'):

		page = requests.get( __.url +  'toProcess.php')
		_.saveText( page.content , _v.myTables + _v.slash+'researchData-toProcess.json' )
		toProcess = _.getTable( 'researchData-toProcess.json' )
		_.colorThis(  [ '\n',len(toProcess), 'assets acquired' ], 'green'  )
		# toProcess.reverse()
		for i,rec in enumerate(toProcess):
			_.colorThis(  [ '\nProcess:', i ], 'yellow'  )
			process( rec['record'] )
			
		
		# _.saveText( page.content, _v.databank+_v.slash+'temp'+_v.slash+'acquired.json' )
		# if _.switches.isActive('Pause'):
		#   pause=input('pause')
		# records = _.getTable2(_v.databank+_v.slash+'temp'+_v.slash+'acquired.json')
		if False:
			records = eval(page.content)
			_.pr( type(records) )
			# _.pr( (records) )
			_.printVar1(records)

		_.colorThis(  [ '\nCompleted: structure, indexes, registration, and schedules' ], 'green'  )
		sys.exit()
	# if _.switches.isActive('New'):

	#   do = 'n ' + _v.myTables + _v.slash+'researchData-TEMP.json'
	#   os.system( '"' + do + '"' )

	#   sys.exit()
	#   # _v.myTables

	# if _.switches.isActive('Save'):
	#   pass


	#   # sys.exit()



	# try:
	#   data = _.getTable( 'researchData-TEMP.json' )
	# except Exception as e:
	#   data = None

	# if data is None:
	#   do = 'n ' + _v.myTables + _v.slash+'researchData-TEMP.json'
	#   os.system( '"' + do + '"' )

	#   _.pr( 'Blank' )
	# else:
	#   _.printVar( data )

	# pass
	if _.switches.isActive('Tables'):
		tag_stem_index_file = _v.databank + _v.slash+'indexes'+_v.slash+'tag_stem_indexes.index'
		tag_stem_index = _.getTable2( tag_stem_index_file )
		tablesList = build_Tag_Path_Stems( _.switches.values('Tables') )


		tables = '-'.join( tablesList )
		plus   = '-'.join( _.switches.values('Plus') )
		minus = ''
		if _.switches.isActive('Minus'):
			minus   = '(--'+ '-'.join( _.switches.values('Plus') )+')'

		# tables = _str.stripNonAlphaNumaric(tables)
		plus = _str.stripNonAlphaNumaric(plus)
		
		queryFolder = _v.databank+_v.slash+'indexes'+_v.slash+'queries'+_v.slash+tables.upper()
		path = queryFolder+_v.slash+ plus +minus+ '.index'
		# filename  = 'databank_query_cache__' + tables + '_;;_' + plus + '__.json'
		# path = _v.databank+_v.slash+'query_cache'+_v.slash + filename

		if not os.path.isdir( queryFolder ):
			os.mkdir( queryFolder )


		if os.path.isfile(path):
			if _.switches.isActive('Edit'):
				# do = 'n ' + path
				os.system( 'n "' + path + '"' )
				sys.exit()
				# os.system( '"' + do + '"' )
			else:
				data = _.getTable2( path )
		else:
			bank = DataBank( t=_.switches.values('Tables'), s=_.switches.values('Plus'),  )
			data = bank.data()
			_.saveTable2( data, path )
		
		if not _.switches.isActive('JustReturn'):
			_.printVar1(data)

		return data

	# _.fields.register( 'cnt', 'val', 7, m=6 )
	# test = _.fields.padZeros( 'cnt', 'val', 5 )

	# _v.research
	# _v.data
__.url = 'http://www.rightthumb.com/projects/extension/aquire/'

keyOmit = [
				'[edit]',
]
# index['tag_stems']
formatProfile = {
					'file_extens': {
														'case': 'lower',
														'split': [',','(','/','&',_v.slash,' or '],
														'chars': '.-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
														'startswith': '.',
														'lengths': [3,4,5,6],
					},
}

cacheTables = None

ps = None

delete_after_download = False


# build_Tag_Path_Stems

########################################################################################
if __name__ == '__main__':
	action()