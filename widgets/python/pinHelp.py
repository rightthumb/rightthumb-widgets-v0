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

import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str



_.appInfo[__name__] = {
	'file': 'pinHelp.py',
	'description': 'Lists apps that do pinterest stuff',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}


_.appInfo[__name__]['relatedapps'].append('** Dont use this help menu **')

_.appInfo[__name__]['examples'].append('p pinHelp ')


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f


def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# __.pipeData = list(data)
	# _.appData[__name__]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__name__]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__name__]['pipe'].append(pd)








########################################################################################
def action():

	print('\t')
	print('\t   Doing a pinterest project??')
	print('\t')
	print('\t   here are some notes that might help')
	print('\t')
	print('\t')
	print('\t________________________________________________________________________________________________________')
	print('\t')
	print('\t')
	print('\t')
	print('\tp pin ')
	print('\t')
	print('\t')
	print('\tp pinterestBoards ')
	print('\t')
	print('\t')
	print('\tp pinterestBoardIDs https://www.pinterest.com/n0tech/-rel/ 100')
	print('\t')
	print('\t\tNOTE: last run had 31,140 and 7,706 unique')
	print('\t')
	print('\t')
	print('\tp pinterestPin 461548661803573016 ')
	print('\t')
	print('\t')
	print('\tb tt')
	print('\tp pinterestProcessList >> pinterestProcessList_SuccessLog.txt')
	print('\t')
	print('\t')
	print('\tb pd')
	print('\tp pinterestProcessedData')
	print('\t')
	print('\t')
	print('\tb pc')
	print('\tp pinterestCachePages')
	print('\t')
	print('\t')
	
	
	print('\tp pinterestResearchByFilename -i file.html -field ')
	print('\t')
	print('\t')
	print('\tp pc')
	print('\tp pinterestGetPageTitleFromCache')
	print('\t')
	print('\t')
	print('\tp auditHTML')
	print('\t')
	print('\t')
	print('\t')
	print('\t')
	print('\t________________________________________________________________________________________________________')
	print('\t')
	print('\tp findKey -i Pinterest_Pin_Data_ID-461548661794872242.json -showpath -showitems -field orig')
	print('\t')
	print('\t')
	print('\tp findKey -i Pinterest_Pin_Data_ID-461548661795474614.json -field name link orig + :orig article aggregated_pin_data  -or -one -showpath -showitems')
	print('\t')
	print('\t')
	print('\tp txtLenFolder + *.json -report')
	print('\t')
	print('\tp txtLenFolder + *.html -report')
	print('\t')
	print('\t')















	# print('p pinHelp ?')
	# print('p getPageTest')
	# print('pin_scrap.txt')



########################################################################################
if __name__ == '__main__':
	action()