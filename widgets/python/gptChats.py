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
	_.switches.register( 'Name', '-n,-name' )
	_.switches.register( 'Download', '-dl' )
	_.switches.register( 'Search', '--s,-search' )
	_.switches.register( 'Chat-id', '-cid' )
	_.switches.register( 'OpenChat', '-o,-open' )
	_.switches.register( 'Just-Title', '-title' )
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
	if _.switches.isActive('OpenChat'):
		url = 'https://chatgpt.com/c/'
		
		a = _.switches.value('OpenChat')
		b = _.switches.value('GPT-id')
		
		if a:
			url += a
		elif b:
			url += b
		else:
			_.pr('❌ Missing -o or -id for open', c='red')
			return
		import webbrowser
		webbrowser.open(url)
		return None
	
	fo = _v.tt + _v.slash + 'gptChats' + _v.slash

	if _.switches.isActive('Chat-id'):
		if not _.switches.isActive('GPT-id'):
			_.pr('❌ Missing -id for search', c='red')
			return
		gptID = _.switches.value('GPT-id')

		cache = _.getTable2(fo+gptID+'.cache')
		content = cache['chat'][int(_.switches.value('Chat-id')) - 1].get('content', '')
		# _.pr(content, c='cyan')
		_.pr(_.colorPlus(content))
		_.pr(line=1,c='cyan')
		# _.printVarSimpleFake2(content)
		return None



	if _.switches.isActive('Search'):
		if not _.switches.isActive('GPT-id'):
			_.pr('❌ Missing -id for search', c='red')
			return
		gptID = _.switches.value('GPT-id')

		cache = _.getTable2(fo+gptID+'.cache')
		key = 'chat' if 'chat' in cache else 'files'
		_.pr('Type: ',key.title(), c='yellow')
		for i, item in enumerate(cache[key]):
			content = item.get('content', '')
			# print(content)
			ii = i + 1
			if _.showLine(content):
				snippet = content[:50].replace('\n', ' | ')
				# _.pr(line=1,c='cyan')
				if key == 'chat':
					words = content.strip().split()
					snippet = ' '.join(words[:8])
					_.pr(f'\t{ii}\t{item.get("role", "unknown")}\t{snippet}...')
				else:
					_.pr(f'\t{ii}\tfile\t{item.get("name", "unknown")}\t{snippet}...')

		return None


	if _.switches.isActive('List'):
		files = _.fo(fo)
		for file in files:
			cache = _.getTable2(file)
			key = 'chat ' if 'chat' in cache else 'files'
			id = _.pr(cache.get('id', ''), c='purple', p=0)
			title = _.pr(cache.get('title', ''), c='yellow', p=0)
			if _.showLine(title):
				_.pr(id, key, title)
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




		if _.switches.isActive('Download'):
			download_all()




		if _.switches.isActive('Name') and not _.switches.isActive('File-id'):
			if _.switches.isActive('GPT-id'):
				file_path = f"gptChats{_v.slash}{_.switches.value('GPT-id')}.cache"
				gpt = _.getTable(file_path)
			else:
				gpt = _.getTable('gptChats.dex')

			if 'files' in gpt:
				_.pr()
				_.pr('🗂️ Code Headings:', c='cyan')
				for i, file in enumerate(gpt['files']):
					name = '📁 ' + file.get('name', '')
					if _.showLine(name):
						I = _.pr(i + 1, c='cyan', p=0)
						Label = _.pr(name, c='green', p=0)
						_.pr(f'\t{I}\t{Label}')
				_.pr()
			else:
				_.pr('⚠️ No files found in this entry', c='red')
			return





	if _.switches.isActive('GPT-id'):
		file_path = f"gptChats{_v.slash}{_.switches.value('GPT-id')}.cache"
		gpt = _.getTable(file_path)
	else:
		gpt = _.getTable('gptChats.dex')
	if not _.switches.all() or (len(_.switches.all()) == 1 and _.switches.isActive('GPT-id')):
		_.pr(gpt.get('id', ''), c='purple')
		_.pr(gpt.get('title', ''), c='yellow')
		_.pr()
		Type = ''
		if 'files' in gpt:
			Type = 'files'; Type = _.pr(Type, h='orange',p=0)
			for i, file in enumerate(gpt['files']):
				name = '📁 ' + _.pr(file.get('name', ''), h='dark_salmon',p=0)
				content = file.get('content', '')
				words = content.strip().split()
				snippet = ' '.join(words[:8])
				if _.showLine(name):
					_.pr(f'\t{i+1}\t{Type}\t{name}')
		elif 'chat' in gpt:
			# Type = 'chat'; Type = _.pr(Type, c='yellow',p=0)
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



