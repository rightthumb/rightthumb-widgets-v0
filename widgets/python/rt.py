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

