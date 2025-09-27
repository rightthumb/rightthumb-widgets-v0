import xml.etree.ElementTree as ET
import colorama
from colorama import Fore, Style
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__)
__.appReg=appDBA
import _rightThumb._base3 as _
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register('Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False)
	_.switches.register('ID', '-id')
	_.switches.register('Credentials', '-cred,--credentials')
	_.switches.register('Notes', '-n,-notes')
	_.switches.register('Search', '-s,-search', isData='string', description='Search string')

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'KeePassXML.py',
	'description': 'KeePass XML Parser',
	'categories': ['DEFAULT'],
	'examples': [_.hp('p KeePassXML.py -f file.txt')],
	'columns': [],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp(__file__), _.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return {'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()]}

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe', True)
_.l.sw.register(triggers, sw)

########################################################################################

# Initialize colorama
colorama.init(autoreset=True)

def parse_keepass_xml(file_path):
	try:
		tree = ET.parse(file_path)
		return tree.getroot()
	except ET.ParseError as e:
		print(Fore.RED + f"Error parsing XML file: {e}" + Style.RESET_ALL)
		return None

def search_records(root, search_string):
	results = []
	for entry in root.findall(".//Entry"):
		for string in entry.findall(".//String"):
			key = string.find("Key").text
			value = string.find("Value").text
			if search_string.lower() in value.lower():
				results.append(entry)
				break
	return results

def view_record(entry):
	record = {}
	for string in entry.findall(".//String"):
		key = string.find("Key").text
		value = string.find("Value").text
		record[key] = value
	return record

def colorize_output(key, value):
	colors = {
		'Title': Fore.RED,
		'UserName': Fore.GREEN,
		'Password': Fore.YELLOW,
		'URL': Fore.CYAN,
		'Notes': Fore.MAGENTA
	}
	color = colors.get(key, Fore.WHITE)
	return f"{color}{key}: {value}{Style.RESET_ALL}"

def main():
	# Switch variables
	file_path = ''  # KeePass XML file path
	search_string = ''  # --search, -s
	record_id = None  # --record, -r
	view_credentials = False  # --cred
	view_notes = False  # --notes

	ID = None
	if _.switches.isActive('ID'):
		ID = _.switches.value('ID')

	file_path = _.switches.values('Files')[0] if _.switches.isActive('Files') else ''
	search_string = _.switches.value('Search') if _.switches.isActive('Search') else ''
	record_id = int(ID) if ID else None
	view_credentials = _.switches.isActive('Credentials')
	view_notes = _.switches.isActive('Notes')

	root = parse_keepass_xml(file_path)
	if root is None:
		return

	if search_string:
		results = search_records(root, search_string)
		for i, entry in enumerate(results):
			print(Fore.BLUE + f"ID: {i+1}" + Style.RESET_ALL)
			for string in entry.findall(".//String"):
				key = string.find("Key").text
				value = string.find("Value").text
				print(colorize_output(key, value))
			print()

	elif record_id is not None:
		entries = root.findall(".//Entry")
		if 0 < record_id <= len(entries):
			entry = entries[record_id - 1]
			record = view_record(entry)
			for key, value in record.items():
				if view_credentials and key in ['UserName', 'Password']:
					print(colorize_output(key, value))
				elif view_notes and key == 'Notes':
					print(colorize_output(key, value))
				elif not view_credentials and not view_notes:
					print(colorize_output(key, value))
		else:
			print(Fore.RED + "Record ID out of range" + Style.RESET_ALL)

	else:
		print(Fore.RED + "No valid operation specified" + Style.RESET_ALL)

###########################################

def action():
	main()

########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)