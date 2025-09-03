import os
# import sys; sys.exit(0)
from typing import Optional, Union, List

from pygments import highlight
from pygments.lexers import guess_lexer, get_all_lexers, get_lexer_by_name
from pygments.util import ClassNotFound
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter, TerminalFormatter

# These may not exist on very old Pygments; we guard the imports.
try:
	from pygments.formatters import Terminal256Formatter
except Exception:
	Terminal256Formatter = None

try:
	from pygments.formatters import TerminalTrueColorFormatter
except Exception:
	TerminalTrueColorFormatter = None


class CodeColor:
	def __init__(
		self,
		style: str = 'one-dark',
		output: str = 'terminal',
		prefer_truecolor: bool = True,
		prefer_256: bool = True,
	):
		self.style = style
		self.output_format = output.lower()
		self.prefer_truecolor = prefer_truecolor
		self.prefer_256 = prefer_256
		self._validate_style()
		self.formatter = self._get_formatter()
		self.supported_languages = self._get_supported_languages()

	# ---------- capability detection ----------
	@staticmethod
	def _supports_truecolor() -> bool:
		# Common indicators across terminals
		ct = os.getenv('COLORTERM', '').lower()
		return 'truecolor' in ct or '24bit' in ct

	@staticmethod
	def _supports_256() -> bool:
		term = os.getenv('TERM', '').lower()
		return '256color' in term or 'xterm' in term or 'screen-256color' in term

	# ---------- setup ----------
	def _validate_style(self) -> None:
		available = set(get_all_styles())
		if self.style not in available:
			raise ValueError(f"Invalid style '{self.style}'. Available styles: {sorted(available)}")

	def _get_formatter(self):
		if self.output_format == 'html':
			return HtmlFormatter(style=self.style)

		# terminal path: try truecolor -> 256 -> 16-color
		if self.prefer_truecolor and TerminalTrueColorFormatter and self._supports_truecolor():
			return TerminalTrueColorFormatter(style=self.style)

		if self.prefer_256 and Terminal256Formatter and self._supports_256():
			return Terminal256Formatter(style=self.style)

		return TerminalFormatter(style=self.style)


	def _get_supported_languages(self) -> List[str]:
		global ALL_LANGUAGES
		return ALL_LANGUAGES
	
	# def _get_supported_languages(self) -> List[str]:
	# 	return list({alias for lexer in get_all_lexers() for alias in lexer[1]})


	# ---------- API ----------
	def detect_language(self, code: str) -> str:
		try:
			return guess_lexer(code).name
		except ClassNotFound:
			return "unknown"

	def color(self, code: str, language: Optional[str] = None) -> str:
		return self.highlight(code, language)

	def highlight(self, code: str, language: Optional[str] = None) -> str:
		try:
			lexer = get_lexer_by_name(language) if language else guess_lexer(code)
			return highlight(code, lexer, self.formatter)
		except ClassNotFound:
			return code

	def set_style(self, new_style: str) -> None:
		self.style = new_style
		self._validate_style()
		self.formatter = self._get_formatter()

	def set_output_format(self, format: str) -> None:
		self.output_format = format.lower()
		self.formatter = self._get_formatter()

	def list_languages(self) -> List[str]:
		return sorted(self.supported_languages)

	def list_styles(self) -> List[str]:
		return list(get_all_styles())

	def print_languages(self) -> None:
		print("Supported languages:")
		for lang in sorted(self.supported_languages):
			print(f"- {lang}")

	def print_styles(self) -> None:
		print("Available styles:")
		for style in self.list_styles():
			print(f"- {style}")

	def get_css(self) -> str:
		if not isinstance(self.formatter, HtmlFormatter):
			raise RuntimeError("CSS is only available for HTML output format")
		return self.formatter.get_style_defs()



	def analyze(self, code: str, language: str = None):
		"""Return a list of token dictionaries with type and value."""
		from pygments import lex # type: ignore
		lexer = get_lexer_by_name(language) if language else guess_lexer(code)
		return [
			{"type": str(tok_type), "value": tok_value}
			for tok_type, tok_value in lex(code, lexer)
		]















