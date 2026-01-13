#!/usr/bin/python3

banners={}

banners['widgets']='''
 **       **   **   *******       ********    ********   **********    ********
/**      /**  /**  /**////**     **//////**  /**/////   /////**///    **////// 
/**   *  /**  /**  /**    /**   **      //   /**            /**      /**       
/**  *** /**  /**  /**    /**  /**           /*******       /**      /*********
/** **/**/**  /**  /**    /**  /**    *****  /**////        /**      ////////**
/**** //****  /**  /**    **   //**  ////**  /**            /**             /**
/**/   ///**  /**  /*******     //********   /********      /**       ******** 
//       //   //   ///////       ////////    ////////       //       ////////  
'''
banners['fail']='''
 ********       **       **   **      
/**/////       ****     /**  /**      
/**           **//**    /**  /**      
/*******     **  //**   /**  /**      
/**////     **********  /**  /**      
/**        /**//////**  /**  /**      
/**        /**     /**  /**  /********
//         //      //   //   //////// 
'''
banners['success']='''
  ******** **     **   ******    ******  ********  ********  ********
 **////// /**    /**  **////**  **////**/**/////  **//////  **////// 
/**       /**    /** **    //  **    // /**      /**       /**       
/*********/**    /**/**       /**       /******* /*********/*********
////////**/**    /**/**       /**       /**////  ////////**////////**
	/**/**    /**//**    **//**    **/**             /**       /**
 ******** //*******  //******  //****** /******** ********  ******** 
////////   ///////    //////    //////  //////// ////////  ////////  
'''
banners['valid']='''
 **      **       **       **         **   *******  
/**     /**      ****     /**        /**  /**////** 
/**     /**     **//**    /**        /**  /**    /**
//**    **     **  //**   /**        /**  /**    /**
 //**  **     **********  /**        /**  /**    /**
  //****     /**//////**  /**        /**  /**    ** 
   //**      /**     /**  /********  /**  /*******  
	//       //      //   ////////   //   ///////   
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
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END

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
#e)--> examples

### EXAMPLE: END
########################################################################################
# START



colors='''ColorBold.gray
ColorBold.red
ColorBold.green
ColorBold.yellow
ColorBold.blue
ColorBold.magenta
ColorBold.cyan
ColorBold.white
Color.purple
Color.cyan
Color.darkcyan
Color.blue
Color.green
Color.yellow
Color.red
Color.bold
Background.red
Background.green
Background.yellow
Background.blue
Background.purple
Background.light_blue
Background.grey
Background.black
BackgroundGrey.black
BackgroundGrey.red
BackgroundGrey.green
BackgroundGrey.brown
BackgroundGrey.blue
BackgroundGrey.magenta
BackgroundGrey.cyan
BackgroundGrey.gray
BackgroundGreyBold.black
BackgroundGreyBold.red
BackgroundGreyBold.green
BackgroundGreyBold.blue
BackgroundGreyBold.magenta
BackgroundGreyBold.cyan
BackgroundGreyBold.gray'''.split('\n')
_all_colors_tact_='''ColorBold.gray
ColorBold.red
ColorBold.green
ColorBold.yellow
ColorBold.blue
ColorBold.magenta
ColorBold.cyan
ColorBold.white
Color.purple
Color.cyan
Color.darkcyan
Color.blue
Color.green
Color.yellow
Color.red
Color.bold
Background.red
Background.green
Background.yellow
Background.blue
Background.purple
Background.light_blue'''.split('\n')
# import _rightThumb._banners as _banners

import random
def mf(clear=False,single=False,c=None,loops=10):
	global colors
	global _all_colors_tact_
	global letters
	if not c is None: single=True
	if single:
		if c is None:
			_.pr(letters['__________'],c='red')
		else:
			_.pr(letters['__________'],c=c)
		return None
	_mf=''
	for mf in '__________':
		_mf+=mf
		_.clear()
		_.pr(letters[_mf],c=random.choice(_all_colors_tact_))
		time.sleep(1)
	l=0
	while l < loops:
		if not clear: _.clear()
		l+=1
		_.pr(letters[_mf],c=random.choice(_all_colors_tact_))
		time.sleep(1)
	if not clear: _.clear()
	_.pr(letters[_mf],c='red')
	# time.sleep(5)



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





