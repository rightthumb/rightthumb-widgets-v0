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
	_.switches.register( 'Database', '-db', 'index.db' )
	pass
	#b)--> examples
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
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
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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
import os



# function to check if file is text file
def is_text(filename):
	try:
		with open(filename, 'tr') as check_file:
			check_file.read()
		return True
	except:
		return False

# function to get file content
def get_content(filename):
	try:
		with open(filename, 'r') as read_file:
			return read_file.read()
	except:
		return ""

# function to index files
# def index_files(c,directory, recursion = False):
#     for filename in os.listdir(directory):
#         abs_path = os.path.join(directory, filename)

#         if os.path.isdir(abs_path) and recursion:
#             index_files(abs_path, recursion)
#         else:
#             size = os.path.getsize(abs_path)
#             created = os.path.getctime(abs_path)
#             is_dir = 1 if os.path.isdir(abs_path) else 0
#             content = get_content(abs_path) if is_text(abs_path) else ""

#             # Insert a row of data
#             c.execute("INSERT INTO files VALUES (?,?,?,?,?,?)", (filename, abs_path, size, created, is_dir, content))
cnt = 0
def index_files(c, directory, recursion=False):
	global cnt
	global conn
	for filename in os.listdir(directory):
		try:
			abs_path = os.path.join(directory, filename)

			if os.path.isdir(abs_path) and recursion:
				index_files(c, abs_path, recursion)  # Corrected the arguments here
			else:
				try:
					size = os.path.getsize(abs_path)
					created = os.path.getctime(abs_path)
					modified = os.path.getmtime(abs_path)
					is_dir = 1 if os.path.isdir(abs_path) else 0
					content = get_content(abs_path) if is_text(abs_path) else ""
					cnt += 1
					# Insert a row of data
					c.execute("INSERT INTO files VALUES (?,?,?,?,?,?,?)", (filename, abs_path, size, created, modified, is_dir, content))
					if cnt % 100 == 0:
						conn.commit()
						_.pr( cnt, r=1 )
				except: pass
		except: pass

def numb(num):
	num = int(num)
	if num < 10:
		return '0'+str(num)
	else:
		return str(num)
def dbRename(db):
	db = __.path(db)
	fo = __.path(db,fo=True)+os.sep
	fi = __.path(db,fi=True)
	if os.path.isfile(db):
		import shutil
		modified = _.friendlyDate( _.autoDate( _.mod(db) ) ).split(' ')[0].replace('-','.')
		# print(modified); sys.exit();
		to = fo+modified+'-'+fi
		i=1
		while os.path.isfile(to):
			i+=1
			to = fo+modified+'-'+numb(i)+'-'+fi
			
		shutil.move(db,to)

def action():
	global conn
	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
	else:
		db = 'index.db'
	dbRename(db)
	# connect to the sqlite database
	conn = sqlite3.connect(db)
	c = conn.cursor()

	# Create table
	c.execute('''CREATE TABLE files
				 (name text, path text, size real, created real, modified real, is_dir integer, content text)''')
	# apply the index_files function to the current directory
	index_files(c,os.getcwd(), True)

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

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

