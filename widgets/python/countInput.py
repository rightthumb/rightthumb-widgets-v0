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

# alias: ci
import sys

pipeResults = ''
safaChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

if not sys.stdin.isatty():
	pipeResults = sys.stdin.readlines()
	if not pipeResults[0][0] in safaChar:
		pipeResults[0] = pipeResults[0][1:]

for line in pipeResults:
	print(line)
print('')
print(len(pipeResults))