import yaml
import re
import json

class MdFig:
    LANGUAGE_MAP = {
        "js": "JavaScript", "py": "Python", "php": "PHP", "java": "Java", "c": "C",
        "cpp": "C++", "cs": "C#", "ruby": "Ruby", "sql": "SQL", "swift": "Swift",
        "html": "HTML", "xml": "XML", "yml": "YAML", "yaml": "YAML", "css": "CSS",
        "scss": "SCSS", "sass": "SASS", "rs": "Rust", "ada": "Ada", "spark": "SPARK",
        "go": "Go", "ts": "TypeScript", "sh": "Shell", "bash": "Bash", "zsh": "Zsh",
        "bat": "Batch", "cmd": "Batch", "ps1": "PowerShell", "psm1": "PowerShell",
        "dart": "Dart", "kotlin": "Kotlin", "perl": "Perl", "lua": "Lua", "r": "R",
        "json": "JSON", "toml": "TOML", "ini": "INI", "makefile": "Makefile",
        "dockerfile": "Dockerfile", "gitignore": "GitIgnore", "cmake": "CMake",
        "asm": "Assembly", "nasm": "NASM", "arm": "ARM Assembly", "verilog": "Verilog",
        "vhdl": "VHDL"
    }

    ITER_COMMENTS = {
        "py": "#", "php": "//", "js": "//", "java": "//", "c": "//", "cpp": "//",
        "cs": "//", "ruby": "#", "sql": "--", "yml": "#", "yaml": "#", "css": "/*",
        "scss": "//", "sass": "//", "rs": "//", "ada": "--", "spark": "--",
        "go": "//", "ts": "//", "sh": "#", "bash": "#", "zsh": "#", "bat": "REM",
        "cmd": "REM", "ps1": "#", "psm1": "#", "dart": "//", "kotlin": "//",
        "perl": "#", "lua": "--", "r": "#", "json": "//", "toml": "#", "ini": "#",
        "makefile": "#", "dockerfile": "#", "gitignore": "#", "cmake": "#",
        "asm": ";", "nasm": ";", "arm": ";", "verilog": "//", "vhdl": "--",
        "swift": "//"  # ✅ Fix: Add Swift support
    }


    def __init__(self, md=''):
        self.md = md.split('\n') if isinstance(md, str) else md
        self.structure = {}
        self.parents = {}
        self.categories = {}
        self.languages = {}
        self.snippets = {}
        self.file_label = "Comprehensive Configuration File"

        self.current_section = None
        self.current_snippet = []
        self.is_snippet = False
        self.snippet_language = None
        self.current_iter = None
        self.active_iters = {}
        self.current_code_block = []
        self.snippet_key = None

        self.parse()

    def parse(self):
        snippet_start_pattern = re.compile(r"^~~~(\w+)")
        snippet_end_pattern = re.compile(r"^~~~$")
        iter_start_pattern = re.compile(r"(#|//|--|REM|\*/)\s*iter:Start:(\w+)")
        iter_end_pattern = re.compile(r"(#|//|--|REM|\*/)\s*iter:End:(\w+)")
        section_pattern = re.compile(r"^#{2,}\s+(.+)")

        for line in self.md:
            line = line.rstrip()

            # Detect Sections (## Section)
            section_match = section_pattern.match(line)
            if section_match and not self.is_snippet:
                self.current_section = section_match.group(1).title()
                self.structure[self.current_section] = []
                continue

            # Detect Snippet Start (~~~language)
            snippet_match = snippet_start_pattern.match(line)
            if snippet_match:
                self.is_snippet = True
                self.snippet_language = snippet_match.group(1)
                self.current_snippet = []
                self.current_code_block = []
                self.active_iters = {}  # Reset iter tracking
                continue

            # Detect Snippet End (~~~)
            if snippet_end_pattern.match(line):
                if self.is_snippet and self.snippet_language:
                    lang_name = self.LANGUAGE_MAP.get(self.snippet_language, self.snippet_language).title()
                    self.snippet_key = f"{lang_name} Snippet"

                    if self.current_section:
                        self.structure[self.current_section].append(self.snippet_key)
                        self.parents[self.snippet_key] = [self.current_section]

                    if lang_name not in self.languages:
                        self.languages[lang_name] = {"Count": 0, "Keys": []}
                    self.languages[lang_name]["Count"] += 1
                    self.languages[lang_name]["Keys"].append(self.snippet_key)

                    cleaned_code = "\n".join([
                        line for line in self.current_code_block
                        if not (line.strip().startswith("#") and "iter:" not in line)
                    ])

                    original_code = "\n".join(self.current_code_block)
                    self.snippets[self.snippet_key] = {
                        "Category": self.current_section,
                        "Original": original_code,
                        "Code": cleaned_code,
                        "Language": lang_name,
                        "Iter": list(self.active_iters.values()),  # Capture all iter blocks
                        "Metadata": {}
                    }

                self.is_snippet = False
                self.snippet_language = None
                continue

            # Detect Iter Start
            iter_start_match = iter_start_pattern.search(line)
            if iter_start_match and self.is_snippet and self.snippet_key:
                iter_name = iter_start_match.group(2)
                self.current_iter = iter_name
                self.active_iters[iter_name] = {
                    "Reference": f"{self.ITER_COMMENTS[self.snippet_language]} iter:{iter_name}",
                    "Subject": iter_name,
                    "Replace": {
                        "Start": line.strip(),
                        "End": f"END-{iter_name}"
                    },
                    "Code": []
                }
                continue

            # Detect Iter End
            iter_end_match = iter_end_pattern.search(line)
            if iter_end_match and self.is_snippet and self.snippet_key:
                iter_name = iter_end_match.group(2)
                if iter_name in self.active_iters:
                    self.active_iters[iter_name]["Replace"]["End"] = line.strip()
                    self.active_iters[iter_name]["Code"] = "\n".join(self.active_iters[iter_name]["Code"])
                self.current_iter = None
                continue

            # Capture Iter Content
            if self.is_snippet and self.current_iter and self.snippet_key:
                self.active_iters[self.current_iter]["Code"].append(line.strip())

            # Store Full Code
            if self.is_snippet:
                self.current_code_block.append(line)

        # Convert iter `Code` list to string
        for key in self.active_iters:
            self.active_iters[key]["Code"] = "\n".join(self.active_iters[key]["Code"])



    def get_json(self):
        return json.dumps(self.get_code(), indent=4)

# Example Usage:
# parser = MdFig(your_markdown_content)
# print(parser.get_json())
