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

ips = {}

fh = open("C:\Users\Scott\Desktop\qsort\qsort-2017.08.31-17.44-.txt", "r").readlines()
for line in fh:
	ip = line.split("\n")[0]
	print ip
	if 6 < len(ip) <=15:
		ips[ip] = ips.get(ip, 0) + 1
# print ips
# print fh

