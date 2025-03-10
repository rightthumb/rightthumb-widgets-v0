#!/usr/bin/python3

# alias mc.server="sudo /opt/minecraft/stuff/simple-minecraft-server-starter.sh"
# alias w.ports="echo 'sudo lsof -i -P -n | grep LISTEN' "
# echo ""
# echo "mc.srv -creative -name scott"
# echo "mc.srv -survival -name scott"
# echo "w.ports"
# echo ""


# simple-minecraft-server-starter.sh

# #!/bin/bash
# /opt/minecraft/stuff/run.py "$@"
# sh /opt/minecraft/stuff/server.sh



import os,sys,subprocess,time
from shutil import copyfile

isBackup=0
isCreative=0
isSurvival=0
theName='A'

folder='/opt/minecraft'
stuff='stuff'
srv='minecraft_server.jar'
server=folder+'/'+stuff+'/'+srv
eula=folder+'/'+stuff+'/'+'/eula.txt'
starter=folder+'/'+stuff+'/'+'/server.sh'
properties=folder+'/'+stuff+'/'+'/properties.txt'
gamemode='this-this-this'

def run(cmd):
	# print(cmd)
	os.system(cmd)
	# result = subprocess.check_output( cmd.split(' ') )
	# print( result )

def process_folder(fo):
	global stuff
	global srv
	if os.path.isdir(fo):
		for item in os.listdir( fo ):
			path=fo+os.sep+item
			if item == srv and not '/'+stuff+'/'+srv in path:
				os.unlink(path)
			elif os.path.isdir(path):
				process_folder(path)

def mod7(path):
	os.chmod( path, 0o777 )

def getText(theFile):
	f = open(theFile, 'r', encoding='utf-8')
	lines = f.readlines()
	f.close()
	return ''.join( lines )

def saveText(rows,theFile):

	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		if type(rows) == str:
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		try:
			open(theFile, 'wb').write(rows)
		except Exception as e:
			try:
				open(theFile, 'w').write(rows)
			except Exception as e:
				new_text = ''
				for x in rows:
					if x in _str.printable:
						new_text+=x
				open(theFile, 'w', encoding='utf-8').write(new_text)


def build_starter(path):
	global server
	global starter
	global srv

	# if os.path.isfile(starter):
	#     os.unlink(starter)

	file_data='#!/bin/bash'
	file_data+='\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='echo "You are AWSOME!!!"\n'
	file_data+='\n'
	file_data+='cd '+ path
	file_data+='\n'
	file_data+='java -Xmx1024M -Xms1024M -jar '+server+' --port 1337 nogui'
	file_data+='\n'
	saveText( file_data, starter )
	mod7(starter)




for i,arg in enumerate(sys.argv):
	if arg == '-backup':
		isBackup=1
	elif arg == '-creative':
		isCreative=1
	elif arg == '-survival':
		isSurvival=1
	elif arg == '-name':
		try:
			theName=sys.argv[i+1]
		except Exception as e:
			pass

# if not isCreative and not isSurvival:
#     isCreative = 1

if isBackup:

	file='#!/usr/bin/expect -f\n'
	file+='spawn scp /opt/minecraft/backup.zip  backup-23BE3AF4E@vps.rightthumb.com:/home/backup-23BE3AF4E/minecraft/backup-'+str(time.time())+'.zip\n'
	file+='expect "assword:"\n'
	file+='send "4ED168D841DB49BB\\n"\n'
	file+='interact\n'


	saveText(file,folder+'/'+stuff+'/auto_backup.exp')


	run('clear')
	time.sleep(1)
	
	run('clear')    
	print('Backing up')
	time.sleep(1)
	run('clear')


	if os.path.isfile( folder+'/backup.zip' ):
		print('Deleting old backup')
		os.unlink(folder+'/backup.zip')

	run('clear')
	print('Zipping files')
	time.sleep(1)

	run('zip -r '+folder+'/backup.zip '+folder+'/java/')

	run('clear')
	print('Copying backup to another server')
	time.sleep(1)

	run(folder+'/'+stuff+'/auto_backup.exp')

	run('clear')
	print('Server backup is complete')
	
	# process_folder( folder+'/java' )



if isCreative or isSurvival:
	print( folder+'/java/'+theName )

	if not os.path.isdir( folder+'/java/'+theName ):
		os.mkdir(folder+'/java/'+theName)


	if not os.path.isfile( folder+'/java/'+theName+'/eula.txt' ):
		copyfile( eula, folder+'/java/'+theName+'/eula.txt' )

	if not os.path.isfile( folder+'/java/'+theName+'/server.properties' ):
		copyfile( properties, folder+'/java/'+theName+'/server.properties' )

	prop = getText( folder+'/java/'+theName+'/server.properties' )

	newFile = []
	for line in prop.split('\n'):
		if not 'gamemode=' in line:
			newFile.append(line)
		elif isSurvival:
			newFile.append('gamemode=survival')
		elif isCreative:
			newFile.append('gamemode=creative')

	saveText( '\n'.join(newFile), folder+'/java/'+theName+'/server.properties' )


	build_starter(folder+'/java/'+theName+'/')


# java -Xmx1024M -Xms1024M -jar minecraft_server.1.18.jar nogui
# java -Xmx1024M -Xms1024M -jar server.jar nogui
