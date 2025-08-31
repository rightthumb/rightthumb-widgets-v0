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
	_.switches.register( 'Files', '-f,-fi,-file,-files','fileBackup.json', isData='name', description='Files' )
	_.switches.register( 'Just-Lines', '-jl,-just-lines' )

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
	'file': 'fi-len.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'cound the length of lines in large text files cheap',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'file',
						'size',
						'len',
						'length',
						'cheap',
						'large',
						'fast',
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
						_.hp('p fi-len -f fileBackup.json'),
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
os = __.os
import _rightThumb._dir as _dir
import _rightThumb._mimetype as _mime

def action():
	global print_info
	_.clear()
	_.linePrint(c='yellow')
	for i, path in enumerate( _.isData(r=0) ):
		if not os.path.isfile(path): _.e( 'error: files does not exist\n', path ); return None
		# if not _mime.isText(path): _.e( ['error: this is a binary file.','\texpected text file.',''], path )
		_.linePrint(c='yellow')
		_.pr()
		_.pr(path,c='cyan')
		info = _dir.info(path,mini=True)

		# _.pr()
		# _.pr( '\t lines:',_.file_len(path) )
		# _.pr( '\t lines:',_.addComma( _.file_len(path) ) )
		# _.pr()
		# _.pr( '\t bytes:', info['bytes'] )
		# _.pr( '\t bytes:',_.addComma( info['bytes'] ) )
		# _.pr()
		# _.pr( '\t size:', info['size'] )
		if _mime.isText(path):
			out={}
			out['lines'] = _.file_len(path)
			out[' lines'] = _.addComma( _.file_len(path) )
			out['bytes'] = info['bytes']
			out[' bytes'] = _.addComma( info['bytes'] )
			out['size'] = info['size']
			del info['bytes']
			del info['size']
			if print_info and not _.switches.isActive('Just-Lines'):
				_.linePrint(c='cyan')
				info = _.dicKeys( info, omit='name_ folder name path ext year' )
				_.pr(info,dic=1)
			_.linePrint(c='cyan')
			_.pr(out,dic=1)
		if not _mime.isText(path):
			_.linePrint(c='red')
			_.pr()
			_.pr('  error: ',c='red')
			_.pr()
			_.pr('\t this is a binary file.',c='yellow')
			_.pr('\t\t expected text file.',c='yellow')
			_.pr()
			_.linePrint(c='red')
			_.pr(info,dic=1)
		_.linePrint(c='yellow')
		diffm = _._2dates( time.time(), info['me'], dic=1 )
		diffc = _._2dates( time.time(), info['ce'], dic=1 )
		# diffa = _._2dates( time.time(), info['ae'] )
		_.pr()
		if diffm['txt'] == diffc['txt']:
			_.pr(diffm['txt'], c='green')
		else:
			_.pr('created',c='cyan')
			_.pr('\t',diffc['txt'], c='green')
			_.pr('modified',c='cyan')
			_.pr('\t',diffm['txt'], c='green')
			# if not diffa['txt'] == diffc['txt']:
			#     _.pr('accessed',c='cyan')
			#     _.pr('\t',diffa['txt'], c='green')

print_info=True


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




