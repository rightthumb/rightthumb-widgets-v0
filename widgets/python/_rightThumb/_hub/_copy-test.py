

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


############################################################## copy-fn-class


def defaultScriptTriggers():
	global defaultScriptTriggers_run
	defaultScriptTriggers_run = True
	__.appReg_bk = __.appReg


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

	def addPadding( self, value, extra, right ):
		value = self.runTrigger( str(value) )
		oValue = value
		addPadding = (extra + self.maxField) - len( value )
		add = ''

		while not len(value) >= self.maxField+extra:
			value += ' '
			add += ' '
		# for x in range(1,addPadding+1):
		#   value += ' '
		# return str(self.maxField)+' '+str(len( value ))+value
		if right:
			value = add + oValue
		return value

	def addPaddingSetSpaces( self, value ):
		value = self.runTrigger( str(value) )
		addPadding = self.maxField - len( value )
		newValue = value
		Zeros = ''
		while not len(newValue) == self.maxField:
			Zeros += ' '
			newValue = Zeros + value
		return newValue

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
		self.fields = {}
		self.extra = 0

	def lengths( self, project ):
		result = {}
		for record in self.fields[project]:
			if record.project == project:
				result[record.name] = record.maxField
			
		return result
		

	def register( self, project='', names='', value='', appReg=False, script=False, maxField=None,        p=None, n=None, v=None, m=None, isRegisterDic=False ):

		# if project in self.fields:
		#   if not isRegisterDic:
		#       del self.fields[ project ]

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
		if not project in self.fields:
			self.fields[project] = []
		for name in names.split(','):

			shouldAdd = True

			for i,s in enumerate(self.fields[project]):
				if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
					shouldAdd = False
			if shouldAdd:
				self.fields[project].append( Field( project, name, value, appReg, script, maxField ) )
				if maxField and type(value) == int:
					return self.fields[project][len(self.fields[project])-1].addPaddingZeros(value)
				elif maxField and type(value) == str:
					return self.fields[project][len(self.fields[project])-1].addPadding(value)
			else:
				self.registerValue( project, name, value, appReg )

	def registerValue( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		
		result = False
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				self.fields[project][i].registerValue( value )
				result = True
		return result


	def padZeros( self, project, name, value, extra=None, appReg=False, space=False ):

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				if space:
					return self.fields[project][i].addPaddingSetSpaces( value )
				else:
					return self.fields[project][i].addPaddingZeros( value )
				result = self.fields[project][i].addPaddingZeros( value )
		return result


	def value( self, project, name, value, extra=None, right=False, appReg=False,    r=None ):
		result = value
		if not r is None:
			right = r

		if extra is None:
			extra = self.extra

		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPadding( value, extra, right )
		return result
	def valuez( self, project, name, value, appReg=False ):
		if type(appReg) == bool:
			appReg = __.appReg
		for i,s in enumerate(self.fields[project]):
			if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and name == self.fields[project][i].name:
				result = self.fields[project][i].addPaddingZeros( value )
		return result

	def asset( self, project, asset, appReg=False ):
		self.fields[project] = []
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
			self.register( project, name, asset[name], appReg, isRegisterDic=True )


def showLine( string, plus = '', minus = '', plusOr = False, end=None ):
	# print(plus)
	# print(string)
	global switches
	# print(switches.isActive('Plus'))
	# print(switches.values('Plus'))
	# sys.exit()
	if switches.isActive('Plus') or not plus == '':
		# print('asdf')
		result = positiveResults(string,plus,plusOr,end)
		if not result and switches.isActive('PlusClose'):
			result = closeResults( string )

	else:
		result = True
	if result == True and  (switches.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print(result)
	return result


def minusResults(string,minus=''):
	global switches
	if not switches.isActive('StrictCase'):
		string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switches.values('Minus')
	if type( minusInput ) == str:
		if not switches.isActive('StrictCase'):
			minusInput = minusInput.lower()
		else:
			minusInput = minusInput
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i] = minusInput[i].lower()

		minusList = minusInput

	try:
		for s in minusList:
			if not switches.isActive('StrictCase'):
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


def closeResults( string ):
	global switches
	global plusClose
	
	if len( switches.value('PlusClose') ):
		try:
			plusClose = float( switches.value('PlusClose') )
		except Exception as e:
			pass

	test = patternDiff( string, switches.value('Plus') )
	# print( int(test), string, switches.value('Plus') )
	if test >= plusClose:
		# print( test, string )
		return True
	else:
		return False


def patternDiff(a,b):
	# print('here')
	# a = 'gensslkey'
	# b = 'gensslkey'
	# b = 'gensslkeyz'
	# b = 'ssl_socket_bridge_client_user_administrator_logs_b'
	a = a.lower()
	b = b.lower()
	testing = 0

	if testing:
		print()
		print()
		print('________________________________________________________')
		print()
		print()
		print( a,b )
	x = patternMatch( a, b )
	d = get_change( len(a),len(b) )
	e = get_change( x, d )
	# e = get_change( d, x )
	if testing:
		print('x',x)
		print( 'd',d )
		print( 'e,f',e )
	f = int(100-e)
	f =e
	# print( 'f',f )
	if f == 0:
		f = 100
	# dd = d
	dd = int(100-d)
	if dd == 0:
		dd = 100
	if testing:
		print( 'dd',dd )
	# if d <= f:
	if d >= f:
		aa = dd
		bb = f
	else:
		aa = f
		bb = dd
	alphaTest = 'b'
	if alphaTest == 'a':
		kAA = {}
		kAB = {}
		kBA = {}
		kBB = {}
		for ch0 in a:
			if not ch0 in kAA:
				kAA[ch0] = 0
				kAB[ch0] = 0
			if ch0 in b:
				kAA[ch0] += 1
				for ch1 in b:
					kAB[ch0] += 1

		for ch0 in b:
			if not ch0 in kBA:
				kBA[ch0] = 0
				kBB[ch0] = 0
			if ch0 in a:
				kBA[ch0] += 1
				for ch1 in a:
					kBB[ch0] += 1


		theSetA = []
		theSetB = []
		for kk in kAA:
			theSetA.append( percentageDiffIntAuto( kAA[kk], kAB[kk] ) )
		for kk in kAA:
			try:
				theSetB.append( percentageDiffIntAuto( kBA[kk], kBB[kk] ) )
			except Exception as e:
				print()
				sys.exit()

		# pp = av(theSet)
		pA = av(theSetA)
		pB = av(theSetB)

	elif alphaTest == 'b':
		tA = 0
		tB = 0
		for ch0 in a:
			if ch0 in b:
				tA += 1

		for ch0 in b:
			if ch0 in a:
				tB += 1
		pA = percentageDiffIntAuto( tA, len(a) )
		pB = percentageDiffIntAuto( tB, len(b) )

	if testing:
		print( 'pA', pA )
		print( 'pB', pB )

	zz = xMultiply(  [aa,100], [bb,0]  )
	if zz > 100:
		zz = xMultiply(  [bb,100], [aa,0]  )

	if testing:
		print([aa,100], [bb,0])
		print(  'diff', zz )
		print( [aa,bb, pA,pB] )
		print(  'av', av([aa,bb, pA,pB])  )
	ww = av([aa,bb, pA,pB])
	# if pA > pB:
	#   if pA < ww
	# print( int(ww), [aa,bb, pA,pB], a, b,  )
	return ww


def av( ds ):
	total = 0
	for x in ds:
		total+=x
	return total / len(ds)


def xMultiply( a, b ):
	fail = False
	if not type(a) == list or not type(b) == list or not len(a) == 2 or not len(b) == 2:
		fail=True

	if not b[1]:
		z = (a[1] * b[0]) / a[0]
	elif not b[0]:
		z = (a[0] * b[1]) / a[1]
	elif not a[1]:
		z = (a[0] * b[1]) / a[0]
	elif not a[0]:
		z = (a[1] * b[0]) / a[1]
	else:
		fail=True
	if fail:
		colorThis( 'Error: xMultiply' )
		colorThis( '\texpected:', 'yellow' )
		colorThis( ['\t\t', str([960,540]), str([480,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([960,540]), str([0,270])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([960,0])], 'yellow' )
		colorThis( '\t\t         or' )
		colorThis( ['\t\t', str([480,270]), str([0,540])], 'yellow' )
		colorThis( 'fail' )
		sys.exit()
	if str(z).endswith('.0'):
		return int(z)
	else:
		return z


def colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False, simpleDic=False, colorProfile=None,      p=None, c=None, sd=None, isError=False ):

	if isError:
		color = 'red'

	if not c is None:
		color = c
	if not sd is None:
		simpleDic = sd

	if not p is None:
		shouldPrint = p

	if simpleDic and type(strings) == dict:
		newString = ''
		for k in strings.keys():
			newString += ' ' + k + ': ' + str(strings[k]) + ' '
		strings = newString

	if simpleDic and type(strings) == list:
		for i,thisItem in enumerate(strings):
			if type(thisItem) == dict:
				newString = ''
				for k in thisItem.keys():
					newString += ' ' + k + ': ' + str(thisItem[k]) + ' '
				strings[i] = newString

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




	if type(strings) == list:

		for i,x in enumerate(strings):

			strings[i] = str( x )

		string = ' '.join( strings )
	else:
		string = str(strings)

	global switches
	if switches.isActive( 'NoColor' ):
		if shouldPrint:
			print(string)
			return string
		else:
			return string

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
		print()
		print( strings )
		print()
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
		if isError:
			sys.exit()
		return None



	return result


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


def genUUID( project='', label='', uniqueTimestamp=False ):
	global appData
	global appInfo
	uuid = __.imp('uuid')
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


def saveTable( rows, theFile, tableTemp=False, printThis=True, indentCode=True, sort_keys=False, archive=False,                k=0,s=0,tmp=None,here=None,h=None,    p=1, me=0   ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not h is None: here = True;
	if not here is None: saveTable2( rows, theFile ); return None;
	if not tmp is None: tableTemp = True;
	if k or s: sort_keys = True;
	if not p: printThis = False;
		

	


	# defaults to myTables
	px = ''
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		file0 = _v.stmp + _v.slash + theFile
		px = file0
	else:
		if not tableTemp:
			file0 = _v.myTables + _v.slash + theFile
			px = theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
			px = file0

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = simplejson.dumps(rows)
	
	if archive:
		import _rightThumb._md5 as _md5

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
	HD.chmod(theFile)

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
	if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );
	return file0


def changeM( path, stampM, stampA=None, meta=False, p=0 ):
	if p:
		mn = ''
		if time_diff(stampM) == 'today':
			mn = ', '+str(int((time.time() - stampM) /60)) + ' min'
			if mn == '0 min':
				mn = ', just now'
		print( friendlyDate(stampM), colorThis( [time_diff(stampM)+ mn], 'yellow', p=0 ), path )
	if stampA is None:
		stampA = stampM
	# print(stampM)
	# print(stampA)
	global changeDate_Table
	global _dir
	global touch_meta



	if _dir is None:
		import _rightThumb._dir as _dir

	if meta:
		touch_meta = getTable( 'touch.meta' )
		if not path in touch_meta:
			touch_meta[path] = {}
		if not 'epoch' in touch_meta[path]:
			touch_meta[path]['epoch'] = {}
		touch_meta[path]['epoch']['me'] = stampM
		touch_meta[path]['epoch']['ae'] = stampA
		saveTable( touch_meta, 'touch.meta', p=0 )

	if not meta:
		if changeDate_Table is None:
			changeDate_Table = getTable( 'touch.index' )
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		if os.path.isfile(path):
			if not path in changeDate_Table:
				changeDate_Table[path] = _dir.info(path)
				saveTable( changeDate_Table, 'touch.index', p=0 )
			try:
				os.utime(path,(stampA, stampM))
			except Exception as e:
				pass


def getTable( theFile, tableTemp=False,      isDic=None, isList=None,      tmp=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	# defaults to myTables
	if not type( tableTemp ) == bool:
		if tableTemp == 'split':
			file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	else:
		if tableTemp == True:
			file0 = _v.stmp + _v.slash + theFile
		else:
			file0 = _v.myTables + _v.slash + theFile


	if not os.path.isfile(file0):
		file0 = theFile
	if os.path.isfile(file0):
		# print( 'theFile', theFile )
		# print( 'file0', file0 )
		# import bigjson
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		return json_data
		# with open( file0, 'rb' ) as f:
			# json_data = bigjson.load(f)
			# json_data = bigjson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
	else:
		return __.data_default(file=theFile,default=[]).default()


def time_diff(epoch):
	return dateDiffText( epoch )
	global _dir
	if _dir is None:
		import _rightThumb._dir as _dir
	return _dir.time_diff(autoDate(epoch))


def autoDate( theDate ):
	# if type(theDate) == float or type(theDate) == int:
	#   return theDate
	import _rightThumb._date as _date
	return _date.autoDate( theDate )


def dateDiffText( theDate, epoch=None ):

	y=0
	m=0
	w=0

	theDate = autoDate( theDate )
	if epoch is None:
		epoch = time.time()
	# woy = getWOY( theDate )
	days = abs(daysDiff( theDate, epoch ))
	
	if theDate < epoch:
		end = '<'
	else:
		end = '>'

	msDiff = epoch - theDate

	if msDiff > 0 and msDiff <= 86400:
		return 'today'
	elif msDiff > 0 and msDiff <= 82800:
		return 'today'
	elif msDiff > 0 and msDiff <= 169200:
		return 'yesterday'
	elif msDiff > 0 and msDiff <= 604801:
		return 'this week'



	# print( theDate, days, theDate < epoch, theDate > epoch, epoch, time.time() )
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'

	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )

	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )


def daysDiff( one, two ):
	global date_datetime
	oneA = autoDate( one )
	twoB = autoDate( two )
	g = 1
	if two > one:
		g = 2

	if one == two:
		return 0
	elif one > two:
		one = friendlyDate( oneA ).split(' ')[0]
		two = friendlyDate( twoB ).split(' ')[0]
	else:
		one = friendlyDate( twoB ).split(' ')[0]
		two = friendlyDate( oneA ).split(' ')[0]


	# print( '090', one, two )

	oneB = one.split('-')
	twoB = two.split('-')
	if date_datetime is None:
		from datetime import date as date_datetime
	d0 = date_datetime(int(oneB[0]), int(oneB[1]), int(oneB[2]))
	# print( '080', twoB )
	d1 = date_datetime(int(twoB[0]), int(twoB[1]), int(twoB[2]))
	delta = d1 - d0
	dd = delta.days
	if g == 1:
		dd = abs(dd)
	return dd


def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )


