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
	_.switches.register( 'Database', '-db', 'index.db' )
	_.switches.register( 'Has', '-h,-has', 'php' )
	_.switches.register( 'File', '-f,-file','index.php' )
	_.switches.register( 'Path', '-p,-path','ai.sds' )
	_.switches.register( 'Size', '-size', '10mb, 1mb' )
	_.switches.register( 'Ago', '-ago', '1w' )
	_.switches.register( 'GreaterLess-Ago', '-gl', 'gtr, lss' )
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'Data', '-d,-data,-cc,-contents,-x' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'PrintContentsSearch', '-search' )

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
	'file': 'search-indexDB-files.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Query file contents in db created with indexDB-files',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'sql',
						'db',
						'database',
						'query',
						'file contents',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						'dex',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						'indexDB-files',
						'dex',
						'dex.',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						'Database must be created with:',
						'\tindexDB-files',
						'\t\tAlias: dex.',
	],
	'examples': [
						_.hp('dex -db daily -has Piller + *.md 2024 -print -search email'),
						_.hp(''),
						_.hp('p search-indexDB-files -db daily -has Piller + *.md 2024 -print -search email'),
						_.hp(''),
						_.hp('dex -f .htaccess - .site -2 .save .bk .old .cp .htaccess2 .htaccess3'),
						_.linePrint(label='simple',p=0),
						_.hp('p search-indexDB-files -f .htaccess - .site -2 .save .bk .old .cp .htaccess2 .htaccess3'),
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

class DBManager:
	def __init__(self, db_name="files.db"):
		self.db_name = db_name
		self.conn = None
		self.cursor = None
		self.connect()
	def connect(self):
		self.conn = sqlite3.connect(self.db_name)
		self.cursor = self.conn.cursor()

	def search_func(self, query_dict, gl=None):
		for key in query_dict:
			if key == 'name':     query_dict[key] = '%'+query_dict[key]+'%'
			if key == 'content':  query_dict[key] = '%'+query_dict[key]+'%'
			if key == 'path':     query_dict[key] = '%'+query_dict[key]+'%'
			if key == 'is_dir':   query_dict[key] = '%'+query_dict[key]+'%'
			if key == 'created':  query_dict[key] = str(query_dict[key])
			if key == 'modified': query_dict[key] = str(query_dict[key])
			if key == 'size':     query_dict[key] = str(_.unFormatSize(query_dict[key]))
			if _.switches.isActive('Test'):
				if key == 'name':     query_dict[key] = '"'+query_dict[key]+'"'
				if key == 'content':  query_dict[key] = '"'+query_dict[key]+'"'
				if key == 'path':     query_dict[key] = '"'+query_dict[key]+'"'
				if key == 'is_dir':   query_dict[key] = '"'+query_dict[key]+'"'

		# search_query = "SELECT * FROM files WHERE "
		search_query = "SELECT path FROM files WHERE "
		search_terms = []
		for key, value in query_dict.items():
			do = 'like'
			if not gl or not key in gl: do = '>'
			elif gl[key] == 'gtr': do = '>'
			else: do = '<'
			if key == 'content': do = 'like'
			if key == 'is_dir': do = 'like'
			if key == 'name': do = 'like'
			if key == 'path': do = 'like'
			search_terms.append(f"{key} {do} ?")
		search_query += ' AND '.join(search_terms)
		if _.switches.isActive('Test'):
			complete_query = search_query.replace('?','%s') % tuple(query_dict.values())
			print(complete_query)
			sys.exit()
		else:
			try:
				self.cursor.execute(search_query, tuple(query_dict.values()))
				result = self.cursor.fetchall()
				return result
			except Exception as e:
				_.pr(e,c='red')
				_.isExit(__file__)

	def search_by_name(self, name):
		return self.search_func({'name': name})

	def search_by_path(self, path):
		return self.search_func({'path': path})

	def search_by_size(self, size):
		return self.search_func({'size': size})

	def search_by_created(self, created):
		return self.search_func({'created': created})

	def search_by_modified(self, modified):
		return self.search_func({'modified': modified})

	def search_by_is_dir(self, is_dir):
		return self.search_func({'is_dir': is_dir})

	def search_by_content(self, content):
		return self.search_func({'content': content})

	def data(self, path):
		sql = 'select content from files where path = "'+path+'"'
		self.cursor.execute(sql)
		result = self.cursor.fetchall()
		try:
			return result[0][0]
		except: return 'no data'
import os

def aliases(db):
	aliases=_.getTable('file-open-aliases.hash')
	if not 'aliases' in aliases: aliases['aliases']={}
	if not 'files' in aliases: aliases['files']={}
	if db in aliases['aliases']:
		db = aliases['aliases'][db]
	return db

def action(filePath=None):
	# if not _.showLine(filePath):return None
	# _.e('incomplete','not finished')
	if _.switches.isActive('Database'):
		db = _.switches.value('Database')
		db = aliases(db)
	else:
		db = 'index.db'
	query = DBManager(db)
	if not filePath is None or _.switches.isActive('Data') and os.path.isfile(_.switches.value('File')):
		if not filePath is None:
			_.pr('\n')
			_.pr(filePath,c='cyan')
			# if not _.showLine(filePath):return None
			contents = query.data(filePath); _.pr(contents);
		else:
			for path in _.switches.values('File'):
				# if not _.showLine(path):return None
				contents = query.data(path); _.pr(contents);
		return contents
	# db.create_table()
	# print(db.search_by_name('file1.txt'))
	data = {}
	gl={}
	if _.switches.isActive('Has'):
		value =' '.join(_.switches.values('Has'))
		data = {'content': value}

	if _.switches.isActive('File'):
		value =' '.join(_.switches.values('File'))
		data['name'] = value

	if _.switches.isActive('Path'):
		value =' '.join(_.switches.values('Path'))
		data['path'] = value

	if _.switches.isActive('Size'):
		value =' '.join(_.switches.values('Size'))
		data['size'] = value
		if len(_.switches.values('Size')) > 1: gl['size'] = _.switches.values('Size')[1]

	if _.switches.isActive('Ago'):
		value =_.switches.values('Ago')[0]
		data['modified'] = value
		if len(_.switches.values('Size')) > 1: gl['size'] = _.switches.values('Size')[1]

	if _.switches.isActive('GreaterLess-Ago'):
		gl['modified'] = _.switches.value('GreaterLess-Ago')
		gl['created'] = _.switches.value('GreaterLess-Ago')

	# print(data); sys.exit();

	i=0
	for path in query.search_func(data,gl):
		i+=1
		for p in path:
			if _.showLine(p):
				if _.switches.isActive('Data'):
					action(p)
				else:
					if _.switches.isActive('Print'):
						searchAndPrint(p)
					else:
						_.pr(p,c='cyan')
	# print(search)
	_.pr()
	_.pr('',_.addComma(i),c='green')

def searchAndPrint(path):
	if not _.switches.isActive('Print'):
		return False
	if not _.switches.isActive('PrintContentsSearch') and _.switches.isActive('Has'):
		_.switches.fieldSet('PrintContentsSearch','active',True)
		_.switches.fieldSet('PrintContentsSearch','value',','.join(_.switches.values('Has')))
		_.switches.fieldSet('PrintContentsSearch','values',_.switches.values('Has'))
	if not os.path.isfile(path): return False
	contents = _.getText(path,raw=True).replace('\r','')
	if not _.showLine(contents,_.switches.values('PrintContentsSearch'),_.switches.values('Minus')): return False
	_.pr()
	_.pr(path,c='cyan')
	for line in contents.split('\n'):
		line = line.strip()
		if not _.showLine(line,_.switches.values('PrintContentsSearch'),_.switches.values('Minus')): continue
		if _.switches.isActive('PrintContentsSearch'):
			for plusSearchX in _.switches.values('PrintContentsSearch'):
				plusSearchX = _.ci( plusSearchX )
				for subject in _.caseUnspecificCode( line, plusSearchX ):
					line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )
			if line:
				print('\t',line)
	return True

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

