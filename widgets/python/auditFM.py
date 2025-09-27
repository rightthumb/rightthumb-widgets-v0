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

import os
# import sys
# import simplejson as json
# import shutil
# import sqlite3

from lxml import html
import requests
import cssselect

from bs4 import BeautifulSoup 



import pathlib

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
_.appInfo=    {
	'file': 'auditFM.py',
	'description': 'Autit documented XML from FileMaker database tables',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p auditFM')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p auditFM | p line -p ;.;. 0 --c | p line -u')

if __name__ == '__main__':
	pass
	# _.switches.register('Input', '-i','appIn.py')
	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')


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
if __name__ == '__main__':
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
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')

#    books = _.getText(_v.myTables + _v.slash+'bible_books.csv')

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
# _.showLine(item)
########################################################################################
def fieldInfo(path,file):
	global fieldData
	f = open(path, 'r')
	s = f.read()
	# soup = BeautifulSoup(s,"lxml")
	soup = BeautifulSoup(s,"html.parser")
	# print(soup.prettify())
	snips = soup.find_all('fmxmlsnippet')
	for sn in snips:
		fields = sn.find_all('field')
		# print(len(fields))
		for f in fields:
			# print(f.prettify())
			try:
				if 'Calculated' == f['fieldtype']:
					try:
						calc = sn.find_all('calculation')
						text = calc[0].get_text()
						# print(text)
					except Exception as e:
						pass
			except Exception as e:
				pass
			try:
				fieldData.append({'table': file.replace('Fields-','').replace('.xml',''),'name': f['name'], 'type': f['fieldtype']})
				# if 'Calculated' == f['fieldtype']:
					# fieldData.append({'table': file.replace('Fields-','').replace('.xml',''),'name': f['name'], 'type': f['fieldtype']})
			except Exception as e:
				fieldData.append({'table': file, 'name': f['name'], 'type': ''})
				pass
def fieldList():
	global fieldData
	xmlFolder = 'D:\\_Scott\\S_Documents\\Projects\\Reph\\Docs\\DB\\structure_XML'
	dirList = os.listdir(xmlFolder)
	i = 0
	for item in dirList:
		path = xmlFolder + _v.slash + item
		if os.path.isfile(item) and 'Fields-' in item:
			i += 1
			# print(item)
			fieldInfo(path,item)

	companyUNC = xmlFolder + _v.slash + 'Fields-Company.xml'
	company = pathlib.Path(companyUNC).as_uri()

	_.tables.register('fieldData',fieldData)
	_.tables.print('fieldData','table,name,type')
	print()
	print('Fields:\t',len(fieldData))
	print()
	print('Tables:\t',i)
	print()



def scriptFields(scripts,file):
	global scriptData
	# print(len(scripts))
	for f in scripts:
		scriptData.append({'table': file, 'name': f['name']})
		groups = f.find_all('group')
		print(len(groups))
		# scriptFields(groups,file)
		# for x in list(f.children):
			# print(x)
		# for g in groups:
	# print()
	# print(len(groups))
	# print()


def scriptInfo(path,file):
	global scriptData
	f = open(path, 'r')
	s = f.read()
	# soup = BeautifulSoup(s,"lxml")
	soup = BeautifulSoup(s,"html.parser")
	# print(soup.prettify())



	# snips = soup.find_all('fmxmlsnippet')
	# for sn in snips:
	#     scripts = sn.find_all('script')
	#     scriptFields(scripts,file)
	#     groups = sn.find_all('group')
	#     # for g in groups:
	#     # print(len(groups))
	#     scriptFields(groups,file)




	code = ''
	for x in list(soup.children):
		code += str(x)
		# print(x)
	tree = html.fromstring(code)
	scripts = tree.cssselect('script')
	for script in scripts:
		try:
			name = str(script.attrib['name'])
			scriptData.append({'table': file, 'name': name})
		except Exception as e:
			pass
	




