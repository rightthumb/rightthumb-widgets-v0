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
# import sys
# import simplejson as json
# import shutil
# import sqlite3
import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Input', '-i,-f,-file','style.css')
_.switches.register('Attrib', '-attrib')
_.switches.register('HTML', '-html')
_.switches.register('Issue', '-issue')

_.appInfo[__name__] = {
	'file': 'auditcss2.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}


_.appInfo[__name__]['examples'].append('p auditcss2 -file style.css')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditcss2 -f responsive2.css + .resumeItem - " "')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')


_.appInfo[__name__]['examples'].append('p auditcss2 -f responsive2.css + #edubody .resumeItem -attrib > %tmpf6%')
_.appInfo[__name__]['examples'].append('n %tmpf6%')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('type %tmpf6% | p line - "@" "." #')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditcss2 -html %tmpf6% -f style.css -attrib')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditcss2 -html %tmpf6% -f style1.css -attrib -issue')
_.appInfo[__name__]['examples'].append('p auditcss2 -html %tmpf6% -f style1.css -attrib -issue width')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('p auditcss2 -f css/responsive.css -attrib height + cert')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')

# _.appInfo[__name__]['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo[__name__]['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f

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


#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)



########################################################################################
# class TheChildItems:

#     def __init__(self, name, switch):
#         self.name = name
#         self.active = False
#         self.value = None

#     def trigger(self,script):
#         self.script_trigger = script

#     def changeStatus(self,newStatus):
#         self.active = newStatus
# class TheParentItems:

#     def __init__(self):
#         self.childItemRows = []

#     def register(self, name):
#         self.childItemRows.append(TheChildItems(name))
#     def print(self):
#         childItems = []
#         for ci in self.childItemRows:
#             childItems.append({'name':ci.name})
#         _.tables.register('childClassItems',childItems)
#         # tables.trigger('switches','switch,name',test,True)
#         _.tables.print('childClassItems','name')
#     def printStatus(self):
#         childItems = []
#         for ci in self.childItemRows:
#             if ci.active:
#                 active = 'True'
#             else:
#                 active = 'False'
#             value = ci.value
#             if ci.value == True:
#                 value = 'True'
#             elif ci.value == False:
#                 value = 'False'

#             childItems.append({'name':ci.name ,'active':active,'value': value})
#         _.tables.register('childClassItems',childItems)
#         _.tables.print('childClassItems','name,active,value')
#     def status(self,name,newStatus):
#         for i,ci in enumerate(self.childItemRows):
#             if ci.name == name:
#                 self.childItemRows[i].changeStatus(newStatus)




#     json = _.getTable('base64Key.json')
#    books = _.getText(_v.myTables + '\\bible_books.csv')

# _.saveTable(jsonFile,'file.json')
# _.saveText(convertedFile,_.ci(_.switches.value('Output')))
# _.saveText(convertedFile,'file.txt')
# _.showLine(item)
########################################################################################
def hasChildren(string):
	result = False
	if string.startswith( '@' ):
		result = True
	return result
def prepHTML(string):
	global commentOpen
	global commentClose
	string = string.replace('\n','')
	string = string.replace(commentOpen,'\n' + commentOpen)
	string = string.replace(commentClose,commentClose + '\n')
	tmp = ''

	for x in string.split('\n'):
		if not commentOpen in x:
			tmp += x
		else:
			pass
	string = ''
	string = tmp
	string = string.replace('>','>\n')
	string = string.replace('<','\n<')
	return string
def prep(string):
	global commentOpen
	global commentClose
	# string = _str.replaceAll(string,'{','\n{\n')
	# string = _str.replaceAll(string,'}','\n}\n')
	string = string.replace('\n','')
	string = string.replace(commentOpen,'\n' + commentOpen)
	string = string.replace(commentClose,commentClose + '\n')
	tmp = ''

	for x in string.split('\n'):
		# print(x)
		if not commentOpen in x:
			tmp += x
		else:
			pass
			# print(x)
	string = ''
	string = tmp
	string = string.replace('{','{\n')
	string = string.replace('}','\n}\n')
	string = string.replace("'",'"')
	# string = re.sub(r'<[^>]+>', string, '')
	return string
