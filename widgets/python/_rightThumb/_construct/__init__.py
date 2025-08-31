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

'''
# Undocumented switches

--nc
	No Comments - Removes all comments from the code.
	This is useful for processing code without comments.

--appReg  or os debug=yes
	Print when switches.process() changes __.appReg

'''

##################################################
# import sys

# if not sys.stdin.isatty():
#     LINES = [line.strip() for line in sys.stdin if line.strip()]
# else:
#     LINES = []
##################################################
class Meta_Namespace():
	def __init__( self ):
		pass
dot=Meta_Namespace
fn=Meta_Namespace()
switch_skimmer = Meta_Namespace()
switch_skimmer.scan = {}
##################################################
switchTableSpentPrint = []
##################################################
# App Help Menu Switch Grouping
SwitchGroup_Help = Meta_Namespace()
SwitchGroup_Help.Delim = ''
SwitchGroup_Help.Group = '>'
SwitchGroup_Help.SubGroup = '>' # if this len 1: SwitchGroupDepth +=1
SwitchGroup_Help.Group_After = ' | \u25BD Group \u25BD '
SwitchGroup_Help.SubGroup_After = ' | \u25BD SubGroup cnt\u25BD '
SwitchGroup_Help.NoGroup_After = '  \u25BD Switches \u25BD '
SwitchGroup_Help.NoGroup = '-'
SwitchGroup_Help.PostLabel = '  '
SwitchesModifier = Meta_Namespace()
SwitchesModifier.Trigger = {}
SwitchesModifier.PrintActive = True
appInfoAcquiredData = { 'app': '', 'focus': '', 'data': None }

# HasSwitchSubGroup search for in framework

##################################################
##################################################

language = None



class Language:
	def __init__(self, lang=None, isLine=False):
		""" Initialize the Language class with a specific language. """
		self.isLine = isLine
		self.valid = False
		
		self.ext2language = {
			'py': 'python',
			'js': 'javascript',
			'ts': 'typescript',
			'java': 'java',
			'c': 'c',
			'cpp': 'cpp',
			'cs': 'csharp',
			'go': 'go',
			'swift': 'swift',
			'kt': 'kotlin',
			'kts': 'kotlin',
			'php': 'php',
			'rb': 'ruby',
			'html': 'html',
			'htm': 'html',
			'css': 'css',
			'rs': 'rust',
			'pl': 'perl',
			'pm': 'perl',
			'sh': 'bash',
			'bash': 'bash',
			'ps1': 'powershell',
			'r': 'r',
			'lua': 'lua',
			'hs': 'haskell',
			'asm': 'assembly',
			's': 'assembly',
			'md': 'markdown',
			'xml': 'xml',
			'json': 'json',
			'yml': 'yaml',
			'yaml': 'yaml',
			'bat': 'batch',
			'cmd': 'batch',
			'ini': 'ini',
			'toml': 'toml',
			'makefile': 'make',
			'mk': 'make',
		}

		self.lang = lang
		# if self.lang is None:
		# 	self.lang = 'python'
		if self.lang in self.ext2language:
			self.lang = self.ext2language[self.lang]
			# print(self.lang, 'language set from extension')



		# Define inline comment markers for many languages
		self.inlineComments = {
			'python': '#',
			'javascript': '//',
			'typescript': '//',
			'java': '//',
			'c': '//',
			'cpp': '//',
			'csharp': '//',
			'go': '//',
			'swift': '//',
			'kotlin': '//',
			'php': '//',
			'bash': '#',
			'powershell': '#',
			'ruby': '#',
			'perl': '#',
			'r': '#',
			'lua': '--',
			'haskell': '--',
			'assembly': ';',
		}

		# Define multiline comment markers (start, end)
		self.multilineComments = {
			'python': [("'''", "'''"), ('"""', '"""')],
			'javascript': [('/*', '*/')],
			'typescript': [('/*', '*/')],
			'java': [('/*', '*/')],
			'c': [('/*', '*/')],
			'cpp': [('/*', '*/')],
			'csharp': [('/*', '*/')],
			'go': [('/*', '*/')],
			'swift': [('/*', '*/')],
			'kotlin': [('/*', '*/')],
			'php': [('/*', '*/')],
			'ruby': [('=begin', '=end')],
			'html': [('<!--', '-->')],
			'css': [('/*', '*/')],
			'rust': [('/*', '*/')],
			'perl': [('=pod', '=cut')],
			'lua': [('--[[', ']]')],
		}

		if self.lang and (self.lang in self.inlineComments or self.lang in self.multilineComments):
			self.valid = True


	def inline(self, lang):
		""" Set the language for inline-only code processing. """
		self.lang = lang
		self.isLine = True

	def set(self, lang):
		""" Set the language for the Language class. """
		self.lang = lang

	def get(self):
		""" Get the current language of the Language class. """
		return self.lang

	def noComments(self, code):
		""" Remove inline and multiline comments from the code based on the current language. """
		if self.lang not in self.inlineComments and self.lang not in self.multilineComments:
			raise ValueError(f"Unsupported language: {self.lang}")

		# Remove inline comments
		code = self._remove_inline_comments(code)

		# Remove multiline comments unless line-mode is active
		if not self.isLine:
			code = self._remove_multiline_comments(code)

		return code.strip()

	def _remove_inline_comments(self, code):
		""" Remove inline comments using the configured symbol. """
		import re
		comment_symbol = self.inlineComments.get(self.lang)
		if comment_symbol:
			pattern = re.escape(comment_symbol) + r'.*$'
			return re.sub(pattern, '', code, flags=re.MULTILINE)
		return code

	def _remove_multiline_comments(self, code):
		""" Remove all types of multiline comments defined for the current language. """
		import re
		if self.lang not in self.multilineComments:
			return code
		for start, end in self.multilineComments[self.lang]:
			pattern = re.escape(start) + r'.*?' + re.escape(end)
			code = re.sub(pattern, '', code, flags=re.DOTALL)
		return code


#abc123 start new

# _.pr( line, plus='cyan' )
# _.pr( line, plus='yellow,cyan', c='cyan' )
# _.pr( line, plus=1, h='chartreuse,cornflower_blue' )

class FakeSwitches:
	def __init__(self):
		pass
	def isActive(self, name, appReg=None):
		return False
	def values(self, name, appReg=None):
		return []
	def value(self, name, appReg=None):
		return ''

