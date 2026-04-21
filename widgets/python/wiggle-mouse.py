import sys
import time
import pyautogui
import keyboard

def wiggle_mouse(interval=60):
    """Wiggle the mouse cursor every interval seconds and exit if Escape key is pressed."""
    print(f"Wiggling mouse every {interval} seconds. Ctrl+C to stop.")
    
    try:
        while True:
            # Check if escape key is pressed
            if keyboard.is_pressed('esc'):
                raise KeyboardInterrupt

            # Move the mouse slightly to the right
            pyautogui.move(10, 0, duration=0.5)

            # Wait half the interval
            time.sleep(interval/2)

            # Move the mouse slightly to the left
            pyautogui.move(-10, 0, duration=0.5)

            # Wait the remaining half of the interval
            time.sleep(interval/2)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            wiggle_mouse(int(sys.argv[2]))
        else:
            wiggle_mouse(540)
    except ValueError:
        print(f"Invalid argument: {sys.argv[2]}. Please provide a valid integer or no argument for default.")




