import _rightThumb._base3 as _

def hexColor(*args, h=None, c=None, p=False):
    text = ''.join(map(str, args))
    global color_dict
    # print(h,c)
    # if c and c == 'help':
    #     # print(color_dict)
    #     for color in color_dict:
    #         hex_color = color_dict[color]
    #         hex_color = hex_color.lstrip('#')
    #         text = color
    #         r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    #         colorized = f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    #         test = color
    #         test = test.replace('_red','')
    #         test = test.replace('_orange','')
    #         test = test.replace('_purple','')
    #         test = test.replace('_white','')
    #         test = test.replace('_blue','')
    #         test = test.replace('_pink','')
    #         test = test.replace('_green','')
    #         test = test.replace('_gray','')


    #         if _.showLine(test):
    #             print(colorized)
    #     return text


    if c.startswith('#'):
        h = c
        c = None
    if not c is None:
        c=c.lower().strip()
        if not c in color_dict:
            for color in color_dict:
                test = color
                test = test.replace('_red','')
                test = test.replace('_orange','')
                test = test.replace('_purple','')
                test = test.replace('_white','')
                test = test.replace('_blue','')
                test = test.replace('_pink','')
                test = test.replace('_green','')
                test = test.replace('_gray','')
                test=test.strip()
                if test == c:
                    c = color
                    break
        if not c in color_dict:
            c = None
        else:
            h = color_dict[c]
    hex_color = h
    
    if h is None and c is None:
        global colorHelp

        if _.switches.isActive('Plus') and _.switches.value('Plus') == 'help':
            colors = []
            spent=[]
            for color in color_dict:
                for col in colorHelp[color].split(','):
                    hex_color = color_dict[color]
                    hex_color = hex_color.lstrip('#')
                    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                    colorized = f"\033[38;2;{r};{g};{b}m{col}\033[0m"
                    if col in spent:
                        continue
                    colors.append(colorized)
                    spent.append(col)
            # colors.sort()
            for color in colors:
                print(color)
            return ''
        for color in color_dict:
            hex_color = color_dict[color]
            hex_color = hex_color.lstrip('#')
            text = color
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            colorized = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
            
            if color in colorHelp:
                ColorCategory = colorHelp[color]
            else:
                ColorCategory = 'a5db92a1b958'
            if _.showLine(color) or _.showLine(ColorCategory):
                print(colorized)
        return ''
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    colorized = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    if p:
        print(colorized)
    # print(colorized)
    return colorized

