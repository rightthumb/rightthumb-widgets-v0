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

# https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w
# when done rename to label file 
import sys
import os

 # thisFile=sys.argv[1]
# labelLegacy="#835B0032\n"
thefile=sys.argv[1]
theLabel=sys.argv[2]
tmpFile="AE9F42AC-98AB-E12A-5BAE-C0C3ABB05392.txt"

def insert(originalfile,string):

	with open(originalfile,'r') as f:
		with open(tmpFile,'w') as f2: 
			f2.write(string+"\n")
			f2.write(f.read())
	if os.path.exists(originalfile):
		os.remove(originalfile)
	os.rename(tmpFile,originalfile)
	if os.path.exists(tmpFile):
		os.remove(tmpFile)

noAction=False
def check(originalfile,string):
	with open(originalfile,'r') as f:
		for line in f:
			if string in line:
				global noAction
				noAction=True


check(thefile,theLabel)

if not noAction:
	insert(thefile,theLabel)

check(thefile,theLabel)




