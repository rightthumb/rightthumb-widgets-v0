import sys, time
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
	pass
	_.switches.register( 'Roll', '-r,-roll', 'senior developer, lawyer' )
	_.switches.register( 'Prompt', '-p,-prompt' )
	_.switches.register( 'Model', '-m,-model','3 4 4k | gpt-3.5-turbo gpt-4 gpt-4-32k' )
	_.switches.register( 'Tokens', '-t,-tokens', 's m l | small medium large' )
	_.switches.register( 'TokensMinus', '-tm,-minus', '1000' )
	_.switches.register( 'Query', '-q,-query', 'To add a line to answer based on __.isData()' )
	_.switches.register( 'JustPrompt', '-j,-jp', 'depreciated' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'usage': [
	],
	'relatedapps': [
	],
	'prerequisite': [
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [
	],
	'notes': [
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

def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

interact = _.getTable('ai-bot-interaction.index')
if not 'success' in interact: interact = {'success':[],'failure':[],'chat':[]}
if not 'ai' in interact: interact['ai'] = []
_keychain = _.regImp(__.appReg, 'keychain')

if not 'openai' in _v.fig:
	_.pr('Missing config',r='red')
	_.pr('Run `p config`',r='yellow')
	_.isExit(__file__)









def action(): pass





## Start: Legacy code

def ai(prompt, model='gpt-4'):

	import openai
	import time
	# pip install openai==0.28
	openai.api_key = _v.fig['openai']
	response = openai.ChatCompletion.create(
		model="gpt-4",
		messages=[
			{"role": "user", "content": "How do I list all files in a directory using Python?"}
		]
	)
	print(response['choices'][0]['message']['content'])

	import openai
	import time
	# Model manager
	if _.switches.isActive('Model') and '3' in _.switches.value('Model'):   model='gpt-3.5-turbo'
	elif _.switches.isActive('Model') and 'k' in _.switches.value('Model'): model='gpt-4-32k'
	elif _.switches.isActive('Model') and '4' in _.switches.value('Model'): model='gpt-4'

	# Base max_tokens for each model
	model_token_limits = {
		"gpt-4-32k": 32_768,
		"gpt-4": 8_192,
		"gpt-3.5-turbo": 4_096
	}

	# Default to 2,048 tokens for any unknown models
	max_tokens = model_token_limits.get(model, 2_048)
	if _.switches.isActive('TokensMinus'):
		max_tokens -= int(_.switches.value('TokensMinus'))
	# Adjust max_tokens based on 'small', 'medium', 'large' switches
	if _.switches.isActive('Tokens'):
		if 's' in _.switches.value('Tokens'):
			max_tokens = int(max_tokens * 0.1)  # 10% of the model's max tokens for 'small'
		elif 'm' in _.switches.value('Tokens'):
			max_tokens = int(max_tokens * 0.5)  # 50% of the model's max tokens for 'medium'
		elif 'l' in _.switches.value('Tokens'):
			max_tokens = max_tokens             # Use full max tokens for 'large'

	try:
		# Set OpenAI API key
		openai.api_key = _v.fig['openai']

		# Make a request to OpenAI API
		response = openai.ChatCompletion.create(
			model=model,
			messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": prompt}
			],
			temperature=0.9,
			top_p=1,
			frequency_penalty=0.0,
			presence_penalty=0.6,
			max_tokens=max_tokens,
			stop=None,
		)

		# Output the response
		_.pr(response["choices"][0]["message"]["content"])

		# Track interaction
		global interact
		interact['ai'].append({
			'epoch': time.time(),
			'prompt': prompt,
			'response': response["choices"][0]["message"]["content"]
		})
		_.saveTable(interact, 'ai-bot-interaction.index', p=0)

	except AttributeError as e:
		_.pr(f"An unexpected error occurred: {str(e)}", c='red')

def action_____OLD():
	tail = '\n\n'
	prompt = ''
	if _.isData():
		if _.switches.isActive('Query'):
			prompt += 'Answer based on this:'+tail
		prompt += '\n'.join(_.isData())+tail
	if _.switches.isActive('Prompt'):
		if _.switches.isActive('Query'):
			prompt += 'The query:'+tail
		Prompt = ' '.join(_.switches.values('Prompt'))
		Prompt = Prompt.strip()
		# if not Prompt.endswith(':'): Prompt += ':'
		Prompt += '\n'
		prompt += Prompt

	try:
		ai(prompt)
	except Exception as e:
		_.pr(e, c='red')
		import platform
		_.pr('An unexpected error occurred', c='red')
		if platform.system() == 'Windows':
			_.pr('pip install openai', c='yellow')
		else:
			_.pr('pip install openai==0.28', c='yellow')

## End: Legacy code


















import openai # pip install openai==0.28.0

import tiktoken
import time
class AIChat_028:
	def __init__(self, 
					api_key, 
					model='gpt-4', 
					log_file=None, 
					t=False,  
					tm=None,
					roll=None,
				):
		self.roll = roll
		if not self.roll:
			self.roll = 'senior developer'
		self.size = t # str: s,m,l for small, medium, large
		self.minus = tm # int: minus tokens
		if not self.size:
			self.size = False
		if not self.minus:
			self.minus = False
		else:
			self.minus = int(self.minus)
		
		self.api_key = api_key
		self.model = model
		self.log_file = log_file
		self.interactions = []
		openai.api_key = self.api_key

		self.model_token_limits = {
			"gpt-4-32k": 32768,
			"gpt-4": 8192,
			"gpt-3.5-turbo": 4096
		}

	def estimate_tokens(self, messages):
		try:
			encoding = tiktoken.encoding_for_model(self.model)
		except KeyError:
			encoding = tiktoken.get_encoding("cl100k_base")
		total = 0
		for msg in messages:
			total += 4  # OpenAI message overhead
			for key, value in msg.items():
				total += len(encoding.encode(str(value)))
		total += 2  # Assistant reply overhead
		_v.log(total, _v.gptTokens)
		return total

	def ask(self, 
				prompt, 
				temperature=0.9, 
				top_p=1.0, 
				presence_penalty=0.6,
				frequency_penalty=0.0, 
				t=None, 
				tm=None,
				roll=None,
			):
		if not roll:
			roll = self.roll
		if t:
			token_scale = t
		else:
			token_scale = self.size

		if tm:
			tokens_minus = tm
		else:
			tokens_minus = self.minus


		try:
			messages = [
				{"role": "system", "content": f"Act as a {roll}."},
				{"role": "user", "content": prompt}
			]

			total_limit = self.model_token_limits.get(self.model, 2048)
			used_tokens = self.estimate_tokens(messages)

			if token_scale in ('s', 'small'):
				max_tokens = int(total_limit * 0.1)
			elif token_scale in ('m', 'medium'):
				max_tokens = int(total_limit * 0.5)

			else:
				max_tokens = total_limit - used_tokens

			max_tokens -= tokens_minus
			max_tokens = max(1, max_tokens)  # ensure it's always > 0

			response = openai.ChatCompletion.create(
				model=self.model,
				messages=messages,
				temperature=temperature,
				top_p=top_p,
				frequency_penalty=frequency_penalty,
				presence_penalty=presence_penalty,
				max_tokens=max_tokens
			)

			reply = response["choices"][0]["message"]["content"]
			self.interactions.append({
				'epoch': time.time(),
				'prompt': prompt,
				'response': reply
			})

			if self.log_file:
				_.saveTable(self.interactions, self.log_file, p=0)

			# _.pr(reply)

			return reply

		except Exception as e:
			_.pr(f"[ERROR] {e}", c='red')
			return None














# class AIChat_1x:
#     import time
#     import tiktoken
#     from openai import OpenAI
#     def __init__(self, 
#                  api_key, 
#                  model='gpt-4', 
#                  log_file=None, 
#                  t=False, 
#                  tm=None):
		
#         self.size = t  # Token scale: 's', 'm', 'l', or False
#         self.minus = int(tm) if tm else 0
#         self.model = model
#         self.log_file = log_file
#         self.interactions = []
#         self.client = OpenAI(api_key=api_key)


#         self.model_token_limits = {
#             "gpt-4-32k": 32768,
#             "gpt-4": 8192,
#             "gpt-3.5-turbo": 4096,
#             "gpt-4-turbo-preview": 128000,  # Latest GPT-4 Turbo
#             "gpt-4o": 128000,              # Latest flagship model
#             "gpt-3.5-turbo-16k": 16384     # Newer 3.5 Turbo with larger context
#         }

#     def estimate_tokens(self, messages):
#         try:
#             encoding = tiktoken.encoding_for_model(self.model)
#         except KeyError:
#             encoding = tiktoken.get_encoding("cl100k_base")

#         total = 0
#         for msg in messages:
#             total += 4  # Base per-message overhead
#             for key, value in msg.items():
#                 total += len(encoding.encode(str(value)))
#         total += 2  # Final reply overhead

#         import _rightThumb._vars as _v
#         _v.log(total, _v.gptTokens)
#         return total

#     def ask(self, 
#             prompt, 
#             temperature=0.9, 
#             top_p=1.0, 
#             presence_penalty=0.6, 
#             frequency_penalty=0.0,
#             t=None, 
#             tm=None):

#         import _rightThumb._base3 as _
#         token_scale = t if t else self.size
#         tokens_minus = int(tm) if tm else self.minus

#         try:
#             messages = [
#                 {"role": "system", "content": "You are a helpful assistant and a senior developer."},
#                 {"role": "user", "content": prompt}
#             ]

#             total_limit = self.model_token_limits.get(self.model, 2048)
#             used_tokens = self.estimate_tokens(messages)

#             if token_scale in ('s', 'small'):
#                 max_tokens = int(total_limit * 0.1)
#             elif token_scale in ('m', 'medium'):
#                 max_tokens = int(total_limit * 0.5)
#             else:
#                 max_tokens = total_limit - used_tokens

#             max_tokens -= tokens_minus
#             max_tokens = max(1, max_tokens)



#             response = self.client.chat.completions.create(
#                 model=self.model,
#                 messages=messages,
#                 temperature=temperature,
#                 top_p=top_p,
#                 frequency_penalty=frequency_penalty,
#                 presence_penalty=presence_penalty,
#                 max_tokens=max_tokens
#             )

#             reply = response.choices[0].message.content
#             self.interactions.append({
#                 'epoch': time.time(),
#                 'prompt': prompt,
#                 'response': reply
#             })

#             if self.log_file:
#                 _.saveTable(self.interactions, self.log_file, p=0)

#             _.pr(reply)
#             return reply

#         except Exception as e:
#             _.pr(f"[ERROR] {e}", c='red')
#             return None











def action():
	tail = '\n\n'
	prompt = ''

	# If there's piped or file/url/etc input
	if _.isData():
		if _.switches.isActive('Query'):
			prompt += 'Answer based on this:' + tail
		prompt += '\n'.join(_.isData()) + tail

	# If a Prompt switch is active, append it
	if _.switches.isActive('Prompt'):
		if _.switches.isActive('Query'):
			prompt += 'The query:' + tail
		Prompt = ' '.join(_.switches.values('Prompt')).strip() + '\n'
		prompt += Prompt





	# Create the chat object
	try:
		if openai.__version__.startswith('0.28'):
			AIChat_Smart = AIChat_028
		else:
			# AIChat_Smart = AIChat_1x
			AIChat_Smart = AIChat_028
		chat = AIChat_Smart(
			api_key=_v.fig['openai'],
			model='gpt-4',
			log_file='ai-bot-interaction.index',
			t=_.switches.value('Tokens'),
			tm=_.switches.value('TokensMinus'),
		)
		response = chat.ask(prompt)
		if response.count('```') == 2:
			response = response.split('```')[1]
			lines = response.split('\n')
			lines.pop(0)
			response = '\n'.join(lines)
		_.pr(response)
	except Exception as e:
		_.pr(e, c='red')
		import platform
		_.pr('An unexpected error occurred', c='red')
		if platform.system() == 'Windows':
			_.pr('pip install openai', c='yellow')
		else:
			_.pr('pip install openai==0.28', c='yellow')













########################################################################################
# pip install openai==0.28
########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)