import os
import platform
import psutil
import json
from _rightThumb._forms import genForm


# Function to get drive information
def get_drive_info():
	def get_drive_serial(drive_letter):
		import subprocess
		import re
		result = subprocess.run(['vol', drive_letter], stdout=subprocess.PIPE, text=True, shell=True)
		match = re.search(r"Volume Serial Number is ([\w-]+)", result.stdout)
		if match:
			return match.group(1)
		else:
			return None

	def get_drive_model(drive_letter):
		import wmi
		c = wmi.WMI()
		logical_disk = c.Win32_LogicalDisk(DeviceID=drive_letter)[0]
		partition = c.query(f"ASSOCIATORS OF {{Win32_LogicalDisk.DeviceID='{drive_letter}'}} WHERE AssocClass=Win32_LogicalDiskToPartition")[0]
		disk_drive = c.query(f"ASSOCIATORS OF {{Win32_DiskPartition.DeviceID='{partition.DeviceID}'}} WHERE AssocClass=Win32_DiskDriveToDiskPartition")[0]
		return disk_drive.Model

	import socket
	import time
	if platform.system() == "Windows":
		import win32api
	cwd = os.getcwd()
	if platform.system() == "Windows":
		drive = os.path.splitdrive(cwd)[0]
	else:
		drive = os.path.realpath(cwd).split('/')[1]
		drive = '/' + drive

	drive_info = psutil.disk_usage(drive)
	capacity = drive_info.total
	used = drive_info.used
	free = drive_info.free
	model = "N/A"
	serial = "N/A"
	if platform.system() == "Windows":
		model = get_drive_model(drive)
		serial = get_drive_serial(drive)
	else:
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
	
	pc_name = socket.gethostname()
	epoch_time = int(time.time())
	info = {
		"model": model,
		"serial": serial,
		"capacity": capacity,
		"used": used,
		"free": free,
		"mount": drive,
		"epoch": epoch_time,
		"pc": pc_name
	}
	return info

if __name__ == "__main__":
	drive_info = get_drive_info()
	form_structure = {
		"Config": {
			"html": True,
			"title": "Drive Registration",
			"description": "Register a Drive",
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Drive Information": [
			{"label": "Model", "type": "text", "value": drive_info.get("model", "")},
			{"label": "Serial", "type": "text", "value": drive_info.get("serial", "")},
			{"label": "Capacity", "type": "text", "value": drive_info.get("capacity", "")},
			{"label": "Used", "type": "text", "value": drive_info.get("used", "")},
			{"label": "Free", "type": "text", "value": drive_info.get("free", "")},
			{"label": "Mount", "type": "text", "value": drive_info.get("mount", "")},
			{"label": "Epoch", "type": "text", "value": drive_info.get("epoch", "")},
			{"label": "PC", "type": "text", "value": drive_info.get("pc", "")}
		],
		"User Input": [
			{"label": "Label", "type": "text", "value": "", "validation": {"required": True}},
			{"label": "Priority", "type": "text", "value": "", "config": {"width": 20}, "validation": {"required": True}},
			{"label": "Owner", "type": "text", "value": "", "validation": {"required": True}},
			{"label": "Notes", "type": "text_area", "value": "", "config": {"width": 60}, "validation": {"required": True}},
			{"label": "Descriptors", "type": "text_area", "value": "", "validation": {"required": True}},
			{"label": "Drive Type", "type": "radio", "options": ["internal", "external", "thumb", "button", "network"], "value": "", "validation": {"required": True}},
		]
	}
	record = genForm(form_structure)
	print(json.dumps(record, indent=4))

