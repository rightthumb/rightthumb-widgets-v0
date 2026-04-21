import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register('Cheap', '-cheap')
	_.switches.register('Short', '-short')
	_.switches.register('Dump', '--d')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
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

import re

def is_tld_price_in_range(line):
	# parts = line.split(' ')
	# good = False
	# for p in parts:
	# 	if p.startswith('$'):
	# 		if len(p.split('.')[0]) == 2:
	# 			# print(p)
	# 			good =True
	# return good
	regex = r'^\S+\s+\$\d\.\d{2}'
	# regex = r'\$\d\.\d{2}'	
	return re.match(regex, line) is not None




def action():
	out=[]
	isTable=False
	for line in _.isData():
		line=line.strip()
		if line:
			line=line.replace('\t','    ')
			if '    ' in line: isTable = True
			if line.startswith('.'):
				if _.switches.isActive('Cheap'):
					if is_tld_price_in_range(line): out.append(line)
				elif _.switches.isActive('Short'):
					if len(line.split(' ')[0]) < 4: out.append(line)
				else:
					out.append(line)
	if _.switches.isActive('Dump'):
		isTable=False
	if not isTable:
		for line in out: print(line)
		return None
	table=[]
	for line in out:
		# print(type(line))
		rec={}
		for i,li in enumerate(line.split('    ')):
			if i == 0: key = 'domain'
			if i == 1: key = '1 yr'
			if i == 2: key = '2 yr'
			if i == 3: key = '3 yr'
			if i == 4: key = '4 yr'
			if i == 5: key = '5 yr'
			rec[key] = li
		table.append(rec)
	_.pt(table)
# https://www.domain.com/domains/new-domain-extensions
# https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);