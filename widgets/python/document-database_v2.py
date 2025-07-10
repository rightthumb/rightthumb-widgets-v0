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
	_.switches.register( 'DB', '-db,-database' )
	_.switches.register( 'Location', '-location' )
	_.switches.register( 'Build', '-re,-rebuild,-build' )
	_.switches.register( 'Upload', '-u,-upload' )
	# _.switches.register( 'Extract-Data', '-extract' )
	_.switches.register( 'Additional-Data', '-add' )
	_.switches.register( 'Folders', '-fo,-folder,-fos,-folders' )
	_.switches.register( 'ZipFolder', '-zip', 'C:\\tech\\document-database' )
	# _.switches.register( 'Reprocess-Addresses', '-reprocess' )
	# _.switches.register( 'Reprocess-Headers', '-h,-head,-headers' )

	# _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
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
	'file': 'document-database.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Save meta and file content of documents, option of uploading to webapp',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'documents',
						'meta',
						'cache',
						'webapp',
						'vps',
						'app',
						'dev',
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
						_.hp('p document-database -reprocess'),
						_.hp('p document-database + resume -upload -zip C:\\tech\\document-database'),
						_.hp('p document-database + resume -upload -zip C:\\tech\\document-database -build'),
						_.hp('p document-database -extract + resume -build  -add ..\\File_Name_Title.csv ..\\indexDB.csv'),
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


########################################################################################




import simplejson
import sqlite3

def clean_field_names(field_names):
	cleaned_names = []
	for field_name in field_names:
		cleaned_name = ''.join(char for char in field_name if char.isalnum()).lower()
		cleaned_names.append(cleaned_name)
	return cleaned_names

def determine_column_types():
	column_types = []
	for field_name in _.v.dd.records[0].keys():
		column_type = None
		for row in _.v.dd.records:
			if isinstance(row[field_name], (int, float)):
				column_type = 'REAL'
				break
			elif isinstance(row[field_name], str):
				column_type = 'TEXT'
		if column_type is None:
			column_type = 'TEXT'
		column_types.append(column_type)
	return column_types

def create_sqlite_table(field_names, column_types):
	if _.switches.isActive('Build'):
		_.pr(_.v.dd.db,c='green')
		if os.path.isfile(_.v.dd.db):
			os.unlink(_.v.dd.db)
	else:
		if os.path.isfile(_.v.dd.db): return None
	_.switches.fieldSet( 'Build', 'active', True )
	conn = sqlite3.connect(_.v.dd.db)
	c = conn.cursor()
	column_names = ','.join(field_names)
	column_defs = ','.join([f'{name} {column_types[i]}' for i, name in enumerate(field_names)])
	create_table_query = f'CREATE TABLE {_.v.dd.table} ({column_defs})'
	c.execute(create_table_query)
	conn.commit()
	conn.close()



import sqlite3

def import_json_data(key='path'):


	def insert_all():
		conn = sqlite3.connect(_.v.dd.db)
		c = conn.cursor()

		for row in _.v.dd.records:
			values = [row[field_name] for field_name in row]
			print('INSERT',row[key])
			insert_query = f'INSERT INTO {_.v.dd.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
			# print(insert_query,values)
			# _.pv(values)
			c.execute(insert_query, values)
		conn.commit()
		conn.close()


	if _.switches.isActive('Build'):
		insert_all()
		return None
	conn = sqlite3.connect(_.v.dd.db)
	c = conn.cursor()

	for row in _.v.dd.records:
		# _.pv(_.v.dd.records)
		key_value = row.get(key, None)
		if key_value:
			c.execute(f"SELECT COUNT(*) FROM {_.v.dd.table} WHERE {key}=?", (key_value,))
			record_count = c.fetchone()[0]
			if record_count > 0:
				# Record exists, update it
				print('UPDATE',row[key])
				update_query = f'UPDATE {_.v.dd.table} SET {",".join([f"{field_name} = ?" for field_name in row])} WHERE {key}=?'
				values = [row[field_name] for field_name in row] + [key_value]
				c.execute(update_query, values)
				continue

		# Record doesn't exist or key is not set, insert it
		values = [row[field_name] for field_name in row]
		print('INSERT',row[key])
		insert_query = f'INSERT INTO {_.v.dd.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
		c.execute(insert_query, values)

	conn.commit()
	conn.close()






