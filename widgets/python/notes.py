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
	_.switches.register( 'Today', '-t,-today' )
	_.switches.register( 'Alias', '-a,-alias','karla' )
	_.switches.register( 'Files', '-f,-file,-files','index.md', isData='glob', description='Files', isRequired=False )
	_.switches.register( 'is', '-is','person' )
	_.switches.register( 'New', '-n,-new' )

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
	'file': 'notes.py',
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
	# _.switches.trigger( 'Alias', alias_trigger )
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )


########################################################################################
# START

def alias_trigger(data):
	global aliases; load();
	if data in aliases: return aliases[data];
	return data

def alias_create(alias,file):
	global aliases
	aliases[alias]=file
	_.saveTable( aliases, 'app-notes-alias.index' )
	return aliases[alias]

def is_create(alias):
	global nis
	nis[alias]=os.getcwd()+os.sep
	_.saveTable( nis, 'app-notes-is.index' )
	return nis[alias]

def is_trigger(data):
	global nis; load();
	if data in nis: return nis[data];
	return data


def op(path): _file_open.switch('Files',path); _file_open.action(); return path;

def new(what,path=None):
	_.pr(what)
	_.pr(_v.json_temp)

	if 'person' in what:
		op(_v.json_temp)
		_.saveTable2({
								'epoch': time.time(),
								'birthdate': 'r',
								'name': {
											'nick': 'r',
											'first':'',
											'middle':'',
											'last':'',
											'init':'r',
								},
								'connect': [{'mobile':'813'}],
								'id': _.HID('notes'),
			},_v.json_temp)
		op(_v.json_temp)
		wait=input(' > ')
		get=_.getTable2(_v.json_temp)
		if not get['name']['nick'] == 'r':
			fn=get['birthdate']+'-'+get['name']['init']+'-'+get['name']['nick']
			_v.mkdir( _v.life+'people'+os.sep+fn )
			_.saveTable2(get,_v.life+'people'+os.sep+fn+os.sep+'index.hash')
			page=str(requests.post('https://eyeformeta.com/apps/whatever/file.php', data = {'path':'people'+'/'+fn+'/'+'index.hash','data':simplejson.dumps(get, indent=4, sort_keys=False)}).content,'iso-8859-1')
			print(page)
			return get


def action():
	#--> min, architecture {:strict:}
	#--> trigger/callback  <w#
	global aliases
	load()
	fo=_v.life+str(_.isDate(time.time(),f='year'))+os.sep+str(_.isDate(time.time(),f='woy2'))+os.sep
	_v.mkdir(fo)
	today=fo+_.isDate(time.time(),f='date')+'.md'
	if _.switches.isActive('Today'): _.pr(today,c='cyan'); return op(today);

	if _.switches.isActive('Alias') and _.switches.isActive('Files'): alias_create(_.switches.values('Alias')[0],_.switches.values('Files')[0]); return None;
	path=None
	if _.switches.isActive('Files'): path=_.switches.values('Files')[0];
	if _.switches.isActive('Alias'): path=alias_trigger(_.switches.values('Alias')[0]);

	if _.switches.isActive('is') and not _.switches.isActive('New'):
		for xXx in _.switches.values('is'): is_create(xXx);
		return _.sw
	if _.switches.isActive('is') and _.switches.isActive('New'):
		for xXx in _.switches.values('is'): return new(xXx);


	if path:
		if os.path.isfile(path): op(path); return path;
		return op(path)



def load():
	global aliases
	global nis
	if aliases is None:
		aliases = _.getTable( 'app-notes-alias.index' )
	if nis is None:
		nis = _.getTable( 'app-notes-is.index' )
aliases=None
nis=None
_file_open = _.regImp( __.appReg, 'file-open' )
_file_open.switch('App',_v.meta['code_editor'])
os=_.imp('os.sep')
os=_.imp('os.path.isdir')
os=_.imp('os.path.isfile')
os=_.imp('os.getcwd')
requests=_.imp('requests.post')
simplejson = __.imp('simplejson')
'''
simplejson.loads(var)
simplejson.dumps(rows, indent=4, sort_keys=False)
simplejson.dumps(rows)
'''

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()