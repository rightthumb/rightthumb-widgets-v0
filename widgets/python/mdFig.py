import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Label', '-l,-label,-t,-title,-fld,-field', '##' )
	_.switches.register( 'Wrap', '-w,-wrap' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Key', '-key', 'dictKeyName' )
	_.switches.register( 'Advanced', '-a', '' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'mdFig.py',
	'description': 'Markdown Config File ### key ~~~ value',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p mdFig -f  mdFig_Test_File.md -label ##'),
						_.hp('p mdFig -f  mdFig_Test_File.md -label ## -key one'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

def action():
	wrap = _.switches.isActive('Wrap')
	if _.switches.isActive('Label'):
		label = _.switches.value('Label')
	else:
		label = '###'
	file = _.isData()[0]
	# try:
	contents = _.getText( file, raw=True )

	# import sys, os
	# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'code', 'classes')))
	# from MdFig import MdFig # type: ignore
	# mdFig = MdFig(contents)


	try:
		import sys, os
		sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'code', 'classes')))
		from mdFig import mdFig
		mdFig = MdFig(contents)
	except Exception as e:
		_.colorThis( [ 'Error: mdFig', e ], 'red' )
		from mdFig import MdFigParser
		mdFig = MdFigParser(contents)

	fig = mdFig.get_code()
		# fig = _.mdFig( '', label, wrap, file = file )
		# if _.switches.isActive('Advanced'):
		# 	fig = _.mdFig( '', label, wrap, file = file )
		# else:
		# 	fig = _.mdFigSimp( '', label, wrap, file = file )
	# except:
	# 	_.e('Error: mdFig','-f configFile.md')
	if _.switches.isActive('Key'):
		for key in _.switches.values('Key'):
			try:
				_.pr( fig[key] )
			except:
				_.e('Error: bad key or file',['remove -key from command','or','double check the file'])
	else:
		_.pv(fig)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);