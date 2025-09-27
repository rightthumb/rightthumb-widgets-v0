#!/usr/bin/python3
validate='''
 **      **     **     **       ** *******       **     ********** ********
/**     /**    ****   /**      /**/**////**     ****   /////**/// /**///// 
/**     /**   **//**  /**      /**/**    /**   **//**      /**    /**      
//**    **   **  //** /**      /**/**    /**  **  //**     /**    /******* 
 //**  **   **********/**      /**/**    /** **********    /**    /**////  
  //****   /**//////**/**      /**/**    ** /**//////**    /**    /**      
   //**    /**     /**/********/**/*******  /**     /**    /**    /********
	//     //      // //////// // ///////   //      //     //     //////// 
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

import os
import sys
import time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
banner=_.Banner(validate); 
goss=banner.goss
# goss('-\t search hotkeys with the hk command')
# goss('-\t\t hk space')
# goss('-\t\t\t remove-eol-space ctrl,2 space e')
# goss('-\t\t\t dup-spaces ctrl win s')
# goss('-\t\t\t clip-single-space win shift alt s')
# goss('-\t\t\t clip-double-space win shift alt d')
# goss('-\t\t\t clip-dup-spaces ctrl,2 r d s')
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','file.txt',  isRequired=True, description='Files' )
	_.switches.register( 'Process', '-process', ' A or B or C ' )

	_.switches.register( 'Time', '-time' )
	_.switches.register( 'Clean', '--c' )

	_.switches.register( 'NameSpace', '-ns' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'validate.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'validate code',
	'categories': [
						'validate',
						'code',
						'tool',
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
						'p validate -f jquery-1.10.2.js',
						'',
						'p validate -f jquery-1.10.2.js -process B',
						'',
						'p validate -f _app-9a05b382f076e9b2.js + regex',
						'p validate -f _app-9a05b382f076e9b2.js + regex --c',
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


# def file_language():



def action():
	for fi,file in enumerate( _.switches.values('Files') ):
		process(fi)

def process(fi):

	data = _.getText( _.switches.values('Files')[fi], raw=True );


	# _.printVar(data,isDic=False)
	# sys.exit()


	_.switches.values('Files')[fi]

	_code.imp.validator.register( data, 'javascript' )

	A = None
	B = None
	C = None

	if _.switches.isActive('Process'):

		if 'b' in ''.join( _.switches.values('Process') ).lower():
			B = True
		elif 'a' in ''.join( _.switches.values('Process') ).lower():
			A = True
		elif 'c' in ''.join( _.switches.values('Process') ).lower():
			C = True
	elif not _.switches.isActive('Process'):
		B = True
	

	_code.imp.validator.createIndex( data, 'javascript', skipLoad=True, simple=False, A=A, B=B, C=C )
	status = __.setting('validation-status')
	# NameSpace
	
	# _.printVarSimple( _code.imp.validator.identity )
	# sys.exit()

	if status:
		if _.switches.isActive('NameSpace'):
			_.pr( 'name space:' )
			ns = _code.imp.validator.link_jsNameSpace_to_function_payloads()
			_.pr(ns)
			sys.exit()
		_.colorThis( 'Valid', 'green' )
		if _.switches.isActive( 'Time' ):
			_.pr( _code.imp.validator.duration )
	# index = _code.imp.validator.thisTest
	# _.pr( index )
	if True:
		# _.pr( _code.imp.validator.asset )
		if _.switches.isActive('Plus'):
			found = 0
			foundType = []

			for x in _code.imp.validator.identity['identity']:
				o = x
				c = _code.imp.validator.identity['location']['open'][o]
				l = _code.imp.validator.getLabel( o, string=True )
				if _.showLine( _code.imp.validator.identity['identity'][o] ):
					if not _code.imp.validator.identity['identity'][o] in foundType:
						foundType.append(_code.imp.validator.identity['identity'][o])
					found+=1
					if not _.switches.isActive('Clean'):
						_.pr()
						_.pr()
						_.pr()
						_.pr( o,c,l )
						_.pr(  _code.imp.validator.assetSnipet( o, c )  )
			_.pr()
			_.pr()
			_.pr()
			_.colorThis( [ _.addComma(found), ' and '.join( foundType ) ], 'yellow' )
	
	if True:
		if not C is None:
			for x in _code.imp.validator.identity['validation']:
				# _.pr()
				# _.pr()
				# _.pr()
				rec = _code.imp.validator.identity['validation'][x]
				label = []
				values = []
				for yy in rec:
					for ll in yy['label']:
						o = ll
						c = _code.imp.validator.identity['location']['open'][o]
						l = _code.imp.validator.getLabel( o, string=True )
						txt = _code.imp.validator.assetSnipet( o, c )
						label.append(txt)
				for yy in rec:
					for ll in yy['values']:
						o = ll
						if o in _code.imp.validator.identity['location']['open']:
							c = _code.imp.validator.identity['location']['open'][o]
							l = _code.imp.validator.getLabel( o, string=True )
							txt = _code.imp.validator.assetSnipet( o, c )
						else:
							txt = data[o]
						values.append(txt)
				# _.pr( data[x], x, '\t', rec )
				if  len(label):
					_.pr( ' '.join( label ), values )



	# _.printVarSimple( _code.imp.validator.identity )
	# _.pr()
	# _code.imp.validator.the_validation_process()
		# _.pr( type(x) )
		# _.pr(  x, _code.imp.validator.identity['identity'][x]  )

	# for x in index['list']:
	#     _.pr(  _code.imp.validator.assetSnipet( x['start'], x['end'] )  )


	# indexes profile

	# index = _code.imp.validator.auditTable()
	# _code.imp.validator.colorPrint()



_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

# _.colorThis( 0, 'asdf' )
# _.pr( type(324) )
# sys.exit()

########################################################################################
if __name__ == '__main__':
	# banner.pr()
	# banner.gossip()
	action()







