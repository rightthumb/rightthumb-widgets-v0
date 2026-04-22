import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Action', '-a,-action', 'c r u d' )
	_.switches.register( 'Data', '-d,-data', '"name:Sarah Connor|test:1"', isData='raw' )
	_.switches.register( 'Get', '-g,-get', '"name:Sarah Connor|test:1"' )
	
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


def dict_to_get(params, doseq=True, prefix='?'):
	"""
	Convert dict to GET query string.

	Args:
		params (dict): input dictionary
		doseq (bool): handle lists like ?a=1&a=2
		prefix (str): usually '?' or '' if appending

	Returns:
		str
	"""
	params = _.y(params)

	from urllib.parse import urlencode

	if not isinstance(params, dict):
		raise TypeError("params must be a dict")

	if not params:
		return ''

	query = urlencode(params, doseq=doseq)

	return f"{prefix}{query}"


def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Data', _.y )
	_.switches.trigger( 'Get', dict_to_get )
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start
#!/usr/bin/env python3

"""
Simple Python client for the PHP Mongo API.

Set your API URL here:
"""
API_URL = _v.fig['cliDB']
# print(API_URL); import sys; sys.exit()


# pip install requests

import json
import requests # type: ignore


class SimpleMongoApiClient:
	def __init__(self, url):
		self.url = url

	def _post(self, payload):
		response = requests.post(
			self.url,
			headers={"Content-Type": "application/json"},
			data=json.dumps(payload)
		)

		try:
			return {
				"status_code": response.status_code,
				"data": response.json(),
				"text": response.text
			}
		except Exception:
			return {
				"status_code": response.status_code,
				"data": None,
				"text": response.text
			}

	def create(self, record):
		return self._post({
			"app": {
				"action": "create"
			},
			"criteria": {},
			"record": record
		})

	def read(self, criteria):
		return self._post({
			"app": {
				"action": "read"
			},
			"criteria": criteria,
			"record": {}
		})

	def search(self, criteria):
		return self._post({
			"app": {
				"action": "search"
			},
			"criteria": criteria,
			"record": {}
		})

	def update(self, criteria, record):
		return self._post({
			"app": {
				"action": "update"
			},
			"criteria": criteria,
			"record": record
		})

	def delete(self, criteria):
		return self._post({
			"app": {
				"action": "delete"
			},
			"criteria": criteria,
			"record": {}
		})


def pretty(title, obj):
	print("\n" + "=" * 80)
	print(title)
	print("=" * 80)
	print(json.dumps(obj, indent=4, sort_keys=True))


def test():
	api = SimpleMongoApiClient(API_URL)

	# ------------------------------------------------------------
	# CREATE
	# ------------------------------------------------------------
	result_create = api.create({
		"name": "Sarah Connor",
		"phone": "5553211234",
		"city": "West Park",
		"tags": ["tech", "field"],
		"active": True
	})
	pretty("CREATE", result_create)

	inserted_id = None
	try:
		inserted_id = result_create["data"]["data"]["_id"]
	except Exception:
		pass

	# ------------------------------------------------------------
	# READ BY ID
	# ------------------------------------------------------------
	if inserted_id:
		result_read_id = api.read({
			"_id": inserted_id
		})
		pretty("READ BY ID", result_read_id)

	# ------------------------------------------------------------
	# READ BY EXACT FIELD
	# ------------------------------------------------------------
	result_read_exact = api.read({
		"exact": {
			"phone": "5553211234"
		}
	})
	pretty("READ BY EXACT FIELD", result_read_exact)

	# ------------------------------------------------------------
	# SEARCH EXACT
	# ------------------------------------------------------------
	result_search_exact = api.search({
		"exact": {
			"active": True
		},
		"limit": 10,
		"sort": {
			"name": 1
		}
	})
	pretty("SEARCH EXACT", result_search_exact)

	# ------------------------------------------------------------
	# SEARCH CONTAINS
	# ------------------------------------------------------------
	result_search_contains = api.search({
		"contains": {
			"name": "sarah"
		},
		"limit": 20,
		"sort": {
			"createdAt": -1
		}
	})
	pretty("SEARCH CONTAINS", result_search_contains)

	# ------------------------------------------------------------
	# SEARCH STARTS WITH
	# ------------------------------------------------------------
	result_search_starts = api.search({
		"startsWith": {
			"city": "we"
		}
	})
	pretty("SEARCH STARTS WITH", result_search_starts)

	# ------------------------------------------------------------
	# SEARCH ENDS WITH
	# ------------------------------------------------------------
	result_search_ends = api.search({
		"endsWith": {
			"phone": "1234"
		}
	})
	pretty("SEARCH ENDS WITH", result_search_ends)

	# ------------------------------------------------------------
	# SEARCH IN
	# ------------------------------------------------------------
	result_search_in = api.search({
		"in": {
			"city": ["West Park", "Hollywood", "Davie"]
		}
	})
	pretty("SEARCH IN", result_search_in)

	# ------------------------------------------------------------
	# UPDATE
	# ------------------------------------------------------------
	if inserted_id:
		result_update = api.update(
			{
				"_id": inserted_id
			},
			{
				"status": "updated",
				"phone": "5551234567"
			}
		)
		pretty("UPDATE", result_update)

	# ------------------------------------------------------------
	# DELETE
	# ------------------------------------------------------------
	if inserted_id:
		result_delete = api.delete({
			"_id": inserted_id
		})
		pretty("DELETE", result_delete)





