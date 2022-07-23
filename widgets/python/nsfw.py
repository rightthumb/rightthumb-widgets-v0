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
    _.switches.register( 'On', '-on' )
    _.switches.register( 'Off', '-off' )
    _.switches.register( 'Status', '-status' )
    pass
    ### EXAMPLE: START
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
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
    'file': 'thisApp.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Changes the world',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'DEFAULT',
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
                        _.hp('p thisApp -file file.txt'),
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

#b)--> examples
#d)--> code hints to quickly get started
    #n)--> inline examples
        # if _.switches.isActive('Test'): test(); return None;
        # result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
        # bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
        # a=(1 if True else 0) <--# 
        #!)--> m=[[row[i] for row in matrix] for i in range(4)]

    #n)--> python globals
        # for k in globals(): print(k, eval(k) )

    #n)--> webpage from url
        # requests=__.imp('requests.post')
        #!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

    #n)--> import and backup example
        # _bk = _.regImp( focus(), 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
        # _bk.switch( 'Input', path ); bkfi = _bk.action();
#e)--> examples

### EXAMPLE: END
########################################################################################
# START

os=__.imp('os.path.getmtime')

def action():
    should_dl=False
    if not _.switches.isActive('On') and not _.switches.isActive('Off'):
        if not os.path.isfile(_v.rtp+'vars'+os.sep+'nsfw'): should_dl=True, _.pr('cached: does not exist',c='red')
        else:
            _.pr('cached: ',_.isDate(os.path.getmtime(_v.rtp+'vars'+os.sep+'nsfw'),f='ago-txt'),c='yellow')
            diff=time.time()-os.path.getmtime(_v.rtp+'vars'+os.sep+'nsfw')
            if diff > 14415: should_dl=True; _.pr('stale',c='red');
        if not should_dl:
            _.pr('cache valid',c='green');
            if '1' in _.getText(_v.rtp+'vars'+os.sep+'nsfw',raw=True): nsfw=True
            else: nsfw=False
        if should_dl:
            _.pr('downloading',c='green');
            try:
                if '1' in _.URL('https://eyeformeta.com/apps/terminal/status/nsfw'): nsfw=True;
                else: nsfw=False;
            except Exception as ee: nsfw=False;
            if nsfw: _.saveText('1',_v.rtp+'vars'+os.sep+'nsfw')
            else:    _.saveText('0',_v.rtp+'vars'+os.sep+'nsfw')
        
        if nsfw: _.pr('nsfw ON',c='Background.red')
        else: _.pr('nsfw OFF',c='Background.red')
        return None
    if _.switches.isActive('On'):
        _.URL('https://eyeformeta.com/apps/terminal/status/?n=nsfw&v=1')
        _.saveText('1',_v.rtp+'vars'+os.sep+'nsfw')
        _.pr('nsfw ON',c='Background.red')
    else:
        _.URL('https://eyeformeta.com/apps/terminal/status/?n=nsfw&v=0')
        _.saveText('0',_v.rtp+'vars'+os.sep+'nsfw')
        _.pr('nsfw OFF',c='Background.red')




########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()





