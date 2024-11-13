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
	_.switches.register( 'Host', '-host' )
	_.switches.register( 'User', '-user' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'DB', '-db' )
	_.switches.register( 'Port', '-port' )

	_.switches.register( 'Yes', '-y,-yes' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.sql', isData='data', description='Files', isRequired=False )

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
	'file': 'vps-sql-exec.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Run SQL on the server',
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
import mysql.connector

def action():

	# Replace the below database connection parameters as per your MySQL/MariaDB server details
	if _.switches.isActive('Port'):
		try:
			port=int(_.switches.value('Port'))
		except:
			port=3306
		_.pr('Port: ',port,c='yellow')
	else:
		port=33066
	host='localhost'
	user=_vault.imp.s.de('DOm78CRdaN2TmF46JWMtBip4kHgiwk+x')
	db=_vault.imp.s.de('DOm78CRdaN2TmF46JWMtBip4kHgiwk+x')
	password=_vault.imp.s.de('W2GmTR1xyfXB0NZbMkFDfb5mFpKa+ktj6iEHO7G8dw0=')
	if _.switches.isActive('Host'):     host=_.switches.value('Host')
	if _.switches.isActive('User'):     user=_.switches.value('User')
	if _.switches.isActive('Password'): password=_.switches.value('Password')
	if _.switches.isActive('DB'):       db=_.switches.value('DB`')
	
	db_config = {
		"host": host,
		"user": user,
		"password": password,
		"database": db,
		"port": port
	}

	sql_commands = _.pp()
	if type(sql_commands) == list: '\n'.join(sql_commands)

	_.pr('SQL:\n',sql_commands,'\n')
	ask=input('Run?: ').lower()
	if not _.switches.isActive('Yes'):
		if not 'y' in ask:
			_.pr('Did not run',c='red')
			sys.exit()

	connection = None

	try:
		# Connect to the database
		connection = mysql.connector.connect(**db_config)
		cursor = connection.cursor()

		# Execute the SQL commands
		for command in sql_commands.split(";\n"):
			if command.strip():
				cursor.execute(command)

		# Commit the transaction
		connection.commit()

	except mysql.connector.Error as err:
		print(f"Error: {err}")

	finally:
		# Close the database connection
		if connection and connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

_vault = _.regImp( __.appReg, '_rightThumb._vault' )



# python3 -m pip install mysql-connector-python


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

 
