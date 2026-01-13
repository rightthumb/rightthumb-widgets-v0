from pynput import keyboard

# Initialize keyboard controller
controller = keyboard.Controller()

# Define replacements in a structured way
replacements = [
	('p', ['[', '[']),   # Replace `[[` with `p`
]

# Track the last few pressed keys
buffer = []
running = True  # Control loop execution

def on_press(key):
	global buffer, running

	try:
		if key == keyboard.Key.ctrl_c:
			print("\nExiting...")
			running = False  # Stop the listener loop
			return False  # Stop listener

		char = key.char if hasattr(key, 'char') else None
		if char:
			buffer.append(char)

			# Check if buffer matches any replacement pattern
			for replacement, sequence in replacements:
				if buffer[-len(sequence):] == sequence:
					# Simulate backspaces
					for _ in sequence:
						controller.press(keyboard.Key.backspace)
						controller.release(keyboard.Key.backspace)

					# Simulate typing the replacement key
					controller.press(replacement)
					controller.release(replacement)

					# Clear buffer to prevent consecutive misfires
					buffer.clear()
					break

		else:
			buffer.clear()  # Reset buffer if a non-character key is pressed

	except AttributeError:
		buffer.clear()  # Reset buffer if an unrecognized key is pressed

# Listen for keyboard events in a loop that can be interrupted with Ctrl+C
with keyboard.Listener(on_press=on_press) as listener:
	try:
		while running:
			pass  # Keep running until Ctrl+C is pressed
	except KeyboardInterrupt:
		print("\nExiting...")