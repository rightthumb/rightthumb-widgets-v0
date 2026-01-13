import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Digits', '-d,-digits' )
	_.switches.register( 'Count', '-n,-cnt,-numbers,-count' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'pins.py',
	'description': 'Pin generator',
	'categories': [
						'pin',
						'pins',
						'password',
						'passwords',
				],
	'examples': [
						_.hp('p pins'),
						_.hp('p pins -d 4'),
						_.hp('p pins -d 5'),
						_.hp('p pins -d 6'),
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


import random

def generate_random_number(digits=4):
	"""
	Generate a random multi-digit number with the specified number of digits.
	
	:param digits: Number of digits for the generated number (default is 4)
	:return: Random multi-digit number as an integer
	"""
	if digits < 1:
		raise ValueError("Number of digits must be at least 1.")
	
	# Ensure the first digit is not zero
	first_digit = random.randint(1, 9)
	remaining_digits = [random.randint(0, 9) for _ in range(digits - 1)]
	return int(str(first_digit) + ''.join(map(str, remaining_digits)))

def generate_multiple_numbers(count=10, digits=4):
	"""
	Generate a list of random multi-digit numbers.
	
	:param count: Number of random numbers to generate (default is 10)
	:param digits: Number of digits for each generated number (default is 4)
	:return: List of random multi-digit numbers
	"""
	return [generate_random_number(digits) for _ in range(count)]


def action():
	count = 10
	digits = 4
	if _.switches.isActive('Digits'):
		digits = int(_.switches.value('Digits'))
	if _.switches.isActive('Count'):
		count = int(_.switches.value('Count'))
	random_numbers = generate_multiple_numbers(count,digits)
	for pin in random_numbers:
		_.pr( pin )

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);