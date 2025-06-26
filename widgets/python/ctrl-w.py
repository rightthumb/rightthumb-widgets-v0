import keyboard
import time

def simulate_ctrl_w():
    print("Simulating Ctrl+W...")
    keyboard.press_and_release('ctrl+w')

if __name__ == "__main__":
    time.sleep(3)  # Give time to switch to the target application
    simulate_ctrl_w()