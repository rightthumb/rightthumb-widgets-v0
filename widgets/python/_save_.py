import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Folder', '-f', '_docs_' )
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

import os
def create_save_folders(directory):
    """
    Recursively creates a folder named '_save_' in every directory starting from the specified directory.
    It skips creating '_save_' folders inside other '_save_' folders.
    """
    for root, dirs, files in os.walk(directory, topdown=True):
        # Skip any directory that is already a '_save_' directory
        if os.path.basename(root) == '_save_':
            continue
        
        # Update the list of directories to skip creating '_save_' inside '_save_'
        dirs[:] = [d for d in dirs if d != '_save_']
        
        save_path = os.path.join(root, '_save_')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            print(f"Created '_save_' folder in: {root}")


def action():
    if _.switches.isActive('Folder'):
        folder = _.switches.values('Folder')[0]
    else:
        folder = os.getcwd()
    create_save_folders(folder)

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);


