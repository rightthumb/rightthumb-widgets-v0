
def cmdTheme(command=None, switches=None, theme=None, override=None, p=0,       pp=None, per=None, persist=None):
    """
    Theme-aware command colorizer.

    Args:
        command (str|list): command line string or token list
        switches (None|list|set): known switches (passed to cmdColor)
        theme:
            - None                 -> default ("classic")
            - str                  -> theme name (COLOR_THEMES or ColorPallets)
            - dict (cmd-style)     -> direct cmdColor theme
            - dict (palette-style) -> semantic palette
        override (dict|None): final per-key overrides

    Returns:
        colorized string
    """

    global Persistant
    persistantPrint(command, pp, per, persist)
    if not Persistant is None: p = Persistant
    if command is None: return


    # ---- base default ----
    base_theme = COLOR_THEMES.get("classic", {
        "cmd": "blue",
        "py": "yellow",
        "pipe": "red",
        "switches": "green",
        "value": "cyan",
        "quote": "darkcyan",
    })

    resolved = dict(base_theme)

    # ---- resolve theme ----
    if isinstance(theme, str):
        # Command-style theme
        if theme in COLOR_THEMES:
            resolved.update(COLOR_THEMES[theme])

        # Semantic palette
        elif theme in ColorPallets:
            p = ColorPallets[theme]
            resolved.update({
                "cmd":      p.get("primary"),
                "switches": p.get("secondary"),
                "value":    p.get("success"),
                "pipe":     p.get("danger"),
                "py":       p.get("warning"),
                "quote":    p.get("info"),
            })

    elif isinstance(theme, dict):
        # Palette-style dict
        if "primary" in theme and "success" in theme:
            resolved.update({
                "cmd":      theme.get("primary"),
                "switches": theme.get("secondary"),
                "value":    theme.get("success"),
                "pipe":     theme.get("danger"),
                "py":       theme.get("warning"),
                "quote":    theme.get("info"),
            })
        else:
            # Assume cmdColor-style dict
            resolved.update(theme)

    # ---- overrides win last ----
    if isinstance(override, dict):
        resolved.update(override)

    # ---- delegate to cmdColor ----
    return cmdColor(
        command,
        switches=switches,
        theme=resolved,
        p=p
    )



def persistantPrint(command, pp, per, persist):
    global Persistant
    if pp: Persistant = pp
    if per: Persistant = per
    if persist: Persistant = persist
    if not pp is None and pp and command is None:
        Persistant = pp
Persistant=None






class Meta_Namespace():
    def __init__( self ):
        pass


intelligent_code = Meta_Namespace()
intelligent_code.functions = {}
intelligent_code.classes = {}

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from _rightThumb import _vars as _v   # type: ignore

# for p in sys.path:
#     print(p)
# sys.exit()
def cmdColor(*args, **kwargs):
	import importlib.util
	if 'cmdColor' not in intelligent_code.functions:
		import importlib.util
		path = os.path.normpath(_v.w+'/widgets/python/library/code/functions/cmdColor.py')
		spec = importlib.util.spec_from_file_location('cmdColor', path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		intelligent_code.functions['cmdColor'] = module.cmdColor
	return intelligent_code.functions['cmdColor'](*args, **kwargs)





import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from _colorVars import ColorPallets, COLOR_THEMES   # type: ignore