def getWOY( theDate ):
	theDate = autoDate( theDate )
	woy = getWOYFromEpoch(theDate)
	year = getYearFromEpoch(theDate)
	weekAndYear = round(woy * 0.01,2) + year
	weekAndYear = str(weekAndYear)
	if len(weekAndYear) == 6:
		weekAndYear += '0' 
	return weekAndYear


def getYearFromEpoch(theDate):
	theDate = autoDate(theDate)
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]


def getWOYFromEpoch(theDate):
	# print('theDate:',theDate)
	theDate = autoDate(theDate)

	try:
		return datetime.datetime.fromtimestamp( theDate ).isocalendar()[1]
	except Exception as e:
		print( 'Error:', theDate )
		sys.exit()


def printBold( string, color='white', prefix='' ):
	
	if '\n' in string:
		string = string.replace( '\n', '\n'+prefix )
	else:
		string = prefix + string
	
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


def fileDate( theDate ):
	friendly = friendlyDate( theDate )
	friendly = friendly.replace( ' ', '_' )
	friendly = friendly.replace( ':', '-' )
	return friendly


def saveTable2( rows, theFile, printThis=False, sort_keys=False, indentCode=True, p=None, me=0 ):
	HD.chmod(theFile)
	simplejson = __.imp('simplejson')
	if not p is None:
		printThis = p
	# print('*******************',theFile)
	if theFile.startswith('temp'+_v.slash):
		theFile = theFile.replace( 'temp'+_v.slash, '' )
		theFile = _v.stmp + _v.slash + theFile

	if indentCode:
		dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = simplejson.dumps(rows)

	# dataDump = simplejson.dumps(rows, indent=4, sort_keys=sort_keys)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	HD.chmod(theFile)
	if printThis:
		print('Saved: ' + theFile)
	if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );


def d2json( data, sort_keys=False ):
	simplejson = __.imp('simplejson')
	# saveTable2( data, _v.json_temp )
	# txt = getText( _v.json_temp, raw=True )

	return simplejson.dumps(data, indent=4, sort_keys=sort_keys)


def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
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
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

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


def percentageDiffIntAuto( smaller, bigger, isFloat=False ):
	if smaller < bigger:
		s = smaller
		b = bigger
	else:
		s = bigger
		b = smaller
	if not isFloat:
		return percentageDiffInt(s, b)
	else:
		result = round(float((s/b)*100), 1)
		r = str(result)
		if '.0' in r:
			result = int(result)
		return result


def get_change(current, previous):

	if current == previous:
		return 100.0

	if current < previous:
		c = current
		p = previous
	else:
		p = current
		c = previous     

	try:
		return (abs(c - p) / p) * 100.0
	except ZeroDivisionError:
		return 0


def patternMatch( one, two, best=True, simple=True, both=False, unsorted=False ):
	# simple=True
	result = []
	result.append( testPatterns( one, two, simple ) )
	result.append( testPatterns( two, one, simple ) )
	if type(both) == int and both == 2:
		return result
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
		data = generatePatterns2( one, 2 )
		# data = generatePatterns( one, 2 )
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