color_dict = {
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
hexColors = color_dict

colorHelp = {
    "black": "black",
    "white": "white",
    "red": "red",
    "green": "green",
    "blue": "blue",
    "yellow": "yellow",
    "cyan": "cyan,blue,green",
    "magenta_purple": "magenta,purple,red,blue",
    "gray": "gray,black,white",
    "dark_gray": "dark,gray,black",
    "light_gray": "light,gray,white",
    "silver": "silver,gray,white",
    "alice_blue": "alice,blue,white",
    "antique_white": "antique,white",
    "aqua": "aqua,cyan,blue,green",
    "aquamarine": "aquamarine,cyan,green,blue",
    "azure": "azure,blue,white",
    "beige": "beige,tan,white",
    "bisque": "bisque,peach,white",
    "blue_violet": "blue,violet,purple",
    "brown": "brown,red",
    "burly_wood": "burly,wood,brown,tan",
    "cadet_blue": "cadet,blue,gray",
    "chartreuse": "chartreuse,green,yellow",
    "chocolate": "chocolate,brown",
    "coral_orange": "coral,orange,red",
    "cornflower_blue": "cornflower,blue",
    "crimson_red": "crimson,red",
    "dark_blue": "dark,blue",
    "dark_cyan": "dark,cyan,blue,green",
    "dark_goldenrod": "dark,goldenrod,gold,brown",
    "dark_gray": "dark,gray,black",
    "dark_green": "dark,green",
    "dark_khaki": "dark,khaki,yellow,brown",
    "dark_magenta_purple": "dark,magenta,purple,red,blue",
    "dark_olive_green": "dark,olive,green",
    "dark_orange": "dark,orange,red",
    "dark_orchid": "dark,orchid,purple",
    "dark_red": "dark,red",
    "dark_salmon": "dark,salmon,red,orange",
    "dark_sea_green": "dark,sea,green",
    "dark_slate_blue": "dark,slate,blue",
    "dark_slate_gray": "dark,slate,gray,black",
    "dark_turquoise": "dark,turquoise,cyan,blue",
    "dark_violet": "dark,violet,purple",
    "deep_pink": "deep,pink,red",
    "deep_sky_blue": "deep,sky,blue",
    "dim_gray": "dim,gray,black",
    "dodger_blue": "dodger,blue",
    "firebrick": "firebrick,red",
    "forest_green": "forest,green",
    "fuchsia": "fuchsia,magenta,purple,red,blue",
    "gainsboro": "gainsboro,gray,white",
    "gold": "gold,yellow",
    "goldenrod": "goldenrod,gold,yellow,brown",
    "green_yellow": "green,yellow",
    "hot_pink": "hot,pink,red",
    "indian_red": "indian,red",
    "indigo": "indigo,blue,purple",
    "khaki": "khaki,yellow,brown",
    "lawn_green": "lawn,green",
    "light_blue": "light,blue",
    "light_coral": "light,coral,red,orange",
    "light_cyan": "light,cyan,blue,green",
    "light_gray": "light,gray,white",
    "light_green": "light,green",
    "light_pink": "light,pink,red",
    "light_salmon": "light,salmon,red,orange",
    "light_sea_green": "light,sea,green,cyan",
    "light_sky_blue": "light,sky,blue",
    "light_slate_gray": "light,slate,gray,black",
    "light_steel_blue": "light,steel,blue",
    "light_yellow": "light,yellow",
    "lime": "lime,green",
    "lime_green": "lime,green",
    "linen": "linen,white",
    "medium_aquamarine": "medium,aquamarine,cyan,green,blue",
    "medium_blue": "medium,blue",
    "medium_orchid": "medium,orchid,purple",
    "medium_purple": "medium,purple",
    "medium_sea_green": "medium,sea,green",
    "medium_slate_blue": "medium,slate,blue",
    "medium_spring_green": "medium,spring,green",
    "medium_turquoise": "medium,turquoise,cyan,blue",
    "medium_violet_red": "medium,violet,red,purple",
    "mint_cream_white": "mint,cream,white",
    "misty_rose": "misty,rose,pink,red",
    "moccasin": "moccasin,peach,white",
    "navajo_white": "navajo,white",
    "old_lace": "old,lace,white",
    "olive": "olive,green,brown",
    "orange": "orange,red,yellow",
    "orange_red": "orange,red",
    "orchid": "orchid,purple",
    "pale_goldenrod": "pale,goldenrod,gold,yellow,brown",
    "pale_green": "pale,green",
    "pale_turquoise": "pale,turquoise,cyan,blue",
    "pale_violet_red": "pale,violet,red,purple",
    "papaya_whip": "papaya,whip,peach,white",
    "peach_puff": "peach,puff,orange,white",
    "peru": "peru,brown",
    "pink": "pink,red",
    "plum": "plum,purple",
    "powder_blue": "powder,blue",
    "purple": "purple,magenta,blue,red",
    "rebecca_purple": "rebecca,purple",
    "rosy_brown": "rosy,brown",
    "royal_blue": "royal,blue",
    "saddle_brown": "saddle,brown",
    "salmon": "salmon,red,orange",
    "sandy_brown": "sandy,brown",
    "sea_green": "sea,green",
    "seashell": "seashell,white",
    "sienna": "sienna,brown",
    "sky_blue": "sky,blue",
    "slate_blue": "slate,blue",
    "snow": "snow,white",
    "spring_green": "spring,green",
    "steel_blue": "steel,blue",
    "tan": "tan,brown",
    "teal": "teal,cyan,blue,green",
    "thistle": "thistle,purple",
    "tomato_red": "tomato,red,orange",
    "turquoise": "turquoise,cyan,blue,green",
    "violet": "violet,purple",
    "wheat": "wheat,tan,white",
    "yellow_green": "yellow,green",
}