def clean(string):
	# string = _str.replaceAll(string,'\t',' ')
	string = string.replace('\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string
def action2():
	cssFile = _.ci(_.switches.value('Input'))
	# print(cssFile)
	# sys.exit()
	cssFileX = _.getText(cssFile)

	cssFile = ''
	for line in cssFileX:
		line = line.replace('','')
		cssFile += line

	for ix,itemX in enumerate(cssFile.split('}')):
		item = itemX.split('{')
		label = ''
		comment = False
		for lineL in item[0].split('\n'):
			documented = False
			if '/*' in lineL:
				label += lineL.split('/*')[0].split('//')[0]
				documented = True
				if '*/' in lineL:
					label += lineL.split('*/')[1].split('//')[0]
					documented = True
				else:
					comment = True
			if '*/' in lineL:
				label += lineL.split('*/')[1]
				comment = False
				documented = True
			if not documented:
				label += lineL.split('//')[0]



		label = clean(label)
		# print(label)
		print(item[1])
def isIn(selectors,label,eq):
	result = 0
	cnt = label.count(' ') + 1
	for elx in selectors['el']:
		item = elx
		if label.startswith(item+':'):
			result += 1
		if label.startswith(item+' '):
			result += 1
		if label.endswith(' '+item):
			result += 1
		if label.endswith(' '+item+':'):
			result += 1
		if label == item:
			result += 1

	for idx in selectors['id']:
		item = '#'+idx
		if label.startswith(item+':'):
			result += 1
		if label.startswith(item+' '):
			result += 1
		if label.endswith(' '+item):
			result += 1
		if label.endswith(' '+item+':'):
			result += 1
		if label == item:
			result += 1

	for classx in selectors['class']:
		item = '.'+classx
		if label.startswith(item+':'):
			result += 1
		if label.startswith(item+' '):
			result += 1
		if label.endswith(' '+item):
			result += 1
		if label.endswith(' '+item+':'):
			result += 1
		if label == item:
			result += 1



	if not eq:
		if result > 0:
			result = True
		else:
			result = False
	else:
		if cnt == result or cnt < result:
			result = True
		else:
			result = False

	return result 


def action():
	global issues
	global commentOpen
	global commentClose
	if _.switches.isActive('Issue'):
		issue = _.switches.value('Issue')
		if len(issue) == 0:
			for x in issues:
				for y in x['issue'].split(','):
					print(y)
				# print(issue['research'])
			sys.exit()
		else:
			found = False
			for x in issues:
				for y in x['issue'].split(','):
					if issue == y:
						found = True
						_.switches.fieldSet('PlusOr','active',True)
						_.switches.fieldSet('Plus','active',True)
						_.switches.fieldSet('Plus','value',x['research'])
			
			if not found:
				print('Not Found')
				sys.exit()




	if _.switches.isActive('HTML'):

		htmlFile = _.ci(_.switches.value('HTML'))
		selectors = {'id':[], 'class': [], 'el': []}
		htmlFileX = _.getText(htmlFile)
		# print(htmlFileX)

		htmlFile = ''
		for line in htmlFileX:
			line = line.replace('\n','')
			line = line.replace('<!--',commentOpen)
			line = line.replace('-->',commentClose)
			htmlFile += line.split(commentOpen)[0]
		htmlFile = prepHTML(clean(htmlFile))
		ids = []
		classes = []
		els = []
		els.append('*')
		for line in htmlFile.split('\n'):
			if '<' in line and not '</' in line:
				x = line.split('<')[1]
				y = x.split(' ')[0]
				els.append(y)
			if 'id=' in line.lower():
				x = line.split('id="')[1]
				y = x.split('"')[0]
				ids.append(y)
			if 'class=' in line.lower():
				x = line.split('class="')[1]
				y = x.split('"')[0]
				classes.append(y)
		# print(htmlFile)

		selectors['el'] = list(set(els))
		selectors['id'] = list(set(ids))
		selectors['class'] = list(set(classes))

		# print(selectors)




	# if _.switches.isActive('HTML'):
		# sys.exit()
	if not _.switches.isActive('Input'):
		sys.exit()
	cssFile = _.ci(_.switches.value('Input'))
	# print(cssFile)
	# sys.exit()
	cssFileX = _.getText(cssFile)

	cssFile = ''
	for line in cssFileX:
		line = line.replace('\n','')
		line = line.replace('/*',commentOpen)
		line = line.replace('*/',commentClose)
		cssFile += line.split('//')[0]
	cssFile = prep(clean(cssFile))
	# print(cssFile)
	
	depth = 0
	# print(css)
	result = {}
	css = []
	
	for i,line in enumerate(cssFile.split('\n')):
		# print(i,line)
		thisIs = ''
		if '}' in line:
			# print(line)
			depth -= 1
			thisIs = 'END'
		elif '{' in line:
			label = clean(line.split('{')[0])
			result[depth] = label
			depth += 1
			thisIs = 'LABEL'
		elif (len(line) > 0):
			thisIs = 'CODE'
			code = []
			theLabel = []
			for z in line.split(';'):
				if len(clean(z)) > 0:
					code.append(clean(z))
			for z in label.split(','):
				if len(clean(z)) > 0:
					theLabel.append(clean(z))
			# print(label,depth,line)
			# print(depth)
			# print(i,depth,label,thisIs,code)
			if depth == 0:
				pass
				css.append({'label': theLabel, 'code': code, 'parent': ''})
				# print(i,depth,label,code)
			elif depth == 2:
				pass
				# print(label)
				# print(i,depth,result[0],result[1],code)
				css.append({'label': theLabel, 'code': code, 'parent': result[0]})
			else:
				pass
				css.append({'label': theLabel, 'code': code, 'parent': ''})
				# print(i,depth,result[0],code)
	_.saveTable2(css,'css.json')
	# sys.exit()
	if not _.switches.isActive('HTML'):
		for item in css:
			for label in item['label']:
				# print(type(label))
				if _.showLine(label):
					if len(item['parent']) > 0:
						print(item['parent'])
					print(label)
					if _.switches.isActive('Attrib'):
						v = _.switches.value('Attrib')
						for c in item['code']:
							if len(v) > 0:
								if v in c:
									print('\t',c+';')
							else:
								print('\t',c+';')
					print()
	else:
		print()
		print()
		if _.switches.isActive('Issue'):
			for item in css:
				for label in item['label']:
						if isIn(selectors,label,True):
							if len(item['parent']) > 0:
								print(item['parent'])
							print(label)
							for c in item['code']:
								if _.showLine(c):
									print('\t',c+';')

							print()
		else:
			for item in css:
				for label in item['label']:
					if _.showLine(label):
						if isIn(selectors,label,True):

							if len(item['parent']) > 0:
								print(item['parent'])
							print(label)
							if _.switches.isActive('Attrib'):
								v = _.switches.value('Attrib')
								for c in item['code']:
									if len(v) > 0:
										if v in c:
											print('\t',c+';')
									else:
										print('\t',c+';')
							print()





commentOpen = 'DD0C39A6D9B0'
commentClose = 'F108383C7791'
issues = []
issuesAdd = []
issues.append({'issue': 'width,100,100%', 'research': 'width,display'})
issuesAdd.append({'description': 'change doesnt work', 'issue': 'fail', 'resolution': 'add id to class'})
########################################################################################
if __name__ == '__main__':
	action()