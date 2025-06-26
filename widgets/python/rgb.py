from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
import time

# Initialize OpenRGB client
client = OpenRGBClient()
print('client.devices:',client.devices)

# Get keyboard device (you may need to adjust this if you have multiple devices)
keyboard = client.devices[0]  

# Define a function to change the color
def set_keyboard_color(color_name):
    color_map = {
        "red": RGBColor(255, 0, 0),
        "green": RGBColor(0, 255, 0),
        "blue": RGBColor(0, 0, 255),
        "yellow": RGBColor(255, 255, 0),
        "cyan": RGBColor(0, 255, 255),
        "magenta": RGBColor(255, 0, 255),
        "white": RGBColor(255, 255, 255),
        "orange": RGBColor(255, 165, 0),
        "purple": RGBColor(128, 0, 128),
        "pink": RGBColor(255, 105, 180),
        "lime": RGBColor(0, 255, 0),
        "teal": RGBColor(0, 128, 128),
        "brown": RGBColor(165, 42, 42),
        "gray": RGBColor(128, 128, 128),
        "off": RGBColor(0, 0, 0)  # Turns off the lights
    }
    
    color = color_map.get(color_name.lower(), RGBColor(255, 255, 255))  # Default to white if color not found
    keyboard.set_color(color)

# Example Usage
set_keyboard_color("blue")   # Change to blue
time.sleep(2)  # Wait 2 seconds
set_keyboard_color("red")    # Change to red
time.sleep(2)
set_keyboard_color("off")    # Turn off lights
