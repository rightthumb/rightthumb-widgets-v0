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
    #b)--> examples
    _.switches.register( 'Match', '-m', 'D:\\websites\\backup\\RightThumb.com\\public_html\\Beth.gif  /home/rightthumb/public_html/Beth.gif' )
    # _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
    #e)--> examples
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
    # 'app': '8facG-jo0Cxk',
    'file': 'files-compare.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Changes the world',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'lists',
                        'compare',
                        'data',
                        'files',
                        'paths',
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
                        _.hp('p files-compare  -f   local-8131.txt  yavin-8124.txt    -m  D:\\websites\\backup\\RightThumb.com\\public_html\\Beth.gif  /home/rightthumb/public_html/Beth.gif'),
                        _.hp(''),
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

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
    #n)--> inline examples
        # any(ele in 'scott5' for ele in list('0123456789'))
        # if _.switches.isActive('Test'): test(); return None;
        # result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
        # bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
        # a=(1 if True else 0) <--# 
        #!)--> m=[[row[i] for row in matrix] for i in range(4)]

    #n)--> python globals
        # globals()['var']
        # for k in globals(): print(k, eval(k) )

    #n)--> webpage from url
        # for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

    #n)--> webpage from url
        # requests=__.imp('requests.post')
        #!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

    #n)--> import and backup example
        # _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
        # _bk.switch( 'Input', path ); bkfi = _bk.action();
    
    #n)--> inline
        # for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

    #n)--> banner
        # banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def action():
    clean=[]
    if _.switches.isActive('Match'):
        match = []
        for m in _.switches.values('Match'):
            while '\\\\' in m: m = m.replace('\\\\','\\')
            m = m.replace('\\','/')
            m = m[::-1]
            match.append(m)

        i=-1
        for c in m:
            i+=1
            try:
                if not match[0][i] == match[1][i]: break
            except: break

        for m in match:
            # print(m)
            y = m[i:]
            y = y[::-1]+'/'
            if y[1] == ':': y=y.replace('/','\\')
            clean.append(y)

        


    indexes={}
    for i,path in enumerate(_.switches.values('Files')):
        indexes[i]={}
        indexes[i][0]=_.getText(path,raw=True,clean=2).split('\n')
        indexes[i][1]=[]
        for li in indexes[i][0]:
            # print(li)
            for c in clean:
                if li.startswith(c): li=li[len(c):]
            indexes[i][1].append(li.replace('\\','/'))

    lsts=[]
    for i in indexes: lsts.append(indexes[i][1])
    
    main_list=[]
    if len(lsts) == 2: main_list = list(set(lsts[0]) - set(lsts[1]))
    if len(lsts) == 3: main_list = list(set(lsts[0]) - set(lsts[1]) - set(lsts[2]))
    if len(lsts) == 4: main_list = list(set(lsts[0]) - set(lsts[1]) - set(lsts[2]) - set(lsts[3]))


    for li in main_list:
        for i in indexes:
            if li in indexes[i][1]:
                print(  indexes[i][0][  indexes[i][1].index(li)  ]  )

    # for i in indexes: lsts.append(indexes[i][1])

        
    


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
    #b)--> examples

    # banner.pr()
    # if len(_.switches.all())==0: banner.gossip()
    
    #e)--> examples
    action()
    _.isExit(__file__)

