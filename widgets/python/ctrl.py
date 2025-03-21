import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
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
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

# import time

# _.ctrl = _.dot()
# _.ctrl.iter = 0
# _.ctrl.testing = False
# _.ctrl.tap = time.time()
# _.ctrl.double = time.time()


# import ctypes

# # def is_capslock_on():
# #     return ctypes.windll.user32.GetKeyState(0x14) & 1

# def sleep_ms(milliseconds):
#     return milliseconds * 1000

# tt=sleep_ms

# def hh(milliseconds):
#     return milliseconds * 100

# def ms2sec(milliseconds):
#     return milliseconds / 1000

# ht=ms2sec


# import threading
# import keyboard

# # Global variable to track the last Caps Lock activation time
# last_caps_activation = 0

# # Function to check if Caps Lock is currently on
# def is_caps_lock_on():
#     return ctypes.windll.user32.GetKeyState(0x14) & 1
#     return keyboard.is_pressed("caps lock")

# # Function to ensure Caps Lock and Ctrl are released after a delay
# def cleanup_caps_lock_and_ctrl():
#     global last_caps_activation

#     time.sleep(1.5)  # Wait before executing cleanup

#     # If Caps Lock has been held again, exit early
#     if (time.time() - last_caps_activation) < 1.8:
#         return  # Exit cleanup thread if Caps Lock was held again

#     # Ensure Caps Lock is off
#     if is_caps_lock_on():
#         capLockPresser()

#     # Ensure Ctrl is released to fix any sticky key issue
#     if keyboard.is_pressed("ctrl"):
#         keyboard.release("ctrl")

# check = time.time()

# def capLockPresser():
#      if is_caps_lock_on():
#         _.pr('pressing caps lock',c='cyan')
#         keyboard.press_and_release("caps lock")



# def clickOnce(iter):
#     _.pr('waiting 100 ms',c='cyan')
#     # time.sleep(0.8)
#     time.sleep(ms2sec(100))
#     if isDoubleTapActive(): return
#     if _.ctrl.start and iter == _.ctrl.iter:
#         _.pr('activated',c='red')
#         keyboard.press("ctrl")
#     else:
#         _.pr('cancelled',c='cyan')

# # def testing():

# def isDoubleTapActive():
#     diff = time.time() - _.ctrl.double
#     x = tt(diff)
#     # _.pr(diff,x,c='Background.light_blue')
#     if diff < 2:
#         _.pr('isDoubleTapActive',c='red')
#         return True
#     return False

# def doubleTapCheck():
#     diff = time.time() - _.ctrl.tap
#     # x = tt(diff)
#     # _.pr(diff,x,c='Background.light_blue')
#     if diff < 1:
#         _.ctrl.double = time.time()
#         _.pr('double tap',c='Background.red')
#     _.ctrl.tap = time.time()


# # Function to monitor Caps Lock hold duration and act as Ctrl
# def monitor_caps_lock(hold_time_ms=800, max_hold_time_ms=2500):
#     global check
#     global last_caps_activation

#     if is_caps_lock_on():
#         capLockPresser()

#     last_press_time = 0  # Track last press time for double-tap detection
#     while True:
#         if ((time.time() - check) * 1000) > 1000:
#             if is_caps_lock_on():
#                 capLockPresser()

#         keyboard.wait("caps lock")  # Wait for Caps Lock press

#         if _.ctrl.testing:
#             test = time.time()
#             while keyboard.is_pressed("caps lock"):
#                 pass
#             diff = time.time()-test
#             print('test', diff, sleep_ms(diff))





#         _.pr(line=1,c='yellow')
#         press_time = time.time()

#         # Detect if it was a quick double tap (toggle Caps Lock normally)
#         if press_time - last_press_time < 0.3:
#             continue  # Allow normal Caps Lock toggle on quick double-tap

#         last_press_time = press_time
#         last_caps_activation = time.time()  # Update activation time
#         first = True
#         activated=False
#         start_time = time.time()
#         _.ctrl.iter += 1
		
#         start_time = time.time()
#         _.ctrl.start = time.time()
#         doubleTapCheck()
#         if isDoubleTapActive(): continue
		
#         while keyboard.is_pressed("caps lock"):
#             if isDoubleTapActive(): break
#             _.ctrl.last = time.time()
#             if first:
#                 first = False
#                 _.pr('pressed',c='green')
#                 elapsed_time = (time.time() - start_time) * 1000
#             # _.pr(elapsed_time,hold_time_ms,end='')
#             # if not activated:
#             if not activated:
#                 activated=True
#                 clickOnce(_.ctrl.iter)
#             # if elapsed_time >= hold_time_ms:
				

#             if elapsed_time >= max_hold_time_ms:
#                 break  # Prevent getting stuck

#             # time.sleep(0.05)  # Reduce CPU usage
#         activated=False
#         _.ctrl.start = 0
#         keyboard.release("ctrl")  # Release Ctrl when Caps Lock is released
#         _.pr('released',c='yellow')
	   
#         capLockPresser()

#         # Ensure Caps Lock is off after releasing it
#         if is_caps_lock_on():
#             capLockPresser()

#         # Start a cleanup thread to check after 1.8 seconds
#         threading.Thread(target=cleanup_caps_lock_and_ctrl, daemon=True).start()



