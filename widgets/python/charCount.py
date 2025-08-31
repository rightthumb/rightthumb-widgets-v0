import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
    _.switches.register( 'NumberOfCharsToSarchFor', '-chars', '5' )
    _.switches.register( 'ReturnNumberOfChars', '-count', 'b.bat' )
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'charCount.py',
    'description': 'Only prints if has specific number of characters',
    'categories': [
                        'search',
						'tool',
						'refine results',
                ],
    'examples': [
                        _.hp('p file --c | p charCount -chars 5'),
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

def action():
    if _.switches.isActive('ReturnNumberOfChars'):
        print( len(_.switches.values('ReturnNumberOfChars')) )
        return
    
    if _.switches.isActive('NumberOfCharsToSarchFor'):
        chars = int(_.switches.value('NumberOfCharsToSarchFor'))

    for line in _.isData(2):
        l = len(line.strip())
        if l == chars:
            _.pr(line,c='cyan')

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)