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
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Undo', '-undo' )
	_.switches.register( 'Dash', '-dash' )
	_.switches.register( 'Rename-Folders', '-fo' )
	pass

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
	'file': 'renameSpace.py',
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


########################################################################################
# START

def action():
	#--> min, architecture {:strict:}
	#--> trigger/callback  <w#
	#--> todo#> meta to scan for
	load()
	global files
	global undo
	here = os.getcwd()

	if _.switches.isActive('Dash'):
		spacer = '-'
	else:
		spacer = '_'

	if not _.switches.isActive('Undo'):
		for file in files:
			if 1:
			# if ' ' in file:
				new = file.replace(' ', spacer)
				# new = new.replace('Doctor_Who_','DW_')
				# new = new.replace('_Complete_720p_BluRay_x264','')
				# new = new.replace('Season_','Season_0')
				# new = new.replace('Doctor_Who_2005_','')
				a=__.path(file)
				os.rename(file,new)
				b=__.path(new)
				try:
					undo[b] = a
				except: pass
				_.pr( b.replace( __.path(here)+os.sep, '' ) ,c='cyan')
				_.saveTable(undo,'renameSpace-undo.dex',p=0)
			# _.pr(file)
	elif _.switches.isActive('Undo'):
		for file in files:
			a=__.path(file)
			if a in undo:
				b=undo[a]
				del undo[a]
			os.rename(a,b)
			_.pr( b.replace( __.path(here)+os.sep, '' ) ,c='cyan')
			_.saveTable(undo,'renameSpace-undo.dex',p=0)



def load():
	global files
	global undo
	undo = _.getTable('renameSpace-undo.dex')
	here = os.getcwd()

	if _.switches.isActive('Recursive'):
		r=1
	else:
		r=0


	if _.switches.isActive('Rename-Folders'):
		files = _.fos(r=r)
	else:
		files = _.fo(r=r)
	for i, path in enumerate(files):
		files[i] = path.replace( __.path(here)+os.sep, '' )

	# if not _.switches.isActive('Undo'):
	#     undo[here] = files


import os


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




