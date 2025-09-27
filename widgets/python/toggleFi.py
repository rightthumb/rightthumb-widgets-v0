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
import os

def txt(path):
    return _.getText(path, raw=True)

def action():
    # Determine the working folder
    if _.switches.isActive('Folder'):
        folder = os.path.abspath(_.switches.value('Folder')) + os.sep
        os.chdir(folder)
    else:
        folder = os.getcwd() + os.sep

    # Resolve destination file path
    destination_name = _.switches.value('Destination')
    if not destination_name:
        _.e('No destination specified')
    destination = folder + destination_name

    # Read destination content
    try:
        dest = txt(destination)
    except Exception:
        _.e('Destination file does not exist or cannot be read: ' + destination)

    # Prepare list of source files
    files = _.switches.values('Files')
    files = [file if os.sep in file else folder + file for file in files]

    # Determine which source file matches current destination content
    current_index = -1
    for i, file in enumerate(files):
        if not os.path.exists(file):
            _.e('Source file does not exist: ' + file)
        if os.path.exists(file) and txt(file) == dest:
            current_index = i
            break

    # print('Current index:', current_index)
    if current_index == -1:
        current_index = 0
        # _.e('No matching file found in the list of source files.')

    # Determine next file to copy
    next_index = (current_index + 1) % len(files)
    try:
        files[current_index+1]
        next_index = current_index + 1
    except:
        next_index = 0
    # print(next_index)
    # Copy contents to destination
    next_file = files[next_index]
    contents = txt(next_file)
    # print('Copying contents from:', next_file)
    _.saveText(contents, destination)

    # Output result
    relative_name = next_file.replace(folder, '')
    _.pr('Now: ' + relative_name, c='green')
 
    

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)