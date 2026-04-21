import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Refined', '-r,-refined' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'above.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p above -file app.py + item_in_file'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=False )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def preceding(s: str) -> (str, int):
	modified_str = s
	modified_str = s.replace('    ', '\t')
	# modified_str = s.replace('\t', '    ')
	space_count = len(modified_str) - len(modified_str.lstrip(' ').lstrip('\t'))
	spaces = modified_str[:space_count]
	return spaces, space_count



def action():
	if _.switches.isActive('Files'):
		data = _.getText( _.switches.value('Files') )
	else:
		data = _.isData(r=1)
	results = []
	data.reverse()
	active = False
	spaces = 99999999
	spent = []
	for line in data:
		line = line.rstrip()
		# print(line)
		if _.showLine(line,c=True):
			# print(_.sl)
			active = True
			ws, spaces = preceding(line)
			results.append(_.sl)
		if active:
			if preceding(line)[1] < spaces:
				ws, spaces = preceding(line)
				results.append(line)
		
		# else: print(line)

			# print(spaces)
		# if spaces == 0 or ( len(line) == 1 and _.switches.value('Files').lower().endswith('.json') ):
			# print(len(line))
		if spaces == 0:
			break
	results.reverse()
	for line in results:
		print(line)
			
			

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)