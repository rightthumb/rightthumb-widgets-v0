#!/usr/bin/python3
import os
# os.system('echo test')

target = input(' - ')
# output = os.system(target)
os.system(target + '>tmp_log_file.txt')
output = open( 'tmp_log_file.txt', 'r' ).read()
show = input('Show? ')
if 'y' in show or 'Y' in show:
	print(output)
if 's' in show or 'S' in show:
	line = input(' - ')
	os.system('type tmp_log_file.txt | p line ' + line)