def generatePatterns( string, patternLength=2 ):

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
							dataset.sort()
							data.append( dataset )
							# print( ''.join( dataset ) )
						dataset = []


	l = len( string )
	data = []
	genP( patternLength )
	return data


def generatePatterns2( data, patternLength=2 ):
	records = []
	m = len(data)
	for n in range(0,len(data)):
		# a = n-1
		good = True
		pl = 0
		rec = []
		new = n
		while not pl == patternLength:
			if not new < m:
				good = False
			rec.append( new )
			new+=1
			pl+=1
		b = n
		c = n+1
		# if a > -1:
		#   records.append([ a,b ])
		# if c < m:
		if good:
			records.append( rec )
	return records


def positiveResults(string,plus='',plusOr=False,end=None):
	global switches

	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus').copy()
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
		
	pi = []
	for x in plusInput:
		pi.append( ci(x) )
	plusInput = pi
	del pi
	if type( plusInput ) == str:
		if not switches.isActive('StrictCase'):
			plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			if not switches.isActive('StrictCase'):
				plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	if not switches.isActive('StrictCase'):
		string = string.lower()
	# print( plusList )
	# sys.exit()
	for s in plusList:
		if not switches.isActive('StrictCase'):
			s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not switches.isActive('PlusDuplicate') and (  not string.find(ci(s)) == -1 or s in string  ):
			cnt += 1
		elif switches.isActive('PlusDuplicate') and (  string.count(ci(s)) > 1 or string.count(s) > 1 ):
			cnt += 1
		# if 'opus' in string:
		#   print(cnt, string)
		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result


def stripColor(text):
	if '0m' in text and '[' in text:
		pass
	else:
		return text
	import re
	ansi_escape = re.compile(r'''
		\x1B  # ESC
		(?:   # 7-bit C1 Fe (except CSI)
			[@-Z\\-_]
		|     # or [ for CSI, followed by a control sequence
			\[
			[0-?]*  # Parameter bytes
			[ -/]*  # Intermediate bytes
			[@-~]   # Final byte
		)
	''', re.VERBOSE)
	return ansi_escape.sub('', text)


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


def caseUnspecific( data, subject, isPlus=False, minus=None ):

	if not minus is None:
		if type(minus) == list:
			for remove in minus:
				for deleteThis in caseUnspecific( data, remove.lower(), isPlus=False ):
					data = data.replace( deleteThis, '' )
		elif type(minus) == str:
			for deleteThis in caseUnspecific( data, minus.lower(), isPlus=False ):
				data = data.replace( deleteThis, '' )

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


def plusColor( row, color='green' ):
	# row = thePrintLine

	if switches.isActive('Plus'):
		thePrintLine = row
		for plusSearchX in switches.values('Plus'):
			plusSearchX = ci( plusSearchX )

			for subject in caseUnspecific( row, plusSearchX ):
				row = thePrintLine.replace( subject, colorThis( subject, color , p=0 ) )

	return row


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


def colorizeRow( row, tableID=False, prefix='', prefixColor='', haltColorShift=False ):
	global colorizeRow_last
	if len(prefix) and len(prefixColor):
		prefix = colorThis( prefix, prefixColor, p=0 )
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
		if colorizeRow_last is None or not haltColorShift:
			colorizeRow_last = colorID( tableID, up )
		print( prefix + colorizeRow_last + row + Background.end )


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


