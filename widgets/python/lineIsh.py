import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Threshold', '-t,-threshold', '3' )
	_.switches.register( 'Above', '-a,-above', '3' )
	_.switches.register( 'Below', '-b,-below', '3' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'Trim/Strip', '-trim,-strip', '' )
	_.switches.register( 'LineNumber', '-l,-ln,-n,-line,-number', '' )
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	above = 3
	below = 3
	if _.switches.isActive('Threshold'):
		above = int(_.switches.value('Threshold'))
		below = int(_.switches.value('Threshold'))
	if _.switches.isActive('Above'):
		above = int(_.switches.value('Above'))
	if _.switches.isActive('Below'):
		below = int(_.switches.value('Below'))
	found = []
	for i,line in enumerate( _.isData() ):
		if _.showLine(line):
			found.append( i )
	one = False
	two = False
	for k,j in enumerate(found):

		for i,line in enumerate( _.isData() ):
			pr = False
			if True:
				if i < j and i > j - above-1:
					one=True
					pr = True
				elif i > j and i < j + below+1:
					pr = True
				elif i == j:
					one=False
					two=False
					if _.showLine(line):
						for plusSearchX in _.switches.values('Plus'):
							plusSearchX = _.ci( plusSearchX )
							for subject in _.caseUnspecificCode( line, plusSearchX ):
								line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )
						pr = True
			if pr:
				if one == True and two == False:
					two = True
					_.pr(line=True,c='darkcyan')
					_.pr(k+1,c='yellow')
				if _.switches.isActive('Trim/Strip'):
					line = line.strip()
				if _.switches.isActive('LineNumber'):
					_.pr(i,line)
				else:
					_.pr(line)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);