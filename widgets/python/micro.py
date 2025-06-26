#!/usr/bin/python3

loader='''#!/usr/bin/python3

import sys

if not sys.stdin.isatty():
    RawPipe = sys.stdin.read()
    if type(RawPipe) == str: RawPipe = RawPipe.split('\\n')
else:
    RawPipe = False



import os,sys,time,importlib,simplejson
if sys.platform[0] == 'w': figpath=os.getenv('USERPROFILE') +os.sep+'.rt'+os.sep+ '.config.hash'
else: figpath=os.getenv('HOME') +os.sep+'.rt'+os.sep+ '.config.hash'

def yamlSimp(yaml_string):
    table = {}
    lines = yaml_string.split('\\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            table[key.strip()] = value.strip()
        return table


def get_first_char(filename):
     with open(filename, 'r') as file: first_char = file.read(1)
     return first_char


def get_file_content(filename):
     with open(filename, 'r') as file: content = file.read()
     return content


def getTable( file ):
    if not get_first_char(file) == '{' and  not get_first_char(file) == '[':
        return yamlSimp(get_file_content(file))
    json_data={}
    if os.path.isfile(file):
        with open(file,'r', encoding="latin-1") as json_file: json_data = simplejson.load(json_file)
    return json_data


fig=getTable(figpath)
sys.path.append( fig['w']+'/widgets/python'.replace('/',os.sep) )




import _rightThumb._construct as __

__.Pipe = RawPipe

try:
    name__ = __name__
except:
    name__ = '__main__'

try:
    file__ = __file__
except:
    if os.path.isfile('/opt/rightthumb-widgets-v0/widgets/python/micro.py'):
        file__ = '/opt/rightthumb-widgets-v0/widgets/python/micro.py'
    elif os.path.isfile('D:\\.rightthumb-widgets\\widgets\\python\\blank-micro.py'):
        file__ = 'D:\\.rightthumb-widgets\\widgets\\python\\blank-micro.py'
    elif os.path.isfile(figpath+os.sep+'rightthumb-widgets-v0' +os.sep+ 'widgets' +os.sep+ 'python' +os.sep+ 'micro.py'):
        file__ = figpath+os.sep+'rightthumb-widgets-v0' +os.sep+ 'widgets' +os.sep+ 'python' +os.sep+ 'micro.py'
    else:
        file__ = '/opt/rightthumb-widgets-v0/widgets/python/micro.py'


__.appReg = __.clearFocus( name__, file__ )


appDBA = __.appReg
import _rightThumb._base3 as _

def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f


fieldSet=_.l.vars(focus(),name__,file__,appDBA)


_.load()
_v=__.imp('_rightThumb._vars')

import _rightThumb._vars as _v
import _rightThumb._matrix as _matrix
import _rightThumb._base3 as _
_.raq_err=False
_.load()
import _rightThumb._base4 as ___
import _rightThumb._string as _str
import _rightThumb._dir as _dir

_.appInfo[focus()] = {
    # 'app': '8facG-jo0Cxk',
    'file': 'thisApp2.py',
    'liveAppName': 'thisApp2',
    'description': 'Changes the world',
        # _.ail(1,'subject')+
        # _.aib('one')+
    'categories': [
                        'DEFAULT',
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
    'aliases': [],
    'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

__.appReg = __.clearFocus( name__,file__ )

f = __.appName( __.appReg, '', '' )
__.registeredApps.append( __.appReg )


try:
    switches
except:
    def switches(): pass

_._default_settings_()

def triggers():
    _._default_triggers_()
    _.switches.trigger( 'Files', _.myFileLocations, vs=True )
    _.switches.trigger( 'Ago', _.timeAgo )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    _.switches.trigger( 'URL', _.urlTrigger )
    _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)

_.l.conf('appDBA',__.appReg);
_.l.conf('clean-pipe',True); _.l_registerSwitches( triggers, switches );

#_.appInfo[__.appReg] = {"file": "thisApp2.py", "liveAppName": "thisApp2", "description": "Changes the world", "categories": [""], "usage": [], "relatedapps": [], "prerequisite": [], "examples": [""], "columns": [], "aliases": [], "notes": []}
_.appData[__.appReg] = {"start": __.startTime, "uuid": "", "audit": [], "pipe": False, "data": {"field": {"sent": [], "received": []}, "table": {"sent": [], "received": []}}}

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
_.defaultScriptTriggers()
_.switches.process()
_.argvProcess = True
_.postLoad( 'D:\\tech\\hosts\\VULCAN\\widgets\\python\\base-e.py' )

# fileBackup = _.regImp( __.appReg, 'fileBackup' )
# fileBackup.switch( 'Silent,isRunOnce,DoNotSchedule,Flag', 'dirty' )
# fileBackup.switch( 'Input',  _.f('appData',2)  )
# fileBackup.action()

# imp = importlib.import_module(app)
# _.wrapText(  ' '.join(  _.files(  _.back()  )  )  )
# _.f()
# _.f('secure',1)
# _.f('appData',2)
# _.f(p=1)
# _.printVarSimple(  _dir.info(  _.f( 'secure', r=1 )  )  )
# os.system('cls')
# _.pr( str( '\\n'.join( dir(_v) )  ) )
'''