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

db = _.MongoDBMgr('widgets', 'mongodb://localhost:27017/', sanitize_keys=True)
# print(_._ago('3m'))
def test():
    test = db.find('fileBackup')
    for t in test:
        _.pv(t)
        return

def test():
    # print(_._ago('3d'))
    test = db.find('fileBackup',{
        "file": {"$regex": r"\.py$"},
        "timestamp": {"$gt": _._ago('3d')}
    })
    cnt=0
    for t in test:
        cnt+=1
        _.pv(t)
        # return
    print(cnt)


def test():
    # print(_._ago('3d'))
    test = db.db['fileBackup'].find({
        "file": {"$regex": r"\.py$"},
        "timestamp": {"$gt": _._ago('1m ')}
    })
    cnt=0
    for t in test:
        cnt+=1
        _.pv(t)
        # return
    print(cnt)






def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)