import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Input', '-i' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'tmi.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start















import os
import re
import requests

class TMI:
	def __init__(self):
		self.config = {
			'[&]': '||',
			'{&}': '|',
			'&': '*',
			'*': '!',
			',': '~',
			'blank': '-',
			'#': '@',
			'url': 'https://a.sds.sh/assets/py/tmi/',
			'js-fw': 'https://a.sds.sh/assets/py/tmi/',
			'fw.js': 'https://a.sds.sh/assets/py/tmi/framework.js',
		}

	def tmi(self, bundle1=None, bundle2=None):
		if bundle1 is None:
			bundle1 = {}
		if bundle2 is None:
			bundle2 = {}
			
		if not bundle1:
			bundle1 = dict(os.environ)
			
		if isinstance(bundle2, str):
			bundle = bundle1
			bundle['data'] = bundle2
		else:
			bundle = {**bundle1, **bundle2}

		assets = bundle.get('assets') or bundle.get('folder') or bundle.get('fo') or ''
		if not assets:
			if os.path.exists('./assets/'):
				assets = 'assets'
		if not assets:
			if os.path.exists('./__files__/'):
				assets = '__files__'
		if not assets:
			if os.path.exists('./_files_/'):
				assets = '_files_'
				
		self.config['js'] = f"{assets}/js{self.config['js-fw']}"

		data = bundle.get('file') or bundle.get('data') or ''
		header = bundle.get('h') or bundle.get('ext') or bundle.get('head') or bundle.get('header') or bundle.get('fiH') or False
		echo = bundle.get('e') or bundle.get('echo') or bundle.get('print') or False
		
		if not data:
			if 'fi' in bundle:
				bundle['f'] = bundle['fi']
			if 'f' in bundle:
				fi = bundle['f']
				file_parts = fi.split('.')
				if len(file_parts) > 1:
					ext = file_parts[-1].lower()
				else:
					path = f"./{assets}/{fi}".strip()
					if path.endswith('/'):
						skip = True
						path = self.is_folder(path)
				if not skip:
					path_a = f"./{assets}/{ext}/{bundle['f']}"
					path_b = f"./{assets}/{bundle['f']}"
					if os.path.exists(path_a):
						path = path_a
					elif os.path.exists(path_b):
						path = path_b
				while '//' in path:
					header = True
					path = path.replace('//', '/')
				if os.path.exists(path):
					if path.endswith('.php'):
						with open(path) as f:
							exec(f.read())
						exit()
					with open(path) as f:
						data = f.read()
		if 'dup' in bundle:
			data = self._dup2(bundle, data)
		if 'r' in bundle:
			data = self._replace(bundle, data)
		if 'isid' in bundle:
			data = self._id_class(bundle, data)
		if 'del' in bundle:
			data = self._del(bundle, data)
		if 'path' in locals():
			if path.endswith('.js') and self.config['js-fw'] in path:
				data = self.process_includes(data)
		if 'line' in bundle or 'l' in bundle:
			data = self._line(bundle, data)
		if 'load' in bundle:
			data = self._load(bundle, data)
		if 'exec' in bundle or 'x' in bundle:
			exec_ = bundle.get('exec') or bundle.get('x')
			if exec_:
				commands = self.extract_commands(exec_)
				data = ''
				for command in commands:
					cdata = ''
					actions = self.virtual_get_command(command)
					for key, value in actions.items():
						if isinstance(value, list):
							for sub_key, sub_value in value.items():
								cdata = self.process_commands(value, sub_key, cdata)
						else:
							cdata = self.process_commands(actions, key, cdata)
					data += cdata
		# if header:
		# 	with open(os.path.join(os.environ['DOCUMENT_ROOT'], '.re/fi.php')) as f:
		# 		exec(f.read())
		# 	if 'ext' in bundle:
		# 		fiH(f"file.{bundle['ext']}", 0)
		# 	else:
		# 		if 'path' in locals():
		# 			fiH(path, 0)
		if echo:
			print(data)
		return data


	def _replace(self, arr, data):
		replace = arr['r']
		replace = replace.replace('\\n', "\n").replace('%2C', ',')
		replace_pairs = replace.split(',')

		if len(replace_pairs) % 2 != 0:
			raise ValueError("Invalid replace pairs")

		for i in range(0, len(replace_pairs), 2):
			search = replace_pairs[i]
			replace = replace_pairs[i + 1]
			search = search.replace(self.config[','], ',')
			replace = replace.replace(self.config[','], ',')
			search = search.replace(self.config['#'], '#')
			replace = replace.replace(self.config['#'], '#')
			search = search.replace(self.config['*'], '*')
			replace = replace.replace(self.config['*'], '*')

			if search == '1':
				data = f"{replace}\n{data}"
				data = self.process_includes(data)
				continue

			if search == '2':
				data = f"{data}\n{replace}"
				data = self.process_includes(data)
				continue

			if replace.strip() == self.config['blank']:
				replace = ''

			data = data.replace(search, replace)

		return data

	def process_includes(self, data):
		lines = data.split('\n')
		processed_content = ''

		for line in lines:
			match = re.match(r'^include:\s*(.*)$', line, re.IGNORECASE)
			if match:
				relative_path = match.group(1).strip().replace('\\', '/')
				processed_content = ''
				# processed_content += f"\n\n// (include)=> {relative_path}\n\n"
				url = self.config['url']+relative_path
				url = url.replace('\\', '/')
				url = url.replace('//', '/')
				url = url.replace('https:/', 'https://')
				# print(url); exit;
				response = requests.get(url)

				if response.status_code == 200:
					file_contents = response.text
					processed_content += self.process_includes(file_contents)
				else:
					print(f"File not found: {url}")
			else:
				processed_content += line + '\n'

		return processed_content

	def extract_commands(self, string):
		return re.findall(r'\[(.*?)\]', string)

	def virtual_get_command(self, input_):
		parts = input_.split(self.config['[&]'])
		result_array = {}
		for part in parts:
			key, value = part.split('=', 2)
			if value.startswith('{'):
				value = self.build_sub_commands(value)
			result_array[key] = value
		return result_array

	def build_commands(self, input_string):
		commands = self.extract_commands(input_string)
		for command in commands:
			command_array = self.virtual_get_command(command)
			return command_array

	def extract_sub_commands(self, string):
		return re.findall(r'\{(.*?)\}', string)

	def virtual_get_sub_command(self, input_):
		parts = input_.split(self.config['{&}'])
		result_array = {}
		for part in parts:
			key, value = part.split('=', 2)
			result_array[key] = value
		return result_array

	def build_sub_commands(self, input_string):
		sub_commands = self.extract_sub_commands(input_string)
		for sub_command in sub_commands:
			sub_command_array = self.virtual_get_sub_command(sub_command)
			return sub_command_array



	def remove_lines_containing_strings(self, text, string_list):
		lines = text.split('\n')
		filtered_lines = [line for line in lines if not any(s in line for s in string_list)]
		return '\n'.join(filtered_lines)

	def is_folder(self, path):
		if 'is' in os.environ:
			if 'j' in os.environ['is']:
				path += 'index.js'
			if 'p' in os.environ['is']:
				path += 'index.php'
			if 'c' in os.environ['is']:
				path += 'index.css'
			if 'h' in os.environ['is']:
				path += 'index.htm'
			return path
		else:
			for file in ['index.js', 'index.htm', 'index.php', 'index.html', 'index.css', 'script.js', 'module.js']:
				if os.path.exists(path + file):
					path += file
					return path
			exit('No valid path found.')

	def _dup(self, arr, data):
		duplication_instructions = arr['dup'].split(',')
		lines = data.split('\n')
		result_lines = []
		for i in range(0, len(duplication_instructions), 2):
			num_duplicates = int(duplication_instructions[i])
			pattern = duplication_instructions[i + 1]
			for index, line in enumerate(lines):
				if pattern in line:
					for j in range(1, num_duplicates + 1):
						modified_line = re.sub(r'____[a-z]', lambda m: m.group(0) + str(j), line)
						result_lines.append(modified_line)
					continue
				result_lines.append(line)
			lines = result_lines
			result_lines = []
		return '\n'.join(lines)

	def maybe_lower(self, string, ci=True):
		if ci:
			string = string.lower()
		return string

	def _dup2(self, arr, data):
		duplication_instructions = arr['dup'].split(',')
		case = False
		case_insensitive = 'dup-ci' in arr or 'ci' in arr
		lines = data.split('\n')
		result_lines = []
		for line in lines:
			found = False
			for value in duplication_instructions:
				if self.maybe_lower(line, case_insensitive).find(self.maybe_lower(value, case_insensitive)) != -1:
					found = True
			if found:
				result_lines.append(line)
			result_lines.append(line)
		return '\n'.join(result_lines)



























def action():
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);