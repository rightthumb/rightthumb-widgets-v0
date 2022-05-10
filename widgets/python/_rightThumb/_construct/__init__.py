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

import time,signal,sys,platform
tz = str(time.strftime("%z")).replace(':','')
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

try:
    importlib
except Exception as e:
    importlib = None

autoCreationConfiguration = {
                            'backup': True,
                            'logs': True,
                            'folders': True,
                            'created': { '_vars': 0 },
}

settings_table = {
                    'receipt-log': True,
                    'receipt-file': True,
}

class dot:
    def __init__( self ):
        pass
fn=dot()

def settings( subjects, d=None, val='71e9-a678' ):
    results = []
    for subject in subjects:
        results.append(  setting( subject, val, d )  )
    return results

def setting( subject, val='71e9-a678', d=None, default=None ):
    global settings_table

    if not default is None:
        d = default

    if not val == '71e9-a678':
        settings_table[subject] = val

    if not subject in settings_table:
        return d
    
    return settings_table[subject]


releaseAcquiredData = True

table_b_print = False

switch_raw = []


thisOS = platform.system()
theOS = thisOS
OS = theOS
windowsSlash = chr(92)
unixSlash = chr(47)

if thisOS == 'Windows':
    slash = windowsSlash
    isWin  = True
else:
    slash = unixSlash
    isWin  = False

class dot:
    def __init__( self ):
        pass

v = dot()

LOOP = {}

def pathList( *paths ):
    # os = imp('os')
    result = os.sep.join(paths)
    result = result.replace( '/', os.sep )
    result = result.replace( '\\', os.sep )
    result = result.replace( os.sep+os.sep, os.sep )
    result = result.replace( os.sep+os.sep, os.sep )
    result = result.replace( 'tech'+os.sep+'tech', 'tech' )
    return result

def p( *text, w='' ):
    texXxt = []
    for x in text:
        texXxt.append(str(x))
    txt = ' '.join( texXxt )
    
    if w:
        # os = imp('os')
        if os.path.isfile(w):
            file1 = open( w , 'a' )
            file1.write( txt+'\n' )
            file1.close()
        else:
            file1 = open( w , 'w' )
            file1.write( txt+'\n' )
            file1.close()
    print(txt)



def xit():
    sys.exit()

specifications = {}
did_table = {}
def uuid():
    UUID = imp('uuid')
    return str(UUID.uuid4())



def dots(path):
    def _dots_(pth):
        try: exec(pth); return True;
        except Exception as e: return False;
    rts=path.split('.'); exec('global '+rts[0]);
    if _dots_(path): return eval(rts[0])
    pre=[]; thp=[];
    for i,seg in enumerate(rts):
        pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
        if i == len(rts)-1:
            exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
            f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
        else: f='1=dot()'.replace('1',npath);

        if not _dots_(npath):
            exec(f)
            if i == len(rts)-1: return eval(rts[0]);



imp_table = {}
def imp( subject, imp_table_testing=False ):
    # print(subject); sys.exit();
    if '.' in subject and not '_rightThumb' in subject: return dots(subject);
    global imp_table
    global importlib
    if importlib is None:
        import importlib
        if imp_table_testing:
            print('\n\n\t\timport importlib\n\n')

    if not subject in imp_table:
        try:
            imp_table_tmp
        except Exception as e:
            pass
        else:
            del imp_table_tmp



        try:
            imp_table[subject] = importlib.import_module(subject)
            if imp_table_testing:
                print( 'imp.DID' )
            return imp_table[subject]
        except Exception as e:
            if imp_table_testing:
                print( 'imp.NO' )
            return None
    if imp_table_testing:
        print( 'imp.YES' )
    return imp_table[subject]



on_exit_subjects = {}
def onExit(script,subject=None):
    global on_exit_subjects
    if subject is None:
        subject = uuid()
    on_exit_subjects[subject] = script

def isExit():
    global on_exit_subjects
    for subject in on_exit_subjects:
        on_exit_subjects[subject]()


