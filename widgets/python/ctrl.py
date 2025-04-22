import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
	_.switches.register( 'Silent', '--c,--s,-silent' )
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
#     return _.Pressed.key("caps lock")

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
#     if _.Pressed.key("ctrl"):
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














__.monitor = False
__.keyListener = True
# __.monitor.shutdown_flag = True
import ctypes
import time

def test(what):
	_.pr('pressed',what,c='green')

# _.KeyMon.app


















if False:

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

			if _.Pressed.key("ctrl"):
				keyboard.release("ctrl")

		def cap_lock_presser(self):
			if self.is_caps_lock_on():
				_.pr("Pressing Caps Lock (to reset state)", c="cyan")
				keyboard.press_and_release("caps lock")
				# self.start()

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
			if not __.monitor == False:
				__.monitor.shutdown_flag = True
			"""Monitor for Caps Lock + Space combination to exit the app"""
			# return None
			if force:
				_.pr("\nEmergency Kill Triggered! Stopping all threads and exiting...", c="red")
				self.shutdown_flag = True
				sys.exit(0)
			while not self.shutdown_flag:
				if _.Pressed.key("caps lock") and _.Pressed.key("space"):
					_.pr("\nEmergency Kill Triggered! Stopping all threads and exiting...", c="red")
					self.shutdown_flag = True
					sys.exit(0)  # Exit the entire program immediately

		def handle_caps_lock_press(self, hold_time_ms=800, max_hold_time_ms=250000):
				keyboard.wait("caps lock")  # Wait for Caps Lock press
				self.count += 1
				if self.count > 10:
					# self.emergency_shutdown(True)
					self.count = 0
					return False
				press_time = time.time()

				_.pr(line=1, c="yellow")  # Print line marker

				# if press_time - self.last_press_time < 0.3:
				# 	return True

				self.last_press_time = press_time
				self.last_caps_activation = time.time()
				first = True
				activated = False
				self.ctrl.iter += 1
				self.ctrl.start = time.time()
				self.double_tap_check()
				if self.is_double_tap_active():
					return True

				while keyboard.is_pressed("caps lock"):
					if self.is_double_tap_active():
						return False
					self.ctrl.last = time.time()
					if first:
						first = False
						_.pr("Caps Lock Pressed", c="green")
					elapsed_time = (time.time() - press_time) * 1000
					if not activated:
						activated = True
						self.click_once(self.ctrl.iter)

					if elapsed_time >= max_hold_time_ms:
						_.pr("Caps Lock Hold Time Exceeded", c="red")
						return False

				activated = False
				self.ctrl.start = 0
				keyboard.release("ctrl")  # Release Ctrl when Caps Lock is released
				_.pr("Caps Lock Released", c="yellow")

				self.cap_lock_presser()

				if self.is_caps_lock_on():
					self.cap_lock_presser()

				threading.Thread(target=self.cleanup_caps_lock_and_ctrl, daemon=True).start()
		def monitor_caps_lock(self, hold_time_ms=800, max_hold_time_ms=250000):
			if self.is_caps_lock_on():
				self.cap_lock_presser()

			self.last_press_time = 0  # Track last press time for double-tap detection
			while not self.shutdown_flag:
				if _.Pressed.key("caps lock"):
					if not self.handle_caps_lock_press(hold_time_ms, max_hold_time_ms):
						break
				time.sleep(0.1)


		def start(self, threshold=0):
			"""Start the Caps Lock monitoring and emergency shutdown threads"""
			print("Starting / Re-starting Caps Lock Monitor...")
			if threshold > 0:
				print(f"Threshold: {threshold}")
			shutdown_thread = threading.Thread(target=self.emergency_shutdown, daemon=True)
			shutdown_thread.start()

			self.monitor_caps_lock()


	# if True:
	# 	__.monitor = _.KeyMon.app()
	# 	__.monitor.start()
		# __.monitor.shutdown_flag = True


	# Run the application
	if __name__ == "__main__":
		app = CapsLockMonitor()
		app.start()


