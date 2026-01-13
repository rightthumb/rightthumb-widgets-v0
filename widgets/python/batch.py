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

import os
# os.system('echo test')

target = input(' - ')
# output = os.system(target)
os.system(target + '>tmp_log_file.txt')
output = open( 'tmp_log_file.txt', 'r' ).read()
show = input('Show? ')
if 'y' in show or 'Y' in show:
	print(output)
if 's' in show or 'S' in show:
	line = input(' - ')
	os.system('type tmp_log_file.txt | p line ' + line)