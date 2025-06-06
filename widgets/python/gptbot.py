import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Project', '-p,-pj,-proj,-prjct,-project', 'Create a calculator website' )
	_.switches.register( 'OS-Interaction', '-os', 'Save Files, Compile, Service Interaction, Blacklist, Whitelist' )
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



from  _rightThumb._gptbot import GPT4oBot

def action():
	if not _.isData() and not _.switches.isActive('Project'):
		_.e('No data provided. Please provide prompt')
	if _.switches.isActive('Project'):
		goal = ' '.join(_.switches.values('Project'))
	else:
		goal = '\n'.join(_.isData())
	bot = GPT4oBot(os_interaction=_.switches.isActive('OS-Interaction'))
	bot.init_goal(goal=goal )
	while True:
		task, result = bot.run_next_task()
		if not task:
			print(result)
			break
		print(f"\n✅ Completed: {task}\n{result}\n")

if __name__ == '__main__':
	action(); _.isExit(__file__)