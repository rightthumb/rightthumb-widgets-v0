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

import simplejson as json
import sys
import datetime
import time

def getJSONFile():
	with open(sys.argv[2],'r', encoding="latin-1") as json_file:
		json_data = json.load(json_file)
	return json_data

jsonData = getJSONFile()

zero = 0
one = 0
two = 0
three = 0
totals = 0

zeroMax = 0
oneMax = 0
twoMax = 0
threeMax = 0
totalsMax = 0

vfirst = 0
i = 0
for j in jsonData:
	i += 1
	for t in j['timeAudit']:
		# print(t['where'],t['which'],t['stamp'])

		if vfirst == 0:
			vfirst = t['stamp']
		else:
			vlast = t['stamp']

		if t['where'] == 0 and t['which'] == 0:
			first = t['stamp']
		if t['where'] == 3 and t['which'] == 1:
			last = t['stamp']
		if t['which'] == 0:
			prev = t['stamp']
		if t['which'] == 1:
			result = t['stamp'] - prev
			# print(t['where'],result)
			if t['where'] == 0:
				zero += result
				if result > zeroMax:
					zeroMax = result
			if t['where'] == 1:
				one += result
				if result > oneMax:
					oneMax = result
			if t['where'] == 2:
				two += result
				if result > twoMax:
					twoMax = result
			if t['where'] == 3:
				three += result
				if result > threeMax:
					threeMax = result
	result = last - first
	totals += result
	if result > totalsMax:
		totalsMax = result
	# print(result,'\n')
print('')
print('i',f"{i:,d}")
print('')
print('zero',round(zero/i,1))
print('one',round(one/i,1))
print('two',round(two/i,1))
print('three',round(three/i,1))
print('totals',round(totals/i,1))
print('')
print('zero',zeroMax)
print('one',oneMax)
print('two',twoMax)
print('three',threeMax)
print('')


result = datetime.datetime.fromtimestamp(vlast / 1e3) - datetime.datetime.fromtimestamp(vfirst / 1e3)
print('Total:',result)
print('Total:',result.seconds)