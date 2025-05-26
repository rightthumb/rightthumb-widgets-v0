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

def action(): pass

# class SoundDingNotifier:
#     import os
#     import sys
#     import time
#     import platform
#     import numpy as np
#     import sounddevice as sd

#     def __init__(self, threshold=0.02, cooldown=0.75, interval=0.05, on_ding=None, device=None, debug=False):
#         self.THRESHOLD = threshold
#         self.COOLDOWN = cooldown
#         self.INTERVAL = interval
#         self.on_ding = on_ding
#         self.device = device or self._auto_detect_input_device()
#         self.debug = debug

#         self.system = self.platform.system()
#         self.ding_count = 0
#         self.last_ding_time = 0
#         self.original_title = self._get_current_title()

#     def _set_title(self, title):
#         if self.system == "Windows":
#             self.os.system(f"title {title}")
#         else:
#             self.sys.stdout.write(f"\33]0;{title}\a")
#             self.sys.stdout.flush()

#     def _get_title_windows(self):
#         try:
#             import ctypes
#             buffer = ctypes.create_unicode_buffer(1024)
#             ctypes.windll.kernel32.GetConsoleTitleW(buffer, 1024)
#             return buffer.value
#         except Exception:
#             return "Terminal"

#     def _get_title_linux(self):
#         try:
#             import subprocess
#             output = subprocess.check_output(
#                 ['xprop', '-id', self.os.environ['WINDOWID'], 'WM_NAME'],
#                 stderr=self.subprocess.DEVNULL
#             )
#             return output.decode().split('"', 1)[1].rsplit('"', 1)[0]
#         except Exception:
#             return "Terminal"

#     def _get_current_title(self):
#         if self.system == "Windows":
#             return self._get_title_windows()
#         else:
#             return self._get_title_linux()

#     def _flash_title(self, title="DING!!", duration=2):
#         self._set_title(title)
#         self.time.sleep(duration)
#         self._set_title(self.original_title)

#     def _auto_detect_input_device(self):
#         for i, dev in enumerate(self.sd.query_devices()):
#             if dev['max_input_channels'] > 0:
#                 return i
#         raise RuntimeError("No input audio devices found")

#     def _audio_callback(self, indata, frames, time_info, status):
#         volume = self.np.sqrt(self.np.mean(indata**2))
#         now = self.time.time()

#         if self.debug:
#             print(f"Volume: {volume:.5f}", end='\r')

#         if volume > self.THRESHOLD and (now - self.last_ding_time) >= self.COOLDOWN:
#             self.ding_count += 1
#             self.last_ding_time = now
#             if self.on_ding:
#                 self.on_ding(self.ding_count)
#             self._flash_title()

#     def run(self):
#         try:
#             self._set_title(self.original_title)
#             print("🎧 Listening for sound... (Ctrl+C to stop)")
#             print(f"🎤 Using input device index: {self.device}")
#             with self.sd.InputStream(callback=self._audio_callback, device=self.device):
#                 while True:
#                     self.sd.sleep(int(self.INTERVAL * 1000))
#         except KeyboardInterrupt:
#             print("\n👋 Exiting.")
#             self._set_title(self.original_title)
#         except Exception as e:
#             print(f"❌ Error: {e}")
#             self._set_title(self.original_title)


# def my_ding_handler(count):
#     print(f"[{count}] DING detected!")

# def action():
#     notifier = SoundDingNotifier(
#         threshold=0.02,    # sensitive enough for short beeps
#         cooldown=0.75,     # allow fast repeated detection
#         interval=0.05,     # frequent mic checks
#         on_ding=my_ding_handler,
#         debug=True         # show volume levels in real-time
#     )
#     notifier.run()






















# class SoundDingNotifier:
#     import os
#     import sys
#     import time
#     import platform
#     import numpy as np
#     import sounddevice as sd

#     def __init__(self, on_ding=None, cooldown=1.0, interval=0.1, device=None):
#         self.THRESHOLD = 0.001       # Extremely sensitive
#         self.COOLDOWN = cooldown     # Seconds between dings
#         self.INTERVAL = interval     # Interval between checks
#         self.on_ding = on_ding       # Optional callback
#         self.device = device or self._auto_detect_input_device()