if False:

	import threading
	from pynput import keyboard as kb # type: ignore
	import keyboard # type: ignore
	import signal
	import sys
	import ctypes

	# if True:
	# 	__.monitor = _.KeyMon.app()
	# 	__.monitor.start()
		# __.monitor.shutdown_flag = True


	ctrl_pressed = False
	caps_pressed = False
	controller = kb.Controller()
	__.keyListener = True

	def is_caps_lock_on():
		return ctypes.windll.user32.GetKeyState(0x14) & 1

	def status(var,location='generic'):
		if not var == None:
			__.keyListener = var
			_.pr(f"Listener Change: {var} ({location})",c='cyan')
		else:
			_.pr(f"Listener Status: {__.keyListener} ({location})",c='cyan')
		



	# Disable caps lock if it starts enabled
	def caps_lock_off():
		if is_caps_lock_on():
			status(False,'caps_lock_off')
			controller.press(kb.Key.caps_lock)
			controller.release(kb.Key.caps_lock)
			status(True,'caps_lock_off')

	caps_lock_off()

	def on_press(key):
		if _.Pressed.key("caps lock"):
			status(None,'on_press')
		
		if key == kb.Key.esc:
			print("Escape pressed. Exiting...")
			stop()
		
		if __.keyListener: return
		global ctrl_pressed, caps_pressed
		if True:
			if _.Pressed.key("caps lock"):
				status(False,'on_press')
				while keyboard.is_pressed("caps lock"):
					keyboard.press("ctrl")
				keyboard.release("ctrl")
				status(True,'on_press')

		if False:
			try:
				if key == kb.Key.caps_lock and not ctrl_pressed:
					controller.press(kb.Key.ctrl_r)
					ctrl_pressed = True
					caps_pressed = True
				elif key == kb.Key.esc:
					print("Escape pressed. Exiting...")
					stop()
			except Exception as e:
				print(f"Error: {e}")

	def on_release(key):
		if True:
			if __.keyListener: return
		global ctrl_pressed, caps_pressed
		try:
			if key == kb.Key.caps_lock and ctrl_pressed:
				controller.release(kb.Key.ctrl_r)
				ctrl_pressed = False
				# If Caps Lock was not already on before press, toggle it off
				if not caps_pressed and is_caps_lock_on():
					status(False,'on_release')
					controller.press(kb.Key.caps_lock)
					controller.release(kb.Key.caps_lock)
					status(True,'on_release')
					caps_lock_off()
				caps_pressed = False
		except Exception as e:
			print(f"Error: {e}")

	def stop():
		global caps_watcher_running
		caps_watcher_running = False
		keyboard.release("ctrl")
		listener.stop()
		sys.exit(0)

	def stop():
		try:
			if ctrl_pressed:
				controller.release(kb.Key.ctrl_r)
		except:
			pass
		listener.stop()
		sys.exit(0)

	def signal_handler(sig, frame):
		print("\nCtrl+C detected. Exiting...")
		stop()

	signal.signal(signal.SIGINT, signal_handler)

	with kb.Listener(on_press=on_press, on_release=on_release) as listener:
		print("Running... Hold Caps Lock = Right Ctrl. Press Esc or Ctrl+C to exit.")
		listener.join()


if False:
	import threading
	from pynput import keyboard as kb  # type: ignore
	import keyboard  # type: ignore
	import signal
	import sys
	import time


	# if True:
	# 	__.monitor = _.KeyMon.app()
	# 	__.monitor.start()
		# __.monitor.shutdown_flag = True


	caps_pressed = False
	ctrl_pressed = False
	controller = kb.Controller()
	caps_watcher_running = True

	def watch_caps():
		global caps_pressed
		global caps_watcher_running
		once = False
		while caps_watcher_running:
			if not once:
				if _.Pressed.key("ctrl"):
					keyboard.release("ctrl")
					# _.pr('ctrl released, double check',c='Background.red')
					
			if _.Pressed.key("caps lock"):
				if not once:
					if not caps_pressed:
						once = True
						keyboard.press("ctrl")
						caps_pressed = True
						_.pr('ctr pressed',c='Background.green')
			else:
				if caps_pressed:
					keyboard.release("ctrl")
					caps_pressed = False
					keyboard.press("caps lock")
					keyboard.release("caps lock")
					once = False
					_.pr('ctrl released',c='Background.yellow')
			time.sleep(0.01)


	def on_press(key):
		if key == kb.Key.esc:
			duration = time.time()
			while keyboard.is_pressed("esc"):
				pass
				time.sleep(0.1)
			if time.time() - duration < 0.5:
				_.Notify()
				_.pr('Escape pressed. Exiting...',c='Background.red')
				stop()

	def on_release(key):
		pass  # No need for logic here

	def stop():
		global caps_watcher_running
		caps_watcher_running = False
		if _.Pressed.key("caps lock"):
			keyboard.release("caps lock")
		if _.Pressed.key("ctrl"):
			keyboard.release("ctrl")
		listener.stop()
		sys.exit(0)

	def signal_handler(sig, frame):
		print("\nCtrl+C detected. Exiting...")
		stop()

	signal.signal(signal.SIGINT, signal_handler)

	# Start Caps Lock monitoring thread
	threading.Thread(target=watch_caps, daemon=True).start()

	# Start key listener
	with kb.Listener(on_press=on_press, on_release=on_release) as listener:
		_.pr("Running... \nPress Esc to exit.",c='yellow')
		listener.join()

