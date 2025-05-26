# https://chatgpt.com/c/67cfa8dd-0818-800a-8d75-87096628d08a

import yaml
class MdFig:
    LANGUAGE_MAP = {
        "js": "JavaScript",
        "py": "Python",
        "php": "PHP",
        "java": "Java",
        "c": "C",
        "ruby": "Ruby",
        "sql": "SQL",
        "swift": "Swift",
        "html": "HTML"
    }

    def __init__(self, md='', title='###', dic=False, autoDic=True, context=False):
        self.md = md.split('\n') if isinstance(md, str) else md
        self.title = title
        self.dic = dic
        self.autoDic = autoDic
        self.context = context
        self.code = {}
        self.current_section = None
        self.current_snippet = []
        self.is_snippet = False
        self.snippet_language = None
        self.parse()

    def parse(self):
        for line in self.md:
            stripped_line = line.strip()

            if stripped_line.startswith(self.title):
                self.current_section = stripped_line[len(self.title):].strip()
                if not self.current_section:
                    self.current_section = "untitled"
                continue

            if stripped_line.startswith('~~~'):
                if self.is_snippet:
                    self.store_snippet()
                    self.is_snippet = False
                    self.snippet_language = None
                else:
                    self.is_snippet = True
                    lang = stripped_line[3:].lower() if len(stripped_line) > 3 else None
                    self.snippet_language = self.LANGUAGE_MAP.get(lang, lang)
            elif self.is_snippet:
                self.current_snippet.append(line)

        if self.is_snippet:
            self.store_snippet()

    def store_snippet(self):
        if self.current_section:
            snippet_value = '\n'.join(self.current_snippet)
            snippet_metadata = {}
            
            if self.dic or self.autoDic:
                self.code[self.current_section] = {
                    "original": snippet_value,
                    "code": snippet_value.strip(),
                    "language": self.snippet_language,
                    "iter": [],
                    "metadata": snippet_metadata,
                }
            else:
                self.code[self.current_section] = snippet_value
        
        self.current_snippet = []

    def get_code(self):
        return self.code
