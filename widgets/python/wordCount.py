#!/usr/bin/python3
import _rightThumb._string as _str


def getFiles():
	global descriptions
	global words
	with open('exportDescription_FINAL.txt') as f:
	    descriptions = f.read().splitlines()


	with open('words1.txt') as f:
	    words = f.read().splitlines()


def getCount(line,word):
	line = line.lower()
	word = word.lower()
	result = 0
	try:
		# result = line.count(word)
		for item in line.split(' '):
			if _str.totalStrip(item) ==  _str.totalStrip(word):
				result += 1
	except Exception as e:
		pass
	return result


def processWord(word):
	global descriptions
	result = 0
	for d in descriptions:
		# print(d)
		# d = _str.totalStrip(d)
		result += getCount(d,word)
	return result


def processWords():
	global words
	for w in words:
		found = processWord(w)
		print('{},{}'.format(w,found))


getFiles()
processWords()

