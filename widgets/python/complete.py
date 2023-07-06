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
import readline
COMMANDS = ['extra', 'extension', 'stuff', 'errors',
			'email', 'foobar', 'foo']

def complete(text, state):
	for cmd in COMMANDS:
		if cmd.startswith(text):
			if not state:
				return cmd
			else:
				state -= 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)
raw_input('Enter section name: ')

