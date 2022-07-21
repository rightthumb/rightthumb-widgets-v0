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
    _.switches.register( 'Fi', '-f,-fi,-file,-files','notes.md' )
    _.switches.register( 'Date', '-date' )
    _.switches.register( 'Ago', '-ago' )
    _.switches.register( 'Clean', '--c' )
    _.switches.register( 'Open', '-o,-open' )
    _.switches.register( 'Print', '-p,-print' )

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
                        _.hp(''),
                        _.hp('echo. | p day -f notes.md'),
                        '|-   ##### --> timestamp#> 2022-07-21T03:03:49-0400',
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


########################################################################################
# START

bat = '''@echo off
cd path
echo path
echo ago

'''
sh = '''#!/bin/bash
cd path
echo path
echo ago

'''

os = __.imp('os.path.isdir')
os = __.imp('os.system')
os = __.imp('os.chmod')
_docs = _.regImp( __.appReg, 'decrypt-docs' )
_open = _.regImp( __.appReg, 'file-open' )
_md = _.regImp( __.appReg, 'md' )
sep=os.sep
# _docs.switch('Files')

def load():
    global fo
    epoch = time.time()
    if _.switches.isActive('Ago'): epoch = _.switches.value('Ago')
    if _.switches.isActive('Date'): epoch = _.autoDate( _.switches.value('Date') )

    today = _.day(epoch)
    fo =  _v.rtp+'daily'+os.sep+today
    # if not _.switches.isActive('Clean'): _.pr(today)
    _v.mkdir(fo)
    if _.isWin:
        global bat
        # script=_v.ww+sep+'batch'+sep+'.day.bat'
        script=_v.ww+sep+'batch'+sep
        bat = bat.replace('path',fo)
        bat = bat.replace('ago', _.isDate(epoch,f='ago') )
        bat = _str.do('sh',bat); _.saveText( bat, script+'.day.bat' ); _.saveText( bat, script+'.d.bat' );
        _.pr( script, c='Background.light_blue' )
    else:
        global sh
        script = _v.ww+sep+'bash'+sep+'nav'+sep+'day.sh'
        sh = sh.replace('path',fo)
        sh = sh.replace('ago', _.isDate(epoch,f='ago'))
        sh = _str.do('sh',sh); _.saveText( sh, script );
        os.chmod( script, 0o777 )
        _.pr( script, c='Background.light_blue' )

def files(fi):
    global fo
    path=fo+fi
    if _.isData():
        save=True
        txt = '\n'.join(_.isData())
        if os.path.isfile(path):
            _.pr('append file',c='red')
            # ask=input2(' replace file? : ')
            # if 'n' in ask.lower(): save = False
        if save:
            if os.path.isfile(path):
                t2 = _.getText(path,raw=True)+'\n\n'+'##### --> timestamp#> '+_.isDate(time.time(),f='iso')+'\n\n'
                txt=t2+txt
            _.saveText( txt, path ); _.pr( path, c='cyan' )
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
    _docs.switch('Files',no); _docs.action();
    
    if _.switches.isActive('Print'):
        _md.switch('View-Webpage')
        _md.switch('Files',no)
        _md.action()

    if not _.isWin:
        os.system( 'nano '+ no )
    else:
        if _.switches.isActive('Open'): _md.switch('Files',no); _md.action();
        else: _open.switch('Files',no); _open.action();


    # _.pr(path)

# def input2(txt=''):
#     # p = input(txt)
#     line=''
#     i=0
#     while True:
#         i+=1
#         if i > 1000: break
#         try:
#             line = input(txt)
#         except EOFError:
#             pass
#             clear()
#             # return line

#     return line


########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()




