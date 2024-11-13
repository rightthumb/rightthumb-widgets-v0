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

#835B0032-Legacy
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
	print "\n-----------\nRolling the dices...\n"
	print random.randint(min, max)
	print random.randint(min, max)

	roll_again = raw_input("Roll the dices again? ")



