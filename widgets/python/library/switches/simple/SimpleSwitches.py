class SimpleSwitches:
    """
    Minimal switch parser with alias support + optional trigger processing.

    Config format (example):
    switches = {
        "Files": {
            "type": "trigger",
            "switches": ["-f, --f, --files"],
            "description": "...",
            "example": "--files file1.txt file2.txt"
        },
        "Ago": {
            "type": "trigger",
            "switches": ["-ago --a"],   # spaces and/or commas ok
            "trigger": timeAgoTrigger
        },
    }
    """

    def __init__(self, switches_config: dict, argv=None, usage=[]):
        if type(usage) == str: usage = [usage]
        self.usage = usage
        switches_config = self.normalizeSwitches(switches_config)
        if 'Help' not in switches_config:
            switches_config['Help'] = {
                "type": "trigger",
                "switches": ["?", "??", "-h", "--help"],
                "description": "Show help for switches",
                "example": "--help Files",
                "trigger": "__HELP__"
            }

        import sys
        self.reverse = {}
            

        self.cfg = switches_config or {}
        self.alias_to_name = {}
        self.name_to_aliases = {}
        self._raw = {}        # {Name: [tokens...]}
        self._processed = {}  # {Name: [tokens...]} (after trigger)

        # build alias maps
        for name, meta in self.cfg.items():
            aliases = self._parse_aliases(meta.get("switches", []))
            self.name_to_aliases[name] = aliases
            for a in aliases:
                self.alias_to_name[a] = name



        # parse immediately (default: sys.argv[1:])
        if argv is None:
            argv = sys.argv[1:]
        self.parse(argv)
        self._buildReverse()


    def _buildReverse(self):
        """
        Build reverse lookup:
            { '-f': 'Files', '--files': 'Files' }
        """
        self.reverse = {}
        for name, aliases in self.name_to_aliases.items():
            for a in aliases:
                self.reverse[a] = name


    # ---------- your original switch parser (kept minimal) ----------
    @staticmethod
    def getSwitches(allowed_switches, argv):
        # allowed_switches: string or list
        if isinstance(allowed_switches, str):
            s = allowed_switches.replace(",", " ")
            while "  " in s:
                s = s.replace("  ", " ")
            allowed = set(s.split())
        else:
            allowed = set(allowed_switches)

        # argv: string or list
        if isinstance(argv, str):
            a = argv.replace(",", " ")
            while "  " in a:
                a = a.replace("  ", " ")
            argv = a.split()

        out = {}
        current = None
        for token in argv:
            if token in allowed:
                current = token
                out.setdefault(current, [])
            elif current is not None:
                out[current].append(token)
        return out

    # ---------- helpers ----------
    @staticmethod
    def _parse_aliases(switches_field):
        """
        switches_field can be:
          - list like ["-f, --f, --files", "-F"]
          - string like "-f, --f, --files"
        returns list of clean aliases: ["-f","--f","--files"]
        """
        if isinstance(switches_field, str):
            items = [switches_field]
        else:
            items = list(switches_field)

        aliases = []
        for item in items:
            if not item:
                continue
            txt = str(item).replace(",", " ")
            while "  " in txt:
                txt = txt.replace("  ", " ")
            for a in txt.split():
                if a and a not in aliases:
                    aliases.append(a)
        return aliases

    # ---------- public API ----------
    def parse(self, argv):
        """Re-parse a command (string or list)."""
        self._raw = {}
        self._processed = {}

        allowed_aliases = list(self.alias_to_name.keys())
        parsed = self.getSwitches(allowed_aliases, argv)

        # merge alias hits into logical switch names
        for alias, vals in parsed.items():
            name = self.alias_to_name.get(alias)
            if name is None:
                continue
            self._raw.setdefault(name, []).extend(vals)

        # apply triggers (if any)
        for name, vals in self._raw.items():
            meta = self.cfg.get(name, {})
            trig = meta.get("trigger")
            if trig == "__HELP__":
                # optional topic: --help Files
                topic = None
                if vals and len(vals):
                    topic = vals

                help_text = self.Help(topic)

                # store the help text so caller can retrieve it
                self._processed[name] = [help_text]

                # also print it (simple CLI behavior)
                try:
                    print(help_text)
                except Exception:
                    pass

                return self


            if callable(trig):
                out_vals = []
                for v in vals:
                    r = trig(v)
                    if r is None:
                        out_vals.append(v)
                    elif isinstance(r, (list, tuple)):
                        out_vals.extend(list(r))
                    else:
                        out_vals.append(r)
                self._processed[name] = out_vals
            else:
                self._processed[name] = list(vals)

        return self

    def isActive(self, name: str) -> bool:
        return name in self._raw and len(self._raw[name]) >= 0  # present = active (even if no values)

    def values(self, name: str, processed: bool = True):
        d = self._processed if processed else self._raw
        return d.get(name, [])
    
    def len(self, name, switch=None, i=-1, processed=True):
        if not self.isActive(name):
            return -1
        if not switch is None:
            return len(self.Values(name, switch, i))
        else:
            return len(self.values(name, processed=processed))
    
    def value(self, name, i=0, processed=True):
        d = self._processed if processed else self._raw
        if not d.get(name, False):
            return ''
        if not self.isActive(name):
            return ''
        if i == -1:
            return ' '.join(self.values(name, processed=processed))
        else:
            if i < len(self.values(name, processed=processed)):
                return self.values(name, processed=processed)[i]
            else:
                return ''
    def Values(self, name, switch=None, i=-1):
        """
        Values("Files")                -> all values for Files
        Values("Files", "-in")         -> values only for -in
        Values("Files", "-in", 0)      -> first value for -in
        Any error -> []
        """
        try:
            if name not in self._raw:
                return []

            # no specific switch requested → return all
            if switch is None:
                vals = list(self._raw.get(name, []))
            else:
                # ensure switch belongs to this logical name
                if self.reverse.get(switch) != name:
                    return []

                parsed = self.getSwitches([switch], self._argv)
                vals = parsed.get(switch, [])

            # index access if requested
            if i > -1:
                try:
                    return vals[i]
                except Exception:
                    return []

            return vals
        except Exception:
            return []




    def used(self):
        """Which logical switches were used."""
        return sorted(self._raw.keys())


    def normalizeSwitches(self, definition):
        """
        Accepts:
        - full config dict (passes through)
        - shorthand dict: {"Files":"-f"} or {"Files":["-f","--files"]}
        - string: "Files: -f --files | Verbose: -v"
        - list: ["Files: -f --files", "Verbose: -v"]

        Returns canonical dict:
        {"Files": {"switches": ["-f --files"]}, ...}
        """

        # ---- PASS-THROUGH: already canonical/full config ----
        if isinstance(definition, dict):
            # If values are dicts and already have "switches", do nothing.
            if all(isinstance(v, dict) and "switches" in v for v in definition.values()):
                return definition

        out = {}

        # ---- normalize to iterable of clauses ----
        if isinstance(definition, dict):
            items = []
            for k, v in definition.items():
                if isinstance(v, (list, tuple)):
                    items.append(f"{k}: {' '.join(map(str, v))}")
                else:
                    items.append(f"{k}: {v}")
        elif isinstance(definition, str):
            items = [x.strip() for x in definition.split("|") if x.strip()]
        elif isinstance(definition, (list, tuple)):
            items = []
            for x in definition:
                if isinstance(x, str):
                    items.extend(y.strip() for y in x.split("|") if y.strip())
                elif isinstance(x, dict):
                    for k, v in x.items():
                        if isinstance(v, (list, tuple)):
                            items.append(f"{k}: {' '.join(map(str, v))}")
                        else:
                            items.append(f"{k}: {v}")
        else:
            raise TypeError("Unsupported switch definition format")

        # ---- parse clauses ----
        for item in items:
            if ":" not in item:
                continue

            name, switches = item.split(":", 1)
            name = name.strip()

            switches = switches.replace(",", " ")
            while "  " in switches:
                switches = switches.replace("  ", " ")
            switches = switches.strip()

            if not name:
                continue

            out[name] = {"switches": [switches] if switches else []}

        return out


    def Help(self, name=None):
        """
        Return help text for switches.

        name can be:
        - None                  -> all switches + all usage lines
        - "Files"               -> Files help + usage lines containing any Files alias
        - "Files Ago"           -> multiple
        - ["Files","Ago"]       -> multiple
        - "Files|Ago,Verbose"   -> multiple

        Usage filtering is simple:
            for sw in aliases:
                if ' '+sw+' ' in ' '+line+' ':
                    include line

        Any error -> []
        """
        try:
            # ---- normalize requested logical names into a set (or None for "all") ----
            names = None
            if name is None or name == "":
                names = None
            elif isinstance(name, (list, tuple, set)):
                names = set(str(x).strip() for x in name if str(x).strip())
                if not names:
                    names = None
            else:
                s = str(name).replace(",", " ").replace("|", " ")
                while "  " in s:
                    s = s.replace("  ", " ")
                names = set(x.strip() for x in s.split() if x.strip())
                if not names:
                    names = None

            # ---- build switch help text ----
            lines = []
            for key, meta in self.cfg.items():
                if names is not None and key not in names:
                    continue

                aliases = self.name_to_aliases.get(key, [])
                desc = meta.get("description", "")
                example = meta.get("example", "")

                lines.append(f"{key}:")
                if aliases:
                    lines.append(f"  switches: {' '.join(aliases)}")
                if desc:
                    lines.append(f"  desc:     {desc}")
                if example:
                    lines.append(f"  example:  {example}")
                lines.append("")

            help_text = "\n".join(lines).rstrip()

            # ---- usage output (filtered by aliases if names specified) ----
            usage = getattr(self, "usage", [])
            usage_lines = []

            if usage:
                if names is None:
                    # no filter -> print all usage
                    for line in usage:
                        line = str(line)
                        if line.strip():
                            usage_lines.append(line)
                            try:
                                print(line)
                            except Exception:
                                pass
                else:
                    # filter by aliases for requested logical names
                    aliases = []
                    for n in names:
                        for a in self.name_to_aliases.get(n, []):
                            aliases.append(a)

                    for line in usage:
                        line = str(line)
                        L = " " + line + " "
                        hit = False
                        for sw in aliases:
                            if (" " + sw + " ") in L:
                                hit = True
                                break
                        if hit and line.strip():
                            usage_lines.append(line)
                            try:
                                print(line)
                            except Exception:
                                pass

            usage_text = "\n".join(usage_lines).rstrip()

            # ---- decide what to return ----
            if help_text and usage_text:
                return (help_text + "\n\n" + usage_text).rstrip()
            if help_text:
                return help_text
            if usage_text:
                return usage_text
            return ""
        except Exception:
            return []




