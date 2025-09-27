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
	_.switches.register( 'Clean', '--c' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

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


def check_file_header(path):
	signatures = _.getTableDB('file-signatures.json')
	

	header = _.IS(path)
	
	found=[]
	for signature_group in signatures:
		if 'Contents' in signature_group:
			contents = signature_group['Contents']
			for signature in contents:
				if 'Hex signature' in signature and header.startswith(signature['Hex signature']): found.append(signature)
				if 'Extension' in signature and header.startswith(signature['Extension']): found.append(signature)
				if 'Offset' in signature and header.startswith(signature['Offset']):found.append(signature)
				if 'Description' in signature and len(signature['Description'].strip()) and header.startswith(signature['Description']): found.append(signature)
				if 'Description' in signature and len(signature['Description'].strip()):
					if '\n' in signature['Description']:
						for line in signature['Description']:
							line=line.strip()
							if line and header.startswith(signature['Description']):
								found.append(signature)
				if 'ISO 8859-1' in signature and header.startswith(signature['ISO 8859-1']): found.append(signature)
					# return signature['Description']
	if found: return found
	return 'Unknown file format'

import re

def strip_non_alphanumeric(string):
	return re.sub(r'[^a-zA-Z0-9\s]+', '', string)

def check_string_pattern(string):
	items = string.split()
	
	for item in items:
		if len(item) != 2 or not item.isalnum():
			return False
	
	return True
def remove_file_header_signatures(data):
	cleaned_data = []
	for line in data:
		# If line has a hexadecimal signature, skip it
		if re.search(r'^([0-9A-Fa-f]{2}[\s]*)+$', line.strip()):
			continue
		# If line looks like a file signature (not common English words), skip it
		elif re.search(r'^([A-Z]{2,}[\s]*)+$', line.strip()):
			continue
		else:
			cleaned_data.append(line)
	return cleaned_data

def isSig(data):
	data=data.strip()
	if not ' ' in data: return False
	if not '\n' in data: return False
	return check_string_pattern(data)
	# return True

def action():

	for path in _.pp():
		results=check_file_header(path)
		if not _.switches.isActive('Clean') and not _.switches.isActive('Plus'):
			_.pr(_.IS(path),c='cyan')
			_.pr(_.toYML(results),c='yellow')
			_.pr()
			_.pr('',len(results),c='darkcyan')

		clean=[]
		selected=[]
		for rec in results:
			if 'Description' in rec:
				d=strip_non_alphanumeric(rec['Description'])
				des=[]
				if not 'BEGIN SSH2 PUBLIC KEY' in d and not d == '0' and not isSig(d): des.append(d)
				cl=remove_file_header_signatures(des)
				if cl:
					clean.append(cl[0])
					if _.switches.isActive('Plus'):
						if _.showLine(cl[0]):
							selected.append(rec)
		if not _.switches.isActive('Clean'):
			if _.switches.isActive('Plus'):
				for sel in selected:
					_.pr(_.toYML(sel))
			else:
				if len(clean):
					_.pr()
					print(_.pr('Cleaned:',c='green',p=0)+_.pr('','\u2193','\u2193','\u2193',c='red',p=0))
				for x in clean:
					_.pr('\t',x,c='green')
				_.pr()
				_.pr('',len(clean),c='darkcyan')
		else:
			for x in clean: _.pr(x,c='green')
			
		# _.pr()
		# _.pr('extracted with: https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/javascript/tool.js')
		# _.pr('from: https://en.wikipedia.org/wiki/List_of_file_signatures')

# https://en.wikipedia.org/wiki/List_of_file_signatures

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