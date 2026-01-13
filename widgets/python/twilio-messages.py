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
	# _.switches.register( 'Input', '-i' )
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


import os
from twilio.rest import Client
import yaml

def fetch_twilio_messages():
	# Set your environment variables or directly set the values for
	# TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
	account_sid = _keychain.imp.key('twillio-account-sid')
	auth_token = _keychain.imp.key('twillio-auth-token')

	client = Client(account_sid, auth_token)

	# Retrieve the list of messages
	messages = client.messages.list()

	return messages

def convert_messages_to_yaml_0(messages):
	yaml_list = []
	
	for msg in messages:
		yaml_list.append({
			'sid': msg.sid,
			'from': msg.from_,
			'to': msg.to,
			'body': msg.body,
			'date_sent': msg.date_sent.strftime('%Y-%m-%d %H:%M:%S'),
		})

	# Convert to YAML format
	return yaml.dump(yaml_list, default_flow_style=False)

def convert_messages_to_yaml_1(messages):
    yaml_list = []

    for msg in messages:
        # Convert message attributes to dictionary
        message_dict = {attr: getattr(msg, attr) for attr in dir(msg) if not callable(getattr(msg, attr)) and not attr.startswith("_")}
        yaml_list.append(message_dict)

    # Convert to YAML format
    return yaml.dump(yaml_list, default_flow_style=False)


def convert_messages_to_yaml_2(messages):
    yaml_list = []

    for msg in messages:
        # Convert message attributes to dictionary
        message_dict = {attr: getattr(msg, attr) for attr in dir(msg) if not callable(getattr(msg, attr)) and not attr.startswith("_")}

        # Extract and format specific fields
        message_dict['sid'] = msg.sid
        message_dict['from'] = msg.from_
        message_dict['to'] = msg.to
        message_dict['body'] = msg.body
        message_dict['status'] = msg.status
        message_dict['date_sent'] = msg.date_sent.strftime('%Y-%m-%d %H:%M:%S')
        
        yaml_list.append(message_dict)

    # Convert to YAML format
    return yaml.dump(yaml_list, default_flow_style=False)


def resend_to_undelivered(messages, retried_messages_log="retried_messages.log"):
    client = Client(_keychain.imp.key('twillio-account-sid'), _keychain.imp.key('twillio-auth-token'))

    # Read the log of retried messages
    with open(retried_messages_log, "a+") as log:
        log.seek(0)  # Go to the beginning of the file to read
        retried_messages = [line.strip() for line in log.readlines()]

        for msg in messages:
            if msg.status == "undelivered" and msg.sid not in retried_messages:
                # Resend the original message using the original 'from' number
                client.messages.create(
                    to=msg.to,
                    from_=msg.from_,
                    body=msg.body
                )

                # Add the message SID to the log
                log.write(f"{msg.sid}\n")

if __name__ == "__main__":
    messages = fetch_twilio_messages()
    yaml_representation = convert_messages_to_yaml(messages)
    print(yaml_representation)

    # Resend undelivered messages
    resend_to_undelivered(messages)



def action():
	messages = fetch_twilio_messages()
	yaml_representation = convert_messages_to_yaml_2(messages)
	print(yaml_representation)


_keychain = _.regImp( __.appReg, 'keychain' )
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

