#!/usr/bin/python3
import sys
for i,arg in enumerate(sys.argv):
	if 'rt' in arg :
		if not 'rt' in sys.argv[i+1]:
			subject = sys.argv[i+1]
		else:
			subject = sys.argv[i+2]
		break

do='''
#from rightthumb import _'''+subject+'''
from _rightThumb._hub import app_'''+subject+'''
app_'''+subject+'''.loader()
app_'''+subject+'''.action()

'''
# print(do)
exec(do)