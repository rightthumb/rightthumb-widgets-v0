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
	_.switches.register( 'Filtered', '-f,-filter,-filtered' )
	_.switches.register( 'Important', '-i,-important' )
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
import re



def find_imports(filepath):
	global found_imports
	with open(filepath, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	for line in lines:
		match = re.search(r'^import (\S+)(,)?', line)
		if match:
			for module in match.group(1).split(','):
				module = module.strip()
				found_imports[module] = found_imports.get(module, 0) + 1

		match = re.search(r'^from (\S+) import', line)
		if match:
			module = match.group(1).strip()
			found_imports[module] = found_imports.get(module, 0) + 1

		match = re.search(r'^(\S+)=__\.imp', line)
		if match:
			module = match.group(1).strip()
			found_imports[module] = found_imports.get(module, 0) + 1

	return found_imports


def script(path):

	if os.path.isfile(path):
		if path.endswith(".py"):
			found_imports = find_imports(path)


important='''
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_nID\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_vault\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_encryptString\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_base2\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_mimetype\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_md5\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_dir\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_base1\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_string\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_vars\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_base3\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_construct\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_backupLog\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_banners\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_imdb\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_encryptFile\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_profileVariables\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_bookmarks\\__init__.py
D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_simpleThreads\\__init__.py
'''.strip().split('\n')


def action():
	global found_imports
	global important
	found_imports = {}
	fo = _v.py
	if _.switches.isActive('Important'):
		for path in important: script(path)
	else:
		_.fo(fo,script=script)



	# _.saveTable(found_imports,'find-python-imports.json')
	# found_imports=_.getTable('find-python-imports.json')
	if not _.switches.isActive('Filtered'):
		records=[]
		for module, count in sorted(found_imports.items()):
			records.append({'module':module,'count':count})
		records=_.sort(records,'count')
		_.pt(records)
		return records

	spent=[]
	records=[]
	mods={}
	for mod, cnt in sorted(found_imports.items()):
		mod=mod.strip()
		mod=mod.split('.')[0]
		if len(mod):
			if not '_' in mod:
				if not mod in mods: mods[mod]=0
				mods[mod]+=cnt


	for mod, cnt in sorted(mods.items()):
		records.append({'module':mod,'count':cnt})
	records=_.sort(records,'count')
	_.pt(records)


'''
Crypto
arrow
ast
base64
calendar
collections
cssselect
getpass
imp
importlib
lxml
pickle
random
requests
sqlite3
struct
webbrowser
dateutil
pathlib
re
glob
hashlib
math
platform
signal
uuid
operator
simplejson
threading
time
datetime
sys
os
'''


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

