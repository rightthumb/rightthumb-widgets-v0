
def cmdColor(command=None, switches=None, theme=None,  p=0,       pp=None, per=None, persist=None):
    """
    Legacy-style terminal command colorizer (hexColor-based).

    Args:
        command (str|list): command line string or list of tokens
        switches (None|list|set): known switches; if None, auto-detect -/+ and legacy / behavior
        theme (None|dict): override colors (uses your hexColor color names)

    Theme keys:
        cmd, py, pipe, switches, value, quote
    """

    global Persistant
    persistantPrint(command, pp, per, persist)
    if not Persistant is None: p = Persistant
    if command is None:
        return ""
    

    # Default theme matches your legacy example (and uses your hexColor color names)
    default_theme = {
        "cmd": "blue",
        "py": "yellow",
        "pipe": "red",
        "switches": "green",
        "value": "cyan",
        "quote": "darkcyan",
    }
    if theme is None:
        theme = default_theme
    else:
        t = dict(default_theme)
        t.update(theme)
        theme = t

    known = set(switches) if switches else None

    # Normalize input
    if isinstance(command, str):
        while '  ' in command:
            command = command.replace('  ', ' ')
        code = command
        tokens = command.split(" ")
    else:
        tokens = list(command)
        code = " ".join(tokens)

    # --- helpers (kept intentionally "dirty simple" like legacy) ---
    def is_pipe(tok):
        return tok == "|" or tok == "&"

    def is_p_trigger(tok):
        t = tok.lower()
        return (
            (tok.startswith("=") and len(tok) > 1)
            or tok.startswith("`")
            or tok.startswith("||")
            or t == "p"
            or t == "%py%"
            or t == "pp"
            or t == "python"
            or t == "python.exe"
            or t.endswith("python.exe")
        )

    def is_switch(tok):
        # Keep legacy: "+" is a switch
        if tok.startswith("+"):
            return True

        if known is None:
            # Legacy: "-" is switch always
            if tok.startswith("-"):
                return True
            # Legacy-ish: "/" counts as switch only if the overall line doesn't contain " -"
            if tok.startswith("/") and (" -" not in code):
                return True
            return False

        # Explicit switch list mode
        return tok in known

    def color_quotes(value_token):
        # Legacy behavior: if token contains quotes, color quote marks separately
        if '"' not in value_token:
            return hexColor(value_token, c=theme["value"])

        yx = ""
        buf = ""
        for ch in value_token:
            if ch != '"':
                buf += ch
            else:
                if buf:
                    yx += hexColor(buf, c=theme["value"])
                    buf = ""
                yx += hexColor('"', c=theme["quote"])
        if buf:
            yx += hexColor(buf, c=theme["value"])
        return yx

    # --- legacy-ish state machine ---
    result = ""
    lastP = False
    lastSwitch = False
    lastCMD = False
    lastPipe = False

    switchList = []
    for i, x in enumerate(tokens):
        if is_switch(x):
            switchList.append(x)
            # print(x)
    swDic = switchDict(switchList, command)
    _Values = []
    _ValuesRaw = []
    for k in swDic:
        for v in swDic[k]:
            # print(v)
            _ValuesRaw.append(v.strip('"').strip("'").strip())
            _Values.append(v.strip('"').strip("'").strip())
    
    # print pretty json
    # import json
    # print(json.dumps(swDic, indent=4))
    for i, x in enumerate(tokens):
        # print(x)
        if not x:
            continue

        if is_p_trigger(x):
            lastP = True

            # Keep your special prefix stripping exactly-ish
            if x.startswith("`") and x.endswith("`") and len(x) > 1:
                inner = x.replace("`", "")
                result += "`" + hexColor(inner, c=theme["cmd"]) + "`"
            elif x.startswith("`"):
                inner = x.replace("`", "")
                result += "`" + hexColor(inner, c=theme["cmd"])
            elif x.startswith("||"):
                inner = x.replace("||", "")
                result += hexColor(inner, c=theme["cmd"])
            elif x.startswith("="):
                inner = x.replace("=", "")
                result += hexColor(inner, c=theme["cmd"])
            else:
                result += hexColor(x, c=theme["cmd"])

            lastSwitch = False
            lastPipe = False

        elif i == 0 or lastPipe:
            lastPipe = False
            lastCMD = True
            result += hexColor(x, c=theme["cmd"])

        elif lastP:
            lastSwitch = False
            result += hexColor(x, c=theme["py"])

        elif x in _ValuesRaw or x.strip('"').strip("'").strip() in _Values:
            # print(x)
            lastSwitch = False
            result += hexColor(x, c=theme["value"])
            # result += hexColor(x, c=theme["py"])
            print(result)

        elif is_switch(x):
            lastSwitch = True
            result += hexColor(x, c=theme["switches"])

        elif is_pipe(x):
            lastCMD = False
            lastSwitch = False
            lastPipe = True
            result += hexColor(x, c=theme["pipe"])

        elif lastSwitch:
            result += color_quotes(x)

        elif lastCMD:
            result += hexColor(x, c=theme["value"])

        else:
            # fallback: uncolored
            result += x

        result += " "

        # Keep your "p" reset rule
        if x.lower() != "p":
            lastP = False

    payload =  result.rstrip()
    if p:
        print(payload)
    return payload

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from hexColor import hexColor

def persistantPrint(command, pp, per, persist):
    global Persistant
    if pp: Persistant = pp
    if per: Persistant = per
    if persist: Persistant = persist
    if not pp is None and pp and command is None:
        Persistant = pp
Persistant=None
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'switches', 'simple')))
from switchDict import switchDict   # type: ignore