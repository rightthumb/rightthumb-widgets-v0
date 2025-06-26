#!/usr/bin/python3

import sys
import simplejson
if len(sys.argv) > 1:
	mirror=sys.argv[1]

	with open('/opt/rightthumb-widgets-v0/widgets/databank/tables/fo.index', 'r') as file:
		data = file.read().replace('\r','')
	index = simplejson.loads(data)
	# print()
	# print(index)
	# print()
	if mirror in index:
		for line in index[mirror]['folders']: print(line)
