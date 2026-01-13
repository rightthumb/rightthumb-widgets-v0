import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register('No-Comment', '-nc,-nocomment','html py php js')

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'nocomment.py',
	'description': 'Comment Stripper',
	'categories': [
						'code',
						'tool',
						'clean',
				],

	'examples': [
						_.hp('cat fi | p nocomment'),
						_.hp('p nocomment'),
						_.hp('p nocomment -file file.txt'),
	],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
#####################################################################
## Start

def NOTHING(text): return text

def remove_html_comments(string):
	import re
	pattern = re.compile(r'<!--.*?-->', re.DOTALL)
	return pattern.sub('', string)

def remove_python_comments(code):
	import re
	code = re.sub(r'#.*', '', code)
	code = re.sub(r'(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")', '', code, flags=re.DOTALL)
	return code

def remove_php_comments(code):
	import re
	code = re.sub(r'(//.*|#.*)', '', code)
	code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
	return code

def remove_javascript_comments(code):
	import re
	code = re.sub(r'//.*', '', code)
	code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
	return code


def nocomment(text):
	text=remove_php_comments(text)
	text=remove_html_comments(text)
	text=remove_python_comments(text)
	text=remove_javascript_comments(text)
	return text

_copy = _.regImp( __.appReg, '-copy' )

def action():
	load()
	text = '\n'.join(_.myData())
	text = nocomment(text)
	_copy.imp.copy( text )
	
def load():
	if _.switches.isActive('No-Comment'):
		if not 'html' in _.switches.value('No-Comment'): remove_html_comments=NOTHING
		if not 'py' in _.switches.value('No-Comment'): remove_python_comments=NOTHING
		if not 'php' in _.switches.value('No-Comment'): remove_php_comments=NOTHING
		if not 'js' in _.switches.value('No-Comment'): remove_javascript_comments=NOTHING
	else:
		remove_html_comments=NOTHING
		remove_python_comments=NOTHING
		remove_php_comments=NOTHING
		remove_javascript_comments=NOTHING
if __name__ == '__main__':
	action(); _.isExit(__file__);