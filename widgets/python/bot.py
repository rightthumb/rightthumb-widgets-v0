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
_keychain = _.regImp( __.appReg, 'keychain' )
##################################################


def sw():
	pass
	#b)--> examples
	_.switches.register( 'Convert', '-vert,-cv,-convert', 'py js or "# Python 3" "# JavaScript"' )
	_.switches.register( 'Requests', '-r', 'Get news from an rss feed' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files' )
	_.switches.register( 'Log', '-log', 'view log' )
	_.switches.register( 'Ago', '-ago', 'log by date' )

	#e)--> examples

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])
_requests_i=-1

def getSentenceCase(source: str):
	output = ""
	isFirstWord = True
	for c in source:
		if isFirstWord and not c.isspace():
			c = c.upper()
			isFirstWord = False
		elif not isFirstWord and c in ".!?":
			isFirstWord = True
		else:
			c = c.lower()
		output = output + c
	return output
_requests_bk=[]
scriptTrigger=True

def _requests(data):
	global scriptTrigger
	if not type(data) == str: return data
	if scriptTrigger: global _requests_bk; _requests_bk.append(data);
	if not data: return data
	while data.endswith(' '): data=data[:-1]
	while data.startswith(' '): data=data[1:]
	if not data: return data
	global _requests_i
	_requests_i+=1
	if not data[0] in '0123456789':
		data=str(_requests_i)+' '+data
	if not data[-1] in '.?!':
		data+='.'

	if not data == data.lower(): return data
	return getSentenceCase(data)

def _convert(data):
	if not type(data) == str: return data
	if not data: return data
	while data.endswith(' '): data=data[:-1]
	while data.startswith(' '): data=data[1:]
	if not data: return data
	if data[0] == '#': return getSentenceCase(data)

	if data in '.py py py3 .py3': return '# Python 3' 
	if data in '.py2 py2': return '# Python 2' 
	if data in '.js js javascript JavaScript': return '# JavaScript' 
	if data in 'c': return '# JavaScript' 

	return getSentenceCase(data)


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'bot.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'GPT-3 openai API interaction',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'GPT',
						'openai',
						'API',
						'GPT-3',
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
						_.hp('p bot -r '),
						_.linePrint(label='simple',p=0),
						'',
						'ai-bot-interaction.index',
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
	_.switches.trigger( 'Convert', _convert )
	_.switches.trigger( 'Requests', _requests )
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
scriptTrigger=False

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--#
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

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

# https://beta.openai.com/playground/p/default-text-to-command?model=text-davinci-002

import os
import openai

openai.api_key = _keychain.imp.key('open-ai-api')
prompt=''
def runSomeCode(prompt):
	response = openai.Completion.create(
		engine="text-davinci-003",
		# engine="text-davinci-002",
		# engine="code-davinci-002",
		# engine="text-babbage-001",
		# engine="text-curie-001",
		# engine="text-ada-001",
		prompt=prompt,
		temperature=0,
		# max_tokens=1500,
		max_tokens=1500,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0)
	if 'choices' in response:
		x = response['choices']

	if len(x) > 0:
		return x[0]['text']
	else:
		return ''

def snippet(text):

	text=text.replace('"""#','').replace('"""1','')
	text=text.replace('"""','')
	# text=text.replace('"','')
	text=clean(text)
	text=text.replace( chr(10),'')
	text=text.replace( chr(9),'')
	text=clean(text)
	if text.startswith('1 ') or text.startswith('2 ') or text.startswith('# '): text=text[2:]
	return text
	new=''
	for ch in text:
		if ch in _str.visibleChar+' ': new=ch
		else: new=' '
	new2=''
	for i,ch in enumerate(clean(new)):
		if i < 25:
			new2+=ch
	if new2 < new: new2+='...'
	return new2

def genPrompt():
	global prompt
	# if isData():
	#     prompt="\"\"\"\n"+ '\n'.join(_.switches.values('Requests')) +"\n"+ '\n'.join(isData()) +"\n\"\"\"",
	# else:
	if len(_.switches.all())==0 and _.isData():
		prompt="\"\"\"\n"+ '\n'.join(_.isData()) +"\n\"\"\""
		return prompt
	elif len(_.switches.all())==1 and _.isData() and _.switches.isActive('Files'):
		prompt="\"\"\"\n"+ '\n'.join(_.isData()) +"\n\"\"\""
		return prompt

	if _.switches.isActive('Convert'):
		prompt="\"\"\"\n\n"+  _.switches.values('Convert')[0]+'\n\n'+ ' '.join(_.isData()) +'\n\n'+'# Convert to '+_.switches.values('Convert')[1][1:]   +"\n\"\"\""
	elif not _.switches.isActive('Convert'):
		global _requests_bk
		if _requests_bk: _requests_bk.pop(0)
		_ompt=''.join(_.switches.values('Requests'))
		if _requests_bk:
			last_r=False
			_a=True
			for argv in sys.argv:
				if last_r:
					if not ' ' in argv: _a=False; last_r=False; break;
				if argv == '-r': last_r=True
			if not _a: _ompt='# '+' '.join(_requests_bk)
		prompt="\"\"\"\n"+ _ompt +"\n\"\"\""
	_.pr(prompt,c='yellow')
	_.pr(line=1,c='red')
	return prompt
