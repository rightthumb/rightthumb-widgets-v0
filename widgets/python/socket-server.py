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

import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Host', '-host' )
	_.switches.register( 'Port', '-port' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'socket-server.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'socket server',
	'categories': [
						'socket',
						'server',
						'online',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	_.defaultScriptTriggers()
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


import base64
import hashlib
def md5(chunk):
	hash_md5 = hashlib.md5()
	hash_md5.update(bytes(chunk, 'utf-8'))
	return hash_md5.hexdigest()


def pad_string( string ):
	INPUT_SIZE = 8
	new_str = string
	pad_chars = INPUT_SIZE - (len(string) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
	return new_str





def formatData( result ):
	result = str(result)
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result




class Socky:
	def __init__( self, host='127.0.0.1', port=65432, client=None, i=0 ):
		# _.pr('__init__')
		self.i = i
		self.socket = client
		self.socket.settimeout(1)
		self.wait_for_instructions()
		self.note=''
	def recvall( self ):
		self.socket.settimeout(1)
		_.pr('recvall')
		# _.pr('def recvall')
		BUFF_SIZE = 4096 # 4 KiB
		data = b''
		while True:
			part = self.socket.recv(BUFF_SIZE)
			data += part
			if len(part) < BUFF_SIZE:
				# either 0 or end of data
				break
		d=str(data,'iso-8859-1')
		# if 'dmp' in d and len(d) < 5:
		#     pass
		# else:
		#     _.pr('r',d)
		_.pr('r',d)
		return d


	def wait_for_instructions( self ):
		# _.pr('def wait_for_instructions')
		# if self.note == 'exit':
		#     _.pr('wex')
		#     return None
		_.pr('w')
		data = self.recvall()
		_.pr('d')
		self.process_for_instructions( data )

	def process_for_instructions( self, data ):
		# _.pr('def process_for_instructions')
		if not len(data):
			_.pr( '0 len' )
			self.wait_for_instructions()
			return None
		# else:
		_.pr('ddata',data)
		if data == 'dmp':
			self.wait_for_instructions()
			return None

		try:
			self.instructions = _tool.vc.HD.process_code(data)
		except Exception as e:
			self.instructions = eval(data)

		if 'isfile' in self.instructions:
			# _.pr('in isfile')
			self.download()
			# return None

		if 'do-upload' in self.instructions:
			# _.pr('in do-upload')
			path = self.instructions
			path = _tool.vc.FIG.path_resolve(path)
			self.upload(path)
			# return None

		if 'hello' in self.instructions:
			_.pr('in hello')
			instructions = { 'hello': self.i }
			self.upload( '/opt/RightThumb/tech/hosts/Vulcan/projects/test.txt' )
			_.pr('end up')
			# self.upload( '/opt/RightThumb/tech/programs/databank/tables/mac-vendors.hash' )
			# self.upload( '/usr/bin/jq' )
			# self.send(j(instructions))
			# self.wait_for_instructions()
			# return None

		if 'kill' in self.instructions:
			self.note = 'exit'
			# _.pr('in kill')
			v.alive = False
			v.listening_agent.thisThread.kill()
			# return None


		if 'exit' in self.instructions or 'kill' in self.instructions:
			self.note = 'exit'
			# v.alive = False
			_.pr( 'close', self.i )
			# _.pr('in exit')
			self.socket.close()
			if not v.threads[str(self.i)].thisThread is None:
				v.threads[str(self.i)].thisThread.kill()
			return None

		if 'python' in self.instructions:
			_.pr( 'python', self.i )
			if _.isWin:
				result = subdo( 'p_.bat '+self.instructions['python'] )
			else:
				result = subdo( 'sh ./p.sh '+self.instructions['python'] )
			_.pr('rresult',result.count('\n'))
			# _.pr('resultt',result)

			self.longText( result )
			_.pr( 'close', self.i )
			# _.pr('in exit')
			self.socket.close()
			if not v.threads[str(self.i)].thisThread is None:
				v.threads[str(self.i)].thisThread.kill()
			return None



		self.wait_for_instructions()


	def download( self ):
		data = self.recvall()
		path = self.instructions['path']
		path = _tool.vc.FIG.path_resolve(path)
		self.downloadBIN(path,data)

	def longText( self, data, chunk=409600 ):
		instructions = {
							'large-text': True,
							'chunk': chunk,

		}
		parts = chunks( data, instructions['chunk'] )
		_.pr( 'parts', len(parts) )
		ins = j(instructions)
		# _.pv(instructions)
		# self.send( j({'buf':len(ins)}) )
		# self.recvall()
		_.pr( 0 )
		self.send( ins )
		_.pr( 1 )
		# return None
		self.recvall()
		_.pr( 2 )
		# self.process_for_instructions( '{"exit":True}' )
		# return None
		# self.send( data )
		# b = info['bytes']
		t = 0
		chunky = instructions['chunk']
		_.pr( 3 )

		for ij, chunkV in enumerate(parts):
			_.pr('chunkV')
			t+=chunky
			_.pr( 44, ij, len(parts) )
			# _.pr(chunkV)
			# _.pr( 440, ij, len(parts) )
			self.send(  str(chunkV)  )
			_.pr( 55, ij, len(parts) )
			# self.recvall()
			_.pr( 66, ij, len(parts) )



		_.pr( 4 )
		_.updateLine('')
		self.send('C257AC605A4A49998885FB72356A1B7F')
		_.pr( 4.1 )
		# self.recvall()
		# self.wait_for_instructions()
		return None

	def upload( self, path ):




		data = self.uploadBIN(path)
		info = _dir.info(path)
		instructions = {
							'isfile': True,
							'buf': len(data),
							'chunk': 4096,
							'path': _tool.vc.FIG.path_secure(path),
							'meta': {
										'ext': info['ext'],
										'name': info['name'],
										'name_': info['name_'],
										'path': info['path'],
										'folder': info['folder'],
										'bytes': info['bytes'],
										'size': info['size'],
										'me': info['me'],
										'ce': info['ce'],
										'created': info['date_created'],
										'modified': info['date_modified'],
										'ago': info['ago'],
							},
		}
		ins = j(instructions)
		# _.pv(instructions)
		self.send( j({'buf':len(ins)}) )
		self.recvall()
		self.send( ins )
		self.recvall()
		# self.send( data )
		b = info['bytes']
		t = 0
		chunky = instructions['chunk']
		with open( path, 'rb' ) as f:
			for chunk in iter(lambda: f.read(chunky), b""):
				t+=chunky
				_.updateLine( str(_.percentageDiffIntAuto( b,t ))+'%' )
				
				self.socket.sendall(  chunk  )
				self.recvall()

		_.updateLine('')
		self.send('<end>')
		self.recvall()

	def send( self, data ):
		# _.pr('send',data)
		d = formatData(data)
		# while len(d) < 1024:
		#   d+='.'
		self.socket.sendall(  d  )

	def uploadBIN( self, path ):
		with open( path, 'rb' ) as up_file:
			encoded_string = base64.b64encode(up_file.read())
			# encoded_string = base64.encode(up_file.read())
		return encoded_string

	def downloadBIN( self, path, data ):
		decoded_string = base64.b64decode(data)
		with open( path, 'w' ) as dl_file:
			dl_file.write(decoded_string);
	
def chunks(s, size):
	myChunks = []
	part = ''
	i = 0
	while not i == len(s)-1:
		part += s[i]
		if len(part) == size:
			myChunks.append( part )
			part = ''
		i +=1
	if len(part):
		myChunks.append( part )
	return myChunks


def j(data):
	return simplejson.dumps(data, indent=4, sort_keys=False)

def asdf():
	_.pr('asdf')
	_.pr('isAlive',v.listening_agent.thisThread.isAlive())
	if v.listening_agent.thisThread.isAlive():
		v.listening_agent.thisThread.kill()
	_.pr('isAlive',v.listening_agent.thisThread.isAlive())

def function():
	_.pr('function')


def newConnection( kwargs ):
	host = kwargs['host']
	port = kwargs['port']
	client = kwargs['client']
	i = kwargs['i']

# def newConnection( host, port, client, i ):
	# _.pr('newCo8nnection',kwargs )
	v.last_sockets = Socky( host, port, client, i )
	# v.last_sockets.open()
	v.sockets[str(i)] = v.last_sockets

# def listener(kwargs):
#   sock = kwargs['socket']
#   i = kwargs['i']
#   client, address = sock.accept()
#   v.listening = False
#   _.pr( "{} connected".format(address) )
#   v.threads[str(i)] = _.Threads( str(i), func=newConnection, arg={'host': host,'port': port,'client':client,'i':i}, addID=False )

def listener(kwargs):
	# sock = kwargs['socket']
	# host = kwargs['host']
	host = kwargs['host']
	port = kwargs['port']

	v.alive = True
	i=0
	while v.alive:
		# _.pr('socket')
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)

		sock.bind((host, port))
		sock.listen()

		
		while v.alive:
			i += 1
			# _.pr('accept',i)
			try:
				try:
					client, address = sock.accept()
				except Exception as e:
					break
				v.listening = False
				_.pr('connected',i)
				# _.pr( "{} connected".format(address) )
				v.threads[str(i)] = _.Threads( str(i), func=newConnection, arg={'host': host,'port': port,'client':client,'i':i}, addID=False )
				
				# v.listening = True
				# v.listers[str(i)] = _.Threads( str(i), func=listener, arg={'socket':sock,'i':i}, addID=False )
				# while v.listening:
				#   pass
				# v.last_thread = _.Threads( str(i), func=newConnection, arg={'host': host,'port': port,'client':client,'i':i}, addID=False )
				# v.last_thread = _.Threads( str(i), func=newConnection, kwargs=(host,port,client,i), addID=False )
				# v.last_thread = _.Threads( str(i), func=function, addID=False )
				
				# v.threads[str(i)].open()
				# _.threads.add( 'sessions', newConnection, [{'host': host,'port': port,'client':client,'i':i}], kwargs=True )
				
				# break
			finally:
				pass

			# if not v.alive:
			#   try:
			#       sock.shutdown(socket.SHUT_RDWR)
			#   except Exception as e:
			#       pass
			#   try:
			#       sock.close()
			#   except Exception as e:
			#       pass
			#   _.pr('sleep')
			#   while logoutComplete == 0:
			#       time.sleep(.5)
			#   time.sleep(5)
			#   _.pr('killAll')
			#   # _.threads.killAll()
			#   while not logoutComplete == 2:
			#       time.sleep(.5)
			#   time.sleep(8)
			#   _.pr('end')
			#   sys.exit()
			#   raise



def action():
	if _.isWin:
		os.chdir( __.pathList( _v.techFolder, 'tech/programs/servers/socket/smb' ).replace( 'tech\\tech', 'tech' ) )
	else:
		os.chdir( __.pathList( _v.techFolder, 'tech/programs/servers/socket/linux' ) )
	global killswitch
	global alive

	global logoutComplete



	# _.threads.autoLoaded = False
	# _.threads.maxThreadsSafe = 250
	# _.threads.report = False
	# _.threads.auditPrint = False
	# _.threads.register( 'sessions', logout )



	host = 'localhost'
	port = 65432
	if _.switches.isActive('Host'):
		host = _.switches.values('Host')[0]
	if _.switches.isActive('Port'):
		port = int(_.switches.values('Port')[0])


	v.listening_agent = _.Threads( 'agent', func=listener, arg={'host': host,'port': port}, addID=False, timeout=120 )
	
	


	

def logout():
	global logoutComplete
	logoutComplete = 2
	_.pr( 'Logout' )


import socket

v = _.dot()
v.i = 0
v.sockets = {}
v.threads = {}
v.listers = {}
v.subprocess = None
_tool = _.import_path( '?tool' )
try:
	_tool.loader()
except Exception as e:
	_.e( 'tool error' )

def subdo(do,p=0):
	if p:
		_.pr(do)
	if v.subprocess is None:
		import subprocess
		v.subprocess = subprocess
	try:
		result = str(v.subprocess.check_output(do.split(' ')),'iso-8859-1')
	except Exception as e:
		result = ''
	if p > 1:
		_.pr(result)
	return result




logoutComplete = 0
killswitch = False
alive = True

import _rightThumb._dir as _dir
import simplejson
# from threading import Timer


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







