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
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files' )
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
	'file': 'transcript.py',
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
						_.hp('p transcript -file file.txt'),
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
#n)--> start

def action():

	for path in _.isData(r=0):
		lines = _.getText(path,raw=1,clean=2).replace('\r','').split('\n')
		run = 1
		for line in lines:
			if 'audio-chunks' in line or 'p speech -f' in line :
				run = 2
		for line in lines:
			line=line.strip()

			if run==1:
				wav=True
				if not 'transcribe.py' in line:
					pass
					# line = line[line.index(' ')+2:]
				else:
					p = line[line.index('.py')+4:].replace('.mp3.wav','').split('_')
					line = p[0]+'-'+p[1]+'-'+p[2]+' @ '+p[3]+':'+p[4]+':'+p[5].split(' ')[0]
					wav=True
					print('\n________________________________________________')

				if _.showLine(line):
					print(line.strip())
					if wav: print()

			elif run==2:
				wav=False
				if line.startswith('audio-chunks') or 'transcribe.py' in line:
					line = line[line.index(' ')+2:]
				elif '-f' in line:
					p = line[line.index(' -f ')+3:].replace('.mp3.wav','').split('_')
					line = p[0]+'-'+p[1]+'-'+p[2]+' @ '+p[3]+':'+p[4]+':'+p[5]
					wav=True
					print('\n________________________________________________')

				if _.showLine(line):
					print(line.strip())
					if wav: print()


##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
