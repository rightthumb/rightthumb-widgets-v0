import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    _.switches.register('Has-Files-In-Current-Folder', '-cf,-dir')
    _.switches.register('Has-Files-In-Specific-Folder', '-fo,-folder,-folders')
    _.switches.register('Include-File-Paths', '-p,-path')
    _.switches.register('No-File-Extension', '-noext')
    _.switches.register('Clipboard', '-clip')
    _.switches.register('Files', '-f,-fi,-file,-files','file.txt', description='Files', isRequired=False)
    _.switches.register('Invert', '-i')
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
    _.switches.trigger( 'Has-Files-In-Specific-Folder', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    __.SwitchesModifier.Trigger['Has-Files-In-Specific-Folder'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import os

def list_files(folder='.', full_path=None):
    if full_path is None:
        if _.switches.isActive('Include-File-Paths') or _.switches.isActive('No-File-Extension'):
            full_path = True
        else:
            full_path = False
    folder = folder or '.'
    return [
        os.path.join(folder, f) if full_path else f
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]



def refined(folder='.'):
    files = []
    for file in list_files(folder):
        if _.showLine(file):
            files.append(file)
    # print(files)
    return files


def testThis(data):
    global PIPE
    if type(data) == str: data = data.split('\n')

    for test in data:
        # print(test)
        if  not type(test) == str: continue
        test = test.strip()
        if _.switches.isActive('No-File-Extension'):
            if not os.sep in test:
                continue
            else:
                # print(test)
                # test = __.path(test)
                test = os.path.splitext(os.path.basename(test))[0]
                test = test.lstrip('./').lstrip('.\\')
                # print(test)

        if _.switches.isActive('Invert'):
            if test not in PIPE:
                _.pr(test,c='red')
        else:
            if test in PIPE:
                _.pr(test, c='green')

import sys


# import os
# name = os.path.splitext(os.path.basename(full_path))[0]



PIPE = None
def action():
    global PIPE

    PIPE = []
    for line in _.isData(2):
        line = line.strip()
        if line in PIPE: continue
        PIPE.append(line)
    PIPE = '\n'.join(PIPE)

    # print('PIPE:', PIPE)

    if not PIPE: _.e('No data in pipe')


    if PIPE:
        if _.switches.isActive('Files'):
            files = _.switches.values('Files')
            data = []
            for file in files:
                data.append(file)
                if os.sep in file:
                    file = file.split(os.sep)[-1]
                    data.append(file)

            testThis(data)
            return
        
        if _.switches.isActive('Clipboard'):
            _paste = _.regImp( __.appReg, '-paste' )
            clip = _paste.imp.paste()
            testThis(clip)
            return
        
        if _.switches.isActive('Has-Files-In-Current-Folder'):
            files = refined()
            testThis(files)
            return
        

        if _.switches.isActive('Has-Files-In-Specific-Folder'):
            folders = _.switches.values('Has-Files-In-Specific-Folder')

            for folder in folders:
                files = refined(folder)
                testThis(files)

            return

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)