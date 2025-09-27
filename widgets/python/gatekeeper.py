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
import sys, time, os
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
	_.switches.register( 'NewProject', '-new,-project,-register', 'RightThumb.com' )
	_.switches.register( 'AddUser', '-u,-user', 'Scott 813-555-2424' )
	_.switches.register( 'API', '-api', 'ecf5c74ae83545feac983e5f526bb4ff' )
	_.switches.register( 'Register', '-r,-register' )


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
	'file': 'gatekeeper.py',
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
						_.hp('p gatekeeper'),
						_.hp('p gatekeeper'),
						_.hp('p gatekeeper -project RightThumb.com'),
						_.hp('p gatekeeper -user Scott 813-555-2424'),
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










# def scanner(folder):
	# global gatekeeper
	# global gatepath
	# fo=folder
	# i=0
	# while not os.path.isfile( folder+os.sep+_.v.gateFi ):
	#     print(folder+os.sep+_.v.gateFi)
	#     # print(os.path.isfile( folder+os.sep+'.folder.meta'+end ),folder+os.sep+'.folder.meta'+end)
	#     i+=1
	#     if i > 100:
	#         _.e('missing folder meta')
	#     try:
	#         folder = __.path(folder,pop=True)
	#     except Exception as e:
	#         break
	# if os.path.isfile(folder+os.sep+_.v.gateFi):
	#     gatekeeper=_.getYML(folder+os.sep+_.v.gateFi)
	#     # gatekeeper['path']=folder+os.sep+_.v.gateFi
	#     if not type(gatekeeper) == dict: gatekeeper = {}
	#     gatepath = folder+os.sep+_.v.gateFi
	# else:
	#     gatekeeper = {}
	#     gatepath = fo+os.sep+_.v.gateFi
	# return gatekeeper, gatepath





import os

class Gatekeeper:
	def __init__(self):
		# Define the filename to search for
		self.filename = '.gatekeeper_7ea5cf8b'

	def yamlIndex(self, index):
		# Open the file for reading
		with open(index, 'r') as file:
			# Initialize an empty dictionary
			dictionary = {}

			# Loop through each line of the file
			for line in file:
				# Split the line into the hash and phone number using the colon separator
				parts = line.split(':')

				# Add the hash and phone number to the dictionary
				dictionary[parts[0]] = parts[1].strip()

		# Return the dictionary
		return dictionary

	def scan(self):
		# Get the current directory
		directory = os.getcwd()

		# Loop through each parent directory until we reach the root
		while directory != '/'  and not directory[1:] == ':\\':
			# print(directory)
			# Check if the file exists in the current directory
			if os.path.exists(f'{directory}/{self.filename}'):
				# print(f'Found {self.filename} in {directory}')
				return self.yamlIndex(f'{directory}/{self.filename}')
				break

			# Go up one level to the parent directory
			directory = os.path.dirname(directory)

		# If we reached the root and still haven't found the file, it doesn't exist
		if directory == '/' or directory[1:] == ':\\':
			return {}


def scanner(folder):

	gk = Gatekeeper()
	gatekeeper=gk.scan()
	print(gatekeeper)






def create(project):
	folder=os.getcwd()
	fi=folder+os.sep+_.v.gateFi
	print(fi)
	_.saveTable2( config, fi )


def addUser(name,phone):
	global gatekeeper

def text():
	_sms = _.regImp( __.appReg, 'vps-srv-7facG-twilio-send' )
	_sms.imp.action( to='813-690-1260', body='thank you' )
	


def editor(path):
	_file_open = _.regImp( __.appReg, 'file-open' )
	_file_open.switch('App',_v.meta['code_editor'])
	_file_open.switch('Files',path)
	_file_open.action()
	_.pr(path)
	# _.pr(_v.meta['code_editor'],path)


def action():
	if _.switches.isActive('Register'):
		import webbrowser
		url = 'https://eyeformeta.com/apps/gatekeeper/api/'
		webbrowser.open(url, new=2)
		path = _v.tt+os.sep+'gatekeeper.api'
		editor(path)
		return None



	global gatekeeper
	global gatepath
	load()
	if _.switches.isActive('NewProject'):
		project = _.switches.values('NewProject')[0]
		create(project)
		return None
	if _.switches.isActive('AddUser'):
		phone=None
		name=None
		for user in _.switches.values('AddUser'):
			scan=_scan.imp.app.scan.process( user, 'A02F28B2' )
			if 'phone' in scan: phone=scan['phone']
			else: name=user
		addUser(name,phone)
		# if not name is None and not phone is None:
		return None
def load():
	global gatekeeper
	global gatepath
	scanner(os.getcwd())
	

_.v.gateFi = '.gatekeeper_7ea5cf8b'
gatekeeper={}
# os=__.imp('os.sep')
import os
_scan = _.regImp( __.appReg, 'record-cleaner' )

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