def to_struct(data):
	"""
	Convert messy string/dict/list input into a proper dict/list.

	Handles:
		- Proper JSON
		- Single-quoted pseudo JSON
		- Python literals
		- Wrapped strings like '"{...}"'
		- Lists/dicts in string form
	"""

	import json
	import ast

	# -------------------------
	# already good
	# -------------------------
	if isinstance(data, (dict, list)):
		return data

	if not isinstance(data, str):
		return data

	s = data.strip()

	# -------------------------
	# unwrap quotes recursively
	# -------------------------
	while (
		(s.startswith('"') and s.endswith('"')) or
		(s.startswith("'") and s.endswith("'"))
	):
		s = s[1:-1].strip()

	# -------------------------
	# try strict JSON first
	# -------------------------
	try:
		return json.loads(s)
	except Exception:
		pass

	# -------------------------
	# try python literal (SAFE)
	# handles single quotes, etc
	# -------------------------
	try:
		return ast.literal_eval(s)
	except Exception:
		pass

	# -------------------------
	# last attempt:
	# fix common bad JSON patterns
	# -------------------------
	try:
		s_fixed = s.replace("'", '"')

		# True/False/None → JSON equivalents
		s_fixed = (
			s_fixed
			.replace("True", "true")
			.replace("False", "false")
			.replace("None", "null")
		)

		return json.loads(s_fixed)
	except Exception:
		pass

	# -------------------------
	# give up → return original
	# -------------------------
	return data



def normalizeData():
	data = _.isData(2)
	if type(data) == list and isinstance(data[0], dict) and len(data) == 1:
		data = data[0]
	if type(data) == list and isinstance(data[0], str):
		data = '\n'.join(data)
		if type(data) == str:
			data = to_struct(data)

	return data
def action():
	get = ''
	if _.switches.isActive('Get'):
		get = _.switches.value('Get')
		# print(get)
		# return
	# test()
	if not _.isData(2): _.e("data not found", '''-d "name:Sarah Connor|test:1"''', '''cat data.json | p cliDB    ||    echo "{'name': 'Sarah Connor', 'test': 1}" | p cliDB  ''')
	data = normalizeData()

	api = SimpleMongoApiClient(API_URL+get)
	import pprint
	pretty = pprint.pprint
	if _.switches.isActive('Action'):
		action = _.switches.value('Action')
		if action == 'c':
			result_create = api.create(data)
			pretty("CREATE", result_create)
		if action == 'r':
			result_read = api.read(data)
			pretty("READ", result_read)
		if action == 'u':
			result_update = api.update(data)
			pretty("UPDATE", result_update)
		if action == 'd':
			result_delete = api.delete(data)
			pretty("DELETE", result_delete)

	
	print(data)
	

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)