'''
try:
	import textract
except: pass

try:
	import docx2txt
except: pass

try:
	import win32com.client
except: pass

try:
	from PyPDF2 import PdfReader
except: pass

try:
	import PyPDF2
except: pass
'''



########################################################################################

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


########################################################################################
# pip install textract
# pip install docx2txt
# pip install PyPDF2
# pip install pdfminer.six


try: import textract
except: pass

# try: import docx2txt
# except: pass

try: import win32com.client
except: pass

# try: from PyPDF2 import PdfReader
# except: pass

# try: import PyPDF2
# except: pass

try: from pathlib import Path
except: pass

try: import docx
except: pass

import os
# import textract










# import os
# from pathlib import Path
# import docx
# from PyPDF2 import PdfFileReader
# from pyth.plugins.rtf15.reader import Rtf15Reader
# from pyth.plugins.plaintext.writer import PlaintextWriter

# def getContents44(file_path):
#     path = Path(file_path)
#     text = ""

#     try:
#         if path.suffix == ".docx":
#             doc = docx.Document(file_path)
#             full_text = []

#             for paragraph in doc.paragraphs:
#                 full_text.append(paragraph.text)

#             text = "\n".join(full_text)

#         elif path.suffix == ".pdf":
#             with open(file_path, 'rb') as f:
#                 pdf = PdfFileReader(f)
#                 text = "\n".join(page.extract_text() for page in pdf.pages)

#         elif path.suffix == ".rtf":
#             with open(file_path, 'rb') as f:
#                 doc = Rtf15Reader.read(f)
#                 text = PlaintextWriter.write(doc).getvalue()

#         else:
#             text = textract.process(file_path).decode("utf-8")
#     except Exception as e:
#         print(f"Error processing {file_path} with suffix {path.suffix}: {e}")

#     return text




def extract_headers_footers(path):
	try:
		headers = []
		footers = []
		doc = docx.Document(path)
		for section in doc.sections:
			for paragraph in section.header.paragraphs:
				headers.append(paragraph.text)
			for paragraph in section.footer.paragraphs:
				footers.append(paragraph.text)

		return "\n".join(headers), "\n".join(footers)
	except:
		return '',''



def getContents2(file_path):
	path = Path(file_path)
	text = ""
	header, footer = extract_headers_footers(file_path)
	try:
		if path.suffix == ".docx":
			doc = docx.Document(file_path)
			full_text = []

			for paragraph in doc.paragraphs:
				full_text.append(paragraph.text)

			text = "\n".join(full_text)
		else:
			text = textract.process(file_path).decode("utf-8")
	except Exception as e:
		text = ''

	parts = [header, text, footer]
	document = '\n'.join(parts).strip()
	return document


def getContents(path):
	fi=''
	if path.endswith('.txt') or path.endswith('.md'):
		fi = _.getText(path,raw=True)
	elif path.endswith('.pdf'):
		fi = ''
		try:
			pdf_file = open(path, 'rb')
			reader = PyPDF2.PdfReader(pdf_file)
			for page in reader.pages: fi += page.extract_text()+'\n'
		except:
			pass
	else:
		try:
			if path.endswith('.doc') or path.endswith('.rtf'):
				fi = textract.process(path)
			else:
				fi = docx2txt.process(path)
		except:
			word = win32com.client.Dispatch("Word.Application")
			word.visible = False
			wb = word.Documents.Open(path)
			doc = word.ActiveDocument
			fi = doc.Range().Text
			doc.Close()
			word.Quit()

	return fi




def cleaner(data):
	data = data.replace('\r','\n')
	data = data.replace('\t','    ')
	# while '     ' in data: data = data.replace('     ','    ')
	while '  ' in data: data = data.replace('  ',' ')
	lines=data.split('\n') 
	for i,line in enumerate(lines): lines[i] = line.strip()
	data = '\n'.join(lines)
	while '\n\n' in data: data = data.replace('\n\n','\n')
	return data.lower()



