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
	pass
	#b)--> examples
	_.switches.register( 'DefaultDatabases', '-d,-default' )
	_.switches.register( 'Database', '-db' )
	_.switches.register( 'Folders', '-f,-fo,-fos,-folder,-folders' )
	_.switches.register( 'RebuildCache', '-r' )
	# _.switches.register( 'RebuildAllCache', '-a,-ra,,-all,-rebuild' )
	_.switches.register( 'CacheFolders', '-cf' )

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
	'file': 'folderSizeTotals.py',
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
						_.hp('p folderSizeTotals'),
						_.hp('p folderSizeTotals -fo C:\\'),
						_.hp('foSize'),
						_.hp('z'),
						_.hp('z -cf | .mx z -fo {} -r'),
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

import os
import sqlite3

def calculate_total_bytes(database, table, folder):
	conn = sqlite3.connect(database)
	c = conn.cursor()
	
	# folder = folder.replace('\\', '\\\\')
	query = f"SELECT SUM(bytes) AS TotalBytes FROM {table} WHERE path LIKE '{folder}%'"
	# print(query)
	c.execute(query)
	result = c.fetchone()

	conn.close()

	return result[0] if result[0] is not None else 0

def get_subfolder_sizes(database, table, folder):
	global total_all_bytes
	subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
	
	folder_sizes = []
	
	for subfolder in subfolders:
		size = calculate_total_bytes(database, table, subfolder)
		total_all_bytes += size
		folder_sizes.append({'folder': os.path.basename(subfolder), 'bytes': size, 'size': _.formatSize(size)})
		
	return folder_sizes


# import _rightThumb._dir as _dir
__.v.db  = ''

def scriptFoDB(path):
	global table
	if path.endswith('.db'):
		if check_table_exists(path, table):
			__.v.db=path

def calculate_percentage(part, total):
	try:
		return round((part / total) * 100, 2)
	except ZeroDivisionError:
		return 0



def find_db_in_folder_or_parents(path):
	path=__.path(path)
	while not __.v.db and os.sep in path:
		_.fo(path,script=scriptFoDB)
		path=__.path(path,pop=1)
	print(__.v.db)
	return __.v.db


total_current_folder_bytes=0
def scriptFoCurrentTotal(path):
	global total_current_folder_bytes
	path=__.path(path)
	try: total_current_folder_bytes+=os.stat(path).st_size
	except: pass



def check_table_exists(db_path, table_name):
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()

	# Query the master table to retrieve the table names
	cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")

	# Fetch all rows as a list
	result = cursor.fetchall()

	conn.close()

	# If the table exists, result will contain its name
	if result:
		return True
	else:
		return False
cache = {}
loop=0
table = 'files'
def action():
	global loop

	if loop > 1:
		_.e('unable to auto fix database selection','select a database: -db database.db')
	loop+=1
	# print(calculate_percentage(30,100))
	global cache
	global table
	global total_all_bytes
	global total_current_folder_bytes
	
	if not cache: cache = _.getTable('folderSizeTotals.index')

	if _.switches.isActive('CacheFolders'):
		for folder in cache:
			print(folder)
		return None

	if not _.switches.isActive('Folders'):
		folders = [os.getcwd()]
	else:
		folders = []
		for fo in _.switches.values('Folders'):
			folders.append(__.path(fo))

	if _.switches.isActive('RebuildAllCache'):
		_.switches.fieldSet( 'RebuildCache', 'active', True )
		folders = []
		for folder in cache: folders.append(folder)


	databases=[]

	if not _.switches.isActive('Database'):
		if _.switches.isActive('DefaultDatabases'):
			database = False
		else:
			database = find_db_in_folder_or_parents(os.getcwd())
			databases.append(database)
		if not database:
			if not _.isWin:
				_.e('no db','specify a database with: -db database.db')
			elif _.isWin:
				c=False
				d=False
				for fo in folders:
					if not c and fo.lower().startswith('c:'):
						c=True
						# databases.append(_v.myIndexes+os.sep+'2023-04-04__C_Drive.db')
						databases.append(_v.myIndexes+os.sep+'C_Drive.db')
					if not d and fo.lower().startswith('d:'):
						d=True
						# databases.append(_v.myIndexes+os.sep+'2023-04-04__D_Drive.db')
						databases.append(_v.myIndexes+os.sep+'D_Drive.db')
			
	else:
		databases = _.switches.values('Database')
	for database in databases:

		for folder in folders:
			if not _.switches.isActive('RebuildCache'):
				if folder in cache: continue

			total_all_bytes = 0
			total_current_folder_bytes = 0
			try:
				folder_sizes = get_subfolder_sizes(database, table, folder)
			except Exception as e:
				if not _.isWin:
					_.e('db error','missing table '+table)
				else:
					_.switches.fieldSet( 'DefaultDatabases', 'active', True )
					action()
					return None
			
			_.fo(folder,script=scriptFoCurrentTotal)
			current = {'folder': '.'+os.sep+os.path.basename(folder), 'bytes': total_current_folder_bytes, 'size': _.formatSize(total_current_folder_bytes)}
			folder_sizes.append(current)
			total_all_bytes+=total_current_folder_bytes
			for i,rec in enumerate(folder_sizes):
				try:
					folder_sizes[i]['percentage'] = str(calculate_percentage(rec['bytes'], total_all_bytes))
					if folder_sizes[i]['percentage'] == '0.0': folder_sizes[i]['percentage']=0
					folder_sizes[i]['percentage'] += '%'
				except Exception as e:
					folder_sizes[i]['percentage'] = '0%'

			record = {'bytes': total_all_bytes, 'folders': folder_sizes }
			cache[folder] = record
			_.saveTable(cache,'folderSizeTotals.index',p=0)

	for folder in folders:
		record = cache[folder]
		_.pr(folder,c='green')
		folder_sizes = record['folders']
		_.pt(folder_sizes,'folder,size,percentage','bytes')
		_.pr('\n\ttotal:',_.formatSize(record['bytes']),c='yellow')

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