class Line:
	def __init__(self, switches=None, switch_dict=None, run=-1, lang=None, focus=None):
		""" Initialize the Line processor with a SwitchManager instance. Optionally accept a pre-populated switch_dict. """
		if focus is None:
			global appReg
			focus = appReg
		self.appReg = focus
		self.run = run
		self.active = {}
		if switches is None:
			switches = FakeSwitches()
		self.switches = switches
		self.showLine_list = []
		self.showLineC = False
		self.sl = False
		self.hasPlus = None

		global language
		# print(language, 'language')
		if lang is None:
			lang = language
		if lang == 0 or lang == False:
			self.Language = Meta_Namespace()
			self.Language.valid = False
		elif '--nc' in sys.argv:
			# print(sys.argv); sys.exit(0)
			# print(lang)
			self.Language = Language(lang=lang, isLine=True)
			# print(f"Language set to: {self.Language.lang} {self.Language.valid}"); sys.exit(0)
		else:
			self.Language = Meta_Namespace()
			self.Language.valid = False

		switch_dict2 = {}
		if not switch_dict is None:
			if 'appReg' in switch_dict:
				self.appReg = switch_dict['appReg']
			for k in switch_dict:
				switch_dict2[k.lower()] = switch_dict[k]
		self.switch_dict2 = switch_dict2
		# If switch_dict is passed, use it directly, otherwise initialize it with setSwitches
		self.switch_dict = switch_dict if switch_dict is not None else self.setSwitches()

	def register(self, switch_dict=None):
		""" Register a new switch_dict if provided. """
		self.switch_dict = switch_dict if switch_dict is not None else self.setSwitches()

	def setSwitches(self):
		""" Automatically check active switches and populate a dictionary. """
		switch_dict = {}

		# List of all possible switch names that we are checking
		switch_names = [ 'Plus', 'Minus', 'PlusOr', 'PlusCode', 'PlusClose', 'Plus-Sub', 'StrictCase', 'Plus-single', 'PlusDuplicate', 'Minus-single' ]
		switch2dict = {
			'PlusCode': 'code',

		}
		for switch in switch_names:
			if self.switches.isActive(switch, self.appReg) or self.switch_dict2.get(  switch2dict.get(switch, switch.lower())  ,False):
				self.active[switch] = True
				if switch in ['Plus','Minus']:
					x=[]
					for y in self.switches.values(switch, self.appReg):
						x.append(self.ci(y))
				else:
					x=self.switches.values(switch, self.appReg)
				if not switch in switch_dict:
					switch_dict[switch] = x
			else:
				self.active[switch] = False
				switch_dict[switch] = None  # If not active, we set it to None
		
		return switch_dict

	def isActive(self, switch):
		if  switch in self.active and self.active[switch]:
			return True
		if not switch in self.active:
			return False
		return self.active[switch]
	def processArgsKwargs(self, args, kwargs):
		# plus='', minus='', plusOr=False, end=None, isSub=False, OR=None, code=False, itIs=False, c=False
		if (len(args) or len(kwargs)) and not self.switch_dict:
			self.switch_dict = {}
		if len(args) > 0:
			self.switch_dict['Plus'] = args[0] if len(args) > 0 else ''
			if type(self.switch_dict['Plus']) == str:
				self.switch_dict['Plus'] = [self.ci(self.switch_dict['Plus'])]
			else:
				self.switch_dict['Plus'] = [self.ci(x) for x in self.switch_dict['Plus']]
			# print(self.switch_dict['Plus'])
			if self.switch_dict['Plus']:
				self.active['Plus'] = True
		if len(args) > 1:
			self.switch_dict['Minus'] = args[1] if len(args) > 1 else ''
			if type(self.switch_dict['Minus']) == str:
				self.switch_dict['Minus'] = [self.ci(self.switch_dict['Minus'])]
			else:
				self.switch_dict['Minus'] = [self.ci(x) for x in self.switch_dict['Minus']]
			# print(self.switch_dict['Minus'])
			if self.switch_dict['Minus']:
				self.active['Minus'] = True

		if 'StrictCase' in kwargs:
			self.switch_dict['StrictCase'] = kwargs['StrictCase']
			self.active['StrictCase'] = True

		if len(args) > 2:
			self.switch_dict['PlusOr'] = args[2] if len(args) > 2 else False
			if self.switch_dict['PlusOr']:
				self.active['PlusOr'] = True
		if len(args) > 3:
			self.switch_dict['end'] = args[3] if len(args) > 3 else None
		if len(args) > 4:
			self.switch_dict['isSub'] = args[4] if len(args) > 4 else False
			if self.switch_dict['isSub']:
				self.active['Plus-Sub'] = True
		if len(args) > 5:
			self.switch_dict['OR'] = args[5] if len(args) > 5 else None
			if self.switch_dict['OR']:
				self.active['PlusOr'] = True
		if len(args) > 6:
			self.switch_dict['code'] = args[6] if len(args) > 6 else False
			if self.switch_dict['code']:
				self.active['PlusCode'] = True
		if len(args) > 7:
			self.switch_dict['itIs'] = args[7] if len(args) > 7 else False
			if self.switch_dict['itIs']:
				self.active['Plus-Sub'] = True
		if len(args) > 8:
			self.switch_dict['c'] = args[8] if len(args) > 8 else False
		if 'Plus' in kwargs:
			self.switch_dict['Plus'] = kwargs['Plus']
			self.active['Plus'] = True
			self.hasPlus = True
		if 'Minus' in kwargs:
			self.switch_dict['Minus'] = kwargs['Minus']
			self.active['Minus'] = True
		if 'PlusOr' in kwargs:
			self.switch_dict['PlusOr'] = kwargs['PlusOr']
			self.active['PlusOr'] = True
		if 'end' in kwargs:
			self.switch_dict['end'] = kwargs['end']
		if 'isSub' in kwargs:
			self.switch_dict['isSub'] = kwargs['isSub']
			self.active['Plus-Sub'] = True
		if 'OR' in kwargs:
			self.switch_dict['OR'] = kwargs['OR']
			self.active['PlusOr'] = True
		if 'code' in kwargs:
			self.switch_dict['code'] = kwargs['code']
			self.active['PlusCode'] = True
		if 'itIs' in kwargs:
			self.switch_dict['itIs'] = kwargs['itIs']
			self.active['Plus-Sub'] = True
		if 'c' in kwargs:
			self.switch_dict['c'] = kwargs['c']



	def show(self, string, *args, **kwargs):
		""" Processes and shows the string with switch-based conditions. Returns a boolean value. """
		# print(self.switch_dict.get('Minus', ''))
		string = str(string)

		if self.Language.valid:
			string = self.Language.noComments(string)

		self.processArgsKwargs(args, kwargs)

		if not self.isActive('StrictCase'):
			string = string.lower()
			
		# print( self.run, self.switch_dict )


		# if 'Minus' in self.switch_dict and not self.switch_dict['Minus']:
		#     minus = self.switch_dict['Minus']
		# else:
		# minus = self.switch_dict.get('Minus', self.switches.values('Minus'))
		minus = self.switch_dict.get('minus', self.switch_dict.get('Minus', []))
		plus = self.switch_dict.get('plus', self.switch_dict.get('Plus', []))
		# print(plus,self.switch_dict)
		# print(plus); sys.exit(0)
		if len(args) > 1:
			minus = args[1]
		if 'Minus' in kwargs:
			minus = kwargs['Minus']
		# if self.run == 1389:
		#     # print(minus)
		#     return False
		ogString = string
		self.showLineC = False
		string = str(string).strip()

		# Check if 'Plus' switch is active
		if self.hasPlus is None:
			self.hasPlus = self.isActive('Plus')


		result = True

		# Handling the 'Plus' logic
		# plus = self.switch_dict.get('Plus', [])
		run = False    
		if self.isActive('Plus') or (self.switch_dict and 'code' in self.switch_dict and self.switch_dict['code']):
			run = True
		if result and (self.isActive('Minus') or (self.switch_dict and 'Minus' in self.switch_dict and self.switch_dict['Minus'] != '')):
			run = True
		if plus:
			run = True
		if minus:
			run = True
		if not run:
			# print('no run')
			return True
		

		if isinstance(plus, str):
			plus = [plus]
		elif not isinstance(plus, list):
			if plus:
				plus = list(plus)
				# plus = []
		# print('plus:', plus)
		# print(self.switch_dict)
		if plus:
			# print('plus:', plus)
			if plus or  self.isActive('Plus') or (self.switch_dict and 'code' in self.switch_dict and self.switch_dict['code']):
				if self.isActive('PlusCode'):
					result = self.positiveResultsCode(string, plus, self.switch_dict.get('PlusOr', False), self.switch_dict.get('end', None), self.switch_dict.get('OR', None))
				else:
					# print('positiveResults')
					result = self.positiveResults(string, plus, self.switch_dict.get('PlusOr', False), self.switch_dict.get('end', None), self.switch_dict.get('OR', None))

				if not result and self.isActive('PlusClose'):
					result = self.closeResults(string)

				if result and not self.switch_dict.get('isSub', False) and self.isActive('Plus-Sub'):
					result = False
					for xXx in self.switches.values('Plus-Sub', self.appReg):
						if self.ci(xXx) in self.ci(string):
							result = True
							break

		# Handling the 'Minus' logic
		# if result and (self.isActive('Minus') or (self.switch_dict and 'Minus' in self.switch_dict and self.switch_dict['Minus'] != '')):
		if result and minus:
			result = self.minusResults(string, minus, self.switch_dict.get('itIs', False))
			# print(result,'Minus is active, running Plus logic')
			# print('here', result, self.switch_dict.get('Minus', ''))


		# If 'c' switch is active, apply `prWC2`
		if result and self.switch_dict.get('c', False):
			self.showLineC = ogString
			for by in self.showLine_list:
				self.showLineC = self.prWC2(self.showLineC, by)

		self.sl = self.showLineC
		result = bool(result)  # Ensure result is a boolean value
		# print(string,result)
		return bool(result)




	def _prepare_plus_input(self, plus):
		"""Prepare the 'plus' input parameter"""
		global switches
		if not plus:
			return switches.values('Plus').copy()
		elif isinstance(plus, str):
			return [plus]
		return plus


	def _is_substring_present(self, sub, main_string):
		"""Check if a substring is present based on various conditions."""
		if '=' in __.sw.PlusCode:
			return main_string == sub
		if '*x' in __.sw.PlusCode:
			return main_string.endswith(sub)
		if 'x*' in __.sw.PlusCode:
			return main_string.startswith(sub)

		no_break_chars = '[]()_01`23456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"' + "'" + sub
		cleaned_main_string = ''.join(char if char in no_break_chars else ' ' for char in main_string)
		return f' {sub} ' in cleaned_main_string





	def positive_results_code(self, string, plus='', plus_or=False, end=None, OR=None):
		""" Processes string with 'PlusCode' functionality. """
		# if self.switch_dict:
		#     if not plus and 'Plus' in self.switch_dict:
		#         plus = self.switch_dict['Plus']
		#     if not plus_or and 'PlusOr' in self.switch_dict:
		#         plus_or = self.switch_dict['PlusOr']
		#     if not end and 'end' in self.switch_dict:
		#         end = self.switch_dict['end']
		#     if not OR and 'PlusOr' in self.switch_dict:
		#         OR = self.switch_dict['PlusOr']


		switches = self.switches
		plus_or = OR if OR is not None else (plus_or or switches.isActive('PlusOr'))

		plus_input = self._prepare_plus_input(plus)

		# Handle case sensitivity
		strict_case = switches.isActive('StrictCase')
		if not strict_case:
			string = string.lower()
			plus_input = [self.ci(item) for item in plus_input]

		# Add 'end' to 'plusInput' if provided
		if end is not None:
			plus_input = [item + end for item in plus_input]

		# Check if 'plusInput' exists in the string
		count_found = sum(1 for item in plus_input if self._is_substring_present(item, string))

		return count_found == len(plus_input) or (plus_or and count_found > 0)
	
	def positiveResultsCode(self,string,plus='',plusOr=False,end=None,OR=None):
		string = str(string)
		string = string.replace('[',' [')
		# __.sw.PlusCode
		# global showLine_list

		string = string.replace("'",' ').replace('"',' ')
		# global switches
		switches = self.switches
		if switches.isActive('PlusCode') and 'n' in switches.value('PlusCode'):
			return self.positive_results_code(string,plus,plusOr,end,OR)
		if plusOr or switches.isActive('PlusOr'):
			plusOr = True

		if not OR is None:
			plusOr=OR
		if not plus == '':
			if type(plus) == str:
				plusInput = [plus]
			else:
				plusInput = plus
		else:
			plusInput = switches.values('Plus').copy()
		showLine_list = plusInput

		


		if type( plusInput ) == list:
			for i,yh in enumerate(plusInput):
				plusInput[i]= self.ci(plusInput[i])
		# -->   #end> this was added 2022-07-20
		global showLine_quoteFix
		if showLine_quoteFix and type(plusInput)==list:
			new=[]
			for i,x in enumerate(plusInput):
				if "'" in x:
					# new.append(x.replace("'",'"'))
					if not i and switches.isActive('Plus-single'):
						x=x.replace("'",'"')
				new.append(x)
			plusInput=new
		if not end is None:
			if type( plusInput ) == str:
				plusInput += end
			else:
				for i,yh in enumerate(plusInput):
					plusInput[i] += end
		StrictCase=switches.isActive('StrictCase')
		if not StrictCase:
			string=string.lower()
		pi = []
		for x in plusInput:
			if not StrictCase:
				pi.append( self.ci(x) )
			else:
				pi.append( self.ci(x) )

		plusInput = pi
		del pi
		if type( plusInput ) == str:
			plusList = [plusInput]
		else:
			plusList = plusInput
		length = len(plusList)

		if length == 1 and not plusList[0] in string: return False
		elif length == 2:
			if not plusList[0] in string: return False
			if not plusList[1] in string: return False
		elif length == 3:
			if not plusList[0] in string: return False
			if not plusList[1] in string: return False
			if not plusList[3] in string: return False

		cnt = 0
		result = False
		noBreak='[]_01`23456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"'+"'" + ''.join(plusList)
		stringN=' '
		xstringx=string
		for vgo in string:
			if vgo in noBreak: stringN+=vgo
			else: stringN+=' '
		stringN+=' '
		# string=stringN

		code_switch = ''.join(self.switch_dict.get('PlusCode', []))
		# print(plusInput, stringN)

		for s in plusList:
			sN = ' ' + s + ' '
			if len(s) > 1:
				# print(sN); sys.exit(0)
				if '=' in code_switch:
					if string == s:
						cnt += 1
				elif '*x' in code_switch:
					if string.endswith(s):
						cnt += 1
				elif 'x*' in code_switch:
					if string.startswith(s):
						cnt += 1
				else:
					if sN in stringN:
						# print(sN, stringN); sys.exit(0)
						cnt += 1
					elif len(s) == 1 and s in string:
						cnt += 1  # fallback for 1-char token
			if len(s) == 1:
				# print(sN); sys.exit(0)
				if '=' in code_switch:
					if string == s:
						cnt += 1
					elif string.strip().replace(' ','').startswith(s+'='): cnt += 1
					elif stringN+' '.lstrip().endswith(' '+sN.rstrip()): cnt += 1
					elif ' '+stringN.rstrip().endswith(' '+sN.lstrip()): cnt += 1
						
				elif '=' in xstringx:
					if string.strip().replace(' ','').startswith(s+'='): cnt += 1
					# elif stringN.lstrip().endswith(sN.lstrip()): cnt += 1
					# elif stringN.rstrip().endswith(sN.rstrip()): cnt += 1

				elif '*x' in code_switch:
					if string.endswith(sN.rstrip()):
						cnt += 1
				elif 'x*' in code_switch:
					if string.startswith(sN.lstrip()):
						cnt += 1
				else:
					if sN in stringN:
						# print(sN, stringN); sys.exit(0)
						cnt += 1
					elif len(s) == 1 and sN in string:
						cnt += 1  # fallback for 1-char token
					

			if length == cnt:
				result = True
				break
			if plusOr and cnt > 0:
				result = True


		# for s in plusList:
		#     sN=' '+s+' '
		#     if '=' in sw.PlusCode:
		#         if string == s:
		#             cnt += 1
		#     # elif len(s) > 1 and s[0] == '*':
		#     elif '*x' in sw.PlusCode:
		#         if string.endswith(s):
		#             cnt += 1
		#     # elif len(s) > 1 and s[-1] == '*':
		#     elif 'x*' in sw.PlusCode:
		#         if string.startswith(s):
		#             cnt += 1
		#     else:
		#         # if s in string: cnt += 1
		#         if sN in stringN: cnt += 1
		#     # if 'opus' in string:
		#     #   print_(cnt, string)
		#     if length == cnt:
		#         result = True
		#         break
		#     if plusOr:
		#         if cnt > 0:
		#             result = True
		# print(cnt)
		return result







	def positiveResults(self, string, plus='', plusOr=False, end=None, OR=None):
		""" Processes string with 'Plus' functionality. """
		string = str(string)
		plusInput = self.getPlusInput(plus, plusOr, OR)
		# print(plusInput, 'plusInput')
		self.showLine_list = plusInput
		# print(plusInput);sys.exit(0)
		# Apply `ci` to all elements of plusInput if it is a list
		if isinstance(plusInput, list):
			plusInput = [self.ci(x) if isinstance(x, str) else [self.ci(i) for i in x] for x in plusInput]
		if end is not None:
			plusInput = [x + end if isinstance(x, str) else [xi + end for xi in x] for x in plusInput]

		# print(plusInput)
		result = False
		StrictCase = {
			'i': False
		}
		if 'StrictCase' in self.switch_dict and self.switch_dict['StrictCase']:
			if 'i' in self.switch_dict['StrictCase']: StrictCase['i'] = True
		# print(StrictCase)
		# print(plusInput)
		if not StrictCase['i']:
			# print('here')
			# string = string.lower()
			if len(plusInput) == 1 and type(plusInput[0]) == list:
				plusInput = plusInput[0]
			cnt = 0
			# if not 'def getsome' in plusInput:
			#     print(self.run, plusInput,string)
			for s in plusInput:
				# print(s)
				s = str(s)
				if '*' in s:
					if s.startswith('*'):
						s = s[1:]
						if string.endswith(s):
							cnt += 1
					elif s.endswith('*'):
						s = s[:-1]
						if string.startswith(s):
							cnt += 1
				else:
					global appReg
					# if _.switches.isActive('StrictCase'):
					# print(s, string, self.isActive('StrictCase') , appReg, self.active['StrictCase'])
					if s in string:
						# print('here', s, string)
						cnt += 1
			if cnt == len(plusInput) or self.isActive('PlusOr') and cnt > 0:
				result = True
		elif StrictCase['i']:
			plusList = [self.ci(x if not self.switch_dict.get('StrictCase') else x) if isinstance(x, str) else ' '.join([xi for xi in x]) for x in plusInput]
			for s in plusList:
				s = str(s)
				if '*' in s:
					if s.startswith('*'):
						s = s[1:]
						if string.endswith(s):
							return True
					elif s.endswith('*'):
						s = s[:-1]
						if string.startswith(s):
							return True
				else:
					if s in string:
						return True
		return result

	def minusResults(self, string, minus='', itIs=False):
		""" Processes string with 'Minus' functionality. """
		# print('minusResults')
		testMode = False
		testModeInt = False
		# if 'myNotes' in string: testMode = True

		if testModeInt: print(11)

		string = str(string)

		minusInput = self.getMinusInput(minus)
		if minusInput and type(minusInput) == list and type(minusInput[0]) == list:
			minusInput = minusInput[0]
		if isinstance(minusInput, str):
			minusInput = [minusInput]
		if not 'StrictCase' in self.switch_dict or not self.switch_dict['StrictCase']:
			string = string.lower()

			for i, m in enumerate(minusInput):
				minusInput[i] = str(m).lower()
		if testMode:
			print('minusInput:', minusInput, self.run)

		# if not self.run == 510:
		#     print(self.run,minusInput)
		result = True

		# If 'itIs' flag is set, treat exact matches
		if itIs:
			for row in minusInput:
				if string == row:
					return False
				
		if testModeInt: print(22)


		def asterisk(search,string):
			if not '*' in search: return None
			string = string.strip()
			if search.startswith('*'):
				search = search[1:]
				if string.endswith(search):
					return True
			elif search.endswith('*'):
				search = search[:-1]
				if string.startswith(search):
					return True
			return False

		# Iterate through each element in minusInput
		done = False
		# print(self.run,minusInput, string,self.run)
		for s in minusInput:
			if done:
				break
			if s is None:
				continue
			
			if isinstance(s, list):
				# print(s, string)
				for x in s:
					# print(x)
					if x in string:
						result = False
						done=True
						break
			else:
				if '*' in s:
					star = asterisk(s, string)
					if star == True:
						result = False
						done = True
						break

				if s in string:
					result = False
					done = True
					break
		# print(4)
		if testModeInt: print(33)
		if testMode:
			print('minusInput:', minusInput, result)
			# print('string:', string)
			# sys.exit(0)
		return result

	def getPlusInput(self, plus, plusOr, OR):
		""" Returns the appropriate plus input list based on conditions. """
		if plusOr or self.isActive('PlusOr'):
			plusOr = True

		if OR is not None:
			plusOr = OR

		if plus != '':
			plusInput = [plus]
		else:
			plusInput = self.switch_dict.get('plus', self.switch_dict.get('Plus', [])).copy()
		return plusInput

	def getMinusInput(self, minus):
		""" Returns the appropriate minus input list. """
		if minus != '':
			return [minus]
		else:
			return self.switch_dict.get('minus', self.switch_dict.get('Minus', [])).copy()


	def closeResults(self, string):
		""" Handle closing results when 'PlusClose' is active. """
		string = str(string)
		return False

	def prWC2(self, string, by):
		""" Modify the string with the prWC2 function. """
		string = str(string)
		return string

	def ci(self, string):
		""" Case insensitive handling for strings and allows modification of switch values. """
		if isinstance(string, list):
			return [self.ci(x) for x in string]  # Recursive case to handle nested lists
		else:
			string = str(string)
			string = ci(string)
			# print(self.isActive('StrictCase'))
			# if not self.isActive('StrictCase') == True:
			if 'StrictCase' in self.active and  not self.isActive('StrictCase') == True:
				string = string.lower()
		return string


	def color(self, code, keywords=None, color="blue"):
		"""
		Colorizes the code by wrapping keywords in ANSI escape codes with a specified color.
		Case-insensitive search for keywords.

		Args:
			code (str): The code to be colorized.
			keywords (list): A list of keywords or patterns to search for.
			color (str): The color to use for the keywords.

		Returns:
			str: The colorized code.
		"""

		# If no keywords are provided and 'Plus' switch is available in switch_dict, use its value
		if keywords is None:
			if self.switch_dict and self.switch_dict.get('Plus', None):
				keywords = self.switch_dict['Plus']
			else:
				return code  # Return code unchanged if no keywords or 'Plus' found

		# If keywords are not empty and are a list
		if isinstance(keywords, str):
			keywords = [keywords]  # Ensure keywords are a list if a single keyword is passed
		
		if not keywords:
			return code  # Return code unchanged if no valid keywords

		# Select color code from the Color class based on the input color
		global color_map

		color_code = color_map.get(color, Color.blue)  # Default to blue if invalid color
		import re
		# Create a pattern that matches each keyword case-insensitively
		pattern = '|'.join([re.escape(keyword) for keyword in keywords])

		# This function will wrap the matched keyword with the terminal color codes
		def colorize_match(match):
			return f'{color_code}{match.group(0)}{Color.end}'  # Add reset color after match

		# Use re.sub() to replace matched keywords with colorized ANSI codes
		colorized_code = re.sub(pattern, colorize_match, code, flags=re.IGNORECASE)

		return colorized_code



