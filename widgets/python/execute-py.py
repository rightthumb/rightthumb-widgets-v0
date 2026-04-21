#!/usr/bin/python3
import sys, time
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Snippet', '-snip', '@ email strip-an prompt' )
	_.switches.register( 'Bookmark', '-bm', 'exec.l' )
	_.switches.register( 'Clean', '--c' )
_._default_settings_()

_.appInfo[focus()] = {
	'description': 'Execute python snippets',
	'categories': [ 'exec', 'execute', 'python', 'snip', 'snippets' ],
	'examples': [
						_.hp('exec'),
						_.hp('exec strip-an'),
						_.hp('pa | exec strip-an'),
						_.hp('p execute-py'),
						_.hp('p execute-py -snip strip-an'),
						_.hp('pa | p execute-py -snip strip-an'),
						'',
	]
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

def myData():
	text = _.myData()
	if type(text) == list:
		text = '\n'.join(text)
	return text

dic = {}
dic['prompt'] = '''
Assume the role of a programming specialist and ensure that all code with tabs or spaces is indented consistently using four spaces.
Be diligent in thoroughly reviewing and understanding all instructions, reading them a minimum of three times.
'''
dic['email'] = '''
text = myData()
import re
email_pattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,7}\\b'
matches = re.findall(email_pattern, text)
for match in matches:
	print(match)
'''
dic['@'] = dic['email']
dic['strip-an'] = '''
text = myData()
import re
pattern = r'\\w+'
stripped_text = re.sub(pattern, '', text)
print(stripped_text)
'''
dic['dump'] = '''
print(myData())
'''
dic['sep'] = '''
_copy = _.regImp( __.appReg, '-copy' )
text = '########################################################################################\\n#n)--> start'
_copy.imp.copy( text )
'''

def action():
	global dic
	_copy = _.regImp( __.appReg, '-copy' )
	_paste = _.regImp( __.appReg, '-paste' )
	if _.switches.isActive('Snippet'):
		if _.switches.value('Snippet') in dic:
			code = dic[_.switches.value('Snippet')]
		else:
			_.e('Snippet not found', 'Try:',list(dic.keys()))
			# _.e('Snippet not found', '\n\t\tTry:'+'\n\t\t    - '+'\n\t\t    - '.join(list(dic.keys())))
	else:
		code = _paste.imp.paste()

	if _.switches.isActive('Bookmark'):
		if _.switches.value('Bookmark'):
			bm = _v.bookmarkFormat.replace('ALIASHERE',_.switches.value('Bookmark'))
		else:
			bm = _v.bookmarkFormat.replace('ALIASHERE','exec.l')
		fo = _v.resolveFolderIDs(_.getText2(bm,'text').strip())
		os.chdir(fo)
	from contextlib import redirect_stdout
	from io import StringIO
	output_buffer = StringIO()
	with redirect_stdout(output_buffer):
		exec(code)
	captured_output = output_buffer.getvalue()
	if _.switches.isActive('Clean'):
		print(captured_output)
	else:
		try:
			_copy.imp.copy( captured_output )
		except:
			_.pr(captured_output)





########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);