def process(path):
	path = __.path(path)
	shouldRun=True
	if path in _.v.dd.date:
		shouldRun=False
		if _.mod(path) > _.v.dd.date[path]:
			shouldRun=True


	if shouldRun:
		_.pr(path)
		
		try:
			fi = getContents2(path)
		except Exception as e:
			fi = getContents(path)
		fi = cleaner(fi)
		print(len(fi.split('\n')),len(fi.split(' ')))
		info = _dir.info(path)
		_info={}
		for k in info:
			if k in 'path name parent folder bytes size date_created date_modified date_accessed ce me ae ext week_of_year day_of_the_week month year ago'.split(' '):
				if type(info[k]) == float:
					_info[k]=int(str(info[k]).split('.')[0])
				else:
					_info[k]=info[k]
		_info['content']=fi
		global api
		for k in api: _info[k]=api[k]
		_info['machine']=_v.getMachineID().replace('{','').replace('}','')
		_info['uuid']=_v.md5(str(uuid.UUID(int=uuid.getnode())),True).replace('{','').replace('}','')

		if True or _.switches.isActive('Extract-Data'): #################################################################################################################################### EXTRACT
			for k in 'phone email website address'.split(' '):
				if not k in _info: _info[k] = ''

			if _.v.dd.additional_fields:
				for k in _.v.dd.additional_fields:
					if not k in _info: _info[k] = ''

			scan = _scan.imp.app.scan.process( fi, 'A02F28B2' )
			# _.pv(scan)
			for k in scan:
				if not k == 'self' and scan[k]:
					for dat in scan[k]:
						if not dat == 'dennis@theperformersnetwork.com' and not dat == '813-967-7127':
							# print('dat',dat)
							_info[k] = dat
							# break



			###########################################################

			# If the "phone" field is empty, scan for phone numbers
			if not 'phone' in _info:
				phone_numbers = extract_phone_numbers_regex(fi)
				if not phone_numbers: phone_numbers = extract_phone_numbers_phonenumbers(fi)
				# if not phone_numbers: phone_numbers = extract_phone_numbers_basic_loop(fi)
				# if not phone_numbers: phone_numbers = extract_phone_numbers_list_comprehension(fi)

				if phone_numbers:
					pn=[]
					for n in phone_numbers:
						n = format_phone_number(n)
						if not n == '813-967-7127':
							if n:
								pn.append(n)
					if pn:
						_info['phone'] = pn[0]

			
			if not 'email' in _info:
				emails = find_emails_regex(fi)
				if not emails: emails = find_emails_string_methods(fi)
				if not emails: emails = find_emails_basic_loop(fi)
				if not emails: emails = find_emails_list_comprehension(fi)
				if emails:
					e=[]
					for mail in emails:
						mail=mail.lower()
						if not mail == 'dennis@theperformersnetwork.com':
							e.append(mail)


					if e:
						_info['email'] = e[0]

			###########################################################
			if not 'address' in _info: _info['address'] = extract_mailing_address(fi)
			if not 'address' in _info: _info['address'] = extract_mailing_addressB(fi)
			if not 'address' in _info: _info['address'] = extract_mailing_address2(fi)

			###########################################################








			if _.v.dd.additional:
				test = 'path name'
				for t in test.split(' '):
					if _info[t] in _.v.dd.additional:
						for w in _.v.dd.additional[_info[t]]:
							# print('w',w)
							# _.pv(_.v.dd.additional[_info[t]])
							_info[w] = _.v.dd.additional[_info[t]][w]

		def _col_(n):
			return n.replace('_','').replace('-','')
		info={}
		for k in _info: info[_col_(k)] = _info[k]
		# _.pv(_info); sys.exit();
		_.v.dd.records.append(info)
		# _.v.dd.records.append({'file': path, 'content': fi})
		_.v.dd.date[path]=__.startTime
		_.v.dd.files.append(path)


