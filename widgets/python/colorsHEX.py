import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Count', '-cnt', '200' )
	_.switches.register( 'Threshold', '-t', '30' )
	_.switches.register( 'Site', '-site', 'Go to the website uses the output of this app' )

_._default_settings_()

_.appInfo[focus()] = {
	'file': 'colors-light.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start

import random
from colorsys import hls_to_rgb
import math

def color_distance(color1, color2):
	"""Calculate the Euclidean distance between two colors in RGB space."""
	r1, g1, b1 = color1
	r2, g2, b2 = color2
	return math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)

def generate_light_colors(quantity, threshold=30):
	"""Generate distinct light and vibrant colors in hexadecimal format.

	Args:
		quantity (int): The number of light colors to generate.
		threshold (int): The minimum distance between any two colors.

	Returns:
		list: A list of distinct light, vibrant colors in hexadecimal format.
	"""
	colors = []
	hex_colors = []  # List to store hexadecimal colors
	while len(hex_colors) < quantity:
		# Hue is selected randomly, Saturation is kept high, and Lightness is kept high to ensure lightness
		hue = random.random()  # Hue between 0 and 1
		lightness = random.uniform(0.7, 0.9)  # High lightness for lighter colors
		saturation = random.uniform(0.7, 1)  # High saturation for vibrant colors

		# Convert HLS to RGB
		r, g, b = hls_to_rgb(hue, lightness, saturation)
		new_color = (int(r * 255), int(g * 255), int(b * 255))

		# Check if the new color is distinct from the others
		if all(color_distance(new_color, existing_color) >= threshold for existing_color in colors):
			hex_color = "#{:02x}{:02x}{:02x}".format(*new_color)
			colors.append(new_color)  # Append the RGB tuple to check for similarity
			hex_colors.append(hex_color)  # Append the Hex color for output

	return hex_colors


import webbrowser


def action():
	if _.switches.isActive('Site'):
		url='https://sds.sh/a/color/'
		webbrowser.open(url, new=2)
		return None
	number_of_colors = 10
	threshold = 30
	if _.switches.isActive('Count'): number_of_colors = int(_.switches.value('Count'))
	if _.switches.isActive('Threshold'): threshold = int(_.switches.value('Threshold'))

	generated_colors = generate_light_colors(number_of_colors,threshold)
	print(generated_colors)

if __name__ == '__main__':
	action(); _.isExit(__file__);