import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'gptChats.py',
	'description': 'Save, Search, and Download GPT Chats and Files. Evan every file at once!!',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp(''),
						_.hp('Chat:'),
						_.hp('\tchats -list'),
						_.hp('\tchatschats -id 683eedef-c964-800a-b0c7-80f714b03bd7 --s + nexa'),
						_.hp('\tchats -id 683eedef-c964-800a-b0c7-80f714b03bd7 + nexa -cid 36'),
						_.hp(''),
						_.hp('Files:'),
						_.hp('\tchats -list'),
						_.hp('\tchats -id 683b3bf4-1b68-800a-bfae-f3152a05a7af -name'),
						_.hp('\tchats -id 683b3bf4-1b68-800a-bfae-f3152a05a7af       <--(file snippet)'),
						_.hp('\tchats -id 683b3bf4-1b68-800a-bfae-f3152a05a7af -fid 2'),
						_.hp(''),
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

import re

def action():
	liveData=False
	raw = '\n'.join(_.pp())
	if raw.startswith('{') and raw.endswith('}'):
		liveData=True	
		if not '"chat": [' in raw and not '"files": [' in raw:
			liveData=False
	if liveData:
		import json
		data = json.loads(raw)
		_.saveTable(data,'gptChats2.dex',p=0)
	else:
		data = _.getTable('gptChats2.dex')
	
	if not 'chat' in data and not 'files' in data:
		_.e('Invalid data. Expecting live data or previously saved data.')
		return
	

	if 'chat' in data:
		spent = []
		for i, chat in enumerate(data['chat']):
			role = chat['role']
			content = chat['content']
			valid = False
			for line in content.split('\n'):
				if _.showLine(line):
					if not valid:
						_.pr(line=1,c='green')
						_.pr()
						_.pr(role,c='cyan')
						if _.switches.isActive('PlusClose'):
							_.pr()
							_.pr(content)
							break

					valid = True
					_.pr(line)





########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)