def upload():
	if not _.switches.isActive('Upload'): return None
	import requests

	url = "https://eyeformeta.com/apps/documents/piller/u/"

	zip_file_path = _.v.dd.zip
	db_file_path = _.v.dd.db

	zip_file_name = __.path(zip_file_path).split(os.sep)[-1]
	db_file_name = __.path(db_file_path).split(os.sep)[-1]

	headers = {
		"User-Agent": "Mozilla/5.0",
		"APP-API-KEY": "e861e4f6",
	}

	files = {
		"zip_file": (zip_file_name, open(zip_file_path, "rb"), "application/zip"),
		"db_file": (db_file_name, open(db_file_path, "rb"), "application/octet-stream"),
	}

	response = requests.post(url, headers=headers, files=files)

	if response.status_code == 200:
		print("Files uploaded successfully.")
	else:
		print(f"Error uploading files: {response.status_code} {response.reason}")



def action():
	if _.switches.isActive('Reprocess-Headers'):
		Reprocess_Headers()
		return None


	load(); global documents;

	for path in documents:
		try:
			process(path)
		except Exception as e:
			_.pr(e,c='red')
	if _.v.dd.records:
		create_sqlite_table(clean_field_names(_.v.dd.records[0].keys()), determine_column_types())
		import_json_data()
		_.saveTable(_.v.dd.date,'document-database.meta')
		if _.switches.isActive('ZipFolder'):

			import shutil
			epoch = int(str(__.startTime).split('.')[0])
			fo = _.switches.values('ZipFolder')[0]+os.sep+str(epoch)
			_v.mkdir(fo)
			for path in _.v.dd.files:
				md = _hash.string( path )
				os.link(path,fo+os.sep+'__'+md+'.'+path.split('.')[-1].lower())
			shutil.make_archive(fo, 'zip', fo)
			_.v.dd.zip = fo+'.zip'
			upload()




def load():
	global api
	global documents
	if False:
		if not _.switches.isActive('ZipFolder'):
			_.switches.fieldSet( 'ZipFolder', 'active', True )
			if _.isWin:
				_.switches.fieldSet( 'ZipFolder', 'value', 'C:\\tech\\document-database' )
				_.switches.fieldSet( 'ZipFolder', 'values', ['C:\\tech\\document-database'] )
			else:
				_.switches.fieldSet( 'ZipFolder', 'value', '/mnt/c/tech/document-database' )
				_.switches.fieldSet( 'ZipFolder', 'values', ['/mnt/c/tech/document-database'] )

	if _.switches.isActive('DB'):
		_.v.dd.db=_.switches.values('DB')[0]
	elif _.switches.isActive('ZipFolder'):
		_.v.dd.db = _.switches.values('ZipFolder')[0]+os.sep+'documents.db'
	else:
		_.v.dd.db='documents.db'

	if _.switches.isActive('Location'):
		_.pr(_.v.dd.db,c='green')
		sys.exit()
	if _.switches.isActive('Reprocess-Addresses'):
		reprocess_addresses()
		sys.exit()

	gk = _v.tt+os.sep+'gatekeeper.api'
	if not os.path.isfile(gk):
		_gk = _.regImp( __.appReg, 'gatekeeper' )
		_gk.switch('Register')
		_gk.action()
		input('Hit ENTER when done.')

	_gk_ = _.getText(gk,clean=2,raw=True).split('\n')
	api = {
			'app': _gk_[0],
			'api': _gk_[1],
	}



	


	if _.switches.isActive('Folders'):
		folders=_.switches.values('Folders')
	else:
		folders=[os.getcwd()]

	if _.switches.isActive('Build'):
		_.v.dd.date = {}
	else:
		_.v.dd.date = _.getTable('document-database.meta')
	documents=[]
	if _.isData():
		for path in _.isData():
			if path.endswith('.doc') or path.endswith('.docx') or path.endswith('.pdf') or path.endswith('.md') or path.endswith('.rtf'):
				if not '\\~' in path:
					file=os.path.basename(path)
					if _.showLine(file):
						documents.append(path)

	else:
		for folder in folders:
			for path in _.fo(folder):
				if path.endswith('.doc') or path.endswith('.docx') or path.endswith('.pdf') or path.endswith('.md') or path.endswith('.rtf'):
					if not '\\~' in path:
						file=os.path.basename(path)
						if _.showLine(file):
							documents.append(path)



	_.v.dd.additional={}
	_.v.dd.additional_fields=[]
	if _.switches.isActive('Additional-Data'):
		indexes=[]
		for fi in _.switches.values('Additional-Data'):
			if _.getTextFirst(fi) == '{': indexes.append(_.getTable2(fi))
			else:
				if _.getTextFirst(fi) == '[': additional = _.getTable2(fi)
				else: additional = _.csv(fi)

				def index(data,field):
					dex={}
					for rec in data:
						sub=rec[field]
						del rec[field]
						dex[sub]=rec
					return dex

				if additional:
					if 'path' in additional[0]: indexes.append(index(additional,'path'))
					elif 'Path' in additional[0]: indexes.append(index(additional,'Path'))
					elif 'File' in additional[0]: indexes.append(index(additional,'File'))
					elif 'file' in additional[0]: indexes.append(index(additional,'file'))
					elif 'Name' in additional[0]: indexes.append(index(additional,'Name'))
					elif 'name' in additional[0]: indexes.append(index(additional,'name'))
		# _.pv(indexes);sys.exit();
		for dex in indexes:
			for x in dex:
				# print(x)
				for f in dex[x]:
					if not f in _.v.dd.additional: _.v.dd.additional[x]={}
					for k in dex[x]:
						if not k in _.v.dd.additional_fields: _.v.dd.additional_fields.append(k)
						_.v.dd.additional[x][k]=dex[x][k]
						# print(dex[x][k])
		# sys.exit()
	# _.pv(_.v.dd.additional)




