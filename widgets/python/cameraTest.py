import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register('SaveImage', '-save')
	_.switches.register('CameraInfo', '-info')
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

import cv2
import tkinter as tk
from tkinter import messagebox

def capture_and_save_image_opencv(filename='camera_test.jpg'):
	# Initialize the video capture object with the default camera
	cap = cv2.VideoCapture(0)

	# Check if the camera was successfully opened
	if not cap.isOpened():
		print("Error: Unable to access the camera")
		cap.release()
		return False

	# Capture a single frame
	ret, frame = cap.read()

	# Check if the frame was captured successfully
	if ret:
		# Save the captured image to a file
		cv2.imwrite(filename, frame)
		print(f"Image saved as {filename}")
	else:
		print("Error: Unable to capture an image")

	# Release the video capture object
	cap.release()
	return ret




def get_camera_info(camera_index=0):
	cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
	if not cap.isOpened():
		messagebox.showerror("Error", "Camera could not be opened!")
		return {}
	properties = {
		"Frame Width": cap.get(cv2.CAP_PROP_FRAME_WIDTH),
		"Frame Height": cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
		"FPS": cap.get(cv2.CAP_PROP_FPS),
		"Brightness": cap.get(cv2.CAP_PROP_BRIGHTNESS),
		"Contrast": cap.get(cv2.CAP_PROP_CONTRAST),
		"Saturation": cap.get(cv2.CAP_PROP_SATURATION),
		"Hue": cap.get(cv2.CAP_PROP_HUE),
		"Gain": cap.get(cv2.CAP_PROP_GAIN),
		"Exposure": cap.get(cv2.CAP_PROP_EXPOSURE),
		"White Balance": cap.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)
	}
	cap.release()
	return properties

def display_info():
	info = get_camera_info()
	info_text = "\n".join(f"{key}: {value}" for key, value in info.items())
	messagebox.showinfo("Camera Information", info_text)

def action():
	if _.switches.isActive('SaveImage'):
		capture_and_save_image_opencv('camera_test.jpg')
	if _.switches.isActive('CameraInfo'):
		root = tk.Tk()
		root.title("Camera Information App")
		btn_get_info = tk.Button(root, text="Get Camera Info", command=display_info)
		btn_get_info.pack(pady=20)
		root.mainloop()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);