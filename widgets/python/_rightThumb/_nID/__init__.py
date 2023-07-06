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
import math
commitPer = 46285
# import _rightThumb._base3 as _
# import _rightThumb._nID as _nID

# 62,3906,242234,15018570,945927738,1862060570
# https://atozmath.com/NumberSeries.aspx

class nID:
	def __init__( self ):
		self.delim=''
		# self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
		# self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		self.hasRun = False
		self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		# self.code = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		self.code_default = self.code
		# self.max = 100000000
		self.max = 10000
		self.sequence = -1
		self.lastMini = ''
		self.checked = False
		self.table = []
		self.index = {}
		self.default_hash = '{C8B1F7DD-82AC-4768-962F-2DA54C323FA7}'
		self.ph = '-'
		self.ph = '0'
		self.safe = False
		self.safe = True
		self.return_test = False
		# self.max_unsafe = 128
		# self.max_unsafe = 1024
		self.max_unsafe = 4095
		# self.preCheck()
		self.passwordRan = False
	def password( self, pw=None ):
		# if self.passwordRan:
		#     return None
		# if not pw is None:
		self.passwordRan = True
		self.code = self.code_default
		# _.pr(self.code)
		if pw is None:
			pw = self.default_hash
		pw = str(pw) + self.default_hash
		import _rightThumb._md5 as _md5
		from operator import itemgetter
		code_gen = []
		en = _md5.md5( pw )
		# _.pr(en)
		# sys.exit()
		for x in self.code:
			en = _md5.md5( en )
			code_gen.append({ 'code': x, 'sort': en })
		code_sort = sorted(code_gen, key=itemgetter('sort'))
		code = ''
		for x in code_sort:
			code += x['code']
		self.code = code
		# _.pr(self.code)
	def preCheck( self ):
		self.check()
		self.checked = False
	def check( self ):
		if not self.safe:
			self.code = ''
			# for x in range(1,1024):
			self.max_unsafe = 128
			for x in range(1,sys.maxunicode):
				try:
					self.code+=str(chr(x))
				except Exception as e:
					pass
				if len(self.code) == self.max_unsafe+1:
					break
		# _.pr(self.code)
		if type(self.code) == str: self.code = self.code.replace(self.ph,'')
		elif self.ph in self.code: self.code.pop(self.code.index(self.ph)) 
		# _.pr( len( self.code ) )
		# sys.exit()
		table = []
		for x in self.code:
			if not x in table:
				table.append(x)
		self.code = self.delim.join(table) 
		if not self.passwordRan:
			self.password()
		self.base = len(self.code)
		# _.pr(self.base)
		# _.pr(self.table)
		self.place_value_id(save=True)
		# _.pr(self.table)
		# sys.exit()
		self.checked = True



	def next( self ):
		self.sequence+=1
		return self.gen( self.sequence )



	def resolve( self, miniID=None ):
		if not self.hasRun:
			self.gen(0)
		self.hasRun = True
		if miniID is None:
			miniID = self.lastMini

		table = []
		for x in miniID:
			if x == self.ph:
				table.append( self.ph )
			else:
				table.append( self.code.index(x) )

		# _.colorThis( str(table), 'yellow' )


		pvX = 0
		table.reverse()
		data = []
		total = 0
		for i,x in enumerate(table):

			method = 1

			if method == 1:
				# _.pr( type(self.table[i]), type(x), x )
				if not x == self.ph:
					y = self.table[i][x]
					total += y
				# _.colorThis(   [ table, y, type(y) ], 'yellow'   )
		# _.colorThis( [ 'total', total ], 'red' )
		table.reverse()
		if self.return_test:
			return total,table
		return total


	def placeValueQuery( self, num ):
		placeValue = 1
		table = []
		for pvi, pv in enumerate(self.table):
			if pvi:
				table.append({  'value': pv[0], 'pv': pvi+1  })
		# table.reverse()
		for rec in table:
			if num >= rec['value']:
				placeValue = rec['pv']

		# if num >= self.table[6][0]:
		#     placeValue = 7
		# elif num >= self.table[5][0]:
		#     placeValue = 6
		# elif num >= self.table[4][0]:
		#     placeValue = 5
		# elif num >= self.table[3][0]:
		#     placeValue = 4
		# elif num >= self.table[2][0]:
		#     placeValue = 3
		# elif num >= self.table[1][0]:
		#     placeValue = 2


		return placeValue



	def gen( self, num=189922, data=False, d=None ):
		if type(num) == float:
			num = int(num)
		if type(num) == str:
			numX = ''
			for x in num:
				if x in '0123456789':
					numX+=x
			if not len(numX):
				numX = '0'
			num = int(numX)
		if not self.checked: self.check();
		self.sequence = num
		if not d is None:
			data = d

		n = num
		table = []
		pv = 0
		pvDs = []
		while not n == 0:
			if n < self.base:
				table.append(n)
				n = 0
			else:
				run = self.query( n )
				# _.pr( 'run', run )
				# _.pr( 'run', run )
				pvA = self.placeValueQuery(n)
				try:
					n -= run['n']
				except Exception as e:
					_.pr(run)
				pvB = self.placeValueQuery(n)
				pvD = pvA - pvB
				pvDs.append( pvD )
				try:
					table.append(run['id'])
				except Exception as e:
					_.pr('Error: Number is to large')
					sys.exit()

				# if num >= 3906:
				#     _.pr( run )
				# if not n == 0:
				if pvD > 1:
					while not pvD == 1:
						pvD-=1
						table.append(self.ph)



				pv = run['pv']

		# if num >= 3906:
		#     _.pr( table )

		placeValue = self.placeValueQuery( num )

		if len(table) < placeValue:
			i=len(table)
			while i < placeValue:
				i+=1
				table.append(self.ph)


		if data:
			return table
		# _.colorThis( str(table), 'green' )
		miniID = ''
		for x in table:
			if x == self.ph:
				miniID += self.ph
			else:
				miniID += self.code[x]
		self.lastMini = miniID


		# if num >= 3579345993194:
		#     shouldAdd = True
		#     for i,x in enumerate(miniID):
		#         if i and not x == '-':
		#             shouldAdd = True
		#     if shouldAdd:
		#         miniID+='-'
		#         if num >= 221919451578090:
		#             miniID+='-'


		if self.return_test:
			return miniID, table, pvDs
		return miniID


	def query( self, search ):
		
		last = {
					'pv': 0,
					'id': 0,
					'n': 0,
		}
		add = 0
		startAdd = False
		for pvi, pv in enumerate(self.table):
			# _.pr(pv)
			if startAdd: add+=1;
			for numi, num in enumerate(self.table[pvi]):

				if num > search:
					return last
				last = {
							'pv': pvi,
							'id': numi,
							'n': num,
				}
				if num == search:
					return last
				# _.pr( num )
		return None

	def place_value_id( self, test=189922, save=False ):
		def idFix(xy):
			xy+=1
			if xy >= self.base:
				xy=0
			return xy
		if test == 0:
			return 0
		isTest = 0
		if isTest:
			test = m
		p = 0
		gNext = False
		master = []
		theSet = []
		t = 0
		theID = -1
		lastID = None
		lastT = 0
		group = 0
		added = 0
		lastP = -2
		for i in range(1,self.max):
			theID += 1
			if i and 0 and i % (self.base-1) == 0:
				# theID=0; 
				p+=1;
				

			if i % (self.base+1) == 0:
				pass
				# theID = 0

			if not p == lastP and lastP > -1:
				master.append( theSet ); theSet = []
			lastP = p
			
			theSet.append( t )
			add = int( math.pow(self.base,p) ); t = t + add
			if save:
				try:
					self.index[p][theID] = t
				except Exception as e:
					try:
						self.index[p] = {}
						self.index[p][theID] = t
					except Exception as e:
						self.index = {}
						self.index[p] = {}
						self.index[p][theID] = t
				


			if isTest:
				if t >= 15501: sys.exit();
				if t >= 59:
					_.pr( '',theID, p, add, '\t', _nID.gen( t, d=1 ), '   \t', addComma(t), t )
			if isTest and t == 62:
				_.pr( 62, idFix(theID), t )
				sys.exit()
			if test > t:
				lastID = theID
				lastT = t
				lastP = p
			elif test == t:
				if not save:
					return 0, (theID), t, p
					# return 0, idFix(theID), t, p


			else:
				test = test - lastT
				if not save:
					return test, (lastID), lastT, lastP
					return test, idFix(lastID), lastT, lastP
					return test, lastID



			# else:
			#     # test = test - lastT
			#     test = self.index[lastP][idFix(lastID)] - lastT
			#     if not save:
			#         return test, idFix(lastID), self.index[lastP][idFix(lastID)], lastP
			#         return test, idFix(lastID), lastT, lastP
			#         return test, lastID



			
			if i and 1 and i % self.base == 0:
				theID = -1; p+=1;

				# _.pr( len(theSet), self.base )
				# if not len(theSet) == self.base:
				#     while not len(theSet) == self.base:
				#         theSet.pop()
				# if not len(master):
				#     theSet.reverse()
				#     theSet.append(0)
				#     theSet.reverse()
			# if i and 1 and i % (self.base-1) == 0:
				
		if save:
			self.table = master
			# _.saveTable2( master, 'theMaster.json' )
			# if save == 2:









