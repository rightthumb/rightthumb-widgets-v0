import re
class index:
	'''
	myVar = intelligent.fnindex(code)
	myVar.index(code,settings)
	myVar.fn()
	myVar.line(i)
	myVar.inDex(index, pos, i=False)
		index is {} or 'oc' (myVar.db name)
		pos is char pos
		if i is False    <-------------------------------- bool
			returns bool unless
		if i is True     <-------------------------------- pos
			returns pos of open
	myVar.nextDex(index, pos)
		index is {} or 'oc' (myVar.db name)
	myVar.prevDex(pos, index=None)
		index defaults to .db[oc]
		index is {} or 'quotes' (myVar.db name)
	myVar.lineNumber(i)
	myVar.lineStart(i)
	'''

	def __init__(self, code='', language=None, settings={}):
		''''
			settings = {
				'brackets': {
					'<':'>', # not included in brackets dict
				},
				'comments': {}, # dict
				'quotes': [], # list
			}
		'''
		self.db = {
			'comments': {},
			'quotes': {},
			'oc': {},
			'lines': {},
			'text': {},
			'ocqt': {},
			'qt': {},
		}
		self.settings = settings
		if type(code) == list: code = '\n'.join(code)
		self.code = code
		self.language = language
		if self.code == '' and self.language is None: self.language = 'js'
		if self.language is None:
			self.determinLanguage()
		self.language = self.language.lower()
		languages = {
			'js': 'javascript',
			'javascript': 'javascript',
			'py': 'python',
			'python': 'python',
		}
		if self.language in languages: self.language = languages[self.language]
		self.db = self.index(self.code,self.settings)
	def k(self): return 'Keys:'+'\t'+'\n\t'.join(list(self.db.keys()))

	def snip(self, start, end, code=None):
		if code is None: code = self.code
		return code[start:end]
	def ns(self): return self.fn()
	def namespace(self): return self.fn()
	def fnClass(self): return self.fn()

	def fn(self):
		if self.language == 'python':
			index = self.pyFnClass()
		if self.language == 'javascript':
			index = self.jsFnNS()
		return index

	def inDex(self, index, ii, i=False):
		if type(index) == str: index = self.db[index]
		for start, end in index.items():
			if start <= ii <= end:
				if i: return start
				return True
		return False

	def endOfLine(self, i, text=None):
		if text is None: text = self.code
		while i < len(text) and text[i] != '\n':
			i += 1
		return i

	def startOfLine(self, i, text=None):
		if text is None: text = self.code
		while i > 0 and text[i] != '\n':
			i -= 1
		return i

	def nextDex(self, index, i):
		if type(index) == str: index = self.db[index]
		keys = sorted(index.keys(), reverse=False)
		for key in keys:
			if i < key: continue
			return key
		return None

	def prevDexInRange(self, i, o, index=None):
		if index is None: index = self.db['oc']
		if isinstance(index, str): index = self.db[index]
		keys = sorted(index.keys(), reverse=True)
		for key in keys:
			if i > key:
				continue
			if key <= o <= i:
				return key
		return None

	def prevDex(self, i, index=None):
		if index is None: index = self.db['oc']
		if type(index) == str: index = self.db[index]
		keys = list(index.keys())
		keys = sorted(index.keys(), reverse=True)
		for key in keys:
			if i > key: continue
			return key
		return None

	def justDex(self,only,index=None, code=None):
		if type(only) == list: only = ''.join(only)
		if index is None: index = self.db['oc']
		if code is None: code = self.code
		new = {}
		for i in index:
			if code[i] in only:
				new[i] = index[i]
		return new

	def prevChar(self, i, search, code=None):
		if code is None: code = self.code
		if 'a' in search and 'n' in search: search = search.replace('a','').replace('n','')+'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		elif 'a' in search: search = search.replace('a','')+'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		elif 'n' in search: search = search.replace('n','')+'0123456789'
		while not i == 0:
			i-=1
			if code[i] in search:
				return i
			if code[i] in '\n':
				return False
		return None

	def nextChar(self, i, search, code=None):
		if code is None:
			code = self.code
		if 'a' in search and 'n' in search:
			search = search.replace('a', '').replace('n', '') + '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		elif 'a' in search:
			search = search.replace('a', '') + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		elif 'n' in search:
			search = search.replace('n', '') + '0123456789'
		while i < len(code) - 1:
			i += 1
			if code[i] in search:
				return i
			if code[i] == '\n':
				return False
		return None

	def lineNumber(self, i):
		while True:
			i -= 1
			if i < 0:
				return 0
			if i in self.db['lines']:
				return list(self.db['lines'].keys()).index(i)

	def lineStart(self, i):
		while True:
			i -= 1
			if i < 0:
				return 0
			if i in self.db['lines']:
				return i
				break

	def line(self, i):
		while True:
			i -= 1
			if i < 0:
				return 0
			if i in self.db['lines']:
				line = self.code[i:self.db['lines'][i]]
				return line.rstrip()
				break

	def inRange(self, i, o, c):
		if i >= o and i <= c:
			return True
		return False

	def jsFnNS(self):
		'''
			self.db['fn'] = index
			self.db['ns'] = ns
			self.db['parents'] = nsParents
			self.db['nested'] = stack
		'''
		js_code = self.code
		function_patterns = [
			re.compile(r'(?:let|const|var)?\s*\w+\s*=\s*function\s*\([^)]*\)\s*{'),
			re.compile(r'(?:let|const|var)?\s*\w+\s*=\s*\([^)]*\)\s*=>\s*{'),
			re.compile(r'function\s+\w+\s*\([^)]*\)\s*{'),
			re.compile(r'\w+\s*:\s*function\s*\([^)]*\)\s*{'),
			re.compile(r'\w+\s*:\s*\([^)]*\)\s*=>\s*{')
		]
		index = {}
		ns = []
		nsParents = {}
		stack = []
		for match in re.finditer(r'{|}', js_code):
			char_pos = match.start()
			char = match.group()
			if char == '{':
				if stack:
					nsParents[char_pos] = stack[-1]
				stack.append(char_pos)
			elif char == '}' and stack:
				open_pos = stack.pop()
				index[open_pos] = char_pos+1
			if char == '{' and any(pattern.search(js_code[:char_pos]) for pattern in function_patterns):
				ns.append(char_pos)
		namespaces = {}
		for open_pos in ns:
			i = open_pos - 1
			while i >= 0:
				if js_code[i] in "'\"":  # Skip quotes
					quote_char = js_code[i]
					i -= 1
					while i >= 0 and js_code[i] != quote_char:
						i -= 1
					i -= 1
					continue
				if js_code[i] == ':':
					i -= 1
					while i >= 0 and js_code[i].isspace():
						i -= 1
					start = i
					while start >= 0 and (js_code[start].isalnum() or js_code[start] == '_'):
						start -= 1
					namespaces[open_pos] = stack[-1] if stack else None
					break
				elif js_code[i] == '=':
					i -= 1
					while i >= 0 and js_code[i].isspace():
						i -= 1
					start = i
					while start >= 0 and (js_code[start].isalnum() or js_code[start] == '_'):
						start -= 1
					namespaces[open_pos] = stack[-1] if stack else None
					break
				i -= 1
		braces = self.justDex('{')

		def endOfLine(i, text):
			while i < len(text) and text[i] != '\n':
				i += 1
			return i

		def startOfLine(i, text):
			while i > 0 and text[i] != '\n':
				i -= 1
			return i
		varBracesEquals = {}
		for o in braces:
			if not self.prevChar(o,'='): continue
			varBracesEquals[o] = braces[o]
		nsFn = {}
		for o in nsParents:
			if not self.prevChar(o,':'):
				continue
			line = self.line(o)
			if 'function' in line or '=>' in line:
				nsFn[o] = nsParents[o]
		allNS = []
		for i in nsFn:
			active = i
			rents = []
			rents.append(active)
			hasEqual = False
			while True:
				add = None
				if active in nsParents:
					add = nsParents[active]
					active = nsParents[active]
				else:
					if hasEqual: break
					top = self.prevDexInRange(active,i, index=None)
					if not top:
						intelligent.fnpr(line=1,c='red')
						break
					try:
						if not self.inRange(i,top,self.db['oc'][top]): break
					except: break
					rents.append(top)
					break
				pass
				if '=' in line:
					if not hasEqual:
						hasEqual = True
				rents.append(add)
			parents = []
			eq = 0
			for i in rents:
				line = self.line(i)
				if '=' in line:
					break
			allNS.append(rents)
		cleanNS = {}
		for paths in allNS:
			myNS = []
			track = []
			hitEnd = False
			for i in paths:
				try:
					if not self.inRange(paths[0],i,self.db['oc'][i]): continue
				except: continue
				line = self.code[i:startOfLine(i,self.code)]
				track.append([i,line])
				if '=' in line:
					hitEnd = True
				hasEqual = False
				ii = i
				prev = self.prevChar(i, ':')
				if not prev: prev = self.prevChar(i, '=')
				prev = self.prevChar(prev, ''' ` ' " a n _  '''.replace(' ',''))
				q = ''' ` ' "  '''.replace(' ','')
				if not prev: pass
				else:
					o = self.inDex('qt', prev, i=1)
					if not o:
						o = self.inDex('qt', prev-1, i=1)
					try:
						c = self.db['qt'][o]
					except:
						print(o,prev,self.code[prev],self.line(prev))
						o = self.inDex('text', prev, i=1)
						print(o,self.code[o])
					if self.code[prev] in q:
						o +=1
						c -=1
					snip = self.snip(o,c)
					if snip == 'function':
						o-=1
						prev = self.prevChar(o, ''' ` ' " a n _  '''.replace(' ',''))
						if not prev: intelligent.fnpr(line=1,c='red')
						if not prev: pass
						else:
							o = self.inDex('qt', prev, i=1)
							c = self.db['qt'][o]
							if self.code[prev] in q:
								o +=1
								c -=1
							snip = self.snip(o,c)
					if hitEnd: break
					myNS.append( snip )
			myNS.reverse()
			cleanNS['.'.join(myNS)] = paths[0]
		self.db['fn'] = index
		self.db['ns'] = cleanNS
		return {
			'fn': index,
			'ns': ns,
			'parents': nsParents,
		}

	def pyFnClass(self):
		lines = self.code
		if type(lines) == str:
			lines = lines.split('\n')

		def get_leading_whitespace(line):
			return len(line) - len(line.lstrip())
		function_stack = []  # Stack to manage nested functions/classes
		function_ranges = {}  # Stores the open-close line mapping
		last_line_of_text = -1
		for i, line in enumerate(lines):
			stripped_line = line.strip()
			if not stripped_line:
				continue
			last_line_of_text = i
			if stripped_line.startswith("def ") or stripped_line.startswith("class "):
				indentation_level = get_leading_whitespace(line)
				function_stack.append((i, indentation_level))
			while function_stack:
				open_pos, open_indent = function_stack[-1]
				current_indent = get_leading_whitespace(line)
				if current_indent <= open_indent and i != open_pos:
					function_stack.pop()
					function_ranges[open_pos] = last_line_of_text
				else:
					break
		while function_stack:
			open_pos, _ = function_stack.pop()
			function_ranges[open_pos] = last_line_of_text
		self.db['fn'] = function_ranges
		return function_ranges

	def determinLanguage(self):
		slash = 0
		pound = 0
		if '\ndef ' in self.code.replace(' ','').replace('\t',''):
			self.language = 'python'
			return 'python'
		if '<?php' in self.code.lower() or self.code.strip().startswith('<?') or '\n<?' in self.code.replace(' ','').replace('\t',''):
			self.language = 'php'
			return 'php'
		for line in self.code.split('\n'):
			line = line.strip()
			if line.startswith('#'):
				pound += 1
			if line.startswith('//'):
				slash += 1
		if pound > slash:
			self.language = 'python'
		else:
			self.language = 'javascript'

	def get_character_indexes(self,code=None):
		if code is None:
			code = self.code
		characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789intelligent.fn'
		char_index = {char: idx for idx, char in enumerate(characters)}
		open_char_ids = []
		close_char_ids = []
		dex = {}
		for idx, char in enumerate(code):
			if char in char_index:
				if idx not in self.db['comments']:
					if idx % 2 == 0:
						open_char_ids.append(idx)
					else:
						close_char_ids.append(idx)
		for open_id, close_id in zip(open_char_ids, close_char_ids):
			dex[open_id] = close_id
		return dex

	def get_line_positions(self,code):
		data = code
		line_positions = {}
		start_pos = 0
		for line in data.split('\n'):
			end_pos = start_pos + len(line) - 1
			line_positions[start_pos] = end_pos
			start_pos += len(line)
		return line_positions

	def find_text_indexes(self,text):
		valid_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZintelligent.fn")
		result = {}
		start = None
		for i, char in enumerate(text):
			if char in valid_chars:
				if start is None:
					start = i
			else:
				if start is not None:
					result[start] = i
					start = None
		if start is not None:
			result[start] = len(text)
		return result

	def index(self, code, settings):
		text = code
		language = self.language

		def testString(i, string, text):
			try:
				text[i]
			except:
				return None
			if i + len(string) > len(text):
				return False
			return text[i:i+len(string)] == string

		def endOfLine(i, text):
			while i < len(text) and text[i] != '\n':
				i += 1
			return i

		def startOfLine(i, text):
			while i > 0 and text[i] != '\n':
				i -= 1
			return i
		quotes = ['"', "'", '`']
		comments = {}
		if language == 'javascript' or language == 'php':
			comments['/*'] = '*/'
			comments['//'] = '\n'
		elif language == 'python':
			comments['#'] = '\n'
			quotes += ['"""', "'''"]
		brackets = {'(': ')', '{': '}', '[': ']'}
		if 'brackets' in settings: brackets.update(settings['brackets'])
		if 'comments' in settings: comments.update(settings['comments'])
		if 'quotes' in settings: quotes += settings['quotes']
		index = {
			'comments': {},
			'quotes': {},
			'oc': {},
			'lines': {},
			'text': {},
			'words': {},
		}
		stack = []
		line_start = 0
		line_number = 1
		i = 0
		inQuoteOrComment = False
		lastStart = -1
		currentType = None
		inText = False
		lastTextStart = -1
		watch = False
		lastBracketStart = None
		bStack = {}
		for b in brackets:
			bStack[b] = []
		bClose = {}
		for b in brackets:
			bClose[brackets[b]] = b
		carriages = []
		lColons = {}
		lBraces = {}
		while i < len(text) - 1:
			if text[i] == '\n':
				carriages.append(i)
			if not inQuoteOrComment and text[i] == ':':
				lColons[startOfLine(i, text)] = i
			if not inQuoteOrComment and self.language == 'javascript':
				if text[i] == '=' or text[i] == ':':
					try:
						iT = i+1
						while text[iT].isspace():iT += 1
						if not text[iT] == '=':
							if text[iT] == '/':
								b = startOfLine(i, text)
								e =endOfLine(i, text)
								iT +=1
								while not text[iT] == '\n' or text[iT] == '\r' or text[iT] == ';':
									iT += 1
								i = iT
					except Exception as e:
						intelligent.fnpr(e,c='red')
			if i == 6960: watch = True
			if inQuoteOrComment:
				if currentType in comments:
					end = testString(i, comments[currentType], text)
					if end:
						index['comments'][lastStart] = i + len(comments[currentType])
						i += len(comments[currentType])
						inQuoteOrComment = False
						currentType = None
				elif currentType in quotes:
					end = testString(i, currentType, text)
					if end:
						index['quotes'][lastStart] = i + len(currentType)
						ii=i
						i += len(currentType)
						inQuoteOrComment = False
						currentType = None
			else:
				if text[i].isalnum() or text[i] == '_':
					if not inText:
						lastTextStart = i
						inText = True
				else:
					if inText:
						index['words'][lastTextStart] = i
						inText = False
				for c in comments:
					if testString(i, c, text):
						if comments[c] == '\n':
							eol = endOfLine(i, text)
							index['comments'][lastStart] = eol
							line = text[lastStart:eol]
							i = eol
							inQuoteOrComment = False
						else:
							lastStart = i
							currentType = c
							inQuoteOrComment = True
						break
				for q in quotes:
					if testString(i, q, text):
						test = testString(i+1, q, text)
						if not test is None and test:
							inQuoteOrComment = False
							index['quotes'][i] = i+1
							i += 1
						else:
							lastStart = i
							currentType = q
							inQuoteOrComment = True
				if text[i] in brackets:
					if text[i] == '{':
						lBraces[startOfLine(i, text)] = i
					lastBracketStart = i
					stack.append((text[i], i))
					bClose
					bStack[text[i]].append(i)
				elif text[i] in bClose:
					index['oc'][bStack[bClose[text[i]]].pop()] = i+1
			i += 1
		if inText: index['words'][lastTextStart] = len(text)
		alt = None
		nStack = {}
		for b in bStack:
			nStack[b] = []
			if len(bStack[b]):
				if alt is None: alt = intelligent.fncode2(text)
				for i in bStack[b]:
					if i in alt:
						index['oc'][i] = alt[i]
					else:
						nStack[b].append(i)
		bStack = nStack
		self.err = bStack
		index['qc'] = {}
		index['qc'].update(index['comments'])
		index['qc'].update(index['quotes'])
		index['lines'] = {}
		last = 0
		for i in carriages:
			index['lines'][last] = i
			last = i
		index['lines'][carriages[-1]+1] = len(code)-1
		index['text'] = self.find_text_indexes(code)
		index['ocqt'] = {}
		index['ocqt'].update(index['oc'])
		index['ocqt'].update(index['quotes'])
		index['ocqt'].update(index['quotes'])
		index['ocqt'].update(index['text'])
		index['all'] = index['ocqt']
		index['qt'] = {}
		index['qt'].update(index['quotes'])
		index['qt'].update(index['text'])
		return index