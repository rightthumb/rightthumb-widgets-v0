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
	_.switches.register( 'Source', '-src,-from,-f,-file','file.txt', isRequired=True )
	_.switches.register( 'Destination', '-dst,-to','file2.txt', isRequired=False )
	_.switches.register( 'Delete', '-del,-delete', isRequired=False )
	_.switches.register( 'Backup', '-bk,-backup', isRequired=False )
	_.switches.register( 'Ghost', '-ghost', isRequired=False )
	_.switches.register( 'Yes', '-y,-yes', isRequired=False )

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
	'file': 'MoveDelete.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'changes the path in the backup log (so auto versions are accurate)',
		_.ail(1,'including all meta files')+
		# _.aib('one')+
	'categories': [
						'rename',
						'mv',
						'move',
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
						_.hp('p MoveDelete -src D:\\websites\\domains\\test.file -dst C:\\Users\\Scott\\.rt\\profile\\daily\\2023\\38\\09-23'),
						_.hp('p MoveDelete -src D:\\websites\\domains\\test.file '),
						_.hp('p MoveDelete -src D:\\websites\\domains\\secure.md -ghost '),
						_.hp('p MoveDelete -src D:\\websites\\domains\\secure.md -ghost backup'),
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
#n)--> start



def action():
	_md = _.regImp( __.appReg, '_rightThumb._MoveDelete' )
	if _.switches.isActive('Yes'): _md.switch('Yes')
	if _.switches.isActive('Backup'): _md.switch('Backup')
	if _.switches.isActive('Delete'): _md.switch('Delete')
	if _.switches.isActive('Ghost'): _md.switch('Ghost',_.switches.values('Ghost'))
	if _.switches.isActive('Source'): _md.switch('Source',_.switches.values('Source'))
	if _.switches.isActive('Destination'): _md.switch('Destination',_.switches.values('Destination'))
	_md.action()





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


 
