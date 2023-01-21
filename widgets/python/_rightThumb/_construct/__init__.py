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

banner=None


def name(path):
    path=path(path)
    par=path.split(os.sep)
    par.reverse()
    app=par[0]
    fo=par[1]
    root=par[2]
    app=app.replace('.py','')
    if app == '__init__': app=root+'.'+fo
    return app


autoCreationConfiguration = {
                            'backup': False,
                            'logs': True,
                            'folders': True,
                            'created': { '_vars': 0 },
}

settings_table = {
                    #t)--> edit: 1661227949.7667239
                    'receipt-log': False,
                    'receipt-file': False,
}

class Meta_Namespace():
    def __init__( self ):
        pass
dot=Meta_Namespace
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


try:
    importlib
except Exception as e:
    importlib = None
imp_table = {}
def imp( subject, imp_table_testing=False ):
    try:
        return imp_run( subject, imp_table_testing )
    except:
        imp_install(subject)
        return imp_run( subject, imp_table_testing )

def imp_install(mod):
    mod = mod.split('.')[0]
    try:
        exec('import os')
    except Exception as e:
        raise e
    print()
    print('__.imp_install('+mod+')')
    print()
    if '.' in mod: mod = mod.split('.')[0]

    dic = {
            'all': {},
            'win': {},
            'linux': {},
    }

    dic['win']['magic'] = 'python-magic-bin==0.4.14'
    dic['linux']['magic'] = 'python-magic'

    if       sys.platform == 'win32' and mod in dic['win']: mod = dic['win'][mod]
    elif not sys.platform == 'win32' and mod in dic['linux']: mod = dic['linux'][mod]
    elif mod in dic['linux']: mod = dic['all'][mod]


    if mod in dic: mod=dic[mod]

    os.system('pip3 install '+mod+' >nul 2>&1')
    
    # if sys.platform == 'win32':
    #     # os.system('pip3 install python-magic-bin==0.4.14')
    #     os.system('pip3 install '+mod+' >nul 2>&1')
    # else:

    #     def _pipy_(mod):
    #         mod0=mod
    #         try:
    #             import pip
    #             if '=' in mod: mod = mod.split('=')[0]
    #             pip.main(['install', mod])
    #         except: print('pip3 install '+mod0)
    #     import subprocess
    #     if len(subprocess.getoutput('sudo cat /etc/sudoers').split('\n')) > 3:
    #         try: os.system('sudo pip3 install '+mod+'  > /dev/null 2>&1')
    #         except: _pipy_(mod)
    #     else:
    #         try: os.system('pip3 install '+mod+'  > /dev/null 2>&1')
    #         except:_pipy_(mod)




def imp_run( subject, imp_table_testing=False ):
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

        imp_table[subject] = importlib.import_module(subject)
        if imp_table_testing:
            print( 'imp.DID' )
        return imp_table[subject]

        # try:
        #     imp_table[subject] = importlib.import_module(subject)
        #     if imp_table_testing:
        #         print( 'imp.DID' )
        #     return imp_table[subject]
        # except Exception as e:
        #     if imp_table_testing:
        #         print( 'imp.NO' )
        #     return None
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


def path( p, ab=True, pop=False, file=False, slash=None, folder=None, fi=None, fo=None, fix=True ):
    p_bk=p
    # fix used in fileBackup.py

    if not fo is None: pop=True;
    if not folder is None: pop=True;
    if not fi is None: file=True;


    # os = vc.FIG.imp('os')
    # os = imp('os')
    os=imp('os.sep')
    try: os.path.abspath
    except Exception as e: os=imp('os.path.abspath')
    try: os.path.isfile
    except Exception as e: os=imp('os.path.isfile')
    try: os.path.isdir
    except Exception as e: os=imp('os.path.isdir')

    global isWin
    if not isWin:
        if p.startswith('/'):
            if   os.path.isdir(p): return p
            elif os.path.isfile(p): return p

    if ab:
        if os.path.isfile(p) or os.path.isdir(p):
            try:
                p = os.path.abspath(p)
            except Exception as e:
                pass

    if fix and not os.path.isfile(p) and not os.path.isdir(p) and not os.sep in p and p:
        p = os.getcwd() +os.sep+ p
        return p



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
        if os.path.isfile(p) or os.path.isdir(p):
            try:
                p = os.path.abspath(p)
            except Exception as e:
                pass
    if isWin:
        try:
            os=imp('os.path._getfinalpathname')
            p = os.path._getfinalpathname(p).lstrip(r'\?')
            # print(p)
        except Exception as e:
            # print(e)
            pass
    if p_bk[1] == ':' and not p[1] == ':': p = p_bk
    if type(p) == str and len(p)>1 and p[1] == ':':
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
        self.dics = 'yml yaml i index indexes dex ls hash hashes tables logs lists indices meta setting settings dic s fig conf cnf'
        self.lists = 't tbl table cache log list lists l json config'
        while '  ' in self.dics:  self.dics  = self.dics.replace('  ',' ')
        while '  ' in self.lists: self.lists = self.lists.replace('  ',' ')
        self.file = file
        self.default_result = default
    def default( self ):

        for x in self.dics.split(' '):
            if self.file.lower().endswith( '.'+x+'.json' ):
                return {}
        for x in self.lists.split(' '):
            if self.file.lower().endswith( '.'+x+'.json' ):
                return []

        for x in self.dics.split(' '):
            if self.file.lower().endswith( '.'+x+'.yml' ):
                return {}
        for x in self.lists.split(' '):
            if self.file.lower().endswith( '.'+x+'.yml' ):
                return []

        for x in self.dics.split(' '):
            if self.file.lower().endswith( '.'+x+'.yaml' ):
                return {}
        for x in self.lists.split(' '):
            if self.file.lower().endswith( '.'+x+'.yaml' ):
                return []

        for x in self.dics.split(' '):
            if self.file.lower().endswith( '.'+x ):
                return {}
        for x in self.lists.split(' '):
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

