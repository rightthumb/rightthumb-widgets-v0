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
import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import re
import csv



_.switches.register('Input', '-i')
_.switches.register('WordThreshold', '-wordthreshold','Default is 6')
_.switches.register('GroupThreshold', '-groupthreshold','Default is 80 (it is a percent but dont add the percent sign)')

_.appInfo=    {
	'file': 'jsonIntelligentDataKeyGrouping.py',
	'description': 'Convert json to csv',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p jsonIntelligentDataKeyGrouping -i file.json ')


_.switches.process()



########################################################################################
words = []
keyGroups = []
theKeys = []



if _.switches.isActive('WordThreshold') == True:
	thresholdW = int(_.switches.value('WordThreshold'))
else:
	thresholdW = 6

if _.switches.isActive('GroupThreshold') == True:
	thresholdG = int(_.switches.value('GroupThreshold'))
else:
	thresholdG = 80


def checkThreshold(total,item,wORg='w'):
	global thresholdW
	global thresholdG
	total = int(total)
	item = int(item)
	if total > 0 and item > 0:
		percent1 = (item/total)*100
		
		if wORg == 'w':
			if percent1 > thresholdW:
				result = True
			else:
				result = False
			# result = True
		if wORg == 'g':
			percent2 = (total/item)*100

			if percent1 > percent2:
				percent = percent2
			else:
				percent = percent1
			

			if percent > thresholdG:
				result = True
			else:
				result = False
	else:
		result = False

	return result








def buildRelevant():
	global words
	global theKeys
	total = len(words)
	for w in words:
		if checkThreshold(total,w['count']) == True:
			w['relevant'] = True
			for tk in theKeys:
				if w['word'] in tk:
					w['keys'].append(tk)

	for w in words:
		if len(w['keys']) > 0:
			w['implode'] = ', '.join(w['keys'])



def buildGroups():
	buildRelevant()
	global keyGroups
	global words
	crossRef = []

	for word1 in words:
		if word1['relevant'] == True:
			for word2 in words:
				if word2['relevant'] == True:
					if not word1['word'] == word2['word']:
						crossRef.append({'words': {word1['word'],word2['word']}})
						total1 = len(word1['keys'])
						total2 = len(word2['keys'])
						if total1 > total2:
							total = total1
						else:
							total = total2
						matchCount = 0
						for key1 in word1['keys']:
							key1 = key1.replace(word1['word'],'')
							for key2 in word2['keys']:
								key2 = key2.replace(word2['word'],'')
								if key1 == key2:
									matchCount += 1

						if checkThreshold(total,matchCount,'g') == True:
							groupList(word1['word'],word2['word'],word1['keys'])
							groupList(word2['word'],word1['word'],word2['keys'])

	for kg in keyGroups:
		if len(kg['relationships']) > 0:
			kg['implode'] = ', '.join(kg['relationships'])
	return keyGroups


def groupList(word,related,keys):
	global keyGroups
	cnt = 0
	found = False
	for g in keyGroups:
		if keyGroups[cnt]['group'] == word:
			relFound = False
			for rel in keyGroups[cnt]['relationships']:
				if rel == related:
					relFound = True
			if not relFound:
				keyGroups[cnt]['relationships'].append(related)
			found = True
		cnt += 1

	if found == False:
		try:
			test0 = int(word)
			test1 = str(test0)
			if word == test1:
				isNumber = True
			else:
				isNumber = False
		except Exception as e:
			isNumber = False

		if not isNumber:
			keyGroups.append({'group': word, 'relationships': [], 'keys': [keys], 'implode': '',})


def wordList(word):
	global words
	cnt = 0
	found = False
	for w in words:
		if words[cnt]['word'] == word:
			words[cnt]['count'] += 1
			found = True
		cnt += 1
	if found == False:
		try:
			test0 = int(word)
			test1 = str(test0)
			if word == test1:
				isNumber = True
			else:
				isNumber = False
		except Exception as e:
			isNumber = False

		if not isNumber:
			words.append({'word': word, 'count': 1, 'relevant': False, 'keys': [], 'implode': '',})
def keyGrouping(data):
	global theKeys
	for key in data[0].keys():
		# print(key)
		key2 = key
		key2 = _str.replaceAll(key2,'_',' ')
		key2 = _str.replaceDuplicate(key2,' ')
		key2 = _str.cleanFirst(key2,' ')
		key2 = _str.cleanLast(key2,' ')

		key2 = _str.replaceAll(key2,'"','')
		theKeys.append(key2)
		for w in key2.split(' '):
			if len(w) > 0:
				wordList(w)

	return buildGroups()


def action():
	if _.switches.isActive('Input'):
		data0 = _.getTable2(_.switches.value('Input'))
		# print(data0)
		data = keyGrouping(data0)
		# print(data)
		# for kg in data:
		#     print(kg['count'],'\t',kg['word'])
		# print(data)
		# _.tables.register('Auto',words)
		# _.tables.print('Auto','word,count,relevant') # ,implode

		# _.tables.register('Auto',data)
		# _.tables.print('Auto','group,implode') # ,implode
		for d in data:
			# print('\ngroup:',d['group'])
			print()
			print('',d['group'])
			print('\trelationships:')
			for rel in d['relationships']:
				print('\t\t',rel)
			print('\tfields:')
			for k in d['keys'][0]:
				print('\t\t',k)
			print()
		# here
		print()
		print(len(data))
		print()
		_.saveTable(data,'automatedIntelligentDataKeyGrouping.json')

########################################################################################
if __name__ == '__main__':
	action()





