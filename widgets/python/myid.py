#!/usr/bin/python3

# cat /etc/machine-id
# blkid -o value -s UUID
# lsblk -dno SERIAL

# wmic useraccount where name="Administrator" get sid
# reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography /v MachineGuid
# wmic bios get serialnumber
# wmic os get SerialNumber
# vol C:
# getmac

class SystemIdentifier:
	def __init__(self):
		try: import platform
		except: pass
		self.os_type = platform.system()
		self.ids = {}
	def md5_hash(self, string):
		try: import hashlib
		except: pass
		hash = hashlib.md5(string.encode()).hexdigest()
		# Format as UUID-like string: 8-4-4-4-12 characters
		return f"{hash[:8]}-{hash[8:12]}-{hash[12:16]}-{hash[16:20]}-{hash[20:]}"
	def execute_command(self, command):
		try: import subprocess
		except: pass
		try:
			result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
			return result.strip()
		except subprocess.CalledProcessError as e:
			return f"Error: {e.output}"
	def get_linux_ids(self):
		try: import os
		except: pass
		ids = {
			'user': os.environ['USER'],
			'hostname': self.execute_command('cat /etc/hostname'),
			'machine-id': self.execute_command('cat /etc/machine-id'),
			'filesystem-uuid': self.execute_command('blkid -o value -s UUID'),
			'disk-serial': self.execute_command('lsblk -dno SERIAL')
		}
		return ids
	def get_windows_ids(self):
		try: import os
		except: pass
		ids = {
			'user': os.environ['USERNAME'],
			'hostname': os.environ['COMPUTERNAME'],
			'windows-sid': self.execute_command('wmic useraccount where name="Administrator" get sid'),
			'bios-serial': self.execute_command('wmic bios get serialnumber'),
			'windows-product-id': self.execute_command('wmic os get "SerialNumber"'),
			'machine-guid': self.execute_command('reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography /v MachineGuid'),
			'disk-volume-serial': self.execute_command('vol C:'),
			# 'mac-address': self.execute_command('getmac')
		}
		return ids
	def generate_machine_id(self):
		try: import uuid
		except: pass
		if self.os_type == "Linux":
			self.ids = self.get_linux_ids()
		elif self.os_type == "Windows":
			self.ids = self.get_windows_ids()
		self.ids['uuid-getnode'] = str(uuid.UUID(int=uuid.getnode()))
		return self.md5_hash(str(self.ids))
def gen():
	system_identifier = SystemIdentifier()
	machine_id = system_identifier.generate_machine_id()
	return machine_id

if __name__ == '__main__':
	print(gen())