class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'

color_map = {
	"purple": Color.purple,
	"cyan": Color.cyan,
	"darkcyan": Color.darkcyan,
	"blue": Color.blue,
	"green": Color.green,
	"yellow": Color.yellow,
	"red": Color.red,
	"bold": Color.bold,
	"underline": Color.underline
}

def color(*args, c=None, p=True):
	if not args:
		return ''
	text = ' '.join(map(str, args))
	if c:
		color_code = color_map.get(c, Color.blue)
		text = f'{color_code}{text}{Color.end}'
	if p:
		print(text)
	return text
# # Usage example
# switches = SwitchManager()  # Assuming this is your switch manager
# LINE = Line(switches)
# LINE.show(line)
# # Automatically populate the switch_dict by checking the active switches
# switch_settings = line_processor.setSwitches()

# # Example usage of showLine with auto-populated switches
# result = line_processor.showLine("Example string", switch_dict=switch_settings)
# print(result)

#abc123 end new
##################################################
##################################################

##################################################
##################################################



import sys
from io import StringIO

if not sys.stdin.isatty():
	stdin_data = sys.stdin.read()
	sys.stdin = StringIO(stdin_data)  # Replace with in-memory stream
	# PIPE = [line for line in sys.stdin if line]
	PIPE = [line.rstrip() for line in sys.stdin]
	sys.stdin.seek(0)  # Reset pointer for reuse
else:
	PIPE = []






##################################################
ForcePipe = False
import sys
if '--pipe' in sys.argv:
	if not sys.stdin.isatty():
		ForcePipe = sys.stdin.read()
		if type(ForcePipe) == str:
			ForcePipe = ForcePipe.split('\n')
		

##################################################

# earthy_tones oceanic pastel warm_bold autumn midnight
# spring earthy_tones oceanic pastel warm_bold autumn
# midnight spring2 volcano frosty desert forest rainbow
# mystic industrial rustic sci_fi victorian retro
isData_Switches = {}
CodeTheme = 'retro'

##################################################
def isGui():
	import platform
	if platform.system() == "Windows":
		return True
	else:
		display_var = os.getenv('DISPLAY')
		if display_var:
			return True
	return False
##################################################
def Form(form):
	from _rightThumb._forms import genForm
	results = genForm(form)
	return results
#################################################
prFn  = None
def pr( *args, **kwargs ):
	global prFn
	if prFn is None:
		from _rightThumb._base3 import print_
		prFn = print_
	return prFn( *args, **kwargs )
#################################################
startTraceRecords = []
def startTrace(search='widgets'):
	global startTraceRecordsSearch
	startTraceRecordsSearch = search

	import sys
	def trace_calls(frame, event, arg):
		if event == 'call':
			global startTraceRecordsSearch
			global startTraceRecords
			code = frame.f_code
			func_name = code.co_name
			func_line_no = frame.f_lineno
			filename = code.co_filename
			if not startTraceRecordsSearch:
				startTraceRecords.append({'function':func_name,'line':func_line_no,'file':filename})
			elif type(startTraceRecordsSearch) == str and startTraceRecordsSearch.strip() and startTraceRecordsSearch in func_name:
				startTraceRecords.append({'function':func_name,'line':func_line_no,'file':filename})

				# print(f'Calling function: {func_name} in {filename}:{func_line_no}')
		return trace_calls

	sys.settrace(trace_calls)