def path( p, ab=True, pop=False, file=False, slash=None ):
    # os = vc.FIG.imp('os')
    # os = imp('os')
    if slash is None:
        slash = os.sep
    if not p:
        return p.replace(os.sep+os.sep,os.sep)
    # print(p)
    p = p.replace( chr(92), slash )
    p = p.replace( chr(47), slash )
    while slash+slash in p:
        p = p.replace(slash+slash,slash)
    if ab:
        try:
            p = os.path.abspath(p)
        except Exception as e:
            pass
    try:
        p = os.path._getfinalpathname(p).lstrip(r'\?')
    except Exception as e:
        pass
    if type(p) == str and p[1] == ':':
        p = p[0].upper() + p[1:]
    if type(p) == str and ( pop or file ):

        if type(pop) == int:
            i=0
            while not i == pop:
                i+=1
                p = path( p, pop=True, slash=slash )
                # print(p)
            if file:
                p = path( p, file=True, slash=slash )
            return p.replace(os.sep+os.sep,os.sep)
        parts = p.split(slash)
        parts.reverse()
        f = parts.pop(0)
        parts.reverse()
        p = str(slash).join(parts)
        if file:
            p = f
    return p.replace(os.sep+os.sep,os.sep)

def file( p ):
    # os = imp('os')
    p = p.replace( chr(92), os.sep )
    p = p.replace( chr(47), os.sep )
    if not os.sep in p:
        return p
    parts = p.split(os.sep)
    parts.reverse()
    f = parts.pop(0)
    return f


def getTable( file ):
    # os = imp('os')
    json = imp('simplejson')

    if os.path.isfile(file):
        with open(file,'r', encoding="latin-1") as json_file:
            json_data = json.load(json_file)
    else:
        json_data = data_default(file=file,default=[]).default()
    return json_data

def saveTable( data, file, sk=False ):
    json = imp('simplejson')
    dataDump = json.dumps(data, indent=4, sort_keys=sk)

    f = open(file,'w')
    f.write(str(dataDump))
    f.close()


pre_error = False
class Table_Aggregates:
    def __init__( self ):
        self.triggers = {}
    def trigger( self, label, script ):
        self.triggers[label] = script
    def run( self, label, data ):
        return self.triggers[label](data)
table_aggregates = Table_Aggregates()


payloadCache = None
varFoldersCheck = False
myFileLocations_SKIP_VALIDATION = False





"""
__.autoCreationConfiguration['backup']
__.autoCreationConfiguration['logs']
__.autoCreationConfiguration['folders']
"""

# import importlib
try:
    startTime
except Exception as e:
    startTime = time.time()
    
trigger_isPipe = False
isRequired_Pipe = False
isRequired_Pipe_or_File = False
isRequired_or_List = None
isRequired_index = {}
switchList = []
appRegPipe = None
cls_process_switches_help = False

storyboard = []
# __.sbd( fn=sys._getframe().f_code.co_name, d='' )
def sbd( location=1, line=0, fn='', d='' ):
    # add to auto documentation
    global storyboard
    global switchList
    function = fn
    activeSwitches = ''
    inactiveSwitches = ''
    documentation = n

    storyboard.append({ 'timestamp': time.time(), 'function': function, 'active': activeSwitches, 'inactive': inactiveSwitches })


def triggerTest( data ):
    return 'test'

def clearFocus( name, file ):
    global slash
    f = file.split(slash)
    if name == '__main__':
        x = '__' + f[len(f)-1].replace('.py','') + '__'
    else:
        x = f[len(f)-1].replace('.py','')
    return x

def thisApp( file ):
    global slash
    f = file.split(slash)
    x = f[len(f)-1].replace('.py','')
    return x





# delimReg = '_'
delimReg = '_-_'

appReg = ''

registeredApps = []
registeredAppsAll = []

threadQueue = {}

def constructRegistration( file, dba ):
    global registeredAppsAll
    shouldAdd = True
    for ra in registeredAppsAll:
        if ra['dba'] == dba:
            shouldAdd = False
    if shouldAdd:
        registeredAppsAll.append({ 'file': file, 'dba': dba })

def constructApps():
    global registeredAppsAll
    for appreg in registeredAppsAll:
        print(appreg)

def appName( appReg, parentApp='', childApp='' ):
    global delimReg
    global isRequired_index
    if not parentApp == '':
        appReg = appReg + delimReg + parentApp
    if not childApp == '':
        appReg = parentApp + delimReg + appReg
    isRequired_index[appReg] = []
    return appReg

def structure():
    result = []
    global registeredAppsAll
    for raa in registeredAppsAll:
        if type(raa) == dict:
            result.append(raa)
            # print(raa)
    return result

theDelim = '|||'
appInfoScan = False # appInfo.py



# import blank
# blank.focus(focus())
# _.load()
# blank.registerSwitches()
# _.switches.process()
# _.switches.fieldSet('Input','active',True)
# _.switches.fieldSet('Input','value','one')

