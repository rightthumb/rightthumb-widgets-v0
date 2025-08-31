import _rightThumb._construct as __ # type: ignore
import _rightThumb._vars as _v # type: ignore
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(_v.py)
sys.path.append(_v.py+os.sep+'library')
from pygments import highlight # type: ignore
from pygments.lexers import PythonLexer # type: ignore
from pygments.token import Token, Punctuation, Keyword, Name, String, Comment # type: ignore
from pygments.formatters import Terminal256Formatter # type: ignore
from pygments.style import Style # type: ignore

def pyColor(code,theme=None):
    code = code.replace('\t','    ')
    if not theme is None:
        __.CodeTheme = theme
    highlighted_code = highlight(code, PythonLexer(), Terminal256Formatter(style=CustomStyle))
    print(highlighted_code)

# Custom color dictionary
custom_colors = {
    Punctuation: 'bold #ff79c6',      # Brackets and parentheses
    Keyword: 'bold #8be9fd',          # Keywords like def, class, return
    Name: '#f1fa8c',                  # Variable names
    String: '#50fa7b',                # Strings
    Comment: 'italic #6272a4',        # Comments
}

# intelligent_code = __.dot()
# def hexColor(*args, **kwargs):
# 	import importlib.util
# 	if 'hexColor' not in intelligent_code.functions:
# 		import importlib.util
# 		path = os.path.normpath(_v.w+'/widgets/python/library/tools/code/functions/hexColor.py')
# 		spec = importlib.util.spec_from_file_location('hexColor', path)
# 		module = importlib.util.module_from_spec(spec)
# 		spec.loader.exec_module(module)
# 		intelligent_code.functions['hexColor'] = module.hexColor
# 	return intelligent_code.functions['hexColor'](*args, **kwargs)

# from hexColor import hexColors


