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
import socket
##################################################
def sw():
	_.switches.register( 'Thorough', '-deep,-thorough,-all' )
	_.switches.register( 'Dump', '-dump' )
	pass
	### EXAMPLE: START
	_.switches.register( 'IP/Domain', '-i,-ip,-domain,-d', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

def hostname_to_ip(data):
	if not data[0] in '0123456789':
		try:
			data = socket.gethostbyname(data)
		except Exception as e:
			_.cp([e,'\n',data],'red')
			pass
	return data

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
						_.hp('p netblock -ip 45.35.203.103 -all'),
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
	_.switches.trigger( 'IP/Domain', hostname_to_ip )
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )


_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
### EXAMPLE: START


	#--> make hotkey ad-description soon:  <--<w#
	#-->    - outer most typed first
	#-->    - blank pipe
	#-->    __.setting('hotkey-clip.ad_description-start1',d=False)
	#--> _________________________________
	#--> describe selection area two
	#--> 3 write a note here wrap text
	#--> two dignissim
	#--> 1 inceptos
	#--> _________________________________
	#--> describe selection area two
	#-->              |           |
	#-->              |           | - write a note here
	#-->              |           |   wrap text
	#-->              |           |
	#-->              |           | - dignissim
	#-->              |
	#-->              | - inceptos

	# if _.switches.isActive('Test'): test(); return None;
	# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
	# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
	#--> a=(1 if True else 0) <--# 
	#--> m=[[row[i] for row in matrix] for i in range(4)]
	# requests=__.imp('requests.post')
	# data=str(requests.post(url,data={}).content,'iso-8859-1')


### EXAMPLE: END
########################################################################################
# START




def action(payload=None):
	global _cidr_
	index=_.getTableDB('netblock.hash')
	IPs=_.switches.values('IP/Domain')
	_cidr_skim_translate_={}
	# _.pv(IPs)
	for i,ip in enumerate(IPs):
		if ip in index:
			recs=index[ip]
		else:
			if not _.switches.isActive('Dump'):
				if payload is None:
					_.linePrint(c='green')
			url='https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey='+_v.config('whoisxmlapi')+'&ip='+ip
			# _.pr(url)
			info=__.url(url,txt=True,get=True)

			# info=_str.do('linux',info)
			# print(info)
			# sys.exit()
			data=simplejson.loads(str(info))
			
			if _.switches.isActive('Dump'):
				_.pr(data,pvs=1)
				return None
			recs=[]
			try:
				for record in data['result']['inetnums']:
					rec=extract(record)
					if not rec is None:
						recs.append(rec)
					if rec is None:
						if payload is None:
							_.linePrint(c='green')
						break
				if recs: index[ip]=recs; _.saveTableDB(index,'netblock.hash');
			except Exception as e: pass
		if payload is None:
			_json=simplejson.dumps(recs, indent=4, sort_keys=False)
			for _rec in _cidr_:
				if _rec['CIDR']+'"' in _json and not _rec['CIDR'] in _cidr_skim_translate_: _cidr_skim_translate_[_rec['CIDR']]=_rec
			if not recs:
				_.pr('no records found',c='red')
				_.linePrint(c='green')
			if _.switches.isActive('Thorough'):
				_.pr(recs,pvs=1)
			else:
				_.pr(recs[0],pvs=1)
			_.linePrint(c='green')
	if _cidr_skim_translate_:
		_.pr


		# print()
		# _.pr(type(data))
		# _.pr(data['search'])
		# _.pv(info)



