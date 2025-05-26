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

import re
from operator import itemgetter
import _rightThumb._base3 as _

class Code:
	def __init__( self ):

		self.index = {}
		self.dom = {}
		self.dom_index = {}
		self.escape = _v.slash

		self.logistics = {

			'profiles': [
				{  'nestable': True,  'subject': [  '[',']'  ], 'label': 'brackets',             'rules': { 'prefix': ['variable'],    'validate': ['list'] } },
				{  'nestable': True,  'subject': [  '(',')'  ], 'label': 'parentheses',          'rules': { 'prefix': ['variable'],    'validate': ['list'] } },
				{  'nestable': True,  'subject': [  '{','}'  ], 'label': 'braces',               'rules': { 'prefix': ['variable'],    'validate': [{ 'self?is=variable': ['dic'] , 'self?is=orphan': ['dic'] }] } },
				{  'nestable': False, 'subject': [  '"'  ],     'label': 'double_quote',         'rules': { 'prefix': ['variable'], } },
				{  'nestable': False, 'subject': [  "'"  ],     'label': 'single_quote',         'rules': { 'prefix': ['variable'], } },
				{  'nestable': False, 'subject': [  '"""'  ],   'label': 'triple_double_quote',  'rules': { 'prefix': ['variable'], } },
				{  'nestable': False, 'subject': [  "'''"  ],   'label': 'triple_single_quote',  'rules': { 'prefix': ['variable'], } },
			],




			'rules': {


				'behavior': {
					'prefix': {
						'settings': { 'attribute': 'is', 'step': '<', 'start': 'start', 'end': '?', 'default': 'orphan' },
						'patterns': {
							'variable': { 'settings': {'ws': 'wsR'}, 'patterns': [ 'equals', 'label_an_brackets' ] },
						},

					},
					'validate': {
						'settings': { 'attribute': 'valid', 'step': '>', 'start': 'start', 'end': 'end', 'default': 'error' },
						'patterns': {
							'list': { 'settings': {'ws': 'wsR', 'loop':True}, 'patterns': [  'variable', tuple(['comma']) ] },
							'dic': { 'settings': {'ws': 'wsR', 'loop': True}, 'patterns': [ 'quote_label_an', 'colon', 'variable', tuple(['comma']) ] },
						},
					},
				},
				'patterns': {

					'label_an': [ ['0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_'] ],
					'quote_label_an': [ [{'patterns':['label_an']}], [{'patterns':['quote']}] ],
					'quote_label_an_brackets': [[{'patterns':['label_an']}],[{'patterns':['label_an']},{'profiles':['brackets']}]],
					'label_an_brackets': [[{'patterns':['label_an']}],[{'patterns':['label_an']},{'profiles':['brackets']}]],

					'equals': [['=']],
					'colon': [[':']],
					'semicolon': [[';']],
					'comma': [[',']],

					'ws': [[' ']],
					'wsR': [[' ','\n']],

					'variable': [[ {'patterns':['numbers']}, {'patterns':['quote']}, {'patterns':['parentheses']}, {'patterns':['braces']} ]],
  
					'quote': [[ {'profiles': {'~': 'quote'} } ]],
					'numbers': [['0123456789']],
					'brackets': [[ {'profiles': ['brackets'] } ]],
					'parentheses': [[ {'profiles': ['parentheses'] } ]],
					'braces': [[ {'profiles': ['braces'] } ]],

					'datatypes': [],
				},


			},


			'settings': {
				'whitespace': {},
				'startswithINT': {},
			},


			'indexes': {

				'scan': {},
				'IDs': {},

				'escape': [],

				'open': {},
				'close': {},
				'list': [],
				

				'records': [],

				'lines': {
					'list': [],
					'id': {},
				},

				'rules': {
					'list': [],
				},
				'profiles': {
					'searches': {
						'=':{},
						'~':{},
					}
				},

				'dom': { 'o': {}, 'c': {}, 'list': [] },

			},


		}


		

		self.profiles = self.logistics['profiles']

	def start( self ):
		self.index = { 'start': {}, 'end': {} }
		self.dom = {}
		self.dom_index = {}
		self.omit = { 'lists': {}, 'matches': {} }
		self.comments = []

		for i,record in enumerate(self.profiles):
			m = 0
			for x in record['subject']:
				if len(x) > m:
					m = len(x)
			self.profiles[i]['length'] = m

		self.profiles = sorted(self.profiles, key=itemgetter('length'))
		self.profiles.reverse()
		profiles = []
		for i,record in enumerate(self.profiles):
			if not record['nestable']:
				profiles.append( record )
		for i,record in enumerate(self.profiles):
			if record['nestable']:
				profiles.append( record )
		self.profiles = profiles
		for i,recordA in enumerate(self.profiles):
			for ii,recordB in enumerate(self.profiles):
				for subB in recordB['subject']:
					for subA in recordA['subject']:
						if subB in subA and not i == ii:
							if not subA in self.omit['lists']:
								self.omit['lists'][subA] = []
							if not subB in self.omit['matches']:
								self.omit['matches'][subB] = []
							if not subA in self.omit['matches'][subB]:
								self.omit['matches'][subB].append(subA)

		for i,record in enumerate(self.profiles):

			self.logistics['indexes']['IDs'][i] = { 'o': [], 'c': [] }

			if len(record['subject']) == 1:
				self.profiles[i]['subject'].append( record['subject'][0] )

		


		# _.printTest(self.profiles)
		# _.printTest(self.omit)
	def iterStr( self, string ):
		string = string.replace(  _v.slash, _v.slash+_v.slash  )
		string = string.replace(  '{', _v.slash+'{'  )
		string = string.replace(  '(', _v.slash+'('  )
		string = string.replace(  '[', _v.slash+'['  )
		string = string.replace(  ')', _v.slash+')'  )
		return string
	def process( self, data=None ):
		self.test = [ 0,1,2,3,4,5,6,7,8 ]
		self.test = []

		# data = eval(data)
		# data[ 'abcd' ] = ( 1,2,3 )
		data = str(data)

		if 0 in self.test:
			_.pr()
			_.pr()
			_.pr(data)
			_.pr()
			_.pr()
		self.data = data
		self.start()
		index = {}
		spent = {}
		escape = []
		matches = re.finditer(   self.iterStr(self.escape)   , self.data)
		escape = [match.start() for match in matches]
		self.logistics['indexes']['escape'] = escape

		matches = re.finditer(   self.iterStr( '\n' )   , self.data)
		self.logistics['indexes']['lines']['list'] = [match.start() for match in matches]


		for i,record in enumerate(self.profiles):
			for subject in record['subject']:
				if subject in self.data:
					matches = re.finditer(   self.iterStr(subject)   , self.data)
					matches_positions = [match.start() for match in matches]

					for mp in matches_positions:
						if not mp-1 in escape:
							if not subject in self.omit['matches']:
								index[mp] = i
								# index[mp] = subject
							elif not mp in spent:
								index[mp] = i
								# index[mp] = subject

					if subject in self.omit['lists']:
						for mp in matches_positions:
							mi = mp
							mx = mp + len(subject)
							while not mi == mx:
								spent[mi] = i
								self.omit['lists'][subject].append(mi)
								mi+=1



		depth = {}
		isOpen = {}
		for i,record in enumerate(self.profiles):
			depth[i] = 0
			isOpen[i] = {}
		pass
		# _.printTest( index )
		
		records = []
		inComment = False
		dex = []
		commentID = None
		for x in index.keys():
			dex.append( x )
		# _.pr(dex)
		dex.sort()
		# _.pr(dex)

		self.on_line = None

		for i in dex:
			line = self.findLine( i )+1
			# _.pr( self.on_line,   self.logistics['indexes']['lines']['list'][self.on_line],   ': LINE: ', line, i )


			if not inComment or index[i] == commentID:
				isClose = False
				if inComment:
					if index[i] == commentID and self.snippet( i, len(self.profiles[ index[i] ]['subject'][1]) ) == self.profiles[ index[i] ]['subject'][1]:
						inComment = False
						isClose=True
				else:
					if self.snippet( i, len(self.profiles[ index[i] ]['subject'][0]) ) == self.profiles[ index[i] ]['subject'][0]:
						self.logistics['indexes']['lines']['id'][i] = line
						if not self.profiles[ index[i] ]['nestable']:
							inComment = True
							commentID = index[i]
						# _.pr( 'open index', i, index[i],  )
						depth[ index[i] ]+=1
						isOpen[index[i]][ depth[ index[i] ] ] = i
					elif self.snippet( i, len(self.profiles[ index[i] ]['subject'][1]) ) == self.profiles[ index[i] ]['subject'][1]:
						isClose=True

				pass
				if isClose:
					self.logistics['indexes']['lines']['id'][i] = line
					o = isOpen[index[i]][ depth[ index[i] ] ]
					# _.pr( 'close index', i, index[i], self.snippet(o, i) )    
					# _.pr( 'close index', i, index[i], data[i], '\t', i-o )
					self.index['start'][o] = index[i]
					self.index['end'][i] = index[i]
					records.append({   'id': index[i], 'start': o, 'end': i   })
					self.logistics['indexes']['IDs'][ index[i] ]['o'].append( o )
					self.logistics['indexes']['IDs'][ index[i] ]['c'].append( i )
					self.logistics['indexes']['open'][ o ] = i
					self.logistics['indexes']['close'][ i ] = o
					depth[ index[i] ]-=1
						
		
		self.logistics['indexes']['records'] = records


		self.logistics['profiles'] = self.profiles
		for i,record in enumerate(self.profiles):
			for subject in record['subject']:
				self.logistics['indexes']['scan'][subject] = i

		pass
		del self.profiles
		for i in self.logistics['indexes']['open']:
			self.logistics['indexes']['list'].append(i)
		self.logistics['indexes']['list'].sort()

		i = 0
		m = len( self.data )-1
		while i <= m:
			if i in self.logistics['indexes']['open']:
				o = i
				c = self.logistics['indexes']['open'][i]
				self.logistics['indexes']['dom']['o'][o] = c
				self.logistics['indexes']['dom']['c'][c] = o
				self.logistics['indexes']['dom']['list'].append(o)
				i = c
			i+=1


		self.logistics['indexes']['dom']['list'].sort()


		self.rules()



	def rules( self ):

		self.test = []

		if 2 in self.test:
			_.printVar( self.index )
			_.printVar( self.logistics['indexes']['records'] )
		if 3 in self.test:
			_.pr()
			_.pr()
		# rules behavior validate patterns list settings
		self.logistics['indexes']['rules']['behaviors'] = {}
		for behavior in self.logistics['rules']['behavior']:
			self.logistics['indexes']['rules']['behaviors'][behavior] = {}
			for pattern in self.logistics['rules']['behavior'][behavior]['patterns']:
				self.logistics['indexes']['rules']['behaviors'][behavior][pattern] = {'o':{},'c':{}}

		# for o in self.logistics['indexes']['list']:
		for o in self.logistics['indexes']['dom']['list']:
			self.location = o

			# _.pr( 'oooooooooooooooooooooooooooooooooooo', o )
			record = self.lookup( o=o )
			_.pr( self.snippet( record['o'], record['c'] ) )
			# { 'o': o, 'c': c, 'r': r, 'p': p, 'l': l }
			if 3 in self.test:
				_.pr()
				_.pr(record['p']['label'])
			rules = []
			record['attributes'] = {}
			totalValid = True
			for bi,behavior in enumerate(record['p']['rules']):
				valid = False
				a = []
				for pi,pattern in enumerate(record['p']['rules'][behavior]):
					if not valid:
						if type(pattern) == dict:
							resPatts = self.dicRule( record, behavior, pattern, bi, pi, record['attributes'] )
							# _.pr( 'resPatts', resPatts )
							if not resPatts is None:
								for resPatt in resPatts:
									if not valid:
										result = self.rule( record, behavior, resPatt, bi, pi, record['attributes'] )
										_.pr('result',result)
										if result['valid']:
											valid = True

						elif not type(pattern) == dict:
							result = self.rule( record, behavior, pattern, bi, pi, record['attributes'] )
						if result['valid']:
							valid = True
				if result['attribute']:
					record['attributes'][ list(result['attribute'].keys())[0] ] = result['attribute'][ list(result['attribute'].keys())[0] ]
					# _.pr( result['attribute'] )
					
					a = [   record['attributes'][ list(result['attribute'].keys())[0] ], result['attribute'][ list(result['attribute'].keys())[0] ]   ]
				rules.append({ 'behavior': behavior, 'pattern': pattern, 'bi': bi, 'pi': pi,  'result': result, 'attribute': a, 'valid': result['valid'] })

				record['rules'] = rules
				subValid = True
				for rule in rules:
					if not rule['valid']:
						subValid = False
					# if rule['attribute']:
						# record['attributes'] = rule['attributes'][rule['attribute'][0]] = rule['attribute'][1]
					# _.pr(self.logistics['indexes']['rules']['behaviors'])
					p =str(rule['pattern'])
					if not p in self.logistics['indexes']['rules']['behaviors'][ rule['behavior'] ]:
						self.logistics['indexes']['rules']['behaviors'][ rule['behavior'] ][ p ] = {'o':{},'c':{}}
					self.logistics['indexes']['rules']['behaviors'][ rule['behavior'] ][ p ]['o'][record['o']] = record['r']
					self.logistics['indexes']['rules']['behaviors'][ rule['behavior'] ][ p ]['c'][record['c']] = record['r']
					# _.pr( '\t', rule['behavior'], rule['pattern'], rule['valid'],  )
				record['valid'] = subValid
				if not subValid:
					totalValid = False
				
			pass
			record['valid'] = totalValid


		if 3 in self.test:
			_.pr()
			_.pr()

		self.logistics['indexes']['lines']['list']
		self.logistics['indexes']['lines']['id']





	def rule( self, record, behavior, pattern, bi, pi, attributes ):
		# if 4 in self.test:
		_.pr( '-bpa- \t ', behavior, pattern, attributes )
		_.colorThis( '**********************************************************************************************************************************', 'red' )
		a = { 'attribute': {}, 'valid': None }
		a = { 'attribute': { 'is': 'orphan' }, 'valid': None }

		

		if not type( pattern ) == dict:
			s = self.logistics['rules']['behavior'][behavior]['settings']
			ps = self.logistics['rules']['behavior'][behavior]['patterns'][pattern]['settings']
			
			for sk in s.keys():
				ps[sk] = s[sk]
			queries = []
			_.colorThis( 'B------------------------------------------------------------------------', 'yellow' )
			_.pr(  )
			_.pr( behavior, pattern )
			_.pr( '\t s:', s )
			_.pr( '\tps:', ps )
			_.pr()
			_.pr()
			for pat in self.logistics['rules']['behavior'][behavior]['patterns'][pattern]['patterns']:
				# _.pr( '\t\t', pat )
				# _.pr( 'pat pat pat:', pat )
				isRequired = True
				if type(pat) == tuple:
					isRequired = False
					pat = pat[0] 

				result = self.rule_patterns( record, pat, s, ps )
				queries.append({ 'isRequired': isRequired, 'pattern': pat, 'query': result })
				_.colorThis( '\t ------------------------------------------------------------------------', 'green' )
				_.pr( '\n\n\t rule_patterns:\n\t\t', isRequired, result )
			pass


			# def testQuery( testing, iData ):

			def peek( direction, i, test, ws ): # 542
				done = False
				while not done:
					pass

			valid = True
			start = self.location
			i = start
			success = {
					'a': None,
					'b': None,
					'c': None,
					'd': None,
			}
			
			completed = False
			for testing in queries:
				if not completed:
					# success['b'] = False
					_.pr()
					_.pr()
					_.pr('___')

					for aTest in testing['query']:
						if not completed:
							# success['c'] = False
							if not type(aTest) == list:
								_.pr( 'NOT:', aTest )
							elif type(aTest) == list:
								_.pr()
								for bTest in aTest:
									if not type(bTest) == list:
										cTest = [bTest]
									else:
										_.pr('-')
										cTest = bTest
									for dTest in cTest:
										if not completed:
											# success['d'] = False
											done = False
											while not done:
												if not 'step' in ps:
													_.colorThis( 'Error: ps step', 'red' )
													sys.exit()

												if ps['step'] == '<':
													i-=1
												elif ps['step'] == '>':
													i+=1
												else:
													_.colorThis( 'Error: ps step', 'red' )
													sys.exit()

												try:
													self.data[i]
												except Exception as e:
													done = True
													
												if not done:
													if self.data[i] == ' ' or self.data[i] == '\t' :
														if ps['ws'] == 'wsR' or ps['ws'] == 'ws' or ps['ws'] == True:
															pass
														else:
															done = True
													if self.data[i] == '\n':
														if ps['ws'] == 'wsR':
															pass
														else:
															done = True

												if not done:
													if self.data[i] == ' ' or self.data[i] == '\n' or self.data[i] == '\t':
														pass
													else:
														if type(dTest) == str:
															_.color( 'str', 'blue', 'yellow' )
														elif type(dTest) == int:
															_.color( 'int', 'yellow', 'blue' )
														else:
															_.color( [  'Error:', type(dTest)  ], 'red', 'white' )

														if type(dTest) == str:
															
															if self.data[i] in dTest:
																success['d']
																peek()

														elif type(dTest) == int:
															p = self.logistics['profiles'][dTest]
															_.pr( p )
															if i in self.logistics['indexes']['open']:
																_.pr( 'YES, open' )
															else:
																_.pr( 'NO, not open' )

														pass
														# for x in ran:
														#     ran[x] = True


														# _.pr(  )
														done = True




			if not ran['a'] or not ran['b'] and valid:
				valid = False


			if not valid:
				a['valid'] = False
			else:
				a['valid'] = True

			_.colorThis( 'E------------------------------------------------------------------------', 'yellow' )

		a['valid'] = False
		return a

	def rule_patterns( self, record, pattern, s, ps ):
		# _.colorThis( ['\t\t\t', pattern], 'purple' )
		# _.pr()
		# _.colorThis( ['\t\t\t record:', record], 'yellow' )
		# _.colorThis( ['\t\t\t settings:', self.logistics['rules']['patterns'][pattern]], 'yellow' )
		# _.pr()
		results = []
		valid = None
		for pat in self.logistics['rules']['patterns'][pattern]:
			qResults = []
			# _.pr( 'pat pat pat:', pat )
			queries = self.rule_patterns_resolution( pat )
			# valid = None
			# _.pr()
			# _.pr('\t',pattern)
			# i = record['o']
			# _.pr( self.data[i] )
			# _.pr(i)

			if not type(queries) == list:
				qResults.append( queries )

			if type(queries) == list:
				for query in queries:
					# _.pr()
					# _.pr( '\t\tquery:', query )
					if type(query) == list:
						# qResults.append( query )
						for q in query:
							if type(q) == list:
								qResults.append( q )
								# for qq in q:
								#     qResults.append( qq )
							else:
								qResults.append( q )
					else:
						qResults.append( query )


			results.append(qResults)
			# results.append( q )
				# _.pr( '\t\t\t  s:', s )
				# _.pr( '\t\t\t ps:', ps )
				# _.pr()
				# valid
			# sys.exit()
		return results


		
		pass
	def rule_patterns_resolution( self, patterns ):
		# _.pr( 'patterns patterns:', patterns )
		queries = []
		for subject in patterns:
			query = []
			resolution = self.rule_patterns_resolution_item( subject )
			# _.pr( 'subject:', subject, resolution )


			if type(resolution) == int:
				query.append( resolution )
			elif type(resolution) == str:
				query.append( resolution )
			elif type(resolution) == list:
				query.append( resolution )
				# for x in resolution:
					# query.append( x )
			elif type(resolution) == tuple:
				query.append( resolution )

			





			queries.append( query )

		return queries

	def rule_patterns_resolution_item( self, subject ):
		# _.pr( 'subject subject: ', subject )
		result = []
		if type(subject) == list:
			# _.colorThis( 'HERE LIST' )
			for x in subject:
				result.append( self.rule_patterns_resolution_item(x) )

		elif type(subject) == int:
			return subject
		elif type(subject) == str:
			return subject
		elif type(subject) == tuple:
			
			for x in subject:
				y = self.rule_patterns_resolution_item(x)
				if type(y) == int:
					result.append( y )
				elif type(y) == str:
					result.append( y )
				else:
					for z in y:
						result.append( z )
			return tuple(result)

		elif type(subject) == dict:
			pre_query = []
			if 'patterns' in subject:
				if 4 in self.test:
					_.colorThis( [ 'dic patterns:', subject['patterns'] ], 'red' )
				for pati in subject['patterns']:
					for subPati in self.logistics['rules']['patterns'][pati]:
						for x in subPati:
							# _.pr( 'x:', type(x) )
							pre_query.append( x )

						# self.test = [4]
						if 4 in self.test:
							_.colorThis( [  '\t', subPati  ], 'purple' )
						self.logistics['indexes']['open']
						self.logistics['indexes']['close']

			if 'profiles' in subject:
				# _.pr( subject['profiles'] )
				for profile in subject['profiles']:
					if type(subject['profiles']) == str:
						r = self.findProfile( profile )
						if type(r) == list:
							for rr in r:
								pre_query.append( rr )
						else:
							pre_query.append( r )
					elif type(subject['profiles']) == dict:
						special = list(subject['profiles'].keys())[0]
						r = self.findProfile( subject['profiles'][special], special )
						if type(r) == list:
							for rr in r:
								pre_query.append( rr )
						else:
							pre_query.append( r )
					elif type(subject['profiles']) == list:
						for x in subject['profiles']:
							# _.pr( 'HERE x:', type(x) )
							r = self.findProfile( x )
							# _.pr('r',r,x)
							if type(r) == list:
								for rr in r:
									# _.pr( 'rr:', type(rr) )
									pre_query.append( rr )
							else:
								pre_query.append( r )
					else:
						_.colorThis( [  'ERROR:', subject  ], 'red' )
					# _.colorThis( [ profile, r, subject, subject['profiles'] ], 'red' )
					# sys.exit()
					
			# _.pr('pre_query',pre_query)
			for x in pre_query:
				# _.pr( 'pre_query pre_query:', type(x), x )
				if x is None:
					_.colorThis( [ 'ERROR: pre_query X is None', 'red' ] )
					sys.exit()
				y = self.rule_patterns_resolution_item(x)
				# _.colorThis( ['y',y], 'green' )
				if type(y) == int:
					result.append( y )
					# _.pr( 'ADDED', y )
				elif type(y) == str:
					result.append( y )
				elif type(y) == tuple:
					result.append( tuple(y) )
				elif type(y) == list:
					for z in y:
						result.append( z )
		if 5 in self.test:
			_.pr( 'subject:', subject )
		counter=0

		while not self.rule_patterns_resolution_items_VALID(result):
			counter+=1
			# _.pr( 'counter:', counter )
			temp_result = []
			for x in result:
				if type(x) == int:
					temp_result.append(x)
				elif type(x) == str:
					temp_result.append(x)
				elif type(x) == tuple:
					
					for x in x:
						y = self.rule_patterns_resolution_item(x)
						if type(y) == int:
							result.append( y )
						elif type(y) == str:
							result.append( y )
						else:
							for z in y:
								result.append( z )
					return tuple(result)

				elif type(subject) == dict:
					y = self.rule_patterns_resolution_item(x)
					if type(y) == int:
						temp_result.append(x)
					elif type(y) == str:
						temp_result.append(x)
					elif type(y) == tuple:
						
						for xx in y:
							yy = self.rule_patterns_resolution_item(xx)
							if type(yy) == int:
								temp_result.append( yy )
							elif type(y) == str:
								temp_result.append( yy )
							else:
								for z in yy:
									temp_result.append( z )
						return tuple(temp_result)
			result = temp_result
		clean = []
		for x in result:
			if x == 0 or x:
				clean.append(x)
		return clean

	def rule_patterns_resolution_items_VALID( self, subject, initialized=False ):
		if not initialized:
			self.rule_patterns_resolution_items_VALID_GOOD = True
		if not self.rule_patterns_resolution_items_VALID_GOOD:
			return False

		if type(subject) == int:
			return True
		elif type(subject) == str:
			return True
		elif type(subject) == tuple:
			for x in subject:
				self.rule_patterns_resolution_items_VALID( x, initialized=True )
		elif type(subject) == list:
			for x in subject:
				self.rule_patterns_resolution_items_VALID( x, initialized=True )
		elif type(subject) == dict:
			self.rule_patterns_resolution_items_VALID_GOOD = False
			return False

		return True
	def findProfile( self, subject, special='=' ):
		# _.pr('findProfile:',subject,special)
		results = []
		if subject in self.logistics['indexes']['profiles']['searches'][special]:
			# _.pr('subject',subject,self.logistics['indexes']['profiles']['searches'][special][subject])
			return self.logistics['indexes']['profiles']['searches'][special][subject]

		for i,x in enumerate(self.logistics['profiles']):
			if special == '=':
				if subject.lower() in self.logistics['profiles'][i]['label'].lower():
				# if not subject == self.logistics['indexes']['profiles']['searches'][special]:
					self.logistics['indexes']['profiles']['searches'][special][subject] = i
					# _.pr('subject',subject,self.logistics['indexes']['profiles']['searches'][special][subject])
					return i

			elif special == '~':
				if subject.lower() in self.logistics['profiles'][i]['label'].lower():
				# if not subject in self.logistics['indexes']['profiles']['searches'][special]:
					# self.logistics['indexes']['profiles']['searches'][special][subject] = i
					# _.pr('subject',subject,self.logistics['indexes']['profiles']['searches'][special][subject])
					results.append(i)
					# return i
		if special == '~':
			self.logistics['indexes']['profiles']['searches'][special][subject] = results
			# _.colorThis(   ['subject', subject, special, results], 'purple'   )
			return results

		return None


	def a_rule_proces_pattern( self, i, s, pattern, pat ):
		if 4 in self.test:
			_.pr( pat )

			if type(rec) == tuple: _.colorThis( 'tuple', 'yellow' );
			if type(rec) == list:  _.colorThis( 'list', 'yellow' );
			if type(rec) == str:   _.colorThis( 'string', 'yellow' );
			if type(rec) == dict:  _.colorThis( 'dic', 'yellow' );
		pass
		"""
		{ 'prefix': 'variable',    'validate': { 'self?is=variable': ['dic,function'], 'self?is=orphan': ['function'] } } }

		{ 'step': '<', 'start': 'start', 'end': '?', 'default': 'orphan' }
		{ 'attribute': 'is', 'step': '>', 'start': 'start', 'end': 'end', 'default': 'error' }
		{'ws': 'wsR', 'loop':True}
		rules behavior prefix settings
		rules behavior prefix patterns variable

		rules behavior validate settings
		rules behavior validate patterns list settings
		rules behavior validate patterns list patterns
		rules behavior validate patterns dic
		[  'variable', ('comma') ]

		rules patterns 
		{'profiles': {'~': 'quote'} }
		{'patterns':['label_an']}
		{'profiles':['brackets']}
		"""
		self.logistics['indexes']['rules']['list']

		
		self.logistics['rules']['behavior']['prefix']['patterns']['variable']['settings']
		self.logistics['rules']['behavior']['prefix']['patterns']['variable']['patterns']





	def dicRule( self, record, behavior, pattern, bi, pi, attributes ):
		result = None
		if type( pattern ) == dict:
			hasBeenFound = False
			for key in pattern.keys():
				good = True
				if not hasBeenFound:
					if 'self?' in key:
						aa = key.split('?')[1]
						if '-=' in aa:
							isOmit = True
							bb = aa.split('-=')
						elif '-~' in aa:
							isOmit = True
							bb = aa.split('-~')
						elif '=' in aa:
							isOmit = False
							bb = aa.split('=')
						elif '~' in aa:
							isOmit = False
							bb = aa.split('~')
						k = bb[0]
						v = bb[1]
						if k in attributes:
							wasFound = False
							xIS = None
							xIN = None

							if '~' in aa:
								if _.showLine( str(attributes[k]), v ):
									xIN = True
								else:
									xIN = False
							elif '=' in aa:
								if v.lower() == str(attributes[k]).lower():
									xIS = True
								else:
									xIS = False

							if '~' in aa:
								if xIN or xIS:
									wasFound = True
							if '=' in aa:
								if xIN or xIS:
									wasFound = True
						if isOmit and wasFound:
							good = False
						elif not isOmit and not wasFound:
							good = False
					if good:
						hasBeenFound = True
						result = pattern[key]


		return result




	def segment( self, o=None, c=None ):
		pass

	

	def findLine( self, i ):
		if self.on_line is None:
			self.on_line = 0
			if 1 in self.test:
				_.pr()
				_.pr('lines')
				for x in self.logistics['indexes']['lines']['list']:
					_.pr(x)
				_.pr()
		if i == 0:
			self.on_line = 0
			return 0

		if self.on_line == 0:
			if not len(self.logistics['indexes']['lines']['list']):
				return 0
			if i > 0 and i < self.logistics['indexes']['lines']['list'][0]:
				return self.on_line
		n = self.on_line
		if i > self.logistics['indexes']['lines']['list'][n-1] and i < self.logistics['indexes']['lines']['list'][n]:
			return self.on_line
		found = False
		mx = len(self.logistics['indexes']['lines']['list'])-1
		while not found:
			if n+1 > mx:
				found=True
				self.on_line = n
				return self.on_line
			if i > self.logistics['indexes']['lines']['list'][n] and i < self.logistics['indexes']['lines']['list'][n+1]:
				found = True
				self.on_line = n+1
				return self.on_line
			n+=1
			
		return self.on_line


	def lookup( self, o=None, c=None ):
		if not o is None:
			c = self.logistics['indexes']['open'][o]

		if not c is None:
			o = self.logistics['indexes']['close'][c]

		r = self.index['start'][o]
		p = self.logistics['profiles'][r]
		l = {
					'o': {
								'l': self.logistics['indexes']['lines']['id'][o],
								's': None,
								'e': None,
					},
					'c': {
								'l': self.logistics['indexes']['lines']['id'][c],
								's': None,
								'e': None,
					},
		}
		if len(self.logistics['indexes']['lines']['list']):
			l['o']['e'] = self.logistics['indexes']['lines']['list'][ l['o']['l']-1 ]
			l['c']['e'] = self.logistics['indexes']['lines']['list'][ l['c']['l']-1 ]
		else:
			l['o']['e'] = 0
			l['c']['e'] = 0

		if l['o']['l']-2 < 0:
			l['o']['s'] = 0
		else:
			l['o']['s'] = self.logistics['indexes']['lines']['list'][ l['o']['l']-2 ]


		if l['c']['l']-2 < 0:
			l['c']['s'] = 0
		else:
			l['c']['s'] = self.logistics['indexes']['lines']['list'][ l['c']['l']-2 ]

		# _.pr( l )

		return { 'o': o, 'c': c, 'r': r, 'p': p, 'l': l }
	def snippet( self, i, length=None, end=None ):

		if not length is None:
			return self.data[i:i+length]
		elif not end is None:
			end+=1
			return self.data[i:end]

"""

EXAMPLES:

	b ttt

	pp aggregate -aggregate trigger[format,sum[trigger['round',bytes]]] folder ext
	pp aggregate -aggregate "trigger[(format),sum[trigger['round',bytes]]]" folder ext
	pp aggregate -f cleric_spell_slots.json
	pp aggregate -f Ports_Complete_List_Index.json
	pp aggregate -f dic_omit.json
	pp aggregate -f sorcerer.json
	pp aggregate -f sql_commands.txt
	pp aggregate -f fileID_efficiency.index
	pp aggregate -time -f fileID_efficiency.index
	pp aggregate -time -f cleric_spell_slots.json
	pp aggregate -time -f dic_omit.json
	pp aggregate
	pp aggregate -f temp.json

	b ttt
	pp aggregate -f dic_omit.json.js


"""
"""

LEFT OFF:

	413        self.rule
		446        self.rule_patterns
			solve the STEP for validation


457 def peek(


"""


 



