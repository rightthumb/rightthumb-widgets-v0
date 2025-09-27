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
	_.switches.register( 'Add', '-add' )
	_.switches.register( 'Print', '-p,-print' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='glob,name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )    
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

v = _.dot()
v.exit = False
v.IPd = '0.0.0.0'
v.ports = {
			'ssh': 22,
			'cpanel': 443,
			'smb': [139,445],
			'rdp': 3389,
			'mysql': 3306,
			'l2tp': [500,4500],
			'pptp': 1723,
			'ssl-ftp': [989, 990],
			'ftp': 21,
			'sftp': 22,
			'tftp': 69,
			'tftp': 69,
			'pop3': 110,
			'smtp': 25,
			'imap': 143,
			'pop3-ssl': 995,
			'smtp-ssl': 465,
			'imap-ssl': 993,
			'ntp': 123,
			'ldap': 389,
}

def autoPorts(srv):
	srv = srv.replace(' ','')
	p = []
	for s in srv.split(','):
		if s in v.ports:
			pot = v.ports[s]
			if type(pot) == int:
				p.append( pot )
			elif type(pot) == list:
				for po in pot:
					p.append( po )
	return p

def getIP(host):
	# ip = socket.gethostbyname(host)
	# _.pr(':ip:',ip)
	# return ip
	if host == 'localhost':
		return '127.0.0.1'
	try:
		return socket.gethostbyname(host)
	except Exception as e:
		return v.IPd


def ask(say):
	if not v.exit:
		if say == 'password':
			return getpass.getpass()
		return input( '\t'+say+': ' )
	return None



def fields(record):
	d = {}
	_.cp( 'keep value with: !' )
	
	for k in record:
		if k == 'ip' and not skipIP:
			pass
		elif k == 'password' and not d['vault'] == '':
			pass
		else:
			d[k] = record[k]
			wt = _.autoWrapText( _.cp( [ k+':', record[k] ], 'cyan', p=0 ), prefix=len('serving: '), pre_skip_0=True )
			# _.pr(wt)
			# _.pr(type(wt))
			if type(wt) == str:
				_.pr(wt)
			else:
				_.pr( '\n'.join(wt) )
			# for w in wt:
			#     _.pr(w)
			val = ask( k )
			if val == '!':
				keep = True
			else:
				keep = False

			if not val == '!':
				d[k] = val
			_.cp( [ '\t\t', d[k] ], 'yellow' )
			if k == 'serving':
				po = autoPorts(d[k])
				d['ports'] = po
				_.cp( [ '\t\t', po ], 'yellow' )

			if k == 'host':
				ip = record['ip']
				hip = getIP(d[k])

				if hip == v.IPd:
					skipIP = True
				else:
					_.cp( ['\t\t',hip], 'yellow' )
					skipIP = False

				d['ip'] = hip
				record['ip'] = hip
				if hip == v.IPd:
					qq = ask( 'ip: '+v.IPd+' keep?(y):' )
					if qq == 'n':
						d['ip'] = ip
						record['ip'] = ip



			if not keep and k == 'password':
				d[k] = _vault.imp.s.en(d[k])

	_.pr()
	_.pr()
	_.cp( [ '!! default fields completed !!' ], 'red' )
	_.pr()
	_.pr()
	_.cp( [ 'adding custom fields' ], 'green' )
	_.pr()
	_.pr()

	_.cp( [ 'leave field blank when done or value=exit' ], 'cyan' )
	while not v.exit:
		f = ask('field')
		if f == 'x' or f == 'exit' or f == '' or f == '!':
			v.exit = True
			return d
		if not v.exit:
			val = ask('value')
			if val == 'exit' or val == '!':
				v.exit = True

		if not v.exit:
			d[f] = val
	return d

def combine( base, add ):
	for k in add:
		base[k] = add[k]
	return base

def process(srv):
	global table
	if not srv in table:
		table[srv] = {
						'host': 'vps.rightthumb.com',
						'ip': v.IPd,
						'serving': ', '.join( list( v.ports.keys() ) ),
						'user': 'scott',
						'vault': 'vps.scott',
						'password': '-',
						# 'ports': '22, 443, 139,445, 1723, 500,4500, 21, 69',
		}
	else:
		_.pv(table[srv])
	
	rec = fields(table[srv])
	table[srv] = combine( table[srv], rec )
	temp = {
				srv: table[srv]
	}
	_.pv( temp )
	_.saveTableDB( table, 'server-vault.hash' )

		

def action():
	global table
	load()
	if _.switches.isActive('Print'):
		_.pv( table )
		return table
	if _.switches.isActive('Add'):
		for srv in _.switches.values('Add'):
			process(srv)
		return table


def load():
	global table
	table = _.getTableDB( 'server-vault.hash' )


import socket
import getpass

_vault = _.regImp( __.appReg, '_rightThumb._vault' )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