# _.appInfo[blank.focus(focus())] = _.appInfo[blank.focus()]
# _.appData[blank.focus(focus())] = _.appData[blank.focus()]
# __.constructRegistration(_.appInfo[blank.focus(focus())]['file'],blank.focus(focus()))


class data_default:
    # __.data_default(file=theFile,default=[])
    def __init__( self, file, default ):
        self.dics = 'index,indexes,dex,ls,hash,hashes,tables,logs,lists,indices,meta,setting,settings,dic,s,fig,conf,cnf'
        self.lists = 'table,cache,log,list,json,config'
        self.file = file
        self.default_result = default
    def default( self ):

        for x in self.dics.split(','):
            if self.file.lower().endswith( '.'+x+'.json' ):
                return {}
        for x in self.lists.split(','):
            if self.file.lower().endswith( '.'+x+'.json' ):
                return []

        for x in self.dics.split(','):
            if self.file.lower().endswith( '.'+x ):
                return {}
        for x in self.lists.split(','):
            if self.file.lower().endswith( '.'+x ):
                return []
        return self.default_result
# return __.data_default(file=theFile,default=[]).default()


class file_headers:
    # __.data_default(file=theFile,default=[])
    def __init__( self, path, default='' ):
        self.watermark = '''
## {R2D2919B742E} ##
###########################################################################
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
   - Scott Taylor Reph, RightThumb.com
###########################################################################
## {C3P0D40fAe8B} ##

'''.replace('\r','')
        self.path = path
        self.headers = {
                            'functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
                            '_functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
                            '_fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
                            'fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
                            '.folder.meta':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.h'},
                            '.folder.meta.b':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.b'},
                            '.txt': '__________________________________________________________________________________\n',
                            '.sh': '#!/bin/bash\n',
                            '.py': '#!/usr/bin/python3\n',
                            '.bat': '@echo off\n',
                            '.html': {'url':'https://apps.eyeformeta.com/templates/html/0.htm'},
                            '.htm':  {'url':'https://apps.eyeformeta.com/templates/html/1.htm'},
                            '.php':  {'url':'https://apps.eyeformeta.com/templates/html/0.php.txt'},
        }
        self.comment = {
                            # '.js': '//',
                            '.sh': '#',
                            '.py': '#',
                            '.bat': 'rem',
        }
        # self.nospace=['.sh']
        self.nospace=[]
        self.default_result = default
    def add_watermark(self,code):
        for ext in self.comment:
            if self.path.endswith(ext):
                for line in self.watermark.split('\n'):
                    if len( line.replace(' ','').replace('\t','') ):
                        code+=self.comment[ext]+' '+line+'\n'
                    else:
                        code+='\n'
        for ext in self.nospace:
            if self.path.endswith(ext):
                import _rightThumb._string as _str
                code = code.replace('\r','')
                code = _str.cleanBE(code,' ')
                code = _str.cleanBE(code,'\n')
                code = _str.replaceDuplicate(code,'\n')
                code = _str.cleanBE(code,'\n')
                code = _str.cleanBE(code,' ')
                code+='\n'

        return code.replace('\r','')


    def default( self ):
        for ext in self.headers:
            if self.path.endswith(ext):
                if type(self.headers[ext]) == dict:
                    try:
                        import requests
                        page = requests.get(self.headers[ext]['url'])
                        return page.content.decode("utf-8").replace('\r','')
                    except Exception as e:
                        return self.add_watermark(self.default_result)
                        
                return self.add_watermark(self.headers[ext])
        return self.add_watermark(self.default_result)
# __.file_headers(path).default()


setting('myFileLocations-skip-validation',False)
setting('require-pipe',False)
setting('require-pipe||file',False)
setting('pre-error',False)
setting('switch-raw',[])
setting('require-list',[])
setting('receipt-log',True)
setting('receipt-file',True)

os = imp('os.system')
os = imp('os.sep')
os = imp('os.path.abspath')
os = imp('os.path.isfile')
os = imp('os.path.isdir')
sys = imp('sys.exit')
# import os

def url( URL, data={}, d=None, raw=False, r=None ):
    import _rightThumb._string as _str
    def _url_(data): return _str.do('.sh',data);

    if not r is None: raw=r;
    if not d is None: data=d;
    page=imp('requests.post').post(URL, data = data)
    if raw: return page;
    result=page.content
    for encodeing in 'ISO-8859-1 UTF-8 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
        try: return _url_(str(result,encodeing));
        except Exception as e: pass;
    return _url_(str(result))
page=url
