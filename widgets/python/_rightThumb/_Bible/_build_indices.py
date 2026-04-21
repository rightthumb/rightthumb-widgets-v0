import _rightThumb._construct as __

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import _rightThumb._base3 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._Bible as _B

import sys

def all(include_query=True):
	_.pr('Bible')
	Bible()
	_.pr('books')
	books()
	_.pr('labels')
	labels()
	if include_query:
		_.pr('query indices')
		search_indices()
	_.pr('\n','DONE')

indexes = {}
def search_indices():
	global indexes
	indexes = {
					'single': {},
					'double': {},
	}

	def doublesIndexAdd( subject, b, c, v ):

		if not subject in indexes['double']:
			indexes['double'][subject] = {}
		if not str(b) in indexes['double'][subject]:
			indexes['double'][subject][str(b)] = {}
		if not str(c) in indexes['double'][subject][str(b)]:
			indexes['double'][subject][str(b)][str(c)] = {}
		indexes['double'][subject][str(b)][str(c)][str(v)] = {}


	def strip(word):
		word = word.replace( "'s",'' )
		if "'" in word:
			n=[]
			for x in word.split(' '):
				if "'" in x:
					x=x.split("'")[0]
				n.append(x)
			word = ' '.join(n)
		y = ''
		for x in word:
			if x in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
				y+=x

		return y



	def wordStem(word):
		global processWordStem
		if processWordStem is None:
			import nltk
			from nltk.stem import PorterStemmer
			from nltk.tokenize import word_tokenize
			processWordStem = PorterStemmer()
		return processWordStem.stem(word)

	bk = 1
	ch = 1
	vs = 1
	done=False
	i=0
	while not done:
		# if i>100:
		#     done = True
		i+=1
		if not done and not str(vs) in _B.Bible[str(bk)][str(ch)]:
			vs = 1
			ch+=1

			if not done and not str(ch) in _B.Bible[str(bk)]:
				vs = 1
				ch = 1
				bk+=1

				if not done and not str(bk) in _B.Bible:
					done = True

		if not done:
			VERSE = _B.Bible[str(bk)][str(ch)][str(vs)]
			CLEAN = strip( VERSE )
			STEMs =[]
			diff=[]
			for x in CLEAN.split(' '):
				y = wordStem( x ).lower()

				if not y in indexes['single']:
					indexes['single'][y] = {}
				if not str(bk) in indexes['single'][y]:
					indexes['single'][y][str(bk)] = {}
				if not str(ch) in indexes['single'][y][str(bk)]:
					indexes['single'][y][str(bk)][str(ch)] = {}
				indexes['single'][y][str(bk)][str(ch)][str(vs)] = {}

				if not x.lower()==y:
					diff.append(y)
				STEMs.append(y)
			STEMS = ' '.join(STEMs)

			patterns = _.generatePatterns( STEMs )
			# _.pr()
			# _.pr()
			# _.pr( VERSE )
			# _.pr( STEMS )
			# _.pr(patterns)
			for Wi in patterns:
				Ws = []
				for tWi in Wi:
					Ws.append( STEMs[tWi] )
				subject = ' '.join(Ws)
				doublesIndexAdd( subject, bk, ch, vs )

				# _.pr(subject)
			# # _.pr( wordStem( VERSE ) )

			# _.pr( ' '.join(diff) )
			# _.pr()
			# input(' ')

			# sys.exit()

		vs+=1
	
	_.saveTableProject( 'Bible.query.indices', indexes['single'], _B.files['query']['single'], indentCode=False  )
	_.saveTableProject( 'Bible.query.indices', indexes['double'], _B.files['query']['double'], indentCode=False  )


def labels():
	theBooksA = _.getCSV( _v.projectData('Bible.src')+'Bible_books.csv' )
	Bible_books_print = {}
	for i,record in enumerate(theBooksA):
		bID = i+1
		Bible_books_print[str(bID)] = record['name']

	_.saveTableProject( 'Bible.app', Bible_books_print, _B.files['app']['book_labels'] )

def books():
	theBooksA = _.getCSV( _v.projectData('Bible.src')+'Bible_books.csv' )
	theBooksB = _.getText( _v.projectData('Bible.src')+'Bible_Books_abbreviations.txt', raw=True, clean=1 )
	_B.Books = {}
	tmpBooks = {}
	for i,record in enumerate(theBooksA):
		bID = i+1
		tmpBooks[record['name']] = bID
	#     _.pr( bID, record['name'] )
	# sys.exit()
	for i,record in enumerate(theBooksB.split('\n')):
		bID = i+1
		record = _str.replaceDuplicate(record,' ')
		record = _str.cleanBE(record,' ')
		recs = record.split(',')
		if not bID == tmpBooks[recs[0]]:
			_.colorThis( ['ERROR: ',bID,  record], 'red' )

		# try:
		#     _.pr( bID, tmpBooks[recs[0]], recs[0],  )
		#     # _.pr( bID, theBooksA[i], recs[0], tmpBooks[recs[0]] )
		# except Exception as e:
		#     _.colorThis( ['ERROR: ',bID,  record], 'red' )
		for rec in recs:
			_B.Books[rec] = bID
			_B.Books[rec.lower()] = bID
			_B.Books[rec.lower().replace(' ','')] = bID
			_B.Books[rec.replace(' ','')] = bID

	_.saveTableProject( 'Bible.app', _B.Books, _B.files['app']['books'] )
	_.saveTableProject( 'Bible.app', _B.Bible, _B.files['app']['Bible'] )
		# Books[ record['name'] ] = bID
		# Books[ record['abbreviation'] ] = bID
		# xx = record['abbreviation']
		# xx = xx.replace( '.', '' )
		# Books[ xx ] = bID
		# xx = xx.replace( ' ', '' )
		# Books[ xx ] = bID


def Bible():
	theText = _.getText( _v.projectData('Bible.src')+'Bible_av.txt', raw=True, clean=1 );
	_B.Bible = {}
	for i,row in enumerate(theText.split('\n')):
		# row = row.replace( '\t', '  ' )
		# row = _str.replaceDuplicate(row,'  ')
		verse = row.split('\t')
		try:
			vID = verse[0]
			vB = verse[1]
			vCh = verse[2]
			vV = verse[3]
			vV = _str.cleanBE(vV,' ')
			words = verse[4]
			words = _str.cleanBE(words,' ')
		except Exception as e:
			_.pr( row )
			_.pr( verse )
			sys.exit()
		if not vB in _B.Bible:
			_B.Bible[vB] = {}
		if not vCh in _B.Bible[vB]:
			_B.Bible[vB][vCh] = {}
		_B.Bible[vB][vCh][vV] = words
	_.saveTableProject( 'Bible.app', _B.Bible, _B.files['app']['Bible'] )



processWordStem = None







