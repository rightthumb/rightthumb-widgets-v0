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
    _.switches.register( 'Date', '-d,-date' )
    _.switches.register( 'Epoch', '-e,-epoch' )
    _.switches.register( 'Ago', '-ago' )
    _.switches.register( 'Clean', '--c' )
    _.switches.register( 'Open', '-o,-open' )
    _.switches.register( 'Print', '-p,-print' )
    _.switches.register( 'Change-Dir', '-cd' )

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

def hush():
    global isWin
    if isWin: return ' > nul 2>&1'
    else: return ' > /dev/null 2>&1'

bat = '''@echo off
call m back   > nul 2>&1
echo Background.green linePrint       > %tmpf%-print_color-day
echo yellow last fo: b back          >> %tmpf%-print_color-day
call bb back > %tmpf%-back
SET /p pretty_back=<%tmpf%-back
echo purple %pretty_back%  >> %tmpf%-print_color-day
echo.                                >> %tmpf%-print_color-day
echo darkcyan ago                    >> %tmpf%-print_color-day
echo cyan path                       >> %tmpf%-print_color-day
echo Background.green linePrint      >> %tmpf%-print_color-day
call p print_color -f %tmpf%-print_color-day -tab 2
cd path
'''
sh = '''#!/bin/bash
source $HOME/.bashrc
$m back   > /dev/null 2>&1
echo ''    >> $HOME/.bashrc.once.print
echo last fo: b.back >> $HOME/.bashrc.once.print
$bb back   >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
echo ago   >> $HOME/.bashrc.once.print
echo path  >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
sed -i 's/^/\t\t/' $HOME/.bashrc.once.print
if [ ! -f path/notes.md ] then
    touch path/notes.md
fi
# $cdf path/notes.md
cd path
$SHELL

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
    global epoch
    epoch = time.time()
    ep=epoch
    if _.switches.isActive('Epoch'): epoch = float(_.switches.value('Ago'))
    if _.switches.isActive('Ago'): epoch = _.switches.value('Ago'); epoch-=5;
    if _.switches.isActive('Date'): epoch = _.autoDate( _.switches.value('Date') )
    
    today = _.day(epoch)
    fo =  _v.rtp+'daily'+os.sep+today
    # if not _.switches.isActive('Clean'): _.pr(today)
    _v.mkdir(fo)
    # ago1=_.isDate(epoch,f='ago').replace(' <','').replace('<',''); ago2=str(_.isDate(epoch,f='ago-dic')).replace('"','').replace("'",'').replace('{','').replace('}','').replace('<','').replace('>',''); ago='( '+ago1+' ) '+ago2;
    # if ago1 == 'today': ago=ago1
    ago=_.isDate(float(epoch),f='ago-txt')
    if _.isWin:
        global bat
        # script=_v.ww+sep+'batch'+sep+'.day.bat'
        script=_v.ww+sep+'batch'+sep
        bat = bat.replace('path',fo)
        bat = bat.replace('ago', ago )
        bat = _str.do('sh',bat); _.saveText( bat, script+'.day.bat' ); _.saveText( bat, script+'.d.bat' );
        _.pr( script, c='Background.light_blue' )
    # else:
    #     global sh
    #     script = _v.ww+sep+'bash'+sep+'nav'+sep+'day.sh'
    #     sh = sh.replace('path',fo)
    #     sh = sh.replace('ago', ago)
        
    #     sh = _str.do('sh',sh); _.saveText( sh, script );
    #     os.chmod( script, 0o777 )
    #     _.pr( script, c='Background.light_blue' )

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
                t2 = _.getText(path,raw=True)+'\n\n'+'##### --> timestamp#> '+_.isDate(time.time(),f='iso')+'\n\n'; txt=t2+txt;
            _.saveText( txt, path ); _.pr( path, c='cyan' )
        # return None
    if path.lower().endswith('.md'):
        crypt = True
        if not os.path.isfile(path):
            crypt = False; ask = input(' crypt doc: ');
            if 'y' in ask.lower(): crypt = True
        if crypt: _docs.switch('Files',path); _docs.action();
    _open.switch('Files',path); _open.action();

    # if not os.path.isfile(path):
    #     _.saveText()

def new_file_defaults(fi):
    global fo; global epoch;
    path=fo+fi
    if os.path.isfile(path): return None

    # if fi.endswith('.md'):
        



def action():
    _.pr( _v.fig, dic=1 ); return None;
    global epoch; global fo; load();

    if _.switches.isActive('Change-Dir'):

        if _.isWin:
            os.system('cd /d  "'+fo+'"')
            # os.chdir(fo)
        else:
            os.system('cd "'+fo+'"; $SHELL;')
        return None

    path = fo
    
    if _.switches.isActive('Fi'):
        for fi in _.switches.values('Fi'):
            files(fi)
            new_file_defaults(fi)
        return None
    no = path+'notes.md'
    _.pr(no,c='cyan')
    if not os.path.isfile(no): _.saveText('___\n# '+_.isDate(epoch,f='date')+'\n\n',no)
    _docs.switch('Files',no); _docs.action();
    
    if _.switches.isActive('Print'): _md.switch('View-Webpage'); _md.switch('Files',no); _md.action();

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
os=__.imp('os.system')
os=__.imp('os.chdir')

########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()




