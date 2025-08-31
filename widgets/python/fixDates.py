import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

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






#!/usr/bin/env python3
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

def default_epoch(months_ago: int = 6) -> float:
    """
    Returns an epoch timestamp for N months ago (default: 6).
    """
    target_dt = datetime.now() - relativedelta(months=months_ago)
    return target_dt.timestamp()

def set_mtime(path: str, target_epoch: float, include_dirs: bool = False):
    """
    Recursively set modification times of all files (and optionally directories)
    under `path` to `target_epoch`.
    """
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                atime = os.path.getatime(file_path)
                os.utime(file_path, (atime, target_epoch))
                print(f"Updated file: {file_path}")
            except Exception as e:
                print(f"Error updating {file_path}: {e}")

        if include_dirs:
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    atime = os.path.getatime(dir_path)
                    os.utime(dir_path, (atime, target_epoch))
                    print(f"Updated dir: {dir_path}")
                except Exception as e:
                    print(f"Error updating {dir_path}: {e}")

# ----------------
# Example usage
# ----------------
if __name__ == "__main__":
    # Example 1: Use default (6 months ago)
    epoch_six_months = default_epoch(6)
    # epoch_one_month = default_epoch(1)
    # set_mtime(".", epoch_six_months, include_dirs=False)




import os
import time

def create_file_with_mtime(path: str, epoch: float):
    """
    Create a file at `path` and set its modification time to `epoch`.
    If the file already exists, its mtime will still be updated.
    """
    try:
        # create file if missing, leave untouched if exists
        with open(path, "a"):
            os.utime(path, (os.path.getatime(path), epoch))
        print(f"Created/updated file: {path} -> mtime set to {time.ctime(epoch)}")
    except Exception as e:
        print(f"Error creating/updating file {path}: {e}")






import os
def action():
    base = os.getcwd()+os.sep
    _.pr()
    _.pr('',base,c='red')
    _.pr()
    ask = input('Change dates?: ')
    if not 'y' in ask:
        return
    db = _.getTable('fileBackup.json')
    latest = {}
    for rec in db:
        file = rec['file']
        epoch = rec['timestamp']
        if base in file:
            if not file in latest:
                latest[file] = epoch
            else:
                if epoch > latest[file]:
                    latest[file] = epoch
    for path in latest:
        create_file_with_mtime(path, latest[path])
        _.pr(path)




########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)