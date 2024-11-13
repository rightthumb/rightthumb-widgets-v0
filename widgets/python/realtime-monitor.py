import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
    pass
    _.switches.register( 'Folder', '-f,-folder,-folders,-fo' )
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
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import os
import time

spent = []

def fo(folder=None, recursive=False, first=True):
    global spent
    if folder is None:
        folder = os.getcwd()


    if not os.path.isdir(folder):
        return

    try:
        files = os.listdir(folder)
    except Exception as e:
        print(f"Error accessing folder {folder}: {e}")
        return

    for item in files:
        path = os.path.join(folder, item)

        if path not in spent:
            spent.append(path)
            if os.path.isfile(path): thisIs = "Fi"
            elif os.path.isdir(path): thisIs = "Fo"
            print(thisIs+':', path)

        # If recursive flag is set and it's a directory, recurse into it
        if recursive and os.path.isdir(path):
            fo(path, recursive=False, first=False)

def action():
    folder = os.getcwd()  # Change this if you want a specific folder to monitor
    while True:
        fo(folder, recursive=True)
        time.sleep(5)  # Adjust sleep duration as needed

if __name__ == "__main__":
    action()


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__);