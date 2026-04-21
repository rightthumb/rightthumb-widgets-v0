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

from lxml import html
import requests
import cssselect
import _rightThumb._string as _str
import _rightThumb._vars as _v
import simplejson as json
print('\nBuilding database of every registered network in the world.\n')
def saveTable(rows,theFile,tableTemp = True,printThis = True):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + file0)
def getCountryData(thisUrl):
	countryData = []
	try:
		newURL = 'https://www.nirsoft.net/countryip/' + thisUrl
		print(newURL)
		page = requests.get(newURL)
		tree = html.fromstring(page.content)

		# print(tree['body'])
		# test = tree.xpath('//td/text()')
		# test = tree.xpath('//tr')

		tables = tree.cssselect('table')
		rows = tables[6].getchildren()
		i = 0
		start = False
		i = 0
		# print(len(tables))
		result = []
		for r in rows:
			row = {0: '',1: '',2: '',3: '',4: ''}
			ii = 0
			for d in r.getchildren():
				line = _str.cleanSpecial(d.text_content())
				row[ii] = line
				# print(line)
				ii += 1
			result.append(row)
		for rr in result:
			countryData.append({'network': rr[0],'subnet': rr[1],'nodes': rr[2],'date': rr[3]})
			print(rr[0],rr[1],rr[2],rr[3])
	except Exception as e:
		pass
	return countryData

page = requests.get('https://www.nirsoft.net/countryip/')
tree = html.fromstring(page.content)


links = tree.cssselect('a')  # or tree.xpath('//a')

out = []
for link in links:
	# we use this if just in case some <a> tags lack an href attribute
	if 'href' in link.attrib:
		out.append({'name': link.text_content(), 'url': link.attrib['href']})
		test = link
countries = []
start = False
i = 0
for o in out:
	if o['name'] == 'Afghanistan':
		start = True
	if start:
		if i == 0:
			pass
		print('getting data for: ', o['name'])
		countries.append({'name':o['name'],'ip': getCountryData(o['url'])})
		i += 1

saveTable(countries,'countries_ips.json')