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
	_.switches.register( 'Folders', '-f,-folder,-Folders' )
	_.switches.register( 'Recursive', '-r,recursive' )

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
	'file': 'organize-files-by-date.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'move file year/month/file',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'move',
						'file',
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
						_.hp('b applog'),
						_.hp('p organize-files-by-date'),
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


########################################################################################
# START



def process(folder):
	global confirmed
	try: items=os.listdir(folder)
	except Exception as e: _.e(e)

	for item in items:
		path=folder+os.sep+item
		if os.path.isfile(path):
			me=_dir.info(path,f='me')
			file=_dir.info(path)['name']
			# # _.pv(file)
			# # sys.exit()
			# # file=_dir.info(path,f='file')
			# # _.pr(me)
			# month=_.isDate(me,f='month')
			

			nf=folder+_v.slash+_.day(me)
			_.pr(path)
			_.pr(nf)



			if not confirmed:
				ask=input('move ?Yn: ')
				if not 'n' in ask.lower(): confirmed=True


			if confirmed: _v.mkdir(nf); shutil.move(path,nf+os.sep+file);


		elif os.path.isdir(path):
			if _.switches.isActive('Recursive'): process(path)

def action():
	
	if _.switches.isActive('Folders'): folders=_.switches.values('Folders')
	else: folders=[os.getcwd()]

	for folder in folders: process(folder)
# import shutil
confirmed=False
import _rightThumb._dir as _dir
shutil=__.imp('shutil.move')
os=__.imp('os.sep')
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()