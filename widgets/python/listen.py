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
	pass
	#b)--> examples
	_.switches.register( 'Requests', '-r' )
	_.switches.register( 'Print', '-print' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

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


def _listener_():
	global hk
	# hkr.do("beepy.note('d',3,'dotted_eigth')") # (:g e:) c,    c#, d, d#, e, f, f#, g, g#, a, a#
	# sys.exit()
	hk.beepy.note('d',3,'dotted_eigth')
	r = sr.Recognizer()
	with sr.Microphone() as source:
		if _.switches.isActive('Print'):
			print("Talk")
		# audio = r.listen(source,timeout=1)
		audio = r.listen(source)
	try:
		# beepy.note('f')
		_translate_(r.recognize_google(audio))
		# hk.beepy.note('d')
		# beepy.note('a')

	except Exception as e:
		print(e)
		pass
		if _.switches.isActive('Print'):
			print('translate failure')
		hk.beepy.note('d',4,'dotted_eigth')

def _translate_(speech):
	global hk
	speech=speech.lower()

	finagled=False
	for finagle in _.v.finagling['_replace']:
		if not finagled and finagle in speech: speech=speech.replace(finagle,_.v.finagling['_replace'][finagle]); finagled=True;
	for finagle in _.v.finagling['_startswith']:
		if not finagled and speech.startswith(finagle): speech=speech=_.v.finagling['_startswith'][finagle]; finagled=True;

	# os.system('say '+speech)
	if _.switches.isActive('Print'):
		print('said:',speech)
	_.v.prompt=speech
	subject=None
	def check(tst): return tst if not subject and len(tst.split(' ')) == sum(1 for y in tst.split(' ') if ' ' + y + ' ' in ' ' + speech + ' ') else None
	def checkAll(dic):
		subject=None
		for sub in dic:
			if not subject:
				if check(sub):
					if _.switches.isActive('Print'):
						print(0,dic[sub])
					subject = sub
					if not sub in _.v.local:
						hkr.do(dic[sub])
					else:
						exec(dic[sub])
					if _.switches.isActive('Print'):
						print(1,dic[sub])
			# if subject: print(dic[sub])
		return subject

	global dic


	subject = checkAll(dic)
	if subject:
		# hkr.do("beepy.note('d',3,'dotted_eigth')")
		run='say '+subject
		if _.switches.isActive('Print'):
			print(run)
		# os.system(run)
		hk.beepy.note('d',3,'whole')
	else:
		print('no subject')
		hk.beepy.note('d',2,'half')
		# hkr.do("beepy.note('d',2,'dotted_eigth')")
		# print('no subject')

# sub='explode'
# elif check(sub):
#     subject=sub
#     Clip.explode()

# sub='implode'
# if check(sub):
#     subject=sub
#     Clip.implode()




		
	# print(speech)




def action():
	if _.switches.isActive('Requests'):
		global dic
		table=[]
		for k in dic:
			rec={ 'request': k, 'action': dic[k] }
			if _.showLine(str(rec)):
				table.append(rec)
		_.pt(table)
	else:
		_listener_()


# print(1)
# hkr.do('_test_()')
# print(2)
# sys.exit()
# import hotkeys as hk


def ai():
	max_tokens=1024
	if _.switches.isActive('Print'): print('ai: initialization')
	global interact
	# Sally paste  convert the folling python to a single line
	prompt = _.v.prompt.replace('sally','')
	if 'unlimited tokens' in _.v.prompt:
		_.v.prompt.replace('max tokens','')
		max_tokens=int(max_tokens*2)
	if 'paste' in prompt:
		prompt=prompt.replace('paste','')
		_paste = _.regImp( __.appReg, '-paste' )
		lines=[]
		lines.append(prompt.strip()+': ')
		for line in _paste.imp.paste().replace('\r','').split('\n'):
			if 'python' in prompt.lower(): line=line.split('#')[0]
			if 'javascript' in prompt.lower(): line=line.split('//')[0]
			line=line.replace('    ','\t').rstrip()
			if line: lines.append(line)
		prompt = '\n'.join(lines)
	import openai

	if _.switches.isActive('Print'):
		print('_________________')
		print(prompt)
		print('_________________')
	# Apply the API key
	openai.api_key = _blowfish.decrypt('+WDUtsrHiXMJ2Rk2Z7QMSyoo+xzLW/BhSw/kTcUwPmZGQBDpZs7LcGpy2hm+rAWQ+ZtzKKLFVO8=', _vault.key() )

	# Define your prompt
	# prompt = "Write a short story about a person who finds a treasure."

	# Request a response from the API
	response = openai.Completion.create(
		# https://platform.openai.com/docs/models/codex
		# engine="code-davinci-002",
		# engine="text-davinci-002",
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=max_tokens,
		n=1,
		stop=None,
		temperature=0.5,
	)

	# Print the response

	interact['listen'].append({'epoch': time.time(), 'prompt': prompt, 'response': response["choices"][0]["text"]})
	_.saveTable(interact,'ai-bot-interaction.index',p=0)
	if _.switches.isActive('Print'):
		print(response["choices"][0]["text"])
	_copy = _.regImp( __.appReg, '-copy' )
	_copy.imp.copy( response["choices"][0]["text"] )




##################################################
# https://nitratine.net/blog/post/simulate-mouse-events-in-python/

# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _code.imp.validator.register( 'data', 'javascript' )
# _code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False, B=True )
# c = _code.imp.validator.identity['location']['open'][o]


# _.pv(selectors)
# sys.exit()

def cp():
	global keyboard
	with keyboard.pressed(Key.ctrl): vVv='c'; keyboard.press(vVv); keyboard.release(vVv);
def pa():
	global keyboard
	with keyboard.pressed(Key.ctrl): vVv='v'; keyboard.press(vVv); keyboard.release(vVv);

def aquire_snippets():
	print('aquire_snippets')
	global keyboard
	global ti
	snippets=[]
	i=0
	while not i==3:
		i+=1
		time.sleep(ti['min'])
		cp()
		time.sleep(ti['min'])
		snippets.append( _paste.imp.paste() )
		time.sleep(ti['min'])
		keyboard.press(Key.up)
		time.sleep(ti['tiny'])
		keyboard.release(Key.up)
		time.sleep(ti['min'])
	return snippets


# def probable_selectors(snippets):

#     _code.imp.validator.register( 'data', 'javascript' )

#     selectors=[]
#     for snip in snippets:
#         snip=snip.replace('\r','')
#         lines=snip.split('\n')
#         _code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False, B=True )
#         c = _code.imp.validator.identity['location']['open'][o]

def snippet_to_selector(snippets):
	print('snippet_to_selector')
	payload=[]
	profiles = {
					'tag':     {
							'definitive': [
											'pre',
											'code',
											'h3',
							],
							'common': [
											'div',
											'td',
							],
							'parent': [
							],
							'children': [
											'a',
							],
							'omit': [
											'span',
											'tbody',
											'thead',
							],
					},
					# 'attributes':     {},
	}
	proDex={}
	omit=[]
	yTag=[]
	# profiles['tag']['definitive']
	for sec in profiles['tag']:
		for tag in profiles['tag'][sec]:
			if sec == 'omit':
				omit.append(tag)
			else:
				proDex[tag]=sec
				if sec == 'children' or sec == 'parent':
					yTag.append(tag)


	_.pv(proDex)
	# sys.exit()


	results=[]
	for snip in snippets:
		code=snip.replace('\r','').split('\n')[0]
		simpin = {
					' ': 'bc05cdf4',
					'\\"': 'fa9509d9',
		}
		# code='<td class="titleColumn another yet" test="a a\\"s s\\"ds f" yy="abc 123 def 456">'
		sel={}
		selectors={}
		selectors['tag']='err'
		selectors['classes']=''
		selectors['attributes']={}
		selectors['selectors']=[]
		if not '"' in code: selectors['tag']=code.split(' ')[0][1:]  
		elif '"' in code:
			code=code.replace('\\"',simpin['\\"'])
			parts=code.split('"')
			key=''
			isNext=False
			for i,x in enumerate(parts):
				if not i:
					_.pr(x,c='green')
					y=x.split(' ')[0]
					selectors['tag']=y[1:]
					_.pr(y,c='purple')
				if x.endswith('='):
					isNext=True
					# print(i,'=',x)
					if ' ' in x: key=x.split(' ')[1]
					else: key=x
					key=key.replace('=','')
				elif isNext:
					sel[key]=x.replace(simpin['\\"'],'\\"')
					isNext=False
					# print(i,'Y',x)
				# else: print(i,'N',x)
			# _.pv(sel)
			if 'class' in sel:
				_classes=[]
				for cl in sel['class'].split(' '): _classes.append('.'+cl)
				selectors['classes']=' '.join(_classes)

			
			selectors['attributes']=sel
			selectors['selectors'].append(selectors['tag']+' '+selectors['classes'])
			tcl=selectors['tag']+' '+selectors['classes'].split(' ')[0]
			if not tcl in selectors['selectors']: selectors['selectors'].append(tcl)
			for cl in selectors['classes'].split(' '): selectors['selectors'].append(cl)
			results.append(selectors)
	# _.saveTable2(results,'listen_snippet_to_selector.json')
	# _.pv(results)
	refined=[]
	for rec in results:
		refined.append(rec)
		if rec['tag'] in proDex and proDex[rec['tag']] == 'parent':
			break
		if rec['classes']: break
	refined.reverse()
	for rec in refined:
		if rec['tag'] in profiles['tag']['definitive']: return rec['tag']
		tag=rec['tag']
		classy=rec['classes']
		_sel_=''
		started=True
		if not tag in omit:
			if tag in proDex: started=True
			if started:
				if tag in proDex:
					if tag in yTag:
						_sel_+=tag
					if classy:
						_sel_+=' '+classy

		if _sel_: payload.append(_sel_)
	_.pv(results)
	_.pv(yTag)
	print('snippet_to_selector')
	return '  '.join(payload)


	

def code_scanner():
	print('code_scanner')
	global keyboard
	global ti
	def _scan_(code,r=False):
		global keyboard
		_copy.imp.copy( code )
		with keyboard.pressed(Key.ctrl): vVv='`'; keyboard.press(vVv); keyboard.release(vVv);

		time.sleep(ti['abit1'])
		pa()
		time.sleep(ti['min'])
		keyboard.press(Key.enter); keyboard.release(Key.enter);

		clip=_paste.imp.paste()
		while clip==code:
			time.sleep(ti['min'])
			clip=_paste.imp.paste()

		return clip
	snippets=aquire_snippets()
	# result=_scan_('_skimmer_=123; copy(_skimmer_);')
	# _.pv(snippets)
	# _.saveTable2(snippets,'listen_snippets.json')
	# print('_skimmer_:',result)
	# _.pv(snippets)
	selector = snippet_to_selector(snippets)
	time.sleep(ti['min'])
	keyboard.press(Key.f12)
	keyboard.release(Key.f12)
	time.sleep(ti['abit2'])
	print('selector:',selector)
	if not selector:
		_.e('unable to copy','selector is empty')
	_copy.imp.copy( selector )
	time.sleep(ti['abit1'])
	hkr.do('Clip.browser_f12_tooljs_text()')



ti={
		'tiny': .05,
		'min': .2,
		'abit1': .3,
		'abit2': .6,
}





def auto_scrape():
	print('auto_scrape')
	global mouse
	global keyboard
	global ti
	# time.sleep(3)
	mouse.click(Button.right, 1)
	time.sleep(ti['min'])
	keyboard.press(Key.up)
	keyboard.release(Key.up)
	time.sleep(ti['min'])
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	time.sleep(ti['abit1'])
	code_scanner()
	lines=[]
	count={}
	for line in _paste.imp.paste().replace('\r','').split('\n'):
		line=line.strip()
		if line:
			if not line in count:
				count[line]=0
			count[line]+=1
	for line in lines:
		line=line.strip()
		if line:
			if not count[line] > 2:
				lines.append(line)
	_copy.imp.copy('\n'.join(lines))





# time.sleep(ti['min'])
# keyboard.press(Key.f12)
# keyboard.release(Key.f12)




# sys.exit()

##################################################
dic = {
			'sally': 'ai()',
			'auto scrape': 'auto_scrape()',

			'explode': 'Clip.explode()',
			'implode': 'Clip.implode()',
			'first': 'Clip.first()',
			'lower case': 'Clip.toLower()',
			'upper case': 'Clip.toUpper()',
			'randomize case': 'Clip.toRandomCase()',

			'scrape text': 'Clip.browser_f12_tooljs_text()',
			'extract text': 'Clip.browser_f12_tooljs_text()',

			'extract table': 'Clip.browser_f12_tooljs_table()',
			'scrape table': 'Clip.browser_f12_tooljs_table()',

			'scrape table no header': 'Clip.browser_f12_tooljs_table0()',
			'extract table no header': 'Clip.browser_f12_tooljs_table0()',

			'remove duplicate spaces': 'Clip.dup_space()',

			'convert': 'Clip.auto_yaml_json_converter()',
			# 'yaml to json': 'Clip.yaml2json()',
			# 'json to yaml': 'Clip.json2yaml()',

			'strip': 'Clip.strip1()',
			'clean up': 'Clip.strip2()',

			'space to underscore': 'Clip.space_2_underscore_text()',

			'reverse lines': 'Clip.reverse_lines()',

			'double space': 'Clip.space_double()',
			'single space': 'Clip.space_single()',

			'invert quotes': 'Clip.quote_inverter()',

			'dirty eval': 'Clip.dirty_eval()',

			'build app': 'Clip.SQL_to_crud()',

			'decrypt': 'Clip.decrypt_lines()',
			'encrypt lines': 'Clip.encrypt_lines()',
			'encrypt': 'Clip.encrypt_all()',

			'remove comments and spaces': 'Clip.remove_py_comments_spaces()',
			'remove comments': 'Clip.remove_py_comments()',
			
			'encode': 'Clip.base64_encode()',
			'decode': 'Clip.base64_decode()',

			'encrypt': 'Clip.encrypt_all()',
			'decrypt': 'Clip.decrypt_lines()',

			'math': 'Clip.math()',


}
_.v.local=['sally','auto scrape']

_.v.finagling={
	'_replace': {
		'cobalt': 'kobold',
		'auto script': 'auto scrape',
	},
	'_startswith': {
		'auto scr': 'auto scrape',
		'autoscr': 'auto scrape',
		'andcode': 'encode',
	},
}

##################################################

# sally paste  convert the folling python to a single line

##################################################
from pynput.mouse import Button, Controller
from pynput.keyboard import Key
from pynput.keyboard import Controller as mController
mouse = Controller()
keyboard = mController()

##################################################


try: import speech_recognition as sr
except: pass
import os
hkr = _.regImp( __.appReg, 'hotkeys' )
hk=hkr.imp

_paste = _.regImp( __.appReg, '-paste' )
_copy = _.regImp( __.appReg, '-copy' )
##################################################
import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
interact=_.getTable('ai-bot-interaction.index')
if not 'success' in interact: interact = {'success':[],'failure':[],'chat':[]}
if not 'listen' in interact: interact['listen']=[]
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

# https://www.imdb.com/chart/top/