def download_all():
	import sys, os
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'os', 'file')))
	from FileAnalyzer import FileAnalyzer

	if _.switches.isActive('GPT-id'):
		file_path = f"gptChats{_v.slash}{_.switches.value('GPT-id')}.cache"
	else:
		_.pr('❌ Missing -id for download', c='red')
		return

	gpt = _.getTable(file_path)
	base_folder = 'downloads'
	all_files = gpt.get('files', [])
	skipped = []

	# Build cross-reference tokens from all files
	name_to_content = {
		file.get('name', '').replace('📁', '').strip(): file.get('content', '')
		for file in all_files
	}
	name_patterns = FileAnalyzer.fn.generate_patterns_dict(name_to_content)
	reference_tokens = {}
	for fname, text in name_to_content.items():
		for token in FileAnalyzer.fn.extract_name_tokens(text):
			reference_tokens[token] = text
	ref_patterns = FileAnalyzer.fn.generate_patterns_dict(reference_tokens)
	ref_matches = FileAnalyzer.fn.compare_patterns_dicts(ref_patterns, name_patterns, threshold=0.25)

	for i, file in enumerate(all_files):
		name = file.get('name', '').replace('📁', '').strip()
		content = file.get('content', '')

		# 🧠 Determine if it's likely a file
		likelihood = FileAnalyzer.fn.score_file_likelihood(name, content, list(reference_tokens.keys()))
		if likelihood < 0.35:
			skipped.append((i + 1, name, likelihood))
			continue

		# 🧠 Guess file path
		candidates = (
			FileAnalyzer.fn.scrape_windows_file_paths(name + '\n' + content) +
			FileAnalyzer.fn.scrape_windows_file_paths2(name + '\n' + content) +
			FileAnalyzer.fn.scrape_linux_file_paths(name + '\n' + content)
		)

		# 🧼 Filter out junky candidates that are just fragments or code
		candidates = [
			p for p in candidates
			if (
				len(p) < 255 and
				'.' in os.path.basename(p) and
				not os.path.basename(p).startswith('.') and
				not any(x in p for x in ['_.', 'pr(', 'replace', 'print', '"', "'", '\\n', 'def ', 'path.', 'snippet', 'file.', '=', ':'])
			)
		]

		if not candidates and likelihood < 0.5:
			skipped.append((i + 1, name, likelihood))
			continue

		if candidates:
			rel_path = candidates[0]
		else:
			# Look for best reference match
			ref_guess = None
			for ref_name, matches in ref_matches.items():
				for matched_name, score in matches:
					if matched_name == name:
						ref_guess = ref_name
						break
				if ref_guess:
					break
			if ref_guess:
				rel_path = ref_guess
			else:
				parts = name.split()
				for p in parts:
					if '.' in p:
						rel_path = p
						break
				else:
					rel_path = name or 'file.txt'

		try:
			saved_path = FileAnalyzer.fn.save_file_safe(base_folder, rel_path, content)
			_.pr(f'✅ Saved {saved_path}', c='green')
		except Exception as e:
			_.pr(f'❌ Failed to save: {rel_path} — {e}', c='red')

	if skipped:
		_.pr('\n🔍 Skipped possible section headers (not treated as files):', h='goldenrod')
		for idx, sname, sscore in skipped:
			_.pr(f'⏭️ {idx}\t{sname} (score={sscore})', h='light_gray')

	return

import os






########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)