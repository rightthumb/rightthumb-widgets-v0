

def dic_key_sort2( table, n=False, ip=False, r=False ):


	keys = list( table.keys() )
	dic = {}
	theData = []
	if ip:
		fields.register( 'cnt-ip', 'val', 7, m=3 )
		for x in keys:

			if not x.count('.') == 3:
				theData.append( x )
			else:
				zZz = []

				for y in x.split('.'):
					xXx = fields.padZeros( 'cnt-ip', 'val', int(y) )
					# print_(xXx)

					zZz.append( xXx )
				theData.append( '.'.join(zZz) )
		theData.sort()
		if r:
			theData.reverse()
		for x in theData:
			y = ''
			zZz = []
			if not x.count('.') == 3:
				y = x
			elif x.count('.') == 3:
				for y in x.split('.'):
					# print_(y)
					zZz.append( str(int(y)) )
				y = '.'.join(zZz)
				# print_(y)
			if y in table:
				dic[y] = table[y]
		# print_(theData)
		# printVarSimple(dic)
		# print_()
		return dic



	if not n:
		keys.sort()
		if r:
			keys.reverse()

		for x in keys:
			dic[x] = table[x]
		return dic
	else:
		nKeys = []
		fields.register( 'cnt-n', 'val', 7, m=40 )
		for k in keys:
			nKeys.append(  fields.padZeros( 'cnt-n', 'val', int(k) )  )
		nKeys.sort()
		if r:
			nKeys.reverse()

		for x in nKeys:
			dic[  str(int(x))  ] = table[str(int(x))]
		return dic