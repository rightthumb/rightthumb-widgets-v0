import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Copy', '-cp' )
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
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start
import os

def numb(num):
	num = int(num)
	if num < 10:
		return '0'+str(num)
	else:
		return str(num)
def renameFile(db):
	db = __.path(db)
	fo = __.path(db,pop=True)+os.sep
	# fi = __.path(db,fi=True)
	fi = db.split(os.sep)[-1]
	# _.pr(db,c='green')
	# _.pr(fo,fi,c='darkcyan')
	if os.path.isfile(db):
		import shutil
		modified = _.friendlyDate( _.autoDate( _.mod(db) ) ).split(' ')[0].replace('-','.')
		# print(modified); sys.exit();
		to = fo+modified+'-'+fi
		sub = modified+'-'+fi
		i=1
		while os.path.isfile(to):
			i+=1
			sub = modified+'-'+numb(i)+'-'
			to = fo+sub+'-'+fi
		# _.pr(db,to,c='cyan')
		if _.switches.isActive('Copy'):
			shutil.copy(db,to)
		else:
			shutil.move(db,to)
		return sub
def action():
	# _.switches.fieldSet('Length','active',True)
	records = []
	for path in _.isData():
		path = path.strip()
		if not os.path.isfile(path): continue
		name = renameFile(path)
		records.append({ 'file': path, 'new': name })
	_.pt(records)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);