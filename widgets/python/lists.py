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

import numpy
import os
import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('File1', '-f1','file1.txt')
_.switches.register('File2', '-f2','file2.txt')

_.appInfo=    {
	'file': 'lists.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p lists -f1 file1.txt -f2 file2.txt')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
def action():
	file1Raw = []

	file1 = []
	file2 = []
	files = []
	files2 = []
	good = []
	bad = []
	f1 = _.switches.value('File1')
	f2 = _.switches.value('File2')
	threshold = 90 
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	def diff(a,b):
		try:
			if a > b:
				result = (b/a)*100
			elif a == b:
				result = 100
			else:
				result = (a/b)*100
		except Exception as e:
			result = 0
		return result
	if os.path.isfile(f1) == True:
		with open(f1,  'r', encoding='latin-1') as f:
			for line in f:
				data = {}
				line = line.replace('\n','')
				file1Raw.append(line)
				data = {'line': line}
				i=0
				for c in chars:
					cnt = line.lower().count(c)
					i+=cnt
					data[c] = cnt
				if i > 2:
					file1.append(data)
					files.append(line)
					files2.append(line)
			f.close()
	if os.path.isfile(f2) == True:
		with open(f2,  'r', encoding='latin-1') as f:
			for line in f:
				data = {}
				line = line.replace('\n','')
				data = {'line': line}
				i=0
				for c in chars:
					cnt = line.lower().count(c)
					# print(cnt)
					i+=cnt
					data[c] = cnt
				if i > 2:
					file2.append(data)
					files.append(line)
			f.close()
	if len(file1) < len(file2):
		tmp2 = file2
		tmp1 = file1
		file1 = tmp2
		file2 = tmp1
		del tmp1
		del tmp2
	# print(file1)
	# print(file2)
	def mostProbable(row):
		t = []
		for d in file2:

			a = []
			for c in chars:
				calcDiff = diff(d[c],row[c])
				# if calcDiff > -1:
				a.append(calcDiff)
			t.append({'line': d['line'], 'rank': numpy.mean(a)})
		ttt = sorted(t, key=lambda k: k['rank']) 
		# for tt in ttt:
		#     print(tt['rank'],tt['line'])
		# sys.exit()
		return ttt[len(ttt)-1]
	
	for ff in file1:
		probableMatch = mostProbable(ff)
		# print(probableMatch)
		is_100 = []
		if probableMatch['rank'] > threshold:
			if not probableMatch['line'] in is_100 and not ff['line'] in is_100:
				if int(round(probableMatch['rank'])) == 100:
					# print( probableMatch['line'] )
					is_100.append( probableMatch['line'] )
				good.append({'list1':ff['line'],'list2':probableMatch['line'],'rank':int(round(probableMatch['rank']))})
		else:
			bad.append({'list1':ff['line'],'list2':probableMatch['line'],'rank':int(round(probableMatch['rank']))})
	_.tables.register('good',good)
	_.tables.register('bad',bad)
	_.tables.fieldProfileSet('bad','_header_','alignment','center')
	_.tables.fieldProfileSet('good','_header_','alignment','center')
	_.switches.fieldSet('Long','active',True)
	_.switches.fieldSet('Sort','active',True)
	_.switches.fieldSet('Sort','value','d;.rank')
	print()
	print('GOOD:',len(good))
	_.tables.print('good','list1,list2,rank')
	print()
	print()
	print('BAD:',len(bad))
	_.tables.print('bad','list1,list2,rank')
	print()
	print()
	print('Not 100%')
	print()
	the100 = []
	for item in good:
		if item['rank'] == 100:
			the100.append( item['list1'] )

	for item in file1Raw:
		if not item in the100:
			print( item )


	# missing = []
	# for bad in files:
	#     if not bad in files2:
	#         missing.append(bad)
	# print('Missing:',len(missing))
	# for m in missing:
	#     print(m)
	# totalDif = 0
	# if len(file1) > len(file2):
	#     totalDif = len(file1) - len(file2)
	# else:
	#     totalDif = len(file2) - len(file1)
	# print()
	# print(len(file1),len(file2), totalDif)
########################################################################################
if __name__ == '__main__':
	action()





