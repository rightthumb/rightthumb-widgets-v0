import _rightThumb._construct as __

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.token import Token, Punctuation, Keyword, Name, String, Comment
from pygments.formatters import Terminal256Formatter
from pygments.style import Style

# Custom color dictionary
custom_colors = {
    Punctuation: 'bold #ff79c6',      # Brackets and parentheses
    Keyword: 'bold #8be9fd',          # Keywords like def, class, return
    Name: '#f1fa8c',                  # Variable names
    String: '#50fa7b',                # Strings
    Comment: 'italic #6272a4',        # Comments
}
from _rightThumb._base3.library.tools.code.functions.hexColor import hexColors


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
def pyColor(code,theme=None):
    if not theme is None:
        __.CodeTheme = theme
    highlighted_code = highlight(code, PythonLexer(), Terminal256Formatter(style=CustomStyle))
    print(highlighted_code)














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