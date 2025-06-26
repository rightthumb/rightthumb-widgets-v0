import yaml
import re

class MdFig:
    LANGUAGE_MAP = {
        "js": "JavaScript",
        "py": "Python",
        "php": "PHP",
        "java": "Java",
        "c": "C",
        "cpp": "C++",
        "cs": "C#",
        "ruby": "Ruby",
        "sql": "SQL",
        "swift": "Swift",
        "html": "HTML",
        "xml": "XML",
        "yml": "YAML",
        "yaml": "YAML",
        "css": "CSS",
        "scss": "SCSS",
        "sass": "SASS",
        "rs": "Rust",
        "ada": "Ada",
        "spark": "SPARK",
        "go": "Go",
        "ts": "TypeScript",
        "sh": "Shell",
        "bash": "Bash",
        "zsh": "Zsh",
        "bat": "Batch",
        "cmd": "Batch",
        "ps1": "PowerShell",
        "psm1": "PowerShell",
        "dart": "Dart",
        "kotlin": "Kotlin",
        "perl": "Perl",
        "lua": "Lua",
        "r": "R",
        "json": "JSON",
        "toml": "TOML",
        "ini": "INI",
        "makefile": "Makefile",
        "dockerfile": "Dockerfile",
        "gitignore": "GitIgnore",
        "cmake": "CMake",
        "asm": "Assembly",
        "nasm": "NASM",
        "arm": "ARM Assembly",
        "verilog": "Verilog",
        "vhdl": "VHDL"
    }

    ITER_COMMENTS = {
        "py": ["#"],
        "php": ["//", "/* {} */"],
        "js": ["//", "/* {} */"],
        "java": ["//", "/* {} */"],
        "c": ["//", "/* {} */"],
        "cpp": ["//", "/* {} */"],
        "cs": ["//", "/* {} */"],
        "ruby": ["#"],
        "sql": ["--", "/* {} */"],
        "yml": ["#"],
        "yaml": ["#"],
        "css": ["/* {} */"],
        "scss": ["//", "/* {} */"],
        "sass": ["//"],
        "rs": ["//"],
        "ada": ["--"],
        "spark": ["--"],
        "go": ["//"],
        "ts": ["//", "/* {} */"],
        "sh": ["#"],
        "bash": ["#"],
        "zsh": ["#"],
        "bat": ["REM", "::"],
        "cmd": ["REM", "::"],
        "ps1": ["#"],
        "psm1": ["#"],
        "dart": ["//"],
        "kotlin": ["//"],
        "perl": ["#"],
        "lua": ["--"],
        "r": ["#"],
        "json": ["//"],
        "toml": ["#"],
        "ini": ["#"],
        "makefile": ["#"],
        "dockerfile": ["#"],
        "gitignore": ["#"],
        "cmake": ["#"],
        "asm": [";"],
        "nasm": [";"],
        "arm": [";"],
        "verilog": ["//"],
        "vhdl": ["--"]
    }

    def __init__(self, md='', title='###'):
        self.md = md.split('\n') if isinstance(md, str) else md
        self.title = title
        self.code = {}
        self.structure = {}
        self.parents = {}
        self.categories = {}
        self.languages = {}
        self.current_section = None
        self.current_category = None
        self.current_snippet = []
        self.is_snippet = False
        self.snippet_language = None
        self.iter_items = []
        self.file_title = ""
        self.parse()

    def parse(self):
        inside_iter = False
        current_iter_code = []
        iter_subject = None
        current_category = None
        section_hierarchy = []
        iter_start = None

        for line in self.md:
            stripped_line = line.strip()

            if stripped_line.startswith('#') and not self.file_title:
                self.file_title = stripped_line[1:].strip()
                continue
            
            match = re.match(r'^(#+)\s+(.*)', stripped_line)
            if match:
                level = len(match.group(1))
                title = match.group(2)

                while len(section_hierarchy) >= level:
                    section_hierarchy.pop()
                section_hierarchy.append(title)

                clean_title = self.clean_iter_subject(title)
                self.structure[clean_title] = {
                    "level": level,
                    "parent": section_hierarchy[-2] if len(section_hierarchy) > 1 else None,
                    "children": []
                }

                if len(section_hierarchy) > 1:
                    parent = self.clean_iter_subject(section_hierarchy[-2])
                    self.structure[parent]["children"].append(clean_title)

                if level == 2:
                    current_category = clean_title
                    self.categories[clean_title] = []
                elif level >= 3:
                    self.current_section = clean_title
                    self.parents[clean_title] = [self.clean_iter_subject(p) for p in section_hierarchy[:-1]]
                continue
            
            if stripped_line.startswith('~~~'):
                if self.is_snippet:
                    self.store_snippet(current_category)
                    self.is_snippet = False
                    self.snippet_language = None
                else:
                    self.is_snippet = True
                    lang = stripped_line[3:].lower() if len(stripped_line) > 3 else None
                    self.snippet_language = self.LANGUAGE_MAP.get(lang, lang)
                    self.current_snippet = []
                continue
            
            if self.is_snippet:
                if "iter:Start:" in stripped_line:
                    inside_iter = True
                    iter_subject = self.clean_iter_subject(stripped_line)
                    iter_start = stripped_line
                    current_iter_code = []
                    continue
                elif "iter:End:" in stripped_line:
                    inside_iter = False
                    iter_code_only = self._extract_inner_code(current_iter_code)
                    self.iter_items.append({
                        "Subject": iter_subject,
                        "Replace": {
                            "Start": iter_start,
                            "End": stripped_line
                        },
                        "Code": iter_code_only
                    })
                    current_iter_code = []
                    iter_start = None
                    continue
                elif inside_iter:
                    current_iter_code.append(line)
                    continue
                
                self.current_snippet.append(line)

        if self.is_snippet:
            self.store_snippet(current_category)

    def clean_iter_subject(self, line):
        subject = re.sub(r'iter:\w+:', '', line).strip()
        subject = re.sub(r'[*/#-]+$', '', subject).strip()
        return subject

    def _extract_inner_code(self, snippet_lines):
        return '\n'.join(snippet_lines).strip()

    def store_snippet(self, category):
        if self.current_snippet:
            snippet_value = '\n'.join(self.current_snippet)

            if self.snippet_language:
                if self.snippet_language not in self.languages:
                    self.languages[self.snippet_language] = {"count": 0, "keys": []}
                self.languages[self.snippet_language]["count"] += 1
                self.languages[self.snippet_language]["keys"].append(self.current_section)

            self.code[self.current_section] = {
                "category": category,
                "original": snippet_value,
                "code": snippet_value,
                "language": self.snippet_language,
                "iter": self.iter_items,
                "metadata": {},
            }

            if category:
                self.categories[category].append(self.current_section)
        
        self.current_snippet = []
        self.iter_items = []

    def get_code(self):
        return {
            "mdFig": {
                "label": self.file_title,
                "languages": self.languages,
                "categories": self.categories,
                "structure": self.structure,
                "parents": self.parents,
            },
            "snippets": self.code
        }
