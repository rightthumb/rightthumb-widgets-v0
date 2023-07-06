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

import os, sys, time
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
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files' )
	_.switches.register( 'Split', '-split' )
	_.switches.register( 'Iteration', '-i,-iter,-itter,-iteration' )
	_.switches.register( 'After', '-after' )
	_.switches.register( 'Before', '-before' )
	_.switches.register( 'inLine', '-line' )
	_.switches.register( 'inResult', '-result' )
	_.switches.register( 'join-by', '-join' )

	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'split.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'explode files by bits',
	'categories': [
						'split',
						'explode',
						'text',
						'code',
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
						_.hp('type *.txt | p split -split " " -after install -line apt install -before -y | sort | p countEach'),
						'',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
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


def process():
			rows = _.getText(path)
			run(rows,split,sLine,sResult,before,after) 
	

def run(rows=[],split=[' '],sLine=None,sResult=None,before=None,after=None):
	delim = '485B'
	subject = []
	table = {}
	subs = []
	# _.pr(len(rows))
	# _.pr( split )
	if not after is None:

		for i,row in enumerate( rows ):
			last = ''
			subject = []
			for s in split:
				for x in _.caseUnspecific(row, s):
					row = row.replace( x, delim )
				
				for i,sub in enumerate(row.split(delim)):

					for af in after:
						if af.lower() in sub.lower():
							last = af
					# _.pr(row, last, after)
					if last in after and not last.lower() in sub.lower():

						shouldAdd=False
						if not sResult is None:
							for x in _.caseUnspecific(sub, sResult):
								shouldAdd = True
						else:
							shouldAdd = True
						# _.pr( after, shouldAdd, last, sub )
						if shouldAdd:
							if not before is None and sub in before:
								sub = rows[i-1]
							# _.pr(sub)
							subject.append( sub )
							last = ''
			subs.append(subject)
		# _.pr( subs )
		return subs

		
	elif not before is None:



		for i,row in enumerate( rows ):
			last = ''
			subject = []
			for s in split:
				for x in _.caseUnspecific(row, s):
					row = row.replace( x, delim )
				item = row.split(delim) ##########################################################################
				item.reverse() ##########################################################################
				for sub in row.split(item):
					for af in after:
						if af.lower() in sub.lower():
							last = af
					# _.pr(row, last, after)
					if last in after and not last.lower() in sub.lower():

						shouldAdd=False
						if not sResult is None:
							for x in _.caseUnspecific(sub, sResult):
								shouldAdd = True
						else:
							shouldAdd = True
						# _.pr( after, shouldAdd, last, sub )
						if shouldAdd:
							# _.pr(sub)
							subject.append( sub )
							last = ''
			subject.reverse() ##########################################################################
			subs.append(subject)
		# _.pr( subs )
		subs.reverse() ##########################################################################
		return subs



		# subs = []
		# for i,row in enumerate( rows ):
		#     last = ''
		#     for s in split:
		#         for x in _.caseUnspecific(row, s):
		#             row = row.replace( x, delim )
		#         item = row.split(delim) ##########################################################################
		#         item.reverse() ##########################################################################
		#         for sub in row.split(item):
		#             for af in after:
		#                 if af.lower() in sub.lower():
		#                     last = af
		#             # _.pr(row, last, after)
		#             if last in after and not last.lower() in sub.lower():

		#                 shouldAdd=False
		#                 if not sResult is None:
		#                     for x in _.caseUnspecific(sub, sResult):
		#                         shouldAdd = True
		#                 else:
		#                     shouldAdd = True
		#                 # _.pr( after, shouldAdd, last, sub )
		#                 if shouldAdd:
		#                     subject.append( sub )
		#                     last = ''
		#     subject.reverse() ##########################################################################
		#     subs.append(subject)
		# subs.reverse() ##########################################################################


		# for i,row in enumerate( rows ):
		#     last = ''        
		#     for s in split:
		#         for x in _.caseUnspecific(row, s):
		#             row = row.replace( x, delim )
		#         item = row.split(delim)
		#         item.reverse() ##########################################################################
		#         for sub in item:
		#             for af in before:
		#                 if af.lower() in sub.lower():
		#                     last = af
				
		#         if last in before:
		#             shouldAdd=False
		#             if not sResult is None:
		#                 for x in _.caseUnspecific(sub, sResult):
		#                     shouldAdd = True
		#             else:
		#                 shouldAdd = True
		#             if shouldAdd:
		#                 subject.append( sub )
		#                 last = ''
		#         subject.reverse() ##########################################################################

		

	else:
		for i,row in enumerate( rows ):
			table = {}
			for s in split:
				for x in _.caseUnspecific(row, s):
					row = row.replace( x, delim )
			subject = []

			for sub in row.split(delim):
				if not sResult is None:
					for x in _.caseUnspecific(sub, sResult):
						subject.append( sub )
				else:
					subject.append( sub )
		sub = subject
					
	# _.pr(sub)
	return sub



split = [' ']
def action():
	global split
	rows=[];sLine=None;sResult=None;before=None;after=None;split=[' '];
	splits = ' '
	if _.switches.isActive('Split'):
		_.pr("_.switches.values('Split'):", _.switches.values('Split'))
		split = _.switches.values('Split')
		if not split:
			splits = " "
		else:
			splits = _.ci(_.switches.values('Split')[0])
	if _.switches.isActive('join-by'):
		splits = _.switches.values('join-by')[0]
	if _.switches.isActive('inLine'):
		sLine = _.switches.values('inLine')
	if _.switches.isActive('inResult'):
		sLine = _.switches.values('inResult')
	
	if _.switches.isActive('Before'):
		before = _.switches.values('Before')
	if _.switches.isActive('After'):
		after = _.switches.values('After')

	if _.switches.isActive('Files'):
		for path in _.switches.values('Files'):
			rows = _.getText(path)
			sub = run(rows,split,sLine,sResult,before,after)
			subjects(sub,splits)
	else:
		rows = _.isData(r=1)
		sub = run(rows,split,sLine,sResult,before,after)
		subjects(sub,splits)


def subjects(sub,splits):
	for x in sub:
		if len(x):
			s = splits.join(x)

			_.pr( s )
			# _.pr(x)


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







