#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
    global appDBA;f=__.appName(appDBA,parentApp,childApp);
    if reg:__.appReg=f;
    return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################

def sw():
    pass
    ### EXAMPLE: START
    _.switches.register( 'Fi', '-f,-fi,-file,-files','notes.md' )
    _.switches.register( 'Date', '-date' )
    _.switches.register( 'Ago', '-ago' )
    _.switches.register( 'Clean', '--c' )
    _.switches.register( 'Open', '-o,-open' )
    # _.switches.register( 'Files', '-f,-fi,-file,-files' )
    ### EXAMPLE: END

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
    # 'app': '8facG-jo0Cxk',
    'file': 'day.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'daily documentaion system',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'notes',
                        'documentaion',
                        'today',
                ],
    'usage': [
                        # 'epy another',
                        # 'e nmap',
                        # '',
    ],
    'relatedapps': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'prerequisite': [
                        # 'p another -file file.txt',
                        # '',
    ],
    'examples': [
                        _.hp('p day'),
                        _.linePrint(label='simple',p=0),
                        '',
    ],
    'columns': [
                       # { 'name': 'name', 'abbreviation': 'n' },
                       # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
    ],
    'aliases': [
                       # 'this',
                       # 'app',
    ],
    'notes': [
                       # {},
    ],
}

_.appData[focus()] = {
        'start': __.startTime,
        'uuid': '',
        'audit': [],
        'pipe': False,
        'data': {
                    'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
                    'table': {'sent': [], 'received': [] },
        },
    }


def triggers():
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'URL', _.urlTrigger )
    _.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
### EXAMPLE: START


    #--> make hotkey ad-description soon:  <--<w#
    #-->    - outer most typed first
    #-->    - blank pipe
    #-->    __.setting('hotkey-clip.ad_description-start1',d=False)
    #--> _________________________________
    #--> describe selection area two
    #--> 3 write a note here wrap text
    #--> two dignissim
    #--> 1 inceptos
    #--> _________________________________
    #--> describe selection area two
    #-->              |           |
    #-->              |           | - write a note here
    #-->              |           |   wrap text
    #-->              |           |
    #-->              |           | - dignissim
    #-->              |
    #-->              | - inceptos

    # if _.switches.isActive('Test'): test(); return None;
    # result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
    # bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
    #--> a=(1 if True else 0) <--# 
    #--> m=[[row[i] for row in matrix] for i in range(4)]
    # requests=__.imp('requests.post')
    # data=str(requests.post(url,data={}).content,'iso-8859-1')
    # for k in globals(): print(k, eval(k) )


### EXAMPLE: END
########################################################################################
# START

os = __.imp('os.path.isdir')
_docs = _.regImp( __.appReg, 'decrypt-docs' )
_open = _.regImp( __.appReg, 'file-open' )
_md = _.regImp( __.appReg, 'md' )
# _docs.switch('Files')

def load():
    global fo
    today = _.day()
    fo =  _v.rtp+'daily'+os.sep+today
    # if not _.switches.isActive('Clean'): _.pr(today)
    _v.mkdir(fo)

def files(fi):
    global fo
    path=fo+fi
    if _.isData():
        save=True
        txt = '\n'.join(_.isData())
        if os.path.isfile(path):
            ask=input(' replace file? : ')
            if 'n' in ask.lower(): save = False
        if save: _.saveText( txt, path ); _.pr( path, c='cyan' )
        # return None
    _open.switch('Files',path)
    _open.action()



def action():
    global fo
    load()
    path = fo
    
    if _.switches.isActive('Fi'):
        for fi in _.switches.values('Fi'):
            files(fi)
        return None
    no = path+'notes.md'
    _.pr(no,c='cyan')
    if not os.path.isfile(no): _.saveText('___\n# '+_.isDate(time.time(),f='date')+'\n\n',no)
    
    _docs.switch('Files',no)
    _docs.action()
    if _.switches.isActive('Open'):
        _open.switch('Files',no)
        _open.action()
    else:
        _md.switch('Files',no)
        _md.action()


    # _.pr(path)




########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()





