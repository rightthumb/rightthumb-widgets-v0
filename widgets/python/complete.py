#!/usr/bin/python3
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