def endTrace(functions=None,a=False):
	sys.settrace(None)
	table = {}
	for record in startTraceRecords:
		shouldPrint = True
		if functions is not None:
			shouldPrint = False
			for file in functions:
				if record['file'].endswith(file):
					for function in functions[file]:
						if record['function'] == function:
							shouldPrint = True
		if shouldPrint:
			if a:
				print(f'{record["function"]} in {record["file"]}:{record["line"]}')
			else:
				if not record['file'] in table:
					table[record['file']] = {}
				if not record['function'] in table[record['file']]:
					table[record['file']][record['function']] = 0
				if table[record['file']][record['function']] == 0:
					print(f'{record["function"]} in {record["file"]}:{record["line"]}')
#################################################
def print_table1(data,title=None):
	from pprint import pprint

	def print_single_table(rows, title=None):
		if not rows:
			print(f"\n{title or 'Table'}: (empty)\n")
			return

		headers = list(rows[0].keys())
		col_widths = {h: max(len(h), *(len(str(row.get(h, ''))) for row in rows)) for h in headers}
		line = ' | '.join(f'{h:<{col_widths[h]}}' for h in headers)

		if title:
			print(f"\n{title}\n{'=' * len(title)}")

		print(line)
		print('-' * len(line))

		for row in rows:
			print(' | '.join(f'{str(row.get(h, "")):<{col_widths[h]}}' for h in headers))

	if isinstance(data, list):
		print_single_table(data)
	elif isinstance(data, dict):
		for key, value in data.items():
			if isinstance(value, list):
				print_single_table(value, title=str(key))
			else:
				print(f"\n{key}:\n(Not a list, skipping)")
	else:
		print("Unsupported data type.")



def align(text, align='center', width=None):
	def center(text, width):
		if type(width) != int:
			width = len(width)
		if width <= len(text):
			return text
		# x = (width - len(text)) // 2
		# return ' ' * x + text + ' ' * (width - len(text) - x)
		return text.center(width)

	def right(text, width):
		if type(width) != int:
			width = len(width)
		if width <= len(text):
			return text
		return ' ' * (width - len(text)) + text

	def left(text, width):
		if type(width) != int:
			width = len(width)
		if width <= len(text):
			return text
		return text + ' ' * (width - len(text))

	if 'c' in align:
		return center(text, width)
	elif  'r' in align:
		return right(text, width)
	elif  'l' in align:
		return left(text, width)
	else:
		return text


def dicGen(ns, val=None, dic=None, default=None):
	"""
	Creates/updates or retrieves a value from a nested dictionary using a dotted path.

	Args:
		ns (str): Dot-separated keys for the nested structure.
		val (optional): The value to set at the final key. If None, the function
						will return the value instead of setting it.
		dic (dict, optional): The dictionary to update or search in. If None, creates a new one.

	Returns:
		dict or value: If val is given, returns the updated dict.
					   If val is None, returns the value at the path or None if not found.
	"""
	if dic is None:
		dic = {}

	keys = ns.split(".")
	current = dic

	if val is None:  # GET MODE
		for key in keys:
			if isinstance(current, dict) and key in current:
				current = current[key]
			else:
				return default
		return current

	# SET MODE
	for key in keys[:-1]:
		if key not in current or not isinstance(current[key], dict):
			current[key] = {}
		current = current[key]

	current[keys[-1]] = val
	return dic



# # Example usage:
# settings = dicGen('fields.cols.help.case', 'upper')
# settings = dicGen('fields.cols.help.align', 'center', settings)
# settings = dicGen('fields.cols.help.trigger', lambda: print("Triggered!"), settings)

# print(settings)

# settings = { 'fields': { 'title': {...}, 'heading': {...}, 'cols': {colName: {...}} } }

def render_table(data, title=None, settings=None, pre=5, p=True):
	# --- normalize settings to a dict and extract fields ---
	if callable(settings):
		try:
			settings = settings()  # allow zero-arg factory
		except TypeError:
			settings = {}
	if not isinstance(settings, dict):
		settings = {}
	fields = settings.get('fields', {}) if isinstance(settings.get('fields', {}), dict) else {}

	out = []
	prefix = (' ' * pre) if isinstance(pre, int) else (pre if isinstance(pre, str) else '')

	# --- helpers that read your native structure ---
	def _field_case(kind=None, col=None, default=None):
		if col is not None:
			return fields.get('cols', {}).get(col, {}).get('case', default)
		if kind in ('title', 'heading'):
			return fields.get(kind, {}).get('case', default)
		return default

	def _field_align(kind=None, col=None, default=None):
		if col is not None:
			return fields.get('cols', {}).get(col, {}).get('align', default)
		if kind in ('title', 'heading'):
			return fields.get(kind, {}).get('align', default)
		return default

	def _field_trigger(col):
		"""Optional per-col value transformer. Must be a callable(v, row, col)."""
		trig = fields.get('cols', {}).get(col, {}).get('trigger')
		if callable(trig):
			return trig
		# also tolerate a 1-arg callable(v)
		if callable(trig):
			try:
				return lambda v, row=None, c=None: trig(v)
			except TypeError:
				pass
		return lambda v, row=None, c=None: v

	def _change_case(text, mode):
		if text is None:
			return ''
		s = str(text)
		if not s.strip() or not mode:
			return s
		if mode == 'upper':  return s.upper()
		if mode == 'lower':  return s.lower()
		if mode == 'title':  return s[:1].upper() + s[1:]
		return s

	def _cell_value(col, row):	
		trig = _field_trigger(col)
		raw = row.get(col, '')
		val = trig(raw, row, col)
		val = _change_case(val, _field_case(col=col))
		return str(val)

	def build_single_table(rows, maybe_title=None):
		if not rows:
			out.append(f"{prefix}{maybe_title or 'Table'}: (empty)")
			out.append("")
			return

		headers = list(rows[0].keys())

		# Compute widths AFTER triggers/case so alignment fits final text
		col_widths = {}
		for h in headers:
			max_data = max((len(_cell_value(h, r)) for r in rows), default=0)
			col_widths[h] = max(len(str(h)), max_data)

		width = sum(col_widths[h] for h in headers) + 3 * (len(headers) - 1)

		# Title
		if maybe_title:
			t = _change_case(maybe_title, _field_case(kind='title', default='title'))
			t = align(t, _field_align(kind='title', default='center'), width)
			out.append(prefix + color(t, c='yellow', p=0))
			out.append(prefix + color('=' * width, c='purple', p=0))

		# Header row
		sep = color(' | ', c='green', p=0)
		head_cells = []
		for h in headers:
			hh = _change_case(h, _field_case(kind='heading', default='title'))
			hh = align(hh, _field_align(kind='heading', default='center'), col_widths[h])
			head_cells.append(color(hh, c='bold', p=0))
		out.append(prefix + sep.join(head_cells))
		out.append(prefix + color('-' * width, c='darkcyan', p=0))

		# Rows
		cell_sep = color(' | ', c='bold', p=0)
		for row in rows:
			cells = []
			for h in headers:
				txt = _cell_value(h, row)
				txt = align(txt, _field_align(col=h, default='left'), col_widths[h])
				cells.append(color(txt, c='cyan', p=0))
			out.append(prefix + cell_sep.join(cells))
		out.append("")

	if isinstance(data, list):
		build_single_table(data, title)
	elif isinstance(data, dict):
		for k, v in data.items():
			if isinstance(v, list):
				build_single_table(v, str(k))
			else:
				out.append(f"{prefix}{k}:")
				out.append(f"{prefix}(Not a list, skipping)")
				out.append("")
	else:
		out.append(prefix + "Unsupported data type.")
		out.append("")
	if p:
		print('\n'.join(out))
	return out


pt=render_table
#################################################