hexColors = {
	# Basic Colors
	"black": "#000000",
	"white": "#ffffff",
	"red": "#ff0000",
	"green": "#00ff00",
	"blue": "#0000ff",
	"yellow": "#ffff00",
	"cyan": "#00ffff",
	"magenta_purple": "#ff00ff",
	
	# Grayscale
	"gray": "#808080",
	"dark_gray": "#404040",
	"light_gray": "#d3d3d3",
	"silver": "#c0c0c0",
	# "charcoal": "#333333",
	
	# Web Colors
	"alice_blue": "#f0f8ff",
	"antique_white": "#faebd7",
	"aqua": "#00ffff",
	"aquamarine": "#7fffd4",
	"azure": "#f0ffff",
	"beige": "#f5f5dc",
	"bisque": "#ffe4c4",
	# "blanched_almond": "#ffebcd",
	"blue_violet": "#8a2be2",
	"brown": "#a52a2a",
	"burly_wood": "#deb887",
	"cadet_blue": "#5f9ea0",
	"chartreuse": "#7fff00",
	"chocolate": "#d2691e",
	"coral_orange": "#ff7f50",
	"cornflower_blue": "#6495ed",
	"crimson_red": "#dc143c",
	"dark_blue": "#00008b",
	"dark_cyan": "#008b8b",
	"dark_goldenrod": "#b8860b",
	"dark_gray": "#a9a9a9",
	"dark_green": "#006400",
	"dark_khaki": "#bdb76b",
	"dark_magenta_purple": "#8b008b",
	"dark_olive_green": "#556b2f",
	"dark_orange": "#ff8c00",
	"dark_orchid": "#9932cc",
	"dark_red": "#8b0000",
	"dark_salmon": "#e9967a",
	"dark_sea_green": "#8fbc8f",
	"dark_slate_blue": "#483d8b",
	"dark_slate_gray": "#2f4f4f",
	"dark_turquoise": "#00ced1",
	"dark_violet": "#9400d3",
	"deep_pink": "#ff1493",
	"deep_sky_blue": "#00bfff",
	"dim_gray": "#696969",
	"dodger_blue": "#1e90ff",
	"firebrick": "#b22222",
	# "floral_white": "#fffaf0",
	"forest_green": "#228b22",
	"fuchsia": "#ff00ff",
	"gainsboro": "#dcdcdc",
	# "ghost_white": "#f8f8ff",
	"gold": "#ffd700",
	"goldenrod": "#daa520",
	"green_yellow": "#adff2f",
	# "honeydew": "#f0fff0",
	"hot_pink": "#ff69b4",
	"indian_red": "#cd5c5c",
	"indigo": "#4b0082",
	# "ivory": "#fffff0",
	"khaki": "#f0e68c",
	# "lavender": "#e6e6fa",
	# "lavender_blush": "#fff0f5",
	"lawn_green": "#7cfc00",
	# "lemon_chiffon": "#fffacd",
	"light_blue": "#add8e6",
	"light_coral": "#f08080",
	"light_cyan": "#e0ffff",
	# "light_goldenrod_yellow": "#fafad2",
	"light_gray": "#d3d3d3",
	"light_green": "#90ee90",
	"light_pink": "#ffb6c1",
	"light_salmon": "#ffa07a",
	"light_sea_green": "#20b2aa",
	"light_sky_blue": "#87cefa",
	"light_slate_gray": "#778899",
	"light_steel_blue": "#b0c4de",
	"light_yellow": "#ffffe0",
	"lime": "#00ff00",
	"lime_green": "#32cd32",
	"linen": "#faf0e6",
	# "maroon": "#800000",
	"medium_aquamarine": "#66cdaa",
	"medium_blue": "#0000cd",
	"medium_orchid": "#ba55d3",
	"medium_purple": "#9370db",
	"medium_sea_green": "#3cb371",
	"medium_slate_blue": "#7b68ee",
	"medium_spring_green": "#00fa9a",
	"medium_turquoise": "#48d1cc",
	"medium_violet_red": "#c71585",
	# "midnight_blue": "#191970",
	"mint_cream_white": "#f5fffa",
	"misty_rose": "#ffe4e1",
	"moccasin": "#ffe4b5",
	"navajo_white": "#ffdead",
	# "navy": "#000080",
	"old_lace": "#fdf5e6",
	"olive": "#808000",
	# "olive_drab": "#6b8e23",
	"orange": "#ffa500",
	"orange_red": "#ff4500",
	"orchid": "#da70d6",
	"pale_goldenrod": "#eee8aa",
	"pale_green": "#98fb98",
	"pale_turquoise": "#afeeee",
	"pale_violet_red": "#db7093",
	"papaya_whip": "#ffefd5",
	"peach_puff": "#ffdab9",
	"peru": "#cd853f",
	"pink": "#ffc0cb",
	"plum": "#dda0dd",
	"powder_blue": "#b0e0e6",
	"purple": "#800080",
	"rebecca_purple": "#663399",
	"rosy_brown": "#bc8f8f",
	"royal_blue": "#4169e1",
	"saddle_brown": "#8b4513",
	"salmon": "#fa8072",
	"sandy_brown": "#f4a460",
	"sea_green": "#2e8b57",
	"seashell": "#fff5ee",
	"sienna": "#a0522d",
	"sky_blue": "#87ceeb",
	"slate_blue": "#6a5acd",
	# "slate_gray": "#708090",
	"snow": "#fffafa",
	"spring_green": "#00ff7f",
	"steel_blue": "#4682b4",
	"tan": "#d2b48c",
	"teal": "#008080",
	"thistle": "#d8bfd8",
	"tomato_red": "#ff6347",
	"turquoise": "#40e0d0",
	"violet": "#ee82ee",
	"wheat": "#f5deb3",
	"yellow_green": "#9acd32",
}

# 🌱 Earthy Tones Theme
earthy_tones = {
    Punctuation: "bold " + hexColors["saddle_brown"],
    Keyword: "bold " + hexColors["dark_orange"],
    Name: hexColors["pale_green"],
    String: hexColors["light_sea_green"],
    Comment: "italic " + hexColors["peru"],
}

# 🌊 Oceanic Theme
oceanic = {
    Punctuation: "bold " + hexColors["dodger_blue"],
    Keyword: "bold " + hexColors["dark_turquoise"],
    Name: hexColors["cadet_blue"],
    String: hexColors["medium_aquamarine"],
    Comment: "italic " + hexColors["cornflower_blue"],
}

