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

#A1695618-Converted
from html.parser import HTMLParser
import html.entities

class HTMLTextExtractor(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.result = [ ]

	def handle_data(self, d):
		self.result.append(d)

	def handle_charref(self, number):
		codepoint = int(number[1:], 16) if number[0] in ('x', 'X') else int(number)
		self.result.append(chr(codepoint))

	def handle_entityref(self, name):
		codepoint = html.entities.name2codepoint[name]
		self.result.append(chr(codepoint))

	def get_text(self):
		return ''.join(self.result)

def html_to_text(html):
	s = HTMLTextExtractor()
	s.feed(html)
	return s.get_text()

def preCleanup(html):
	html=html.replace('<', ' <')
	html=html.replace('>', '> ')

	html=html.replace("\r", '')
	html=html.replace("\n", '')
	html=html.replace("\t", '')

	html=html.replace('<div', '----p<div')
	html=html.replace('</div', '----/p</div')

	html=html.replace('<p', '----p<p')
	html=html.replace('</p', '----/p</p')
	return html

def cleanup(html):
	html=html.replace("\r", '')
	html=html.replace("\n", '')
	html=html.replace("\t", '')

	html=html.replace(_v.slash+'r', '')
	html=html.replace(_v.slash+'n', '')
	html=html.replace(_v.slash+'t', '')
	html=html.replace(_v.slash+'x', "\n\\x")
	html=html.replace('----p',"\n")
	html=html.replace('----/p',"\n")

	while '  ' in html:
		html=html.replace('  ', ' ')
	while "\n " in html:
		html=html.replace("\n ","\n")

	while "\n\n\n" in html:
		html=html.replace("\n\n\n","\n\n")


	lines=html.split("\n")
	for line in lines:
		if excludeLine(line):
			print(line)
			# code+=line
	return '' 

def excludeLine(string):
	result=True
	if '==' in string:
		result=False
	if '.src' in string:
		result=False
	if _v.slash+'x' in string:
		result=False

	return result



import urllib.request, urllib.parse, urllib.error
# url = "http://stackoverflow.com"
# url = 'https://rephrecruiting.com/'



import sys

try:
	url = sys.argv[1]
	f = urllib.request.urlopen(url)
	code=str(f.read())
	code0=preCleanup(code)
	code1=html_to_text(code0)
	code2=cleanup(code1)
	result=code2
except:
	print("Please specify a url")


