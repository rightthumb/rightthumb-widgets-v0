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
    _.switches.register( 'Files', '-f,-fi,-file,-files', isRequired=True )
    _.switches.register( 'Clip', '-clip', isRequired=True )
    # _.switches.register( 'Save', '-save', isRequired=True )
    pass
    ### EXAMPLE: START
    # _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
    ### EXAMPLE: END

# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('require-list',[])
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


### EXAMPLE: END
########################################################################################
# START

def timex(string):
    t=_.dot(); t.a='0'; t.b='0'; t.c='__'+string.replace(':','.');
    p=string.split('-')
    if p[0].count(':') == 1:
        tas=p[0].split(':')[1]
        t.a=str(  (int(p[0].split(':')[0])*60)+int(tas) )
    elif p[0].count(':') == 2:
        tas1=(int(p[0].split(':')[0])*60)*60
        tas2=(int(p[0].split(':')[1])*60)
        tas3=int(p[0].split(':')[2])
        t.a=str( tas1+tas2+tas3  )
    if p[0].count(':') == 1:
        tbs=p[1].split(':')[1]
        t.b=str(  (int(p[1].split(':')[0])*60)+int(tbs) )
    elif p[1].count(':') == 2:
        tas1=(int(p[1].split(':')[0])*60)*60
        tas2=(int(p[1].split(':')[1])*60)
        tas3=int(p[1].split(':')[2])
        t.b=str( tas1+tas2+tas3  )
    return t

def action():
    global  c3po
    #--> min, architecture {:strict:}
    # s=_.switches.values('Save')[0]
    # tt=
    # print(tt)
    for t2 in _.switches.values('Clip'):
        t=timex(t2)
        for i, path in enumerate( _.switches.values('Files') ):
            if os.path.isfile(path):
                info=_dir.info(path)
                fx='ffmpeg -i ff1 -ss aaa -t bbb -acodec copy -vcodec copy ff2'.replace('aaa',t.a).replace('bbb',t.b).replace('ff1',info['name']).replace('ff2','clip-'+str(_.HID('ffmpeg-clip'))+'-'+info['name'].replace('.'+info['ext'].lower(),'').replace('.'+info['ext'].upper(),'').replace('.'+info['ext'],'')+t.c+'.'+info['ext'])
                _.pr(fx)
        del t
def load():
    global  c3po

os=_.imp('os.sep')
import _rightThumb._dir as _dir
"""
p ffmpeg-clip -f piller-10-2.mp4 -clip "0:38-7:03" | p execute
p ffmpeg-clip -f piller-01.mp4 -clip "4:38-7:24 11:26-13:35 17:54-19:30" | p execute
p ffmpeg-clip -f piller-02.mp4 -clip "0:04-2:20 9:53-12:28 27:37-30:06 32:27-32:55" | p execute
p ffmpeg-clip -f piller-03.mp4 -clip "24:57-27:02 44:12-45:33" | p execute
p ffmpeg-clip -f piller-04.mp4 -clip "4:00-6:20 10:38-13:25 26:10-29:28" | p execute
p ffmpeg-clip -f piller-05.mp4 -clip "29:07-32:16 45:40-47:05 48:10-48:20" | p execute
p ffmpeg-clip -f piller-07-1.mp4 -clip "57:03-1:01:02" | p execute
p ffmpeg-clip -f piller-07-2.mp4 -clip "13:51-16:20 28:19-30:47 40:45-43:58" | p execute
p ffmpeg-clip -f piller-09.mp4 -clip "28:46-32:08 44:51-45:26" | p execute
p ffmpeg-clip -f piller-10-1.mp4 -clip "1:45-4:53" | p execute
p ffmpeg-clip -f piller-10-2.mp4 -clip "1:13-6:29 33:20-37:15 50:52-54:55 1:02:39-1:03:47" | p execute

p ffmpeg-clip -f piller-11.mp4 -clip "28:46-31:57 43:25-45:22" | p execute
p ffmpeg-clip -f piller-12-1.mp4 -clip "18:05-20:31 55:01-57:57" | p execute
p ffmpeg-clip -f piller-12-2.mp4 -clip "9:21-12:31 26:24-28:56 43:29-46:28" | p execute
p ffmpeg-clip -f piller-13.mp4 -clip "28:50-32:10 43:58-45:26 49:51-53:33" | p execute

p ffmpeg-clip -f piller-14-1.mp4 -clip "10:42-13:40" | p execute
p ffmpeg-clip -f piller-14-2.mp4 -clip "4:55-8:11 23:55-27:06 29:54-32:39" | p execute

p ffmpeg-clip -f piller-15.mp4 -clip "5:52-6:34 53:32-54:50" | p execute
p ffmpeg-clip -f piller-16.mp4 -clip "59:37-1:02:30 1:24:45-1:27:59" | p execute
p ffmpeg-clip -f piller-17.mp4 -clip "1:23:33-1:26:56 1:31:50-1:32:55" | p execute
"""


########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()





