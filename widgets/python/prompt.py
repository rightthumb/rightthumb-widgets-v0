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

import readline
import colorama
colorama.init()
COMMANDS = ['qwerty','uiop','asdf','ghjkl']

def complete(text, state):
	for cmd in COMMANDS:
		if cmd.startswith(text):
			if not state:
				return cmd
			else:
				state -= 1

def main():
	readline.parse_and_bind("tab: complete")
	readline.set_completer(complete)
	while True:
		test_input=raw_input(':')
		print(test_input)

main()

