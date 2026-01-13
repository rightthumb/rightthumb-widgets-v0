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

# import os
import sys
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
# from netaddr import IPAddress
# import socket,struct

from lxml import html
import requests
import cssselect


_.switches.register('IP', '-ip')


_.switches.process()


########################################################################################

def pageData(theUrl,lookupWhat):
	page = requests.get(theUrl)
	tree = html.fromstring(page.content)
	data = tree.cssselect(lookupWhat)
	result = []
	for d in data:
		result.append(d.text_content())
	return result

########################################################################################
def action():
	countries = _.getTable('countries_ips.json')

	if _.switches.isActive('IP') == True:

		try:
			theUrl = 'http://whois.arin.net/rest/nets;q=' + _.switches.value('IP') + '?showDetails=true&showARIN=false'
			profile = pageData(theUrl,'orgRef')
			company = pageData(profile[0],'name')
			print('\narin:')
			print('\t',company[0])
			print('\t',company[1])
		except Exception as e:
			raise e
########################################################################################
if __name__ == '__main__':
	action()