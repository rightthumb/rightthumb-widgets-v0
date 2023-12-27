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
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################


def sw():
	_.switches.register( 'Template', '-t' )
	_.switches.register( 'Remove-Comments', '-cl,-nc,-no,-comment,-nocomment', 'js htm html' )
	pass
	#b)--> examples
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

_._default_settings_()
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
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

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
		# Count leading spaces
		leading_spaces = len(line) - len(line.lstrip(' '))
		# Replace each space with four spaces
		new_line = ' ' * 4 * leading_spaces + line.lstrip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)

def expand_spaces2(input_string):
	expanded_lines = []
	for line in input_string.split('\n'):
		# Count leading spaces
		leading_spaces = len(line) - len(line.lstrip(' '))
		# Replace each space with four spaces
		new_line = ' ' * 2 * leading_spaces + line.lstrip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)

def expand_spaces_to_tabs(input_string):
	expanded_lines = []
	for line in input_string.split('\n'):
		# Count leading spaces
		leading_spaces = len(line) - len(line.strip(' '))
		# Replace each space with a tab
		new_line = '\t' * leading_spaces + line.strip(' ')
		expanded_lines.append(new_line)
	return '\n'.join(expanded_lines)



def action():
	url = 'https://apps.eyeformeta.com/templates/html/'
	if not _.switches.isActive('Template'):
		url+='0.htm'
	elif _.switches.value('Template') == 't': url+='template.htm'
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
		if rc:
			if 'js' in rc:
				page = remove_js_comments(page)
			if 'ht' in rc:
				page = remove_html_comments(page)
		else:
			page = remove_html_comments(page)
	_.pr(page)

import requests

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
	action(); _.isExit(__file__);

