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
import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
##################################################


def sw():
    pass
    #b)--> examples
    _.switches.register( 'Convert', '-cv,-convert', '.py .js or "# Python 3" "# JavaScript"' )
    _.switches.register( 'Requests', '-r', 'Get news from an rss feed' )
    _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files' )
    #e)--> examples

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])
_requests_i=0

def getSentenceCase(source: str):
    output = ""
    isFirstWord = True
    for c in source:
        if isFirstWord and not c.isspace():
            c = c.upper()
            isFirstWord = False
        elif not isFirstWord and c in ".!?":
            isFirstWord = True
        else:
            c = c.lower()
        output = output + c
    return output
_requests_bk=[]
scriptTrigger=True
def _requests(data):
    global scriptTrigger
    if not type(data) == str: return data
    if scriptTrigger: global _requests_bk; _requests_bk.append(data);
    if not data: return data
    while data.endswith(' '): data=data[:-1]
    while data.startswith(' '): data=data[1:]
    if not data: return data
    global _requests_i
    _requests_i+=1
    if not data[0] in '0123456789':
        data=str(_requests_i)+' '+data
    if not data.endswith('.'):
        data+='.'
    return getSentenceCase(data)

def _convert(data):
    if not type(data) == str: return data
    if not data: return data
    while data.endswith(' '): data=data[:-1]
    while data.startswith(' '): data=data[1:]
    if not data: return data
    if data[0] == '#': return getSentenceCase(data)

    if data in '.py py py3 .py3': return '# Python 3' 
    if data in '.py2 py2': return '# Python 2' 
    if data in '.js js javascript JavaScript': return '# JavaScript' 
    if data in 'c': return '# JavaScript' 

    return getSentenceCase(data)


_.appInfo[focus()] = {
    # 'app': '8facG-jo0Cxk',
    'file': 'bot.py',
    'liveAppName': __.thisApp( __file__ ),
    'description': 'GPT-3 openai API interaction',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'GPT',
                        'openai',
                        'API',
                        'GPT-3',
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
                        _.hp('p bot -r '),
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
    _.switches.trigger( 'Convert', _convert )
    _.switches.trigger( 'Requests', _requests )
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    # _.switches.trigger( 'Ago', _.timeAgo )
    # _.switches.trigger( 'Folder', _.myFolderLocations )
    # _.switches.trigger( 'URL', _.urlTrigger )
    # _.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
scriptTrigger=False

########################################################################################
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
        # _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
        # _bk.switch( 'Input', path ); bkfi = _bk.action();

    #n)--> inline
        # for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

    #n)--> banner
        # banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

# https://beta.openai.com/playground/p/default-text-to-command?model=text-davinci-002

import os
import openai
openai.api_key = _blowfish.decrypt(  '3cH4NSWCVF8FWsrXyFleWGuRw7rl80It4Qksu3xT/KPUyQKZC+AzxWlDU6ClZn8aaw0+4NlfxUU='  , _vault.key() )

def runSomeCode():
    # if isData():
    #     prompt="\"\"\"\n"+ '\n'.join(_.switches.values('Requests')) +"\n"+ '\n'.join(isData()) +"\n\"\"\"",
    # else:
    prompt="\"\"\"\n"+ '\n'.join(_.switches.values('Requests')) +"\n\"\"\"",

    response = openai.Completion.create(
        engine="text-davinci-002",
        # engine="text-babbage-001",
        # engine="text-curie-001",
        # engine="text-ada-001",
        prompt=prompt,
        temperature=0,
        # max_tokens=1500,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    if 'choices' in response:
        x = response['choices']

    if len(x) > 0:
        return x[0]['text']
    else:
        return ''


def action():
    # _requests_bk=[]
    answer = runSomeCode()
    print(answer)



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


.._copy = _.regImp( __.appReg, '-copy' )
_copy.imp.copy(  )

import _rightThumb._dir as _dir
_copy = _.regImp( __.appReg, '-copy' )
_copy.imp.copy(  )