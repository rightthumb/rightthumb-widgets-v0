import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Report', '-r,-report' )
	_.switches.register( 'Drive', '-d,-drive' )
	_.switches.register( 'Drives', '-ds,-drives' )
	_.switches.register( 'Serial', '-ss,-serial' )
	_.switches.register( 'Fields', '-field' )

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'driveUtil.py',
	'description': 'Drive utility',
	'categories': [
						'hd',
						'hard drive',
						'storage',
						'manager',
						'tool',
						'os',
				],
	'examples': [
						_.hp('p driveUtil -r'),
						_.hp('p driveUtil -report'),
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

import subprocess
import json
import platform
import sys
import uuid


def execute_and_return(command):
	try:
		result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  check=True)
		return result.stdout.decode('utf-8')
	except subprocess.CalledProcessError as e:
		return e.stderr

def run_powershell_and_get_json_drive(drive_letter):
	# PowerShell command to get details for a specific logical drive
	ps_command = f"Get-WmiObject Win32_LogicalDisk -Filter \"DeviceID='{drive_letter}:'\" | ConvertTo-Json -Depth 10"

	# Determine PowerShell executable based on the OS
	powershell_executable = "powershell" if platform.system().lower() == "windows" else "pwsh"
	
	# Form the complete command
	command = [powershell_executable, '-Command', ps_command]

	try:
		return json.loads(execute_and_return(command))
	except subprocess.CalledProcessError as e:
		print(f"Error executing PowerShell command: {e.stderr}")
		return None
	except json.JSONDecodeError as e:
		print(f"Error parsing JSON output: {e}")
		return None

def run_powershell_and_get_json():
	# PowerShell command as one line
	ps_command = "Get-WmiObject Win32_DiskDrive | Select-Object * | ConvertTo-Json"
	# ps_command = "Get-WmiObject Win32_DiskDrive | Select-Object * | ConvertTo-Json -Depth 10"

	# Determine PowerShell executable based on the OS
	powershell_executable = "powershell" if platform.system().lower() == "windows" else "pwsh"

	# Form the complete command
	command = [powershell_executable, '-Command', ps_command]

	try:
		# Execute the command
		result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		# Convert the JSON output from PowerShell to a Python dictionary
		return json.loads(result.stdout.decode('utf-8'))
	except subprocess.CalledProcessError as e:
		print(f"Error executing PowerShell command: {e.stderr}")
		return None
	except json.JSONDecodeError as e:
		print(f"Error parsing JSON output: {e}")
		return None

import subprocess
import json

def get_drive_letter_from_serial(serial_number):
	# PowerShell script to get drive letter from serial number
	ps_script = f'''
	$serialNumber = "{serial_number}"
	$diskDrives = Get-WmiObject Win32_DiskDrive
	$targetDrive = $diskDrives | Where-Object {{$_.SerialNumber -match $serialNumber}}
	if ($targetDrive) {{
		$partitions = Get-WmiObject Win32_DiskPartition | Where-Object {{$_.DiskIndex -eq $targetDrive.Index}}
		$logicalDisks = Get-WmiObject Win32_LogicalDiskToPartition
		foreach ($partition in $partitions) {{
			$logicalDisk = $logicalDisks | Where-Object {{$_.Antecedent -match $partition.DeviceID}}
			if ($logicalDisk) {{
				$driveLetter = ($logicalDisk.Dependent -split "=")[1].Trim('"')
				Write-Output $driveLetter
				break
			}}
		}}
	}} else {{
		Write-Output "Not Found"
	}}
	'''

	try:
		# Execute the PowerShell command
		# result = subprocess.run(["powershell", "-Command", ps_script], capture_output=True, text=True, check=True)
		return execute_and_return(["powershell", "-Command", ps_script])
		# Process and return the result
		if result.stdout.strip() == "Not Found":
			print(f"No drive found with serial number: {serial_number}")
			return None
		else:
			return result.stdout.strip()
	except subprocess.CalledProcessError as e:
		print(f"Error executing PowerShell command: {e.stderr}")
		return None

import ctypes
import string

def list_drive_letters_ctypes():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
            # drives.append(letter + ":\\")
        bitmask >>= 1
    return drives

# # Example usage
# drive_letters = list_drive_letters_ctypes()
# print("Available drive letters:", drive_letters)



#n)--> start
def action():
	if _.switches.isActive('Drives'):
		# drive_letters = list_drive_letters_ctypes()
		for drive in list_drive_letters_ctypes():
			try:
				data = run_powershell_and_get_json_drive(drive)
				if data:
					for key in data:
						if 'serial' in key.lower():
							_.pr(drive,data[key])
				# print(drive,data['VolumeSerialNumber'])
			except: pass
		# print(drive_letters)
	if _.switches.isActive('Serial'):
		for serial in _.switches.values('Serial'):
			for drive in list_drive_letters_ctypes():
				try:
					data = run_powershell_and_get_json_drive(drive)
					if serial == data['VolumeSerialNumber']:
						print(drive)
						return None
				except: pass

			# data = get_drive_letter_from_serial(serial)
			return data
	if _.switches.isActive('Drive'):
		# Example usage
		for drive in _.switches.values('Drive'):
			data = run_powershell_and_get_json_drive(drive)
			if _.switches.isActive('Fields'):

				for field in _.switches.values('Fields'):
					_.pr(data[field])

			else:
				_.pv(data)
			# records = run_powershell_and_get_json()
			# print(records)
			# serial_number = get_drive_serial_number(drive)
			# print(serial_number); sys.exit();
			# records = run_powershell_and_get_json()
			# for record in records:
				# print(record)
				# sys.exit()

				# if record['SerialNumber'] == serial_number:
				# 	_.pv(record)

	elif _.switches.isActive('Report'):
		# Example usage
		data = run_powershell_and_get_json()
		_.saveTable(data,'driveUtil.json')
		_.pv(data)
		# if data:
			# print("Drive information:", data)
		# else:
			# print("Failed to retrieve drive information.")
		# data = run_powershell_script_and_parse_json()
		# print(data)
		# _.pv(data)
		#   get_drive_details2()
			# get_drive_details_via_powershell()
			# get_drive_details()
			# list_drives()
			# get_drive_details()
			

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);