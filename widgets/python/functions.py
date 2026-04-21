import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
import sys
def sw():
	# _.switches.register( 'JavaScript', '-js' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'functions.py',
	'description': 'index code files, js namespace',
	'categories': [
						'tool',
						'js',
						'namespace',
				],
	'examples': [
						_.hp('p functions -f script.js'),
						_.hp('p functions -f script.py'),
						_.hp(''),
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger('Files',_.myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


########################################################################################
# C:\Users\Scott\.rt\profile\daily\2025\02\01-11\functions.py.md
########################################################################################



import sys
import os


def action():
	file = _.switches.value('Files')
	_.pr()
	_.pr(file)
	_.pr()
	f, ext = os.path.splitext(file)
	ext = ext[1:]
	# print(ext); _.isExit(__file__)
	data = _.getText( file, raw=True ).replace('\r','')
	code = _.index( data, ext )
	code.fn()

	print(code.k())

	if ext == 'js':
		k = code.k()
		_.pr(k)

		# _.pv(code.db['fn'])
		for o in code.db['fn']:
			c = code.db['fn'][o]
			snip = code.code[o:c]
			_.pr(line=1)
			_.pr(snip)


	# _.pv(code.db['ns'])
	# for path in code.db['ns']:
	#     line = code.line(code.db['ns'][path])
	#     _.pr(line=1)
	#     _.pr(code.db['ns'][path],path)
	#     try:
	#          _.pr(code.snip(code.db['ns'][path], code.db['oc'][code.db['ns'][path]]))
	#     except:
	#         _.pr('err',path,c='red')


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);