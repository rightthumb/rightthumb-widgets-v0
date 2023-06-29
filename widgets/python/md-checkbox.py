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
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
    _.switches.register( 'ID', '-id' )
    _.switches.register( 'Change-Status', '-status' )
    pass
    ### EXAMPLE: START
    # _.switches.register( 'Files', '-f,-fi,-file,-files' )
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
    'file': 'vps-cfarm-md-checkbox.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'Change checkbox status in markdown',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'md',
                        'markdown',
                        'editor',
                        'text',
                        '.md',
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
                        _.hp('p vps-cfarm-md-checkbox -id 1 -status off -f 2022-06-04.md'),
                        _.hp('p vps-cfarm-md-checkbox -id 1 -status on -f 2022-06-04.md'),
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

def change(md,i,to):
    ii=0
    md=md.replace('~~','~~~')
    md=md.replace('~~~~','~~~')
    md=md.replace('~~~~','~~~')




    md=md.replace('-[x]','- [x]')
    md=md.replace('-[x]','- [x]')
    md=md.replace('- [x]','- [x]')

    md=md.replace('-[ ]','- [ ]')
    md=md.replace('-[]','- [ ]')
    md=md.replace('- []','- [ ]')
    md=md.replace('- [ ]','- [ ] ')
    md=md.replace('- [ ]  ','- [ ] ')
    md=md.replace('- [ ]  ','- [ ] ')
    md=md.replace('- [ ]  ','- [ ] ')
    md=md.replace('- [x]','- [x] ')
    md=md.replace('- [x]  ','- [x] ')
    md=md.replace('- [x]  ','- [x] ')
    what0='[x],[-x],[-x-],[x-]'.upper()+',[x],[-x],[-x-],[x-],[ ],[-]'
    what=what0.split(',')
    lines=[]
    for line in md.split('\n'):
        for wha in what:
            if wha in line:
                ii=ii+1
                if i == ii:
                    _.pr(ii,line)
                    _.pr( i, to )
                    if to:
                        line=line.replace('- '+wha,'- [x]')
                    else:
                        line=line.replace('- '+wha,'- [ ]')
                _.pr(ii,line)

        lines.append(line)

    return '\n'.join(lines)




def action():
    #--> min, architecture {:strict:}
    #--> trigger/callback  <w#
    #--> todo#> meta to scan for
    load()
    global c3po
    
    i=int(_.switches.value('ID'))
    if 't' in _.switches.value('Change-Status') or 'y' in _.switches.value('Change-Status') or '1' in _.switches.value('Change-Status') or 'on' in _.switches.value('Change-Status'):
        to=True
    else:
        to=False
    
    _.saveText(change(c3po,i,to),_.switches.value('Files'))
    _.pr(_.switches.value('Files'))
    backup(_.switches.value('Files'))




def load():
    global c3po
    c3po = _.getText( _.switches.value('Files'), raw=True )
    _.pr(_.switches.value('Files'))
    
    #--> new table printer
    # _.pt(c3po)
def backup(path):
    appReg=__.appReg
    _bk = _.regImp( __.appReg, 'fileBackup' )
    _bk.switch( 'Silent' )
    _bk.switch( 'isPreOpen' )
    _bk.switch( 'Input', path )
    bkfi = _bk.action()
    __.appReg=appReg

########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()