def printVarColor( data ):
	_code = regImp( __.appReg, '_rightThumb._auditCodeBase' )
	validator = _code.imp.Validator()

	# index = validator.createIndex( data, 'javascript' )
	# validator.colorPrint_old()
	# print(data)
	index = validator.createIndex( data, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	# printVarSimple(validator.identity)
	# index = validator.createIndex( data, 'javascript', simple=False, B=True )
	validator.colorPrint()


def printVarSimple( data, sort_keys=False, isDic=None, prefix=None, remove=None ):
	data = json_clean(data)
	if not isDic is None and isDic and type(data) == str:
		saveText( data, _v.myTemp + _v.slash+'printVarSimple.json' )
		data = getTable2( _v.myTemp + _v.slash+'printVarSimple.json' )
	printVarOld( data, sort_keys, prefix=prefix, remove=remove )


def printVarOld( data, sort_keys=False, prefix=None, remove=None ):
	result = d2json( data, sort_keys )
	# result = type( result )
	result = printVarColor_OLD( result )
	if not remove is None:
		for x in remove:
			result = result.replace(x,'')
	if prefix is None:
		print( result )
	else:
		for x in result.split('\n'):
			print( prefix+x )


def printVarColor_OLD( data ):
	result = ''
	for char in data:
		result += printVarColorChar( char )
	return result


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


def getTable2( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	if theFile.lower().endswith('.index') or theFile.lower().endswith('.indexes'):
		isDic = True
	if os.path.isfile(theFile):
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def saveText( rows, theFile, errors=True, me=0 ):
	HD.chmod(theFile)
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
		try:
			open(theFile, 'wb').write(rows)
		except Exception as e:
			try:
				open(theFile, 'w').write(rows)
			except Exception as e:
				new_text = ''
				for x in rows:
					if x in _str.printable:
						new_text+=x
				open(theFile, 'w', encoding='utf-8').write(new_text)
		HD.chmod(theFile)
		# if errors:
		#   print( 'Auto correction when saving text' )
	if me and theFile in v.opened_file_me: changeM( theFile, v.opened_file_me[theFile] );


def json_clean(obj):
	if hasattr(obj, '__class__') and '.'  in str(obj.__class__):
		obj = dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__'))
		obj = prep4JSON(obj)
	return obj


def prep4JSON(d, to_delete=None):
	# remove keys from multidimensional dicts and lists
	def autoFindKeys(d):
		# removes functions and methods
		global autoFindKeys_temp
		if isinstance(d, dict):
			for k in d.keys():
				t = type( d[k] )
				if 'function' in str(t):
					autoFindKeys_temp.append( k )
				elif 'method' in str(t):
					autoFindKeys_temp.append( k )
				
			for k, v in d.items():
				autoFindKeys(v)
		elif isinstance(d, list):
			for i in d:
				autoFindKeys(i)
		return d

	if to_delete is None:
		global autoFindKeys_temp
		autoFindKeys_temp = []
		autoFindKeys(d)
		return prep4JSON(d, to_delete=autoFindKeys_temp)

	if isinstance(to_delete, str):
		to_delete = [to_delete]
	if isinstance(d, dict):
		for single_to_delete in set(to_delete):
			if single_to_delete in d:
				d[single_to_delete] = ' ** removed ** '
		for k, v in d.items():
			prep4JSON(v, to_delete)
	elif isinstance(d, list):
		for i in d:
			prep4JSON(i, to_delete)
	return d


class regImp:

	def __init__( self, focus, app, argvProcessForce=False, dirty=False ):
		global regImps
		global appInfo

		regImps[focus] = {}

		# self.functions = autoKwargsGetArgsFromApp(app)

		self.app = app
		self.parent = focus
		# print( 'self.imp = importlib.import_module', app )
		self.imp = importlib.import_module(app)
		# self.imp = importlib.util.spec_from_file_location( app, _v.py + _v.slash + app + '.py' )
		# print( os.path.isfile( _v.py + _v.slash + app + '.py' ) )
		# print( self.imp )
		# print( self.imp.test )
		# sys.exit()
		# print(self.imp.focus())

		self.focus = self.imp.focus( parentApp=focus )
		self.focusPop = focus
		
		self.saveLog = True

		
		self.imp.registerSwitches( argvProcessForce=False)

		appInfo[self.imp.focus(focus)] = appInfo[self.imp.focus()]
		appData[self.imp.focus(focus)] = appData[self.imp.focus()]
		__.constructRegistration(appInfo[self.imp.focus(focus)]['file'],self.imp.focus(focus))

		regImps[focus] = {}
		regImps[focus][app] = self.imp

		__.appReg = self.focusPop

		if dirty   and   not self.focus == '__init___-___init__':
			self.imp.appDBA = self.focus


		# self.provideImport()

	def provideImport( self ):
		return self.imp

	def listFunctions( self ):
		self.functions
		for func in self.functions:
			print( func['name'], func['args'] )

	def pipe( self, data=[], xfer=False, clear=True, appReg=False ):
		global appData
		if type(data) == bool:
			return appData[self.focus]['pipe']

		if type(appReg) == bool:
			appReg = self.focusPop

		if not len( data ):
			if xfer:
				data = appData[appReg]['pipe']
				if clear:
					appData[appReg]['pipe'] = []

		appData[self.focus]['pipe'] = data

		try:
			appData[self.focus]['data']['table']['received']
			
			profile = _profile.records.audit( 'pipe', data, appReg=[appReg,self.focus] )
			appData[appReg]['data']['table']['sent'].append( profile )
			appData[self.focus]['data']['table']['received'].append( profile )
		except Exception as e:
			pass

	def switch( self, names, value=None, appReg=False, delete=False,        d=False ):
		global appData
		global switches

		if type(appReg) == bool:
			appReg = self.focusPop

		for name in names.split(','):
			vl = value
			if name == 'Password':
				vl = '*******'
			if not value is None:
				try:
					appData[self.focus]['data']['field']['received']
					profile = _profile.records.audit( name, vl, appReg=[appReg,self.focus] )
					appData[appReg]['data']['field']['sent'].append( profile )
					appData[self.focus]['data']['field']['received'].append( profile )
				except Exception as e:
					pass


			# print(self.focus)
			__.appReg = self.focus

			if delete or d:
				switches.fieldSet( name, 'active', False )

			else:

				switches.fieldSet( name, 'active', True )

				# if not type ( value ) == bool:
				if not value is None:
					if type( value ) == list:
						switches.fieldSet( name, 'values', value )
						switches.fieldSet( name, 'value', ','.join(value) )
					else:
						switches.fieldSet( name, 'value', value )
						switches.fieldSet( name, 'values', [value] )


		__.appReg = self.focusPop

	def deleteSwitch( self, name ):
		global switches
		__.appReg = self.focus

		switches.fieldSet( name, 'active', False )

		__.appReg = self.focusPop

	def action( self, focusPop=True ):
		__.appReg = self.focus

		result = self.imp.action()

		if focusPop:
			__.appReg = self.focusPop

		return result


	def do( self, func, arg=False, focusPop=True ):

		__.appReg = self.focus

		if type( func ) == str:
			theFunction = eval( 'self.imp.' + func )
		else:
			theFunction = func

		if type( arg ) == bool:
			result = theFunction()
		elif type( arg ) == dict:
			result = theFunction(**arg)
		elif type( arg ) == list:
			result = theFunction(*arg)
		else:
			result = theFunction(arg)

		

		if focusPop:
			__.appReg = self.focusPop

		return result

	def execute( self, func, arg=False, nofocus=False ):
		global threads
		theFunc = eval('self.imp.'+func)

		shouldRun = True
		if not nofocus and  type(arg) == bool:
			args = [ self.focus ]
		elif not nofocus and  not type(arg) == bool:
			args = [ arg, self.focus ]

		if nofocus and  type(arg) == bool:
			shouldRun = False
			theID = threads.add( 'execute', theFunc, loaded=True )
		elif nofocus and  not type(arg) == bool:
			args = [ arg ]


		if shouldRun:

			theID = threads.add( 'execute', theFunc, args, loaded=True )

		# if self.saveLog:
		# else:
		#   theID = threads.add( 'execute', theFunc, [ arg, self.focus ], trigger=saveThreadsLog, loaded=True )

		return theID


def autoKwargsGetArgsFromApp(app):
	if not '.py' in app:
		app = app + '.py'
	appText = getText(_v.myAppsPy + _v.slash + app)
	func = []
	for row in appText:
		if 'def ' in row:
			fr = row.split('def ')[1].replace(' ','')
			name = fr.split('(')[0]
			if name+'():' in fr:
				args = []
			else:
				tmp = fr.replace(name+'(','')
				arg = tmp.split('):')[0]
				args = []
				for x in arg.split(','):
					if '=' in x:
						args.append( { 'arg': x.split('=')[0], 'default': x.split('=')[1] } )
					else:
						args.append( { 'arg': x, 'default': '' } )


			func.append( { 'name': name, 'args': args } )
	return func


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
	result = _str.cleanBE( result, ',' )
	return result


def payloadCache( data, file=None, theFocus=None ):
	# _.payloadCache( saveFile, __file__, focus() )
	
	if theFocus is None:
		theFocus = __.appReg
	if file is None:
		appDBA = __.thisApp( __.postLoadFile )
	else:
		appDBA = __.thisApp( file )
	releaseAcquiredData( appDBA, theFocus, data )


def releaseAcquiredData( appDBA, theFocus, payload=None ):
	if appDBA == '__init__':
		return None
	if not __.releaseAcquiredData:
		return None
	if not os.name == 'nt':
		return None
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
				'session': _v.session(),
				'rebuiltCommand': rebuiltCommand,
				'rebuiltCommandEpoch': rebuiltCommandEpoch,
				'files': [],
				'switches': switches.getTable(),
				'errors': [],
	}
	if not payload is None:
		info['payload'] = payload

	if not autoBackupData:
		saveTable2( info, log )

	if autoBackupData:
		if len( myFileLocation_Files ):
			for i,file in enumerate(myFileLocation_Files):
				if os.path.isfile(file):
					thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_file' + str(i) + '.cache'
					import _rightThumb._dir as _dir
					dirRecord = _dir.info( file, mime=True )
					info['errors'] = []
					fileError = 'Error: File is ' + dirRecord['mime'] + ' and ' + dirRecord['size']
					try:
						if dirRecord['mime'] == 'Text' and dirRecord['bytes'] < 5242880:
							tmpData = getText( file )
							saveText( tmpData, _v.myAppLogs + _v.slash + thisName )
							info['files'].append( thisName )
						else:
							info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })
							saveText( fileError, _v.myAppLogs + _v.slash + thisName )
							

					except Exception as e:
						info['errors'].append({ 'error': fileError, 'file': _v.myAppLogs + _v.slash + thisName })

		# print( theFocus, type( appData[theFocus]['pipe'] ) )
		# print('theFocus',theFocus)
		if not type( appData[theFocus]['pipe'] ) == bool:
			thisName = 'files-' + appDBA + '-' + str( __.startTime ) + '_pipe' + '.cache'
			saveText( appData[theFocus]['pipe'], _v.myAppLogs + _v.slash + thisName )
			# print(info)
			info['files'].append( thisName )
			
		

		saveTable2( info, log )


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