########################################################

try:
	import usaddress # type: ignore
except: pass



def extract_mailing_address3(content):
	# Preprocess the content by replacing newlines with spaces and joining lines
	content = content.replace('\r\n', ' ').replace('\n', ' ')

	# Split the content into sentences using a simple approach
	sentences = content.split('. ')

	# Iterate through sentences to find an address
	for sentence in sentences:
		try:
			# Parse the address components
			parsed_address, address_type = usaddress.tag(sentence)
			
			# Check if the parsed address is a street address
			if address_type == 'Street Address':
				# Reconstruct the address from its components
				address = ', '.join([part for label, part in parsed_address.items()])
				return address
		except usaddress.RepeatedLabelError:
			pass
	
	return None



def extract_mailing_address2(content):
	# Address components regex
	street_regex = r'\d+\s+[\w\s]+'
	city_regex = r'[\w\s]+'
	state_regex = r'\b[A-Z]{2}\b'
	zip_code_regex = r'\d{5}'

	# Combined multi-line address regex
	address_regex = fr'({street_regex})\s*[\r\n]+({city_regex})\s*[\r\n]+({state_regex})\s+({zip_code_regex})'
	
	match = re.search(address_regex, content, re.MULTILINE)
	
	if match:
		street, city, state, zip_code = match.groups()
		return f'{street}, {city}, {state} {zip_code}'
	else:
		return None


def extract_mailing_address(content):
	content=content.replace('\t',' ')
	content=content.replace('\n',',')
	address_regex = r'\d+\s+[\w\s]+\,\s*\w+\,\s*\w+\s+\d{5}'
	match = re.search(address_regex, content)
	return match.group(0) if match else None

def extract_mailing_addressB(content):
	address_regex = r'\d+\s+[\w\s]+\,\s*\w+\,\s*\w+\s+\d{5}'
	match = re.search(address_regex, content)
	return match.group(0) if match else None
########################################################















def reprocess_addresses():


	# Connect to the SQLite database
	conn = sqlite3.connect(_.v.dd.db)
	cursor = conn.cursor()

	# Fetch all records with content and their ids
	cursor.execute('SELECT path, content, address FROM documents')
	rows = cursor.fetchall()

	# Update records with extracted addresses
	for row in rows:
		record_id, content, address = row
		mailing_address=address
		if not mailing_address: mailing_address = extract_mailing_address(content)
		if not mailing_address: mailing_address = extract_mailing_addressB(content)
		if not mailing_address: mailing_address = extract_mailing_address2(content)
		# if not mailing_address: mailing_address = extract_mailing_address3(content)
		if mailing_address:
			cursor.execute('UPDATE documents SET address = ? WHERE path = ?', (mailing_address, record_id))

	# Commit changes and close the connection
	conn.commit()
	conn.close()


