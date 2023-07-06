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

# import os
import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import re

_.switches.register('GenerateData', '-generate')
_.switches.register('GenerateTopicList', '-topics')

_.appInfo=    {
	'file': 'bibleGateTopicProcess.py',
	'description': 'Process bibleGateTopic data (biblegateway.json)',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p bibleGateTopicProcess -generate')
_.appInfo['examples'].append('p bibleGateTopicProcess')
_.appInfo['examples'].append('p bibleGateTopicProcess -topics')



_.switches.process()




########################################################################################

errors = []
def action():
	global books
	global errors
	if _.switches.isActive('GenerateData'):
		books = []
		booksRaw = _.getText(_v.myTables + _v.slash+'bible_books.csv')
		verses = _.getText(_v.myTables + _v.slash+'bibleRef_books2.txt')
		# topics = _.getTable('biblegateway.json')
		
		for i,bR in enumerate(booksRaw):
			if ',' in bR:
				b = bR.split(',')[0]
				a = bR.split(',')[1].replace('\n','').replace('.','')
				res = {'id': i+1, 'name': b, 'abbrev': a}
				books.append(res)
				# #####x  print(res)

		# for bX in books:
		#     #####x  print(bX)
		maxChapter = []
		maxVerse = []
		last0 = ''
		last1 = ''
		last = ['','','']
		check = ['','','']
		nu = 0
		for vS in verses:
			check[0] = vS.split(':')[0]
			check[1] = check[0].split(',')[0]
			check[2] = vS.split(':')[1].replace('\n','')
			# #####x  print(check1)
			try:
				ch = last[0].split(',')[1]
			except Exception as e:
				ch = ''
			if not last[0] == check[0]:
				if not nu == 0:
					maxVerse.append({'book': int(nu), 'chapter': int(ch), 'verses': int(last[2])})
					# #####x  print(nu,ch,last[2])
			if not last[1] == check[1]:
				if not nu == 0:
					maxChapter.append({'book': int(nu),'chapters': int(ch)})
					# #####x  print(nu,last[0],books[nu-1]['name'])
					# #####x  print(nu,ch)
				nu += 1
				# maxVerse = []
			last[0] = check[0]
			last[1] = check[1]
			last[2] = check[2]

		for i,bX in enumerate(books):
			books[i]['chapters'] = maxChapter[i]['chapters']
			mVi = 0
			mCv = []
			for mV in maxVerse:
				if mV['book'] == bX['id']:
					mCv.append({'chapter': mV['chapter'], 'verses': mV['verses']})
					# #####x  print(bX['id'],mV['verses'],mVi)
					mVi += mV['verses']
			books[i]['verses'] = mVi
			books[i]['chapter_verses'] = mCv
		_.saveTable(books,'bible_chapter_verse_meta.json')




	if not _.switches.isActive('GenerateData') and not _.switches.isActive('GenerateTopicList'):
		topics = _.getTable('biblegateway.json')
		books = _.getTable('bible_chapter_verse_meta.json')
		global book_Lf
		global book_La

		book_Lf = []
		book_La = []
		for bK in books:
			book_Lf.append(bK['name'].replace(' ','').lower())
			book_La.append(bK['abbrev'].replace(' ','').lower())
		newTopics = []
		for i,tCs in enumerate(topics):
			result = []
			dataSets = []
			preProcess = tCs['vs']
			preProcess = preProcess.replace('13 Kings','1 Kings').replace('with','').replace('141 Chronicles','1 Chronicles').replace('15 Samuel','1 Samuel').replace('27 Chronicles','2 Chronicles').replace('83 Kings','2 Kings').replace('83 Chronicles','1 Chronicles').replace('8 John 3:22','1 John 3:22').replace('6 Corinthians 2:7','2 Corinthians 2:7').replace('6 Peter 1:8','1 Peter 1:8').replace('7 Kings 13:','1 Kings 13:')
			# preProcess = _str.cleanSpecial(preProcess)
			# ATONEMENT 6 Peter
			preProcess = preProcess.replace(' ','').lower()
			# if '9:1,17;10:20,21' in preProcess:
			#     preProcess = '20samuel9:1,17;10:20,21'
			# #####x  print('**',preProcess)
			# if i == 0:
			result_found = False
			result_error = False

			if True:
				# #####x  print(preProcess)
				#####x  print(tCs)
				# #####x  print()
				last = ''
				new_TopicsBuild = ''
				for pI in preProcess.split(';'):
					pI = _str.cleanBE(pI,'-')
					pI = _str.cleanBE(pI,':')
					# pI = pI.replace('20samuel','1samuel')
					# pI = pI.replace('4chronicles11:6','2chronicles11:6')
					# pI = pI.replace('4kings7:21','1kings7:21')
					# pI = pI.replace('26samuel24:1-9','2samuel24:1-9')
					# pI = pI.replace('51chronicles21:1-7','1chronicles21:1-7')
					# pI = pI.replace('4samuel23','2samuel23')
					# pI = pI.replace('51kings7:8-10','2kings7:8-10')
					#####x  print(pI)
					nameCheck = pI.replace(':','').replace('-','').replace(',','')
					# #####x  print(nameCheck)
					good = True
					# if nameCheck == 'chronicles' or nameCheck == 'samuel' or nameCheck == 'timothy':
					if not hasNumbers(nameCheck):
						good = False

					if len(nameCheck) == 1:
						try:
							int(nameCheck)
							good = True
						except Exception as e:
							good = False
					# if not good:
					#     print(pI)
						# try:
						#     nx = books[last-1]['name'] + ' ' +  pI
						#     pI = nx
						#     good = True
						# except Exception as e:
						#     pass

					if good:
						if len(nameCheck) > 0:
							try:
								twoA = int(nameCheck)
								hasAlpha = False
							except Exception as e:
								hasAlpha = True
							try:
								if hasAlpha:
									# #####x  print('Alpha')
									data0 = lineProcess(pI,tCs)
									last = data0[0]
								else:
									# #####x  print('Numeric')
									data0 = [last,pI]
								dataSets.append(data0)
								do = expandRef(data0)
								for rdo in do:
									result.append(rdo)
								# tCs['ref'] = do
								# newTopics.append(tCs)
								new_TopicsBuild += books[data0[0]-1]['name'] + ' ' + str(data0[1]) + '; '
								result_found = True
							# #####x  print(result)
							# pass
							except Exception as e:
								errors.append({'process': pI, 'data': tCs})
								result_error = True
								new_TopicsBuild += '(((' + pI + ')));'
				if result_found:
					tCs['vs'] = _str.cleanBE(new_TopicsBuild,'; ')
					# tCs['ref'] = result
					tCs['error'] = result_error
					tCs['dataSets'] = dataSets
					newTopics.append(tCs)
					# sys.exit()

			
	_.saveTable(newTopics,'bible_topic_NEW.json')
	_.saveTable(errors,'bible_topic_errors.json')
	if _.switches.isActive('GenerateTopicList'):
		topics = _.getTable('biblegateway.json')
		topicsUx = []
		for tCs in topics:
			# tCs = tCs
			
			s = re.sub('[^0-9a-zA-Z]+', ' ', tCs['word'].split('(')[0].lower())
			topicsUx.append(s)

		topicsUz = set(topicsUx)
		global topicsU
		topicsU = []
		omit = ['am','at','and','of','s','in','i','the','to','for','on','son','king','god','father','wife','from','false']
		for tCs in topicsUz:
			for x in tCs.split(' '):
				if not x in omit and len(x) > 1: 
					topicsU.append(' ' + x + ' ')
		_.saveTable(topicsU,'bible_topic_words.json')
			# #####x  print(tCs)
		# for tCs in topicsU:
		#     #####x  print(tCs)

		# for tCs in topics:
		#     t = prepText(tCs)
		#     #####x  print()
		bad = []
		for tCs in topics:
			t = tCs['description'].replace(_v.slash+'xbb','').lower()
			s = re.sub('[^0-9a-zA-Z]+', ' ', t)
			t = ' ' + s + ' '
			# #####x  print(t)
			found = False
			for tU in topicsU:
				if tU in t and len(tU) > 1:
					# #####x  print(tU,t)
					found = True
			if found:
				pass
				# #####x  print('good')
			else:
				bad.append(t)
				# #####x  print('bad',t)

		for bD in bad:
			for bS in bD.split(' '):
				if len(bS) > 1:
					pass
					#####x  print(bS)

########################################################################################
def prepText(tCs):
	t = tCs['description'].replace(_v.slash+'xbb','').lower()
	s = re.sub('[^0-9a-zA-Z]+', ' ', t)
	t = ' ' + s + ' '
	return t
def genTextList(string):
	global topicsU
	global words
	wordList = []
	found = False
	if len(words) == 0:
		words = _.getTable('bible_topic_words.json')
	for tU in words:
		if tU in string and len(tU) > 1:
			# #####x  print(tU)
			wordList.append(tU)
			found = True
	return wordList
def hasNumbers(string):
	return bool(re.search(r'\d', string))
def checkVerseExist(i,vs,data0,ref):
	global books
	global book_Lf
	found = True
	# print()
	# print(vs)
	xY = vs.replace(book_Lf[i],'')
	xYc = xY.split(':')[0]
	xYv0 = xY.split(':')[1].split('-')
	if len(xYv0) > 1:
		xYv1 = xYv0[1]
	else:
		xYv1 = xYv0[0]
	xYv2 = xYv1.split(',')
	if len(xYv2) > 1:
		xYv = xYv2[1]
	else:
		xYv = xYv2[0]
	xY_mXv = books[i]['chapter_verses'][int(xYc)-1]['verses']
	xY_xx = books[i]['chapter_verses'][int(xYc)-1]['chapter']
	# print(i,xY_xx,xYc,xY_mXv,xYv)
	if int(xY_mXv) < int(xYv):
		found = False
		# print('* vs error *')

	for rF in ref:
		mXv = books[rF[0]-1]['chapter_verses'][int(rF[1])-1]['verses']
		xx = books[rF[0]-1]['chapter_verses'][int(rF[1])-1]['chapter']
		# print(xx,rF[1],mXv,rF[2])

		# #####x  print(rF)
		# #####x  print(mXv)
		if int(mXv) < int(rF[2]):
			found = False
			# print('* ref error *')


		# for bC in books[rF[0]-1]['chapter_verses']:
		#     vsCount = bC['verses']
		#     # print(bC)
		#     if int(bC['chapter']) == int(rF[1]):
		#         if int(vsCount) < int(rF[2]):
		#             found = False
		#             print(books[rF[0]-1]['name'],data0,int(mXv), int(rF[2]))





	# sys.exit()
	# {
	#     "id": 65,
	#     "name": "Jude",
	#     "abbrev": "Jude",
	#     "chapter_verses": [
	#         {
	#             "chapter": 1,
	#             "verses": 25
	#         }
	#     ],
	#     "chapters": 1,
	#     "verses": 25
	# },
	# if not found:
	#     print()
	#     print(vs,books[i]['name'])
	#     print(books[i]['chapter_verses'][int(xYc)-1])

	#     print(i,xY_xx,xYc,xY_mXv,xYv)
	return found
sameIssue = []
autoWord = []
def lineProcess(string,data,test=False):
	# string = string
	global books
	global book_Lf
	global book_La
	global sameIssue
	global autoWord

	book = ''
	for iS,sT in enumerate(string):
		if not iS == 0:
			try:
				test = int(sT)
				break
			except Exception as e:
				pass
		book += sT
	# #####x  print(book)
	if book in book_Lf:
		for iF,lF in enumerate(book_Lf):
			if book == lF:
				result = [iF+1,string.replace(book,'')]
	elif book in book_La:
		for iA,lA in enumerate(book_La):
			if book == lA:
				result = [iA+1,string.replace(book,'')]
	else:
		#####x  print('Fail',book,string)
		fA = False
		b = ''
		st = ''
		for s in string:
			try:
				int(s)
				if fA:
					break
				st += s
			except Exception as e:
				fA = True
			if fA:
				b += s
		foundCount = 0
		#####x  print(foundCount)
		lastBS = 0
		existList = []
		for iF,lF in enumerate(book_Lf):
			if b in lF:
				tmp = string.replace(st+b,lF)
				data0 = lineProcess(tmp,data,True)
				ref = expandRef(data0)
				existList.append({'verse': data0, 'exists': checkVerseExist(iF,tmp,data0,ref)})
				
				search = buildList(data)
				bs = bibleSearch(ref,search)
				if len(bs) > lastBS:
					result = data0
					for bXs in bs:
						autoWord.append(bXs)
					_.saveTable(autoWord,'bible_auto_words.json',1,0)

				if len(bs) > 0 and len(bs) == lastBS:
					sameIssue.append({'vs': tmp, 'data0': data0, 'ref': ref, 'searchBible': bs, 'data': data, 'search': search})
					_.saveTable(sameIssue,'bible_verse_Same.json')

				lastBS = len(bs)
		####################
		found = True
		for eL in existList:
			if eL['exists'] == False:
				found = False
				# print(eL)
		if not found:
			for eL in existList:
				if eL['exists']:
					result = eL['verse']
					# print(eL)
					# print()
		####################

	try:
		result
	except Exception as e:
		found = True
		for eL in existList:
			if eL['exists'] == False:
				found = False
				# print(eL)
		if not found:
			for eL in existList:
				if eL['exists']:
					result = eL['verse']
					# print(eL)
					# print()

	# try:
	#     result
	# except Exception as e:
	#     pass
	#     # result = [1,'1']
	#     #####x  print('Found 0')
	#     # sys.exit()
	return result

def expandRef(data0):
	global books
	verses = []
	b = books[data0[0]-1]['name']
	# #####x  print(data0)
	# #####x  print()
	############### dont forget if :
	#####x  print(data0)
	if len(data0[1]) > 0:
		if ':' in data0[1]:
			cT = data0[1].split(':')[0]
			iT = data0[1].split(':')[1].split(',')

			# #####x  print('ch',cT)
			for iX in iT:
				if '-' in iX:
					# #####x  print(iX)
					th = iX.split('-')
					for xD in range(int(th[0]),int(th[1])+1):
						r_b = data0[0]
						r_c = cT
						r_v = xD
						verses.append([int(r_b),int(r_c),int(r_v)])
						#####x  print(b,cT,xD)
				else:
					r_b = data0[0]
					r_c = cT
					r_v = iX
					if len(r_v) == 0:
						r_v = 0
					# print(r_b,r_c,r_v)
					# verses.append([data0[0],cT,iX])
					verses.append([int(r_b),int(r_c),int(r_v)])
					#####x  print(b,cT,iX)
		else:
			#####x  print('********************************************')
			
			for bCH in books[data0[0]-1]['chapter_verses']:
				if bCH['chapter'] == int(data0[1]):
					for xD in range(1,int(bCH['verses']) +1):
						r_b = data0[0]
						r_c = data0[1]
						r_v = xD
						# verses.append([data0[0],int(data0[1]),xD])
						verses.append([int(r_b),int(r_c),int(r_v)])
						#####x  print(b,int(data0[1]),xD)

			#####x  print('********************************************')
	return verses

theBible = []
wordsT = []
words = []
def bibleSearch(data,search):
	found = 0
	result = []
	for d in data:
		text = bibleText(d)
		s = re.sub('[^0-9a-zA-Z]+', ' ', text.replace('-','').lower())
		t = ' ' + s + ' '
		#####x  print('Verse:',text)
		for w in search:
			if w in t:
				found = 1
				#####x  print('Found:',w)
				result.append(w)
	return result
def bibleText(data):
	global theBible
	result = ''
	if len(theBible) == 0:
		theBible = _.getTable('t_asv.json')
	# #####x  print(data[0])
	for tB in theBible['resultset']['row']:
		# if data[0] == tB['field'][1]:
			# #####x  print(tB['field'][1])
		if int(data[0]) == tB['field'][1] and int(data[1]) == tB['field'][2] and int(data[2]) == tB['field'][3]:
			result = tB['field'][4]
			# #####x  print(tB)
	return result

def buildList(data):
	global wordsT
	global words
	if len(wordsT) == 0:
		wordsT = _.getTable('bible_word_type.json')
	if len(words) == 0:
		words = _.getTable('bible_topic_words.json')
	omit = ['am','at','and','of','s','in','i','the','to','for','on','son','king','god','father','wife','from','false','held','into']
	search = []
	t = re.sub('[^0-9a-zA-Z]+', ' ', data['word'].split('(')[0].lower())
	search.append(t)
	for wD in t.split(' '):
		if not wD in omit and len(wD) > 1:
			if wD in words:
				search.append(wD)
			elif wD in wordsT['noun']:
				#####x  print('noun')
				search.append(wD)
			elif wD in wordsT['verb']:
				#####x  print('verb')
				search.append(wD)
			elif wD in wordsT['adv']:
				#####x  print('adv')
				search.append(wD)
			elif wD in wordsT['adj']:
				#####x  print('adj')
				search.append(wD)
			elif wD in wordsT['none']:
				#####x  print('none')
				search.append(wD)

	# s = re.sub('[^0-9a-zA-Z]+', ' ', data['word'].split('(')[0].lower())
	# for w in s.split(' '):
	#     if not w in omit and len(w) > 1:
	#         search.append(w)

	d = prepText(data)
	#####x  print(d)
	# for da in d:
	for w in d.split(' '):
		if not w in omit and len(w) > 1:
			if w in words:
				search.append(w)
			elif w in wordsT['noun']:
				#####x  print('noun')
				search.append(w)
			elif w in wordsT['verb']:
				#####x  print('verb')
				search.append(w)
			elif w in wordsT['adv']:
				#####x  print('adv')
				search.append(w)
			elif w in wordsT['adj']:
				#####x  print('adj')
				search.append(w)
			elif w in wordsT['none']:
				#####x  print('none')
				search.append(w)

	return search

########################################################################################
if False: # Example

	{
		"word": "AARON",
		"description": "Lineage of ",
		"vs": "Exodus 6:16-20; Joshua 21:4,10; 1 Chronicles 6:2,3;23:13"
	},
	{
		"id": 65,
		"name": "Jude",
		"abbrev": "Jude",
		"chapter_verses": [
			{
				"chapter": 1,
				"verses": 25
			}
		],
		"chapters": 1,
		"verses": 25
	},

########################################################################################
if __name__ == '__main__':
	action()





