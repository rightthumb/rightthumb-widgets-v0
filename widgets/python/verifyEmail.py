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
import re
import dns.resolver
import socket
import smtplib
# import simplejson as json
import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Email', '-email','example@example.com')
# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p thisApp -file file.txt')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Column',formatColumns)
_.switches.process()


# _.tables.trigger(field,script,includes = False)

if _.switches.isActive('File_'):
	file = _.switches.value('File')
	variable = _.getTable(file)
	_.saveTable(xRefList,file)

	variable = _.getTable2(file)
	_.saveTable2(xRefList,file)

	line = _str.replaceAll(line,'  ',' ')
	line = _str.cleanFirst(line,' ')
	line = _str.cleanLast(line,' ')
	line = _str.cleanSpecial(line)
	line = _str.totalStrip(line)
	line = _str.removeAll(line)
	line = _str.replaceDuplicate(line,' ')
	_.tables.register('xRef',xRefList)
	_.tables.get('xRef','fileName')
	

	file = _.switches.value('Files')
	_.tables.register('toCheck')
	_.tables.get('toCheck',file)
	_.tables.register('processes')
	_.tables.get('processes','processes')

	_.tables.trigger('xRef','date',_.float2Dated,True)
	_.tables.sort('xRef', 'name')
	
	_.switches.fieldSet('Sort','active',True)
	_.switches.fieldSet('Sort','value','name')

	testTable = []
	testTable.append({'name': 'Scott', 'age': '37'})
	testTable.append({'name': 'Sarah', 'age': '55'})
	testTable.append({'name': 'Sam', 'age': '22'})
	_.tables.register('test_table',testTable)
	_.tables.print('test_table','name,age')

	_.tables.registerView('test_table','sample','name','name')
	_.tables.registerView('test_table','sample2','age,name','desc.name')
	_.tables.registerView('test_table','sample3','name,age','age')
	# _.tables.registerView('tableName','viewName','includeField1,name','desc.sortBy')
	_.tables.view('test_table','sample')
	_.tables.view('test_table','sample2')
	_.tables.view('test_table','sample3')

	_.switches.print()

	if _.switches.exists('Column2'):
		print('This is a valid switch')

	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)1111
	_.switches.fieldSet('Sort','value','name')
	_.switches.fieldGet('Column','pos')

	i = 0
	for value in _.switches.value('Plus'):
		p[i] = _.svc(value)
		i += 1



	if _.switches.isActive('Output') == True:
		_.saveTable2(jsonFile,_.switches.value('Output'))
		_.saveText(convertedFile,_.ci(_.switches.value('Output')))

	if _.switches.isActive('Move') == True:
			shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
	# if _.showLine(string):
		# print(line)
pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if not pipeData[0][0] in _str.safeChar:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass

########################################################################################
def action():
	email_address = _str.totalStrip(_.ci(_.switches.value('Email')))
	print(email_address)
	#Step 1: Check email
	#Check using Regex that an email meets minimum requirements, throw an error if not
	addressToVerify = email_address
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

	# if match == None:
	#     print('Bad Syntax in ' + addressToVerify)
	#     print('N')
	#     sys.exit()
		# raise ValueError('Bad Syntax')

	#Step 2: Getting MX record
	#Pull domain name from email address
	domain_name = email_address.split('@')[1]

	#get the MX record for the domain
	records = dns.resolver.query(domain_name, 'MX')
	mxRecord = records[0].exchange
	mxRecord = str(mxRecord)
	print()
	print(mxRecord)
	print()
	#Step 3: ping email server
	#check if the email address exists

	# Get local server hostname
	host = socket.gethostname()

	# SMTP lib setup (use debug level for full output)
	server = smtplib.SMTP()
	server.set_debuglevel(0)

	# SMTP Conversation
	server.connect(mxRecord)
	server.helo(host)
	server.mail('scott.reph@gmail.com')
	code, message = server.rcpt(str(addressToVerify))
	server.quit()

	# Assume 250 as Success
	if code == 250:
		print('Y')
	else:
		print('N')



########################################################################################
if __name__ == '__main__':
	action()





