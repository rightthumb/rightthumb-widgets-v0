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



def action():
	IPs=_.switches.values('IP/Domain')
	# _.pv(IPs)
	for i,ip in enumerate(IPs):
		if not _.switches.isActive('Dump'):
			_.linePrint(c='green')
		url='https://ip-netblocks.whoisxmlapi.com/api/v2?apiKey=at_KTUpnwlfmFrgqmIPVa2jTVWEyvjrt&ip='+ip
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
					_.linePrint(c='green')
					break

		except Exception as e:
			pass
		if not recs:
			_.pr('no records found',c='red')
			_.linePrint(c='green')
		if _.switches.isActive('Thorough'):
			_.pr(recs,pvs=1)
		else:
			_.pr(recs[0],pvs=1)
		_.linePrint(c='green')


		# print()
		# _.pr(type(data))
		# _.pr(data['search'])
		# _.pv(info)

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





