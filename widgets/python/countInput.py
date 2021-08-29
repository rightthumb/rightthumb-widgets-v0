#!/usr/bin/python3
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
