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
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'record-cleaner.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'clean fields and move data to appropriate fields',
	'categories': [
						'json',
						'clean',
						'data',
						'form',
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START



import re


class Address:
	def __init__( self ):
		self.cities_fl = _.getTableDB( 'florida-cities.list' )
		self.cities = [
						'Cypress',
						'Bulverde',
						'Efland',
						'Thomasville',
						'Springfield',
		]


	def fixCity( self, address ):
		for city in self.cities_fl:
			city=city.replace('.','').replace("'",'')
			if city.lower() in address.lower():
				for subject in _.caseUnspecific( address, city ):
					address = address.replace('\n'+subject,', '+city)
					address = address.replace(subject,', '+city)
				if not 'fl' in address.lower():
					address = address.replace(city,city+', Fl ')

		for city in self.cities:
			city=city.replace('.','').replace("'",'')
			if city.lower() in address.lower():
				for subject in _.caseUnspecific( address, city ):
					address = address.replace('\n'+subject,', '+city)
					address = address.replace(subject,', '+city)
		return address

	def hasCity( self, address ):
		for city in self.cities_fl:
			city=city.replace('.','').replace("'",'')
			if city.lower() in address.lower():
				return True
		return False


	def shorten_rd( self, address ):
		'''Completes the road type. I.e. Rd becomes Road, st becomes Street as per Google etc.'''
		address = address.title()
		address = re.sub(r" Street(?=$| [NE(So|S$)(We|W$)])", ' St', address)
		address = re.sub(r" Road(?=$| [NE(So|S$)(We|W$)])", ' Rd', address)
		address = re.sub(r"(?<!The) Avenue(?=$| [NE(So|S$)(We|W$)])", ' Ave', address)
		address = re.sub(r" Close(?=$| [NE(So|S$)(We|W$)])", ' Cl', address)
		address = re.sub(r" Court(?=$| [NE(So|S$)(We|W$)])", ' Ct', address)
		address = re.sub(r"(?<!The) Crescent(?=$| [NE(So|S$)(We|W$)])", ' Cres', address)
		address = re.sub(r" Boulevarde?(?=$| [NE(So|S$)(We|W$)])", ' Blvd', address)
		address = re.sub(r" Drive(?=$| [NE(So|S$)(We|W$)])", ' Dr', address)
		address = re.sub(r" Lane(?=$| [NE(So|S$)(We|W$)])", ' Ln', address)
		address = re.sub(r" Place(?=$| [NE(So|S$)(We|W$)])", ' Pl', address)
		address = re.sub(r" Square(?=$| [NE(So|S$)(We|W$)])", ' Sq', address)
		address = re.sub(r"(?<!The) Parade(?=$| [NE(So|S$)(We|W$)])", ' Pde', address)
		address = re.sub(r" Circuit(?=$| [NE(So|S$)(We|W$)])", ' Cct', address)
		return address

	def lengthen_rd( self, address ):
		address = address.title()
		address = re.sub(r" St(?=$| [NE(So|S$)(We|W$)])", " Street", address)
		address = re.sub(r" Rd(?=$| [NE(So|S$)(We|W$)])", " Road", address)
		address = re.sub(r" Ave(?=$| [NE(So|S$)(We|W$)])", " Avenue", address)
		address = re.sub(r" Cl(?=$| [NE(So|S$)(We|W$)])", " Close", address)
		address = re.sub(r" Ct(?=$| [NE(So|S$)(We|W$)])", " Court", address)
		address = re.sub(r" Cres(?=$| [NE(So|S$)(We|W$)])", " Crescent", address)
		address = re.sub(r" Blvd(?=$| [NE(So|S$)(We|W$)])", " Boulevard", address)
		address = re.sub(r" Dr(?=$| [NE(So|S$)(We|W$)])", " Drive", address)
		address = re.sub(r" Ln(?=$| [NE(So|S$)(We|W$)])", " Lane", address)
		address = re.sub(r" Pl(?=$| [NE(So|S$)(We|W$)])", " Place", address)
		address = re.sub(r" Sq(?=$| [NE(So|S$)(We|W$)])", " Square", address)
		address = re.sub(r" Pde(?=$| [NE(So|S$)(We|W$)])", " Parade", address)
		address = re.sub(r" Cct(?=$| [NE(So|S$)(We|W$)])", " Circuit", address)
		return address

	def standard_addr( self, address ):
		'''Checks for unit numbers and street addresses and puts them in the standard format''' 
		#print("################################")
		#print("### Address: ", address)
		unit_nums = re.findall(r"(?<=Unit )\w?\d+\w?|(?<=U)\d+\w?|\w?\d+\w?(?=\s*/)", address)
		unit_num = unit_nums[0] if len(unit_nums)==1 else ""
		#print("Unit Number: ", unit_num)
		proc_addr = re.sub(r"Unit \w?\d+\w?/?|U\d+\w?/?|\w?\d+\w?\s*/", "", address)
		proc_addr = re.sub(r"^[,\- ]+|[,\- ]+$", "", proc_addr)
		#print("Unitless address: ", proc_addr)
		type_opts = r"Terrace|Way|Walk|St|Rd|Ave|Cl|Ct|Cres|Blvd|Dr|Ln|Pl|Sq|Pde|Cct"
		road_attrs_pattern = r"(?P<rd_no>\w?\d+(\-\d+)?\w?\s+)(?P<rd_nm>[a-zA-z \d\-]+)\s+(?P<rd_tp>" + type_opts + ")"
		#print("Road Attr Pattern: ", road_attrs_pattern)
		road_attrs = re.search(road_attrs_pattern, proc_addr)
		try:
			road_num = road_attrs.group('rd_no').strip()
		except AttributeError:
			road_num = ""
		#print("Road number: ", road_num)
		try:
			road_name = road_attrs.group('rd_nm').strip()
		except AttributeError:
			road_name = ""
		#print("Road name: ", road_name)
		try:
			road_type = road_attrs.group('rd_tp').strip()
		except AttributeError:
			road_type = ""
		#print("Road type: ", road_type)
		proc_addr = self.lengthen_rd(re.sub(r"^[,\- ]+|[,\- ]+$", "", re.sub(road_attrs_pattern, "", proc_addr)))
		#print("Leftover: ", proc_addr)

		unit_seg = (unit_num + "/" if unit_num!="" else "") if road_num != "" else ("Unit " + unit_num + ", " if unit_num!="" else "")
		road_seg = ((road_num + " " if road_num!="" else "") + road_name + " " + road_type).strip()
		post_road_seg = " " + proc_addr if proc_addr != "" else ""
		proc_addr = (unit_seg + road_seg) + post_road_seg
		#print("### Processed Address: ", proc_addr)
		return proc_addr

	def miniClean( self, aa ):
		aa = aa.replace('Fl, Fl','Fl')
		aa = aa.replace(', ,',',')
		aa = aa.replace(',',', ')
		aa = aa.replace(' ,',',')
		aa = aa.replace(',',', ')
		aa = aa.replace(' .','.')
		aa = aa.replace(' .','.')
		aa = aa.replace(', ,',',')
		aa = aa.replace(',,',',')
		aa = aa.replace('\r','')
		aa = aa.replace('\t',' ')
		aa = aa.replace(' \n','\n')
		aa = aa.replace('\n ','\n')
		aa = aa.replace('\n,','\n')
		aa = _str.replaceDuplicate(aa,' ')
		aa = _str.replaceDuplicate(aa,'\n')
		aa = _str.cleanBE(aa,' ')
		aa = _str.cleanBE(aa,'\n')
		return aa

	def process( self, address ):
		address = self.shorten_rd(self.standard_addr(address))
		address = self.miniClean(address)
		address = address.replace('United States','')
		address = address.replace('United States','')
		address = address.replace('United St Ates','')
		address = address.replace('Florida','Fl')
		address = address.replace('fl','Fl')
		address = address.replace('FL','Fl')
		address = address.replace(' Fl',', Fl')
		address = address.replace(',,',',')
		address = address.replace('.','')
		address = address.replace('L O L','Land O Lakes ')
		address = address.replace('Land O Lake,','Land O Lakes,')
		address = address.replace('Bradington','Bradenton')
		address = address.replace('Cl Earwater','Clearwater')
		address = address.replace('Pl Ant','Plant')
		address = address.replace('St Pete','St Petersburg')
		address = address.replace('Saint Petersburg','St Petersburg')
		address = address.replace('St Petersburgrsburg','St Petersburg')
		address = address.replace('Bch','Beach')
		address = address.replace('0,','0')
		address = address.replace('1,','1')
		address = address.replace('2,','2')
		address = address.replace('3,','3')
		address = address.replace('4,','4')
		address = address.replace('5,','5')
		address = address.replace('6,','6')
		address = address.replace('7,','7')
		address = address.replace('8,','8')
		address = address.replace('9,','9')
		address = address.replace('0/','0')
		address = address.replace('1/','1')
		address = address.replace('2/','2')
		address = address.replace('3/','3')
		address = address.replace('4/','4')
		address = address.replace('5/','5')
		address = address.replace('6/','6')
		address = address.replace('7/','7')
		address = address.replace('8/','8')
		address = address.replace('9/','9')
		address = self.miniClean(address)
		address = self.miniClean(address)
		address = self.fixCity(address)
		address = self.miniClean(address)
		address = self.miniClean(address)
		address = address.replace('Fl, Fl','Fl')
		address = address.replace(', 0',', Fl 0')
		address = address.replace(', 1',', Fl 1')
		address = address.replace(', 2',', Fl 2')
		address = address.replace(', 3',', Fl 3')
		address = address.replace(', 4',', Fl 4')
		address = address.replace(', 5',', Fl 5')
		address = address.replace(', 6',', Fl 6')
		address = address.replace(', 7',', Fl 7')
		address = address.replace(', 8',', Fl 8')
		address = address.replace(', 9',', Fl 9')
		address = address.replace('Fl0',', Fl 0')
		address = address.replace('Fl1',', Fl 1')
		address = address.replace('Fl2',', Fl 2')
		address = address.replace('Fl3',', Fl 3')
		address = address.replace('Fl4',', Fl 4')
		address = address.replace('Fl5',', Fl 5')
		address = address.replace('Fl6',', Fl 6')
		address = address.replace('Fl7',', Fl 7')
		address = address.replace('Fl8',', Fl 8')
		address = address.replace('Fl9',', Fl 9')
		address = address.replace(',\n','\n')
		address = address.replace('Clearwater, Beach','Clearwater Beach')
		address = address.replace('Clearwater Beach','Clearwater')
		address = address.replace('New, Port Richey','New Port Richey')
		address = address.replace('Fl, Tx','Tx')
		address = self.miniClean(address)
		address = self.miniClean(address)
		address = self.lengthen_rd(address)
		return address



class Record:
	def __init__( self, index=None ):
		# address email phone name website notes
		# BillingName ContactName BillingAddress ShippingAddress Email Phone Mobile Website Notes
		self.index = {

					'fields': {
						'BillingName': 'name',
						'ContactName': 'name',
						'BillingAddress': 'address',
						'ShippingAddress': 'address',
						'Email': 'email',
						'Phone': 'phone',
						'Mobile': 'phone',
						'Website': 'website',
						'Notes': 'notes',
					},
					'order': {
						'overflow': {'field':None, 'location': 'last' , 'delim': '\n'},
						'notes': ['Notes'],
						'name': ['BillingName'],
						'phone': ['Mobile','Phone'],
						'email': ['Email'],
						'address': ['BillingAddress','ShippingAddress'],
						'website': ['Website'],
					},
					'count': {},
		}
		if not index is None:
			self.index=index
		for k in self.index['fields']:
			if not k in self.index['count']:
				self.index['count'][k]=0
			self.index['count'][k]+=1

	def process( self, record ):
		record=self.run(record)
		record=self.run(record)
		return record
	def run( self, record ):
		record = self.scan(record)
		for key in record:
			if key in self.index['fields']:
				subject = self.index['fields'][key]
				if False:
					pass
				elif subject == 'email':
					record[key] = app.email.process( record[key] )
				elif subject == 'phone':
					record[key] = app.phone.process( record[key] )
				elif subject == 'website':
					record[key] = app.website.process( record[key] )
				elif subject == 'name':
					record[key] = app.text.process( record[key] )
				elif subject == 'notes':
					record[key] = app.text.process( record[key] )
				elif subject == 'text':
					record[key] = app.text.process( record[key] )
				elif subject == 'overflow':
					record[key] = app.text.process( record[key] )
				elif subject == 'address':
					record[key] = app.address.process( record[key] )
		return record
	def scan( self, record ):
		# print(5)
		for key in record:
			if key in self.index['fields']:
				subject = self.index['fields'][key]
				scan = app.scan.process( record[key], subject )
				for yek in scan:
					if yek == 'self':
						record[key] = scan[yek]
					else:
						for fix in scan[yek]:
							placed = False
							for field in self.index['order'][yek]:
								if not len(record[field]):
									record[field] = fix
									placed = True
							if not placed:
								# 'overflow': {'field':None, 'location': 'last' , 'delim': '\n'},
								fx = self.index['order']['overflow']['field']
								lx = self.index['order']['overflow']['location']
								if 'delim' in self.index['order']['overflow']:
									delim = self.index['order']['overflow']['delim']

								if type(fx) == str:
									record[fx] = fix + '\n' + record[fx]
								else:
									if lx == 'last':
										to = self.index['order'][subject][-1]
									elif lx == 'first':
										to = self.index['order'][subject][0]
									record[to] += delim + record[to]
		return record


# ** 
# dont forget to format field in scan class
# ** 

class Phone:
	def __init__( self ):
		pass

	def process( self, data ):
		data=data.replace('\r','')
		data=data.replace('\n','')
		data=data.replace('+','')
		for item in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", data):
			item = item.group(0)
			clean=''
			for x in item:
				if x in '0123456789':
					clean+=x
			data = data.replace(item,clean)
			if data.startswith('1 '):
				data=data[2:]
			if data.startswith('+1 '):
				data=data[3:]
			if data.startswith(' '):
				data=data[1:]
		test=''
		for x in data:
			if x in '0123456789':
				test+=x
		if len(test)==10:
			data=test
		if len(data)==11 and data.startswith('1'):
			data=data[1:]
		p=[]
		for y in data.split(' '):
			if len(y) == 10:
				try:
					y=format(int(y[:-1]), ",").replace(",", "-") + y[-1]
				except Exception as e:
					pass
			p.append(y)
		data=' '.join(p)
		return data

class Website:
	def __init__( self ):
		pass

	def process( self, data ):
		return data

class Email:
	def __init__( self ):
		pass

	def process( self, data ):
		return data

class Scanner:
	def __init__( self ):
		sample = {'self': 'new', 'phone': [app.phone.process('813-690-1260')]}
		pass

	def process( self, data, subject='A02F28B2' ):
		data=data.replace('),',')')
		# address email phone name website notes
		bk=data
		dic = {}

		# if not subject == 'phone':
		# 	for line in data.split('\n'):
		# 		found=False
		# 		for item in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", line):
		# 			found=True
		# 		if found:
		# 			if not 'phone' in dic:
		# 				dic['phone'] = []
		# 			dic['phone'].append(line)
		# 			data = data.replace(line,'')



		if not subject == 'phone':
			for item in re.finditer(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", data):
				item = item.group(0)
				# item = str(item)
				if not 'phone' in dic:
					dic['phone'] = []
				if not item in dic['phone']:
					dic['phone'].append(item)
				data = data.replace(item,'')

		if not subject == 'email':
			for item in re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data.lower()):

				# item = item.group(0)
				if not 'email' in dic:
					dic['email'] = []
				if not item in dic['email']:
					dic['email'].append(item)
				for clean in _.caseUnspecific( data, item ):
					data = data.replace(clean,'')

		if not subject == 'website':
			try:
				url = re.search("(?P<url>https?://[^\s]+)", data).group("url")
			except Exception as e:
				url = None
			if not url is None:
				if not 'website' in dic:
					dic['website'] = []
				dic['website'].append(url)
				data = data.replace(url,'')

			# for item in re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', data):
			# 	# item = item.group(0)
			# 	if not 'website' in dic:
			# 		dic['website'] = []
			# 	dic['website'].append(item)
			# 	data = data.replace(item,'')

		if not subject == 'address':
			for item in re.findall("[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}", data):
				# item = item.group(0)
				if not 'address' in dic:
					dic['address'] = []
				dic['address'].append(item)
				data = data.replace(item,'')
		if not bk == data:
			dic['self'] = data
		# return {}
		return dic

class Flags:
	def __init__( self ):
		pass

	def process( self, data ):
		return data

class dot:
	def __init__( self ):
		pass

app = dot()
app.record = Record()
app.email = Email()
app.address = Address()
app.phone = Phone()
app.website = Website()
app.text = Website()
app.scan = Scanner()
app.flags = Flags()



# x=app.scan.process( '(727) 443-7736', 'asdf' )
# x=app.scan.process( 'Don 813-469-3530	', 'asdf' )
# x=app.scan.process( 'scott.reph@gmail.com', 'asdf' )
# x=app.scan.process( '44 West 22nd Street, New York, NY 12345', 'asdf' )
# x=app.scan.process( 'https://eyeformeta.com/', 'asdf' )
# x=app.scan.process( 'https://www.google.com/search?q=python+extract+all+email+addresses&rlz=1C1RXQR_enUS929US929&sxsrf=APq-WBtrxEUFvbpwqXq7AKj6b2YrJ3NrUw%3A1643384417889&ei=YQ70Ya-8Ne6MwbkPmp6S4Ac&oq=python+extract+all+email+&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCCEQoAEyBQghEKABMgUIIRCrAjIFCCEQqwI6BwgAEEcQsAM6CggAEIAEEIcCEBQ6BQgAEIAEOgYIABAWEB46CAghEBYQHRAeSgQIQRgASgQIRhgAUOAKWOwWYLIqaAFwAngAgAFtiAHmBZIBAzkuMZgBAKABAcgBCMABAQ&sclient=gws-wiz', 'asdf' )
# x=app.scan.process( 'mailto:lorrainemsmith1517@gmail.com;mailto:trader1@mindspring.com;mailto:claytonfrank@hotmail.com', 'asdf' )
# print(x)
# sys.exit()



def action():
	pass

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