def scriptList():
	global scriptData
	xmlFolder = 'D:\\_Scott\\S_Documents\\Projects\\Reph\\Docs\\DB\\structure_XML'
	dirList = os.listdir(xmlFolder)
	i = 0
	for item in dirList:
		path = xmlFolder + _v.slash + item
		if os.path.isfile(item) and 'Scripts-' in item:
			i += 1
			# print(item)
			scriptInfo(path,item)



	# print(len(snips))



		# for x in list(sn.children):
			# print(x)

	_.tables.register('scriptData',scriptData)
	# tables.trigger('switches','switch,name',test,True)
	_.tables.print('scriptData','table,name')
	print()
	print('Scripts:\t',len(scriptData))
	print()
	print('Tables:\t',i)
	print()

def tableList(flds = False):
	global fieldData
	global fieldList
	dup = []
	path = 'all_fields.xml'
	f = open(path, 'r')
	s = f.read()
	soup = BeautifulSoup(s,"html.parser")

	code = ''
	for x in list(soup.children):
		code += str(x)
	tree = html.fromstring(code)
	tables = tree.cssselect('basetable')
	i = 0
	for tbl in tables:
		try:
			table = str(tbl.attrib['name'])
			# scriptData.append({'table': file, 'name': name})
			i += 1
			if not flds:
				print(table)
			else:
				########################
				fields = tbl.cssselect('field')
				# print(len(fields))
				for f in fields:
					# print(f.prettify())
					try:
						if 'Calculated' == f.attrib['fieldtype']:
							try:
								calc = sn.cssselect('calculation')
								text = calc[0].text_content()
								# print(text)
							except Exception as e:
								pass
					except Exception as e:
						pass
					try:
						fullname = table + '::' + f.attrib['name']
					except Exception as e:
						fullname = ''
					try:
						if f.attrib['name'] in fieldList and not fullname in dup:
							dup.append(fullname)
							fieldData.append({'idt': i,'table': table,'name': f.attrib['name'],'name2': f.attrib['name'].replace('_','0').lower(), 'type': f.attrib['fieldtype']})
						# if 'Calculated' == f['fieldtype']:
							# fieldData.append({'table': file.replace('Fields-','').replace('.xml',''),'name': f['name'], 'type': f['fieldtype']})
					except Exception as e:
						if f.attrib['name'] in fieldList and not fullname in dup:
							dup.append(fullname)
							fieldData.append({'idt': i,'table': table, 'name': f.attrib['name'], 'name2': f.attrib['name'].replace('_','0').lower(), 'type': ''})
						pass
				########################
		except Exception as e:
			pass
	_.switches.fieldSet('Sort','active',True)
	_.switches.fieldSet('Sort','value','idt,name2')
	_.tables.register('fieldData',fieldData)
	_.tables.print('fieldData','table,name,type')
	print()
	print('Fields:\t',len(fieldData))
	print()
	# print('Tables:\t',i)
	print()





def layoutInfo(path,file):
	global layoutData
	global scriptData
	f = open(path, 'r')
	s = f.read()

	soup = BeautifulSoup(s,"html.parser")


	code = ''
	for x in list(soup.children):
		code += str(x)
		# print(x)
	tree = html.fromstring(code)
	def scripts():
		items = tree.cssselect('script')
		for item in items:
			try:
				name = str(item.attrib['name'])
				# name = item.text_content()
				scriptData.append({'table': file, 'name': name})
			except Exception as e:
				pass
	def fields():
		items = tree.cssselect('name')
		for item in items:
			try:
				# name = str(item.attrib['name'])
				name = item.text_content()
				layoutData.append({'table': file, 'name': name})
			except Exception as e:
				pass

		items = tree.cssselect('field')
		for item in items:
			try:
				name = str(item.attrib['name'])
				table = str(item.attrib['table'])
				name = table + '::' + name
				# name = item.text_content()
				layoutData.append({'table': file, 'name': name})
			except Exception as e:
				pass

	fields()


