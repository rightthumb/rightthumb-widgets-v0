import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Reverse', '-r,-reverse' )
	_.switches.register( 'DirtyJsonLine', '-d' )
	_.switches.register( 'Join', '-j,-join' )
	_.switches.register( 'Original', '-og' )
	_.switches.register( 'Switch', '-sw,-switch' )
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

def action():
	if _.switches.isActive('Files'):
		data = _.getText( _.switches.value('Files') )
	else:
		data = _.isData(2)


	if _.switches.isActive('Original'):
		print(  '  '.join(data)  )
		return
	
	if _.switches.isActive('Switch'):
		print(  '"'+'" "'.join(data).strip().rstrip(',')+'"'  )
		return

	
	if _.switches.isActive('DirtyJsonLine'):
		import simplejson as json
		data = ''.join(data).strip().rstrip(',')
		dic = json.loads(f'{{data}}')
		
		

	if type(data) == str:
			data = data.split('\n')
	
	elif not _.switches.isActive('DirtyJsonLine'):
		if not _.switches.isActive('Reverse'):
			data = '\n'.join(data)

		
		elif _.switches.isActive('Reverse'):
			data = '\n'.join(data).replace('\\n','\n')
			

	if type(data) == str:
		data = data.replace('\\n','\n')
		data = data.replace('\\t','\t')
		data = data.replace('\\r','\r')
		data = data.replace('\r','')
		data = data.split('\n')

	by = '  '
	if _.switches.isActive('Join'):
		by = _.ci(_.switches.value('Join'))
		by = by.replace('\\n','\n')
		by = by.replace('\\t','\t')
		by = by.replace('\\r','\r')
		by = by.replace('\r','')



	data = by.join(data)
	_copy = _.regImp( __.appReg, '-copy' )
	_copy.imp.copy( data )
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)