def unixAutoColumns( asset, columns, focus=None ):
	if not len(asset):
		return asset
		# return columns
	asset = asset.copy()
	# if __.thisOS == 'Windows':

	if not __.terminal.width:
		return columns

	cols = __.terminal.width
	if focus is None:
		focus = __.appReg
	global appInfo
	rec = {}
	for k in asset[0].keys():
		rec[k]=k
	asset.append( rec )
		# cols = 102
	reg = appInfo[focus]['columns'].copy()
	reg.reverse()
	importance = []
	for x in reg:
		importance.append(x['name'])
	# importance = [
	#               'date_accessed',
	#               'week_of_year',
	#               'date_created',
	#               'date_modified',
	#               'ext',
	#               'size',
	# ]
	fields.asset( 'asset', asset )
	lengths = fields.lengths( 'asset' )

	# printVarSimple( lengths )

	total = 3
	for col in columns.split(','):
		total+=3
		for key in lengths:
			if col.lower() == key.lower():
				total += lengths[key]
	# print( total, columns )
	# print( cols, type(cols) )
	nextDel = 0
	done = False
	newList = []
	while total > cols and not done:
		total = 3
		newCols = []
		for col in columns.split(','):
			if col == importance[nextDel]:
				if not col in newList:
					newList.append(col)
			if not col == importance[nextDel]:
				newCols.append(col)
				total+=3
				for key in lengths:
					if col.lower() == key.lower():
						total += lengths[key]
			columns = ','.join(newCols)
		nextDel += 1
		if not len(newCols):
			done=True
	pass
	if not len(columns):
		columns = newList[ len(newList)-1 ]
	# print( total, columns )


	# print( 'total:', total )

	# sys.exit()
	return columns


