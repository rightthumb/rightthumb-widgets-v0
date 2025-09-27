import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'SingleLine', '-single' )
	_.switches.register( 'All', '-all' )
	_.switches.register( 'Multiple-In-One-Line', '-m,-multi,-multiple' )
	_.switches.register( 'Functions', '-fn,-func,-functions' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'Parentheses.py',
	'description': 'Finds parentheses in a file',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p Parentheses -f ae.fn.java -fn'),
						_.hp('p Parentheses -f ae.fn.java + ('),
						_.hp('par  | p upper'),
						_.hp('par 0 | p upper'),
						_.hp('par 0'),
						_.hp('par '),
						_.hp('par app.py'),
						_.hp('cat ae.fn.java + GETCOLEQ GETCOL('),
						_.hp('cat ae.fn.java + GETCOLEQ GETITEM'),
						_.hp(''),
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

def action():
	if _.switches.isActive('Multiple-In-One-Line'):
		cnt = 1
	else:
		cnt = 0
	if _.switches.isActive('Functions'):
		spent = []

		####################################
		if True:
			function_pattern = r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\('  # Regular expression to match function names
			for line in _.isData():
				fn = []
				if line.count('(') > cnt and _.showLine(line):
					# Find all function matches in the line
					matches = re.findall(function_pattern, line)
					for match in matches:
						if match not in spent:
							fn.append(match)
							if _.switches.isActive('SingleLine'):
								_.pr(match)
								if not _.switches.isActive('All'):
									spent.append(match)
				if not _.switches.isActive('SingleLine'):
					res = ' '.join(fn)
					if res and res not in spent:
						_.pr(res)
						if not _.switches.isActive('All'):
							spent.append(res)
		####################################


		####################################
		if True:
			for line in _.isData():
				fn = []
				if line.count('(') > cnt and _.showLine(line):
					rev = line[::-1]
					code = []
					start = False
					for c in rev:
						if start and not c.isalnum() and c != '_':
							fn.append(''.join(code[::-1]))
							start = False
							code = []
						elif c == '(':
							start = True
						elif start:
							code.append(c)
				if len(fn) > 0:
					match = ' '.join(fn)
					for result in match.split(' '):  # Handle multiple functions in a line
						if result not in spent:
							if _.switches.isActive('SingleLine'):
								_.pr(result)
								if not _.switches.isActive('All'):
									spent.append(result)
							else:
								_.pr(result)
								if not _.switches.isActive('All'):
									spent.append(result)
		####################################


		####################################
		if True:
			for line in _.isData():
				fn = []
				if line.count('(') > cnt and _.showLine(line):
					# Split the line by '(' to isolate possible function calls
					parts = line.split('(')
					for part in parts:
						# Split by spaces to get tokens, and check if the last token before '(' is a valid function name
						tokens = part.split()
						if tokens:
							candidate = tokens[-1]
							# Ensure the candidate is a valid identifier (function name)
							if candidate.isidentifier():
								fn.append(candidate)
				
				# After collecting all functions in the line, process the results
				if len(fn) > 0:
					result = ' '.join(fn)
					# Split the result by spaces to handle multiple functions in a single line
					for function_name in result.split():
						if function_name not in spent:
							if _.switches.isActive('SingleLine'):
								# Print each function name on a new line
								_.pr(function_name)
								if not _.switches.isActive('All'):
									spent.append(function_name)
							else:
								# Print all function names on the same line
								_.pr(result)
								if not _.switches.isActive('All'):
									spent.append(result)
		####################################
















	else:
		for line in _.isData():
			if line.count('(') > 1 and _.showLine(line):
				for plusSearchX in _.switches.values('Plus'):
					plusSearchX = _.ci(plusSearchX)
					for subject in _.caseUnspecificCode(line, plusSearchX):
						line = line.replace(subject, _.colorThis(subject, 'green', p=0))
				_.pr(line)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);