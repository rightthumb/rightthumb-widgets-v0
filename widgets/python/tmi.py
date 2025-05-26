import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
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

import re
import os

class TMI:
	def __init__(self):
		self.config = {
			'[&]': '||',
			'{&}': '|',
			'&': '*',
			'*': '!',
			',': '~',
			'=': '--',
			'blank': '-',
			'#': '@',
			'js-fw': '/sds/'
		}
		self.bundle_backup = {}
		self.just_return = False
		self.bundle = {}
		self.files = []
		self.settings = {}
		self.no_comments = False
		self.bundle_remove = {
			'include': ['i', 'inc', 'include']
		}
		self.abbreviations = {
			'a': 'after',
			'r': 'replace',
			'l': 'line',
			'x': 'exec',
			'i': 'include',
			'd': 'data',
			'u': 'url',
			'e': 'echo',
			'h': 'header',
			'a': 'assets',
			'fo': 'folder',
			'up': 'url-post',
			'uh': 'url-header'
		}
		self.valid_keys = 'data,justReturn,assets,noComments,file,header,f,r,include,a,dup,isid,del,line,load,wrap,dup-ci,id,class,after,url,url-post,url-header,exec'.split(',')
		self.assets_folders = [
			"./a/",
			"./assets/",
			"./__files__/",
			"./_files_/",
			"./_docs_/",
			"./docs/",
			"./f/",
		]

	def bundle_clean(self, bundle, subject='include'):
		if subject not in self.bundle_remove:
			return bundle
		for item in self.bundle_remove[subject]:
			if item in bundle:
				del bundle[item]
		return bundle

	def bundle_cleaner(self, bundle):
		package = {key: value for key, value in bundle.items() if key in self.valid_keys}
		return package

	def bundle_abbreviations(self, bundle):
		newBundle = {}
		for k in bundle:
			if k in self.abbreviations:
				newBundle[self.abbreviations[k]] = bundle[k]
			else:
				newBundle[k] = bundle[k]
		# for alias, key in self.abbreviations.items():
		# 	if alias in bundle:
		# 		bundle[key] = bundle.pop(alias)
		return newBundle

	def tmi(self, bundle1=None, bundle2=None):
		if bundle1 is None:
			bundle1 = {}
		if bundle2 is None:
			bundle2 = {}
		if not bundle1:
			bundle1 = self._get_request()
		if isinstance(bundle2, str):
			bundle = bundle1
			bundle['data'] = bundle2
		else:
			bundle = {**bundle1, **bundle2}

		if 'justReturn' in bundle:
			self.just_return = True
			del bundle['justReturn']

		self.bundle_backup = bundle
		assets = bundle.get('assets') or bundle.get('folder') or bundle.get('fo') or ''
		if not assets:
			assets = self.find_assets_folder()

		self.no_comments = bundle.get('noComments', False)

		bundle = self.bundle_abbreviations(bundle)

		self.config['js'] = f"{assets}/js" + self.config['js-fw']
		data = bundle.get('file') or bundle.get('data', '')
		header = bundle.get('header') or bundle.get('ext') or bundle.get('head') or bundle.get('fiH', False)
		echo = bundle.get('echo') or bundle.get('print', False)
		assets = bundle.get('assets') or bundle.get('folder') or bundle.get('fo', '{4284339c8bde}')
		assets = './' + assets.strip('./').strip('/') + '/'

		if os.path.isdir(assets):
			self.config['assets'] = assets
		else:
			for folder in self.assets_folders:
				if os.path.isdir(folder):
					assets = folder
					break

		self.config['assets'] = assets
		self.config['file'] = None

		if not data:
			if 'file' in bundle:
				bundle['f'] = bundle['file']

		for key, value in bundle.items():
			data = self.process_commands(bundle, key, data)
			bundle = self.bundle_clean(bundle, key)

		if header and header.endswith('.js'):
			data = self.process_includes(data, bundle)

		if echo or not self.just_return:
			self.set_doc_header(self.config['file'])
			print(data)

		return {
			'data': data,
			'file': self.config['file'],
			'files': self.files,
			'bundle': self.bundle_backup,
			'assets': self.config['assets']
		}

	def _F(self, bundle, data):
		original_data = data
		assets = self.config['assets']
		if 'file' in bundle:
			fi = bundle['file']
			self.files.append(fi)
			self.config['file'] = fi
			self.set_doc_header(fi)
			file_parts = fi.split('.')
			if len(file_parts) > 1:
				ext = file_parts[-1].lower()
			else:
				path = os.path.join(assets, fi).strip()
				if path.endswith('/'):
					path = self.is_folder(path)
			path_a = os.path.join(assets, ext, bundle['file'])
			path_b = os.path.join(assets, bundle['file'])
			path = path_a if os.path.exists(path_a) else path_b if os.path.exists(path_b) else None
			if path and os.path.exists(path):
				if path.endswith('.php'):
					return original_data
				data += open(path).read()
		return data

	def command_processor(self, commands, data):
		for command in commands:
			cdata = ''
			actions = self.extract_commands(command)
			for key, value in actions.items():
				if isinstance(value, list):
					for sub_key, sub_value in value.items():
						cdata = self.process_commands(value, sub_key, cdata)
				else:
					if 'exec' in actions:
						sub_exec = actions['exec']
						if sub_exec:
							sub_exec = sub_exec.strip()
							sub_exec = self._prepare_sub_exec(sub_exec)
							sub_commands = self.extract_commands(sub_exec)
							sub_commands = self.bundle_abbreviations(sub_commands)
							cdata = self.command_processor(sub_commands, cdata)
					cdata = self.process_commands(actions, key, cdata)
			data += cdata
		return data

	def find_assets_folder(self):
		for folder in self.assets_folders:
			if os.path.exists(folder):
				return folder
		return ''

	def extract_commands(self, string):
		commands = string.strip('[]').split(',')
		command_dict = {}
		
		for command in commands:
			if '=' in command:
				key, value = command.split('=', 1)
				command_dict[key] = value
			else:
				# Check if the next part is a value
				next_index = commands.index(command) + 1
				if next_index < len(commands) and '=' not in commands[next_index]:
					command_dict[command] = commands[next_index]
				else:
					command_dict[command] = None
					
		return command_dict



	# def virtual_get_command(self, input):
	# 	parts = input.split(self.config['[&]'])
	# 	result_array = {}
	# 	for part in parts:
	# 		key, value = part.split('=', 1)
	# 		if value.startswith('{'):
	# 			value = self.build_sub_commands(value)
	# 		result_array[key] = value
	# 	return result_array

	def build_commands(self, input_string):
		commands = self.extract_commands(input_string)
		for command in commands:
			if 'exec' == command:
				command_array = self.extract_commands(command)
			return command_array

	def extract_sub_commands(self, string):
		return re.findall(r'\{(.*?)\}', string)

	def virtual_get_sub_command(self, input):
		parts = input.split(self.config['{&}'])
		result_array = {}
		for part in parts:
			key, value = part.split('=', 1)
			result_array[key] = value
		return result_array

	def build_sub_commands(self, input_string):
		sub_commands = self.extract_sub_commands(input_string)
		for sub_command in sub_commands:
			sub_command_array = self.virtual_get_sub_command(sub_command)
			return sub_command_array

	def set_doc_header(self, ext):
		if not ext:
			return
		ext = ext.lower()
		if '.' in ext:
			ext = os.path.splitext(ext)[-1][1:]
		headers = {
			'css': 'Content-Type: text/css',
			'js': 'Content-Type: application/javascript',
			'json': 'Content-Type: application/json',
			'hash': 'Content-Type: application/json',
			'index': 'Content-Type: application/json',
			'dex': 'Content-Type: application/json',
			'fig': 'Content-Type: application/json',
			'ls': 'Content-Type: application/json',
			'csv': 'Content-Type: application/csv',
			'txt': 'Content-Type: text/plain',
			'log': 'Content-Type: text/plain',
			'sh': 'Content-Type: text/plain',
			'bat': 'Content-Type: text/plain',
			'md': 'Content-Type: text/markdown',
			'yaml': 'Content-Type: application/x-yaml',
			'yml': 'Content-Type: application/x-yaml',
			'html': 'Content-Type: text/html',
			'htm': 'Content-Type: text/html',
			'xml': 'Content-Type: application/xml',
			'svg': 'Content-Type: image/svg+xml',
			'ini': 'Content-Type: text/plain',
		}
		if ext in headers:
			print(headers[ext])

	def path_prep(self, path):
		relative_path = path.strip()
		while self.config['assets'].startswith(('.', '/')):
			self.config['assets'] = self.config['assets'].replace('.', '').replace('/', '')
		self.config['assets'] = './' + self.config['assets'].rstrip('/')

		new_path = os.path.join(self.config['assets'], relative_path)
		new_path = new_path.replace('../', './').replace('././', './')

		if 'public_html' in new_path or '.php' in new_path:
			exit('Hack Detected')

		return new_path

	def gen_comment(self, comment, path):
		comment = comment.replace("\r", "")
		if self.no_comments:
			return ''
		if path.lower().endswith(('.js', '.php', '.css', '.html', '.htm')):
			return f"\n\n/* {comment} */\n\n" if '\n' in comment else f"\n\n// {comment}\n\n"
		return ''

	def process_includes(self, data, bundle):
		if data is None:
			data = ''
		processed_content = ''
		if 'include' in bundle:
			files = bundle['include'].split(',')
			for f in files:
				f = f.strip()
				new_path = self.path_prep(f)
				if not os.path.exists(new_path):
					processed_content += self.gen_comment('(not found)=> ' + f, new_path)
					continue
				processed_content += self.gen_comment('(include)=> ' + f, new_path)
				if 'wrap' in bundle:
					processed_content += f"\n\nfunction {bundle['wrap']}() {{\n\n"
				if os.path.exists(new_path):
					self.files.append(new_path)
					self.config['file'] = new_path
					processed_content += open(new_path).read()
				if 'wrap' in bundle:
					processed_content += "\n\n}\n\n"
		lines = data.split('\n')
		for line in lines:
			match = re.match(r'^include:\s*(.*)$', line, re.I)
			if match:
				includes = match.group(1).strip().split(',')
				for relative_path in includes:
					relative_path = relative_path.strip()
					new_path = self.path_prep(relative_path)
					if os.path.exists(new_path):
						file_notify = self.gen_comment('(include)=> ' + relative_path, new_path)
						if 'wrap' in bundle:
							file_contents = file_notify + f"\n\nfunction {bundle['wrap']}() {{\n\n"
							file_contents += open(new_path).read()
							file_contents += "\n\n}\n\n"
						else:
							file_contents = file_notify + open(new_path).read()
							self.files.append(new_path)
							self.config['file'] = new_path
							self.set_doc_header(new_path)
						processed_content += self.process_includes(file_contents, bundle)
					else:
						processed_content += f"\n// File not found: {relative_path}\n"
			else:
				processed_content += line + "\n"
		return processed_content

	def remove_lines_containing_strings(self, text, string_list):
		lines = text.split('\n')
		filtered_lines = [line for line in lines if not any(string in line for string in string_list)]
		return '\n'.join(filtered_lines)

	def is_folder(self, path):
		if 'is' in self._get_request():
			if 'j' in self._get_request()['is']:
				path += 'index.js'
			if 'p' in self._get_request()['is']:
				path += 'index.php'
			if 'c' in self._get_request()['is']:
				path += 'index.css'
			if 'h' in self._get_request()['is']:
				path += 'index.htm'
			return path
		for file in ['index.js', 'index.htm', 'index.htm', 'index.php', 'index.html', 'index.css', 'script.js', 'module.js']:
			if os.path.exists(path + file):
				path += file
				return path
		if not os.path.exists(path):
			exit('No valid path found.')

	def process_commands(self, arr, key, data):
		# print(key)
		if data is None:
			data = ''
		arr = self.bundle_abbreviations(arr)
		if key == 'file':
			data = self._F(arr, data)
			data = self.process_includes(data, arr)
		if key == 'replace':
			data = self._replace(arr, data)
			data = self.process_includes(data, arr)
		if key == 'include':
			data = self.process_includes(data, arr)
		if key == 'after':
			data = self._after(arr, data)
			data = self.process_includes(data, arr)
		if key == 'dup':
			data = self._dup(arr, data)
		if key == 'isid':
			data = self._id_class(arr, data)
		if key == 'del':
			data = self._del(arr, data)
		if key == 'line':
			data = self._line(arr, data)
		if key == 'load':
			data = self._load(arr, data)
		if key == 'url':
			data = self._url(arr, data)
			data = self.process_includes(data, arr)
		if key == 'exec':
			exec = arr['exec']
			if exec:
				exec = exec.replace(',i:', ',include:').strip()
				exec = self._prepare_sub_exec(exec)
				commands = self.extract_commands(exec)
				# print(commands); _.isExit(__file__)
				print(commands)
				commands = self.bundle_abbreviations(commands)
				print(commands); _.isExit(__file__)
				data = self.command_processor(commands, data)
		return data

	def _prepare_sub_exec(self, exec_str):
		exec_str = exec_str.replace('{', '[').replace('}', ']')
		exec_str = exec_str.replace('(', '[').replace(')', ']')
		exec_str = exec_str.replace('<', '[').replace('>', ']')
		return exec_str

	def _replace(self, arr, data):
		replace = arr['replace']
		replace = replace.replace('\\n', "\n").replace('%2C', ',')
		replace_pairs = replace.split(',')
		if len(replace_pairs) % 2 != 0:
			raise Exception("Invalid replace pairs")
		for i in range(0, len(replace_pairs), 2):
			search = replace_pairs[i]
			replacement = replace_pairs[i + 1]
			search = self.string_config_replace(search)
			replacement = self.string_config_replace(replacement)
			if search == '1':
				data = f"{replacement}\n{data}"
				data = self.process_includes(data, arr)
				continue
			if search == '2':
				data = f"{data}\n{replacement}"
				data = self.process_includes(data, arr)
				continue
			if replacement.strip() == self.config['blank']:
				replacement = ''
			data = data.replace(search, replacement)
		return data

	def _after(self, arr, data):
		after = arr['after']
		search_pairs = after.split(',')
		if len(search_pairs) % 2 != 0:
			raise Exception("Invalid after pairs")
		lines = data.split("\n")
		for i in range(0, len(search_pairs), 2):
			search_string = search_pairs[i]
			add_string = search_pairs[i + 1]
			add_string = self.string_config_replace(add_string)
			for j in range(len(lines)):
				if search_string in lines[j]:
					leading_whitespace = ''
					if re.match(r'^\s*', lines[j]):
						leading_whitespace = re.match(r'^\s*', lines[j]).group()
					lines[j] += f"\n{leading_whitespace}{add_string}"
		return "\n".join(lines)

	def _del(self, arr, data):
		strings_to_remove = arr['del'].split(',')
		data = self.remove_lines_containing_strings(data, strings_to_remove)
		return data

	def _line(self, arr, data):
		replace = arr['line']
		replace = replace.replace('\\n', "\n").replace('%2C', ',')
		replace_pairs = replace.split(',')
		if len(replace_pairs) % 2 != 0:
			raise Exception("Invalid replace pairs")
		for i in range(0, len(replace_pairs), 2):
			search = replace_pairs[i]
			replacement = replace_pairs[i + 1]
			if search == '1':
				data = f"{replacement}\n{data}"
				continue
			if search == '2':
				data = f"{data}\n{replacement}"
				continue
			lines = data.split("\n")
			for j, line in enumerate(lines):
				if search in line:
					leading_whitespace = ''
					if re.match(r'^\s*', line):
						leading_whitespace = re.match(r'^\s*', line).group()
					replacement = replacement.replace("\n", f"\n{leading_whitespace}")
					lines[j] = f"{leading_whitespace}{replacement}"
			data = "\n".join(lines)
		return data

	def _load(self, arr, data):
		data += "\n\n// (include)=> load.js\n\n"
		data += open(self.config['js'] + 'load.js').read()
		resources = self.yf(open(self.config['js'] + 'c/l/resources.yml').read())
		load = arr['load'].replace('%2C', ',')
		load_list = load.split(',')
		build = False
		if load_list:
			build = True
			if len(load_list) == 1 and load_list[0] == '1':
				build = False
		if build:
			add = ''
			# add = "\n\n// (queue)=> push\n\n"
			# add += "_.lo	def yf(self, data):	template = '        "c1c5-ce020329",' + "\n"
			for lo in load_list:
				rep = ''
				if self.config['&'] in lo:
					parts = lo.split(self.config['&'], 2)
					lo = parts[0]
					rep = '&' + parts[1].replace(self.config['&'], '&').replace(self.config[','], ',')
				if lo in resources:
					js = template.replace('c1c5', resources[lo]).replace('-ce020329', rep)
					add += js
			add += "]);\n\n"
			data += add
		return data

	def _url(self, arr, data):
		url = arr.get('url')
		post = arr.get('url-post')
		head = arr.get('url-header')
		if not url:
			return data
		has_http = 'https://' in url or 'http://' in url
		if not has_http:
			url = 'https://' + url
		form_data = {}
		headers = []
		if post:
			items = post.split(',')
			for item in items:
				item = self.string_config_replace(item)
				k, v = item.split('=', 1)
				form_data[k] = v
		if head:
			items = head.split(',')
			for item in items:
				item = self.string_config_replace(item)
				k, v = item.split('=', 1)
				headers.append((k, v))
		response = self.curl(url, form_data, headers)
		data = f"\n\n{response}\n\n"
		return data

	def curl(self, url, form_data, headers):
		import requests
		response = requests.post(url, data=form_data, headers=dict(headers))
		return response.text

	def string_config_replace(self, string):
		for key, value in self.config.items():
			string = string.replace(value, key)
		return string

	def yf(self, data):
		import yaml
		return yaml.safe_load(data)

	def _id_class(self, arr, data):
		if 'id' in arr:
			rep = arr['id'].split(',')
			data = data.replace(f"#{rep[0]}", f"#{rep[1]}")
			data = data.replace(f"'{rep[0]}'", f"'{rep[1]}'")
			data = data.replace(f'"{rep[0]}"', f'"{rep[1]}"')
		if 'class' in arr:
			rep = arr['class'].split(',')
			data = data.replace(f".{rep[0]}", f".{rep[1]}")
			data = data.replace(f"getElementById('{rep[0]}')", f"querySelectorAll('.{rep[1]}')[0]")
			data = data.replace(f'getElementById("{rep[0]}")', f'querySelectorAll(".{rep[1]}")[0]')
			data = data.replace(f"getElementById( '{rep[0]}' )", f"querySelectorAll('.{rep[1]}')[0]")
			data = data.replace(f'getElementById( "{rep[0]}" )', f'querySelectorAll(".{rep[1]}")[0]')
		return data

	def _dup(self, arr, data):
		duplication_instructions = arr['dup'].split(',')
		lines = data.split("\n")
		result_lines = []
		for i in range(0, len(duplication_instructions), 2):
			num_duplicates = int(duplication_instructions[i])
			pattern = duplication_instructions[i + 1]
			for line in lines:
				if pattern in line:
					for j in range(1, num_duplicates + 1):
						modified_line = re.sub(r'____[a-z]', lambda match: match.group() + str(j), line)
						result_lines.append(modified_line)
					continue
				result_lines.append(line)
			lines = result_lines
			result_lines = []
		return "\n".join(lines)

	def _dup2(self, arr, data):
		duplication_instructions = arr['dup'].split(',')
		case_insensitive = 'dup-ci' in arr or 'ci' in arr
		lines = data.split("\n")
		result_lines = []
		for line in lines:
			found = False
			for value in duplication_instructions:
				if (case_insensitive and value.lower() in line.lower()) or (not case_insensitive and value in line):
					found = True
			if found:
				result_lines.append(line)
			result_lines.append(line)
		return "\n".join(result_lines)
	
	def remove_lines_containing_strings(self, text, string_list):
		lines = text.split('\n')
		filtered_lines = [line for line in lines if not any(string in line for string in string_list)]
		return '\n'.join(filtered_lines)

	def _del(self, arr, data):
		strings_to_remove = arr['del'].split(',')
		data = self.remove_lines_containing_strings(data, strings_to_remove)
		return data

	def _line(self, arr, data):
		replace = arr['line']
		replace = replace.replace('\\n', "\n").replace('%2C', ',')
		replace_pairs = replace.split(',')
		if len(replace_pairs) % 2 != 0:
			raise Exception("Invalid replace pairs")
		for i in range(0, len(replace_pairs), 2):
			search = replace_pairs[i]
			replacement = replace_pairs[i + 1]
			if search == '1':
				data = f"{replacement}\n{data}"
				continue
			if search == '2':
				data = f"{data}\n{replacement}"
				continue
			lines = data.split("\n")
			for j, line in enumerate(lines):
				if search in line:
					leading_whitespace = ''
					if re.match(r'^\s*', line):
						leading_whitespace = re.match(r'^\s*', line).group()
					replacement = replacement.replace("\n", f"\n{leading_whitespace}")
					lines[j] = f"{leading_whitespace}{replacement}"
			data = "\n".join(lines)
		return data

	def _line(self, arr, data):
		replace = arr['line']
		replace = replace.replace('\\n', "\n").replace('%2C', ',')
		replace_pairs = replace.split(',')
		if len(replace_pairs) % 2 != 0:
			raise Exception("Invalid replace pairs")
		for i in range(0, len(replace_pairs), 2):
			search = replace_pairs[i]
			replacement = replace_pairs[i + 1]
			if search == '1':
				data = f"{replacement}\n{data}"
				continue
			if search == '2':
				data = f"{data}\n{replacement}"
				continue
			lines = data.split("\n")
			for j, line in enumerate(lines):
				if search in line:
					leading_whitespace = ''
					if re.match(r'^\s*', line):
						leading_whitespace = re.match(r'^\s*', line).group()
					replacement = replacement.replace("\n", f"\n{leading_whitespace}")
					lines[j] = f"{leading_whitespace}{replacement}"
			data = "\n".join(lines)
		return data

	def _load(self, arr, data):
		data += "\n\n// (include)=> load.js\n\n"
		data += open(self.config['js'] + 'load.js').read()
		resources = self.yf(open(self.config['js'] + 'c/l/resources.yml').read())
		load = arr['load'].replace('%2C', ',')
		load_list = load.split(',')
		build = False
		if load_list:
			build = True
			if len(load_list) == 1 and load_list[0] == '1':
				build = False
		if build:
			add = "\n\n// (queue)=> push\n\n"
			add += "_.load.queue.push([\n"
			template = '        "c1c5-ce020329",' + "\n"
			for lo in load_list:
				rep = ''
				if self.config['&'] in lo:
					parts = lo.split(self.config['&'], 2)
					lo = parts[0]
					rep = '&' + parts[1].replace(self.config['&'], '&').replace(self.config[','], ',')
				if lo in resources:
					js = template.replace('c1c5', resources[lo]).replace('-ce020329', rep)
					add += js
			add += "]);\n\n"
			data += add
		return data

	def _url(self, arr, data):
		url = arr.get('url')
		post = arr.get('url-post')
		head = arr.get('url-header')
		if not url:
			return data
		has_http = 'https://' in url or 'http://' in url
		if not has_http:
			url = 'https://' + url
		form_data = {}
		headers = []
		if post:
			items = post.split(',')
			for item in items:
				item = self.string_config_replace(item)
				k, v = item.split('=', 1)
				form_data[k] = v
		if head:
			items = head.split(',')
			for item in items:
				item = self.string_config_replace(item)
				k, v = item.split('=', 1)
				headers.append((k, v))
		response = self.curl(url, form_data, headers)
		data = f"\n\n{response}\n\n"
		return data

	def curl(self, url, form_data, headers):
		import requests
		response = requests.post(url, data=form_data, headers=dict(headers))
		return response.text

	def string_config_replace(self, string):
		for key, value in self.config.items():
			string = string.replace(value, key)
		return string

	def yf(self, data):
		import yaml
		return yaml.safe_load(data)

	def is_folder(self, path):
		if 'is' in self._get_request():
			if 'j' in self._get_request()['is']:
				path += 'index.js'
			if 'p' in self._get_request()['is']:
				path += 'index.php'
			if 'c' in self._get_request()['is']:
				path += 'index.css'
			if 'h' in self._get_request()['is']:
				path += 'index.htm'
			return path
		for file in ['index.js', 'index.htm', 'index.htm', 'index.php', 'index.html', 'index.css', 'script.js', 'module.js']:
			if os.path.exists(path + file):
				path += file
				return path
		if not os.path.exists(path):
			exit('No valid path found.')

	def _F(self, bundle, data):
		original_data = data
		assets = self.config['assets']
		if 'file' in bundle:
			fi = bundle['file']
			self.files.append(fi)
			self.config['file'] = fi
			self.set_doc_header(fi)
			file_parts = fi.split('.')
			if len(file_parts) > 1:
				ext = file_parts[-1].lower()
			else:
				path = os.path.join(assets, fi).strip()
				if path.endswith('/'):
					path = self.is_folder(path)
			path_a = os.path.join(assets, ext, bundle['file'])
			path_b = os.path.join(assets, bundle['file'])
			path = path_a if os.path.exists(path_a) else path_b if os.path.exists(path_b) else None
			if path and os.path.exists(path):
				data += open(path).read()
		return data

	def command_processor(self, commands, data):
		for command in commands:
			cdata = ''
			# actions = self.extract_commands(command)
			actions = command
			# print(actions); _.isExit(__file__)
			action_keys = list(actions.keys())  # Create a list of the keys to avoid modifying the dictionary while iterating
			for key in action_keys:
				value = actions[key]
				if isinstance(value, list):
					for sub_key, sub_value in value.items():
						cdata = self.process_commands(value, sub_key, cdata)
				else:
					if 'exec' in actions:
						sub_exec = actions['exec']
						if sub_exec:
							sub_exec = sub_exec.strip()
							sub_exec = self._prepare_sub_exec(sub_exec)
							sub_commands = self.extract_commands(sub_exec)
							sub_commands = self.bundle_abbreviations(sub_commands)
							cdata = self.command_processor(sub_commands, cdata)
					cdata = self.process_commands(actions, key, cdata)
			data += cdata
		return data


	def find_assets_folder(self):
		for folder in self.assets_folders:
			if os.path.exists(folder):
				return folder
		return ''

	def extract_commands(self, string):
		commands = re.findall(r'\[(.*?)\]', string)
		command_dict = {}
		for command in commands:
			key_value_pairs = command.split(',')
			for pair in key_value_pairs:
				if '=' in pair:
					key, value = pair.split('=', 1)
					command_dict[key] = value
				else:
					command_dict[pair] = None
		return command_dict

	def virtual_get_command(self, input):
		# if not input.startswith('['):
		# 	input = f'[{input}]'
		input = input.replace('include:','f=')
		parts = input.split(self.config['[&]'])
		
		# print(self.config['[&]']); _.isExit(__file__)
		# print(parts); _.isExit(__file__)
		result_array = {}
		for part in parts:
			part = part.strip()
			try:
				key, value = part.split('=', 1)
			except:
				print(part); _.isExit(__file__)
			if value.startswith('{'):
				value = self.build_sub_commands(value)
			result_array[key] = value
		# print(result_array); _.isExit(__file__)
		return result_array


	def build_commands(self, input_string):
		commands = self.extract_commands(input_string)
		for command in commands:
			if 'exec' == command:
				command_array = self.extract_commands(command)
			return command_array

	def extract_sub_commands(self, string):
		return re.findall(r'\{(.*?)\}', string)

	def virtual_get_sub_command(self, input):
		parts = input.split(self.config['{&}'])
		result_array = {}
		for part in parts:
			key, value = part.split('=', 1)
			result_array[key] = value
		return result_array

	def build_sub_commands(self, input_string):
		sub_commands = self.extract_sub_commands(input_string)
		for sub_command in sub_commands:
			sub_command_array = self.virtual_get_sub_command(sub_command)
			return sub_command_array

	def set_doc_header(self, ext):
		if not ext:
			return
		ext = ext.lower()
		if '.' in ext:
			ext = os.path.splitext(ext)[-1][1:]
		headers = {
			'css': 'Content-Type: text/css',
			'js': 'Content-Type: application/javascript',
			'json': 'Content-Type: application/json',
			'hash': 'Content-Type: application/json',
			'index': 'Content-Type: application/json',
			'dex': 'Content-Type: application/json',
			'fig': 'Content-Type: application/json',
			'ls': 'Content-Type: application/json',
			'csv': 'Content-Type: application/csv',
			'txt': 'Content-Type: text/plain',
			'log': 'Content-Type: text/plain',
			'sh': 'Content-Type: text/plain',
			'bat': 'Content-Type: text/plain',
			'md': 'Content-Type: text/markdown',
			'yaml': 'Content-Type: application/x-yaml',
			'yml': 'Content-Type: application/x-yaml',
			'html': 'Content-Type: text/html',
			'htm': 'Content-Type: text/html',
			'xml': 'Content-Type: application/xml',
			'svg': 'Content-Type: image/svg+xml',
			'ini': 'Content-Type: text/plain',
		}
		if ext in headers:
			print(headers[ext])


def action():

	_.e('Error','extract_commands not working yet')
	# Example usage of the TMI class with the given URL parameters

	# Initialize the TMI class
	tmi = TMI()

	# Define the bundle based on the given URL parameters
	bundle1 = {
		'api': '2ae35777d9f4',
		'exec': '[r=1,include:sds/js/load.js,///,-,_url_or_html_,https://tbox.cx/js/ck/?test_cookie=one%20two%20three]',
		'v': '1'
	}

	# Process the bundle using the TMI class
	result = tmi.tmi(bundle1)
	print(result)
	# Print the result to see if it matches the expected output
	print(result['data'])
	# print("File processed:", result['file'])
	# print("Files included:", result['files'])
	# print("Bundle backup:", result['bundle'])
	# print("Assets path:", result['assets'])


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);