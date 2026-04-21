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


indices = {
				'single': None,
				'double': None,
}



def query(query):
	if len(query) == 1:
		result = searchSingle( wordStem(query[0]) )
		_.pr( result )

		x = _.traverse( result )
		for rec in x['fields']:
			if len( rec['parents'] ) == 2:
				bk = rec['parents'][0]
				ch = rec['parents'][1]
				vs = rec['field']
				_.pr( bk, ch, vs )
		# _.pr( x.keys() )

	else:
		q = []
		for x in query:
			q.append( wordStem(x) )
		result = []
		references = {}
		setCount = 0
		for qSet in _.generatePatterns( q ):

			# _.pr('qSet',qSet)
			setCount+=1
			indices = searchDouble(  q[qSet[0]]+' '+q[qSet[1]]  )
			if indices is None:
				_.pr('Error:',q[qSet[0]]+' '+q[qSet[1]])
			if not indices is None:
				for bk in indices:
					for ch in indices[bk]:
						for vs in indices[bk][ch]:
							if not bk in references:
								references[bk] = {}
								references[bk]['cnt'] = 0
							if not ch in references[bk]:
								references[bk][ch] = {}
								references[bk][ch]['cnt'] = 0
							if not vs in references[bk][ch]:
								references[bk][ch][vs] = {}
								references[bk][ch][vs]['cnt'] = 0

							references[bk]['cnt'] += 1
							references[bk][ch]['cnt'] += 1
							references[bk][ch][vs]['cnt'] += 1

		# _.pr(references)
		# sys.exit()
		wow = _.factor( references, count=setCount )
		# _.pr(wow['factors']['single'])
		table = {}
		books = []
		for relevant in wow['factors']['single'][1]['relevant']:
			rec = wow['records'][1][ relevant['id'] ]
			books.append( int( rec['path'].split('.')[0] ) )
			# _.pr(rec)
		for relevant in wow['factors']['single'][3]['relevant']:
			rec = wow['records'][3][ relevant['id'] ]
			# _.pr()
			bk = int( rec['path'].split('.')[0] )
			ch = int( rec['path'].split('.')[1] )
			vs = int( rec['path'].split('.')[2] )
			# if bk == 41:
			#     _.pr( rec )
			if not bk in table:
				table[bk] = {}
			if not ch in table[bk]:
				table[bk][ch] = {}
			if not vs in table[bk][ch]:
				table[bk][ch][vs] = {}

			# _.colorThis( [  eval(  "_B.labels['"+rec['path'].split('.')[0]+"']"  ), rec['path'].split('.')[1]+':'+rec['path'].split('.')[2]  ], 'yellow' )
			# word = eval(  '_B.Bible'+rec['buildB']  )
			# for x in query:
			#     for y in _.caseUnspecific(word,x):
			#         word = word.replace( y, _.colorThis( y, 'yellow', p=0 ) )
			# _.pr( word )
			# _.pr( rec )

		pass
		table = eval(   _.d2json( table, sort_keys=True )   )
		prefix = '\t\t'
		for bk in books:
			bk = str(bk)
			if bk in table:
				_.pr( '\n\n'+  _.colorThis( _B.labels[bk], 'green', p=0 )  + '\n' )
				chs = []
				for ch in table[bk]:
					chs.append( int(ch) )
				chs.sort()
				for ch in chs:
					ch = str(ch)
					result = []
					cnt=0
					mx=200

					result.append( '\n\t'+  _.colorThis( ch, 'red', p=0 )  + '\n' )
					result.append(prefix)
					vss = []
					for vs in table[bk][ch]:
						vss.append(int(vs))
					vss.sort()
					for vs in vss:
						vs = str(vs)

						word = eval(  "_B.Bible['"+bk+"']['"+ch+"']['"+vs+"']"  )
						for tmp in vs:
							cnt +=1
						if cnt > mx:
							cnt=0
							result.append( '\n'+prefix )
						result.append( ' '+_.colorThis( vs, 'yellow', p=0 )+' ' )
						rx=''
						past = False
						for tw in word:
							cnt +=1
							if cnt > mx:
								past=True
							if past and  tw==' ':
								rx+='\n'+prefix
								cnt=0
								past=False
							rx+=tw
						for x in query:
							for y in _.caseUnspecific(rx,x):
								rx = rx.replace( y, _.colorThis( y, 'cyan', p=0 ) )
						result.append( rx )

						# _.pr( '\t\t',_.colorThis( vs, 'cyan', p=0 ), word )
					_.pr( ''.join( result ) )
						# _.pr( rec )

			

			# for x in wow['records']:
			#     for y in wow['records'][x]:
			#         _.pr( y )




def searchDouble(subject):
	global indices

	if indices['double'] is None:
		global file
		indices['double'] = _.getTableProject( 'Bible.query.indices', _B.files['query']['double'] )
	if subject in indices['double']:
		return indices['double'][subject]
	return None

def searchSingle(subject):
	global indices

	if indices['single'] is None:
		global file
		indices['single'] = _.getTableProject( 'Bible.query.indices', _B.files['query']['single'] )
	if subject in indices['single']:
		return indices['single'][subject]
	return None

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
	word = word.lower()
	word = strip(word)
	global processWordStem
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	return processWordStem.stem(word)



processWordStem = None







