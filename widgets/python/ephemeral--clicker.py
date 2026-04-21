import pyperclip
import pyautogui
import time

pyautogui.doubleClick()
pyautogui.click()
pyautogui.rightClick()

clipboard_text = pyperclip.paste()
print(clipboard_text)
pyperclip.copy(clipboard_text.strip())
print("Copied to clipboard: " + clipboard_text)
