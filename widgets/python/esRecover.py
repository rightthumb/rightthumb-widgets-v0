import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
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

_copy = _.regImp( __.appReg, '-copy' )

def file_exists_recursive(folder: str, filename: str) -> bool:
    """
    Recursively check if `filename` exists inside `folder`.
    
    Args:
        folder (str): Path to the starting folder.
        filename (str): Name of the file to search for (not full path).
    
    Returns:
        bool: True if found, False otherwise.
    """
    for root, dirs, files in os.walk(folder):
        if filename in files:
            return True
    return False


import os
import shutil
def action():
    _.clear()
    db = _.getTable2('esRecover.list')
    for file in _.isData(2):
        file = file.strip()
        if not file: continue
        skip = False
        for spent in db:
            sp = spent['file'].lower()
            # print('sp',sp,sp == file.lower(), '\\'+sp in file.lower())
            if sp == file.lower() or '\\'+sp in file.lower():
                skip = True
                break
        if skip: continue
        fi = file.split('\\')[-1]
        if file_exists_recursive('.', fi):
            continue

        _.pr()
        _.pr(line=1,c='green')
        _.pr(file)
        _.pr()
        _copy.imp.copy( ri, p=0 )
        search = input('Search: ').strip()
        if search == 'x': return
        res = _.cmd('es '+search)
        _copy.imp.copy( res.split('\n')[0], p=0 )

        _.pr( res )
        _.pr()
        _.pr()
        path = input('Chosen: ')
        path = path.strip()
        if not path:
            db.append({'file': search, 'status': 'no file chosen', 'path': ''})
            _.saveTable2(db,'esRecover.list',p=0)
            _.pr('No file chosen.')
            continue

        # copy chosen to current folder '.'
        shutil.copy(path, '.')
        db.append({'file': search, 'status': 'file copied', 'path': path})
        _.saveTable2(db,'esRecover.list',p=0)
        _.pr('File copied.')



########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)