ALL_LANGUAGES = [
    "abap", "amdgpu", "apl", "abnf",
    "actionscript3", "as3", "actionscript", "as",
    "ada", "ada95", "ada2005", "adl", "agda", "aheui", "alloy",
    "ambienttalk", "ambienttalk/2", "at", "ampl",
    "html+ng2", "ng2",
    "antlr-actionscript", "antlr-as", "antlr-csharp", "antlr-c#", "antlr-cpp",
    "antlr-java", "antlr", "antlr-objc", "antlr-perl", "antlr-python", "antlr-ruby", "antlr-rb",
    "apacheconf", "aconf", "apache",
    "applescript", "arduino", "arrow", "arturo", "art",
    "asc", "pem", "asn1", "aspectj", "asymptote", "asy",
    "augeas", "autoit", "autohotkey", "ahk",
    "awk", "gawk", "mawk", "nawk",
    "bbcbasic", "bbcode", "bc", "bqn",
    "bst", "bst-pybtex", "bare", "basemake",
    "bash", "sh", "ksh", "zsh", "shell", "openrc",
    "console", "shell-session",
    "batch", "bat", "dosbatch", "winbatch",
    "bdd", "befunge", "berry", "be",
    "bibtex", "bib",
    "blitzbasic", "b3d", "bplus",
    "blitzmax", "bmax",
    "blueprint", "bnf", "boa", "boo", "boogie",
    "brainfuck", "bf",
    "bugs", "winbugs", "openbugs",
    "camkes", "idl4",
    "c", "cmake", "c-objdump", "cpsa",
    "css+ul4", "aspx-cs",
    "csharp", "c#", "cs",
    "ca65", "cadl", "capdl", "capnp", "carbon", "cbmbas", "cddl",
    "ceylon", "cfengine3", "cf3",
    "chaiscript", "chai",
    "chapel", "chpl", "charmci",
    "html+cheetah", "html+spitfire", "htmlcheetah",
    "javascript+cheetah", "js+cheetah", "javascript+spitfire", "js+spitfire",
    "cheetah", "spitfire",
    "xml+cheetah", "xml+spitfire",
    "cirru", "clay", "clean", "clojure", "clj",
    "clojurescript", "cljs",
    "cobolfree", "cobol",
    "codeql", "ql",
    "coffeescript", "coffee-script", "coffee",
    "cfc", "cfm", "cfs",
    "comal", "comal80",
    "common-lisp", "cl", "lisp",
    "componentpascal", "cp",
    "coq", "cplint",
    "cpp", "c++",
    "cpp-objdump", "c++-objdumb", "cxx-objdump",
    "crmsh", "pcmk",
    "croc", "cryptol", "cry", "cr", "crystal",
    "csound-document", "csound-csd",
    "csound", "csound-orc",
    "csound-score", "csound-sco",
    "css+django", "css+jinja",
    "css+ruby", "css+erb",
    "css+genshitext", "css+genshi",
    "css", "css+php", "css+smarty",
    "cuda", "cu",
    "cypher", "cython", "pyx", "pyrex",
    "d", "d-objdump", "dpatch", "dart", "dasm16", "dax",
    "debcontrol", "control",
    "debian.sources",
    "delphi", "pas", "pascal", "objectpascal",
    "desktop", "devicetree", "dts",
    "dg", "diff", "udiff",
    "django", "jinja",
    "zone", "docker", "dockerfile", "dtd",
    "duel", "jbst", "jsonml+bst",
    "dylan-console", "dylan-repl",
    "dylan", "dylan-lid", "lid",
    "ecl", "ec", "earl-grey", "earlgrey", "eg",
    "easytrieve", "ebnf", "eiffel", "iex",
    "elixir", "ex", "exs",
    "elm", "elpi",
    "emacs-lisp", "elisp", "emacs",
    "email", "eml",
    "erb", "erlang", "erl",
    "html+evoque", "evoque", "xml+evoque",
    "execline", "ezhil",
    "fsharp", "f#",
    "fstar", "factor", "fancy", "fy", "fan",
    "felix", "flx", "fennel", "fnl",
    "fift", "fif",
    "fish", "fishshell",
    "flatline", "floscript", "flo",
    "forth", "fortranfixed", "fortran", "f90",
    "foxpro", "vfp", "clipper", "xbase",
    "freefem", "func", "fc", "futhark",
    "gap-console", "gap-repl", "gap",
    "gdscript", "gd", "glsl", "gsql",
    "gas", "asm", "gcode",
    "genshi", "kid", "xml+genshi", "xml+kid",
    "genshitext", "pot", "po",
    "gherkin", "cucumber",
    "gleam", "gnuplot", "go", "golang",
    "golo", "gooddata-cl", "googlesql", "zetasql",
    "gosu", "gst",
    "graphql", "graphviz", "dot",
    "groff", "nroff", "man",
    "groovy", "hlsl", "html+ul4", "haml",
    "html+handlebars", "handlebars",
    "hare", "haskell", "hs",
    "haxe", "hxsl", "hx",
    "hexdump", "hsail", "hsa",
    "hspec", "html+django", "html+jinja", "htmldjango",
    "html+genshi", "html+kid", "html",
    "html+php", "html+smarty", "http",
    "haxeml", "hxml", "hylang", "hy", "hybris",
    "idl", "icon", "idris", "idr",
    "igor", "igorpro",
    "inform6", "i6", "i6t",
    "inform7", "i7", "ini", "cfg", "dosini",
    "io", "ioke", "ik",
    "irc", "isabelle", "j", "jmespath", "jp",
    "jslt", "jags", "janet", "jasmin", "jasminxt",
    "java",
    "javascript+django", "js+django", "javascript+jinja", "js+jinja",
    "javascript+ruby", "js+ruby", "javascript+erb", "js+erb",
    "js+genshitext", "js+genshi", "javascript+genshitext", "javascript+genshi",
    "javascript", "js",
    "javascript+php", "js+php",
    "javascript+smarty", "js+smarty",
    "js+ul4", "jcl", "jsgf",
    "json5", "jsonld", "json-ld", "json", "json-object", "jsonnet",
    "jsp", "jsx", "react", "jlcon", "julia-repl", "julia", "jl", "juttle",
    "k", "kal", "kconfig", "menuconfig", "linux-config", "kernel-config",
    "kmsg", "dmesg", "koka", "kotlin", "kuin", "kql", "kusto",
    "lsl", "css+lasso", "html+lasso", "javascript+lasso", "js+lasso",
    "lasso", "lassoscript", "xml+lasso",
    "ldapconf", "ldaprc", "ldif",
    "lean", "lean3", "lean4",
    "less", "lighttpd", "lighty",
    "lilypond", "limbo", "liquid", "literate-agda", "lagda",
    "literate-cryptol", "lcryptol", "lcry",
    "literate-haskell", "lhaskell", "lhs",
    "literate-idris", "lidris", "lidr",
    "livescript", "live-script", "llvm", "llvm-mir-body", "llvm-mir",
    "logos", "logtalk", "lua", "luau", "mcfunction", "mcf",
    "mcschema", "mime", "mips", "moocode", "moo", "doscon",
    "macaulay2", "make", "makefile", "mf", "bsdmake",
    "css+mako", "html+mako", "javascript+mako", "js+mako", "mako", "xml+mako",
    "maple", "maql", "markdown", "md", "mask", "mason",
    "mathematica", "mma", "nb", "matlab", "matlabsession",
    "maxima", "macsyma", "meson", "meson.build",
    "minid", "miniscript", "ms",
    "modelica", "modula2", "m2", "trac-wiki", "moin",
    "mojo", "🔥", "monkey", "monte",
    "moonscript", "moon", "mosel",
    "css+mozpreproc", "mozhashpreproc", "javascript+mozpreproc",
    "mozpercentpreproc", "xul+mozpreproc",
    "mql", "mq4", "mq5", "mql4", "mql5",
    "mscgen", "msc", "mupad", "mxml", "mysql",
    "css+myghty", "html+myghty", "javascript+myghty", "js+myghty", "myghty", "xml+myghty",
    "ncl", "nsis", "nsi", "nsh", "nasm", "objdump-nasm",
    "nemerle", "nesc", "nestedtext", "nt",
    "newlisp", "newspeak", "nginx", "nimrod", "nim", "nit", "nixos", "nix",
    "nodejsrepl", "notmuch", "nusmv", "numpy", "numba_ir", "numbair",
    "objdump", "objective-c", "objectivec", "obj-c", "objc",
    "objective-c++", "objectivec++", "obj-c++", "objc++",
    "objective-j", "objectivej", "obj-j", "objj",
    "ocaml", "octave", "odin", "omg-idl", "ooc", "opa",
    "openedge", "abl", "progress",
    "openscad", "org", "orgmode", "org-mode",
    "output", "pacmanconf", "pan", "parasail", "pawn",
    "pddl", "peg", "perl6", "pl6", "raku",
    "perl", "pl", "phix", "php", "php3", "php4", "php5",
    "pig", "pike", "pkgconfig", "plpgsql", "pointless", "pony",
    "portugol", "postscript", "postscr",
    "psql", "postgresql-console", "postgres-console",
    "postgres-explain", "postgresql", "postgres",
    "pov", "powershell", "pwsh", "posh", "ps1", "psm1",
    "pwsh-session", "ps1con", "praat", "procfile",
    "prolog", "promql", "promela", "properties", "jproperties",
    "protobuf", "proto", "prql", "psysh", "ptx",
    "pug", "jade", "puppet", "pypylog", "pypy",
    "python2", "py2", "py2tb", "pycon", "python-console",
    "python", "py", "sage", "python3", "py3", "bazel", "starlark", "pyi",
    "pytb", "py3tb", "py+ul4", "qbasic", "basic",
    "q", "qvto", "qvt", "qlik", "qlikview", "qliksense", "qlikscript",
    "qml", "qbs", "rconsole", "rout",
    "rng-compact", "rnc", "spec", "racket", "rkt",
    "ragel-c", "ragel-cpp", "ragel-d", "ragel-em", "ragel-java", "ragel",
    "ragel-objc", "ragel-ruby", "ragel-rb",
    "rd", "reasonml", "reason", "rebol", "red", "red/system",
    "redcode", "registry", "rego", "resourcebundle", "resource",
    "rexx", "arexx", "rhtml", "html+erb", "html+ruby",
    "ride", "rita", "roboconf-graph", "roboconf-instances",
    "robotframework", "rql", "rsl",
    "restructuredtext", "rst", "rest",
    "trafficscript", "rts", "rbcon", "irb",
    "ruby", "rb", "duby",
    "rust", "rs", "sas", "splus", "s", "r",
    "sml", "snbt", "sarl", "sass", "savi", "scala",
    "scaml", "scdoc", "scd", "scheme", "scm",
    "scilab", "scss", "sed", "gsed", "ssed",
    "shexc", "shex", "shen", "sieve", "silver",
    "singularity", "slash", "slim", "slurm", "sbatch",
    "smali", "smalltalk", "squeak", "st",
    "sgf", "smarty", "smithy", "snobol", "snowball",
    "solidity", "androidbp", "bp", "soong",
    "sophia", "sp", "debsources", "sourceslist", "sources.list",
    "sparql", "spice", "spicelang", "sql+jinja", "sql",
    "sqlite3", "squidconf", "squid.conf", "squid",
    "srcinfo", "ssp", "stan", "stata", "do",
    "supercollider", "sc", "swift", "swig",
    "systemverilog", "sv", "systemd", "tap",
    "tnt", "toml", "tablegen", "td", "tact", "tads3",
    "tal", "uxntal", "tasm", "tcl", "tcsh", "csh",
    "tcshcon", "tea", "teal", "teratermmacro", "teraterm", "ttl",
    "termcap", "terminfo", "terraform", "tf", "hcl",
    "tex", "latex", "text", "ti", "thingsdb",
    "thrift", "tid", "tlb", "tls",
    "todotxt", "tsql", "t-sql", "treetop", "tsx",
    "turtle", "html+twig", "twig", "typescript", "ts",
    "typoscriptcssdata", "typoscripthtmldata", "typoscript",
    "typst", "ul4", "ucode", "unicon",
    "unixconfig", "linuxconfig", "urbiscript", "urlencoded",
    "usd", "usda", "vbscript", "vcl", "vclsnippets", "vclsnippet",
    "vctreestatus", "vgl", "vala", "vapi",
    "aspx-vb",
    "vb.net", "vbnet", "lobas", "oobas", "sobas", "visual-basic", "visualbasic",
    "html+velocity", "velocity", "xml+velocity",
    "verifpal", "verilog", "v", "vhdl", "vim",
    "visualprologgrammar", "visualprolog",
    "vue", "vyper", "wdiff", "wast", "wat",
    "webidl", "wgsl", "whiley", "wikitext", "mediawiki",
    "wowtoc", "wren", "x10", "xten", "xml+ul4", "xquery",
    "xqy", "xq", "xql", "xqm",
    "xml+django", "xml+jinja",
    "xml+ruby", "xml+erb",
    "xml", "xml+php", "xml+smarty",
    "xorg.conf", "xpp", "x++", "xslt", "xtend",
    "extempore", "yaml+jinja", "salt", "sls", "yaml",
    "yang", "yara", "yar", "zeek", "bro",
    "zephir", "zig"
]
