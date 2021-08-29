import sys

do='''
#from rightthumb import _'''+sys.argv[2]+'''
from _rightThumb._hub import _'''+sys.argv[2]+'''
_'''+sys.argv[2]+'''.sw()
_'''+sys.argv[2]+'''.run()

'''
print(do)
exec(do)