import re

def extract_all_phone_numbers(text):
	# Formats: 813-555-2424, (813)555-2424, (813) 555-2424, 8135552424, 18135552424, 813.555.2424, etc.
	pattern = r'(\+?1\s*[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
	matches = re.finditer(pattern, text)

	formatted_phone_numbers = []
	for match in matches:
		# Remove any non-digit characters
		digits = re.sub(r'\D', '', match.group(0))

		# Format the phone number as 'XXX-XXX-XXXX'
		formatted_phone = f'{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}'
		formatted_phone_numbers.append(formatted_phone)

	return formatted_phone_numbers


def extract_email_addresses(text):
	pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	email_addresses = re.findall(pattern, text)
	return email_addresses


def skim_and_filter_numbers(content):
	result = ''
	sub=[]
	for subject in extract_all_phone_numbers(content):
		if not subject == '813-967-7127':
			sub.append(subject)
	if sub: result=sub[0]
	return result

# if not dat == 'dennis@theperformersnetwork.com' and not dat == '813-967-7127':
def skim_and_filter_emails(content):
	content=content.lower()
	result = ''
	sub=[]
	for subject in extract_email_addresses(content):
		if not subject == 'dennis@theperformersnetwork.com':
			sub.append(subject)
	if sub: result=sub[0]
	return result

def extract_headers_footers(path):
	try:
		headers = []
		footers = []
		doc = docx.Document(path)
		for section in doc.sections:
			for paragraph in section.header.paragraphs:
				headers.append(paragraph.text)
			for paragraph in section.footer.paragraphs:
				footers.append(paragraph.text)

		return "\n".join(headers)+"\n".join(footers)
	except:
		return ''

def Reprocess_Headers():
	if not _.switches.isActive('DB'): _.e('No DB','Specify a database')
	import sqlite3
	conn = sqlite3.connect(_.switches.value('DB'))
	cursor = conn.cursor()
	cursor.execute("SELECT path, name, phone, email FROM documents WHERE phone = '' OR email = '' ")
	rows = cursor.fetchall()
	for row in rows:
		path, name, phone, email = row
		print(name)
		text=extract_headers_footers(name)
		if not text: continue
		else: _.pr(name)
		ran=False
		if not phone.strip():
			phone = skim_and_filter_numbers(text)
			if phone: ran=True
		if not email.strip():
			email = skim_and_filter_emails(text)
			if email: ran=True
		if ran:
			_.pr('ran:',name)
			cursor.execute("UPDATE documents SET phone = ? WHERE path = ?", (processed_phone, path))
	conn.commit()
	conn.close()


_.v.dd = _.dot()
_.v.dd.records=[]

_.v.dd.table = 'documents'
_.v.dd.files = []
_.v.dd.date = {}
# os=__.imp('os.getcwd')
# os=__.imp('os.unlink')
# os=__.imp('os.link')
# os=__.imp('os.path.basename')
# os=__.imp('os.path.isfile')


# linux
	# sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 
	# pip3 install textract python-docx

# p document-database -extract -build  -add ../File_Name_Title.csv  ../indexDB.csv ../File_Name_Title_set2.csv

# C:\Users\Scott\.rt\profile\daily\2023\17\04-25\piller\Resumes

# win
	# https://www.xpdfreader.com/download.html
	# pip3 install pyth
	# antiword-0_37-windows.zip
	# https://softpedia-secure-download.com/dl/e91a8dad5055ba276a0282d92eff439e/64498b56/100136188/software/office/antiword-0_37-windows.zip


##################################################
# def action(): dive_in_MF(_.switches.values('DB')[0])
##################################################

_scan = _.regImp( __.appReg, 'record-cleaner' )

import phonenumbers
import uuid
import _rightThumb._dir as _dir
import _rightThumb._md5 as _hash
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


# import_json_data
# process

