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
_.switches.register('Output', '-o')

_.appInfo=    {
	'file': 'json2csv.py',
	'description': 'Convert json to csv',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p json2csv -i file.json -o file.csv')


_.switches.process()



########################################################################################
def jsonFile(json_file):
	with open(json_file, 'r') as fh:
		bad_json = fh.read()
		#print(bad_json)
		improved_json  = re.sub(r'"\s*$', '",', bad_json, flags=re.MULTILINE)
		#print(improved_json)

		# good_json = re.sub(r'(?<!")(?P<word>[\w-]+)\b(?!")', '"\g<word>"',
		#   improved_json)
		# good_json = re.sub(r'(?<[\{\s])(?P<word>[\w-]+)(?=[:\s])', '"\g<word>"',
		#   improved_json)
		# good_json = re.sub(r'([\{\[\s])(?P<word>[\w-]+)([:,\]\s])', '\1"\g<word>"\3',
		#   improved_json)
		good_json = re.sub(r'(?<=[\{\[\s])(?P<word>[\w-]+)(?=[:,\]\s])', '"\g<word>"',
		improved_json)
		#print(good_json)

	# with open('out.js', 'w') as fh:
	#     fh.write(good_json)

	data = json.loads(good_json)
	return data
########################################################################################
def clean(theValue):
	theValue = str(theValue)
	theValue = _str.cleanSpecial(theValue)
	# theValue = theValue.replace(',','{6BEB554C-3FCE-419F-8917-B5A0678F48BA}')
	# theValue = theValue.replace(',','\",\"')
	return theValue
def myJsonCleaner(data):
	# print(type(data))
	newData = []
	for i,dt in enumerate(data):
		record = {}
		for key in data[0].keys():
			if type(data[i][key]) == list:
				pass
				data2 = data[i][key]
				for i2,dt2 in enumerate(data2):
					for key2 in data[i][key][0].keys():
						pass
						newKey = key + '_' + key2 + '_' + str(i2)
						newKey = str(newKey)
						# print(newKey)
						# print(data2[i2][key2])
						# data[i][newKey] = ''
						# data[i][newKey] = clean(data2[i2][key2])
						record[newKey] = clean(data2[i2][key2])
			else:
				# data[i][key] = clean(data[i][key])
				record[key] = clean(data[i][key])
		newData.append(record)

	return newData


def action():
	if _.switches.isActive('Input') and _.switches.isActive('Output'):
		fileInput = _.switches.value('Input')
		fileOutput = _.switches.value('Output')

		inputFile = open(fileInput)
		data0 = json.load(inputFile)
		data = myJsonCleaner(data0)
		outputFile = open(fileOutput, 'w')
		output = csv.writer(outputFile)

		output.writerow(data[0].keys())
		for row in data:
			output.writerow(row.values())

########################################################################################
if __name__ == '__main__':
	action()





