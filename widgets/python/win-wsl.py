import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
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

import re
import os

def windows_to_wsl(path):
    # Normalize slashes and strip quotes
    path = path.strip().replace('\\', '/').strip('"').strip("'")

    # Match drive letter
    match = re.match(r'^([a-zA-Z]):/(.*)', path)
    if match:
        drive = match.group(1).lower()
        subpath = match.group(2)
        wsl_path = f'/mnt/{drive}/{subpath}'
    else:
        # Already looks like a relative Unix-style path
        wsl_path = path

    # Clean up multiple slashes
    wsl_path = re.sub(r'/+', '/', wsl_path)

    return wsl_path


import re

def wsl_to_windows(path):
    path = path.strip().replace('\\', '/').strip('"').strip("'")

    # Match /mnt/<drive>/path...
    match = re.match(r'^/mnt/([a-zA-Z])/(.*)', path)
    if match:
        drive = match.group(1).upper()
        subpath = match.group(2).replace('/', '\\')
        win_path = f'{drive}:\\{subpath}'
    else:
        # Not in /mnt format; possibly a Unix-style relative path
        win_path = path.replace('/', '\\')

    return win_path


def convert_path_auto(path):
    """
    Detects whether a path is Windows or WSL style and converts accordingly.
    """
    path = path.strip()
    
    # Heuristic: If it starts with a drive letter and backslashes or contains ':' early, it's likely Windows
    if re.match(r'^[a-zA-Z]:[\\/]', path) or '\\' in path:
        return windows_to_wsl(path)
    
    # Heuristic: If it starts with /mnt/<drive>/ it's likely WSL
    if re.match(r'^/mnt/[a-zA-Z]/', path):
        return wsl_to_windows(path)
    
    # Default fallback
    return path



def action():
    for path in _.isData():
        path = convert_path_auto(path)
        _.pr(path)

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)