def myFileLocations( file, silent=False, currentBaseVersion=3 ):

	if not type( __.trigger_isPipe ) == bool:
		if 'glob' in __.trigger_isPipe:
			glob = __.imp('glob')
			g = glob.glob(file)
			for f in g:
				myFileLocations( f, silent, currentBaseVersion )
			file = g

	# print(__.myFileLocations_SKIP_VALIDATION)
	# print(os.path.isdir(file))
	# print(file)
	# sys.exit()
	global appData
	if __.myFileLocations_SKIP_VALIDATION:
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
		appData[__.appReg]['pipe'].append( file )
		return file
	# print( 'HERE HERE HERE HERE ', file )
	if '*' in file:
		import glob
		appData[__.appReg]['pipe'] = glob.glob(file)
		return appData[__.appReg]['pipe']

	global myFileLocation_File
	global backup_subject_files
	if type(__.myFileLocations_SKIP_VALIDATION) == bool and __.myFileLocations_SKIP_VALIDATION:
		# print('here')
		# sys.exit()
		if type( appData[__.appReg]['pipe'] ) == bool:
			appData[__.appReg]['pipe'] = []
			return None
		appData[__.appReg]['pipe'].append( file )
		return None
	# if ',' in file and not os.path.isfile( file ):
	#   nFiles = []
	#   for f in file.split(','):
	#       nFiles.append( myFileLocations2( f, silent, currentBaseVersion ) )
	#   file = ','.join( nFiles )
		
	# else:
	#   myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )

	myFileLocation_File = myFileLocations2( file, silent, currentBaseVersion )
	if  not myFileLocation_File in myFileLocation_Files:
		myFileLocation_Files.append( myFileLocation_File )
	try:
		autoAbbreviations()
	except Exception as e:
		pass
	if len( myFileLocation_Files ):
		# print('xxx')
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
					# if os.path.isfile( thisFile ):
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


def setPipeData( data, theFocus=False, clean=True ):
	global appData
	if type( theFocus ) == bool:
		theFocus = __.appReg
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		appData[theFocus]['pipe'] = []
		if not clean:
			appData[theFocus]['pipe'].append('')
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					appData[theFocus]['pipe'].append(pd)
			else:
				appData[theFocus]['pipe'].append(pd)
		setPipeDataRan = True


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


def myFileLocations2( file, silent=False, currentBaseVersion=3 ):
	if __.myFileLocations_SKIP_VALIDATION:
		return file
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
		return file

	probableLocations = [
		"_v.myAppsPy + _v.slash+'_rightThumb'+_v.slash + '_' + '*THEFILENAME*' + _v.slash+'__init__.py'",
		"_v.myAppsPy + _v.slash+''+_v.slash + '*THEFILENAME*' + '.py'",
		"_v.myAppsPy + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTables + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'batch'+_v.slash + '*THEFILENAME*' + '.bat'",
		"_v.myDatabases + _v.slash+''+_v.slash + '*THEFILENAME*'",

		"os.environ['USERPROFILE'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['USERPROFILE'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",

		"os.environ['HOME'] + _v.slash+'Desktop'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Documents'+_v.slash + '*THEFILENAME*'",
		"os.environ['HOME'] + _v.slash+'Downloads'+_v.slash + '*THEFILENAME*'",
		
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myTXT + _v.slash+''+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'exe'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'php'+_v.slash + '*THEFILENAME*' + '.php'",
		"_v.myApps + _v.slash+'powershell'+_v.slash + '*THEFILENAME*'",
		"_v.myApps + _v.slash+'vbs'+_v.slash + '*THEFILENAME*'",
	]

	if file == 'base':
		file = 'base' + str( currentBaseVersion )

	if True:
		for testThis in probableLocations:
			try:
				theTest = eval( testThis )
				# print()
				# print(theTest)
				theTest = theTest.replace( '*THEFILENAME*', file )
				# print(os.path.isfile( theTest ),theTest)
				if os.path.isfile( theTest ):
					if silentSetTo:
						
						print()
						print( 'File not here but in:', theTest )
						print()

					return theTest
			except Exception as e:
				pass
	
	if not os.path.isfile( _v.relevant_folders ):
		print( 'generateRelevantFolders' )
		import generateRelevantFolders
		generateRelevantFolders.action()

	if os.path.isfile( _v.relevant_folders ):
		for fld in getText( _v.relevant_folders, raw=True, clean=1 ).split('\n'):
			if os.path.isfile( fld  +_v.slash+  file ):
				return fld  +_v.slash+  file
			if 'ext' in __.specifications:
				if os.path.isfile( fld  +_v.slash+  file+ __.specifications['ext'] ):
					return fld  +_v.slash+  file
			# print(fld)

	return file


def myFolderLocations( data ):
	# print(data)
	if type(data) == list:
		for i,d in enumerate(data):
			data[i] = myFolderLocations(d)
		return data

	if os.path.isdir(data):
		return os.path.abspath(data)
	

	global bmIndex
	
	if not len(bmIndex):
		bmIndex = getTable( 'bookmarks.index' )

	# print( bmIndex )
	if data in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data])
	if data.lower() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.lower()])
	if data.upper() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.upper()])
	if data.title() in bmIndex['labels']:
		return _v.resolveFolderIDs(bmIndex['labels'][data.title()])


	return data


def urlTrigger(url):
	if not '.' in url:
		url = 'http://' + url + '.com'
	elif not url.startswith('http'):
		url = 'http://' + url
	return url


def timeAgo( do='', startDate=None ):

	try:
		do = float(do)
		return do
	except Exception as e:
		pass

	global timeAgoBase
	global timeAgoBaseCount
	if not len(timeAgoBase) and timeAgoBaseCount == 0:
		if ',' in do:
			timeAgoBase = do.split(',')
			# print(do)
			# sys.exit()
	timeAgoBaseCount += 1
	# print( do, friendlyDate(startDate) )
	if len(do) == 19 and do.count('-') == 2 and do.count(':') == 2:
		return autoDate( do )
	if len(do) == 16 and do.count('-') == 2 and do.count(':') == 1:
		return autoDate( do )
	if len(do) == 21 and do.count('-') == 4:
		result = []
		for x in do.split(','):
			result.append( timeAgo( x, startDate ) )
		return result
	if len(do) == 10 and do.count('-') == 2:
		ts = autoDate( do )
	else:
		if not do.startswith('+'):
			ts = timeAgo_past(do,startDate)
		elif do.startswith('+'):
			ts = timeFuture(do,startDate)


	if len(timeAgoBase) > 1 and do == timeAgoBase[1]:
		if timeAgoBaseCount == 3 or timeAgoBaseCount == 5 :
			pass
			ts += 86400-1
	# print( timeAgoBaseCount, ts )
	return ts


