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
import hashlib

# p file --c | p line -make "md5.py {}" --c | p execute
# p files --c | p dir -c p -s bytes --c | p line -make "C:\tech\programs\python\md5.py ;'{};'" --c | p execute
# type %tmpf1% | p line -make " md5.py ;'{};'"


def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
def md52(string):
	hash_md5 = hashlib.md5()
	hash_md5.update(string)
	return hash_md5.hexdigest()

# try:
#     result = md5(sys.argv[len(sys.argv)-1])
#     print(result)
#     # print(result,sys.argv[len(sys.argv)-1])
# except Exception as e:
#     print('* Fail *',sys.argv[len(sys.argv)-1])
#     # print('* Fail *')

print(md52('string'))
# for i in sys.argv:
#     print(i)