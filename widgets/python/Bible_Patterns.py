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
	_.switches.register( 'Index', '-index' )
	_.switches.register( 'FindPatterns', '-pat,-patterns' )
	_.switches.register( 'Verses', '-v,-verses' )
	_.switches.register( 'TEMP', '-tmp' )


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'Bible_Patterns.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Build index of every pattern in the Bible',
	'categories': [
						'Bible',
						'pattern',
						'research',
						'bible study',
						'study',
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
						'type b_av.txt | p Bible_Patterns -patterns',
						'type b_av.txt | p Bible_Patterns -index',
						'type b_av.txt | p Bible_Patterns',
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

def generatePatterns( string, patternLength ):
	spent = []
	def genP( by ):
		
		offset = 0
		dataset = []
		for offset in range(0,by):
			# _.pr( offset )
			ix = False
			for i,char in enumerate(string):
				if i >= offset:
					ix = ( i + offset )
					
				if not type(ix) == bool:
					# dataset.append( char )
					try:
						dataset.append( [string[ix],ix] )
					except Exception as e:
						pass
					if len(dataset) % by == 0:
						if len( dataset ):
							xSpent = str(dataset)
							if not xSpent in spent:
								spent.append(xSpent)
								data.append( dataset )
							# _.pr( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data



def newAbbreviations():
	global booksNew
	global booksRaw
	global sections

	for i,br in enumerate(booksRaw):
		br = br.replace('\n','').replace('.','')
		# _.pr( br )
		abbreviation = br.split(',')[1]
		n = {
				'book':        br.split(',')[0],
				'abbreviation':    br.split(',')[1],
				'minimal':    sections[str(i)]['abbreviation']
		}
		booksNew.append( n )


def getBook( book ):
	global booksNew

	for i,bn in enumerate(booksNew):
		if book == bn['book']:
			return bn['abbreviation']

def getBookByID( book ):
	global booksNew
	# _.pr( book )
	for i,bn in enumerate(booksNew):
		if int(book) == i+1:
			return bn['abbreviation']
	# _.pr( 'book' )


def action():

	if _.switches.isActive('TEMP'):

		data = _.getTable2( 'bible_patterns_min_3.json' )


		g = 0
		txt=''
		k=''
		gtr=0
		for key in data.keys():
			cnt = key.count('_')
			if cnt > 5 :
				gtr+=1
				_.pr()
				_.pr( cnt )
				_.pr( key )
				_.pr( txt )

			if cnt > g :
				g = cnt
				k = key
				txt = data[key]
		_.pr()
		_.pr()
		_.pr( g )
		_.pr( k )
		_.pr( txt )
		_.pr('gtr',gtr)

		sys.exit()

	load()
	global omit_words
	from nltk.stem import PorterStemmer
	from nltk.tokenize import word_tokenize
	
	ps = PorterStemmer() 
	if _.switches.isActive('Verses'):

		data = _.getTable2( 'bible_patterns_min_3.json' )

		verses = {}
		for key in data.keys():
			for rec in data[key]:
				try:
					verses[ rec['verse'] ].append( key+'-'+str( len(data[key]) ) )
				except Exception as e:
					verses[ rec['verse'] ] = []
					verses[ rec['verse'] ].append( key+'-'+str( len(data[key]) ) )
		pass
		_.saveTable2( verses, 'bible_patterns_verses.json' )



	if _.switches.isActive('Index'):
		global pattern_index
		global booksRaw
		global booksNew
		global sections



		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner(0)
			# _.printVar( _.appData )
			for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
				pass

				# _.pr( row )
				# sys.exit()
				row = row.replace( '\t', '  ' )
				row = _str.replaceDuplicate(row,'  ')
				verse = row.split('  ')
				try:
					vID = verse[0]
					vB = verse[1]
					vCh = verse[2]
					vV = verse[3]
					vV = _str.cleanBE(vV,' ')
				except Exception as e:
					_.pr( row )
					_.pr( verse )

				words = verse[4].lower()

				words = _str.stripNonAlphaNumaric( words ).split(' ')
				index = {}
				count = {}
				data = []
				for w in words:
					if w in index.keys():
						theStem = index[w]
					else:
						theStem = ps.stem(w)
						index[w] = theStem
					data.append(theStem)
					if theStem in count.keys():
						count[theStem] += 1
					else:
						count[theStem] = 1

				pat = generatePatterns( data, 2 )
				if vID == '15' and 0:
					for xx in pat:
						_.pr(xx)
					sys.exit()
				try:
					ref = getBookByID(vB) + ' ' + vCh+':'+vV
				except Exception as e:
					_.colorThis( 'Error', 'red' )
					_.pr(row)
					_.pr(verse)
					sys.exit()
				spent = []
				for x in pat:
					p = x[0][0] + '_' + x[1][0]
					l = {  'id': vID, 'verse': ref, 'pos':  [ x[0][1], x[1][1] ] }
					xSpent = str(p)
					if not xSpent in spent:
						spent.append(xSpent)
						if p in pattern_index.keys():
							pattern_index[p].append( l )
						else:
							pattern_index[p] = []
							pattern_index[p].append( l )
				pass
				



		# pattern_index

		# _.printVar1( pattern_index )
		_.saveTable2( pattern_index, 'bible_patterns_raw.json' )


	if _.switches.isActive('FindPatterns'):
		index = _.getTable2( 'bible_patterns_raw.json' )
		patterns = {}
		spentIDs = {}
		cache = {}
		pattern_index = {}
		for k in index.keys():
			for words in index[k]:
				spentIDs[ words['id'] ] = []
				if words['id'] in patterns.keys():
					words['pattern'] = k
					patterns[ words['id'] ].append( words )
				else:
					words['pattern'] = k
					patterns[ words['id'] ] = []
					patterns[ words['id'] ].append( words )
				# words['patternX'] = words['pattern']

		for k in index.keys():



			test = {}
			for i, words in enumerate(index[k]):
				test[i] = {
							'id': words['pos'][0],
							'data': getVerseByIndex(words['id']),
							'pattern': words['pattern'],
							'add': [],
				}
			done = False
			while not done:
				tW = []
				for xK in test.keys():
					if test[xK]['id'] in spentIDs[ words['id'] ]:
						done = True
					else:
						test[xK]['id'] -= 1
						if test[xK]['id'] > 0:

							try:
								test[xK]['data'][  test[xK]['id']  ]
							except Exception as e:
								done = True
							else:
								if test[xK]['data'][  test[xK]['id']  ] in cache.keys():
									pst = cache[   test[xK]['data'][  test[xK]['id']  ]   ]
								else:
									pst = ps.stem( test[xK]['data'][  test[xK]['id']  ] )
									cache[   test[xK]['data'][  test[xK]['id']  ]   ] = ps.stem( test[xK]['data'][  test[xK]['id']  ] )
								test[xK]['pattern'] = pst + '_' + test[xK]['pattern']
								tW.append(  test[xK]['pattern']  )

				for xK in test.keys():

					cnt = 0
					for xy in tW:

						if test[xK]['pattern'] == xy:
							cnt +=1
					if not cnt > 1:
						done = True
					else:
						test[xK]['add'].append(test[xK]['id'])
						# words['pos'].append(test[xK]['id'])

						# _.pr(test[xK]['pattern'])

			pass

			for i in test.keys():
				for add in test[i]['add']:
					index[k][i]['pos'].append(add)
				index[k][i]['pos'].sort()

				newPattern = ''
				for pos in index[k][i]['pos']:
				nW = test[i]['data'][pos]
				if nW in cache.keys():
					pst = cache[   nW   ]
				else:
					pst = ps.stem( nW )
					cache[   nW   ] = ps.stem( nW )
				newPattern += '_' + pst
				newPattern = _str.cleanBE( newPattern , '_' )
				index[k][i]['pattern'] = newPattern
				# _.pr(index[k][i]['pattern'])



				# if index[k][i]['pattern'] in pattern_index.keys():
				#     MxPx = str(index[k][i])
				#     found = False
				#     for MyPy in pattern_index[ index[k][i]['pattern']  ]:
				#         if MxPx == str(MyPy):
				#             found = True
				#     if not found:
				#         pattern_index[ index[k][i]['pattern']  ].append( index[k][i] )
				# else:
				#     pattern_index[ index[k][i]['pattern']  ] = []
				#     pattern_index[ index[k][i]['pattern']  ].append( index[k][i] )



			test = {}
			for i, words in enumerate(index[k]):
				test[i] = {
							'id': words['pos'][ len(words['pos'])-1 ],
							'data': getVerseByIndex(words['id']),
							'pattern': words['pattern'],
							'add': [],
				}

			done = False
			while not done:
				tW = []
				for xK in test.keys():
					if test[xK]['id'] in spentIDs[ words['id'] ]:
						done = True
					else:
						test[xK]['id'] += 1
						if test[xK]['id'] > 0:
							try:
								test[xK]['data'][  test[xK]['id']  ]
							except Exception as e:
								done = True
							else:
								if test[xK]['data'][  test[xK]['id']  ] in cache.keys():
									pst = cache[   test[xK]['data'][  test[xK]['id']  ]   ]
								else:
									pst = ps.stem( test[xK]['data'][  test[xK]['id']  ] )
									cache[   test[xK]['data'][  test[xK]['id']  ]   ] = ps.stem( test[xK]['data'][  test[xK]['id']  ] )
								test[xK]['pattern'] =  test[xK]['pattern'] + '_' + pst
								tW.append(  test[xK]['pattern']  )

				for xK in test.keys():

					cnt = 0
					for xy in tW:

						if test[xK]['pattern'] == xy:
							cnt +=1
					if not cnt > 1:
						done = True
					else:
						test[xK]['add'].append(test[xK]['id'])

						# _.pr(test[xK]['pattern'])
			pass
			for i in test.keys():
				for add in test[i]['add']:
					index[k][i]['pos'].append(add)
				index[k][i]['pos'].sort()
								
			# for add in test[xK]['add']:
			#     words['pos'].append(add)
			# words['pos'].sort()

				newPattern = ''
				for pos in index[k][i]['pos']:
				nW = test[i]['data'][pos]
				if nW in cache.keys():
					pst = cache[   nW   ]
				else:
					pst = ps.stem( nW )
					cache[   nW   ] = ps.stem( nW )
				newPattern += '_' + pst
				newPattern = _str.cleanBE( newPattern , '_' )
				index[k][i]['pattern'] = newPattern
				# _.pr(index[k][i]['pattern'])



				pass

				text = getVerseByIndex( index[k][i]['id'] )
				if len( index[k][i]['pos'] ) > 2:
					thisPattern = []
					for pos in index[k][i]['pos']:
						spentIDs[ index[k][i]['id'] ].append( pos )
						if text[  pos  ] in cache.keys():
							pst = cache[   text[  pos  ]   ]
						else:
							pst = ps.stem( text[  pos  ] )
							cache[   text[  pos  ]   ] = ps.stem( text[  pos  ] )
						thisPattern.append( pst )

					try:
						while thisPattern[ len(thisPattern)-1 ] in list(omit_words.keys()):
							thisPattern.pop()
							index[k][i]['pos'].pop()
					except Exception as e:
						pass

					try:
						while thisPattern[ 0 ] in list(omit_words.keys()):
							thisPattern.pop(0)
							index[k][i]['pos'].pop(0)
					except Exception as e:
						pass


					index[k][i]['pattern'] = '_'.join( thisPattern )
					# _.pr( index[k][i]['pattern'] )

					if index[k][i]['pattern'] in pattern_index.keys():
						pattern_index[ index[k][i]['pattern']  ].append( index[k][i] )
					else:
						pattern_index[ index[k][i]['pattern']  ] = []
						pattern_index[ index[k][i]['pattern']  ].append( index[k][i] )



	# for k in index.keys():
	#     for i, words in enumerate(index[k]):
	#         text = getVerseByIndex( words['id'] )
	#         if len( words['pos'] ) > 2:
	#             thisPattern = []
	#             for pos in words['pos']:
	#                 spentIDs[ words['id'] ].append( pos )
	#                 if text[  pos  ] in cache.keys():
	#                     pst = cache[   text[  pos  ]   ]
	#                 else:
	#                     pst = ps.stem( text[  pos  ] )
	#                     cache[   text[  pos  ]   ] = ps.stem( text[  pos  ] )
	#                 thisPattern.append( pst )
	#             words['pattern'] = '_'.join( thisPattern )
	#             # _.pr( words['pattern'] )

	#             if words['pattern'] in pattern_index.keys():
	#                 pattern_index[ words['pattern']  ].append( words )
	#             else:
	#                 pattern_index[ words['pattern']  ] = []
	#                 pattern_index[ words['pattern']  ].append( words )



			# for words in index[k]:
			#     _.pr( words )
			# sys.exit()

		_.saveTable2( pattern_index, 'bible_patterns_min_3.json' )


def getVerseByIndex( vs ):
	row = _.appData[__.appReg]['pipe'][ int(vs)-1 ]
	row = row.replace( '\t', '  ' )
	row = _str.replaceDuplicate(row,'  ')
	verse = row.split('  ')
	try:
		vID = verse[0]
		vB = verse[1]
		vCh = verse[2]
		vV = verse[3]
		vV = _str.cleanBE(vV,' ')
	except Exception as e:
		_.pr( row )
		_.pr( verse )

	words = verse[4].lower()

	words = _str.stripNonAlphaNumaric( words ).split(' ')
	return words

# logCheck = _.tables.returnSorted( 'data', 'd.timestamp', _.getTable('fileBackup.json') )
def load():
	global booksRaw
	global booksNew
	global sections
	global omit_words
	omit_words = _.getTable( 'dic_omit.json' )
	# _.pr( list(omit_words.keys()) )
	# sys.exit()
	booksRaw = _.getText(_v.myTables + _v.slash+'bible_books.csv')
	booksNew = []
	sections = _.getTable('Bible_section_headers.json')
	newAbbreviations()


pattern_index = {}

# data = []
########################################################################################
if __name__ == '__main__':
	action()




