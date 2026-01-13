import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'List', '-l,-list' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )
	_.switches.register( 'ID', '-id' )
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'Keys', '-k,-keys' )
	_.switches.register( 'Cleanup', '-cleanup' )
	_.switches.register( 'Search', '-search' )
	_.switches.register( 'Dumping', '-dmp' )
	_.switches.register( 'Plus-Line', '++' )
	_.switches.register( 'Minus-Line', '--' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'gpt-export.py',
	'description': 'Navigate chat gpt conversation export',
	'categories': [
						'gpt',
						'export',
						'conversations',
				],
	'examples': [
						_.hp('p gpt-export -f conversations.json'),
						_.hp('p gpt-export -f conversations.json -search + SaaS'),
						_.hp(' p gpt-export -f conversations.json -search + .profile .bashrc'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

'''
keys:
	title
	create_time
	update_time
	mapping
	moderation_results
	current_node
	plugin_ids
	conversation_id
	conversation_template_id
	gizmo_id
	is_archived
	safe_urls
	id
'''


def process(path):
	data = _.getTable2(path)
	# print(len(data))
	if _.switches.isActive('Keys'):
		for keys in data[0]: print(keys)
	elif _.switches.isActive('Cleanup'):
		_.saveTable2(data,path)
	elif _.switches.isActive('ID'):
		for rec in data:
			title = rec['title']
			id = rec['conversation_id']
			if not id in _.switches.values('ID'):
				continue
			_.pr(title,c='yellow')
			mapping = rec['mapping']
			for mID in mapping:
				try:
					if mapping[mID]['message']['author']['role'] and not mapping[mID]['message']['author']['role'] == 'system':
						_.pr()
						_.pr(line=1)
						_.pr(mapping[mID]['message']['author']['role']+':',c='green')

				except: pass
				try:
					if 'message' in mapping[mID] and 'content' in mapping[mID]['message'] and 'parts' in mapping[mID]['message']['content']:
						for line in mapping[mID]['message']['content']['parts']:
							_.pr(line,c='cyan')
				except: pass
	elif _.switches.isActive('Search'):
		spent=[]
		records = _.sort(data,'create_time')
		# records.reverse()
		for rec in records:
			include = False
			title = rec['title']
			id = 'https://chatgpt.com/c/'+rec['conversation_id']
			DT = rec['create_time']
			url = 'https://chatgpt.com/c/'+id
			if not _.switches.isActive('URL'): url = ''
			if _.showLine(title):
				if not id in spent:
					spent.append(id)
					titleColor = _.prWC2(title,_.switches.values('Plus'),'darkcyan','cyan')
					_.pr(_.pr(_.friendlyDate(DT).split(' ')[0],c='yellow',p=0),_.pr(id,c='cyan',p=0),url,titleColor)
					# _.pr(id,title,c='cyan')
				continue
			mapping = rec['mapping']
			# mapping.reverse()
			records=[]
			for mID in mapping:
				mapping[mID]['mID'] = mID
				records.append(mapping[mID])
				# print(type()); sys.exit();
			cnt = 0
			def minSize(ii):
				ii = str(ii)
				while len(ii) < 4:
					ii +=' '
				return ii

			Search = {}
			for s in _.switches.values('Plus'):
				Search[s] = 0
			for mID in mapping:
				try:
					if 'message' in mapping[mID] and 'content' in mapping[mID]['message'] and 'parts' in mapping[mID]['message']['content']:
						cnt += 1
						search = '\n'.join(mapping[mID]['message']['content']['parts'])
						for s in Search:
							if s.lower() in search.lower():
								Search[s] += 1

				except: pass
			valid = True
			for s in Search:
				if Search[s] == 0:
					valid = False
					break



			for mID in mapping:
				try:
					if 'message' in mapping[mID] and 'content' in mapping[mID]['message'] and 'parts' in mapping[mID]['message']['content']:
						search = '\n'.join(mapping[mID]['message']['content']['parts'])
						if _.showLine(search):
							if not id in spent:
								spent.append(id)
								
								_.pr('cnt:',minSize(cnt),'\t',_.friendlyDate(DT).split(' ')[0],id,url,title,c='green')
								# continue
								if _.switches.isActive('Plus-Line'):
									for line in mapping[mID]['message']['content']['parts']:

										if '\n' in line:
											lines = line.split('\n')
										else:
											lines = [line]
										for li in lines:
											if _.showLine(li,_.switches.values('Plus-Line'),_.switches.values('Minus-Line')):
												_.pr('\t',li,c='cyan')
											# if not id in spent:
												# spent.append(id)
												# _.pr(id,title)
									# continue

				except: pass
			if not id in spent and valid:
				spent.append(id)
				_.pr('cnt:',minSize(cnt),'\t',_.friendlyDate(DT).split(' ')[0],id,url,title,c='yellow')
	elif _.switches.isActive('Dumping'):
		for rec in data:
			title = rec['title']
			id = rec['conversation_id']
			mapping = rec['mapping']
			for mID in mapping:
				try:
					if 'message' in mapping[mID] and 'content' in mapping[mID]['message'] and 'parts' in mapping[mID]['message']['content']:
						for line in mapping[mID]['message']['content']['parts']:
							print(line)
				except: pass

def listChats(path):
	data = _.getTable2(path)
	records = _.sort(data,'create_time')
	# records.reverse()
	cnt = 0
	for rec in records:
		include = False
		title = rec['title']
		id = rec['conversation_id']
		if _.showLine(title):
			cnt += 1
			id = _.pr(id,c='purple',p=0)
			title = _.pr(title,c='yellow',p=0)
			_.pr(id,title)
	_.pr()
	if not cnt == len(records):
		_.pr('\t',_.addComma(cnt), 'of',_.addComma(len(records)),'chats',c='yellow')
	else:
		_.pr('\t',_.addComma(len(records)),'chats',c='yellow')
import sys

def action():
	if _.switches.isActive('List'):
		if not _.switches.isActive('Files'):
			listChats('conversations.json')
		for path in _.switches.values('Files'):
			listChats(path)
		return None

	if not _.switches.isActive('Files'):
		process('conversations.json')
		return None
	for path in _.switches.values('Files'):
		process(path)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);