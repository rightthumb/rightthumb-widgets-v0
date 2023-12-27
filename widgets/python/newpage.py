import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Template', '-t', '"" js s t -h h 0 1 2 3 4' )
	_.switches.register( 'Remove-Comments', '-cl,-nc,-no,-comment,-nocomment', 'js htm html' )
	pass
_._default_settings_()

_.appInfo[focus()] = {
	'description': 'Website project templates',
	'categories': [ 'website',],
	'examples': [
						_.hp('p newpage'),
						_.hp('p newpage -t js -cl js'),
						_.linePrint(label='simple',p=0),
						_.hp('js: js.js'),
						_.hp('s:  template.htm'),
						_.hp('t:  template.htm'),
						_.hp('-h: headers.htm'),
						_.hp('h:  headers'),
						_.hp('0:  0.1.htm'),
						_.hp('1:  1.htm'),
						_.hp('2:  blank2.htm'),
						_.hp('3:  blank3.htm'),
						_.hp('4:  blank4.htm'),
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

def remove_html_comments(input_text):
	import re
	comment_pattern = r'<!--.*?-->'
	cleaned_text = re.sub(comment_pattern, '', input_text, flags=re.DOTALL)
	lines=[]
	for line in cleaned_text.split('\n'):
		if line.strip():
			lines.append(line)
	return '\n'.join(lines)

def remove_js_comments(input_text):
	lines=[]
	for line in input_text.split('\n'):
		if line.strip():
			if '//' in line and not '://' in line and not '"//' in line and not '-//' in line:
				line=line.split('//')[0]
			if line.strip():
				lines.append(line)
	return '\n'.join(lines)

def expand_spaces(input_string):
	expanded_lines = []
	for line in input_string.split('\n'):
		leading_spaces = len(line) - len(line.lstrip(' '))
		new_line = ' ' * 4 * leading_spaces + line.lstrip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)

def expand_spaces2(input_string):
	expanded_lines = []
	for line in input_string.split('\n'):
		leading_spaces = len(line) - len(line.lstrip(' '))
		new_line = ' ' * 2 * leading_spaces + line.lstrip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)

def expand_spaces_to_tabs(input_string):
	expanded_lines = []
	for line in input_string.split('\n'):
		leading_spaces = len(line) - len(line.strip(' '))
		new_line = '\t' * leading_spaces + line.strip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)

def action():
	url = 'https://apps.eyeformeta.com/templates/html/'
	if not _.switches.isActive('Template'):
		url+='0.htm'
	elif _.switches.value('Template') == 's': url+='template.htm'
	elif _.switches.value('Template') == 't': url+='template.htm'
	elif _.switches.value('Template') == '-h': url+='headers.htm'
	elif _.switches.value('Template') == 'headers': url+='headers'
	elif _.switches.value('Template') == 'head': url+='headers'
	elif _.switches.value('Template') == 'h': url+='headers'
	elif _.switches.value('Template') == '0': url+='0.1.htm'
	elif _.switches.value('Template') == '1': url+='1.htm'
	elif _.switches.value('Template') == '2': url+='blank2.htm'
	elif _.switches.value('Template') == '3': url+='blank3.htm'
	elif _.switches.value('Template') == '4': url+='blank4.htm'
	elif _.switches.value('Template') == 'js': url+='js.js'
	else: url+=_.switches.value('Template')
	page = requests.get(url).content.decode('utf-8')
	if _.switches.isActive('Remove-Comments'):
		rc=_.switches.value('Remove-Comments').strip()
		if _.switches.isActive('Template') and _.switches.value('Template') == 'js':
			page = remove_js_comments(page)
		else:
			if rc:
				if 'js' in rc:
					page = remove_js_comments(page)
				if 'ht' in rc:
					page = remove_html_comments(page)
			else:
				page = remove_html_comments(page)
	_.pr(page)
import requests

if __name__ == '__main__':
	action(); _.isExit(__file__);