#--> todo#> create app to scan to fix this situation below


# import os

def url( URL, data={}, d=None, raw=False, r=None,txt=None,text=None,t=None, dic=None, get=None ):
    headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}
    if not txt is None: t=txt;
    if not text is None: t=text;
    import _rightThumb._string as _str

    if not r is None: raw=r;
    if not d is None: data=d;
    def _url_(data): return _str.do('.sh',data);
    # if not json is None and json:
    #     page=imp('requests.get').json(URL, headers=headers)
    #     return page
    if not get is None and get:

        page=imp('requests.get').get(URL, headers=headers)
        if raw: return page;
        if not t is None and t:
            result=page.text
        else:
            result=page.content
        for encodeing in 'UTF-8 ISO-8859-1 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
            try: return _url_(str(result,encodeing));
            except Exception as e: pass;
        return _url_(str(result))



    if not dic is None and dic:
        _dic={
            "href": "https://www.google.com/search?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
            "origin": "https://www.google.com",
            "domain": "google.com",
            "host": "www.google.com",
            "protocol": "https",
            "folder": "",
            "path": "google.com/search",
            "port": "443",
            "param": "?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
            "params": {},
            "username": "",
            "password": ""
        }

        return _dic



    page=imp('requests.post').post(URL, data = data)
    if raw: return page;
    if not t is None and t:
        result=page.text
    else:
        result=page.content
    for encodeing in 'ISO-8859-1 UTF-8 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
        try: return _url_(str(result,encodeing));
        except Exception as e: pass;
    return _url_(str(result))
page=url

print_=print
def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
    try: _str;
    except Exception as e:
        try: import _rightThumb._string as _str;
        except Exception as e: pass;
    if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
    # HD.chmod(theFile)
    lines = None
    if os.path.isfile(theFile):
        try:
            f = open(theFile, 'r', encoding='utf-8')
            lines = f.readlines()
            f.close()
        except Exception as e:
            try:
                f = open(theFile, 'r', encoding='latin-1')
                lines = f.readlines()
                f.close()
            except Exception as e:
                f = open(theFile, 'r')
                lines = f.readlines()
                f.close()
    else:
        if not e:
            return None
        print_('(getText) Error: No File')
        sys.exit()
    if raw:
        txt = ''.join( lines )
        # txt = txt.replace( _v.slash+'n', '\n' )

        if clean:
            txt = _str.replaceDuplicate( txt, '\n' )
            txt = _str.cleanBE( txt, '\n' )
        if clean == 2:
            txt = txt.replace( '\t', ' ' )
            txt = _str.replaceDuplicate( txt, ' ' )
            while '\n \n' in txt:
                txt = txt.replace( '\n \n', '\n' )
            txt = _str.replaceDuplicate( txt, '\n' )
            txt = _str.cleanBE( txt, '\n' )
        return txt
    elif c > 0:
        if c > 1:
            txt = ''.join( lines )
            TXT = ''
            txt = txt.replace( "'\"\"\"'", '' )
            if '"""' in txt:
                for i,item in enumerate(txt.split('"""')):
                    if i % 2 == 0:
                        TXT+=item
            elif not '"""' in txt:
                TXT = txt
            while '    ' in TXT:
                TXT = TXT.replace( '    ', '\t' )
            while ' (' in TXT:
                TXT = TXT.replace( ' (', '(' )
            while ' =' in TXT:
                TXT = TXT.replace( ' =', '=' )
            while '= ' in TXT:
                TXT = TXT.replace( '= ', '=' )
            while 'def  ' in TXT:
                TXT = TXT.replace( 'def  ', 'def ' )
            while 'class  ' in TXT:
                TXT = TXT.replace( 'class  ', 'class ' )
            lines = TXT.split('\n')

        newLines = []
        for i,row in enumerate(lines):
            # row = row.replace('\n','')
            row = row.replace('\r','')
            
            if not c > 1:
                newLines.append(row)
            else:
                row = row.split('#')[0]
                test = row
                # while test.startswith(' ') or test.startswith('\t'):
                #   test = _str.cleanBE( test, ' ' )
                #   test = _str.cleanBE( test, '\t' )
                if not test.startswith('#') and len(test):
                    newLines.append(row)


            


        return newLines

    elif clean:
        # lines = _str.replaceDuplicate( lines, '\n' )
        # lines = _str.cleanBE( lines, '\n' )
        for i,row in enumerate(lines):
            row = row.replace( '\n', '' )
            row = row.replace( '\r', '' )
            if type(clean) == int:
                row = row.replace( '\t', ' ' )
                row = _str.replaceDuplicate( row, ' ' )
                row = _str.cleanBE( row, ' ' )
            if clean == 3:
                row = ' ' + row + ' '

            # print_( row )
            lines[i] = row
        return lines
    else:
        return lines

os = imp('os.system')
os = imp('os.sep')
os = imp('os.listdir')
os = imp('os.getcwd')
os = imp('os.path.abspath')
os = imp('os.path.isfile')
os = imp('os.path.isdir')
os = imp('os.name')
os = imp('os.stat')
sys = imp('sys.exit')
