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
__.setting('require-pipe||file',True)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'odt.py',
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
						_.hp('p odt -file file.txt'),
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


from odf import text, teletype
from odf.opendocument import load
def action():
	sep=os.sep
	for path in _.isData(r=1):
		# textdoc = load('C:\\Users\\Scott\\.rt\\profile\\daily\\2022\\33\\08-20\\Text Documents\\Accounts and Passwords\\thinksteroids Account.odt')
		textdoc = load(path)
		#n)--> test
		# for x in dir( text ):
		#     try: allparas = textdoc.getElementsByType(eval('text.'+x))
		#     except: allparas  = None


		#     if not allparas is None:
		#         # _.pr(x,type(allparas))
		#         # _.pr(line=1)
		#         _.pr(x)
		#         for y in allparas:
		#             _.pr('\t',type(y))

		#     # print(x)
		# sys.exit()


		#n)--> original
		lines=[]
		valid=False
		allparas = textdoc.getElementsByType(text.P)
		for _par in allparas:
			_teletype=teletype.extractText(_par)
			if not_blank(_teletype):
				valid=True
				lines.append(_teletype)
		if valid:
			if not sep in path:
				label=path.replace('.odt','')
			else:
				label=path.split(sep)[-1].replace('.odt','')
			_.pr()
			_.pr('_________________')
			_.pr(label)
			for line in lines:
				_.pr('    ',line)

			
			

		#n)--> fail, del
		# allparas = textdoc.getElementsByType(text.Page)
		# _teletype=teletype.extractText(allparas)
os=__.imp('os.sep')
def not_blank(text):
	if not text: return False
	for t in text:
		if t in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': return True
	return False

##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
