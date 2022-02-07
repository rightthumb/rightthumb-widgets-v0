#!/usr/bin/python3

import sys

for i,arg in enumerate(sys.argv):
	if arg == '-backup':
		isBackup=1
	elif arg == '-creative':
		isCreative=1
	elif arg == '-survival':
		isSurvival=1
	elif arg == '-name':
		try:
			theName=sys.argv[i+1]
		except Exception as e:
			pass

