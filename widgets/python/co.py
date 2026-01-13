import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Alias', '-a' )
	_.switches.register( 'Print', '-p' )
	_.switches.register( 'Save', '--s,-save' )
	_.switches.register( 'Make', '-m,-make' )
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
	_.switches.trigger( 'Alias', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	_.switches.trigger( 'Save', _.aliasesFi )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start



def action():
	if _.switches.isActive('Make'):
		make = _.switches.values('Make')
		items = []
		for i in make:
			# print(i)
			if i.startswith('('):
				i = i.replace('(','').replace(')','')
				i = _.aliasesFo(i)
			elif i.startswith('{'):
				i = i.replace('{','').replace('}','')
				# print(i)
				i = _.aliasesFi(i)
			items.append(i)
		
		_.pr( ' '.join(items) )
		return

	if _.switches.isActive('Alias'):
		alias = _.switches.value('Alias')
		if _.switches.isActive('Print'):
			_.pr(alias)
			return
		if _.switches.isActive('Save'):
			_.saveText(alias, _.switches.value('Save'),p=0)
			_.pr(alias)
			return
		_copy = _.regImp( __.appReg, '-copy' )
		_copy.imp.copy( alias )    

	# if not _.switches.isActive('Alias'):
	#     _.pr('No Alias switch')
	#     return None
	# Alias = _.switches.value('Alias')
	# aliases=_.getTable('file-open-aliases.hash')
	# if 'aliases' in aliases and Alias in aliases['aliases']:
	#     alias = aliases['aliases'][Alias]


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)