import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt',  isData='name', description='Files', isRequired=False )
    _.switches.register( 'Folder', '-fo,-folder','folder/' )
    _.switches.register( 'Copy', '-cp,--c' )
    _.switches.register( 'Move', '-mv,--m,-m' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': '-File2Folder.py',
    'description': 'Copy or Move Files to a Folder using Framework and possibly aliases, or urls',
    'categories': [
                        'os',
                        'copy',
                        'move',
                ],
    'examples': [
                        _.pr('The reason for this app is to use file and folder aliases built into the terminal framework',c='Background.red',p=0),
                        _.hp(''),
                        _.hp('The source is registed so you know where it came from'),
                        _.hp(''),
                        _.hp('p -File2Folder -f file.txt -fo ../folder'),
                        _.hp(''),
                        _.hp('No file specified gets file from clipboard'),
                        _.hp(''),
                        _.hp(''),
                        _.hp('rust'),
                        _.hp('p files + *.exe target\\release\\ - \\build\\ \\deps\\ -copy'),
                        _.hp('p -File2Folder -fo exe.rust'),
                        _.hp(''),
                        _.hp('p -File2Folder -f ClipView.exe -fo exe.bin'),
                        _.hp(''),
                        _.hp(''),
                        _.hp('Move to alias for JavaScript archive folder: archive.js'),
                        _.hp('p -File2Folder -f file1.js file2.js -fo archive.js -move'),
                        _.hp(''),
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

import shutil
import os

def action():
    _.isDataClip(__.appReg)
    folder = _.switches.value('Folder')
    for file in _.isData(2):
        fi = file.split(os.sep)[-1]
        # print(file, folder)
        if _.switches.isActive('Copy') or not _.switches.isActive('Move'):
            shutil.copy(file, folder)
            _.pr('Copied: \n  {}\n  {}'.format(file, folder))
            _.RegID.add(fi, 'Copy src: '+file, '-File2Folder')
        elif _.switches.isActive('Move'):
            shutil.move(file, folder)
            _.pr('Moved: \n  {}\n  {}'.format(file, folder))
            _.RegID.add(fi, 'Move src: '+file, '-File2Folder')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)