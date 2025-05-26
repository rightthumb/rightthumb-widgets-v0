#!/usr/bin/python3

default = 'default'
default = 'storage'

import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Input', '-f,-i,-input' )
	_.switches.register( 'JS-Namespace', '-js', '_.cookies.' )
	_.switches.register( 'PHP-Namespace', '-php', '$myClass->' )
	_.switches.register( 'Project', '-p,-project', 'storage' )
	_.switches.register( 'Edit-Project-Customizations', '-edit', 'storage' )
	
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'php-js.py',
	'description': 'CryptoJS to PHP and vice versa',
	'categories': [
						'javascript',
						'js',
						'php',
						'converter',
						'conversion',
						'code',
						'programming',
						'fullstack',
				],
	'examples': [
						_.hp('p php-js --pa | cp'),
						_.hp('p php-js -i "md5($one).$two.md5($three);" | cp'),
						_.hp('p php-js -i "CryptoJS.MD5(_.$subject$.one).toString()+_.$subject$.two+CryptoJS.MD5(_.$subject$.three).toString();" | cp'),
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
_.l.conf('clean-pipe',False); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

def tailSpin(data,o,tail):
	index = {
		'CryptoJS.MD5': '.toString()',
	}
	for k in tail: index[k] = tail[k]
	for dex in index:
		i=o
		dex = dex[::-1]
		valid = True
		broke = False
		for s in dex:
			if broke: continue
			i -= 1
			try:
				if not data[i] == s:
					valid = False
			except:
				broke = True
		if valid: return index[dex[::-1]]
	return False

def process(data,tailPass={}):
	_code.imp.validator.register( data, 'javascript' )
	_code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False )
	found = []
	for o,c in enumerate(data):
		if c == '(' and o in _code.imp.validator.identity['location']['open']:
			tail = tailSpin(data,o,tailPass)
			if tail:
				c=_code.imp.validator.identity['location']['open'][o]
				snip = _code.imp.validator.assetSnipet( o, c )
				found.append({'snip': snip, 'add': tail})
	found.reverse()
	for f in found:
		data = data.replace(f['snip'],f['snip']+f['add'])
	return data

def phpKeysClean(data,o):
	index = {
		'$_REQUEST',
		'$_SERVER',
		'$_COOKIE',
		'$_FILES',
		'$_ENV',
		'$_POST',
	}
	for dex in index:
		i=o-1
		dex = dex[::-1]
		valid = True
		broke = False
		for s in dex:
			if broke: continue
			i -= 1
			try:
				if not data[i] == s:
					valid = False
				else:
					snippet = _code.imp.validator.assetSnipet( i, o-1 )
					if snippet in index:
						valid = True
						broke = True
						first = i
						last = _code.imp.validator.identity['location']['open'][o]
			except:
				broke = True
		if valid:
			if o+1 in _code.imp.validator.identity['location']['open']:
				oo = o+1
				cc = _code.imp.validator.identity['location']['open'][oo]
				snip = _code.imp.validator.assetSnipet( first, last )
				return snip
			else:
				return False
	return False

def processPhpKeys(data,php):
	# print('processPhpKeys')
	_code.imp.validator.register( data, 'javascript' )

	
	# original
	_code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False )
	
	# used for testing found in script-helper
	# _code.imp.validator.createIndex( data, 'javascript',  skipLoad=True, simple=False, B=True  )
	
	
	
	_code.imp.validator.identity['location']['open']
	found = []
	for o,c in enumerate(data):
		if c == '[' and o in _code.imp.validator.identity['location']['open']:
			needsFix = phpKeysClean(data,o)
			c=_code.imp.validator.identity['location']['open'][o]
			snip = _code.imp.validator.assetSnipet( o+2, c-2 )
			# print(snip)
			if needsFix:
				found.append({'snip': snip, 'add': needsFix})
	found.reverse()
	for f in found:
		data = data.replace(f['add'],php+f['snip'])
	return data

def action():
	global default
	if _.switches.isActive('Edit-Project-Customizations'):
		if _.switches.isActive('Project') and len(_.switches.values('Project')) == 1:
			editor(_.switches.values('Project')[0])
		elif len(_.switches.values('Edit-Project-Customizations')) == 1:
			editor(_.switches.values('Edit-Project-Customizations')[0])
		else:
			editor(default)
	data = "CryptoJS.MD5(sub.session+sub.device+sub.session).toString()+sub.device+sub.session+sub.lS.getItem('pepper')+CryptoJS.MD5(sub.lS.getItem('pepper')).toString();"
	data = "md5($session.$device.$session).$device.$session.$pepper.md5($pepper);"
	if _.switches.isActive('JS-Namespace'):
		js = _.switches.value('JS-Namespace')
	else:
		js = '_.$subject$.'
	if _.switches.isActive('PHP-Namespace'):
		php = _.switches.value('PHP-Namespace')
	else:
		php = '$'
	if _.switches.isActive('Project'):
		project = _.switches.value('Project')
	else:
		project = default
	if _.switches.isActive('Input'):
		data = ' '.join(_.switches.values('Input')).strip()
	else:
		data = '\n'.join(_.isData()).rstrip().replace('\r','')
	special = _.getTable('php-js_'+project+'.index')
	if not 'js' in special:
		special['js'] = {'tail': {}, 'replace': {}}
		special['php'] = {'tail': {}, 'replace': {}}
	tail = ''
	if '+' in data or 'CryptoJS.' in data or js in data:
		data = data.replace('+','.')
		for sp in special['php']['replace']:
			if sp in data:
				data = data.replace(sp,special['php']['replace'][sp].replace('{}',js))
		data = data.replace('sub.','$').replace('CryptoJS.MD5','md5').replace('.toString()','').replace(js, php)
		data = process(data,special['php']['tail'])
	else:
		data = processPhpKeys(data,php)
		data = data.replace('.','+')
		for sp in special['js']['replace']:
			if sp in data:
				data = data.replace(sp,special['js']['replace'][sp].replace('{}',php))
		data = data.replace(php,js).replace('md5','CryptoJS.MD5')
		data = process(data,special['js']['tail'])
		first = js.split('.')[0]+'.'
	data = data.replace('++','+').replace('..','.').replace('++','+').replace('..','.')
	_.pr(data)

def editor(project):
	os = __.imp('os.path.getsize')
	file = 'php-js_' + project + '.index'
	path = _v.tt + os.sep + file
	if not os.path.isfile(path) or os.path.getsize(path) == 0:
		_.saveTable( {'js':{'tail': {}, 'replace': {}}, 'php':{'tail': {}, 'replace': {}}}, file )
	_file_open = _.regImp( __.appReg, 'file-open' )
	_file_open.switch('App',_v.meta['code_editor'])
	if _.isWin:
		_file_open.switch('Files',path)
		_file_open.action()
	else:
		_file_open.switch('Files',path)
		_file_open.action()
	_.pr(_v.meta['code_editor'],path)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);