# 🌸 Pastel Theme
pastel = {
    Punctuation: "bold " + hexColors["misty_rose"],
    Keyword: "bold " + hexColors["orchid"],
    Name: hexColors["peach_puff"],
    String: hexColors["light_pink"],
    Comment: "italic " + hexColors["light_salmon"],
}

# 🔥 Warm & Bold Theme
warm_bold = {
    Punctuation: "bold " + hexColors["chocolate"],
    Keyword: "bold " + hexColors["crimson_red"],
    Name: hexColors["tomato_red"],
    String: hexColors["gold"],
    Comment: "italic " + hexColors["dark_goldenrod"],
}

# 🌾 Autumn Theme
autumn = {
    Punctuation: "bold " + hexColors["sienna"],
    Keyword: "bold " + hexColors["orange_red"],
    Name: hexColors["burly_wood"],
    String: hexColors["navajo_white"],
    Comment: "italic " + hexColors["pale_violet_red"],
}

# 🌌 Midnight Theme
midnight = {
    Punctuation: "bold " + hexColors["dark_slate_gray"],
    Keyword: "bold " + hexColors["dark_violet"],
    Name: hexColors["medium_slate_blue"],
    String: hexColors["powder_blue"],
    Comment: "italic " + hexColors["indigo"],
}

# 🌼 Spring Theme
spring = {
    Punctuation: "bold " + hexColors["lime_green"],
    Keyword: "bold " + hexColors["chartreuse"],
    Name: hexColors["medium_spring_green"],
    String: hexColors["light_yellow"],
    Comment: "italic " + hexColors["pale_goldenrod"],
}

# 🌱 Earthy Tones Theme
earthy_tones = {
    Punctuation: "bold " + hexColors["saddle_brown"],
    Keyword: "bold " + hexColors["dark_orange"],
    Name: hexColors["pale_green"],
    String: hexColors["light_sea_green"],
    Comment: "italic " + hexColors["peru"],
}

# 🌊 Oceanic Theme
oceanic = {
    Punctuation: "bold " + hexColors["dodger_blue"],
    Keyword: "bold " + hexColors["dark_turquoise"],
    Name: hexColors["cadet_blue"],
    String: hexColors["medium_aquamarine"],
    Comment: "italic " + hexColors["cornflower_blue"],
}

# 🌸 Pastel Theme
pastel = {
    Punctuation: "bold " + hexColors["misty_rose"],
    Keyword: "bold " + hexColors["orchid"],
    Name: hexColors["peach_puff"],
    String: hexColors["light_pink"],
    Comment: "italic " + hexColors["light_salmon"],
}

# 🔥 Warm & Bold Theme
warm_bold = {
    Punctuation: "bold " + hexColors["chocolate"],
    Keyword: "bold " + hexColors["crimson_red"],
    Name: hexColors["tomato_red"],
    String: hexColors["gold"],
    Comment: "italic " + hexColors["dark_goldenrod"],
}

# 🌾 Autumn Theme
autumn = {
    Punctuation: "bold " + hexColors["sienna"],
    Keyword: "bold " + hexColors["orange_red"],
    Name: hexColors["burly_wood"],
    String: hexColors["navajo_white"],
    Comment: "italic " + hexColors["pale_violet_red"],
}

# 🌌 Midnight Theme
midnight = {
    Punctuation: "bold " + hexColors["dark_slate_gray"],
    Keyword: "bold " + hexColors["dark_violet"],
    Name: hexColors["medium_slate_blue"],
    String: hexColors["powder_blue"],
    Comment: "italic " + hexColors["indigo"],
}

# 🌼 Spring Theme
spring2 = {
    Punctuation: "bold " + hexColors["lime_green"],
    Keyword: "bold " + hexColors["chartreuse"],
    Name: hexColors["medium_spring_green"],
    String: hexColors["light_yellow"],
    Comment: "italic " + hexColors["pale_goldenrod"],
}

# 🌋 Volcano Theme
volcano = {
    Punctuation: "bold " + hexColors["firebrick"],
    Keyword: "bold " + hexColors["deep_pink"],
    Name: hexColors["dark_salmon"],
    String: hexColors["light_coral"],
    Comment: "italic " + hexColors["rosy_brown"],
}

