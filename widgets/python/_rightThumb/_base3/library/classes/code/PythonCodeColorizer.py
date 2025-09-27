import _rightThumb._base3 as _



import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', 'library', 'code', 'functions')))
from pyClassesFunctions import pyClassesFunctions

import re

class PythonCodeColorizer:
	def __init__(self):
		# ANSI color codes
		self.colors = {
			'keyword': _.Color.blue,
			'name': _.Color.green,
			'string': _.Background.light_blue,
			'reset': _.Color.end
		}

	def colorize(self, code):
		testing = []
		if 'type' in testing: print(1,type(code),len(str(code)))
		dic = pyClassesFunctions(code)
		codeNew = ''
		for c in code:
			if c in '}{[]()':
				codeNew += f'{_.Color.green}{c}{_.Color.end}'
			else:
				codeNew += c
		code = codeNew
		if 'type' in testing: print(2,type(code),len(str(code)))

		for o in dic['ranges']['functions']:
			c = dic['ranges']['functions'][o]
			txt = code[o:c]
			code = code[:o] + f'{_.Color.cyan}{txt}{_.Color.end}' + code[c:]

		if 'type' in testing: print(3,type(code),len(str(code)))
		for o in dic['ranges']['classes']:
			c = dic['ranges']['classes'][o]
			txt = code[o:c]
			code = code[:o] + f'{_.Color.yellow}{txt}{_.Color.end}' + code[c:]


		if 'type' in testing: print(4,type(code),len(str(code)))
		def custom(code, string, color):
			dic = get_string_ranges(code, string)
			for o in dic:
				c = dic[o]
				txt = code[o:c]
				color = eval(f'_.Color.{color}')
				code = code[:o] + f'{color}{txt}{_.Color.end}' + code[c:]
				return code
			return code

		
		code = custom(code, 'from ', 'cyan')
		code = custom(code, 'import ', 'cyan')
		code = custom(code, 'if ', 'purple')
		code = custom(code, 'not ', 'red')
		code = custom(code, 'as ', 'green')
		code = custom(code, '= ', 'green')
		if 'type' in testing: print(5,type(code),len(str(code)))
		
		
		# return code
		# Patterns for functions, classes, and strings
		keyword_pattern = r'\b(def|class|return)\b'
		name_pattern = r'\b(?:def|class)\s+(\w+)'
		string_pattern = r'(\".*?\"|\'.*?\')'

		# Apply colors using regex substitutions
		code = re.sub(keyword_pattern, self.colors['keyword'] + r'\1' + self.colors['reset'], code)
		code = re.sub(name_pattern, r'\g<0>' + self.colors['name'] + r'\1' + self.colors['reset'], code)
		code = re.sub(string_pattern, self.colors['string'] + r'\1' + self.colors['reset'], code)
		if 'type' in testing: print(6,type(code),len(str(code)))
		return code
		

def get_string_ranges(text, substring):
	"""
	Finds all ranges (start and end positions) of instances of a substring within a given text.

	Args:
		text (str): The text to search within.
		substring (str): The substring to search for.

	Returns:
		list of tuples: A list of (start, end) tuples indicating the ranges of each instance.
	"""
	if not substring:
		return []

	ranges = {}
	start = 0
	# print(77,type(text),len(str(text)))
	while True:
		# print(88,type(text),len(str(text)))
		start = text.find(substring, start)
		if start == -1:
			break
		end = start + len(substring)
		ranges[start] = end
		start += 1
	return ranges





# Sample usage
if __name__ == "__main__":
	sample_code = '''
class SampleClass:
	def hello(self):
		print("Hello, world!")

def my_function(arg1, arg2):
	return arg1 + arg2
	'''

	colorizer = PythonCodeColorizer()
	print(colorizer.colorize(sample_code))





# class PythonCodeColorizer:
#     def __init__(self):
#         # ANSI color codes
#         self.colors = {
#             'keyword': '\033[94m',  # Blue
#             'function_name': '\033[96m',  # Cyan
#             'class_name': '\033[93m',  # Yellow
#             'string': '\033[91m',  # Red
#             'reset': '\033[0m'  # Reset
#         }

#     def colorize(self, code):
#         # Patterns for keywords, function names, class names, and strings
#         keyword_pattern = r'\b(def|class|return)\b'
#         function_name_pattern = r'\bdef\s+(\w+)'
#         class_name_pattern = r'\bclass\s+(\w+)'
#         string_pattern = r'(\".*?\"|\'.*?\')'

#         # Apply colors using regex substitutions
#         code = re.sub(keyword_pattern, self.colors['keyword'] + r'\1' + self.colors['reset'], code)
#         code = re.sub(function_name_pattern, r'def ' + self.colors['function_name'] + r'\1' + self.colors['reset'], code)
#         code = re.sub(class_name_pattern, r'class ' + self.colors['class_name'] + r'\1' + self.colors['reset'], code)
#         code = re.sub(string_pattern, self.colors['string'] + r'\1' + self.colors['reset'], code)

#         return code

# # Sample usage
# if __name__ == "__main__":
#     sample_code = '''
# class SampleClass:
#     def hello(self):
#         print("Hello, world!")

# def my_function(arg1, arg2):
#     return arg1 + arg2
#     '''

#     colorizer = PythonCodeColorizer()
#     print(colorizer.colorize(sample_code))
