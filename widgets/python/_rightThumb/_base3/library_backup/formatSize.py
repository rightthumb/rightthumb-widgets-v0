
def formatSize(size,what=None):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if what is None:

		if size == None:
			result = ''
		elif size < 1024:
			result = str(size) + ' B'
		elif size >= 1024 and size < 1048576:
			num = round(size / 1024, 2)
			result = str(num) + ' KB'
		elif size >= 1048576 and size < 1073741824:
			num = round(size / 1048576, 2)
			result = str(num) + ' MB'
		elif size >= 1073741824 and size < 1099511627776 :
			num = round(size / 1073741824, 2)
			result = str(num) + ' GB'
		elif size >= 1099511627776 and size < 1125899906842624 :
			num = round(size / 1099511627776, 2)
			result = str(num) + ' TB'
		elif size >= 1125899906842624 and size < 1152921504606847000 :
			num = round(size / 1125899906842624, 2)
			result = str(num) + ' PB'
		elif size >= 1152921504606847000 and size < 1180591620717411303424 :
			num = round(size / 1152921504606847000, 2)
			result = str(num) + ' EB'
		elif size >= 1180591620717411303424 and size < 1208925819614629174706176 :
			num = round(size / 1180591620717411303424, 2)
			result = str(num) + ' ZB'
		else:
			num = round(size / 1208925819614629174706176, 2)
			result = str(num) + ' YB'

	elif not what is None:
		what=what.upper()
		if size == None:
			result = ''
		elif what == 'B':
			result = str(size) + ' B'
		elif what == 'KB':
			num = size / 1024
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' KB'
		elif what == 'MB':
			num = size / 1048576
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' MB'
		elif what == 'GB':
			num = size / 1073741824
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' GB'
		elif what == 'TB':
			num = size / 1099511627776
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' TB'
		elif what == 'PB':
			num = size / 1125899906842624
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' PB'
		elif what == 'EB':
			num = size / 1152921504606847000
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' EB'
		elif what == 'ZB':
			num = size/1180591620717411303424
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' ZB'
		elif what == 'YB':
			num = size / 1208925819614629174706176
			test = str(num)
			if '.' in test:
				roun=2
				x=test.split('.')[1]
				for y in x:
					if y == '0':
						roun+=1
					else:
						break
				pass
				num=round(num,roun)
			result = str(num) + ' YB'
		else:
			result = str(size) + ' B'
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''
	# 1152921504606846976
	if False:
		pass



	elif 'YB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size:
		factor = 1152921504606847000
	elif 'PB' in size:
		factor = 1125899906842624
	elif 'TB' in size:
		factor = 1099511627776
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024

	else:
		factor = 1
	size2 = ''
	for c in size:
		if c in '0123456789.':
			size2+=c
	size = size2
	# size = size.replace('X','')
	# size = size.replace('Y','')
	# size = size.replace('Z','')
	# size = size.replace('E','')
	# size = size.replace('P','')
	# size = size.replace('T','')
	# size = size.replace('B','')
	# size = size.replace('M','')
	# size = size.replace('K','')
	# size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)

	result = round(size * factor,0)
	# print_( size, factor )
	# result = size * factor
	return int(result)

def unFormatSize2(size):
	size = str(size)
	# size = size.upper()
	factor = ''
	# 1152921504606846976

	bity=False
	if False:
		pass



	elif 'YB' in size or 'yB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size or 'zB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size or 'eB' in size:
		factor = 1152921504606847000
	elif 'PB' in size or 'pB' in size:
		factor = 1125899906842624
	elif 'TB' in size or 'tB' in size:
		factor = 1099511627776
	elif 'GB' in size or 'gB' in size:
		factor = 1073741824
	elif 'MB' in size or 'mB' in size:
		factor = 1048576
	elif 'KB' in size or 'kB' in size:
		factor = 1024




	elif 'Yb' in size or 'yb' in size or 'ybit' in size.lower():
		bity=True
		factor = 1000000000000000000000000
	elif 'Zb' in size or 'zb' in size or 'zbit' in size.lower():
		bity=True
		factor = 1000000000000000000000
	elif 'Eb' in size or 'eb' in size or 'ebit' in size.lower():
		bity=True
		factor = 1000000000000000000
	elif 'Pb' in size or 'pb' in size or 'pbit' in size.lower():
		bity=True
		factor = 1000000000000000
	elif 'Tb' in size or 'tb' in size or 'tbit' in size.lower():
		bity=True
		factor = 1000000000000
	elif 'Gb' in size or 'gb' in size or 'gbit' in size.lower():
		bity=True
		factor = 1000000000
	elif 'Mb' in size or 'mb' in size or 'mbit' in size.lower():
		bity=True
		factor = 1000000
	elif 'Kb' in size or 'kb' in size or 'kbit' in size.lower():
		bity=True
		factor = 1000

	else:
		factor = 1
	size2 = ''
	for c in size:
		if c in '0123456789.':
			size2+=c
	size = size2
	# size = size.replace('X','')
	# size = size.replace('Y','')
	# size = size.replace('Z','')
	# size = size.replace('E','')
	# size = size.replace('P','')
	# size = size.replace('T','')
	# size = size.replace('B','')
	# size = size.replace('M','')
	# size = size.replace('K','')
	# size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)

	result = round(size * factor,0)
	if 0 and bity:
		result = result /8
	# print_( size, factor )
	# result = size * factor
	rt = str(result)
	if rt.endswith('.0'):
		return int(result)
	return result



def to_bytes(size_str):
	if 'Kb' in size_str: size_str = size_str.replace('Kb', 'kbit')
	if 'Mb' in size_str: size_str = size_str.replace('Mb', 'mbit')
	if 'Gb' in size_str: size_str = size_str.replace('Gb', 'gbit')
	if 'Tb' in size_str: size_str = size_str.replace('Tb', 'tbit')
	if 'Pb' in size_str: size_str = size_str.replace('Pb', 'pbyte')
	if 'Eb' in size_str: size_str = size_str.replace('Eb', 'ebyte')
	if 'Zb' in size_str: size_str = size_str.replace('Zb', 'zbyte')
	if 'Yb' in size_str: size_str = size_str.replace('Yb', 'ybyte')

	size_str = size_str.lower()
	unit_map = {
		'b': 1,
		'kb': 1024,
		'mb': 1024**2,
		'gb': 1024**3,
		'tb': 1024**4,
		'pb': 1024**5,
		'eb': 1024**6,
		'zb': 1024**7,
		'yb': 1024**8,
		'byte': 1,
		'kbyte': 1024,
		'mbyte': 1024**2,
		'gbyte': 1024**3,
		'tbyte': 1024**4,
		'pbyte': 1024**5,
		'ebyte': 1024**6,
		'zbyte': 1024**7,
		'ybyte': 1024**8,
		'kbit': 1024/8,
		'mbit': 1024**2/8,
		'gbit': 1024**3/8,
		'tbit': 1024**4/8,
		'pbit': 1024**5/8,
		'ebit': 1024**6/8,
		'zbit': 1024**7/8,
		'ybit': 1024**8/8,
		'bit': 1/8
	}
	try:
		size, unit = size_str.split()
		size = float(size)
		if unit[-1] in ['b', 'e', 't', 'p', 'z', 'y']:
			unit = unit[:-1]
		if unit[-1] == 'k':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'm':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'g':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 't':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'p':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'e':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'z':
			unit = unit[:-1] + 'byte'
		elif unit[-1] == 'y':
			unit = unit[:-1] + 'byte'
		return int
	except:
		raise ValueError(f'Invalid size string: {size_str}')