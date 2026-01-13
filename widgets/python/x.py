import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Files', '-f','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Args', '-a,-arg,-args', isRequired=False )
_._default_settings_(); __.setting('default-switches',False);
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

def execute_python(path):
	if not os.path.exists(path):
		print("File does not exist:", path)
		return

	code = _.getText2(path, 'text')
	# # print(code); sys.exit();
	local_namespace = {}
	exec(code, globals(), local_namespace)
	# exec(code)
	return local_namespace

import subprocess
import sys
import os

# def execute_script(path):
# 	if not os.path.exists(path):
# 		print("File does not exist:", path)
# 		return

# 	if __.isWin:
# 		shell_cmd = ['cmd', '/c']
# 	else:
# 		shell_cmd = ['/bin/bash']

# 	# Include the file path in the command
# 	shell_cmd.append(path)

# 	# Start the process
# 	process = subprocess.Popen(shell_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# 	# Stream the output
# 	while True:
# 		output = process.stdout.readline()
# 		if process.poll() is not None and output == b'':
# 			break
# 		if output:
# 			print(output.decode('utf-8'), end='')

# 	# Ensure the process has finished
# 	process.poll()

import sys
import subprocess
import os

def process_initial_arguments():
	"""
	Process and potentially modify the initial command-line arguments.
	Removes the first argument (typically the script name) and any '--remove' flags.
	"""
	# new_argv = [arg for arg in sys.argv[1:] if arg != '--remove']
	# return new_argv
	# start = 0
	arguments = []
	if _.switches.isActive('Args'):
		arguments = _.switches.values('Args')
	# for arg in sys.argv[1:]:
	# 	if start == 2:
	# 		arguments.append(arg)
	# 	if start == 1: start == 2
	# 	if arg == '-f':
	# 		start = 1

	return arguments

def execute_script(path, arguments):
	"""
	Execute a shell script with the provided arguments.
	"""
	if not os.path.exists(path):
		print(f"File not found: {path}")
		return

	# Prepare the command to execute, including the script path and arguments
	command = [path] + arguments

	try:
		# Execute the command and capture the output
		result = subprocess.run(command, text=True, capture_output=True)
		print(result.stdout)  # Print the standard output of the script
		if result.stderr:
			print("Error:", result.stderr)  # Print any standard error output
	except Exception as e:
		print(f"Error running the shell script: {e}")




def action():
	for path in _.isData():
		path = __.path(path)
		if path.endswith('.py'):
			execute_python(path)
		else:
			execute_script(path, process_initial_arguments())

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);