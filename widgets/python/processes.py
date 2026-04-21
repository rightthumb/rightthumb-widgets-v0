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

import sys
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

from lxml import html
import requests
import cssselect

_.switches.register('File', '-file','file.txt')


_.appInfo=    {
	'file': 'processes.py',
	'description': 'Check if processes are ok',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}
_.appInfo['examples'].append('p processes -file file.txt')
# _.appInfo['columns'].appedn({'name': 'name', 'abbreviation': 'n'})

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
def lookupFile(process,url,site):
	# url = 'https://www.bleepingcomputer.com/startups/search/'
	# page = requests.post(url, data = {'keyword':file,'sort': 'filename'})
	
	if site == 'bleepingcomputer.com':
		try:
			error = False
			found = False
			page = requests.get(url)
			tree = html.fromstring(page.content)
			# tables = tree.cssselect('.processBad')
			tables = tree.cssselect('h6')
			for h6 in tables:
				text = h6.text_content()
				text = _str.cleanupString0(text)
				if 'undesirable' in text:
					found =True
		except Exception as e:
			error = True

	if error:
		result = 'Unknown'
	else:
		if found:
			result = 'Bad'
			print(process,'Bad')
		else:
			result = 'OK'
			print(process,'Checked')
	
	return result



def research(search,site):
	# site = 'pcpitstop.com'
	# site = 'file.net'
	# site = 'bleepingcomputer.com'
	url = 'https://www.google.com/search?q=site:' + site + '+'
	newURL = url + _str.replaceAll(_str.replaceAll(search,',','+'),' ','+')
	print(newURL)
	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('.r')

	i = 0
	found = False
	
	for t in tables:
		item = t.text_content()
		links = t.cssselect('a')
		link0 = str(links[0].attrib['href'])
		link1 = link0.replace('/url?q=http','http')
		
		if not found and search in item.lower() and site in link1.lower():
			found = True
			link = link1
			
		i += 1

	if found:
		# print(link)
		return lookupFile(search,link,site)
	else:
		print('E:',len(tables),search,'Unknown')
		return 'Unknown'



pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if not pipeData[0][0] in _str.safeChar:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass

def cleanupString0(string):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	return string

########################################################################################
def action():
	if _.switches.isActive('File'):
		research(_.switches.value('File'),'bleepingcomputer.com')
	else:
		global pipeData
		_.tables.register('processes')
		processes = _.tables.get('processes','processes.json')
		# _.tables.file('processes','processes.json')
		if len(processes) > 0:
			loaded = True
		else:
			loaded = False
		# print(loaded)
		# sys.exit()
		for row in set(pipeData):
			# row = row.replace('\n','')
			# print(len(row),row)
			row = cleanupString0(row)
			if len(row) > 3:
				# processes.append({'process': row, 'status': research(row)})
				if loaded:
					found = False

					for pro in processes:
						if not found and row == pro['process']:
							found = True
							if pro['status'] == 'Unknown':
								pass
							print('-',row,pro['status'])
					if not found:
						result = research(row,'bleepingcomputer.com')
						processes.append({'process': row, 'status': result})
				else:
					result = research(row,'bleepingcomputer.com')
					processes.append({'process': row, 'status': result})


		_.tables.set('processes',processes)
		_.tables.save('processes')



########################################################################################
if __name__ == '__main__':
	action()