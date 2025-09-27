import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Path', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
    _.switches.register( 'Delete', '-rm,-del' )
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

def extended_path(path: str) -> str:
    """Return a Windows extended-length path for reserved names."""
    if not os.sep in path:
        path = os.getcwd() + os.sep + path
    pre = path
    abs_path = os.path.abspath(path)
    if len(abs_path) < len(pre):
        abs_path = pre
    return r"\\?\{}".format(abs_path)

def safe_delete(path: str):
    """Delete file or directory, even if named with reserved words like 'nul'."""
    ep = extended_path(path)
    if os.path.isdir(ep):
        shutil.rmtree(ep, ignore_errors=True)
    elif os.path.isfile(ep):
        os.remove(ep)
    else:
        print(f"Path not found: {ep}")

def windows_extended_path(rel_path: str) -> str:
    """
    Convert a relative or normal path into a Windows extended-length path
    using the \\?\ prefix, which allows deletion/handling of reserved names like 'nul'.
    Example:
        windows_extended_path("logs/nul")
        -> '\\\\?\\C:\\Users\\Scott\\project\\logs\\nul'
    """
    abs_path = os.path.abspath(rel_path)
    return r"\\?\{}".format(abs_path)

def action():
    _.isDataClip(__.appReg)
    for path in _.isData(2):
        ext = extended_path(path)
        _.pr(ext,c='cyan')
        if _.switches.isActive('Delete'):
            safe_delete(path)
            _.pr("Deleted: {}".format(path), c='red')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)