# 🧊 Frosty Theme
frosty = {
    Punctuation: "bold " + hexColors["alice_blue"],
    Keyword: "bold " + hexColors["azure"],
    Name: hexColors["light_cyan"],
    String: hexColors["medium_turquoise"],
    Comment: "italic " + hexColors["powder_blue"],
}

# 🏜️ Desert Theme
desert = {
    Punctuation: "bold " + hexColors["burly_wood"],
    Keyword: "bold " + hexColors["goldenrod"],
    Name: hexColors["sandy_brown"],
    String: hexColors["khaki"],
    Comment: "italic " + hexColors["old_lace"],
}

# 🌿 Forest Theme
forest = {
    Punctuation: "bold " + hexColors["forest_green"],
    Keyword: "bold " + hexColors["dark_olive_green"],
    Name: hexColors["olive"],
    String: hexColors["lime_green"],
    Comment: "italic " + hexColors["medium_sea_green"],
}

# 🌈 Rainbow Theme
rainbow = {
    Punctuation: "bold " + hexColors["red"],
    Keyword: "bold " + hexColors["orange"],
    Name: hexColors["yellow"],
    String: hexColors["green"],
    Comment: "italic " + hexColors["blue"],
}

# 🧙‍♂️ Mystic Theme
mystic = {
    Punctuation: "bold " + hexColors["blue_violet"],
    Keyword: "bold " + hexColors["dark_orchid"],
    Name: hexColors["medium_purple"],
    String: hexColors["plum"],
    Comment: "italic " + hexColors["thistle"],
}

# ⚙️ Industrial Theme
industrial = {
    Punctuation: "bold " + hexColors["dim_gray"],
    Keyword: "bold " + hexColors["dark_slate_gray"],
    Name: hexColors["slate_blue"],
    String: hexColors["steel_blue"],
    Comment: "italic " + hexColors["light_steel_blue"],
}

# 🍂 Rustic Theme
rustic = {
    Punctuation: "bold " + hexColors["sienna"],
    Keyword: "bold " + hexColors["brown"],
    Name: hexColors["burly_wood"],
    String: hexColors["navajo_white"],
    Comment: "italic " + hexColors["wheat"],
}

# 🧪 Sci-Fi Theme
sci_fi = {
    Punctuation: "bold " + hexColors["lime"],
    Keyword: "bold " + hexColors["aqua"],
    Name: hexColors["medium_turquoise"],
    String: hexColors["deep_sky_blue"],
    Comment: "italic " + hexColors["dodger_blue"],
}

# 🎩 Victorian Theme
victorian = {
    Punctuation: "bold " + hexColors["antique_white"],
    Keyword: "bold " + hexColors["rosy_brown"],
    Name: hexColors["misty_rose"],
    String: hexColors["peach_puff"],
    Comment: "italic " + hexColors["bisque"],
}


# Retro Theme
retro = {
    Punctuation: 'bold '+hexColors['wheat'],
    Keyword: 'bold '+hexColors['salmon'],
    Name: hexColors['rosy_brown'],
    String: hexColors['dark_sea_green'],
    Comment: 'italic '+hexColors['pale_violet_red'],
}


# earthy_tones oceanic pastel warm_bold autumn midnight
# spring earthy_tones oceanic pastel warm_bold autumn
# midnight spring2 volcano frosty desert forest rainbow
# mystic industrial rustic sci_fi victorian retro


# theme = eval(__.CodeTheme)

# Custom Style that uses the color dictionary
class CustomStyle(Style):
    default_style = ""
    styles = eval(__.CodeTheme)

# Function to colorize Python code with custom colors















# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.token import Punctuation
# from pygments.formatters import Terminal256Formatter
# from pygments.style import Style
# from pygments.styles.default import DefaultStyle

# # Custom Style to colorize brackets and keep original syntax colors
# class CustomStyle(DefaultStyle):
#     styles = DefaultStyle.styles.copy()
#     styles[Punctuation] = 'bold #ff79c6'

# # Function to colorize Python code with customized bracket colors
# def pyColor(code):
#     highlighted_code = highlight(code, PythonLexer(), Terminal256Formatter(style=CustomStyle))
#     print(highlighted_code)






# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import TerminalFormatter

# def pyColor(code):
#     highlighted_code = highlight(code, PythonLexer(), TerminalFormatter())
#     print(highlighted_code)