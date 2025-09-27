import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
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

# locate */home/*/bookmarks.index | p line - .rt/.rt --c | p syncAliases
# locate */home/*/file-open-aliases.hash | p line - .rt/.rt --c | p syncAliases

# p fileBackup -f /root/.rt/profile/tables/file-open-aliases.hash &&  p fileBackup -f /root/.rt/profile/tables/bookmarks.index && locate */home/*/bookmarks.index | p line - .rt/.rt --c | p syncAliases && locate */home/*/file-open-aliases.hash | p line - .rt/.rt --c | p syncAliases && p fileBackup -f /root/.rt/profile/tables/file-open-aliases.hash &&  p fileBackup -f /root/.rt/profile/tables/bookmarks.index
# alias a.="p fileBackup -f /root/.rt/profile/tables/file-open-aliases.hash &&  p fileBackup -f /root/.rt/profile/tables/bookmarks.index && locate */home/*/bookmarks.index | p line - .rt/.rt --c | p syncAliases && locate */home/*/file-open-aliases.hash | p line - .rt/.rt --c | p syncAliases && p fileBackup -f /root/.rt/profile/tables/file-open-aliases.hash &&  p fileBackup -f /root/.rt/profile/tables/bookmarks.index"

def action():
    # _bk = _.regImp( __.appReg, 'bk' )
    # _bk.pipe( [_v.tt+_v.slash+'file-open-aliases.hash'] )
    # _bk.action()
    # _bk.pipe( [_v.tt+_v.slash+'bookmarks.index'] )
    # _bk.action()
    db = _.getTable('file-open-aliases.hash')
    for path in _.isData():
        if not 'file-open-aliases.hash' in path: continue
        tb = _.getTable2(path)
        # print(tb); break
        if not 'aliases' in tb:
            _.pv(tb)
            tb['aliases'] = {}
        for k in tb['aliases']:
            if not k in db['aliases']:
                db['aliases'][k] = tb['aliases'][k]
        if not 'files' in tb:
            _.pv(tb)
            tb['files'] = {}
        for k in tb['files']:
            for a in tb['files'][k]:
                if not k in db['files']:
                    db['files'][k] = []
                if not a in db['files'][k]:
                    db['files'][k].append(a)
    _.saveTable(db, 'file-open-aliases.hash')

    db = _.getTable('bookmarks.index')
    for path in _.isData(2):
        if not 'bookmarks.index' in path: continue
        tb = _.getTable2(path)
        # print(tb); break
        if not 'labels' in tb:
            _.pv(tb)
            tb['labels'] = {}
        for k in tb['labels']:
            if not k in db['labels']:
                db['labels'][k] = tb['labels'][k]
        if not 'paths' in tb:
            _.pv(tb)
            tb['paths'] = {}
        for k in tb['paths']:
            for a in tb['paths'][k]:
                if not k in db['paths']:
                    db['paths'][k] = []
                if not a in db['paths'][k]:
                    db['paths'][k].append(a)
    _.saveTable(db, 'bookmarks.index')

    # labels
    # paths


        
########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)