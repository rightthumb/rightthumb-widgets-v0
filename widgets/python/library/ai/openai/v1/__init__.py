import os
import openai # type: ignore
# import copy
# print(copy.__file__)
# import sys; sys.exit(0)

import base64
import json



class GPT: # GPT Assistant: class for interacting with OpenAI's GPT models
	def __init__(self, api_key=None, model="gpt-4o", m=False, token_mode="x"):
		if m:
			model = "gpt-4o-mini"
		self.log = []
		self.activity = []

		# Load openai api key
		self.api_key = False
		rt_path = os.path.expanduser('~/.rt')
		key_file = os.path.join(rt_path, 'openai.key')
		config_file = os.path.join(rt_path, '.config.hash')

		if os.path.exists(key_file):
			with open(key_file, 'r', encoding='utf-8') as f:
				self.api_key = f.read().strip()
		elif os.path.exists(config_file):
			with open(config_file, 'r', encoding='utf-8') as f:
				try:
					config = json.load(f)
					self.api_key = config.get('openai', False)
				except json.JSONDecodeError:
					self.api_key = False



		if not self.api_key:
			raise ValueError("File ~/.rt/openai.key not found.")
		openai.api_key = self.api_key

		self.model = model
		self.messages = []
		self.token_limit = self._resolve_token_limit(token_mode)
		

	def _resolve_token_limit(self, mode):
		mode = mode.lower()[0]
		return {
			"t": 128,
			"s": 512,
			"m": 1024,
			"l": 2048,
			"h": 4096,
			"x": 8192,
		}.get(mode, 1024)

	def set_model(self, model):
		self.model = model

	def reset_conversation(self):
		self.messages = []

	def chat(self, *prompt, system="You are a helpful assistant.", temperature=0.7,  s=None):
		parts = []
		files = 0
		for p in prompt:
			if os.path.exists(p):
				with open(p, 'r', encoding='utf-8') as f:
					parts.append(f.read()+"\n")
					files += 1
			else:
				parts.append(p)
		if files > 0:
			prompt = '\n'.join(parts).strip()
		else:
			prompt = ' '.join(parts).strip()

		if not s is None: system = s
		system_prompt = system
		self.activity.append({
			"function": 'chat',
			"system_prompt": system_prompt,
			"temperature": temperature,
			"model": self.model,
			"token_limit": self.token_limit
		})
		self.log.append({
			"prompt": prompt,
		})
		if not self.messages:
			self.messages.append({"role": "system", "content": system_prompt})
		self.messages.append({"role": "user", "content": prompt})

		response = openai.ChatCompletion.create(
			model=self.model,
			messages=self.messages,
			temperature=temperature,
			max_tokens=self.token_limit,
		)
		reply = response.choices[0].message.content
		self.log.append({
			"reply": reply,
		})
		self.messages.append({"role": "assistant", "content": reply})
		return reply



	def extract_code(self,text):
		if not '```' in text and not '```' in text:
			return text
		import re
		pattern = r'```(?:[\w+-]*)\s*(.*?)```'
		return re.findall(pattern, text, re.DOTALL)


	def clean_binary_to_text(self,path):
		import os
		import re
		try:
			with open(path, 'rb') as f:
				raw = f.read()
				# Remove null bytes and decode with 'utf-8' fallback
				text = raw.replace(b'\x00', b'').decode('utf-8', errors='ignore')
				# Optional: Strip non-printable/control characters (except newline/tab)
				text = re.sub(r'[^\x09\x0A\x0D\x20-\x7E\u00A0-\uFFFF]', '', text)
				return text
		except Exception as e:
			print(f"Failed to read {path}: {e}")
			return None

	def prompt(self, *prompt, system="You are a helpful assistant.", temperature=0.7,  s=None, code=True):
		# print(f"Prompt: {prompt}"); return
		parts = []
		files = 0
		text = {}
		key = 0
		text[key] = []
		if len(prompt) and type(prompt[0]) is list:
			prompt = prompt[0]
		for p in prompt:
			# print(f"'{p}'")
			if os.path.exists(p):
				# parts.append(f"|File: {p}|")
				if os.path.isfile(p):
					key += 1
					text[key] = []
					text[key].append(self.clean_binary_to_text(p))
				# parts.append(f"|File: {p}|")
				# 	parts.append(self.clean_binary_to_text(p) + "\n") # Read file content
				# 	files += 1
				# else:
				# 	print(f"Skipping invalid file: {p}")

			else:
				text[key].append(p)
				parts.append(p)
			# print(p)
		# if files > 0:
		# 	prompt = '\n'.join(parts).strip()
		# else:
		# 	prompt = ' '.join(parts).strip()
		prompt = ''
		for k in text:
			if len(text[k]) > 0:
				prompt += ' '.join(text[k]) + '\n\n'
		
		# print(prompt); return prompt
		if not s is None: system = s
		system_prompt = system
		self.activity.append({
			"function": 'chat',
			"system_prompt": system_prompt,
			"temperature": temperature,
			"model": self.model,
			"token_limit": self.token_limit
		})
		self.log.append({
			"prompt": prompt,
		})

		response = openai.ChatCompletion.create(
			model=self.model,
			messages=[
				{"role": "system", "content": system_prompt},
				{"role": "user", "content": prompt}
			],
			temperature=temperature,
			max_tokens=self.token_limit,
		)
		reply = response.choices[0].message.content
		self.log.append({
			"reply": reply,
		})
		if code:
			reply = self.extract_code(reply)
		return reply

	def vision(self, prompt, image_path):
		with open(image_path, "rb") as f:
			b64_image = base64.b64encode(f.read()).decode("utf-8")

		response = openai.ChatCompletion.create(
			model="gpt-4o",
			messages=[{
				"role": "user",
				"content": [
					{"type": "text", "text": prompt},
					{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}}
				]
			}],
			max_tokens=self.token_limit,
		)
		results = response.choices[0].message.content

		return results

	def transcribe(self, audio_path):
		with open(audio_path, "rb") as f:
			result = openai.Audio.transcribe("whisper-1", f)
		return result['text']

	def translate(self, audio_path):
		with open(audio_path, "rb") as f:
			result = openai.Audio.translate("whisper-1", f)
		return result['text']

	def speech(self, text, voice="alloy", output_file="speech.mp3"):
		response = openai.Audio.speech.create(
			model="tts-1",
			voice=voice,
			input=text
		)
		with open(output_file, "wb") as f:
			f.write(response.content)
		return output_file

	def embed(self, text):
		response = openai.Embedding.create(
			input=[text],
			model="text-embedding-3-small"
		)
		return response['data'][0]['embedding']

	def pr(self, *args, c=None, line=False, p=True):
		"""
		Returns the combined args as a single colored string using ANSI color codes.
		
		:param args: Strings to be combined and colorized
		:param c: Color name as string (default is 'cyan')
		:return: Colored string
		"""
		colors = {
			'black':   '\033[30m',
			'red':     '\033[31m',
			'green':   '\033[32m',
			'yellow':  '\033[33m',
			'blue':    '\033[34m',
			'magenta': '\033[35m',
			'purple':  '\033[35m',
			'cyan':    '\033[36m',
			'white':   '\033[37m',
			'reset':   '\033[0m'
		}

		if line:
			if len() == 1:
				args = [self.terminal_line(args[0])]
			else:
				args = [self.terminal_line()]
		if c:
			color_code = colors.get(c.lower(), colors['cyan'])  # default to cyan if invalid
			reset = colors['reset']
			processed = color_code + ' '.join(str(arg) for arg in args) + reset
		else:
			processed = ' '.join(str(arg) for arg in args)
		if p:
			print(processed)
		return processed
	

	def terminal_line(self,char='_'):
		"""
		Returns a line made of the given character that spans the terminal width.
		
		:param char: The character to repeat (default is '─')
		:return: A string that spans the terminal width
		"""
		import shutil
		width = shutil.get_terminal_size((80, 20)).columns
		return char * width


	def info(self):
		tokens_price ='''
chat:
  - name: gpt-4o              # Chat + vision + audio input
	max_tokens: 128000
	input_price_per_1k: 0.005
	output_price_per_1k: 0.015

  - name: gpt-4o-mini         # like gpt-4o, but lighter and cheaper
	max_tokens: 128000
	input_price_per_1k: 0.0015
	output_price_per_1k: 0.0045

  - name: gpt-4-turbo         # Chat + tools (functions/files)
	max_tokens: 128000
	input_price_per_1k: 0.01
	output_price_per_1k: 0.03

  - name: gpt-3.5-turbo       # Chat only
	max_tokens: 16000
	input_price_per_1k: 0.0005
	output_price_per_1k: 0.0015

vision:
  - name: gpt-4o              # Only GPT-4o supports vision
	note: Vision included at no extra cost (text token pricing applies)

tts:
  - name: tts-1               # Base model
	price_per_second: 0.015

  - name: tts-1-hd            # High-definition model
	price_per_second: 0.030

voices:
  - alloy     # Available voice
  - echo      # Available voice
  - fable     # Available voice
  - onyx      # Available voice
  - nova      # Available voice
  - shimmer   # Available voice

audio:
  - name: whisper-1           # Used for both transcribe and translate
	price_per_minute: 0.006

embedding:
  - name: text-embedding-3-small   # Smaller, faster embedding model
	dimensions: 1536
	price_per_1k: 0.0001

  - name: text-embedding-3-large   # More accurate, larger embedding model
	dimensions: 3072
	price_per_1k: 0.0004
'''

		self.pr(tokens_price, c='cyan')
		self.pr(line=1, c='yellow')
		self.pr(self.list_supported_models(), c='cyan')

	def list_supported_models(self,yaml=True):
		"""
		Returns a dictionary of supported models categorized by type.
		"""
		if yaml:
			return '''
chat:
  - gpt-4o              # Chat + vision + audio input
  - gpt-4o-mini         # like gpt-4o, but lighter and cheaper
  - gpt-4-turbo         # Chat + tools (functions/files)
  - gpt-3.5-turbo       # Chat only

vision:
  - gpt-4o              # Only GPT-4o supports vision

tts:
  - tts-1               # Base model
  - tts-1-hd            # High-definition model

voices:
  - alloy               # Available voice
  - echo                # Available voice
  - fable               # Available voice
  - onyx                # Available voice
  - nova                # Available voice
  - shimmer             # Available voice

audio:
  - whisper-1           # Used for both transcribe and translate

embedding:
  - text-embedding-3-small   # Smaller, faster embedding model
  - text-embedding-3-large   # More accurate, larger embedding model

'''
		return {
			"chat": [
				"gpt-4o",              # Chat + vision + audio input
				"gpt-4o-mini",         # like gpt-4o, but lighter and cheaper
				"gpt-4-turbo",         # Chat + tools (functions/files)
				"gpt-3.5-turbo",       # Chat only
			],
			"vision": [
				"gpt-4o",              # Only GPT-4o supports vision
			],
			"tts": [
				"tts-1",               # Base model
				"tts-1-hd",            # High-definition model
			],
			"voices": [
				"alloy", "echo", "fable", "onyx", "nova", "shimmer"
			],
			"audio": [
				"whisper-1",           # Used for both transcribe and translate
			],
			"embedding": [
				"text-embedding-3-small",
				"text-embedding-3-large",
			]
		}

	def help(self):
		self.pr(self.terminal_line('='), c='yellow')
		self.pr('GPT Class Help', c='green')
		self.pr(self.terminal_line('='), c='yellow')
		self.pr()

		self.pr('Available Methods:', c='cyan')
		methods = [
			('chat(..., system=..., temperature=...)', 'Chat with memory. Accepts text or file paths.'),
			('prompt(..., system=..., temperature=...)', 'One-shot prompt (no memory).'),
			('vision(prompt, image_path)',              'Multimodal (image + text input).'),
			('transcribe(audio_path)',                  'Transcribe audio using Whisper.'),
			('translate(audio_path)',                   'Translate audio using Whisper.'),
			('speech(text, voice="alloy")',             'Convert text to speech. Saves output file.'),
			('embed(text)',                             'Get embedding vector from input text.'),
			('reset_conversation()',                    'Clear conversation history.'),
			('set_model(model)',                        'Change the active model (e.g., gpt-4o-mini).'),
			('info()',                                  'Show model pricing and limits.'),
			('list_supported_models(yaml=True)',        'Return supported model info (YAML or dict).'),
			('help()',                                  'Show this help screen.')
		]

		for method, desc in methods:
			self.pr('  ' + method.ljust(38), desc, c='white')

		self.pr()
		self.pr('Note:', 'chat() and prompt() accept multiple arguments or filenames. Files are auto-read.', c='cyan')
		self.pr(self.terminal_line('-'), c='yellow')
		self.info()