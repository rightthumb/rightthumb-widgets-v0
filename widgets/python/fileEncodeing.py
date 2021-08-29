#!/usr/bin/python3
import chardet 
file = 'appServer.py'   
rawdata = open(file, "r").read()
result = chardet.detect(rawdata)
charenc = result['encoding']