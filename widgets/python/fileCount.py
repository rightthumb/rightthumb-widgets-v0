import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
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

# Encrypted URL
# M2ITwl3r2+8ymuMysZBeGa0+Y+cjUMH6y5RoJRi6sqGZkHrO+VPZm8/N7qbKaNOijsq+M4azaw5mb1n2iHcjqQ==


###########################################
import os
import argparse

def build_file_list(base_path):
	file_list = []

	for root, dirs, files in os.walk(base_path):
		relative_path = os.path.relpath(root, base_path)
		file_count = len(files)
		file_entry = {"path": relative_path, "files": file_count}
		file_list.append(file_entry)

	return file_list

def print_file_list(file_list):
	for entry in file_list:
		print(f"{entry['files']}\t{entry['path']}")

def save_file_list(file_list, output_file):
	with open(output_file, 'w') as f:
		for entry in file_list:
			f.write(f"{entry['files']}\t{entry['path']}\n")

def action():
	parser = argparse.ArgumentParser(description="Recursively traverse folders and count files.")
	parser.add_argument("-o", "--output", help="Output file to save the list.", default=None)
	args = parser.parse_args()

	base_path = os.getcwd()
	file_list = build_file_list(base_path)

	if args.output:
		save_file_list(file_list, args.output)
	else:
		print_file_list(file_list)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);