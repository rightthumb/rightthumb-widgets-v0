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

# audit.bat
'''
@echo off
echo ____________________________________________________________________ >> %userprofile%\tasklist.txt
echo %DATE:~-4%-%DATE:~4,2%-%DATE:~7,2% @ %TIME:~0,2%.%TIME:~3,2% >> %userprofile%\tasklist.txt
tasklist >> %userprofile%\tasklist.txt
echo.
echo .         audit complete
echo.
title audit complete
prompt -
echo.
set /p load= -
echo %load%
rem if [%load%] == [y]
call rr.bat
'''
# "commandline": "cmd /k \"C:\\Users\\Scott\\audit.bat\"",



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
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )

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

# def parse_tasklist(output):

import re
def parse_tasklist(output):
	lines = output.strip().split("\n")
	headers = lines.pop(0).split()
	tasks = []
	for line in lines:
		task = {}
		# Use regex to extract values from the line
		match = re.match(r'(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s+([\d,]+ K)', line)
		if match:
			task['ImageName'] = match.group(1)
			task['PID'] = int(match.group(2))
			task['SessionName'] = match.group(3)
			task['Session#'] = int(match.group(4))
			task['MemUsage'] = int(match.group(5).replace(',', '').replace('K', ''))
			tasks.append(task)
	return tasks

def get_top_5_memory_usage(tasks):
	mem_usage_dict = {}
	grand_total = 0

	for task in tasks:
		image_name = task['ImageName']
		mem_usage = task['MemUsage']
		grand_total += mem_usage

		if image_name in mem_usage_dict:
			mem_usage_dict[image_name] += mem_usage
		else:
			mem_usage_dict[image_name] = mem_usage

	top_5_memory_usage = sorted(mem_usage_dict.items(), key=lambda x: x[1], reverse=True)[:5]

	return top_5_memory_usage, grand_total

def kilobytes_to_bytes(kilobytes):
	bytes_value = kilobytes * 1024
	return bytes_value

def size(mem): return _.formatSize(kilobytes_to_bytes(mem))


def sect():
	return {
				'date': '',
				'epoch': 0,
				'tasklist': [],
				'table': []
	}

def extract(lines):
	sections=[]
	section=sect()

	active=False
	for line in lines:
		if line.strip().startswith('__________________') and section['epoch'] and section['tasklist']:
			section['table'] = parse_tasklist( '\n'.join(section['tasklist']).strip() )
			sections.append(section)
			section=sect()
			active=False
		elif line.strip().startswith('Image Name'):
			active=True
		if active:
			section['tasklist'].append(line)
		if not active and line.strip().startswith('20'):
			section['epoch']=_.autoDate(line.strip().replace('.',':').replace(' ',''))
			section['date']=_.friendlyDate(section['epoch'])
			section['head']=line.strip().replace('.',':').replace(' ','')
	section['table'] = parse_tasklist( '\n'.join(section['tasklist']).strip() )
	sections.append(section)

	for rec in sections:
		_.pr(line=1)
		# _.pv(rec)
		# sys.exit()
		print(rec['date'])
		top_5_memory_usage, grand_total = get_top_5_memory_usage(rec['table'])
		m=0
		for r in top_5_memory_usage:
			# print(r[0])
			m+=r[1]
		print()
		mems=[]
		for r in top_5_memory_usage: mems.append({'app':r[0],'bytes':r[1],'memory':size(r[1])})
		mems=_.sort(mems,'d.bytes')
		_.pt(mems,'app,memory')
		_.pr('\tTop 5 total:',size(m),c='yellow')
		_.pr('Total:',size(grand_total),c='green')
		# for r in mems: print(r['mem'],r['app'])

		# print(top_5_memory_usage)

		# sys.exit()

		# _.pt(rec['table'])


def action():
	extract(str('\n'.join(_.isData(r=0))+'\n').split('\n'))
	


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

