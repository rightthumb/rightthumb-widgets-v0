#!/usr/bin/python3
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