#!/usr/bin/env python3

import _rightThumb._construct as __
appDBA = __.clearFocus(__name__, __file__)
__.appReg = appDBA
import _rightThumb._base3 as _  # type: ignore
import os
def focus(parentApp='', childApp='', reg=True):
	global appDBA
	f = __.appName(appDBA, parentApp, childApp)
	return f if reg else f

fieldSet = _.l.vars(focus(), __name__, __file__, appDBA)
_.load()
_v = __.imp('_rightThumb._vars')


def sw():
	swGrp = 1
	_.switches.register('Config', '-config', 'config.yml', group=[swGrp,'Configuration'] )
	_.switches.register('URL', '-url', group=[swGrp,'Configuration'] )
	_.switches.register('APIKey', '-key,-api-key', group=[swGrp,'Configuration'] )

	swGrp += 1
	_.switches.register('DB', '-db,+db', group=[swGrp,'Mongo Target'] )
	_.switches.register('Collection', '+c,-collection', group=[swGrp,'Mongo Target'] )

	swGrp += 1
	_.switches.register('Create', '--c,-create', group=[swGrp,'CRUD Actions'] )
	_.switches.register('Read', '--r,-read', group=[swGrp,'CRUD Actions'] )
	_.switches.register('Search', '--s,-search', group=[swGrp,'CRUD Actions'] )
	_.switches.register('Update', '--u,-update', group=[swGrp,'CRUD Actions'] )
	_.switches.register('Delete', '--d,-del,-delete', group=[swGrp,'CRUD Actions'] )

	swGrp += 1
	_.switches.register('ID', '-id', group=[swGrp,'Record Selection'] )
	_.switches.register('Fields', '-f,-fields', group=[swGrp,'Record Selection'] )


def y(yaml,p=False):
	if os.path.isfile(yaml): yaml = open(yaml,'r').read()
	yaml = yaml.replace('\n','||')
	yaml = yaml.replace(',','||')
	yaml = yaml.replace('--','||')
	yaml = yaml.replace('::','||')
	while ': ' in yaml: yaml = yaml.replace(': ',':')
	yaml = yaml.replace(':',': ').replace(':  ',': ')
	while ' ||' in yaml:
		yaml = yaml.replace(' ||', '||')
	while '|| ' in yaml:
		yaml = yaml.replace('|| ', '||')
	yaml = yaml.replace('||','|')
	yaml = yaml.replace('|','\n')
	if p:
		print(yaml)
	return _.fromYML(yaml)


_._default_settings_()




