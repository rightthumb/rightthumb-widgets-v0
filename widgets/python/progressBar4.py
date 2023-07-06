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

from progress.bar import Bar
from time import sleep

bar = Bar('Processing', max=20)
for i in range(20):
	sleep(0.1)
	# Do some work
	bar.next()
bar.finish()

