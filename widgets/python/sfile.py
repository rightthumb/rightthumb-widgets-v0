import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Folders', '-f,-fo,-folder,-folders' )
    _.switches.register( 'Recursive', '-r' )
    _.switches.register( 'FullPath', '-p,-path' )
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

def getFilesInDir( dirPath, recursive=False ):
    import os
    fileList = []
    if recursive:
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                if not _.showLine(file): continue
                path = os.path.join(root, file)
                if not _.switches.isActive('FullPath'):
                    path = path.replace( dirPath.rstrip( os.sep ) + os.sep, '' )
                fileList.append( path )
    else:
        for item in os.listdir(dirPath):
            fullPath = os.path.join(dirPath, item)
            if os.path.isfile(fullPath):
                if not _.showLine(item): continue
                path = fullPath
                if not _.switches.isActive('FullPath'):
                    path = path.replace( dirPath.rstrip( os.sep ) + os.sep, '' )
                fileList.append( path )
                # fileList.append( fullPath )
    return fileList

def action():
    # list files in dir
    files = []
    folders = _.switches.values('Folders')
    if not folders:
        import os
        folders = [ os.getcwd() ]
    for folder in folders:
        recursive = _.switches.isActive('Recursive')
        filesInDir = getFilesInDir( folder, recursive )
        if len(_.switches.values('Folders')) > 1:
            _.pr( 'Folder:', folder )
            for f in filesInDir: _.pr( '\t'+f, c='cyan' )
        else:
            for f in filesInDir: _.pr( f, c='cyan' )
        # files.extend( filesInDir )


########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)