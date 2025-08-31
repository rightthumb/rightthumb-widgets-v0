import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Input', '-i' )
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

###########################################




def get_drive_info():


	def get_drive_serial(drive_letter):
		import subprocess
		import re
		# Execute the vol command
		result = subprocess.run(['vol', drive_letter], stdout=subprocess.PIPE, text=True, shell=True)
		
		# Extract the serial number from the output using regex
		match = re.search(r"Volume Serial Number is ([\w-]+)", result.stdout)
		if match:
			return match.group(1)
		else:
			return None

	def get_drive_model(drive_letter):
		import wmi
		c = wmi.WMI()

		# Find the logical disk corresponding to the drive letter
		logical_disk = c.Win32_LogicalDisk(DeviceID=drive_letter)[0]

		# Find the partition associated with this logical disk
		partition = c.query(f"ASSOCIATORS OF {{Win32_LogicalDisk.DeviceID='{drive_letter}'}} WHERE AssocClass=Win32_LogicalDiskToPartition")[0]

		# Find the disk drive associated with this partition
		disk_drive = c.query(f"ASSOCIATORS OF {{Win32_DiskPartition.DeviceID='{partition.DeviceID}'}} WHERE AssocClass=Win32_DiskDriveToDiskPartition")[0]

		return disk_drive.Model


	import os
	import platform
	import psutil
	import time
	import socket
	if platform.system() == "Windows":
		import win32api
	# Get current working directory
	cwd = os.getcwd()

	# Get the drive where the current directory is located
	if platform.system() == "Windows":
		drive = os.path.splitdrive(cwd)[0]
	else:
		drive = os.path.realpath(cwd).split('/')[1]
		drive = '/' + drive

	# Get drive information
	drive_info = psutil.disk_usage(drive)
	capacity = drive_info.total
	used = drive_info.used
	free = drive_info.free

	# Get file system info (model and serial)
	model = "N/A"
	serial = "N/A"

	if platform.system() == "Windows":
		model = get_drive_model(drive)
		serial = get_drive_serial(drive)
	else:
		# print('not windows')
		try:
			result = subprocess.run(['lsblk', '-o', 'NAME,SERIAL,MODEL'], stdout=subprocess.PIPE, text=True)
			output = result.stdout.strip().split('\n')
			for line in output[1:]:
				parts = line.split()
				if drive in parts[0]:
					serial = parts[1]
					model = parts[2] if len(parts) > 2 else "N/A"
					break
		except Exception as e:
			serial = "N/A"
			model = "N/A"
	
	# Get the computer name
	pc_name = socket.gethostname()

	# Get the current epoch time
	epoch_time = int(time.time())
	info = {
		"model": model,
		"serial": serial,
		"capacity": capacity,
		"used": used,
		"free": free,
		"drive_letter_or_mount_info": drive,
		"epoch": epoch_time,
		"pc": pc_name
	}
	print(json.dumps(info, indent=4))
	return info
###########################################
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import platform
import psutil
from datetime import datetime

# def get_drive_info():
#     # Collect drive information
#     drive_info = {}
#     partitions = psutil.disk_partitions()
#     for partition in partitions:
#         if partition.mountpoint == '/':
#             usage = psutil.disk_usage(partition.mountpoint)
#             drive_info['Model'] = "Unknown"  # Model might need to be fetched using system-specific calls
#             drive_info['Serial'] = "Unknown"  # Serial might need to be fetched using system-specific calls
#             drive_info['Capacity'] = usage.total
#             drive_info['Used'] = usage.used
#             drive_info['Free'] = usage.free
#             drive_info['Drive Letter or Mount Info'] = partition.device
#             break

#     drive_info['Epoch'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     drive_info['PC'] = platform.node()

#     return drive_info

def validate_data():
	# Placeholder for validation logic
	if not label_var.get():
		messagebox.showerror("Validation Error", "Label is required")
		return False
	if not priority_var.get():
		messagebox.showerror("Validation Error", "Priority is required")
		return False
	if len(priority_var.get()) != 4:
		messagebox.showerror("Validation Error", "Priority must be 4 characters long")
		return False
	if not owner_var.get():
		messagebox.showerror("Validation Error", "Owner is required")
		return False
	if drive_type_var.get() not in ["internal", "external", "thumb", "button", "network"]:
		messagebox.showerror("Validation Error", "Drive type must be selected")
		return False
	return True

def save_data():
	if not validate_data():
		return
	global drive_info
	global form_data
	form_data.update(drive_info)  # Merge drive info with form data
	form_data['Label'] = label_var.get()
	form_data['Priority'] = priority_var.get()
	form_data['Owner'] = owner_var.get()
	form_data['Notes'] = notes_text.get("1.0", tk.END).strip()
	form_data['Descriptors'] = descriptors_text.get("1.0", tk.END).strip()
	form_data['Drive Type'] = drive_type_var.get()
	
	print(json.dumps(form_data, indent=4))
	root.destroy()  # Close the form after submission

# Initial drive information
drive_info = get_drive_info()

form_data = {}

root = tk.Tk()
root.title("Hard Drive Registration System")
root.geometry("400x600")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), padding=5)
style.configure("TEntry", padding=5)
style.configure("TCombobox", padding=5)
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
style.configure("TRadiobutton", font=("Arial", 12), padding=5)

# Variables
label_var = tk.StringVar()
priority_var = tk.StringVar()
owner_var = tk.StringVar()
notes_text = tk.Text(root, height=5, width=30, wrap="word", font=("Arial", 12))
descriptors_text = tk.Text(root, height=5, width=30, wrap="word", font=("Arial", 12))
drive_type_var = tk.StringVar(value="")

# Layout
ttk.Label(root, text="Drive Registration", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(root, text="Label:").grid(row=1, column=0, sticky=tk.E)
ttk.Entry(root, textvariable=label_var).grid(row=1, column=1, pady=5, padx=10)

ttk.Label(root, text="Priority:").grid(row=2, column=0, sticky=tk.E)
ttk.Entry(root, textvariable=priority_var).grid(row=2, column=1, pady=5, padx=10)

ttk.Label(root, text="Owner:").grid(row=3, column=0, sticky=tk.E)
ttk.Entry(root, textvariable=owner_var).grid(row=3, column=1, pady=5, padx=10)

ttk.Label(root, text="Notes:").grid(row=4, column=0, sticky=tk.NE)
notes_text.grid(row=4, column=1, pady=5, padx=10)

ttk.Label(root, text="Descriptors:").grid(row=5, column=0, sticky=tk.NE)
descriptors_text.grid(row=5, column=1, pady=5, padx=10)

ttk.Label(root, text="Drive Type:").grid(row=6, column=0, sticky=tk.E)
ttk.Radiobutton(root, text="Internal", variable=drive_type_var, value="internal").grid(row=6, column=1, sticky=tk.W)
ttk.Radiobutton(root, text="External", variable=drive_type_var, value="external").grid(row=7, column=1, sticky=tk.W)
ttk.Radiobutton(root, text="Thumb", variable=drive_type_var, value="thumb").grid(row=8, column=1, sticky=tk.W)
ttk.Radiobutton(root, text="Button", variable=drive_type_var, value="button").grid(row=9, column=1, sticky=tk.W)
ttk.Radiobutton(root, text="Network", variable=drive_type_var, value="network").grid(row=10, column=1, sticky=tk.W)

ttk.Button(root, text="Submit", command=save_data).grid(row=11, column=0, columnspan=2, pady=20)

root.mainloop()


def action():
	pass

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);