# pcopy.py
import sys

try:
    import pyperclip
except ImportError:
    print('[Error] Missing dependency: pyperclip\nInstall it with: pip install pyperclip')
    sys.exit(1)

text = sys.stdin.read().strip()

if text:
    pyperclip.copy(text)
    print(f'[Copied] {repr(text)}')
else:
    print('[No Input] Nothing was piped in.')