_cidr_=[
	{
		"CIDR": "/32",
		"SUBNET MASK": "255.255.255.255",
		"WILDCARD MASK": "0.0.0.0",
		"# OF IP ADDRESSES": "1",
		"# OF USABLE IP ADDRESSES": "1"
	},
	{
		"CIDR": "/31",
		"SUBNET MASK": "255.255.255.254",
		"WILDCARD MASK": "0.0.0.1",
		"# OF IP ADDRESSES": "2",
		"# OF USABLE IP ADDRESSES": "2*"
	},
	{
		"CIDR": "/30",
		"SUBNET MASK": "255.255.255.252",
		"WILDCARD MASK": "0.0.0.3",
		"# OF IP ADDRESSES": "4",
		"# OF USABLE IP ADDRESSES": "2"
	},
	{
		"CIDR": "/29",
		"SUBNET MASK": "255.255.255.248",
		"WILDCARD MASK": "0.0.0.7",
		"# OF IP ADDRESSES": "8",
		"# OF USABLE IP ADDRESSES": "6"
	},
	{
		"CIDR": "/28",
		"SUBNET MASK": "255.255.255.240",
		"WILDCARD MASK": "0.0.0.15",
		"# OF IP ADDRESSES": "16",
		"# OF USABLE IP ADDRESSES": "14"
	},
	{
		"CIDR": "/27",
		"SUBNET MASK": "255.255.255.224",
		"WILDCARD MASK": "0.0.0.31",
		"# OF IP ADDRESSES": "32",
		"# OF USABLE IP ADDRESSES": "30"
	},
	{
		"CIDR": "/26",
		"SUBNET MASK": "255.255.255.192",
		"WILDCARD MASK": "0.0.0.63",
		"# OF IP ADDRESSES": "64",
		"# OF USABLE IP ADDRESSES": "62"
	},
	{
		"CIDR": "/25",
		"SUBNET MASK": "255.255.255.128",
		"WILDCARD MASK": "0.0.0.127",
		"# OF IP ADDRESSES": "128",
		"# OF USABLE IP ADDRESSES": "126"
	},
	{
		"CIDR": "/24",
		"SUBNET MASK": "255.255.255.0",
		"WILDCARD MASK": "0.0.0.255",
		"# OF IP ADDRESSES": "256",
		"# OF USABLE IP ADDRESSES": "254"
	},
	{
		"CIDR": "/23",
		"SUBNET MASK": "255.255.254.0",
		"WILDCARD MASK": "0.0.1.255",
		"# OF IP ADDRESSES": "512",
		"# OF USABLE IP ADDRESSES": "510"
	},
	{
		"CIDR": "/22",
		"SUBNET MASK": "255.255.252.0",
		"WILDCARD MASK": "0.0.3.255",
		"# OF IP ADDRESSES": "1,024",
		"# OF USABLE IP ADDRESSES": "1,022"
	},
	{
		"CIDR": "/21",
		"SUBNET MASK": "255.255.248.0",
		"WILDCARD MASK": "0.0.7.255",
		"# OF IP ADDRESSES": "2,048",
		"# OF USABLE IP ADDRESSES": "2,046"
	},
	{
		"CIDR": "/20",
		"SUBNET MASK": "255.255.240.0",
		"WILDCARD MASK": "0.0.15.255",
		"# OF IP ADDRESSES": "4,096",
		"# OF USABLE IP ADDRESSES": "4,094"
	},
	{
		"CIDR": "/19",
		"SUBNET MASK": "255.255.224.0",
		"WILDCARD MASK": "0.0.31.255",
		"# OF IP ADDRESSES": "8,192",
		"# OF USABLE IP ADDRESSES": "8,190"
	},
	{
		"CIDR": "/18",
		"SUBNET MASK": "255.255.192.0",
		"WILDCARD MASK": "0.0.63.255",
		"# OF IP ADDRESSES": "16,384",
		"# OF USABLE IP ADDRESSES": "16,382"
	},
	{
		"CIDR": "/17",
		"SUBNET MASK": "255.255.128.0",
		"WILDCARD MASK": "0.0.127.255",
		"# OF IP ADDRESSES": "32,768",
		"# OF USABLE IP ADDRESSES": "32,766"
	},
	{
		"CIDR": "/16",
		"SUBNET MASK": "255.255.0.0",
		"WILDCARD MASK": "0.0.255.255",
		"# OF IP ADDRESSES": "65,536",
		"# OF USABLE IP ADDRESSES": "65,534"
	},
	{
		"CIDR": "/15",
		"SUBNET MASK": "255.254.0.0",
		"WILDCARD MASK": "0.1.255.255",
		"# OF IP ADDRESSES": "131,072",
		"# OF USABLE IP ADDRESSES": "131,070"
	},
	{
		"CIDR": "/14",
		"SUBNET MASK": "255.252.0.0",
		"WILDCARD MASK": "0.3.255.255",
		"# OF IP ADDRESSES": "262,144",
		"# OF USABLE IP ADDRESSES": "262,142"
	},
	{
		"CIDR": "/13",
		"SUBNET MASK": "255.248.0.0",
		"WILDCARD MASK": "0.7.255.255",
		"# OF IP ADDRESSES": "524,288",
		"# OF USABLE IP ADDRESSES": "524,286"
	},
	{
		"CIDR": "/12",
		"SUBNET MASK": "255.240.0.0",
		"WILDCARD MASK": "0.15.255.255",
		"# OF IP ADDRESSES": "1,048,576",
		"# OF USABLE IP ADDRESSES": "1,048,574"
	},
	{
		"CIDR": "/11",
		"SUBNET MASK": "255.224.0.0",
		"WILDCARD MASK": "0.31.255.255",
		"# OF IP ADDRESSES": "2,097,152",
		"# OF USABLE IP ADDRESSES": "2,097,150"
	},
	{
		"CIDR": "/10",
		"SUBNET MASK": "255.192.0.0",
		"WILDCARD MASK": "0.63.255.255",
		"# OF IP ADDRESSES": "4,194,304",
		"# OF USABLE IP ADDRESSES": "4,194,302"
	},
	{
		"CIDR": "/9",
		"SUBNET MASK": "255.128.0.0",
		"WILDCARD MASK": "0.127.255.255",
		"# OF IP ADDRESSES": "8,388,608",
		"# OF USABLE IP ADDRESSES": "8,388,606"
	},
	{
		"CIDR": "/8",
		"SUBNET MASK": "255.0.0.0",
		"WILDCARD MASK": "0.255.255.255",
		"# OF IP ADDRESSES": "16,777,216",
		"# OF USABLE IP ADDRESSES": "16,777,214"
	},
	{
		"CIDR": "/7",
		"SUBNET MASK": "254.0.0.0",
		"WILDCARD MASK": "1.255.255.255",
		"# OF IP ADDRESSES": "33,554,432",
		"# OF USABLE IP ADDRESSES": "33,554,430"
	},
	{
		"CIDR": "/6",
		"SUBNET MASK": "252.0.0.0",
		"WILDCARD MASK": "3.255.255.255",
		"# OF IP ADDRESSES": "67,108,864",
		"# OF USABLE IP ADDRESSES": "67,108,862"
	},
	{
		"CIDR": "/5",
		"SUBNET MASK": "248.0.0.0",
		"WILDCARD MASK": "7.255.255.255",
		"# OF IP ADDRESSES": "134,217,728",
		"# OF USABLE IP ADDRESSES": "134,217,726"
	},
	{
		"CIDR": "/4",
		"SUBNET MASK": "240.0.0.0",
		"WILDCARD MASK": "15.255.255.255",
		"# OF IP ADDRESSES": "268,435,456",
		"# OF USABLE IP ADDRESSES": "268,435,454"
	},
	{
		"CIDR": "/3",
		"SUBNET MASK": "224.0.0.0",
		"WILDCARD MASK": "31.255.255.255",
		"# OF IP ADDRESSES": "536,870,912",
		"# OF USABLE IP ADDRESSES": "536,870,910"
	},
	{
		"CIDR": "/2",
		"SUBNET MASK": "192.0.0.0",
		"WILDCARD MASK": "63.255.255.255",
		"# OF IP ADDRESSES": "1,073,741,824",
		"# OF USABLE IP ADDRESSES": "1,073,741,822"
	},
	{
		"CIDR": "/1",
		"SUBNET MASK": "128.0.0.0",
		"WILDCARD MASK": "127.255.255.255",
		"# OF IP ADDRESSES": "2,147,483,648",
		"# OF USABLE IP ADDRESSES": "2,147,483,646"
	},
	{
		"CIDR": "/0",
		"SUBNET MASK": "0.0.0.0",
		"WILDCARD MASK": "255.255.255.255",
		"# OF IP ADDRESSES": "4,294,967,296",
		"# OF USABLE IP ADDRESSES": "4,294,967,294"
	}
]



def extract(record):
	info={}
	try: info['route']=record['route']
	except Exception as e: pass

	try: info['domain']=record['as']['domain']
	except Exception as e: pass

	try: info['name']=record['org']['name']
	except Exception as e: pass
	
	try: info['email']=record['org']['email']
	except Exception as e: pass
	
	try: info['address']=record['org']['address']
	except Exception as e: pass

	try: info['zip']=record['org']['postalCode']
	except Exception as e: pass
	if not info:
		return None
	return record
	_.pr(record,pvs=1)
	return True

simplejson=__.imp('simplejson')

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