# # Start the main Caps Lock monitoring loop
# monitor_caps_lock()



import time
import ctypes
import threading
import keyboard # type: ignore
import sys

class CapsLockMonitor:
	def __init__(self):
		# _ = _  # Store framework reference
		self.ctrl = self.Dot()
		self.ctrl.iter = 0
		self.ctrl.testing = False
		self.ctrl.tap = time.time()
		self.ctrl.double = time.time()
		self.last_caps_activation = 0  # Track the last Caps Lock activation time
		self.shutdown_flag = False  # Global flag to stop all threads
		self.check = time.time()
		self.count = 0
		self.threads = []

	class Dot:
		pass

	def sleep_ms(self, milliseconds):
		return milliseconds * 1000

	def ms2sec(self, milliseconds):
		return milliseconds / 1000

	def is_caps_lock_on(self):
		return ctypes.windll.user32.GetKeyState(0x14) & 1

	def cleanup_caps_lock_and_ctrl(self):
		time.sleep(1.5)  # Wait before executing cleanup

		if (time.time() - self.last_caps_activation) < 1.8:
			return  # Exit cleanup thread if Caps Lock was held again

		if self.is_caps_lock_on():
			self.cap_lock_presser()

		if keyboard.is_pressed("ctrl"):
			keyboard.release("ctrl")

	def cap_lock_presser(self):
		if self.is_caps_lock_on():
			_.pr("Pressing Caps Lock (to reset state)", c="cyan")
			keyboard.press_and_release("caps lock")
			self.start()

	def click_once(self, iter):
		_.pr("Waiting 100ms", c="cyan")
		time.sleep(self.ms2sec(100))
		if self.is_double_tap_active():
			return
		if self.ctrl.start and iter == self.ctrl.iter:
			_.pr("Activated (Ctrl Press)", c="red")
			keyboard.press("ctrl")
		else:
			_.pr("Cancelled", c="cyan")

	def is_double_tap_active(self):
		diff = time.time() - self.ctrl.double
		if diff < 2:
			_.pr("Double Tap Active", c="red")
			return True
		return False

	def double_tap_check(self):
		diff = time.time() - self.ctrl.tap
		if diff < 1:
			self.ctrl.double = time.time()
			_.pr("Double Tap Detected", c="Background.red")
		self.ctrl.tap = time.time()

	def emergency_shutdown(self,force=False):
		"""Monitor for Caps Lock + Space combination to exit the app"""
		# return None
		if force:
			_.pr("\nEmergency Kill Triggered! Stopping all threads and exiting...", c="red")
			self.shutdown_flag = True
			sys.exit(0)
		while not self.shutdown_flag:
			if keyboard.is_pressed("caps lock") and keyboard.is_pressed("space"):
				_.pr("\nEmergency Kill Triggered! Stopping all threads and exiting...", c="red")
				self.shutdown_flag = True
				sys.exit(0)  # Exit the entire program immediately

	def monitor_caps_lock(self, hold_time_ms=800, max_hold_time_ms=250000):
		if self.is_caps_lock_on():
			self.cap_lock_presser()

		last_press_time = 0  # Track last press time for double-tap detection
		while not self.shutdown_flag:
			keyboard.wait("caps lock")  # Wait for Caps Lock press
			self.count += 1
			if self.count > 10:
				self.emergency_shutdown(True)
				self.count = 0
				return None
			press_time = time.time()

			_.pr(line=1, c="yellow")  # Print line marker

			if press_time - last_press_time < 0.3:
				continue  # Allow normal Caps Lock toggle on quick double-tap

			last_press_time = press_time
			self.last_caps_activation = time.time()
			first = True
			activated = False
			self.ctrl.iter += 1
			self.ctrl.start = time.time()
			self.double_tap_check()
			if self.is_double_tap_active():
				continue

			while keyboard.is_pressed("caps lock"):
				if self.is_double_tap_active():
					break
				self.ctrl.last = time.time()
				if first:
					first = False
					_.pr("Caps Lock Pressed", c="green")
				elapsed_time = (time.time() - press_time) * 1000
				if not activated:
					activated = True
					self.click_once(self.ctrl.iter)

				if elapsed_time >= max_hold_time_ms:
					break

			activated = False
			self.ctrl.start = 0
			keyboard.release("ctrl")  # Release Ctrl when Caps Lock is released
			_.pr("Caps Lock Released", c="yellow")

			self.cap_lock_presser()

			if self.is_caps_lock_on():
				self.cap_lock_presser()

			threading.Thread(target=self.cleanup_caps_lock_and_ctrl, daemon=True).start()

	def start(self, threshold=0):
		"""Start the Caps Lock monitoring and emergency shutdown threads"""
		print("Starting / Re-starting Caps Lock Monitor...")
		if threshold > 0:
			print(f"Threshold: {threshold}")
		shutdown_thread = threading.Thread(target=self.emergency_shutdown, daemon=True)
		shutdown_thread.start()

		self.monitor_caps_lock()


# Run the application
if __name__ == "__main__":
	app = CapsLockMonitor()
	app.start()





def action():
	pass
	# monitor_shift(500)
	 

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)