trig = {}
class SwitchManager:
	def __init__(self, Switches=None, Triggers=None, Help=None, command=None, c=None, cmd=None):
		if not cmd is None: command = cmd
		if not c is None: command = c
		if command is None and Switches is None and Triggers is None:
			color("SwitchManager args:     Switches, Triggers, command",c='red',p=1)
			command = sys.argv[1:] if len(sys.argv) > 1 else []
		if isinstance(command, int):
			command = sys.argv[command:]
		elif isinstance(command, str):
			command = command.replace('  ', ' ').split(' ')
		elif not command:
			command = sys.argv

		self.command = command
		self.app = command[0]
		self.args = command[1:]

		if Switches is None:
			Switches = {}
		if Triggers is None:
			Triggers = {}
		self.triggers = {**Triggers}
		if Help is None: Help = {}
		self.Help = Help
		self.Switches = Switches
		self.possibleList()

		self.switchesRegister = self._flatten_switches(self.Switches)
		if not 'Help' in self.switchesRegister:
			self.switchesRegister['Help'] = '?,-h,--help,?h,?help'
		if not 'Help' in self.triggers:
			self.triggers['Help'] = self.help

		self.used = {}
		self._Values = {}
		self.usage = {}
		self.instances = {}

		# ---------- ADDED for occurrence grouping ----------
		# Per-occurrence buckets and order per switch
		# _occ_buckets: { name: { flag: [ [vals1], [vals2], ... ] } }
		# _occ_sequence: { name: [ (flag, idx), ... ] } in the order seen
		self._occ_buckets = {}
		self._occ_sequence = {}
		# ---------------------------------------------------

		self.flag_to_key = {}
		for key, val in self.switchesRegister.items():
			self.used[key] = False
			self._Values[key] = []
			if isinstance(val, str):
				val = ' '.join(val.split()).replace(' ', ',')
				self.switchesRegister[key] = val
			for flag in self.switchesRegister[key].split(','):
				self.flag_to_key[flag] = key

		self.parse()
		if 'Help' in self.usage:
			if 'Help' in self._Values and self._Values['Help'] and type(self._Values['Help']) == list:
				self.triggers['Help'](self._Values['Help'][0])
			else:
				self.triggers['Help']()

		# self.usage[key].append(flag)
		# self._Values[key].append(flag)

	def help(self,full=None):
		if full:
			self.validate()
			print('\n\n')

		isGrouped = False
		if type(self.Switches[next(iter(self.Switches))]) == dict:
			isGrouped = True
		
		if not isGrouped:
			table = []
			for key in self.Switches:
				rec = {}
				rec['name'] = key
				rec['switch'] = self.Switches[key]
				if self.Help:
					if key in self.Help:
						rec['help'] = self.Help[key]
					else:
						rec['help'] = ''
				table.append(rec)

			# settings = dicGen('fields.cols.help.case', 'upper')
			pt(table,'switches',settings)

		elif isGrouped:

			tables = {}
			for group in self.Switches:
				tables[group] = []
				for key in self.Switches[group]:
					rec = {}
					rec['name'] = key
					rec['switch'] = self.Switches[group][key]
					if self.Help:
						if key in self.Help:
							rec['help'] = self.Help[key]
						else:
							rec['help'] = ''
					tables[group].append(rec)
			pt(tables,'switches')
		sys.exit(0)



	def possibleList(self):
		isGrouped = False
		if type(self.Switches[next(iter(self.Switches))]) == list:
			isGrouped = True
		elif not type(self.Switches) == list: return
		global trig

		Switches = self.Switches.copy()
		self.Switches = {}

		if not isGrouped:
			for rec in Switches:
				self.Switches[rec['n']] = rec['s']
				if 't' in rec:
					if type(rec['t']) == str:
						if rec['t'] in globals() and callable(globals()[rec['t']]):
							rec['t'] = eval(rec['t'])
						elif rec['t'] in trig and callable(trig[rec['t']]):
							rec['t'] = trig[rec['t']]
					self.triggers[rec['n']] = rec['t']
				if 'h' in rec:
					self.Help[rec['n']] = rec['h']

		elif isGrouped:
			for group in Switches:
				self.Switches[group] = {}
				for rec in Switches[group]:
					self.Switches[group][rec['n']] = rec['s']
					if 't' in rec:

						if type(rec['t']) == str:
							if rec['t'] in globals() and callable(globals()[rec['t']]):
								rec['t'] = eval(rec['t'])
							elif rec['t'] in trig and callable(trig[rec['t']]):
								rec['t'] = trig[rec['t']]
						self.triggers[rec['n']] = rec['t']
					if 'h' in rec:
						self.Help[rec['n']] = rec['h']

	def _flatten_switches(self, switches):

		flat = {}
		for group_or_key, val in switches.items():
			if isinstance(val, dict):
				flat.update(val)
			else:
				flat[group_or_key] = val
		return flat

	def _clean_quotes(self, value):
		if not isinstance(value, str):
			return value
		for quote in ["'", '"']:
			if value.startswith(quote * 2) and value.endswith(quote * 2):
				value = value[2:-2]
			elif value.startswith(quote) and value.endswith(quote):
				value = value[1:-1]
		return value

	def unset(self, name, instance=None):
		"""Clear usage data for a switch, optionally just for one instance (flag)."""
		if name in self.used:
			self.used[name] = False

		if instance is None:
			self._Values[name] = []
			self.usage.pop(name, None)

			# ---------- ADDED for occurrence grouping ----------
			self._occ_buckets.pop(name, None)
			self._occ_sequence.pop(name, None)
			# ---------------------------------------------------

			self.instances.pop(name, None)
		else:
			if name in self.usage:
				self.usage[name] = [i for i in self.usage[name] if i != instance]
				if not self.usage[name]:
					self.usage.pop(name)
			if name in self.instances and instance in self.instances[name]:
				self.instances[name].pop(instance)
			if name in self.instances and not self.instances[name]:
				self.instances.pop(name)

			# ---------- ADDED for occurrence grouping ----------
			if name in self._occ_buckets and instance in self._occ_buckets[name]:
				# Drop sequence entries referencing this flag
				if name in self._occ_sequence:
					self._occ_sequence[name] = [
						(f, idx) for (f, idx) in self._occ_sequence[name] if f != instance
					]
					if not self._occ_sequence[name]:
						self._occ_sequence.pop(name)
				self._occ_buckets[name].pop(instance)
				if not self._occ_buckets[name]:
					self._occ_buckets.pop(name)
			# ---------------------------------------------------

			# Don't clear _Values if other instances remain
			self._Values[name] = [
				val for inst in self.instances.get(name, {}).values() for val in (inst if isinstance(inst, list) else [])
			] if name in self.instances else []

	def set(self, name, flag=None, values=None, add=False):
		"""Add switch usage manually (values can be list or single)."""

		# next(iter(self.Switches))
		if type(flag) == int:
			if name in self.switchesRegister:
				flag = self.switchesRegister[name].split(',')[flag].strip()
				flagFixed = True
		elif not flag:
			flagFixed = False
			if name in self.instances:
				flag = next(iter(self.instances[name]))
				flagFixed = True
			if not flagFixed and name in self.switchesRegister:
				flag = self.switchesRegister[name].split(',')[0].strip()
				flagFixed = True

		if not add:
			self.unset(name, flag)

		self.used[name] = True
		if name not in self._Values or self._Values[name] is True:
			self._Values[name] = []
		if isinstance(values, str):
			values = [values]
		elif values is None:
			values = []

		if name not in self.usage:
			self.usage[name] = []
		if flag not in self.usage[name]:
			self.usage[name].append(flag)

		if name not in self.instances:
			self.instances[name] = {}
		if flag not in self.instances[name]:
			self.instances[name][flag] = []

		# ---------- ADDED for occurrence grouping ----------
		if name not in self._occ_buckets:
			self._occ_buckets[name] = {}
		if flag not in self._occ_buckets[name]:
			self._occ_buckets[name][flag] = []
		# Start a new occurrence bucket if we're not "adding" to an existing one
		if not add or not self._occ_buckets[name][flag]:
			self._occ_buckets[name][flag].append([])
			if name not in self._occ_sequence:
				self._occ_sequence[name] = []
			self._occ_sequence[name].append((flag, len(self._occ_buckets[name][flag]) - 1))
		# ---------------------------------------------------

		for val in values:
			cleaned = self._clean_quotes(val)
			if name in self.triggers:
				cleaned = self.triggers[name](cleaned)
			self._Values[name].append(cleaned)
			self.instances[name][flag].append(cleaned)

			# ---------- ADDED for occurrence grouping ----------
			self._occ_buckets[name][flag][-1].append(cleaned)
			# ---------------------------------------------------

	def parse(self,args=None, reset=False):
		current_switch = None
		current_key = None
		i = 0

		if args is None:
			args = self.args

		while i < len(args):
			arg = self.args[i]

			# Handle --flag=value format
			if arg.startswith('--') and '=' in arg:
				flag, val = arg.split('=', 1)
				key = self.flag_to_key.get(flag)
				if key:
					current_key = key
					current_switch = flag
					self._register_usage(key, current_switch)
					values = val.split(',')
					for v in values:
						value = self.triggers[key](v) if key in self.triggers else v
						value = self._clean_quotes(value)
						self._Values[key].append(value)
						self.instances[key][current_switch].append(value)

						# ---------- ADDED for occurrence grouping ----------
						self._occ_buckets[key][current_switch][-1].append(value)
						# ---------------------------------------------------

			# Handle standalone flags like -pulldown or -m
			elif arg in self.flag_to_key:
				key = self.flag_to_key[arg]
				current_key = key
				current_switch = arg
				self._register_usage(key, current_switch)
				if self._Values[key] == []:
					self._Values[key] = True

			# Handle values passed after a flag
			elif current_key and current_switch:
				if self._Values[current_key] is True:
					self._Values[current_key] = []
				value = self.triggers[current_key](arg) if current_key in self.triggers else arg
				value = self._clean_quotes(value)
				self._Values[current_key].append(value)
				self.instances[current_key][current_switch].append(value)

				# ---------- ADDED for occurrence grouping ----------
				self._occ_buckets[current_key][current_switch][-1].append(value)
				# ---------------------------------------------------

			# Orphan value (no active flag) — ignored, or could log
			else:
				pass

			i += 1

	def _register_usage(self, key, flag):
		self.used[key] = True
		if key not in self.instances:
			self.instances[key] = {}
		if flag not in self.instances[key]:
			self.instances[key][flag] = []
		if key not in self.usage:
			self.usage[key] = []
		if flag not in self.usage[key]:
			self.usage[key].append(flag)

		# ---------- ADDED for occurrence grouping ----------
		if key not in self._occ_buckets:
			self._occ_buckets[key] = {}
		if flag not in self._occ_buckets[key]:
			self._occ_buckets[key][flag] = []
		# start a NEW bucket for this occurrence
		self._occ_buckets[key][flag].append([])
		occ_idx = len(self._occ_buckets[key][flag]) - 1

		if key not in self._occ_sequence:
			self._occ_sequence[key] = []
		self._occ_sequence[key].append((flag, occ_idx))
		# ---------------------------------------------------

	def isActive(self, name, instance=None):
		if name not in self.used or not self.used[name]:
			return False
		if instance is None:
			return True
		return instance in self.usage.get(name, [])

	def data(self, what, name, instance=None):
		if what == 0: what = 'name'
		elif what == 1: what = 'data'
		val = self.values(name, instance)
		if not val:
			global PIPE
			return PIPE if PIPE else []
		elif what == 'data':
			os=imp('os.path.isfile')
			if os.path.isfile(val[0]):
				with open(val[0], 'r') as f:
					return f.read().splitlines()
			return val

		return val

	def values(self, name, instance=None):
		if not instance is None: return self.Values(name, instance)
		val = self._Values.get(name, [])
		if val is True:
			return []
		return val

	def value(self, name):
		vals = self.values(name)
		if len(vals) == 1:
			return vals[0]
		return ','.join(vals)

	def Values(self, name, instance=None):
		if name not in self.instances:
			return []
		if instance is not None:
			return self.instances[name].get(instance, [])
		return self.values(name)

	# ---------- ADDED: accessor for grouped-by-occurrence ----------
	def Instances(self, name, instance=None):
		"""
		Return grouped occurrences for a switch.

		- Instances('Has') -> list of lists in global occurrence order across all flags
		- Instances('Has', '-and') -> list of lists for that flag only (each occurrence)
		- Instances('Has', '-or') -> list of lists for that flag only
		"""
		if name not in self._occ_buckets:
			return []
		if instance is None:
			if name not in self._occ_sequence:
				return []
			out = []
			for (flag, idx) in self._occ_sequence[name]:
				bucket_list = self._occ_buckets[name].get(flag, [])
				if 0 <= idx < len(bucket_list):
					out.append(bucket_list[idx])
			return out
		else:
			return list(self._occ_buckets[name].get(instance, []))
	# ---------------------------------------------------------------

	def strip(self):
		return [item for item in self.command if item not in self.flag_to_key]

	def resetState(self):
		self.used = {}
		self._Values = {}
		self.usage = {}
		self.instances = {}
		# ---------- ADDED for occurrence grouping ----------
		self._occ_buckets = {}
		self._occ_sequence = {}
		# ---------------------------------------------------
		for key in self.switchesRegister:
			self.used[key] = False
			self._Values[key] = []

	def validate(self):
		import json
		color('___________\nApp:',c='cyan')
		color(self.app, c='yellow')
		color('___________\nUsed:',c='cyan')
		color(json.dumps(self.used, indent=4), c='yellow')
		color('___________\nValues:',c='cyan')
		color(json.dumps(self._Values, indent=4), c='yellow')
		color('___________\nUsage:',c='cyan')
		color(json.dumps(self.usage, indent=4), c='yellow')
		color('___________\nInstances:',c='cyan')
		color(json.dumps(self.instances, indent=4), c='yellow')

	def dump(self):
		return {
			'command': self.command,
			'app': self.app,
			'used': self.used,
			'values': self._Values,
			'usage': self.usage,
			'instances': self.instances
		}



