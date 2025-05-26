import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Save', '-save','file.csv' )
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

def has_no_alpha(line):
    return not any(char.isalpha() for char in line)

def action():
	# _paste = _.regImp( __.appReg, '-paste' )
	# text = _paste.imp.paste().split('\n')
	text = _.getText( _.switches.value('Files'),clean=2, raw=True ).split('\n')
	records = []
	part = []
	spent = []
	for line in text:
		line = line.strip()
		parts=line.split(' ')
		person = None
		email = None
		phone = None
		part = []
		for p in parts:
			if '@' in p:
				person = ' '.join(part)
				# print(person)
				if email is None: email = []
				email.append(p.replace(',',''))
				part = []
			# elif has_no_alpha(p) and '-' in p:
			# 	if phone is None: phone = []
			# 	phone.append(p.replace(',',''))
			# 	part.append(p)
				
				# part = []
			else:
				part.append(p.replace(',',''))

		# if phone is not None:
		phone = ', '.join(part).replace(':,',':').replace(': ',':')
		if email is not None:
			email = ', '.join(email)
		if phone is None:
			phone = ''
		if email is None:
			email = ''
		if person is None:
			person = ''
		if person:
			phone = phone.strip()
			numbers = {
				'Mobile': '',
				'Home': '',
				'Work': '',
				'Emergency': '',
				'Alternate': '',
			}
			for ph in phone.split(','):
				ph = ph.strip()
				if not ':' in ph:
					numbers['Mobile'] = ph
				else:
					for k in numbers:
						if k in ph:
							numbers[k] = ph.split(':')[1]
			if ' ' in person:
				first = person.split(' ')[0]
				last = person.split(' ')[1]
			else:
				first = person
				last = ''
			if not email.lower() in spent:
				spent.append(email.lower())
				# records.append({'First':first,'Last':last,'Email':email})
				# records.append({'First':first,'Last':last,'Email':email,'Mobile Phone': numbers['Mobile'], 'Home Phone': numbers['Home'], 'Work Phone': numbers['Work'], 'Emergency Phone': numbers['Emergency'], 'Alternate Phone': numbers['Alternate']})
				records.append({'Name': person,'Email':email,'Mobile Phone': numbers['Mobile'], 'Home Phone': numbers['Home'], 'Work Phone': numbers['Work'], 'Emergency Phone': numbers['Emergency'], 'Alternate Phone': numbers['Alternate']})
	_.saveCSV(records,_.switches.value('Save'))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)