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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( focus(), '_rightThumb._auditCodeBase' )
##################################################

##################################################


def appSwitches():
	_.switches.register('Alias', '-a,-i,-alias','d,sendto,docs')
	_.switches.register('Print', '-print')
	_.switches.register('Clean', '--c')
	_.switches.register('Folder', '-f,-fo,-folder')
	

	

_.appInfo[focus()] = {
	'file': 'm.py',
	'description': 'Save bookmark to current folder',
	'categories': [
						'command line',
						'enviroment',
						'navigation',
						'cmd',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()


########################################################################################
# START

# def profileClean( label ):
#     label = label.replace( ,  )



# def bmLog(p):
#     log = _.getTableDB( 'bookmarks_index_log.tables' )
#     if not 'm' in log:
#         log['m'] = []
#     log['m'].append({ 'epoch': time.time(), 'bm': _.switches.value('Alias'), 'location': p, 'session': _v.session() })
#     _.saveTableDB( log, 'bookmarks_index_log.tables', p=0 )

# def action():
#     p = _v.sanitizeFolder( folder )
#     b = _v.bookmarkFormat.replace( 'ALIASHERE', _.switches.value('Alias') )
	
#     if len(_.switches.value('Alias')) == 0:
#         _.pr( 'Error' )
#     else:
#         _.saveText( p, b )

#         bmLog(p)

#         index = _.getTableDB( 'bookmarks.index' )
#         # labels paths
#         if _.switches.value('Alias') in index['labels'].keys():
#             old = index['labels'][_.switches.value('Alias')]
#             if p in index['paths'].keys():
#                 nX = []
#                 for record in index['paths'][p]:
#                     if not record == _.switches.value('Alias'):
#                         nX.append( record )
#                 index['paths'][p] = nX
#             if not _.switches.isActive('Clean'):
#                 _.colorThis( [  '\told', old  ], 'yellow' )
#             if os.path.isdir(old):
#                 status = 'still exists'
#                 if not _.switches.isActive('Clean'):
#                     _.colorThis( [  '\t\t', status  ], 'green' )
#             else:
#                 status = 'no longer exists'
#                 if not _.switches.isActive('Clean'):
#                     _.colorThis( [  '\t\t', status  ], 'red' )
#         index['labels'][_.switches.value('Alias')] = p

#         if p in index['paths'].keys():
#             index['paths'][p].append( _.switches.value('Alias') )
#         else:
#             index['paths'][p] = []
#             if not _.switches.value('Alias') in index['paths'][p]:
#                 index['paths'][p].append( _.switches.value('Alias') )
#         _.saveTableDB( index, 'bookmarks.index', p=0 )
#         if not _.switches.isActive('Clean'):
#             _.colorThis( [  _.switches.value('Alias'), folder  ], 'cyan' )


#     if _.switches.isActive('Print'):
#         _.pr( p )
#         _.pr( b )



def action():

	if _.switches.isActive('Folder'):
		folder = _.switches.values('Folder')[0]
	else:
		folder = os.getcwd()

	made={}
	if 'wprofile' in _v.config_hash:
		made['h'] = 1
		h  = _v.config_hash['wprofile']
	if 'ww' in _v.config_hash:
		made['ww'] = 1
		ww = _v.config_hash['ww']
	# _.pr('made',made)
	if 'ww' in made  and 'h' in made:
		a = ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bookmarks.index'
		b = h+os.sep+'tables'+os.sep+'bookmarks.index'
		# _.pr(os.path.isfile(b))
		try:
			if not os.path.isfile(b) and os.path.isfile(a):
				from shutil import copyfile
				copyfile(a,b)
		except Exception as e:
			pass

	x = _bm.Bookmarks( _.switches.value('Alias'), folder ).save()

	if not _.isWin:
		bashrc_path = os.getenv('HOME') + _v.slash + '.bashrc'
		bashrc = _.getText( bashrc_path, raw=True )
		s = '## {42F74F699A95} ##'
		e = '## {6D2B143FF720} ##'
		if not s in bashrc:
			bashrc += '\n\n'
			bashrc += s
			bashrc += '\n\n'
			bashrc += e
			bashrc += '\n\n'

		bm = _.getTable( 'bookmarks.index' )

		alias = []
		for label in bm['labels']:
			path = _bm.Bookmarks().resolve(bm['labels'][label])
			if os.path.isdir(path):
				a = "alias LABEL='cd \"PATH\"'".replace( 'LABEL', 'b.'+label ).replace( 'PATH', path )
				alias.append(a)

		active=False
		wasActive=False
		new_bashrc = ''
		for line in bashrc.split('\n'):
			if s in line:
				active=True


			if not active:
				new_bashrc += line + '\n'

			if e in line:
				new_bashrc += s + '\n'
				for a in alias:
					new_bashrc += a + '\n'

				new_bashrc += e + '\n'
				active=False
				wasActive=True


		_.saveText( new_bashrc, bashrc_path )


#######################################################################################################################################


		# bashrc_path = _v.programs +_v.slash+ 'bash' +_v.slash+ 'b.sh'
		# # _.pr( os.path.isfile(bashrc_path),  bashrc_path)
		# bashrc = _.getText( bashrc_path, raw=True )
		# s = '## {42F74F699A95} ##'
		# e = '## {6D2B143FF720} ##'
		# if not s in bashrc:
		#     bashrc += '\n\n'
		#     bashrc += s
		#     bashrc += '\n\n'
		#     bashrc += e
		#     bashrc += '\n\n'

		# bm = _.getTableDB( 'bookmarks.index' )

		# alias = []
		# for label in bm['labels']:
		#     path = _bm.Bookmarks().resolve(bm['labels'][label])
		#     if os.path.isdir(path):
		#         a = "alias LABEL='cd PATH'".replace( 'LABEL', 'b.'+label ).replace( 'PATH', path )
		#         alias.append(a)

		# active=False
		# wasActive=False
		# new_bashrc = ''
		# for line in bashrc.split('\n'):
		#     if s in line:
		#         active=True


		#     if not active:
		#         new_bashrc += line + '\n'

		#     if e in line:
		#         new_bashrc += s + '\n'
		#         for a in alias:
		#             new_bashrc += a + '\n'

		#         new_bashrc += e + '\n'
		#         active=False
		#         wasActive=True


		# _.saveText( new_bashrc, bashrc_path )




	# y = _bm.Bookmarks( _.switches.value('Alias') ).get()

	# _.pr(x)
	# _.pr(y)


import _rightThumb._bookmarks as _bm

########################################################################################
if __name__ == '__main__':
	action()