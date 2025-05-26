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
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
##################################################

# app_navigator: switches
def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i', group='Group Name' )
		##  -->    p SwitchGroupsExamples   <--
	# #e)--> examples
	_.switches.register( 'List', '-l,-list' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'SearchTitles', '-t,-title,-titles' )
	_.switches.register( 'File-id', '-fid' )
	_.switches.register( 'GPT-id', '-id,-gid' )

_._default_settings_()

# __.setting('pipe-cleaner',False)
# __.setting('pipe-cleaner', {'first': False})

# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
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
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()

	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	# _.switches.trigger( 'Files', _.isFileSimple )                 # No File Registration          (Fn Alias Resolves To: def isFile)
	
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

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

	#n)--> caseUnspecific
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)
		#     or
		# results = [rel for rel in [subject for subject in _.isData(r=0) if _.showLine(subject)]]


	#n)--> fields
		# data = []
		# for k in code.db: data.append({'name': k+'  ' })
		# _.fields.asset( 'data', data )
		# for k in code.db:
		# 	_.pr(   _.fields.value( 'data', 'name', k+':' )+'  '+str(len(code.db[k]))   )

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;


	#n)--> gptbot
		# from  _rightThumb._gptbot import GPT4oBot
		# bot = GPT4oBot()
		# bot.init_goal(goal='build a calculator webpage')
		# while True:
		# 	task, result = bot.run_next_task()
		# 	if not task:
		# 		print(result)
		# 		break
		# 	print(f"\n✅ Completed: {task}\n{result}\n")
		# 	input("Press Enter to continue...")


#e)--> examples
########################################################################################
#n)--> start




'''
{
	"id": "68064764-0a54-800a-a45f-c73888222116",
	"title": "Secure PostgreSQL Installation Script",
	"url": "https://chatgpt.com/c/68064764-0a54-800a-a45f-c73888222116",
	"hostname": "chatgpt.com",
	"pathname": "/c/68064764-0a54-800a-a45f-c73888222116",
	"epoch": 1745346020,
	"date": "2025-04-22 14:20",
	"files": [
		{
			"name": "install_postgres_secure.sh",
			"content": "#!/bin/bash\n\nset -e\n\n# Detect package manager"
		}
	]
}
'''

def action():
	if _.switches.isActive('List'):
		fo = _v.tt + _v.slash + 'gptChats' + _v.slash
		files = _.fo(fo)
		for file in files:
			cache = _.getTable2(file)
			id = _.pr(cache.get('id', ''), c='purple', p=0)
			title = _.pr(cache.get('title', ''), c='yellow', p=0)
			if _.showLine(title):
				_.pr(id, title)
		return None

	data_raw = '\n'.join(_.pp())
	if not _.isData(r=0) or data_raw.startswith('{'):
		if not data_raw.startswith('{'):
			data_raw = '\n'.join(_.isData(r=0))
		if data_raw.startswith('{'):
			import simplejson as json
			dic = json.loads(data_raw)
			path = f"gptChats{_v.slash}{dic['id']}.cache"
			_.saveTable(dic, path, p=0)
			_.saveTable(dic, 'gptChats.dex', p=0)

	if _.switches.isActive('GPT-id'):
		file_path = f"gptChats{_v.slash}{_.switches.value('GPT-id')}.cache"
		gpt = _.getTable(file_path)
	else:
		gpt = _.getTable('gptChats.dex')

	if not _.switches.all() or (len(_.switches.all()) == 1 and _.switches.isActive('GPT-id')):
		_.pr(gpt.get('id', ''), c='purple')
		_.pr(gpt.get('title', ''), c='yellow')
		_.pr()

		if 'files' in gpt:
			for i, file in enumerate(gpt['files']):
				name = file.get('name', '')
				content = file.get('content', '')
				words = content.strip().split()
				snippet = ' '.join(words[:8])
				if _.showLine(name):
					_.pr(f'\t{i+1}\tfile\t{snippet}')
		elif 'chat' in gpt:
			for i, chat in enumerate(gpt['chat']):
				role = chat.get('role', '')
				role = 'gpt' if role == 'assistant' else role
				content = chat.get('content', '')
				words = content.strip().split()
				snippet = ' '.join(words[:8])
				if _.showLine(content):
					I = _.pr(i+1, c='cyan', p=0)
					Role = _.pr(role, c='purple', p=0)
					Snippet = _.pr(snippet, c='yellow', p=0)
					_.pr(f'\t{I}\t{Role}\t{Snippet}')

		_.pr()

	elif _.switches.isActive('File-id'):
		id = int(_.switches.value('File-id')) - 1

		if 'files' in gpt and id < len(gpt['files']):
			file_content = gpt['files'][id]['content']
		elif 'chat' in gpt and id < len(gpt['chat']):
			file_content = gpt['chat'][id]['content']
		else:
			_.pr('❌ Invalid File-id', c='red')
			return

		file_content = file_content.replace(chr(10), '\n').replace(chr(27), '').replace('\r', '')
		if _.switches.isActive('NoColor'):
			_.pr(file_content)
		else:
			_.printVarSimpleFake2(file_content)
		# _.pr(file_content)



