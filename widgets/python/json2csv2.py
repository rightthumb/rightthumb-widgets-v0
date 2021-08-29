#!/usr/bin/python3
import simplejson as json
import _rightThumb._string as _str
import sys

# i = 0
# for a in sys.argv:
# 	print(i,a,len(a))
# 	i += 1

exit = True

try:
	if len(sys.argv[2]) > 3:
		exit = False
except Exception as e:
	pass

if exit == True:
	print('Enter File Name')
	sys.exit()
with open(sys.argv[2],'r', encoding="latin-1") as json_file:
	json_data = json.load(json_file)

i = 0
for row in json_data:
	line = ''
	if i == 0:
		for cell in row.keys():
			line += '"' + str(cell) + '",'

		line = _str.cleanLast(str(line),',')
		print(line)
	i += 1

for row in json_data:
	line = ''
	for cell in row.keys():
		line += '"' + _str.cleanSpecial(str(row[cell])) + '",'

	line = _str.cleanLast(str(line),',')
	print(line)

