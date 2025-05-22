#!/usr/bin/python3

loader='''#!/usr/bin/python3
import os,sys,time,importlib,simplejson
if sys.platform[0] == 'w': figpath=os.getenv('USERPROFILE') +os.sep+'.rt'+os.sep+ '.config.hash'
else: figpath=os.getenv('HOME') +os.sep+'.rt'+os.sep+ '.config.hash'


def getTable( file ):
		json_data={}
		if os.path.isfile(file):
				with open(file,'r', encoding="latin-1") as json_file: json_data = simplejson.load(json_file)
		return json_data


fig=getTable(figpath)
sys.path.append( fig['w']+'/widgets/python'.replace('/',os.sep) )
import _rightThumb._construct as __
import _rightThumb._vars as _v
__.appReg = __.clearFocus( '__main__', 'D:\\.rightthumb-widgets\\widgets\\python\\blank-micro.py' )
f = __.appName( __.appReg, '', '' )
__.registeredApps.append( __.appReg )
import _rightThumb._matrix as _matrix
import _rightThumb._base3 as _
_.raq_err=False
_.load()
import _rightThumb._base4 as ___
import _rightThumb._string as _str
import _rightThumb._dir as _dir

_.appInfo[__.appReg] = {"file": "thisApp.py", "liveAppName": "thisApp", "description": "Changes the world", "categories": [""], "usage": [], "relatedapps": [], "prerequisite": [], "examples": [""], "columns": [], "aliases": [], "notes": []}
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