def table( db='nID.db' ):
	global commitPer
	import sqlite3
	import os
	import sys

	if os.path.isfile( db ):
		os.unlink( db )

	
	conn = sqlite3.connect(db)
	cursor = conn.cursor()
	sql =  'CREATE TABLE resolution (resolve text, n int)'
	cursor.execute( sql )
	mits = 0
	for n in range(0,1000000):
		resolve = gen(n)
		cursor.execute(  'INSERT INTO resolution VALUES (?,?)'  ,  (resolve, n)  )
		if n % commitPer == 0:
			conn.commit()
			mits+=1
			_.pr(mits,n)
	conn.commit()



# 6084


def gen2( num, data=None, d=None ):
	if not d is None:
		data = d
	# base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	

	bMax = len(base)
	def placeShift(nVal):
		if not len(nVal):
			return [0]
		lVal = len(nVal)
		nVal.reverse()
		nth = 0
		psAdd = False
		psDone = False
			
		while not psAdd and not psDone:
			try:
				nVal[nth]+=1
			except Exception as e:
				_.pr('nVal[nth]+=1',nVal,nth)
				sys.exit()

			shouldZero = False
			if nVal[nth] == bMax:
				shouldZero = True
				nth += 1
			else:
				psDone = True
			if nth == bMax-1 and nVal[nth] == bMax:
				psAdd = True
			if shouldZero:
				try:
					nVal[nth]
				except Exception as e:
					psAdd = True
				nVal[nth-1] = 0

		nVal.reverse()
		if psAdd:
			nVal.append(0)
		return nVal

	place=0
	i=0
	val = []
	iVal = 0
	while not i==num:
		i+=1
		iVal+=1
		if iVal == bMax:
			iVal=0
			val = placeShift(val)
	result = ''
	theVal = val + [iVal]
	for x in theVal:
		try:
			result += base[x]
		except Exception as e:
			_.pr( 'result += base[x]', x )
	if data:
		return theVal
	return result