def layoutList():
	global layoutData
	global scriptData
	xmlFolder = 'D:\\_Scott\\S_Documents\\Projects\\Reph\\Docs\\DB\\structure_XML'
	dirList = os.listdir(xmlFolder)
	i = 0
	for item in dirList:
		path = xmlFolder + _v.slash + item
		# if os.path.isfile(item) and 'Layouts-085' in item:
		if os.path.isfile(item) and 'Layouts-' in item:
			i += 1
			# print(item)
			try:
				layoutInfo(path,item)
			except Exception as e:
				pass



	# print(len(snips))



		# for x in list(sn.children):
			# print(x)

	tables = []
	for ld in layoutData:
		tables.append(ld['name'].split('::')[0])



	_.tables.register('layoutData',layoutData)
	# tables.trigger('switches','switch,name',test,True)
	# _.tables.print('layoutData','table,name')
	_.tables.print('layoutData','name')
	print()
	print('Fields:\t',len(layoutData))
	print()
	print(' in Tables:\t',len(set(tables)))
	print()
	print('Layouts:\t',i)
	print()






def action():
	# fieldList()
	# scriptList()
	tableList(True)
	# layoutList()

		
# fields = 'ID_Contact,ID_Company,one,ID_Refer,ID_Submit_Process,Description,_ID_Contact_Search,org temp2,Work Postal Code,_ID_Company_Interview,d_org_street,Table_Name,_ID_Search_Interview,ID,ID_Search_if_Active,ID_Submit,_CHECKID,guid,OB,ID_Both,Street_Check,DELETE_LIST_TMP,_Item_ID,SearchRelation,_Search_n_ID_Active Copy,ID_Group_ID_Contact,IDs,Search_Contact_ID,ID_History,ID_Email_Template,_Search_n_ID_Active,ID_Decision_Maker,ID_N_MODEL,_Table_ID,ID_Duplicate,ID_GC,ID_Search,Zip,email_template_name,ID_Affiliation,ID_Parent_Company,ID_History_Related,_WHO,CAN,OA,Type,_org_street,ID_Search_Contact,onlineProfileGUID'
fields = 'ID_History,_2nd_PHONE,ID_History_Status,_Table_ID_Search,_1st_FTF,_Saved_Search_Item_ID,ID_Email_Template,CAN,Saved_Search,Organization,_org_street,ID,OB,ID_Related_Search,_ID_Company_Interview,_1st_PHONE,email_template_name,ID_Company,DELETE_LIST_TMP,Affiliation_1,ID_History_Related,ID_Both,_popupIDcontact,ex,ID_Contact,Affiliation_2,_History_Selected_Search,_Search_n_ID_Active Copy,_TableName,Table_Name,_Table_ID,_HNC_ID_Search,_ID_CC,_Table_ID_Contact,_CHECKID,ID_Search,d_org_street,ID_Group_ID_Contact,WHO,guid,Work Postal Code,_3rd_PHONE,_Select_Group_Description,ID_N_MODEL,_SC_ID,_History_ID,_2nd_FTF,ID_Network,_Search_n_ID_Active,ID_Recruiter,ID_Affiliation,_ID_Contact_Search,ID_Submit,_H_Submittal,SearchName,_Selected_Affiliate_ID,Type,one,Street_Check,Description,Search_Contact_ID,TRn,Email_Template_Related,OA,ID_Interviewer_Main,onlineProfileGUID,IDs,ID_GC,org temp2,Zip,ID_Parent_Company,ID_Search_if_Active,ID_Submit_Process,TRt,ID_Decision_Maker,SearchID,ID_Search_Contact,FULL_PATH,_3rd_FTF,H_Type,temp_ID,SearchRelation,ID_Refer,_ID_Search_Interview,_History_Search_ID_Contact,_Contact_ID,ID_Reports_To,_Item_ID,ID_Duplicate,Email_Template_Name,_WHO,ID_Item'
fieldList = fields.split(',')
layoutData = []
fieldData = []
scriptData = []
# print(len(fieldList))
# sys.exit()
########################################################################################
if __name__ == '__main__':
	action()



# https://www.dataquest.io/blog/web-scraping-tutorial-python/