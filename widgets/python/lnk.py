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
import os, sys, time
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
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Folders', '-fo,-fos,-folder,-folders' )
	_.switches.register( 'Recursive', '-r,-recursive' )
	_.switches.register( 'JSON', '-json' )
	_.switches.register( 'Dump', '-dmp' )

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

import pylnk3

def file(path):
	directory, filename = os.path.split(path)
	name, extension = os.path.splitext(filename)
	return name




def info(path):
	lnk_info = {}
	with open(path, "rb") as f:
		lnk = pylnk3.parse(f)

		lnk_info["name"] = file(path)
		try:
			lnk_info["access_time"] = lnk.access_time
		except AttributeError:
			lnk_info["access_time"] = None
		try:
			lnk_info["arguments"] = lnk.arguments
		except AttributeError:
			lnk_info["arguments"] = None
		try:
			lnk_info["creation_time"] = lnk.creation_time
		except AttributeError:
			lnk_info["creation_time"] = None
		try:
			lnk_info["description"] = lnk.description
		except AttributeError:
			lnk_info["description"] = None
		try:
			lnk_info["extra_data"] = lnk.extra_data
		except AttributeError:
			lnk_info["extra_data"] = None
		try:
			lnk_info["file"] = lnk.file
		except AttributeError:
			lnk_info["file"] = None
		try:
			lnk_info["file_flags"] = lnk.file_flags
		except AttributeError:
			lnk_info["file_flags"] = None
		try:
			lnk_info["file_size"] = lnk.file_size
		except AttributeError:
			lnk_info["file_size"] = None
		try:
			lnk_info["hot_key"] = lnk.hot_key
		except AttributeError:
			lnk_info["hot_key"] = None
		try:
			lnk_info["icon"] = lnk.icon
		except AttributeError:
			lnk_info["icon"] = None
		try:
			lnk_info["icon_index"] = lnk.icon_index
		except AttributeError:
			lnk_info["icon_index"] = None
		try:
			lnk_info["link_flags"] = lnk.link_flags
		except AttributeError:
			lnk_info["link_flags"] = None
		try:
			lnk_info["link_info"] = lnk.link_info
		except AttributeError:
			lnk_info["link_info"] = None
		try:
			lnk_info["modification_time"] = lnk.modification_time
		except AttributeError:
			lnk_info["modification_time"] = None
		try:
			lnk_info["path"] = lnk.path
		except AttributeError:
			lnk_info["path"] = None
		try:
			lnk_info["relative_path"] = lnk.relative_path
		except AttributeError:
			lnk_info["relative_path"] = None
		try:
			lnk_info["shell_item_id_list"] = lnk.shell_item_id_list
		except AttributeError:
			lnk_info["shell_item_id_list"] = None
		try:
			lnk_info["show_command"] = lnk.show_command
		except AttributeError:
			lnk_info["show_command"] = None
		try:
			lnk_info["specify_local_location"] = lnk.specify_local_location
		except AttributeError:
			lnk_info["specify_local_location"] = None
		try:
			lnk_info["specify_remote_location"] = lnk.specify_remote_location
		except AttributeError:
			lnk_info["specify_remote_location"] = None
		try:
			lnk_info["window_mode"] = lnk.window_mode
		except AttributeError:
			lnk_info["window_mode"] = None
		try:
			lnk_info["work_dir"] = lnk.work_dir
		except AttributeError:
			lnk_info["work_dir"] = None
		try:
			lnk_info["working_dir"] = lnk.work_dir
		except AttributeError:
			lnk_info["working_dir"] = None
		try:
			lnk_info["write"] = lnk.work_dir
		except AttributeError:
			lnk_info["write"] = None
	if _.switches.isActive('Dump'):
		_.pr(_.toYML(lnk_info))

	return lnk_info






def process(path):
	if os.path.isfile(path):
		global records
		try:
			rec = info(path)
			records.append(rec)
		except: pass



def action():
	global records
	records=[]
	paths=[]

	if not _.switches.isActive('Folders') and not _.isData():
		_.switches.fieldSet( 'Folders', 'active', True )
		_.switches.fieldSet( 'Folders', 'value', os.getcwd() )
		_.switches.fieldSet( 'Folders', 'values', [os.getcwd()] )

	if _.switches.isActive('Folders'):
		paths=_.switches.values('Folders')
	else:
		paths=_.isData()

	for path in paths:
		if os.path.isfile(path):
			process(path)
		elif os.path.isdir(path):
			_.fo(path,script=process,r=_.switches.isActive('Recursive'))
	pass
	if _.switches.isActive('JSON'):
		return None

	if len(records) == 0:
		_.e('No Records','No records were found')
	elif len(records) == 1:
		print(records[0]['path'])
		# _.pr( _.toYML(records[0]) )
	else:
		_.pt(records,'name,path')
		_.pr('',len(records),c='yellow')


_.switches.fieldSet( 'Long', 'active', True )


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

