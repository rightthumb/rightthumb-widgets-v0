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


##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	_.switches.register( 'DB', '-db' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] },
		},
	}


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start



import sqlite3
import re
import phonenumbers

# Phone number extraction methods
def extract_phone_numbers_regex(text):
	pattern = re.compile(r'(\+?\d{1,2}\s?)?(\d{3}|\(\d{3}\))\s?\d{3}[-\.\s]?\d{4}')
	return pattern.findall(text)

def extract_phone_numbers_phonenumbers(text, region="US"):
	phone_numbers = []
	for match in phonenumbers.PhoneNumberMatcher(text, region):
		phone_numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
	return phone_numbers

# Email extraction methods
def find_emails_regex(text):
	pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
	return pattern.findall(text)

# Phone number formatting method
def format_phone_number(phone_number):
	# Remove all non-numeric characters
	digits = ''.join(filter(str.isdigit, phone_number))
	# Check if the phone number has the correct number of digits
	if len(digits) != 10:
		return ''
		# print(phone_number)
		# raise ValueError("Invalid phone number length. Expected 10 digits.")
	# Format the phone number as (xxx) xxx-xxxx
	formatted_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
	return formatted_number




def extract_phone_numbers_basic_loop(text):
	phone_numbers = []
	number = ''
	for char in text:
		if char.isdigit():
			number += char
			if len(number) == 10:
				phone_numbers.append(number)
				number = ''
		elif number:
			number = ''
	return phone_numbers

def extract_phone_numbers_list_comprehension(text):
	digits = ''.join(filter(str.isdigit, text))
	return [digits[i:i+10] for i in range(0, len(digits), 10) if len(digits[i:i+10]) == 10]



def find_emails_string_methods(text):
	emails = []
	words = text.split()
	for word in words:
		if '@' in word and '.' in word:
			emails.append(word)
	return emails


def find_emails_basic_loop(text):
	emails = []
	email = ''
	for char in text:
		if char.isalnum() or char in ['@', '.', '_', '-']:
			email += char
		elif email and '@' in email and '.' in email:
			emails.append(email)
			email = ''
		else:
			email = ''
	if email and '@' in email and '.' in email:
		emails.append(email)
	return emails

def find_emails_list_comprehension(text):
	words = text.split()
	return [word for word in words if '@' in word and '.' in word]



def dive_in_MF(db_path):
	# Connect to the SQLite database
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()

	# Select all records from the "documents" table
	cursor.execute('SELECT content, phone, email, path  FROM documents')
	records = cursor.fetchall()

	for record in records:
		# print(record)
		# Extract the relevant fields from the record
		i=-1
		i+=1; content = record[i].lower().replace('(','').replace(') ','-').replace(')','-')
		i+=1; phone = record[i]
		i+=1; email = record[i]
		i+=1; path = record[i]
		if not _.showLine(path): continue
		print(path)
		# content = record['content'].lower()
		# phone = record['phone']
		# email = record['email']
		# path = record['path']

		# If the "phone" field is empty, scan for phone numbers
		if not phone:
			phone_numbers = extract_phone_numbers_regex(content)
			if not phone_numbers: phone_numbers = extract_phone_numbers_phonenumbers(content)
			# if not phone_numbers: phone_numbers = extract_phone_numbers_basic_loop(content)
			# if not phone_numbers: phone_numbers = extract_phone_numbers_list_comprehension(content)

			if phone_numbers:
				pn=[]
				for n in phone_numbers:
					n = format_phone_number(n)
					if not n == '813-967-7127':
						if n:
							pn.append(n)
				if pn:
					phone = pn[0]

		# If the "email" field is empty, scan for emails
		if not email:
			emails = find_emails_regex(content)
			if not emails: emails = find_emails_string_methods(content)
			if not emails: emails = find_emails_basic_loop(content)
			if not emails: emails = find_emails_list_comprehension(content)
			if emails:
				e=[]
				for mail in emails:
					mail=mail.lower()
					if not mail == 'dennis@theperformersnetwork.com':
						e.append(mail)


				if e:
					email = e[0]

		# Update the record with the extracted information
		cursor.execute('''
			UPDATE documents
			SET phone = ?, email = ?
			WHERE path = ?
		''', (phone, email, path))

	# Commit the changes and close the connection
	conn.commit()
	conn.close()



def action():
	dive_in_MF(_.switches.values('DB')[0])


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)