'''
# ---------- example ----------
def timeAgoTrigger(value):
    # placeholder: just pass-through for now
    return value


switches = {
    "Files": {
        "type": "trigger",
        "switches": ["-f, --f, --files"],
        "description": "Trigger for file paths",
        "example": "--files file1.txt file2.txt",
    },
    "Ago": {
        "type": "trigger",
        "switches": ["-ago --a"],
        "description": "Trigger for time-based filtering",
        "example": "--a 7d",
        "trigger": timeAgoTrigger,
    }
}



cmd = "app --f file1.txt file2.txt --a 7d"
sw = SimpleSwitches(switches, cmd)

if sw.isActive("Files"):
    for path in sw.values("Files"):
        print(f"File: {path}")
'''




'''
exit()


py

from SimpleSwitches import SimpleSwitches

sw = SimpleSwitches("Files: -f", "app -f fi.txt -f fi2.txt")


sw = SimpleSwitches("Files: -f", "app -f fi.txt -f fi2.txt --help")

sw = SimpleSwitches("Files: -f", "app -f fi.txt")

sw = SimpleSwitches("Files: -in -out", "app -in song.mp4 -out song.mp3")









exit()


py

from SimpleSwitches import SimpleSwitches

switches = { "Files": { "type": "trigger", "switches": ["-f, --f, --files"], "description": "Trigger for file paths", "example": "--files file1.txt file2.txt" }, "Ago": { "type": "trigger", "switches": ["-ago --a"], "description": "Trigger for time-based filtering", "example": "--a 7d" } }

sw = SimpleSwitches(switches, "app -f fi.txt -f fi2.txt --help")


'''