Switches = SwitchManager
#################################################




preSwitches = []
site_url=None
autoCreationConfiguration = {
							'backup': True,
							'logs': True,
							'folders': True,
							'created': { '_vars': 0 },
}

settings_table = {
					#t)--> edit: 1661227949.7667239
					'receipt-log': True,
					'receipt-file': True,
					'default-switches': True,
}
UnixCopy = 'xsel'
truePath = False
truePath = True
isHeaders = {
	# IS(path, 'gz')
	'gzip': '1F 8B 08 08',
	'docx': [
		'50 4B 03 04',
		'50 4B 05 06',
	],
	'isCrypt': '41 45 53 02 00 00 1B',
	'gz': '1F 8B 08 08',
	'bz2': '42 5A 68',
}
import time,signal,sys,platform
tz = str(time.strftime("%z")).replace(':','')
try:
	signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
except:
	sys.exit(0)

banner=None
def _local_(do): print('not registered')


def name(path):
	path=path(path)
	par=path.split(os.sep)
	par.reverse()
	app=par[0]
	fo=par[1]
	root=par[2]
	app=app.replace('.py','')
	if app == '__init__': app=root+'.'+fo
	return app



def settings( subjects, d=None, val='71e9-a678' ):
	results = []
	for subject in subjects:
		results.append(  setting( subject, val, d )  )
	return results

def setting( subject, val='71e9-a678', d=None, default=None ):
	global settings_table

	if not default is None:
		d = default

	if not val == '71e9-a678':
		settings_table[subject] = val

	if not subject in settings_table:
		return d
	
	return settings_table[subject]


releaseAcquiredData = True

table_b_print = True

switch_raw = []


thisOS = platform.system()
theOS = thisOS
OS = theOS
windowsSlash = chr(92)
unixSlash = chr(47)

if thisOS == 'Windows':
	slash = windowsSlash
	isWin  = True
else:
	slash = unixSlash
	isWin  = False

class dot:
	def __init__( self ):
		pass

v = Meta_Namespace()

LOOP = {}

def pathList( *paths ):
	# os = imp('os')
	result = os.sep.join(paths)
	result = result.replace( '/', os.sep )
	result = result.replace( '\\', os.sep )
	result = result.replace( os.sep+os.sep, os.sep )
	result = result.replace( os.sep+os.sep, os.sep )
	result = result.replace( 'tech'+os.sep+'tech', 'tech' )
	return result

def p( *text, w='' ):
	texXxt = []
	for x in text:
		texXxt.append(str(x))
	txt = ' '.join( texXxt )
	
	if w:
		# os = imp('os')
		if os.path.isfile(w):
			file1 = open( w , 'a' )
			file1.write( txt+'\n' )
			file1.close()
		else:
			file1 = open( w , 'w' )
			file1.write( txt+'\n' )
			file1.close()
	print(txt)



def xit():
	sys.exit()

specifications = {}
did_table = {}
def uuid():
	UUID = imp('uuid')
	return str(UUID.uuid4())












# import os
# import sys
# import importlib

# Helper function to dynamically import modules using dot notation
def dots(path):
	def _dots_(pth):
		try:
			exec(pth)
			return True
		except Exception:
			return False

	parts = path.split('.')
	exec(f'global {parts[0]}')
	
	if _dots_(path):
		return eval(parts[0])

	pre, temp_path = [], []
	for i, segment in enumerate(parts):
		pre = temp_path.copy()
		temp_path.append(segment)
		namespace_prefix = '.'.join(pre)
		current_path = '.'.join(temp_path)

		if i == len(parts) - 1:
			# Import the final segment from the package
			exec(f'from {namespace_prefix} import {parts[-1]}')
			assignment = f'{path} = {parts[-1]}'
		else:
			# Create a dynamic namespace if it doesn't exist
			assignment = f'{current_path} = Meta_Namespace()'

		if not _dots_(current_path):
			exec(assignment)
			if i == len(parts) - 1:
				return eval(parts[0])


# Import helpers
imp_table = {}

def imp(subject, imp_table_testing=False):
	try:
		return imp_run(subject, imp_table_testing)
	except ImportError:
		imp_install(subject)
		try:
			return imp_run(subject, imp_table_testing)
		except ImportError:
			imp_run2(subject)

# Install missing packages using pip
def imp_install(mod):
	mod = mod.split('.')[0]
	
	package_mapping = {
		'all': {},
		'win': {
			'magic': 'python-magic-bin==0.4.14',
		},
		'linux': {
			'magic': 'python-magic',
		},
	}

	# Check platform-specific package mapping
	if sys.platform == 'win32' and mod in package_mapping['win']:
		mod = package_mapping['win'][mod]
	elif sys.platform != 'win32' and mod in package_mapping['linux']:
		mod = package_mapping['linux'][mod]

	# Install the package
	os.system(f'pip install {mod} >nul 2>&1')

# Run secondary import
def imp_run2(subject):
	global importlib
	global imp_table
	if importlib is None:
		import importlib
	exec(f'import {subject}')
	imp_table[subject] = eval(subject)

# Main import runner
def imp_run(subject, imp_table_testing=False):
	global importlib
	if '.' in subject and '_rightThumb' not in subject:
		return dots(subject)

	global imp_table
	if subject in imp_table:
		return imp_table[subject]

	if importlib is None:
		import importlib

	try:
		imp_table[subject] = importlib.import_module(subject)
		if imp_table_testing:
			print('Module imported successfully:', subject)
		return imp_table[subject]
	except ImportError:
		if imp_table_testing:
			print('Failed to import module:', subject)
		return None

















# def dots(path):
# 	def _dots_(pth):
# 		try: exec(pth); return True;
# 		except Exception as e: return False;
# 	rts=path.split('.'); exec('global '+rts[0]);
# 	if _dots_(path): return eval(rts[0])
# 	pre=[]; thp=[];
# 	for i,seg in enumerate(rts):
# 		pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
# 		if i == len(rts)-1:
# 			exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
# 			f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
# 		else: f='1=Meta_Namespace()'.replace('1',npath);

# 		if not _dots_(npath):
# 			exec(f)
# 			if i == len(rts)-1: return eval(rts[0]);


try:
	importlib
except Exception as e:
	importlib = None
# imp_table = {}
# def imp( subject, imp_table_testing=False ):
# 	try:
# 		return imp_run( subject, imp_table_testing )
# 	except:
# 		imp_install(subject)
# 		try:
# 			return imp_run( subject, imp_table_testing )
# 		except:
# 			try:
# 				imp_run2( subject )
# 			except:
# 				print('unable to import:',subject)

# def imp_install(mod):
# 	mod = mod.split('.')[0]
# 	try:
# 		exec('import os')
# 	except Exception as e:
# 		raise e
# 	# print()
# 	# print('__.imp_install('+mod+')')
# 	# print()
# 	if '.' in mod: mod = mod.split('.')[0]

# 	dic = {
# 			'all': {},
# 			'win': {},
# 			'linux': {},
# 	}

# 	dic['win']['magic'] = 'python-magic-bin==0.4.14'
# 	dic['linux']['magic'] = 'python-magic'

# 	if       sys.platform == 'win32' and mod in dic['win']: mod = dic['win'][mod]
# 	elif not sys.platform == 'win32' and mod in dic['linux']: mod = dic['linux'][mod]
# 	elif mod in dic['linux']: mod = dic['all'][mod]


# 	if mod in dic: mod=dic[mod]

# 	os.system('pip3 install '+mod+' >nul 2>&1')
	
# 	# if sys.platform == 'win32':
# 	#     # os.system('pip3 install python-magic-bin==0.4.14')
# 	#     os.system('pip3 install '+mod+' >nul 2>&1')
# 	# else:

# 	#     def _pipy_(mod):
# 	#         mod0=mod
# 	#         try:
# 	#             import pip
# 	#             if '=' in mod: mod = mod.split('=')[0]
# 	#             pip.main(['install', mod])
# 	#         except: print('pip3 install '+mod0)
# 	#     import subprocess
# 	#     if len(subprocess.getoutput('sudo cat /etc/sudoers').split('\n')) > 3:
# 	#         try: os.system('sudo pip3 install '+mod+'  > /dev/null 2>&1')
# 	#         except: _pipy_(mod)
# 	#     else:
# 	#         try: os.system('pip3 install '+mod+'  > /dev/null 2>&1')
# 	#         except:_pipy_(mod)




# def imp_run2( subject ):
# 	global imp_table
# 	global importlib
# 	if importlib is None:
# 		import importlib
# 	exec( 'import '+subject )
# 	imp_table[subject] = eval(subject)

# def imp_run( subject, imp_table_testing=False ):
# 	# print(subject); sys.exit();
# 	if '.' in subject and not '_rightThumb' in subject: return dots(subject);
# 	global imp_table
# 	# if subject in imp_table: return imp_table[subject]
# 	global importlib
# 	if importlib is None:
# 		import importlib
# 		if imp_table_testing:
# 			print('\n\n\t\timport importlib\n\n')

# 	if not subject in imp_table:
# 		try:
# 			imp_table_tmp
# 		except Exception as e:
# 			pass
# 		else:
# 			del imp_table_tmp

# 		imp_table[subject] = importlib.import_module(subject)
# 		if imp_table_testing:
# 			print( 'imp.DID' )
# 		return imp_table[subject]

# 		# try:
# 		#     imp_table[subject] = importlib.import_module(subject)
# 		#     if imp_table_testing:
# 		#         print( 'imp.DID' )
# 		#     return imp_table[subject]
# 		# except Exception as e:
# 		#     if imp_table_testing:
# 		#         print( 'imp.NO' )
# 		#     return None
# 	if imp_table_testing:
# 		print( 'imp.YES' )
# 	return imp_table[subject]



on_exit_subjects = {}
def onExit(script,subject=None):
	global on_exit_subjects
	if subject is None:
		subject = uuid()
	on_exit_subjects[subject] = script
decompress_log = []
def isExit(fromKill=False):
	global on_exit_subjects
	global decompress_log
	for path in decompress_log:
		compress(path)

	for subject in on_exit_subjects:
		on_exit_subjects[subject]()
	if fromKill and not type(fromKill) == str:
		return True
	KILL()

def compress(path):
	os=imp('os.rename')
	os=imp('os.unlink')
	import gzip
	import shutil
	if IS(path,'gzip'): return False
	path = path(path)
	compressed_file_path = path
	original_file_path = path+'_temp'
	os.rename(path, original_file_path)
	with open(original_file_path, 'rb') as original_file:
		with gzip.open(compressed_file_path, 'wb') as compressed_file:
			shutil.copyfileobj(original_file, compressed_file)
	print(f"File compressed and saved to {compressed_file_path}")
	os.unlink(original_file_path)
def IS(path,check=1):
	path = path.strip()
	if not os.path.isfile(path): return False
	path = path2(path)
	global isHeaders
	if check in isHeaders.keys():
		check = isHeaders[check]
	header=" ".join(['{:02X}'.format(byte) for byte in     open( path, 'rb' ).read(32)    ])
	if check == 1: return header
	if type(check) == str:
		if header.startswith(check): return True
	elif type(check) == list:
		for c in check:
			if header.startswith(c): return True
	
	return False