def timeFuture(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime

	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('+'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switches.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate + remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if 's' in do:
		units = do
		units = units.replace( 's', '' )
		units = int( units )
		return startDate + units


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
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		start_date = yearMath( startDate, nmb, do='+' )
	if 'm' in do:
		# start_date = dateMathEpoch( startDate, 30 * nmb, '+' )
		start_date = monthMath( startDate, nmb, do='+' )
	if 'w' in do:
		start_date = dateMathEpoch( startDate, 7 * nmb, '+' )
	if 'd' in do:
		start_date = dateMathEpoch( startDate, nmb, '+' )
	return start_date


def dateMathEpoch( epoch, theDays, do='+' ):
	# print(epoch, theDays)
	epoch = autoDate(epoch)
	# if do == '+':
	#   return epoch + ( theDays*86400 )
	# elif do == '-':
	#   return epoch - ( theDays*86400 )


	date0 = datetime.datetime.fromtimestamp((epoch))
	if do == '+':
		date1 = date0 + datetime.timedelta(days=theDays)
	elif do == '-':
		date1 = date0 - datetime.timedelta(days=theDays)
	else:
		print( "dateMathEpoch( epoch, theDays, do='+' )" )
		sys.exit()
	# print(date1.timestamp())
	return autoDate((date1.timestamp()))


def monthMath( thisDate, months, do='+' ):
	months = abs(months)
	# print( '040', thisDate, autoDate( thisDate ), friendlyDate(thisDate) )
	theDateParts = friendlyDate( autoDate( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	parts[1] = int(parts[1])
	parts[2] = int(parts[2])
	i = 0
	while not i == months:
		# print( months, 1, parts )
		if do == '+':
			parts[1]+=1
			if parts[1] == 13:
				parts[1] = 1
				parts[0] += 1
		elif do == '-':
			parts[1]-=1
			if parts[1] == 0:
				parts[1] = 12
				parts[0] -= 1
		i+=1
	# print( '048a' )
	bb = str(parts[1])
	cc = str(parts[2])
	# print( '048b' )
	if parts[1] < 10:
		bb = '0'+bb
	if parts[2] < 10:
		cc = '0'+cc
	# print( '048c' )
	text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
	# print( '049', text )
	result = autoDate(  text  )
	# print( '050a', text, type( result ) )
	while type( result ) == bool:

		parts[2]-=1

		bb = str(parts[1])
		cc = str(parts[2])
		if parts[1] < 10:
			bb = '0'+bb
		if parts[2] < 10:
			cc = '0'+cc
		text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
		result = autoDate(  text  )
		# print( '050b', text, type( result ) )



	# print( '050c', text )
	# print( '060', result )
	return result


def yearMath( thisDate, years, do='+' ):
	theDateParts = friendlyDate( autoDate( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	i = 0
	while not i == years:
		if do == '+':
			parts[0] += 1
		elif do == '-':
			parts[0] -= 1
		i+=1
				

	return autoDate(  str(parts[0])+'-'+parts[1]+'-'+parts[2] +' '+ theDateParts[1] )


def resolveEpochTest( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	import _rightThumb._date as _date
	return _date.resolveEpoch( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )


def timeAgo_past(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime
	# return do
	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('-'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = switches.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate - remove  
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  


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
		# start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
		# start_date = dateMathEpoch( startDate, 365 * nmb, '-' )
		start_date = yearMath( startDate, nmb, do='-' )
	if 'm' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
		# start_date = dateMathEpoch( startDate, 30 * nmb, '-' )
		start_date = monthMath( startDate, nmb, do='-' )
	if 'w' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
		start_date = dateMathEpoch( startDate, 7 * nmb, '-' )
	if 'd' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
		start_date = dateMathEpoch( startDate, nmb, '-' )
	return start_date


def rstr(code,o,c):
	i=o-1
	txt=''
	while not i == c:
		i+=1
		txt+=code[i]
	return txt

defaultScriptTriggers_run = False

Switchesswitches = Switches()
ciData = (  
			[ '_;192A;_',   ',' ],
			[ '_;192B;_',   ':' ],
			[ ';;',         ',' ],
			[ ';c',         ',' ],
			
			[ ';_',         '-' ],
			[ ';-',         '-' ],

			[ ';p;',        '%' ],
			[ ';p',         '%' ],
			[ ';.',         ':' ],
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
			[ '[s]',        '$' ],
			[ '[eq]',       '=' ],
			[ ';opar;',     '[' ],
			[ '[pipe]',     '|' ],
			[ '[p]',     '|' ],
			[ '[htmlopen]', '<' ],
			[ '[htmlclose]','>' ],
			[ '[gtr]',      '>' ],
			[ '[lss]',      '<' ],
			[ ';6',         '^' ],
			[ ';+',         '+' ],

			[ '+--+c',          '--c' ],

			[ '[semi]',         ';' ],
			
			[ '[caret]',    '^' ]  )
plusClose = 70

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
ipsum = None

appData = {}
appInfo = {}
changeDate_Table = None

_dir = None

touch_meta = None

date_datetime = None

app_full_color_index = None

row_colors = []
row_colors_ID = 0

colorizeRow_last = None

regImps = {}
Queuethreads = Queue()
autoBackupData = False

myFileLocation_Files = []
myFileLocation_File = False

backup_subject_files = True

printAutoAbbreviations_scheduled = False

myFileLocation_Print = True

bmIndex = []
timeAgoBase = []
timeAgoBaseCount = 0

isTime = False