#         self.system = self.platform.system()
#         self.ding_count = 0
#         self.last_ding_time = 0
#         self.original_title = self._get_current_title()

#     def _auto_detect_input_device(self):
#         for i, dev in enumerate(self.sd.query_devices()):
#             if dev['max_input_channels'] > 0:
#                 return i
#         raise RuntimeError("No input audio devices found")

#     def _set_title(self, title):
#         if self.system == "Windows":
#             self.os.system(f"title {title}")
#         else:
#             self.sys.stdout.write(f"\33]0;{title}\a")
#             self.sys.stdout.flush()

#     def _get_title_windows(self):
#         try:
#             import ctypes
#             buffer = ctypes.create_unicode_buffer(1024)
#             ctypes.windll.kernel32.GetConsoleTitleW(buffer, 1024)
#             return buffer.value
#         except Exception:
#             return "Terminal"

#     def _get_title_linux(self):
#         try:
#             import subprocess
#             output = subprocess.check_output(
#                 ['xprop', '-id', self.os.environ['WINDOWID'], 'WM_NAME'],
#                 stderr=self.subprocess.DEVNULL
#             )
#             return output.decode().split('"', 1)[1].rsplit('"', 1)[0]
#         except Exception:
#             return "Terminal"

#     def _get_current_title(self):
#         if self.system == "Windows":
#             return self._get_title_windows()
#         else:
#             return self._get_title_linux()

#     def _flash_title(self, title="DING!!", duration=2):
#         self._set_title(title)
#         self.time.sleep(duration)
#         self._set_title(self.original_title)

#     def _audio_callback(self, indata, frames, time_info, status):
#         volume = self.np.sqrt(self.np.mean(indata**2))
#         now = self.time.time()

#         if volume > self.THRESHOLD and (now - self.last_ding_time) >= self.COOLDOWN:
#             self.ding_count += 1
#             self.last_ding_time = now

#             if self.on_ding:
#                 self.on_ding(self.ding_count)

#             self._flash_title()

#     def run(self):
#         try:
#             self._set_title(self.original_title)
#             print("🎧 Listening for any sound... (Ctrl+C to stop)")
#             with self.sd.InputStream(callback=self._audio_callback, device=self.device):
#                 while True:
#                     self.sd.sleep(int(self.INTERVAL * 1000))
#         except KeyboardInterrupt:
#             print("\n👋 Exiting.")
#             self._set_title(self.original_title)
#         except Exception as e:
#             print(f"❌ Error: {e}")
#             self._set_title(self.original_title)




# def my_ding(count):
#     print(f"[{count}] 🔔 Sound detected!")

# if __name__ == "__main__":
#     SoundDingNotifier(on_ding=my_ding).run()
































# import sounddevice as sd
# import numpy as np
# import time

# THRESHOLD = 0.001
# COOLDOWN = 1.0  # seconds
# last_ding = 0

# def audio_callback(indata, frames, time_info, status):
#     global last_ding
#     volume = np.sqrt(np.mean(indata**2))
#     now = time.time()
#     if volume > THRESHOLD and (now - last_ding) > COOLDOWN:
#         print("🔔 DING!")
#         last_ding = now

# print("🎙️ Listening for sound... Ctrl+C to stop.")
# with sd.InputStream(callback=audio_callback):
#     while True:
#         sd.sleep(100)




























# import sounddevice as sd
# import numpy as np
# import time

# THRESHOLD = 0.001
# COOLDOWN = 1.0  # seconds
# last_ding = 0

# samplerate = 44100  # Standard audio sampling rate
# duration = 0.1      # 100ms chunks

# print("🎙️ Listening for sound... Ctrl+C to stop.")
# while True:
#     audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='float32')
#     sd.wait()  # Wait until recording is finished

#     volume = np.sqrt(np.mean(audio**2))
#     now = time.time()

#     if volume > THRESHOLD and (now - last_ding) > COOLDOWN:
#         print("🔔 DING!")
#         last_ding = now

#     time.sleep(0.01)





















import soundcard as sc

print("🎤 Microphones:")
for mic in sc.all_microphones(include_loopback=True):
    print(f"- {mic.name} (loopback={mic.is_loopback})")

print("\n🔊 Speakers:")
for spk in sc.all_speakers():
    print(f"- {spk.name}")




















########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)