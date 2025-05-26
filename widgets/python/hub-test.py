import sys

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


do='''
#from rightthumb import _'''+sys.argv[2]+'''
from _rightThumb._hub import _'''+sys.argv[2]+'''
_'''+sys.argv[2]+'''.sw()
_'''+sys.argv[2]+'''.run()

'''
print(do)
exec(do)

