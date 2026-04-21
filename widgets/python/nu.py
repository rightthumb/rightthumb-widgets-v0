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


from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

while True:
	keyboard.press(Key.num_lock)
	keyboard.release(Key.num_lock)
	time.sleep(0.1)