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

# import os
import sys
import time
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'convertFranchise.py',
	'description': 'Single purpose convert file',
	'categories': [
						'format data',
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

_.appInfo[focus()]['examples'].append('p convertFranchise')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
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

########################################################################################
# START

def getKeys( data ):
	global omitKey
	result = []
	for ky in data[0].keys():
		good = True
		for ot in omitKey:
			if ot in ky:
				good = False
		result.append( ky )
	return result

def action():

	franchiseData = _.getTable('imdb_franchises.json')
	display = _.getTable('imdb_franchise_display.json')

	# {
	#     "actual": "bond",
	#     "proper": "James Bond"
	# }

	f = {
			'label': '',
			'alias': [],
			'entertainment': [],
			'people': [],
			'data': [],

	}

	data = []

	franchises = getKeys() 



omitKey = [ '_date', '_list' ]
########################################################################################
if __name__ == '__main__':
	action()


# 573  fdtl = franchiseData[0][franchiseDate].split('-')
# 606  franchiseData[0][franchiseNameList]
# 618  theList = franchiseData[0][franchiseNameList]
# 626  franchiseData[0][franchiseNameList] = list(set(theList))
# 648  franchiseData[0][franchiseName][0]
# 650  franchiseData[0][franchiseName] = []
# 654  franchiseData[0][franchiseName].append( fItem )
# 659  franchiseData[0][franchiseDate] = str(today)
# 661  franchiseData[0] = {franchiseDate: str(today)}
# 663  franchiseList = list(set(franchiseData[0][franchiseName]))
# 671  fdtl = franchiseData[0][franchiseDate].split('-')
# 752  mv = str(len(set(franchiseData[0][franchiseName]))) + ' movies\t\t
# 1335  fdtl = franchiseData[0][franchiseDate].split('-')
# 1367  franchiseData[0][franchiseNameList]
# 1380  theList = franchiseData[0][franchiseNameList]
# 1406  franchiseData[0][franchiseName][0]
# 1408  franchiseData[0][franchiseName] = []
# 1412  franchiseData[0][franchiseName].append( fItem )
# 1417  franchiseData[0][franchiseDate] = str(today)
# 1419  franchiseData[0] = {franchiseDate: str(today)}
# 1463  for fd in set(franchiseData[0][franchiseName]):
# 1468  franchiseData[0][franchiseOmit]
# 1529  _.pr(len(set(franchiseData[0][franchiseName])))
# 1593  mv = str(len(set(franchiseData[0][franchiseName]))) + ' movies\t\t
# 4475  for k in self.franchiseData[0].keys():


# 748  ppl = str(len(set(franchiseData[1][franchiseName]))) + ' people\t\t
# 756  _.pr(franchise.upper(),len(set(franchiseList)),'\t\t',ppl,mv,franchiseData[1][franchiseDate],'\t\t',str(diff.days),'days')
# 1424  franchiseData[1]
# 1432  franchiseData[1][franchiseName]
# 1436  franchiseData[1][franchiseName] = []
# 1530  franchiseData[1][franchiseName] = list(set(thePeopleY))
# 1531  franchiseData[1][franchiseDate] = str(today)
# 1550  franchiseList = list(set(franchiseData[1][franchiseName]))
# 1551  fdtl = franchiseData[1][franchiseDate].split('-')
# 1589  ppl = str(len(set(franchiseData[1][franchiseName]))) + ' people\t\t
# 1597  _.pr(franchise.upper(),len(set(franchiseList)),'\t\t',ppl,mv,franchiseData[1][franchiseDate],'\t\t',str(diff.days),'days')


# 720  franchiseData[2][franchiseName]
# 738  for fdai,fda in enumerate(franchiseData[2][franchiseName]):
# 740  _.pr('\t\t\t\t',franchiseData[2][franchiseName][fdai]['year'],franchiseData[2][franchiseName][fdai]['title'])
# 1428  franchiseData[2]
# 1438  franchiseData[2][franchiseName]
# 1459  franchiseData[2][franchiseName] = []
# 1527  franchiseData[2][franchiseName].append({'year': theYearX, 'title': theTitleX, 'people': thePeopleX, })