def aliasesFi(path): return path

def wPath(_path):
	if not 'widgets' in _path: return _path
	# import _rightThumb._vars as _v
	# print(_path,_path.split('widgets'))
	x = _path.split('widgets')[2]
	# print(x)
	# w =_v.w+'/widgets'+x
	w = '/widgets'+x
	return w.replace('\\','/').replace('//','/').replace('\\\\','/')

def lpath(p):
	# reslolve full path but preserving aliases ln -s
	os = imp('os.sep')
	os = imp('os.path.exists')
	os = imp('os.path.abspath')
	os = imp('os.path.join')
	if type(p) == list:
		new = []
		for i,pp in enumerate(p):
			if type(pp) == str and os.path.exists(pp):
				new.append( lpath(pp) )
		return new
	if not os.path.exists(p):
		return p
	fo = os.environ.get('PWD', os.getcwd())
	if p == '.':
		p = fo
	if not os.sep in p:
		test = os.path.join(fo, p)
		if os.path.exists(test):
			p = test
	else:
		p = os.path.abspath(p)
	return p


def isLink(p):
	os = imp('os.path.abspath')
	os = imp('os.path.realpath')
	p = os.path.abspath(p)     # Get full path without resolving symlinks
	r = os.path.realpath(p)    # Get full path with symlinks resolved
	return p != r              # If they differ, symlinks exist in the path

def path( p, ab=True, pop=False, file=False, slash=None, folder=None, relative=False, fi=None, fo=None, fix=True, ln=None, r=None, R=None, a=None, w=False ):
	try:
		return pathRun( p, ab, pop, file, slash, folder, relative, fi, fo, fix, ln, r, R, a, w )
	except:
		return p

def pathRun( p, ab=True, pop=False, file=False, slash=None, folder=None, relative=False, fi=None, fo=None, fix=True, ln=None, r=None, R=None, a=None, w=False ):
	# print('___')
	# print(p)
	os = imp('os.environ')
	os = imp('os.sep')
	os = imp('os.path.exists')
	import platform
	if platform.system() == "Linux":
		if p == '.': p = os.environ.get('PWD', os.getcwd())
	if type(p) == list:
		new = []
		for i,pp in enumerate(p):
			# print(pp)
			if type(pp) == str and os.path.exists(pp):
				new.append( path(pp, ab, pop, file, slash, folder, relative, fi, fo, fix, ln, r, R, a) )
			# p[i] = path(pp, ab, pop, file, slash, folder, relative, fi, fo, fix, ln, r, R, a)
		return new
	
	if R or a:
		p = aliasesFi(p)
	
	

	p = p.replace('/', os.sep)
	if not r is None:
		relative = r
	os=imp('os.path.isfile')

	# if isLink(p):
	#     p = lpath(p)
	p = lpath(p)

	if relative:
		if not type(relative) == str:
			relative = os.getcwd()
		if relative.endswith('\\') or relative.endswith('/'):
			relative = relative[:-1]
		
		p = p.strip()
		if p.startswith(relative):
			p = p[len(relative)+1:]
		return p
	if not os.path.isfile(p) and not os.path.isdir(p): p = p.strip()
	if not os.path.isfile(p) and not os.path.isdir(p):
		if pop or folder:
			parts = p.split(os.sep)
			parts.pop(-1)
			p = os.sep.join(parts)
		if file:
			parts = p.split(os.sep)
			p = parts.pop(-1)
		return p
	os=imp('os.sep')
	p=p.replace(os.sep+os.sep,os.sep)
	if isWin or not pop: return _path_( p, ab, pop, file, slash, folder, fi, fo, fix, ln )
	# os=imp('os.path.abspath')
	# try: p1 = os.path.abspath(p)
	# except: pass

	# # comment to preserve aliases
	# # comment to preserve aliases
	# # comment to preserve aliases
	# os=imp('os.path.realpath')
	# try: p1 = os.path.realpath(p)
	# except: pass
	
	
	os=imp('os.path.abspath')
	try: p1 = os.path.abspath(p)
	except: pass

	p2 = _path_( p, ab, pop, file, slash, folder, fi, fo, fix, ln )
	if p1 == p2:
		parts = p1.split(os.sep)
		parts.pop(-1)
		return os.sep.join(parts)
	

	return p1
path2=path
def _path_( p, ab=True, pop=False, file=False, slash=None, folder=None, fi=None, fo=None, fix=True, ln=None ):
	
	p_bk=p
	# fix used in fileBackup.py

	if not fo is None: folder=fo;
	if not folder is None: pop=folder;
	if not fi is None: file=fi;


	# os = vc.FIG.imp('os')
	# os = imp('os')
	os=imp('os.sep')
	try: os.path.abspath
	except Exception as e: os=imp('os.path.abspath')
	try: os.path.isfile
	except Exception as e: os=imp('os.path.isfile')
	try: os.path.isdir
	except Exception as e: os=imp('os.path.isdir')

	global isWin
	if not isWin:
		if p.startswith('/'):
			if   os.path.isdir(p): return p
			elif os.path.isfile(p): return p

	if ab:
		if os.path.isfile(p) or os.path.isdir(p):
			try: p = os.path.abspath(p)
			except: pass

	if fix and not os.path.isfile(p) and not os.path.isdir(p) and not os.sep in p and p:
		p = os.getcwd() +os.sep+ p
		return p



	if slash is None:
		slash = os.sep
	if not p:
		return p.replace(os.sep+os.sep,os.sep)
	# print(p)
	p = p.replace( chr(92), slash )
	p = p.replace( chr(47), slash )
	while slash+slash in p:
		p = p.replace(slash+slash,slash)
	if ab:
		if os.path.isfile(p) or os.path.isdir(p):
			try:
				p = os.path.abspath(p)
			except Exception as e:
				pass
	if isWin or (not ln is None and ln):
		global truePath
		if truePath:
			try:
				os=imp('os.path._getfinalpathname')
				p = os.path._getfinalpathname(p).lstrip(r'\?')
			except: pass
	try:
		if p_bk[1] == ':' and not p[1] == ':': p = p_bk
		if type(p) == str and len(p)>1 and p[1] == ':':
			p = p[0].upper() + p[1:]
	except: pass
	if type(p) == str and ( pop or file ):

		if type(pop) == int:
			i=0
			while not i == pop:
				i+=1
				p = path( p, pop=True, slash=slash )
				# print(p)
			if file:
				p = path( p, file=True, slash=slash )
			return p.replace(os.sep+os.sep,os.sep)
		parts = p.split(slash)
		parts.reverse()
		f = parts.pop(0)
		parts.reverse()
		p = str(slash).join(parts)
		if file:
			p = f
	return p.replace(os.sep+os.sep,os.sep)

def file( p ):
	# os = imp('os')
	p = p.replace( chr(92), os.sep )
	p = p.replace( chr(47), os.sep )
	if not os.sep in p:
		return p
	parts = p.split(os.sep)
	parts.reverse()
	f = parts.pop(0)
	return f


def fromYML(text):
	if os.path.isfile(text):
		text=getText(text)
	elif not '\n' in text and text.count(os.sep):
		return {}
	try:
		import yaml # type: ignore
		return yaml.safe_load(text.replace('\t','    '))
	except Exception as e:
		table = {}
		lines = text.split('\n')
		for line in lines:
			if ':' in line:
				key, value = line.split(':', 1)
				table[key.strip()] = value.strip()
			return table
def toYML(dic,path=None):
	text =  imp('yaml').dump( dic, sort_keys=False )
	if path is None:
		return text
	else:
		mkdir(path,isFile=True)
		f = open(path,'w')
		f.write(str(text))
		f.close()

getYML=fromYML
saveYML=toYML

def yamlSimp(text):
	return fromYML(text)


def get_first_char(filename):
	with open(filename, 'r') as file: first_char = file.read(1)
	return first_char

def getText(filename):
	with open(filename, 'r') as file: content = file.read()
	return content
def saveText(text, path):
	mkdir(path,isFile=True)
	try:
		with open(path, 'w') as file:
			file.write(text)
	except IOError:
		print("An error occurred while saving the text to the file.")


get_file_content=saveText


def mkdir(path,isFile=False,pop=False):
	if pop: isFile=True
	if isFile:
		os=imp('os.path.dirname')
		path = os.path.dirname(path)
	os=imp('os.path.abspath')
	os=imp('os.path.exists')
	absolute_path = os.path.abspath(path)
	if not os.path.exists(absolute_path):
		os.makedirs(absolute_path)
	return absolute_path

def getTable( file, simple=False ):
	os = imp('os.path.isfile')
	if not get_first_char(file) == '{' and  not get_first_char(file) == '[':
		if simple:
			return yamlSimp(file)
		return yamlSimp(saveText(file))
	
	
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		print('no json')
	if os.path.isfile(file):
		with open(file,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
	else:
		json_data = data_default(file=file,default=[]).default()
	return json_data

def saveTable( data, file, sk=False ):
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		print('no json')
	dataDump = json.dumps(data, indent=4, sort_keys=sk)

	f = open(file,'w')
	f.write(str(dataDump))
	f.close()


pre_error = False
class Table_Aggregates:
	def __init__( self ):
		self.triggers = {}
	def trigger( self, label, script ):
		self.triggers[label] = script
	def run( self, label, data ):
		return self.triggers[label](data)
table_aggregates = Table_Aggregates()


# payloadCache = None
varFoldersCheck = False
myFileLocations_SKIP_VALIDATION = False




"""
__.autoCreationConfiguration['backup']
__.autoCreationConfiguration['logs']
__.autoCreationConfiguration['folders']
"""

# import importlib
try:
	startTime
except Exception as e:
	startTime = time.time()
	startTime2 = int(str(startTime).split('.')[0])

trigger_isPipe = False
isRequired_Pipe = False
isRequired_Pipe_or_File = False
isRequired_or_List = None
isRequired_index = {}
switchList = []
appRegPipe = None
cls_process_switches_help = False

storyboard = []
# __.sbd( fn=sys._getframe().f_code.co_name, d='' )
def sbd( location=1, line=0, fn='', d='' ):
	# add to auto documentation
	global storyboard
	global switchList
	function = fn
	activeSwitches = ''
	inactiveSwitches = ''
	documentation = n

	storyboard.append({ 'timestamp': time.time(), 'function': function, 'active': activeSwitches, 'inactive': inactiveSwitches })


def triggerTest( data ):
	return 'test'

def clearFocus( name, file ):
	global slash
	f = file.split(slash)
	if name == '__main__':
		x = '__' + f[len(f)-1].replace('.py','') + '__'
	else:
		x = f[len(f)-1].replace('.py','')
	appInfoAcquiredData['app'] = x
	return x

def thisApp( file ):
	global slash
	f = file.split(slash)
	x = f[len(f)-1].replace('.py','')
	return x


def wsl(fi):
	subject = fi
	git_path = subject
	while '\\' in git_path:
		git_path = git_path.replace( '\\', '/' )
	print(git_path)
	git_path = git_path.replace( ':', '' )
	git_path = '/' + git_path
	wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
	wsl5=wsl5.replace(' ','\\ ')
	return wsl5


# delimReg = '_'
delimReg = '_-_'

appReg = ''

registeredApps = []
registeredAppsAll = []

threadQueue = {}

def constructRegistration( file, dba ):
	global registeredAppsAll
	shouldAdd = True
	for ra in registeredAppsAll:
		if ra['dba'] == dba:
			shouldAdd = False
	if shouldAdd:
		registeredAppsAll.append({ 'file': file, 'dba': dba })

def constructApps():
	global registeredAppsAll
	for appreg in registeredAppsAll:
		print(appreg)


regApp = None
def appName( appReg, parentApp='', childApp='' ):
	global regApp
	global delimReg
	global isRequired_index
	if not parentApp == '':
		appReg = appReg + delimReg + parentApp
	if not childApp == '':
		appReg = parentApp + delimReg + appReg
	isRequired_index[appReg] = []
	appInfoAcquiredData['focus'] = appReg
	if regApp is None:
		regApp = appReg
	return appReg

def structure():
	result = []
	global registeredAppsAll
	for raa in registeredAppsAll:
		if type(raa) == dict:
			result.append(raa)
			# print(raa)
	return result

theDelim = '|||'
appInfoScan = False # appInfo.py



# import blank
# blank.focus(focus())
# _.load()
# blank.registerSwitches()
# _.switches.process()
# _.switches.fieldSet('Input','active',True)
# _.switches.fieldSet('Input','value','one')

# _.appInfo[blank.focus(focus())] = _.appInfo[blank.focus()]
# _.appData[blank.focus(focus())] = _.appData[blank.focus()]
# __.constructRegistration(_.appInfo[blank.focus(focus())]['file'],blank.focus(focus()))


class data_default:
	# __.data_default(file=theFile,default=[])
	def __init__( self, file, default ):
		self.dics = 'yml yaml i index indexes dex ls hash hashes tables logs lists indices meta setting settings dic s fig conf cnf'
		self.lists = 't tbl table cache log list lists l json config'
		while '  ' in self.dics:  self.dics  = self.dics.replace('  ',' ')
		while '  ' in self.lists: self.lists = self.lists.replace('  ',' ')
		self.file = file
		self.default_result = default
	def default( self ):

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.json' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.json' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.yml' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.yml' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.yaml' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.yaml' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x ):
				return []
		return self.default_result