if True:
	import time
	import threading
	import signal
	import sys
	import ctypes
	from pynput import keyboard as kb
	import keyboard  # type: ignore

	import platform
	import subprocess
	import shutil

	class CapsCtrlWatcher:
		def __init__(self):
			self.caps_pressed = False
			self.ctrl_pressed = False
			self.controller = kb.Controller()
			self.caps_watcher_running = True
			self.esc_pressed_time = None
			self.listener = None
			self.active = []
			self.cops_lock_off()

		def watch_caps(self):
			once = False
			while self.caps_watcher_running:
				if not once:
					if _.Pressed.key("ctrl"):
						keyboard.release("ctrl")
						# _.pr('ctrl released, double check', c='Background.red')

				if _.Pressed.key("caps lock"):
					if not once:
						if not self.caps_pressed:
							once = True
							keyboard.press("ctrl")
							self.caps_pressed = True
							# _.pr('ctrl pressed', c='Background.green')
				else:
					if self.caps_pressed:
						keyboard.release("ctrl")
						self.cops_lock_off()
						self.num_lock_on()
						self.caps_pressed = False
						once = False
						# _.pr('ctrl released', c='Background.yellow')
				time.sleep(0.01)
		def cops_lock_off(self):
			if self.is_caps_lock_on():
				keyboard.press("caps lock")
				keyboard.release("caps lock")
		# def is_caps_lock_on(self):
		# 	return ctypes.windll.user32.GetKeyState(0x14) & 1

		# def is_num_lock_on(self):
		# 	return ctypes.windll.user32.GetKeyState(0x90) & 1



		def is_caps_lock_on(self):
			system = platform.system()
			if system == 'Windows':
				return ctypes.windll.user32.GetKeyState(0x14) & 1

			elif system == 'Linux':
				if not shutil.which('xset'):
					print("❌ 'xset' is not installed. Run: sudo apt install x11-xserver-utils")
					return None

				try:
					output = subprocess.check_output(['xset', 'q']).decode()
					for line in output.splitlines():
						if 'Caps Lock:' in line:
							return 'on' in line.lower()
				except Exception as e:
					print(f"⚠️  Error checking Caps Lock: {e}")
					return None

			else:
				print(f"❌ Caps Lock detection not supported on: {system}")
				return None

		def is_num_lock_on(self):
			system = platform.system()
			if system == 'Windows':
				return ctypes.windll.user32.GetKeyState(0x90) & 1

			elif system == 'Linux':
				if not shutil.which('xset'):
					print("❌ 'xset' is not installed. Run: sudo apt install x11-xserver-utils")
					return None

				try:
					output = subprocess.check_output(['xset', 'q']).decode()
					for line in output.splitlines():
						if 'Num Lock:' in line:
							return 'on' in line.lower()
				except Exception as e:
					print(f"⚠️  Error checking Num Lock: {e}")
					return None

			else:
				print(f"❌ Num Lock detection not supported on: {system}")
				return None


		def num_lock_on(self):
			if not self.is_num_lock_on():
				keyboard.press("num lock")
				keyboard.release("num lock")

		def on_press(self, key):


			try:
				if hasattr(key, 'char') and key.char is not None:
					KEY = key.char.lower()  # e.g. 'a', 'b', '1'
				else:
					KEY = str(key).replace('Key.', '').lower()  # e.g. 'esc', 'ctrl_l'
			except:
				KEY = str(key).replace('Key.', '').lower()  # e.g. 'esc', 'ctrl_l'

			
			if key == kb.Key.esc and not KEY in self.active:
				self.esc_pressed_time = time.time()
				# print('esc')


			if not KEY in self.active:
				self.active.append(KEY)

		def on_release(self, key):

			try:
				if hasattr(key, 'char') and key.char is not None:
					KEY = key.char.lower()  # e.g. 'a', 'b', '1'
				else:
					KEY = str(key).replace('Key.', '').lower()  # e.g. 'esc', 'ctrl_l'
			except:
				KEY = str(key).replace('Key.', '').lower()  # e.g. 'esc', 'ctrl_l'


			if KEY in self.active:
				self.active.remove(KEY)
			for k in self.active:
				if not _.Pressed.key(k):
					self.active.remove(k)
			
			if key == kb.Key.esc and self.esc_pressed_time:
				duration = time.time() - self.esc_pressed_time
				# _.pr('esc Duration:', duration)
				if duration > 0.5:
					if not _.switches.isActive('Silent'):
						_.Notify('Escape pressed. Exiting...', c='Background.red')
					self.stop()

		def stop(self):
			self.caps_watcher_running = False
			if _.Pressed.key("caps lock"):
				keyboard.release("caps lock")
			if _.Pressed.key("ctrl"):
				keyboard.release("ctrl")
			if self.listener:
				self.listener.stop()
			sys.exit(0)

		def signal_handler(self, sig, frame):
			print("\nCtrl+C detected. Exiting...")
			self.stop()

		def run(self):
			signal.signal(signal.SIGINT, self.signal_handler)
			threading.Thread(target=self.watch_caps, daemon=True).start()
			with kb.Listener(on_press=self.on_press, on_release=self.on_release) as self.listener:
				_.pr("Running... \nPress Esc to exit.", c='yellow')
				self.listener.join()

	watcher = CapsCtrlWatcher()
	watcher.run()


def action():
	pass
	# monitor_shift(500)
	 

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)