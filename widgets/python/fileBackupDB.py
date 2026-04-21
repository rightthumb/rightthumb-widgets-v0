import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	# _.switches.register( 'Ago', '-ago', '2d' )
	# _.switches.register( 'AltSwitchManager', '-@', '''?help | -and one two -and three four -omit five six ''' )
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start
import os; os.system('cls')
_db = _.regImp( __.appReg, '_rightThumb._fileBackup_MongoDB' )

# Switches = {
#     'File': '-f,-fi,-file',
#     'Ago': '-ago',
#     'Has': '-and',
#     'Or': '-or',
#     'Omit': '-omit',
# }
Switches =_.y("File: -f,-fi,-file || Ago: -ago || Has: -and,-or || Omit: -omit || Help: ?h,?help")



Help = {'Ago': 'a 5w 2w'}
Triggers = { 'File': _.resolve, 'Ago': _._ago, }

xyz = '--------------------'
Switches[xyz]=xyz
Help[xyz]=xyz
sw = __.SwitchManager(Switches,Triggers,Help)


def test():
	global sw
	db = _db.imp.db
	has = None
	omit = None

	if sw.isActive('Has'):
		has = sw.Instances('Has','-and')

	if sw.isActive('Omit'):
		omit = sw.values('Omit')

	if sw.isActive('Or'):
		if has:
			has.append(sw.values('Or'))
		else:
			has = sw.values('Or')
	_.pv(has)
	query = db.toQuery('file',has,omit)
	
	if sw.isActive('Ago'):
		ago = sw.values('Ago')
		if isinstance(ago, (list, tuple)) and len(ago) == 2:
			query['timestamp'] = {'$gte': ago[0], '$lte': ago[1]}
		else:
			query['timestamp'] = {'$gte': ago}


	if sw.isActive('File'):
		for f in sw.values('File'):
			query['file'] = f
	print(query)
	# _.pv(query)
	if len(input(': ')): return
	test = db.find('fileBackup',query)
	cnt=0
	for i,t in enumerate(test):
		cnt+=1
		# if not i: _.pv(t)
		print(  _.friendlyDate(t['timestamp']), t['file']  )
		# return
	print(cnt)





test()



def action():
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)