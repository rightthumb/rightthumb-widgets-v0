from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import winsound
# http://stackoverflow.com/questions/911856/detecting-idle-time-in-python
class LASTINPUTINFO(Structure):
	_fields_ = [
		('cbSize', c_uint),
		('dwTime', c_uint),
	]

def get_idle_duration():
	lastInputInfo = LASTINPUTINFO()
	lastInputInfo.cbSize = sizeof(lastInputInfo)
	windll.user32.GetLastInputInfo(byref(lastInputInfo))
	millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
	return millis / 1000.0
while 1:
	GetLastInputInfo = int(get_idle_duration())
	print(GetLastInputInfo)
	if GetLastInputInfo == 480:
		# if GetLastInputInfo is 8 minutes, play a sound
		sound = r"c:\windows\media\notify.wav"
		winsound.PlaySound(sound, winsound.SND_FILENAME)
	if GetLastInputInfo == 560:
		# if GetLastInputInfo is 9 minutes, play a more annoying sound
		sound = r"c:\windows\media\ringout.wav"
		winsound.PlaySound(sound, winsound.SND_FILENAME)
		winsound.PlaySound(sound, winsound.SND_FILENAME)
		winsound.PlaySound(sound, winsound.SND_FILENAME)
		
	time.sleep(1)