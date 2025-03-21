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
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
##################################################

# app_navigator: switches
def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i', group='Group Name' )
		##  -->    p SwitchGroupsExamples   <--
	# #e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

_._default_settings_()
# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
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
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()

	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	# _.switches.trigger( 'Files', _.isFileSimple )                 # No File Registration          (Fn Alias Resolves To: def isFile)
	
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> caseUnspecific
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)
		#     or
		# results = [rel for rel in [subject for subject in _.isData(r=0) if _.showLine(subject)]]


	#n)--> fields
		# data = []
		# for k in code.db: data.append({'name': k+'  ' })
		# _.fields.asset( 'data', data )
		# for k in code.db:
		# 	_.pr(   _.fields.value( 'data', 'name', k+':' )+'  '+str(len(code.db[k]))   )

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

def action():
	pass
	# load(); global c3po;

	#n)--> iterate
	# for subject in _.isData(r=0): _.pr(subject)
	# for subject in _.myData(): _.pr(subject)
	

# def load():
# 	global c3po
# 	c3po = _.getTable( 'table' )
# 	#n)--> print table
# 	_.pt(c3po)


def n2l(n):
	if 1 <= n <= 26:
		return chr(n + 96)
	return None


def myDic(n):
	dic = {}
	for i in range(1, n + 1):
		dic[i] = n2l(i)
	return dic





def pattern(n):
	dic = myDic(5)
	xx = []
	bb = {}
	aa = {}
	t = '(-)'
	for i in range(1, n + 1):
		l = n2l(i)
		aa[l] = f'({l})'

	for i in range(1, n + 1):
		line = ""
		k = []
		# bb = {}
		for x in range(1, i + 1):
			k.append(dic[x])
		bb[i] = k
		xx.append(k)
	return bb

# Example usage
# y = pattern(5)
# _.pv(y)
class SimpleNestedStructure:
	def __init__(self, depth, symbol="🐶"):
		"""
		Initialize the structure with a given depth and symbol.

		:param depth: Number of levels to nest.
		:param symbol: The symbol to place at the lowest level.
		"""
		self.depth = depth
		self.symbol = symbol
		self.letter_map = self._create_letter_mapping(depth)

	def _number_to_letter(self, num):
		"""
		Convert a number to a corresponding lowercase letter.

		Example: 1 -> 'a', 2 -> 'b', ..., 26 -> 'z'

		:param num: Number to convert.
		:return: Corresponding letter or None if out of range.
		"""
		if num >= 1 and num <= 26:
			letter = chr(num + 96)
		else:
			letter = None

		return letter

	def _create_letter_mapping(self, depth):
		"""
		Create a dictionary that maps numbers to letters.

		Example: {1: 'a', 2: 'b', 3: 'c', ...}

		:param depth: Number of mappings to create.
		:return: Dictionary of number-letter pairs.
		"""
		mapping = {}

		for i in range(1, depth + 1):
			letter = self._number_to_letter(i)
			mapping[i] = letter
			_.pv(mapping)
		# _.pv(mapping)
		return mapping

	def _build_nested_structure(self, level):
		"""
		Recursively create a nested dictionary structure.

		:param level: Current depth level.
		:return: Nested dictionary structure.
		"""
		if level > 1:
			key = self.letter_map[level] + "G" + str(level)
		else:
			key = self.letter_map[level] + str(level)

		if level == 1:
			result = {key: self.symbol}
			return result

		previous_level = self._build_nested_structure(level - 1)

		result = {}
		result[key] = previous_level
		result[self.letter_map[level] + str(level)] = self.symbol

		return result

	def generate(self):
		"""
		Generate the full structure up to the specified depth.

		:return: Nested dictionary structure.
		"""
		result = self._build_nested_structure(self.depth)
		return result


# Example usage:
structure = SimpleNestedStructure(3)
nested_dict = structure.generate()

import json
print(json.dumps(nested_dict, indent=4, ensure_ascii=False))




##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__)

