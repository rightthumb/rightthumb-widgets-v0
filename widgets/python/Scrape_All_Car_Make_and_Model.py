import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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

import re
def extract_years(text):
    # Regular expression to match years (single year or range like 1982-1990)
    year_pattern = r"\b(19\d{2}|20\d{2})(?:-(19\d{2}|20\d{2}))?\b"

    # Find all matches
    matches = re.findall(year_pattern, text)

    # Flatten and filter out empty matches
    years = [year for match in matches for year in match if year]

    return years


def action():
	urls = _.dot()
	urls.year = 'https://detail.com/search/vehicles_new?class=automobile&subclass=&year=YEAR'
	urls.make = 'https://detail.com/search/vehicles_new?class=automobile&subclass=&year=YEAR&make=MAKE'

	# url = urls.year.replace('YEAR','2015')
	# data = _.URL2(url)
	# print(data)
	if _.switches.isActive('Files'):
		records = _.getTable2(_.switches.values('Files')[0])
		# _.pv(data[0])
		for rec in records:
			name = rec['name'].title()
			name = name.replace(' &Amp;','')
			name = name.replace(' Full Specs','')
			name = name.replace(' Photos, Engines','')
			years = extract_years(name)
			for year in years:
				pass
				name = name.replace(year,'')
			name = name.replace(' -','')
			name = name.replace('  ','')
			name = name.strip()
			# if 'Volvo 244 ' in name:
				# _.pr(years)
			_.pr(name)



########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)