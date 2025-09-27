import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'SearchFields', '-f,-field,-fields', 'p a d c = path alias date count(greater than)' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'file-open-aliases.py',
	'description': 'View file open aliases',
	'categories': [
						'file-open',
						'file',
						'aliases',
				],
	'examples': [
						_.hp('p file-open-aliases -s count -s d.a + 86AB'),
						_.hp('p file-open-aliases -s count + indexTable_logs'),
						_.hp('p file-open-aliases -s count + sds.sh tmp'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
		{ 'name': 'file', 'abbreviation': 'f', 'sort': '' },
		{ 'name': 'epoch', 'abbreviation': 'e', 'sort': '' },
		{ 'name': 'date', 'abbreviation': 'd', 'sort': 'epoch' },
		{ 'name': 'aliases', 'abbreviation': 'a', 'sort': '' },
		{ 'name': 'count', 'abbreviation': 'c', 'sort': '' },
	],
	'aliases': [],
	'notes': [],
}
# ['file', 'epoch', 'date', 'aliases', 'count']

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
	global aliases

	# for k in aliases:
		# print(k)
	table = []
	for fi in aliases['files']:
		try:
			mod = _.mod(fi)
			rec = {'file': fi, 'epoch': mod, 'date': _.friendlyDate(mod).split(' ')[0], 'aliases': ' '.join(aliases['files'][fi]), 'count': len(aliases['files'][fi])}
			shouldAdd = True

			
			if not _.switches.isActive('SearchFields'):
				if shouldAdd: shouldAdd = _.showLine(str(fi))
			else:
				if 'p' in _.switches.value('SearchFields') and shouldAdd: shouldAdd = _.showLine(rec['file'])
				if 'a' in _.switches.value('SearchFields') and shouldAdd: shouldAdd = _.showLine(rec['aliases'])
				if 'd' in _.switches.value('SearchFields') and shouldAdd: shouldAdd = _.showLine(rec['date'])
				if 'c' in _.switches.value('SearchFields') and shouldAdd and rec['count'] > int(_.switches.value('SearchFields')): shouldAdd = True

			if shouldAdd:
				table.append(rec)
		except: pass
		# print(list(table[0].keys())); _.isExit(__file__)
		# print(fi)
	_.switches.fieldSet('Long','active',True)
	table = _.sort(table,'epoch.a')
	_.pt(table,'date,file,aliases,count')
	# _.pt(table,'file,aliases')

aliases=_.getTable('file-open-aliases.hash')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);