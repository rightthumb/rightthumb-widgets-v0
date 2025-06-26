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

# import os
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'bibleGateTopic.py',
	'description': 'Gets data from biblegateway website',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p bibleGateTopic')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)

_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


# if _.switches.isActive('_File_'):
#     _.tables.register('toCheck') # table, rows = []
#     _.switches.fieldSet('_File_','active',True)
#     _.switches.fieldSet('_File_','value','toCheck.json')
#     _.tables.get('toCheck',_.switches.value('_File_'))
#     _.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
#     _.tables.sort('toCheck', 'name')

#     _.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
#     _.tables.view('test_table','sample') # table, view

#     _.switches.fieldGet('Column','pos')
#     if _.switches.exists('Column2'):
#         print('This is a valid switch')




#     if _.switches.isActive('Output') == True:
#         _.saveTable2(jsonFile,_.switches.value('Output'))
#         # _.saveText(convertedFile,_.ci(_.switches.value('Output')))

#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')


########################################################################################
def getList(url):
	pass
def getNext(url):
	pass
def action():
	url = 'https://www.biblegateway.com/topical/'
	page = requests.get(url)
	tree = html.fromstring(page.content)

	tables = tree.cssselect('.section a')
	base = 'https://www.biblegateway.com'
	payload = []
	for i,tA in enumerate(tables):
		line = _str.cleanSpecial(tA.text_content())
		newURL = base + tA.attrib['href']
		if True:
		# if i == 0:
			print(line,newURL)
			done = False
			offset = 0
			while not done:
				page = requests.get(newURL)
				tree = html.fromstring(page.content)
				nav = tree.cssselect('.results-head .txt-sm a')
				# dataNames = tree.cssselect('[start='1'] li a')
				dataNames = tree.cssselect('li a')
				for dN in dataNames:
					dn_line = _str.cleanSpecial(dN.text_content())

					try:
						dn_newURL = base + dN.attrib['href']
						# print(dn_line,dn_newURL)
					except Exception as e:
						dn_newURL = ''
						# print(dn_line)
					if '/topical/' in dn_newURL and '/Nave' in dn_newURL:
						# print(dn_line,dn_newURL)
						page = requests.get(dn_newURL)
						tree = html.fromstring(page.content)
						dataList = tree.cssselect('ol li') #######
						for dL in dataList:
							try:
								dL_lnk = dL.cssselect('a')
							except Exception as e:
								dL_lnk = []
							# print(len(dL_lnk))
							if len(dL_lnk) > 0:
								# print()
								# print(_str.cleanSpecial(dL_lnk[0].text_content()))
								# print()
								dL_line = _str.cleanSpecial(dL.text_content())
								# print(dL_line)
								# par = dL_line.split('(')
								# if len(par) > 2:
								#     if len(par) == 3:
								#         dL_description = par[0] + '(' + par[1]
								#     if len(par) == 4:
								#         dL_description = par[0] + '(' + par[1] + '(' + par[2]
								#     if len(par) == 5:
								#         dL_description = par[0] + '(' + par[1] + '(' + par[2] + '(' + par[3]
								# else:
								#     dL_description = dL_line.split('(')[0]


								dL_description = dL_line


								# dL_description = ''
								# for dLL in dL_lnk:
								#     dL_description += _str.cleanSpecial(dLL.text_content())
								#     dL_description += '; '
								# dL_description += '54D277C986F0'
								# dL_description = dL_description.replace('; 54D277C986F0','')



								# dL_description = ''
								# try:
								#     dL_vs = dL_line.split('(')[len(par)-1].replace(')','')
								# except Exception as e:
								#     dL_vs = ''
								if len(dL_lnk) > 1:
									if len(dL_lnk) == 2:
										dL_vs = _str.cleanSpecial(dL_lnk[0].text_content()) + '; ' + _str.cleanSpecial(dL_lnk[1].text_content())
									if len(dL_lnk) == 3:
										dL_vs = _str.cleanSpecial(dL_lnk[0].text_content()) + '; ' + _str.cleanSpecial(dL_lnk[1].text_content()) + '; ' + _str.cleanSpecial(dL_lnk[2].text_content())
								else:    
									dL_vs = _str.cleanSpecial(dL_lnk[0].text_content())
								if len(dL_vs) > 0 and not '/topical/' in dL_lnk[0].attrib['href']: # and ' See ' in dL_description
									d = {'word': dn_line, 'vs': dL_vs, 'description': dL_description.replace('('+dL_vs+')','')}
									print(d)
									payload.append(d)

				found = False
				for nA in nav:
					na_line = _str.cleanSpecial(nA.text_content())
					na_newURL = base + nA.attrib['href']
					if 'Next' in na_line and not found:
						found = True
						if not 'offset' in na_newURL:
							newURL = na_newURL + '&offset=' + str(offset) + '&limit=25'
							offset += 25
						else:
							newURL = na_newURL
						print(na_line,newURL)
				if not found:
					done = True
	_.saveTable(payload,'biblegateway.json')





########################################################################################
if __name__ == '__main__':
	action()