def cleanFirst(string,rWhat):
	string = str(string)
	rWhat = str(rWhat)
	# string = replaceDuplicate(string,rWhat)
	string = '*?*' + str(string)
	string = string.replace('*?*' + rWhat, '')
	string = string.replace('*?*', '')
	if string.startswith(rWhat):
		string = cleanFirst(string,rWhat)
	return string


def cleanEnd(string,rWhat):
	string = str(string)
	rWhat = str(rWhat)
	# string = replaceDuplicate(string,rWhat)
	string +=  '*?*'
	string = string.replace(rWhat + '*?*', '')
	string = string.replace('*?*', '')
	if string.endswith(rWhat):
		string = cleanEnd(string,rWhat)

	return string


def cleanBE(string,rWhat):
	string = cleanEnd(string,rWhat)
	string = cleanFirst(string,rWhat)
	return string

def addComma( data ):
	test = 0
	try:
		int(data)
		test+=1
	except Exception as e:
		pass
	try:
		float(data)
		test+=1
	except Exception as e:
		pass
	
	if not test:
		return data

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
	result = cleanBE( result, ',' )
	return result





class checksum:
	def __init__( self, setting=None, password=None ):
		# import _rightThumb._dir as _dir

		self.setting_default = '4'
		if setting is None:
			setting = self.setting_default


		



		self.n = '426823703364514620874542913917197729348219899126521164381552351538128349665262681268148205682501121066833416371782602609153237664861049626896662789132588093508729110062071035645304010595221030020183810820535448688754157846407366282460'
		self.nn = self.n
		self.setting = setting



		self.permutations = {
							'128': '10,573,313,306,183,500,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000',
							'64': '21,147,822,030,980,700,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000',
							'32': '57,407,133,808,466,100,000,000,000,000,000,000,000,000,000,000,000,000',
							'16': '4,243,193,364,951,970,000,000,000,000',
							'8': '4,243,193,364,951,970,000,000,000,000',
							'4': '12,524,520',
							'2': '3,660',
		}

		self.options = {
							'128': 230,
							'64': 115,
							'32': 58,
							'16': 30,
							'8': 15,
							'4': 8,
							'2': 4,
		}
		# https://stattrek.com/online-calculator/combinations-permutations.aspx

		if not self.setting in list(self.options.keys()):
			_.pr( '\t', 'Settings error:' )
			_.pr( '\t\t', 'Try: 128, 64, 32, 16, 8, 4' )
			sys.exit()



		self.index = {}
		self.slots = {}
		self.divs = {}


		self.loaded = None



		self.load(password)


	def file( self, path=None, setting=None, password=None ):

		self.checksum = None
		if setting is None:
			setting = self.setting_default


		self.load(password)

		if not self.processFile(path):
			return None
		# _.pr(self.n)
		return self.checksum

		# self.start()
		# self.chunk(chunk)
		# self.digest()    

	def start( self ):
		self.location = 0
		self.index = []
		for x in self.n:
			self.index.append(int(x))

	def average( self, l ):
		try:
			return sum(l) / len(l)
		except Exception as e:
			_.pr( 'Error: average' )

	def chunk( self, chunk ):
		self.index[ self.location ] += self.average( list(chunk) )
		self.step(1)

	def digest( self ):
		nn = ''
		# _.pr()
		# _.pr(self.n)
		# _.printVar(self.index)
		for i,x in enumerate(self.n):
			ni = int(self.n[i])
			if not ni:
				d = self.index[i]
			elif ni:
				d = self.index[i] / ni
			t = str(d)
			if not '.' in t:
				nn += self.n[i]
			if '.' in t:
				p = t.split('.')[1]
				nn += self.digitB( self.n[i], int(p) )
				# if len(p) < 4:
				#     nn += self.digit( self.n[i], int(p) )
				# else:
				#     ii=0
				#     pp = ''
				#     while not ii == 3:
				#         pp += p[ii]
				#         ii+=1
				#     nn += self.digit( self.n[i], int(pp) )
		self.n = nn
		# _.pr(self.n)
		# _.pr()

		x = mini.gen( int(self.n) )
		xx = ''
		i=0
		for y in x:
			i+=1
			if i <= int(self.setting):
				xx += y
		
		self.checksum = xx

		return True




	def run( self, path=None, setting=None, password=None ):

		if not self.getBin(path):
			return None


		if setting is None:
			setting = self.setting_default


		self.load(password)


		
		self.nIndex = {}
		for i,x in enumerate(self.n):
			self.nIndex[str(i)] = 0
		locationMax = len(self.n)-1
		location = 0
		for i,c in enumerate(self.data):
			try:
				if type(c) == int:
					self.nIndex[ str(location) ] += c
					_.pr(c)
					# _.pr('A')
				else:
					self.nIndex[ str(location) ] += ord(c)
					# _.pr('B')
				
			except Exception as e:
				_.pr()
				_.pr('\tError')
				_.pr( '\t\t',c )
				_.pr()
				_.pr(i,chr(c))
				_.pr()
				_.pr(self.data)

				sys.exit()
			location+=1
			if location > locationMax:
				location=0
		# _.pr( self.n )
		done = self.build()
		# _.pr( self.n )
		x = mini.gen( done )
		xx = ''
		i=0
		for y in x:
			i+=1
			if i <= int(self.setting):
				xx += y
		
		return xx





	def build( self ):


		nn = ''
		for i,x in enumerate(self.n):
			ni = int(self.n[i])
			if not ni:
				d = self.nIndex[str(i)]
			elif ni:
				d = self.nIndex[str(i)] / ni
			t = str(d)
			if not '.' in t:
				nn += self.n[i]
			if '.' in t:
				p = t.split('.')[1]
				nn += self.digitB( self.n[i], int(p) )
				# if len(p) < 4:
				#     nn += self.digit( self.n[i], int(p) )
				# else:
				#     ii=0
				#     pp = ''
				#     while not ii == 3:
				#         pp += p[ii]
				#         ii+=1
				#     nn += self.digit( self.n[i], int(pp) )
		self.n = nn

			
		# for x in self.index.keys():
		#     self.index[x] = self.digit( self.index[x], len(self.data) )

		# newA = ''
		# for x in self.n:
		#     newA += self.index[x]
		
		# newB = ''
		# for i,x in enumerate(newA):
		#     newB += self.digit( x, self.slots[i] )

		return int(self.n)



	def password( self, password ):
		self.n = self.nn
		if  (type(password) == list or type(password) == tuple) and len(password) == 1:
			self.passwordA = str(password[0])
			self.passwordB = str(password[0])
		elif (type(password) == list or type(password) == tuple) and len(password) > 1:
			self.passwordA = str(password[0])
			self.passwordB = str(password[1])
		elif type(password) == int:
			self.passwordA = str(password)
			self.passwordB = str(password)
		elif type(password) == str:
			if not len(password):
				password = None
			self.passwordA = password
			self.passwordB = password
		else:
			self.passwordA = password
			self.passwordB = password
		# _.pr( 'self.passwordB',self.passwordB )
		mini.password( self.passwordB )
		default = '{E23CD55D-E33F-42F2-81B1-72F8319A6087}'
		if self.passwordA is None:
			self.passwordA = default
		pw = str(self.passwordA) + default
		import _rightThumb._md5 as _md5
		from operator import itemgetter
		code_gen = []
		en = _md5.md5( pw )
		for x in self.n:
			en = _md5.md5( en )
			code_gen.append({ 'code': x, 'sort': en })
		code_sort = sorted(code_gen, key=itemgetter('sort'))
		code = ''
		for x in code_sort:
			code += x['code']

		self.n = code


	def load( self, password ):
		# if not self.loaded is None:
		self.loaded = True
		self.n = self.nn

		if not password is None:
			self.password(password)

		nn=''
		for i, x in enumerate(self.n):
			if i <= self.options[self.setting]:
				nn += x
		
		self.locationMX = len(self.n)-1


		# divsA = 1
		# divsB = 5
		# for i,x in enumerate(self.n):
		#     ix = i+1
		#     self.slots[i] = 0
		#     self.index[x] = x
		#     divsI = divsA
		#     while not divsI == divsB:
		#         if ix%divsI==0:
		#             try:
		#                 self.divs[divsI].append(i)
		#             except Exception as e:
		#                 self.divs[divsI] = []
		#                 self.divs[divsI].append(i)
		#         divsI+=1


	def digitB( self, z, much ):
		# _.pr(z,much)
		r = int(z)
		for x in str(much):
			r += int(x)
			for w in str(r):
				r = int(w)

		# _.pr( z,r )
		return self.digit(z,r)

	def digit( self, z, much ):
		z = int(z)
		i = 0
		# _.pr()
		# _.pr(z,much)
		while not i == much:
			
			i+=1
			z += 1
			if z > 9:
				z = 0
		# _.pr(z)
		return str(z)

	def step( self, much ):

		if much == 1:
			self.location+=1
			if self.location > self.locationMX:
				self.location=0

		else:
			i = 0
			while not i == much:
				i+=1
				self.location+=1
				if self.location > self.locationMX:
					self.location=0

	def process( self, ii, char ):

		o=ord(char)

		for x in self.index.keys():
			self.index[x] = self.digit( self.index[x], o )

		for x in self.divs.keys():
			if ii%int(x)==0:
				for y in self.divs[x]:
					self.slots[y]+=o

	def getBin( self, path ):
		if path is None:
			_.pr()
			_.pr( "\tchecksum = _nID.checksum( data, setting='16', password=['abc',123]  ).run()" )
			_.pr()
			sys.exit()

		if not os.path.isfile(path):
			return False

		try:
			f = open( path, 'rb' )
			data = f.read()
			f.close()
			self.data = data
		except Exception as e:
			return False

		return True

	def processFile( self, path ):

		if path is None:
			_.pr()
			_.pr( "\tchecksum = _nID.checksum( data, setting='16', password=['abc',123]  ).run()" )
			_.pr()
			sys.exit()

		if not os.path.isfile(path):
			return False

		self.start()
		# _.pr(path)
		with open( path, 'rb' ) as part:
			for chunk in iter(lambda: part.read(4096), b''):
				self.chunk(chunk)
		return self.digest()


mini = nID()


