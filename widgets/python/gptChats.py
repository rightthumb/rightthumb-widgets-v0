import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'List', '-l,-list' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'SearchTitles', '-t,-title,-titles' )
	_.switches.register( 'File-id', '-fid' )
	_.switches.register( 'GPT-id', '-id,-gid' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
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
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
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
			if not _.switches.all():
				_.pr('❌ No data provided', c='red')
				_.pr()
				_.pr('sb.fn.gpt()   # Files', c='yellow')
				_.pr('sb.fn.gpt2()  # Chats', c='yellow')
				return
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
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)