# def action():

# 	if _.switches.isActive('List'):
# 		fo = _v.tt+_v.slash+'gptChats'+_v.slash
# 		files = _.fo(fo)
# 		for file in files:
# 			cache = _.getTable2(file)
# 			id = _.pr(cache['id'],c='purple',p=0)
# 			title = _.pr(cache['title'],c='yellow',p=0)
# 			if _.showLine(cache['title']):
# 				_.pr(id,title)







# 		return None
# 	# print(_.isData(r=0))
# 	if not _.isData(r=0) or '\n'.join(_.pp()).startswith('{'):
# 		if '\n'.join(_.pp()).startswith('{'):
# 			data = '\n'.join(_.pp())
# 		else:
# 			data = '\n'.join(_.isData(r=0))
# 		if data.startswith('{'):
# 			import simplejson as json
# 			dic = json.loads(data)
# 			_.saveTable(dic,'gptChats'+_v.slash+dic['id']+'.cache',p=0)
# 			_.saveTable(dic,'gptChats.dex',p=0)
# 	if _.switches.isActive('GPT-id'):
# 		gpt = _.getTable('gptChats'+_v.slash+  _.switches.value('GPT-id')  +'.cache')
# 	else:
# 		gpt = _.getTable('gptChats.dex')
# 	if not _.switches.all() or (  len(_.switches.all()) == 1 and _.switches.isActive('GPT-id') ):
# 		_.pr(gpt['id'],c='purple')
# 		_.pr(gpt['title'],c='yellow')
# 		_.pr()
# 		for i,file in enumerate(gpt['files']):
# 			if _.showLine(file['name']):
# 				_.pr('\t',i+1,'\t',file['name'],c='cyan')
# 			# _.pr(file['content'])
# 		_.pr()

# 	elif _.switches.isActive('File-id'):
# 		id = int(_.switches.value('File-id'))-1
# 		file = gpt['files'][id]['content']
# 		file = file.replace( chr(10), '\n' )
# 		file = file.replace( chr(27), '' )
# 		file = file.replace( '\r', '' )
# 		_.pr(file)
		
	# _.pv(gpt)
	


	# load(); global c3po;

	# Threads = _.Threads(t=10, onDone=None)
	# def Done(result): pass  # other onFn have no args
	# Threads.queue(fn,  ak=None, timeout=None, onStart=None, onDone=Done, onKill=None, onTimeout=None, label=None)  # ak = args, kwargs

	#n)--> iterate
	# for subject in _.isData(r=0): _.pr(subject)
	# for subject in _.myData(): _.pr(subject)
	

# def load():
# 	global c3po
# 	c3po = _.getTable( 'table' )
# 	#n)--> print table
# 	_.pt(c3po)


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__)

