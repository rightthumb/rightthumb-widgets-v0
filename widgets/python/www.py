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
    _.switches.register( 'Text', '-t,-text,-txt' )
    _.switches.register( 'URL', '-url', 'https://www.google.com/', isRequired=True )

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
    'file': 'www.py',
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
                        _.hp('p www -url https://www.google.com/'),
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

def url_port(url):
    url=url.replace(' ','')
    if not url.endswith('/'):
        url=url+'/'
    try:
        domain=url.split('//')[1].split('/')[0]
        if ':' in domain:
            return int(domain.split(':')[1])
    except Exception as e:
        return 80
    return 80


def action():
    url=_.switches.value('URL')
    port=url_port(url)

    if not _.switches.isActive('Text'):
        page=__.url( url, text=_.switches.isActive('Text') )
        _.pr(page)
        return None

    requests=__.imp('requests.get')
    
    # html = urlopen(url).read()
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}
    # response=requests.get(url, headers=headers,port=port)
    response=requests.get(url, headers=headers)
    webpage = response.content

    soup = BeautifulSoup(webpage,features="lxml")

    for script in soup(["script", "style"]):
        script.decompose()
    # delete out tags


    strips = list(soup.stripped_strings)
    _.linePrint()
    _.pr( '\n'.join(strips) )
    # _.pr(strips[:5])

# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# import urlopen
from bs4 import BeautifulSoup

########################################################################################
if __name__ == '__main__':
    action()
    __.isExit()




