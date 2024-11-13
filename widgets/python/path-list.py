import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register('Clean', '--c')
	_.switches.register('Path', '-path')
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
import subprocess

def execute_and_return(command):
    """
    Executes the given command in the terminal and returns the output.
    :param command: A string representing the command to be executed.
    :return: The output of the command as a string.
    """
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def action():
	if _.isWin:
		command = "echo %path%"
		output = execute_and_return(command)
		output = output.split(';')
	else:
		command = "echo $PATH"
		output = execute_and_return(command)
		output = output.split(':')
	spent = []
	save=[]
	for line in output:
		if os.path.isdir(line):
			if not line.lower() in spent:
				if _.showLine(line):
					if line.endswith(os.sep):
						line = line[:-1]
					if not _.switches.isActive('Path'):
						_.pr(line)
				spent.append(line.lower())
				save.append(line)
	if not _.switches.isActive('Clean') and not _.switches.isActive('Path'):
		_.pr('\n',len(spent),c='yellow')
	if _.switches.isActive('Path'):
		if _.isWin:
			paths = ';'.join(save)
			path = 'SET "PATH='+paths+'"'
		else:
			paths = ':'.join(save)
			path = 'export PATH='+paths
		_.pr(path)
import os

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);