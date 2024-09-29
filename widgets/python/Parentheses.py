import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'GreaterThanZero', '-0' )
	_.switches.register( 'Functions', '-fn,-func,-functions' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
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

def action():
	if _.switches.isActive('GreaterThanZero'):
		cnt = 0
	else:
		cnt = 1
	if _.switches.isActive('Functions'):
		spent = []
		for line in _.isData():
			fn = []
			if line.count('(') > cnt and _.showLine(line):
				pass
				rev = line[::-1]
				code = []
				start = False
				for c in rev:
					if start and not c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
					# if start and not c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						fn.append( ''.join( code[::-1] ) )
						start = False
						code = []
					elif c == '(':
						start = True
					elif start:
						code.append(c)
			if len(fn) > 0:
				result = ' '.join(fn)
				if not result in spent:
					spent.append(result)
					_.pr(result)


	else:
		for line in _.isData():
			if line.count('(') > 1:
				if _.showLine(line):
					for plusSearchX in _.switches.values('Plus'):
						plusSearchX = _.ci( plusSearchX )
						for subject in _.caseUnspecificCode( line, plusSearchX ):
							line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )
					_.pr(line)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);