_.appInfo[focus()] = {
	'file': 'mongo.py',
	'description': 'MongoDB API Client',
	'categories': ['mongo', 'mongoDB', 'db'],
	'examples': [
		_.hp('p mongo -create -fields "{\\"name\\":\\"Scott\\",\\"active\\":true}"'),
		_.hp('p mongo -search -fields "{\\"contains\\":{\\"name\\":\\"scott\\"},\\"limit\\":10}"'),
		_.hp('p mongo -read -id 67df1c2c9a1234567890abcd'),
		_.hp('p mongo -update -id 67df1c2c9a1234567890abcd -fields "{\\"status\\":\\"updated\\"}"'),
		_.hp('p mongo -delete -id 67df1c2c9a1234567890abcd'),
		_.linePrint(label='simple', p=0),
		'',
	],
	'columns': [],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp(__file__), _.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()

def appRegDics():
	return {
		'appInfo': _.appInfo[focus()],
		'appData': _.appData[focus()],
	}


def triggers():
	_._default_triggers_()
	_.switches.trigger('Files', _.isFileAdvanced, vs=False)
	# _.switches.trigger('DB', _.aliasesFi)
	_.switches.trigger('Fields', y)
	_.switches.trigger('Folder', _.myFolderLocations)
	_.switches.trigger('Folders', _.myFolderLocations)
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger('OutputFolder', _.aliasesFo)


def _local_(do):
	exec(do)


_.l.conf('clean-pipe', True)
_.l.sw.register(triggers, sw)

########################################################################################
#n)--> start


import json
import yaml
import requests


class MongoAPI:

	def __init__(self, config_file='config.yml'):
		self.cfg = {}

		if config_file and os.path.isfile(config_file):
			with open(config_file, 'r') as f:
				self.cfg = yaml.safe_load(f) or {}

		self.url = self.cfg.get('url', 'http://localhost/api.php')
		self.api_key = self.cfg.get('api_key', '')
		self.timeout = self.cfg.get('timeout', 30)

		if _.switches.isActive('URL'):
			self.url = _.switches.value('URL')

		if _.switches.isActive('APIKey'):
			self.api_key = _.switches.value('APIKey')

		self.headers = {
			'Content-Type': 'application/json',
		}

		if self.api_key:
			self.headers['X-API-Key'] = self.api_key

		if isinstance(self.cfg.get('headers'), dict):
			self.headers.update(self.cfg['headers'])

	def request(self, action='', criteria=None, record=None):
		criteria = criteria or {}
		record = record or {}
		db = 'term'
		collection = 'items'
		if _.switches.isActive('DB'):
			db = _.switches.value('DB')
		if _.switches.isActive('Collection'):
			collection = _.switches.value('Collection')
		payload = {
			'db': db,
			'collection': collection,
			'app': {
				'action': action
			},
			'criteria': criteria,
			'record': record
		}

		try:
			r = requests.post(
				self.url,
				headers=self.headers,
				json=payload,
				timeout=self.timeout
			)
		except Exception as e:
			return {
				'success': False,
				'error': str(e),
				'url': self.url
			}

		try:
			return r.json()
		except Exception:
			return {
				'success': False,
				'status_code': r.status_code,
				'text': r.text
			}

	def create(self, record):
		return self.request(action='create', record=record)

	def read(self, criteria):
		return self.request(action='read', criteria=criteria)

	def search(self, criteria):
		return self.request(action='search', criteria=criteria)

	def update(self, criteria, record):
		return self.request(action='update', criteria=criteria, record=record)

	def delete(self, criteria):
		return self.request(action='delete', criteria=criteria)


def get_fields():
	if _.switches.isActive('Fields'):
		fields = _.switches.value('Fields')
		if isinstance(fields, dict):
			return fields
		if isinstance(fields, str) and fields.strip():
			try:
				return json.loads(fields)
			except Exception:
				try:
					return yaml.safe_load(fields) or {}
				except Exception:
					return {}
	return {}


def get_id_criteria():
	if _.switches.isActive('ID'):
		return {
			'_id': _.switches.value('ID')
		}
	return {}


def get_action():
	if _.switches.isActive('Create'):
		return 'create'
	if _.switches.isActive('Read'):
		return 'read'
	if _.switches.isActive('Search'):
		return 'search'
	if _.switches.isActive('Update'):
		return 'update'
	if _.switches.isActive('Delete'):
		return 'delete'

	return 'search'

import os
import yaml # type: ignore

def action():
	config_file = '~/.rt/mongo.yml'
	config_file = os.path.expanduser(config_file)

	if _.switches.isActive('Config'):
		config_file = _.switches.value('Config')
	# print('config file:', config_file)
	if os.path.isfile(config_file):
		with open(config_file, 'r') as f:
			config = yaml.safe_load(f) or {}
		if config.get('url'):
			_.switches.value('URL', config['url'])
		if config.get('api_key'):
			_.switches.value('APIKey', config['api_key'])


	api = MongoAPI(config_file)

	act = get_action()
	fields = get_fields()
	id_criteria = get_id_criteria()

	if act == 'create':
		result = api.create(fields)

	elif act == 'read':
		criteria = fields or id_criteria
		result = api.read(criteria)

	elif act == 'search':
		criteria = fields
		result = api.search(criteria)

	elif act == 'update':
		criteria = id_criteria
		if not criteria:
			criteria = fields.get('criteria', {}) if isinstance(fields, dict) else {}

		record = fields.get('record', fields) if isinstance(fields, dict) else {}

		result = api.update(criteria, record)

	elif act == 'delete':
		criteria = fields or id_criteria
		result = api.delete(criteria)

	else:
		result = {
			'success': False,
			'error': 'Invalid action'
		}   

	print(json.dumps(result, indent=4, sort_keys=False))


########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)

_.isExit(__file__)


# p mongo -create -fields "name: scott || phone: 8136901260 || active: true"