def action():
	# print(_.isData())
	# sys.exit()
	global prompt
	interact=_.getTable('ai-bot-interaction.index')


	if _.switches.isActive('Log') and not _.switches.isActive('Ago'):


		logs=[]
		for status in interact:
			for i,rec in enumerate(interact[status]):
				if _.showLine(str(rec)+status):
					rec['status']=status
					rec['date']=_.isDate(rec['epoch'],f='sdate')
					rec['i']=i
					rec['prompt']=rec['prompt'][5:]
					rec['prompt']=snippet(rec['prompt'])
					rec['answer']=snippet(rec['answer'])


					rec['epoch']=int(rec['epoch'])

					# for k in rec: print(k)
					# sys.exit()

					rec2={}
					for k in 'status, epoch, date, prompt, answer, i'.split(', '): rec2[k]=rec[k]
					logs.append(rec2)

		# for rec in logs:
		#     if 1660871568 == rec['epoch']:
		#         for ch in rec['answer']:
		#             print(ch,ord(ch))
		# sys.exit()

		logs = _.tables.returnSorted( 'data', 'epoch', logs )
		_.pt(logs)
		_.pr()
		_.pr('',_.addComma(len(logs)))
		_.pr()
		_.pr()
		ask=input(' epoch/id: ')
		if ask:
			for rec in logs:
				color='grey'
				if rec['status']=='success': color='green'
				if rec['status']=='failure': color='red'
				if rec['status']=='chat': color='Color.bold'

				hasAlpha=False
				for ch in ask:
					if ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': hasAlpha=True


				

				if ask in str(rec['epoch']):
					orec=interact[rec['status']][rec['i']]
					_.clear()
					_.pr(line=1,c='yellow')
					_.pr(' Prompt',c='yellow')
					_.pr()
					_.pr(orec['prompt'],c='cyan')
					_.pr()

					_.pr(line=1,c=color)
					_.pr(' Answer',c=color)
					_.pr('\t',orec['status'],c=color)
					_.pr()
					_.pr(orec['answer'],c=color)
					_.pr()


		return logs

	if not 'success' in interact: interact = {'success':[],'failure':[],'chat':[]}

	prompt=genPrompt()
	t_start=time.time()
	answer = runSomeCode(prompt)
	t_end=time.time()
	note = False


	_.pr(answer,c='green')
	# _.pr('answer',type(answer))
	_.pr()
	# _.pr('...')
	if _.isData():
		ask='l'
	elif not _.isData():
		prompt_=''
		_ask=True
		if any(x in prompt for x in 'what when how who why where which whose'.split(' ')): prompt_='question'
		if not prompt_:
			if any(x in prompt for x in 'create build'.split(' ')):
				prompt_='build'
				if answer.count('import ') > 10:
					ask='f'; _ask=False
				length=0
				for line in answer.split('\n'):
					line=line.replace('\t',' ')
					line=clean(line)
					if line:
						xF=len(line.split(' '))
						if xF > length: length=xF
				if length < 4:
					ask='f'
					_ask=False

		if not prompt_:
			ln=[]
			for line in prompt.split('\n'):
				line=line.replace('"','')
				line=clean(line)
				if line: ln.append(line)
			if len(ln)==1 and ln[0].endswith('?'): prompt_='question'
			# print(ln)

		if _ask:
			if False:
				pass
			elif prompt_=='build':
				ask=input(' success or ish/success or failure or chat or log ?? S i f c l :  ')
				if not ask: ask='s'
			elif prompt_=='question':
				ask=input(' success or failure or chat or log ?? s i f C l:  ')
				if not ask: ask='c'
			elif not prompt_:
				ask=input(' success or failure or chat or log ?? s i f c L :  ')
				if not ask: ask='l'
			ask=ask.lower()
			if ask == 'g': ask =='s'
			if ask == 'y': ask =='s'
			if ask == 'n': ask =='f'
			if len(ask) > 1 or ask=='i':
				if ask=='i': note = 'ish'
				else: note = ask
				ask ='s'
			else:
				note = False


			_.pr()
			_.pr()


	#n)--> __.startTime can be used to find the execution receipt

	rec = {
			'epoch': __.startTime,
			'start': t_start,
			'end': t_end,
			'duration': t_end-t_start,
			'prompt': prompt,
			'answer': answer,
		}
	if note: rec['note']=note

	if 's' in ask: interact['success'].append(rec)
	elif 'c' in ask: interact['chat'].append(rec)
	else: interact['failure'].append(rec)
	_.saveTable(interact,'ai-bot-interaction.index',p=0)


def clean(text):
	while '  ' in text: text=text.replace('  ',' ')
	while text.startswith(' '): text=text[1:]
	while text.endswith(' '): text=text[:-1]
	return text

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


# .._copy = _.regImp( __.appReg, '-copy' )
# _copy.imp.copy(  )

# import _rightThumb._dir as _dir
# _copy = _.regImp( __.appReg, '-copy' )
# _copy.imp.copy(  )



