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
	_.switches.register( 'Search', '-s,-search,-c,-count' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
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


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'pipe-count.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'how many needles in the haystack',
		# _.ail(1,'how many needles in the haystack')+
		# _.aib('how many needles in the haystack')+
	'categories': [
						'needles',
						'haystack',
						'substring',
						'string',
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
						_.hp('p -paste | p pipe-count -s { ['),
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

def action():
	#--> min, architecture {:strict:}

	text='\n'.join(_.isData(r=0))
	count=0
	for search in _.switches.values('Search'):
		c=text.count(_.ci(search))
		_.pr(_.addComma(c), _.ci(search),c='cyan')
		count+=c

	_.pr( _.addComma(count), c='green' )
	if count:
		_.pr( _.addComma(len(text)/count),'spread', c='green' )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()