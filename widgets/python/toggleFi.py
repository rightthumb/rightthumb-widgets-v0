import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Destination', '-d' )
    _.switches.register( 'Folder', '-fo,-folder' )
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
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

def txt(path):
    return _.getText(path, raw=True)

import os

def action():
    if _.switches.isActive('Folder'):
        os.chdir(_.switches.value('Folder'))
        folder = _.switches.value('Folder')+ os.sep
    else:
        folder = os.getcwd()+ os.sep


    destination = folder+ _.switches.value('Destination')

    dest = txt(destination) if destination else None
    if not dest:
        _.e('no destination')

    files = _.switches.values('Files')

    isI = None
    for i,file in enumerate(files):
        contents = txt(file)
        if contents == dest:
            # _.pr('Is: ' + file,c='green')
            isI = i
            break
    try:
        files[isI+1]
        nextI = isI + 1
    except:
        nextI = 0
    # print('nextI: ' + str(nextI))
    
    contents = txt(files[nextI])
    _.saveText(contents, destination)
    _.pr('Now: ' + files[nextI].replace(_.switches.values('Destination')[0],''),c='green')    
    

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)