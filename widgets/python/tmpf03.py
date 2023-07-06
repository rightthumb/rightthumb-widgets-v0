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
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
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
	'file': 'tmpf3.py',
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
						_.hp('p tmpf3 -file file.txt'),
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



_.l.conf('clean-pipe',False)
# _.l.conf('clean-pipe',True)


_.l.sw.register( triggers, sw )

########################################################################################
#n)--> start
import uuid
# import pickle

def action():
	data = '\n'.join(_.isData(r=0))
	data=data=_str.do('.sh',data)
	data=data.split('\n')
	start=time.time()
	# for line in data: uuid.uuid5(uuid.NAMESPACE_URL, line ).hex
	for line in data: uuid.uuid5(uuid.NAMESPACE_URL, line ).hex
	end=time.time()
	diff=end-start
	_.pr(    ' diff:',  diff)
	_.pr(    '  int:',  int(diff))
	_.pr(    ' i/60:',  int(diff)/60)
	_.pr(    'lines:',  _.addComma(len(data)) )
	_.pr(    'chars:',  _.addComma(len( '\n'.join(data) )) )

	_.pr(line=1,c='red')

	start=time.time()
	uuid_md5=uuid.uuid5(uuid.NAMESPACE_URL, '\n'.join(data) ).hex
	end=time.time()
	diff=end-start
	_.pr(    ' diff:',  diff)
	_.pr(    '  int:',  int(diff))
	_.pr(    ' i/60:',  int(diff)/60)
	_.pr(    'lines:',  _.addComma(len(data)) )
	_.pr(    'chars:',  _.addComma(len( '\n'.join(data) )) )
	_.pr(    'uuid-md5:',  uuid_md5 )


##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)