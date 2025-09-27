import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
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
	'notes': [],
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

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import json

def rgb_to_hex(rgb):
	"""Convert RGB tuple to hex color string."""
	return '#{0:02x}{1:02x}{2:02x}'.format(rgb[0], rgb[1], rgb[2])

def extract_color_palette(image_path, n_colors=5):
	"""Extracts a color palette from an image."""
	# Load image and ensure it is in RGB format
	image = Image.open(image_path).convert('RGB')
	image = image.resize((100, 100))  # Resize for faster processing
	
	# Convert image data to a list of RGB values
	data = np.array(image)
	data = data.reshape((-1, 3))
	
	# Cluster colors using k-means
	kmeans = KMeans(n_clusters=n_colors)
	kmeans.fit(data)
	
	# Get palette (cluster centers) and convert to hex colors
	palette_hex = [rgb_to_hex(color) for color in kmeans.cluster_centers_.astype(int)]
	
	return palette_hex




def action():
	image_path = _.switches.values('Files')[0]
	palette = extract_color_palette(image_path)

	# Echo the resulting palette as JSON
	print(json.dumps(palette, indent=4))


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);