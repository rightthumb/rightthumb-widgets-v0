import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Username', '-u,-user,-username', 'jon' )
	_.switches.register( 'List', '-l,-list' )
	_.switches.register( 'Add', '-a,-add' )
	_.switches.register( 'Change', '-h,-ch,-change' )
	_.switches.register( 'Remove', '-r,-remove' )
	_.switches.register( 'Delete', '-d,-del,-delete' )
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import bcrypt
import os
class HtpasswdManager:

	def __init__(self, htpasswd_path=".htpasswd", htaccess_path=".htaccess"):
		self.htpasswd_path = htpasswd_path
		self.htaccess_path = htaccess_path

	def add_user(self, username, password):
		"""Adds a user with the specified password to the .htpasswd file."""
		hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		entry = f"{username}:{hashed_pw.decode()}\n"
		with open(self.htpasswd_path, "a") as htpasswd_file:
			htpasswd_file.write(entry)
		print(f"Added {username} to {self.htpasswd_path}")
		self._ensure_htaccess_configured()

	def change_password(self, username, new_password):
		"""Changes the password for an existing user in the .htpasswd file."""
		if not os.path.exists(self.htpasswd_path):
			print(".htpasswd file not found.")
			return
		updated = False
		with open(self.htpasswd_path, "r") as htpasswd_file:
			lines = htpasswd_file.readlines()
		with open(self.htpasswd_path, "w") as htpasswd_file:
			for line in lines:
				if line.startswith(f"{username}:"):
					hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
					htpasswd_file.write(f"{username}:{hashed_pw.decode()}\n")
					updated = True
				else:
					htpasswd_file.write(line)
		if updated:
			print(f"Password for {username} updated in {self.htpasswd_path}")
		else:
			print(f"User {username} not found in {self.htpasswd_path}")

	def remove_user(self, username):
		"""Removes a user from the .htpasswd file."""
		if not os.path.exists(self.htpasswd_path):
			print(".htpasswd file not found.")
			return
		with open(self.htpasswd_path, "r") as htpasswd_file:
			lines = htpasswd_file.readlines()
		with open(self.htpasswd_path, "w") as htpasswd_file:
			for line in lines:
				if not line.startswith(f"{username}:"):
					htpasswd_file.write(line)
		print(f"Removed {username} from {self.htpasswd_path}")
		if os.stat(self.htpasswd_path).st_size == 0:
			self._remove_htaccess_config()

	def delete_htpasswd(self):
		"""Deletes the .htpasswd file and removes configuration from .htaccess if needed."""
		if os.path.exists(self.htpasswd_path):
			os.remove(self.htpasswd_path)
			print(f"Deleted {self.htpasswd_path}")
			self._remove_htaccess_config()
		else:
			print(".htpasswd file does not exist.")

	def list_users(self):
		"""Lists all users in the .htpasswd file."""
		if not os.path.exists(self.htpasswd_path):
			print(".htpasswd file not found.")
			return
		with open(self.htpasswd_path, "r") as htpasswd_file:
			lines = htpasswd_file.readlines()
			users = [line.split(':')[0] for line in lines]
			if users:
				print("Users in .htpasswd:")
				for user in users:
					print(user)
			else:
				print("No users found in .htpasswd.")

	def _ensure_htaccess_configured(self):
		"""Ensures the .htaccess file is configured for basic authentication."""
		auth_directives = (
			"AuthType Basic\n"
			"AuthName \"Restricted Area\"\n"
			f"AuthUserFile {os.path.abspath(self.htpasswd_path)}\n"
			"Require valid-user\n"
		)
		if os.path.exists(self.htaccess_path):
			with open(self.htaccess_path, "r") as file:
				if auth_directives in file.read():
					return
		with open(self.htaccess_path, "a") as htaccess_file:
			htaccess_file.write(auth_directives)
		print(f"Updated {self.htaccess_path} with authentication directives.")

	def _remove_htaccess_config(self):
		"""Removes the authentication directives from .htaccess if present."""
		if not os.path.exists(self.htaccess_path):
			return
		with open(self.htaccess_path, "r") as file:
			lines = file.readlines()
		auth_directives = (
			"AuthType Basic\n"
			"AuthName \"Restricted Area\"\n"
			f"AuthUserFile {os.path.abspath(self.htpasswd_path)}\n"
			"Require valid-user\n"
		)
		with open(self.htaccess_path, "w") as file:
			skip_lines = False
			for line in lines:
				if line.strip() == "AuthType Basic" and not skip_lines:
					skip_lines = True
					continue
				if skip_lines and line.strip() == "Require valid-user":
					skip_lines = False
					continue
				if not skip_lines:
					file.write(line)
		print(f"Removed authentication directives from {self.htaccess_path}")

def action():
	manager = HtpasswdManager()
	if not _.switches.isActive('Delete') and not _.switches.isActive('List'):
		username = _.switches.value('Username')
	else:
		username = None
	if _.switches.isActive('Add'):
		import getpass
		password = getpass.getpass("Enter the password: ")
		manager.add_user(username, password)
	elif _.switches.isActive('Change'):
		password = input("Enter the new password: ")
		manager.change_password(username, password)
	elif _.switches.isActive('Remove'):
		manager.remove_user(username)
	elif _.switches.isActive('Delete'):
		manager.delete_htpasswd()
	elif _.switches.isActive('List'):
		manager.list_users()
	else:
		_.e('Switch missing in command','p hspasswd ??')
		print("Invalid action.")
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);