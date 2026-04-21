#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
##################################################
import os
import sys
import time
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._encryptString as _blowfish
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )



##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Config', '-config')
	_.switches.register('Input', '-i,-f,-file','file.txt')
	# _.switches.register('Project', '-p,-project')



_.appInfo[focus()] = {
	'file': 'siteData.py',
	'description': 'Scrape data from front end or direct from console mult-threaded',
	'categories': [
						'tool',
						'online',
						'download',
						'threaded',
						'data',
						'payload',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['relatedapps'].append('p printTable -i siteData_answerFile_auto_labels.json  -long')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('n siteData_answerFile_auto.txt')
_.appInfo[focus()]['relatedapps'].append('n siteData_answerFile_auto_labels.json')
_.appInfo[focus()]['relatedapps'].append('n siteData_config_generate_database_of_andriod_apps_for_this_family_member.json')
_.appInfo[focus()]['relatedapps'].append('')



_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['examples'].append('p siteData -config')
_.appInfo[focus()]['examples'].append('')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()

	_.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )

_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
########################################################################################
# START


def ask_question( field, label, validateionRule=False ):

	global answerFile
	global answerFileLabels
	global answerBackup
	global answerBackupLabels
	_.pr()
	theEnd = ''
	if not type(validateionRule) == bool:
		if validateionRule == 'yn_y':
			theEnd += '(y)'
		if validateionRule == 'yn_n':
			theEnd += '(n)'
		if validateionRule == 'notBlankText':
			theEnd += '*'
		if validateionRule == 'selector':
			theEnd += '*'
	theEnd += ' '
	data = input( label+theEnd )


	shouldClean = True
	if type(validateionRule) == str:
		for x in [ 'password' ]:
			if x == validateionRule:
				shouldClean = False


	if shouldClean:
		# _.pr(data)
		data = _str.replaceDuplicate( data, ' ' )
		data = _str.cleanBE( data, ' ' )


	# _.pr(data)
	result = data
	if not type(validateionRule) == bool:
		result = validateask_question( field, validateionRule, data )
	else:
		result = data
	if type(validateionRule) == bool:
		display = result
	else:
		if 'yn_' in validateionRule:
			if result:
				display = 'yes'
			else:
				display = 'no'
		else:
			display = result
	# _.pr(data)
	_.pr( display )
	answerFile.append( display )
	# answerFileLabels.append( display + ', ' + field + ', ' + label)

	answerFileLabels.append({ 'field': field, 'label': label, 'answer': display, 'validation_rule': textOrBlank(validateionRule) })
	_.saveText( answerFile, answerBackup )
	# _.saveText( answerFileLabels, answerBackupLabels )
	
	return result

def textOrBlank( data ):
	if not type( data ) == str:
		data = ''
	return data



def isDirect( data ):
	# _.pr( data )
	# sys.exit()
	if 'f' in data.lower():
		return False
	else:
		return True

def validateask_question( field, what, data ):


	if what == 'project_type':
		# _.pr( field, what, data )
		# sys.exit()
		if 'f' in data.lower():
			result = 'front_end'
		else:
			result = 'direct'

	elif what == 'selector_or_function':
		if 'f' in data.lower():
			result = 'function'
		else:
			result = 'selector'

	elif what == 'yn_n':
		result = False
		test = [ 't', 'y' ]
		for x in test:
			if x in data.lower():
				result = True

	elif what == 'yn_y':
		result = True
		test = [ 'n', 'f' ]
		for x in test:
			if x in data.lower():
				result = False

	elif what == 'yn_o':
		result = 'only'
		if 'o' in data.lower():
			result = 'only'
		else:
			for x in [ 'n', 'f' ]:
				if data.lower().startswith(x):
					result = 'no'
			for x in [ 'y', 't' ]:
				if data.lower().startswith(x):
					result = 'yes'

	elif what == 'url':
		if data.lower() == 'n':
			result = False
		elif data.lower() == 'f':
			result = False
		elif not 'http' in data.lower():
			_.pr( 'Error: bad url' )
			result = validateask_question( field, what, ask_question( field, 'url:' ) )
		else:
			result = data

	elif what == 'notBlankText':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			result = data

	elif what == 'textFalse':
		if 'false' in data.lower():
			result = False
		else:
			if not len(data):
				result = False
			else:
				result = data


	elif what == 'password':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			if data.endswith('='):
				result = data
			else:
				result = _blowfish.encrypt( data )

	elif what == 'selector':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			result = data

	elif what == 'this,item,all':
		if not len(data):
			result = 'all'
		else:
			if data.lower().startswith('a'):
				result = 'all'
			elif data.lower().startswith('i'):
				result = 'item'
			elif data.lower().startswith('t'):
				result = 'this'
			else:
				result = 'all'

	elif what == 'this,item,all-this':
		if not len(data):
			result = 'this'
		else:
			if data.lower().startswith('a'):
				result = 'all'
			elif data.lower().startswith('i'):
				result = 'item'
			elif data.lower().startswith('t'):
				result = 'this'
			else:
				result = 'this'


	elif what == 'single,list,auto':
		if not len(data):
			result = 'auto'
		else:
			if data.lower().startswith('a'):
				result = 'auto'
			elif data.lower().startswith('s'):
				result = 'single'
			elif data.lower().startswith('l'):
				result = 'list'
			else:
				result = 'auto'

	elif what == 'single,list,dic,list_dic,auto':
		if not len(data):
			result = 'auto'
		else:
			if 'l' in data.lower() and 'd' in data.lower():
				result = 'list_dic'
			elif data.lower().startswith('a'):
				result = 'auto'
			elif data.lower().startswith('s'):
				result = 'single'
			elif data.lower().startswith('l'):
				result = 'list'
			elif data.lower().startswith('d'):
				result = 'dic'
			else:
				result = 'auto'

	else:
		_.pr( 'Error: validateAsk' )
		sys.exit()

	return result

def field2Label( data ):
	data = data.replace( '_', ' ' )
	return str(field).title()+':'



def formatNameForFile( data ):
	data = _str.replaceDuplicate( data, ' ' )
	data = _str.cleanBE( data, ' ' )
	result = data.replace( ' ', '_' )
	result = _.printSafe( result )
	return result


def actionConfig():
	global config
	# config['isDirect']
	# config['testAsWeGo']
	# config['scrape_js']
	_.pr( '________________________________' )
	_.pr( '            action' )
	_.pr()
	thisAction = {}
	thisAction['description'] = ask_question( 'description', 'Description:' )
	thisAction['parentPassUrl'] = ask_question( 'parent_passed_url', 'Does the parent pass a url to process:', 'yn_n' )
	if not thisAction['parentPassUrl']:
		thisAction['url'] = ask_question( 'url', 'Payload url:', 'url' )
	thisAction['item'] = []
	addAnother=True
	while addAnother==True:
		thisAction['item'].append( actionConfigItem() )
		addAnother = ask_question( 'add_another', 'Add another action:item?', 'yn_y' )

	thisAction['child'] = False
	hasChild = ask_question( 'process_children_from_payload_urls', 'Process children from payload urls (children):', 'yn_n' )
	if hasChild:
		thisAction['child'] = actionConfig()
	return thisAction


def actionConfigItem():
	global config
	global payloadTriggerDefault
	global payloadValidatorDefault
	_.pr( '________________________________' )
	_.pr( '         action:item' )
	_.pr()
	thisAction = {}
	thisAction['description'] = ask_question( 'description', 'Description:' )
	if config['isDirect']:
		thisAction['type'] = 'selector'
	else:
		thisAction['type'] = ask_question( 'selector_or_function', 'Selector or Function:', 'selector_or_function' )
	thisAction['pause'] = ask_question( 'pause_between_tasks', 'Pause between tasks?', 'yn_n' )
	thisAction['collection'] = []
	addAnother=True

	if 'f' in thisAction['type']:
		while addAnother:
			thisAction['collection'].append( actionConfigItemFunction(  ) )
			addAnother = ask_question( 'add_another', 'Add another action:item:function?', 'yn_y' )

	else:

		while addAnother:
			thisAction['collection'].append( actionConfigItemSelector() )
			addAnother = ask_question( 'add_another', 'Add another action:item:function?', 'yn_y' )
		
	if not type( payloadTriggerDefault['trigger'] ) == bool:
		if not payloadTriggerDefault['instructions'] == 'all':
			payloadTriggerDefault = { 'instructions': False, 'trigger': False, 'validates': False }

	if not type( payloadValidatorDefault['validator'] ) == bool:
		if not payloadValidatorDefault['instructions'] == 'all':
			payloadValidatorDefault = { 'instructions': False, 'validator': False }
		

	return thisAction


def actionConfigItemSelector():
	global config
	global payloadTriggerDefault
	global payloadValidatorDefault
	_.pr( '________________________________' )
	_.pr( '         action:item:selector' )
	_.pr()
	thisAction = {}
	thisAction['payload_label'] = ask_question( 'payload_label', 'Payload Label:', 'notBlankText' )
	thisAction['selector'] = ask_question( 'selector', 'Selector:', 'selector' )
	thisAction['data_type'] = ask_question( 'data_type', 'Data type? single,list,auto (auto)', 'single,list,auto' )


	thisAction['trigger'] = False
	
	if not type( payloadTriggerDefault['trigger'] ) == bool:
		thisAction['trigger'] = payloadTriggerDefault['trigger']
		thisAction['trigger_validates'] = payloadTriggerDefault['validates']
	else:
		trigger = ask_question( 'payload_trigger', 'Payload field trigger:', 'textFalse' )
		if not type(trigger) == bool:
			try:
				thisAction['trigger'] = eval(trigger)
				if type( payloadTriggerDefault['trigger'] ) == bool:
					thisAction['trigger_validates'] = ask_question( 'does_trigger_also_validate', 'Does trigger behavior include validation? ', 'yn_n' )
					trigger_instructions = ask_question( 'trigger_instructions', 'Trigger for: this, item, all? (all)', 'this,item,all' )
					if not trigger_instructions == 'this':
						payloadTriggerDefault['trigger'] = thisAction['trigger']
						payloadTriggerDefault['instructions'] = trigger_instructions
						payloadTriggerDefault['validates'] = thisAction['trigger_validates']
			except Exception as e:
				_.pr( 'Error: unable to eval(trigger)' )
				_.pr( 'Result: trigger = False' )
				payloadTriggerDefault = { 'instructions': False, 'trigger': False, 'validates': False }


	thisAction['validator'] = False
	
	if not type( payloadValidatorDefault['validator'] ) == bool:
		thisAction['validator'] = payloadValidatorDefault['validator']
	else:
		addValidator = ask_question( 'add_validator', 'Add validator:', 'yn_n' )
		validator = False
		if addValidator:
			validator = ask_question( 'validation_trigger', 'Validation Trigger:', 'textFalse' )
		if not type(validator) == bool:
			try:
				thisAction['validator'] = eval(validator)
				if type( payloadValidatorDefault['validator'] ) == bool:
					validator_instructions = ask_question( 'validator_instructions', 'validator for: this, item, all? (this)', 'this,item,all-this' )
					if not validator_instructions == 'this':
						payloadValidatorDefault['validator'] = thisAction['validator']
						payloadValidatorDefault['instructions'] = validator_instructions
			except Exception as e:
				_.pr( 'Error: unable to eval(validator)' )
				_.pr( 'Result: validator = False' )
				payloadValidatorDefault = { 'instructions': False, 'validator': False }


	return thisAction


def actionConfigItemFunction():
	global config
	global payloadTriggerDefault
	global payloadValidatorDefault
	_.pr( '_______________________________________' )
	_.pr( '         action:item:function' )
	_.pr()
	thisAction = {}
	thisAction['function'] = ask_question( 'function', 'Function:', 'notBlankText' )
	thisAction['has_payload'] = ask_question( 'has_payload', 'Has Payload? y,n:', 'yn_n' )
	thisAction['payload_label'] = False
	if thisAction['has_payload']:
		thisAction['payload_label'] = ask_question( 'payload_label', 'Payload Label:', 'notBlankText' )
		thisAction['data_type'] = ask_question( 'data_type', 'Data type? single,list,dic,list_dic,auto (auto)', 'single,list,dic,list_dic,auto' )

	thisAction['trigger'] = False
	if thisAction['has_payload']:
		if not type( payloadTriggerDefault['trigger'] ) == bool:
			thisAction['trigger'] = payloadTriggerDefault['trigger']
			thisAction['trigger_validates'] = payloadTriggerDefault['validates']
		else:
			trigger = ask_question( 'payload_trigger', 'Payload field trigger:', 'textFalse' )
			if not type(trigger) == bool:
				try:
					thisAction['trigger'] = eval(trigger)
					if type( payloadTriggerDefault['trigger'] ) == bool:
						thisAction['trigger_validates'] = ask_question( 'does_trigger_also_validate', 'Does trigger behavior include validation? ', 'yn_n' )
						trigger_instructions = ask_question( 'trigger_instructions', 'Trigger for: this, item, all? (all)', 'this,item,all' )
						if not trigger_instructions == 'this':
							payloadTriggerDefault['trigger'] = thisAction['trigger']
							payloadTriggerDefault['instructions'] = trigger_instructions
							payloadTriggerDefault['validates'] = thisAction['trigger_validates']
				except Exception as e:
					_.pr( 'Error: unable to eval(trigger)' )
					_.pr( 'Result: trigger = False' )
					payloadTriggerDefault = { 'instructions': False, 'trigger': False, 'validates': False }


		thisAction['validator'] = False
		
		if not type( payloadValidatorDefault['validator'] ) == bool:
			thisAction['validator'] = payloadValidatorDefault['validator']
		else:
			addValidator = ask_question( 'add_validator', 'Add validator:', 'yn_n' )
			validator = False
			if addValidator:
				validator = ask_question( 'validation_trigger', 'Validation Trigger:', 'textFalse' )
			if not type(validator) == bool:
				try:
					thisAction['validator'] = eval(validator)
					if type( payloadValidatorDefault['validator'] ) == bool:
						validator_instructions = ask_question( 'validator_instructions', 'validator for: this, item, all? (all)', 'this,item,all-this' )
						if not validator_instructions == 'this':
							payloadValidatorDefault['validator'] = thisAction['validator']
							payloadValidatorDefault['instructions'] = validator_instructions
				except Exception as e:
					_.pr( 'Error: unable to eval(validator)' )
					_.pr( 'Result: validator = False' )
					payloadValidatorDefault = { 'instructions': False, 'validator': False }


	return thisAction



def action():
	global config
	global answerBackup
	global answerFileLabels
	if _.switches.isActive('Config'):
		_.pr( 'Answer backup to pickup where you left off if problem:', answerBackup )
		_.pr( '________________________________' )
		_.pr( '         project config' )
		_.pr()
		config['testAsWeGo'] = ask_question( 'testAsWeGo', 'Test page as we go?', 'yn_y' )
		config['name'] = ask_question( 'name', 'Project:' )
		config['description'] = ask_question( 'description', 'Description:' )
		config['id'] = _.genUUID( project=config['name'] )
		config['timestamp'] = _.appData[focus()]['start']
		config['type'] = ask_question( 'type', 'Type (direct or front end):', 'project_type' )
		config['isDirect'] = isDirect( config['type'] )
		config['scrape_js'] = False
		config['injectjQuery'] = False
		config['hasLogin'] = False

		config['login_url'] = ''
		config['login'] = ''
		config['password'] = ''
		config['login_selector'] = ''
		config['password_selector'] = ''
		config['login_button'] = ''
		config['password_button'] = ''

		if not config['isDirect']:
			config['injectjQuery'] = ask_question( 'injectjQuery', 'Inject jQuery?', 'yn_y' )
			hasInjection = ask_question( 'hasInjection', 'Inject javascript file?', 'yn_n' )
			if hasInjection:
				config['scrape_js'] = _v.myAppsJs + _v.slash+'siteData' + '_' + formatNameForFile( config['name'] ) + '.js'
				if not os.path.isfile(config['scrape_js']):
					do = 'echo. > ' + config['scrape_js']
					os.system('"' + do + '"')
				do = 'n ' + config['scrape_js']
				os.system('"' + do + '"')
			config['hasLogin'] = ask_question( 'hasLogin', 'Has Login?', 'yn_n' )
			if config['hasLogin']:
				config['login_url'] = ask_question( 'login_url', 'Login url:', 'url' )

				if config['testAsWeGo'] and not type(config['login_url']) == bool:
					# _.pr(config['login_url'])
					_browser.imp.project.open( config['login_url'] )

				config['hasBothLP'] = ask_question( 'hasBothLP', 'Is both login and password visible?', 'yn_y' )
				config['login'] = ask_question( 'login', 'Login:', 'notBlankText' )
				config['login_selector'] = ask_question( 'login_selector', 'Login Selector:', 'selector' )
				if not config['hasBothLP']:
					config['login_button'] = ask_question( 'login_button', 'Login Button Selector:' )

				config['password'] = ask_question( 'password', 'Password:', 'password' )
				config['password_selector'] = ask_question( 'password_selector', 'Password Selector:', 'selector' )

				if not config['hasBothLP']:
					config['password_button'] = ask_question( 'password_button', 'Password Button Selector:' )

				if config['testAsWeGo'] and not type(config['login_url']) == bool:
					url=config['login_url']
					login=config['login']
					password=config['password']
					login_selector=config['login_selector']
					password_selector=config['password_selector']
					login_button=config['login_button']
					password_button=config['password_button']

					_browser.imp.project.loginIndividually( url, login, password, login_selector, password_selector, login_button, password_button )
					

		config['action'] = []
		
		addAnother=True
		while addAnother==True:
			config['action'].append( actionConfig() )
			addAnother = ask_question( 'add_another', 'Add another action?', 'yn_n' )
		
		_.pr()
		_.pr()
		_.saveTable( config, 'siteData_config_' + formatNameForFile( config['name'] ) + '.json')
		_.pr()
		_.saveTable( answerFileLabels, 'siteData_answerFile_auto_labels.json' )
		_.pr()
		_.pr( answerBackup )
					
	else:



		theProject = False
		# _.pr( _v.myTables + _v.slash )
		dirList = os.listdir( _v.myTables + _v.slash )
		i = 0
		relevant = []
		for item in dirList:
			# _.pr( '\t',item )
			path = _v.myTables + _v.slash + item
			if os.path.isfile(path):
				if item.startswith( 'siteData_config_' ) and item.lower().endswith( '.json' ):
					# _.pr( item )
					label = item.replace( 'siteData_config_', '' ).replace( '.json', '' ).replace( '_', ' ' )
					relevant.append({ 'id': i, 'item': item, 'path': path, 'label': label })
					i+=1
		# _.pr( len(dirList) )
		# sys.exit()
		selected = []
		i = 0
		for data in relevant:
			if _.showLine(data['label']):
				data['id'] = i
				selected.append( data )
				i+=1
		##
		if len( selected ) == 1:
			theProject = selected[0]
		elif not len( selected ):
			_.pr()
			_.tables.register('data',relevant)
			_.tables.print('data','id,label')
			_.pr()
			ask = input( 'ID: ' )
			try:
				theProject = relevant[int(ask)]
			except Exception as e:
				_.pr( 'Error: expected int' )
				sys.exit()

		elif len( selected ) > 1:
			_.pr()
			_.tables.register('data',selected)
			_.tables.print('data','id,label')
			_.pr()
			ask = input( 'ID: ' )
			try:
				theProject = selected[int(ask)]
			except Exception as e:
				_.pr( 'Error: expected int' )
				sys.exit()
		##

		global payload


		if not type( theProject ) == bool:
			config = _.getTable( theProject['item'] )

			if config['type'] == 'front_end':
				if config['hasLogin']:
					if not config['hasBothLP']:
						_browser.imp.project.loginIndividually( config['login_url'], config['login'], config['password'], config['login_selector'], config['password_selector'], config['login_button'], config['password_button'] )
					else:
						_browser.imp.project.login( config['login_url'], config['login'], config['password'], config['login_selector'], config['password_selector'] )
				##
				for instructions in config['action']:
					takeAction( config, instructions )


		try:
			_browser.imp.project.close()
		except Exception as e:
			pass

		return payload


def takeAction( config, thisAction ):
	global payload
	data = {}
	if not thisAction['parentPassUrl']:
		try:
			_browser.imp.project.open(thisAction['url'])
		except Exception as e:
			_.pr( 'Error: action page did not load' )
			sys.exit()
	if config['injectjQuery']:
		_browser.imp.project.jqueryInject()
	if not type( config['scrape_js'] ) == bool:
		_browser.imp.project.inject( _.getText( config['scrape_js'] ) )

	for item in thisAction['item']:
		# payload_label
		fields = False
		lc = len( item['collection'] )
		for i,collection in enumerate(item['collection']):
			if item['type'] == 'function':
				if not collection['has_payload']:
					_browser.imp.project.inject( collection['function'] )
				else:
					if not collection['payload_label'] == bool:
						fields = True
						data[collection['payload_label']] = processTriggers( collection['trigger'], collection['trigger_validates'], collection['validator'], _browser.imp.project.injectReturn( collection['function'] ))
					else:
						payload.append( processTriggers( collection['trigger'], collection['trigger_validates'], collection['validator'], _browser.imp.project.injectReturn( collection['function'] )) )
				if item['pause']:
					_.pr(  )
					_.pr( 'Waiting for task completion' )
					ix = 0
					while not _browser.imp.project.injectReturn('return window.taskComplete;'):
						time.sleep( 1 )
						ix+=1
						_.pr( ix, end='\r', flush=True )
					_.pr(  )

			else:
				fields = True
				data[collection['payload_label']] = processTriggers( collection['trigger'], collection['trigger_validates'], collection['validator'], _browser.imp.project.injectReturn( collection['function']) )

		if fields:
			payload.append( data )
		
	if not type( thisAction['child'] ) == bool:
		_.pr()
		for i,link in enumerate(findLinks(payload)):
			_.pr( 'Processing:', i )
			try:
				_browser.imp.project.open( link )
				pageLoaded = True
			except Exception as e:
				_.pr( 'Error: cannot load', link )
				_.pr()
				pageLoaded = False

			if pageLoaded:
				try:
					takeAction( config, config['child'] )
				except Exception as e:
					_.pr( 'Error: action failure', link )
					_.pr()

	_.printVar( payload )


def processTriggers( trigger, triggerVal, validator, data ):
	return data

def findLinks( payload ):
	href = _browser.imp.project.injectReturn('return location.href;')
	
	

payloadTriggerDefault = { 'instructions': False, 'trigger': False, 'validates': False }
payloadValidatorDefault = { 'instructions': False, 'validator': False }
config = {}
answerFileLabels = []
answerFile = []
answerFile.append( 'c' )
answerFile.append( 'p siteData -config' )
answerBackup = _v.myTables + _v.slash+'siteData_answerFile_auto.txt'
answerBackupLabels = _v.myTables + _v.slash+'siteData_answerFile_auto_labels.txt'
payload = []

# _.pr( '                                                      ', 'siteData_config_generate_database_of_andriod_apps_for_this_family_member.json' )

# ******************************************************************************************************
## all validator functions should have fields labels in case you want a master by field name
# ******************************************************************************************************


########################################################################################
if __name__ == '__main__':
	action()






