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

import os
import shutil

def save_incremental_backup(source, backup_folder, prefix='fileBackup-', extension='.json', max_digits=2):
    os.makedirs(backup_folder, exist_ok=True)
    existing_files = [
        f for f in os.listdir(backup_folder)
        if f.startswith(prefix) and f.endswith(extension)
    ]
    numbers = []
    for fname in existing_files:
        try:
            number = int(fname[len(prefix):-len(extension)])
            numbers.append(number)
        except ValueError:
            continue  # skip if not a number
    next_number = max(numbers) + 1 if numbers else 0
    next_filename = f"{prefix}{next_number:0{max_digits}d}{extension}"
    target_path = os.path.join(backup_folder, next_filename)
    shutil.copy2(source, target_path)
    print(f"Backup saved as {target_path}")
    return target_path

def action():
    _v.mkdir(_v.tt+os.sep+'backup_log')
    save_incremental_backup(_v.tt+os.sep+'fileBackup.json', _v.tt+os.sep+'backup_log')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)