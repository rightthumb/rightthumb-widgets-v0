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
	_.switches.register('Recursive', '-r')
	_.switches.register('Full-Path', '-path')
	_.switches.register('Mirror', '-m,-mirror')
	_.switches.register('View-Mirror', '-v,-view')
	_.switches.register('Folders', '-f,-fo,-fos,-folder,-folders')
	# _.switches.register('Pop', '-pop', 'first')

	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('require-list',[])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'fo.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Folder Stuff',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'folder',
						'os folder',
						'cache',
						'mirror',
						'structure',
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
						_.hp('p fo'),
						_.hp('p fo -r -fo _docs_\\ai'),
						_.hp('p fo -r -fo _docs_/ai'),
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
os=__.imp('os.sep')

def action():
	#--> min, architecture {:strict:}
	#--> trigger/callback  <w#
	#--> todo#> meta to scan for
	load()
	global c3po
	global index
	records=[]

	base=os.getcwd()

	mirror='null'
	if _.switches.isActive('Mirror'):
		mirror = _.switches.values('Mirror')[0]
	if _.switches.isActive('View-Mirror'):
		# _.pr('Mirror:\n')
		mirror = _.switches.values('View-Mirror')[0]
		base=index[mirror]['base']
		c3po = index[mirror]['folders']

	for fo in c3po:
		if not _.switches.isActive('View-Mirror'): records.append(fo)
		if _.showLine(fo):
			print(fo)
			# _.pr(fo,c='cyan')
	index[mirror]={'base':os.getcwd(),'folders':records}
	if _.switches.isActive('Mirror') and not _.switches.isActive('View-Mirror'): _.saveTableDB(index,'fo.index')




def load():
	global c3po
	global index
	index = _.getTableDB('fo.index')
	# print(index)
	if _.switches.isActive('Recursive'):
		r=1
	else:
		r=0
	if not _.switches.isActive('Folders'):
		c3po = _.fos(r=r)
	else:
		c3po=[]
		for f in _.switches.values('Folders'):
			for fo in _.fos(f,r=r):
				# print(fo)
				# sys.exit()
				if not _.switches.isActive('Full-Path'):
					fo = fo.replace( __.path(os.getcwd())+os.sep+f+os.sep, '' )
				c3po.append(fo)
	# sys.exit()
	if not _.switches.isActive('Full-Path'):
		for i, fo in enumerate(c3po):
			c3po[i]=fo.replace( __.path(os.getcwd())+os.sep, '' )
	c3=[]
	for i, fo in enumerate(c3po):
		if _.showLine(fo): c3.append(fo)
	c3po=c3

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()
