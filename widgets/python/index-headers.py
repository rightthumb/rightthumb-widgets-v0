import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Concat', '-concat','This concatenates the extensions with the description', isData="name", isRequired=False )
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
import sys
def is_hex(value):
	try:
		int(value, 16)
		return True
	except ValueError:
		return False

def find_signature_key(data):
	for key, value in data.items():
		if isinstance(value, str):
			value = clean_string(value)
			hex_values = value.strip().split()
			if all(len(val) == 2 for val in hex_values) and 3 <= len(hex_values) <= 32 and all(is_hex(val) for val in hex_values):
				return key
	return None
import re

def clean_string(input_string):
	# Remove everything except alphanumeric characters and spaces
	cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
	# Remove duplicate spaces
	cleaned_string = re.sub(r'\s+', ' ', cleaned_string)
	# Strip leading and trailing spaces
	cleaned_string = cleaned_string.strip()
	return cleaned_string

def action():
	head = _.getTableDB('hex_headers.json')
	dex = {}
	for rec in head:
		subject = 'default'
		if not rec['extension'].strip() and rec['description'].strip():
			subject = rec['description'].strip()
		elif rec['extension'].strip() and rec['description'].strip():
			if _.switches.isActive('Concat'):
				subject = rec['extension'].strip() + ' - ' + rec['description'].strip()
			else:
				subject = rec['extension'].strip()
		if subject not in dex: dex[subject] = []
		# dex[subject].append(rec['signature'])
		xyz = find_signature_key(rec)
		if not xyz: continue
		dex[subject].append(rec[xyz])
	_.pv(dex)
	_.saveTableDB(dex,'index-headers--IS.dex',printThis=True)
x = {
	"extension": "EXE",
	"signature": "4D 5A 90 00 03 00 00 00",
	"description": "C# Compiled Windows",
	"src": "SoftwareDevelopmentSolutions"
}
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);