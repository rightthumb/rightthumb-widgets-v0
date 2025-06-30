import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	# _.switches.register( 'FormID', '-id', '1' )
	_.switches.register( 'Form', '-f,-form', 'login code' )
	_.switches.register( 'ShowFields', '-fld,-field,-fields' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'forms.py',
	'description': 'Terminal, tkinter, or html (temporary server) forms',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p forms -f login'),
						_.hp('p forms -f login -fld'),
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

# from _rightThumb._forms import genForm
from _rightThumb._forms._forms_example import example_forms1, example_forms2, checkboxes

showFields = _.switches.isActive('ShowFields')
if showFields:
	spent = []
	for rec in example_forms1:
		for k in rec:
			if not k == 'Config':
				for field in rec[k]:
					if not field['type'] in spent:
						spent.append(field['type'])
						print(field['type'])
	_.isExit(__file__)


import random

forms = {}
forms['login'] = {
	'Config': {
		# 'html': True,
		'terminal': True,
		'post': 'https://cli.sds.sh/forms/login/',
		# 'table': 'forms-test.json',
		# 'save': 'forms-test.json',
	},
	'Login': [
		{'label': 'Login', 'type': 'text', 'value': ''},
		{'label': 'Password', 'type': 'password', 'value': '', 'md5': True},
	],
}

forms['code'] = {
	'Config': {
		# 'html': True,
		# 'terminal': True,
		'post': 'https://cli.sds.sh/forms/',
		'table': 'Code_Snippet_Documentation',
		# 'save': 'forms-test.json',
	},
	'Code Snippet Documentation': [
		{'label': 'Subject', 'type': 'text', 'value': ''},
		{'label': 'Language', 'type': 'text', 'value': ''},
		{'label': 'Code', 'type': 'text_area', 'value': ''},
		{'label': 'Tags', 'type': 'text_area', 'value': ''},
	],
}

forms['paths'] = {
	'Config': {
		# 'html': True,
		'terminal': True,

		# 'post': 'https://cli.sds.sh/forms/',
		# 'table': 'Paths_Documentation',
		
		# 'print': True,
		'sqlite': 'Paths_Documentation',

		
		# 'save': 'forms-test.json',
	},
	'Paths': [
		{'label': 'PathType', 'type': 'radio', 'options': ['windows_folder', 'linux_folder', 'windows_file', 'linux_file', 'url', 'ftp','other'], 'value': ''},
		{'label': 'Path', 'type': 'text', 'value': ''},
		{'label': 'Note', 'type': 'text', 'value': ''},
	],
}
forms['advanced'] = {
    "Config": {
        "advanced": True,
        "description": "Complete Field Type Test",
        "field": { "width": 40 }
    },
    "Full Field Type Test Section": [
        { "label": "Username", "type": "text", "value": "test_user" },
        { "label": "Password", "type": "password", "value": "secret123" },
        { "label": "Bio", "type": "text_area", "value": "This is a short bio.\nSupports multiline input." },
        { "label": "User Role", "type": "radio", "options": ["Admin", "Editor", "Viewer"], "value": "Editor" },
        { "label": "Subscription Plan", "type": "dropdown", "options": ["Free", "Basic", "Pro", "Enterprise"], "value": "Pro" },
        { "label": "Notification Preferences", "type": "checkbox", "options": ["Email", "SMS", "Push"], "value": ["Email", "Push"] }
    ]
}

def action():
	global forms
	results = _.Form(forms[_.switches.value('Form')])
	
	if not _.switches.value('Form') == 'login':
		if type(results) == str:
			_.pr(results)
		else:
			_.pv(results)
	else:
		# _.pr('results:',results)
		
		__.secureModule = 'This is default data because: Access Denied: scott 123'
		if not results == 0 and not results == '0':
			exec(results)
			color = 'green'
		else:
			color = 'red'

		_.pr(__.secureModule,c=color)
	# _.pv(checkboxes)
	# results = _.Form(checkboxes)

	# cnt = len(example_forms)
	# # _.pr(cng)
	# form = random.choice(example_forms)
	# _.pv(form)
	# results = _.Form(form)
	# _.pv(results)
	
	# _.pv(checkboxes)
	# results = _.Form(checkboxes)
	# _.pv(results)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);