# return __.data_default(file=theFile,default=[]).default()


class file_headers:
	# __.data_default(file=theFile,default=[])
	def __init__( self, path, default='' ):
		self.watermark = '''
## {R2D2919B742E} ##
###########################################################################
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
	- Scott Taylor Reph, RightThumb.com
###########################################################################
## {C3P0D40fAe8B} ##

'''.replace('\r','')
		self.path = path
		self.headers = {
							'functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'_functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'_fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'.folder.meta':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.h'},
							'.folder.meta.b':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.b'},
							'.txt': '__________________________________________________________________________________\n',
							'.sh': '#!/bin/bash\n',
							'.py': '#!/usr/bin/python3\n',
							'.bat': '@echo off\n',
							'.html': {'url':'https://apps.eyeformeta.com/templates/html/0.htm'},
							'.htm':  {'url':'https://apps.eyeformeta.com/templates/html/1.htm'},
							'.php':  {'url':'https://apps.eyeformeta.com/templates/html/0.php.txt'},
		}
		self.comment = {
							# '.js': '//',
							'.sh': '#',
							'.py': '#',
							'.bat': 'rem',
		}
		# self.nospace=['.sh']
		self.nospace=[]
		self.default_result = default
	def add_watermark(self,code):
		for ext in self.comment:
			if self.path.endswith(ext):
				for line in self.watermark.split('\n'):
					if len( line.replace(' ','').replace('\t','') ):
						code+=self.comment[ext]+' '+line+'\n'
					else:
						code+='\n'
		for ext in self.nospace:
			if self.path.endswith(ext):
				import _rightThumb._string as _str
				code = code.replace('\r','')
				code = _str.cleanBE(code,' ')
				code = _str.cleanBE(code,'\n')
				code = _str.replaceDuplicate(code,'\n')
				code = _str.cleanBE(code,'\n')
				code = _str.cleanBE(code,' ')
				code+='\n'

		return code.replace('\r','')


	def default( self ):
		for ext in self.headers:
			if self.path.endswith(ext):
				if type(self.headers[ext]) == dict:
					try:
						import requests
						page = requests.get(self.headers[ext]['url'])
						return page.content.decode("utf-8").replace('\r','')
					except Exception as e:
						return self.add_watermark(self.default_result)
						
				return self.add_watermark(self.headers[ext])
		return self.add_watermark(self.default_result)
# __.file_headers(path).default()


setting('myFileLocations-skip-validation',False)
setting('require-pipe',False)
setting('require-pipe||file',False)
setting('pre-error',False)
setting('switch-raw',[])
setting('require-list',[])
setting('receipt-log',True)
setting('receipt-file',True)
setting('fileBackup-secure_file',False)

#--> todo#> create app to scan to fix this situation below


# import os

def url( URL, data={}, d=None, raw=False, r=None,txt=None,text=None,t=None, dic=None, get=None ):
	headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
						"KHTML, like Gecko) Version/4.0 Safari/534.30"}
	if not txt is None: t=txt;
	if not text is None: t=text;
	import _rightThumb._string as _str

	if not r is None: raw=r;
	if not d is None: data=d;
	def _url_(data): return _str.do('.sh',data);
	# if not json is None and json:
	#     page=imp('requests.get').json(URL, headers=headers)
	#     return page
	if not get is None and get:

		page=imp('requests.get').get(URL, headers=headers)
		if raw: return page;
		if not t is None and t:
			result=page.text
		else:
			result=page.content
		for encodeing in 'UTF-8 ISO-8859-1 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
			try: return _url_(str(result,encodeing));
			except Exception as e: pass;
		return _url_(str(result))



	if not dic is None and dic:
		_dic={
			"href": "https://www.google.com/search?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
			"origin": "https://www.google.com",
			"domain": "google.com",
			"host": "www.google.com",
			"protocol": "https",
			"folder": "",
			"path": "google.com/search",
			"port": "443",
			"param": "?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
			"params": {},
			"username": "",
			"password": ""
		}

		return _dic



	page=imp('requests.post').post(URL, data = data)
	if raw: return page;
	if not t is None and t:
		result=page.text
	else:
		result=page.content
	for encodeing in 'ISO-8859-1 UTF-8 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
		try: return _url_(str(result,encodeing));
		except Exception as e: pass;
	return _url_(str(result))
page=url

print_=print
def getText2( theFile, raw=False, clean=False,  e=0, c=0 ):
	try: _str;
	except Exception as e:
		try: import _rightThumb._string as _str;
		except Exception as e: pass;
	os=imp('os.path.getmtime')
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	# HD.chmod(theFile)
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		if not e:
			return None
		print_('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print_( row )
			lines[i] = row
		return lines
	else:
		return lines
try:
	os = imp('os.system')
	os = imp('os.sep')
	os = imp('os.listdir')
	os = imp('os.getcwd')
	os = imp('os.path.abspath')
	os = imp('os.path.isfile')
	os = imp('os.path.isdir')
	os = imp('os.name')
	os = imp('os.stat')
	sys = imp('sys.exit')
except:
	import os
	import sys





import sys

class VariableManager:
	def __init__(self):
		self.values = {}
		self.triggers = {}
		self.triggersAll = {}
		self.aliases = {}
		self.globals = {}

	def setGlobal(self, name):
		if name in self.aliases:
			name = self.aliases[name]
		self.globals[name] = True

	def g(self, name):
		self.setGlobal(name)

	def append(self, name, value, p=None, c=None, h=None, pp=True):
		return self.set(name, value, append=True, p=p, c=c, h=h, pp=pp)

	def appendIf(self, name, value, p=None, c=None, h=None, pp=True):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			if self.triggers[name](value):
				return self.set(name, value, append=True, p=p, c=c, h=h, pp=pp)
			else:
				return False
		else:
			return None

	def ai(self, name, value, p=None, c=None, h=None, pp=True):
		return self.appendIf(name, value, p=p, c=c, h=h, pp=pp)

	def setIf(self, name, value, p=None, c=None, h=None, pp=True):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			if self.triggers[name](value):
				return self.set(name, value, p=p, c=c, h=h, pp=pp)
			else:
				return False
		else:
			return None

	def If(self, name, value, p=None, c=None, h=None, pp=True):
		return self.setIf(name, value, p=p, c=c, h=h, pp=pp)

	def runTrigger(self, name, value):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			return self.triggers[name](value)

	def Trigger(self, name, value): return self.runTrigger(name, value)
	def t(self, name, value): return self.runTrigger(name, value)
	def run(self, name, value): return self.runTrigger(name, value)
	def check(self, name, value): return self.runTrigger(name, value)

	def set(self, name, value, append=False, a=None, p=None, c=None, h=None, pp=True):
		if a is not None:
			append = a
		if name in self.aliases:
			name = self.aliases[name]
		if append:
			if name not in self.values:
				self.values[name] = []
			self.values[name].append(value)
			if name in self.globals:
				setattr(self, name, self.values[name])  # Replaces exec
		else:
			self.values[name] = value
			if name in self.globals:
				setattr(self, name, value)  # Replaces exec
		if name in self.triggersAll:
			self.triggersAll[name](self.values[name])
		if name in self.triggers:
			self.triggers[name](value)
		for alias, actual_name in self.aliases.items():
			if actual_name == name:
				if name in self.globals:
					setattr(self, alias, self.values[name])  # Replaces exec
		if p:
			if not pp:
				return pr(value, c=c, h=h, p=pp)  # Using placeholder pr function
			else:
				pr(value, c=c, h=h)
		return self.values[name]

	def alias(self, name, *aliases):
		for a in aliases:
			if a in self.values:
				print(self.values)
				pr('Error: Alias already exists in values:', name, c='red')
				KILL()
			self.aliases[a] = name

	def value(self, name):
		if name in self.aliases:
			name = self.aliases[name]
		return self.values.get(name, None)

	def get(self, name): return self.value(name)
	def val(self, name): return self.value(name)

	def trigger(self, name, script, all=False):
		if name in self.aliases:
			name = self.aliases[name]
		if all:
			self.triggersAll[name] = script
		else:
			self.triggers[name] = script

# Placeholder `pr()` function (replace with your actual implementation)
# def pr(value, c=None, h=None, p=True):
#     print(f"{c.upper() if c else ''} {value}")


# appInfoAcquiredData  app focus data

def vmTrigger_payloadCache(value):
	global appInfoAcquiredData
	appInfoAcquiredData['data'] = value

VM = VariableManager
Store = VariableManager
Vars = VariableManager
store = VariableManager()
store.set('payloadCache', None)
store.alias('payloadCache', 'data','payload','records')
store.trigger('payloadCache', vmTrigger_payloadCache, all=True)


def KILL():
	isExit(fromKill=True)
	os = imp('os._exit')
	os._exit(1)

# os=imp('os')