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
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Table', '-table', 'meta', isRequired=True )
	_.switches.register( 'DB', '-db', 'meta.db', isRequired=True )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=True )
	_.switches.register( 'Build', '-build' )
	_.switches.register( 'DeleteDB', '-del' )

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
	for field_name in _.v.db.records[0].keys():
		column_type = None
		for row in _.v.db.records:
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
		_.pr(_.v.db.db,c='green')
		if _.switches.isActive('DeleteDB'):
			if os.path.isfile(_.v.db.db): os.unlink(_.v.db.db)
	else:
		if os.path.isfile(_.v.db.db): return None
	_.switches.fieldSet( 'Build', 'active', True )
	conn = sqlite3.connect(_.v.db.db)
	c = conn.cursor()
	column_names = ','.join(field_names)
	column_defs = ','.join([f'{name} {column_types[i]}' for i, name in enumerate(field_names)])
	create_table_query = f'CREATE TABLE {_.v.db.table} ({column_defs})'
	c.execute(create_table_query)
	conn.commit()
	conn.close()



import sqlite3

def import_json_data(key='path'):


	def insert_all():
		conn = sqlite3.connect(_.v.db.db)
		c = conn.cursor()

		for row in _.v.db.records:
			values = [row[field_name] for field_name in row]
			print('INSERT',row[key])
			insert_query = f'INSERT INTO {_.v.db.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
			# print(insert_query,values)
			# _.pv(values)
			c.execute(insert_query, values)
		conn.commit()
		conn.close()


	if _.switches.isActive('Build'):
		insert_all()
		return None
	conn = sqlite3.connect(_.v.db.db)
	c = conn.cursor()

	for row in _.v.db.records:
		# _.pv(_.v.db.records)
		key_value = row.get(key, None)
		if key_value:
			c.execute(f"SELECT COUNT(*) FROM {_.v.db.table} WHERE {key}=?", (key_value,))
			record_count = c.fetchone()[0]
			if record_count > 0:
				# Record exists, update it
				print('UPDATE',row[key])
				update_query = f'UPDATE {_.v.db.table} SET {",".join([f"{field_name} = ?" for field_name in row])} WHERE {key}=?'
				values = [row[field_name] for field_name in row] + [key_value]
				c.execute(update_query, values)
				continue

		# Record doesn't exist or key is not set, insert it
		values = [row[field_name] for field_name in row]
		print('INSERT',row[key])
		insert_query = f'INSERT INTO {_.v.db.table} VALUES ({",".join(["?" for _ in range(len(values))])})'
		c.execute(insert_query, values)

	conn.commit()
	conn.close()







def action():
	fi = _.isData(r=1)[0]
	if _.getTextFirst(fi) == '[': records = _.getTable2(fi)
	else: records = _.csv(fi)
	_.v.db         = _.dot()
	_.v.db.db      = _.switches.value('DB')
	_.v.db.table   = _.switches.value('Table')
	_.v.db.records = records
	if _.v.db.records:
		create_sqlite_table(clean_field_names(_.v.db.records[0].keys()), determine_column_types())
		import_json_data('name')
import os

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

