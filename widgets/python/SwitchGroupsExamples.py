import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	swGrp = 0
	swGrp += 1
	# post label precedes with a zero
	_.switches.register( 'Files', '-f,-fi,-file,-files','(optional) file.txt', isPipe='glob', description='Files', group=[swGrp,'A Group',0,'Post Label Here'])
	_.switches.register( 'One', '-one', group=[swGrp,'A Group'] )
	_.switches.register( 'Two', '-two', group=[swGrp,'Same swGrp But Different Label'] )
	tabSubGroupDepth = 2
	_.switches.register( 'Three', '-three', group=[swGrp,'BB Group',tabSubGroupDepth] )
	swGrp += 1
	_.switches.register( 'Four', '-for', group=[swGrp,'B Group'] )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
	_.switches.register( 'Fo', '-fo,-folder,-folders' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'swGrpsExamples.py',
	'description': 'Switch Group Examples: Empty App That Opens Help Menu Only To Display nth Nested Grouped Switch',
	# 'description': ['one','two','three','four'],
	'categories': [
						'example',
						'grouped switches',
						'switch groups',
						'nested switches subgroups',
						'nth switch group depth',
				],
	'examples': [
						_.hp('p swGrpsExamples'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [ 'All Python Framework Apps' ],
	'prerequisite': [ 'A RightThumb Framework App' ],
	'required': [  ],
	'notes': [ 'Modify this to test nth nested switch groups' ],
}
__.isRequired_or_List = ['Curiosity of how to use switch groups']
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Fo', _.myFolder )
	# _.switches.trigger( 'Fo', _.aliasesFo )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	if _.switches.isActive('Fo'):
		# print('value',_.switches.value('Fo'))
		# print(_.switches.values('Fo'))
		# print(__.appReg)
		for path in _.switches.values('Fo'):
			_.pr( path )
		return None
	_.help(1)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);