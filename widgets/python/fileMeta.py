import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Meta', '-m,-meta','me ce md5 sha1', isRequired=False )
	_.switches.register( 'Individual', '-i', isRequired=False )
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

def action():
	for path in _.isData():
		path = __.path(path)
		file = __.path(path,fi=True)
		# fileMeta = __.path(path,fo=True)+os.sep+'.file.meta'
		fileMeta = '.file.meta'
		# print(path); sys.exit();
		individual = _.switches.isActive('Individual')
		if _.switches.isActive('Meta'):
			record = _.fileMeta(path,'me '+_.switches.value('Meta').replace(',',' ').strip(),individual)
		else:
			record = _.fileMeta(path,'',individual)
		if os.path.isfile(_v.myTables + os.sep + fileMeta):
			meta = _.getYML(fileMeta)
		else:
			meta = {}
		if type(record) == dict:
			if path in meta:
				for k in record:
					meta[path][k] = record[k]
			else:
				meta[path] = record
			_.saveYML(meta,fileMeta)
			# _.pr('record',c='yellow')
			_.pv(record)
			# _.pr()
			# _.pr('.file.meta',c='yellow')
			# _.pv(meta)
		else:
			_.pr(record,c='cyan')
			key = _.switches.value('Meta').strip()
			record = {key: record}
			if path in meta:
				for k in record:
					meta[path][k] = record[k]
			else:
				meta[path] = record
import sys, os
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);