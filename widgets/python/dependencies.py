#!/usr/bin/python3

dependencies='''
	**                                                 **                                  **                    
	/**             ******                             /**                                 //                     
	/**    *****   /**///**    *****    *******        /**    *****    *******     *****    **    *****     ******
  ******   **///**  /**  /**   **///**  //**///**    ******   **///**  //**///**   **///**  /**   **///**   **//// 
 **///**  /*******  /******   /*******   /**  /**   **///**  /*******   /**  /**  /**  //   /**  /*******  //***** 
/**  /**  /**////   /**///    /**////    /**  /**  /**  /**  /**////    /**  /**  /**   **  /**  /**////    /////**
//******  //******  /**       //******   ***  /**  //******  //******   ***  /**  //*****   /**  //******   ****** 
 //////    //////   //         //////   ///   //    //////    //////   ///   //    /////    //    //////   //////  
'''
dependencies2='''
	**                                       **                          **                
	/**         ******                       /**                         //                 
	/**  ***** /**///**  *****  *******      /**  *****  *******   *****  **  *****   ******
  ****** **///**/**  /** **///**//**///**  ****** **///**//**///** **///**/** **///** **//// 
 **///**/*******/****** /******* /**  /** **///**/******* /**  /**/**  // /**/*******//***** 
/**  /**/**//// /**///  /**////  /**  /**/**  /**/**////  /**  /**/**   **/**/**////  /////**
//******//******/**     //****** ***  /**//******//****** ***  /**//***** /**//****** ****** 
 //////  ////// //       ////// ///   //  //////  ////// ///   //  /////  //  ////// //////  
'''

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
	_.switches.register( 'No-Banner', '-nobanner' )
	_.switches.register( 'Modules', '-m,-mod,-mods,-module,-modules', 'guesslang tensorflow' )

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
	'file': 'dependencies.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'find every imorted module or file recursively',
	'categories': [
						'child',
						'children',
						'sherlock',
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
						_.hp('p dependencies -F file.py'),
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

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def clean(line):
	line=_str.do('dup',line,' ')
	line=_str.do('be',line,'\t')
	line=_str.do('be',line,' ')
	line=_str.do('be',line,'\t')
	return line
def test_app(): pass

def module_surfing(file):
	global table
	if file in table: return False
	
	_modules = []

	def _add_mod_(mo,_modules):
		global modules
		if mo and not mo in _modules: _modules.append(mo)
		if mo and not mo in modules: modules.append(mo); _.pr(mo,c='green');
		return _modules

	def _line_mods_(line,_modules):
		
		if ' from ' in line: mo = clean(line).split(' ')[1].split('.')[0]; _modules = _add_mod_(mo,_modules);
		elif ' import ' in line and ',' in line and ' as ' in line:

			line=line.split(' import ')[1]
			for mo in line.split(','):
				mo=mo.replace('\t','').replace(' ','')
				_modules = _add_mod_(mo,_modules)
		elif ' import ' in line and ',' in line:
			line=line.split(' import ')[1]
			
			for mo in line.split(','):
				mo = mo.split(' as ')[0]
				mo=mo.replace('\t','').replace(' ','')
				_modules = _add_mod_(mo,_modules)

		elif ' import ' in line or ' from ' in line:
			mo = clean(line).split(' ')[1].split('.')[0]; _modules = _add_mod_(mo,_modules);

	for i, line in enumerate(file.split('\n')):
		line=' '+line.split('#')[0]
		line = line.replace(';',' ; ')
		if not '"' in line and not "'" in line and ( ' import ' in line or ' from ' in line ):
			if not ';' in line:
				_modules=_line_mods_(line,_modules)
			elif ';' in line:
				for li in line.split(';'):
					_modules=_line_mods_(li,_modules)

	table[file] = _modules
	return _modules



def module_dependency_folder(module):
	try: mod=eval(module)
	except Exception as e: _.pr(e,c='red'); mod=None;

	# path=eval(mod+'.__file__')
	_.pr(path)

os=__.imp('os.path.isfile')
table={}
modules=[]
def module_dependency_module(module):

	def _py_(path):
		if os.path.isfile(path) and path.endswith('.py'): return True
		return False

	global modules
	if os.path.isfile(module+'.py'):
		module = module+'.py'
	if not os.path.isfile(module):
		path = module_path(module)
	print(path)
	fo=__.path(path,pop=True)
	if fo.endswith(os.sep+'lib'+os.sep) or fo.endswith(os.sep+'lib'):
		files_py=[path]
	else: files_py = _.fo2(fo,test=_py_,r=True)
	# print(fo)
	# files_py = _.fo(fo,r=True)
	# _files_py=[]
	# for _fi in files_py:
	#     if _py_(path): _files_py.append(path)
	# files_py=_files_py
	for path in files_py:
		print(path)
		_modules = module_surfing(path)
		if _modules:
			for mod in _modules:
				_.pr(mod)
				module_dependency_module(module)

modules=[]

# def module_dependency_modules(module):


def module_path(module):
	
	try:
		mod=eval(module)
		if mod:  exec('del '+module)
	except Exception as e:
		pass
		# raise e
	exec('import '+module)
	path=eval(module+'.__file__')
	return path
	



def action():
	global modules
	if _.switches.isActive('Modules'):
		for module in _.switches.values('Modules'):
			module_dependency_module(module)
		for mod in modules: _.pr(mod)
		return None



	# load(); global c3po;

	#--> iterate
	for subject in _.isData(r=0): _.pr(subject)
	

# def load():
#     global c3po
#     c3po = _.getTable( 'table' )
#     #--> print table
#     _.pt(c3po)


##################################################
#b)--> examples
banner=_.Banner(dependencies)
goss=banner.goss
goss('-\t '+_.appInfo[focus()]['description'])
goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
if __name__ == '__main__':
	#b)--> examples
	if not _.switches.isActive('No-Banner'):
		banner.pr()
		if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)





