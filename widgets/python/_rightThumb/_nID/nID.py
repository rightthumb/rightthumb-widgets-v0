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
		# self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
		# self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		self.code = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		# self.max = 100000000
		self.max = 10000
		self.sequence = -1
		self.lastMini = ''
		self.checked = False
		self.table = []
		self.index = {}
		self.default_hash = '{C8B1F7DD-82AC-4768-962F-2DA54C323FA7}'
		self.ph = '-'
		self.safe = False
		self.safe = True
		self.return_test = False
		# self.max_unsafe = 128
		# self.max_unsafe = 1024
		self.max_unsafe = 4095
		# self.preCheck()
	def password( self, pw=None ):
		if pw is None:
			pw = self.default_hash
		pw = str(pw) + self.default_hash
		import _rightThumb._md5 as _md5
		from operator import itemgetter
		code_gen = []
		en = _md5.md5( pw )
		for x in self.code:
			en = _md5.md5( en )
			code_gen.append({ 'code': x, 'sort': en })
		code_sort = sorted(code_gen, key=itemgetter('sort'))
		code = ''
		for x in code_sort:
			code += x['code']

		self.code = code

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
		self.code = self.code.replace(self.ph,'')
		table = []
		for x in self.code:
			if not x in table:
				table.append(x)
		self.code = ''.join(table)
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


mini = nID()







