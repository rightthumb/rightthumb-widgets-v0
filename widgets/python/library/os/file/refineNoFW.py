import os
import time

sampleOptions = {
	# Text/Binary filtering
	"Text": True,         # only allow text files
	"Binary": False,      # don't allow binary files

	# Ago (time filtering)
	# Example: only files modified between 2w ago and 1w ago
	"Ago": [
		1755815275.803617,   # 2 weeks ago timestamp
		1756506474.843919    # 1 week ago timestamp
	],
	"AgoMode": "md",        # md = check modified date
	# Other valid modes:
	#   "default" = modified by default
	#   "resent"  = modified OR created OR accessed
	#   "a"       = accessed date
	#   "cd"      = created date
	#   "md"      = modified date

	# Size filter
	# ("g", 10485760) = greater than 10 MB
	# ("l", 1024)     = less than 1 KB
	"Size": ("g", 10485760),

	# Extension filter
	# Only allow files with these extensions
	"Extensions": [".py", ".txt", ".md", ".log"],

	# Header filter
	## Encrypted filter
	### Requires is_crypt(path) to return True
	"Encrypted": False,
	
	# Encrypted filter
	"Header": '41 45 53 02 00 00 1B' # AES
	#  or
	# "Header": [ "FF D8 FF E0", "FF D8 FF E1", "FF D8 FF E8" ] # jpg
}



def refine(path, options=None, trigger=None, failTrigger=None):
	"""
	Check if a file passes a set of filters.

	:param path: Path to the file
	:param options: Dict of options, may include:
		{
			"Text": bool,
			"Binary": bool,
			"Ago": [timestamp, ...],
			"AgoMode": str in {"default","resent","ad","cd","md"},
			"Size": ("l"|"g", int),
			"Extensions": [".py", ".txt"],
			"Encrypted": bool
		}
	:param trigger: callback(path) if file is valid
	:param failTrigger: callback(path) if file is invalid
	"""

	if isinstance(options, list): # _.switches.all()
		# Convert list of switches to dict
		converted = {}
		for sw in options:
			if not sw.get("active"):
				continue
			name = sw["name"]
			vals = sw.get("values", [])
			val = sw.get("value", "")

			# Special handling for Ago
			if name == "Ago" and vals:
				mode = None
				if isinstance(vals[-1], str) and vals[-1] in ("md", "cd", "ad", "resent", "default"):
					mode = vals[-1]
					vals = vals[:-1]  # remove mode token
				converted["Ago"] = vals
				if mode:
					converted["AgoMode"] = mode
				continue

			# Size -> ("g", int) or ("l", int)
			if name == "Size" and len(vals) >= 2:
				converted["Size"] = (vals[0], vals[1])
				continue

			# Simple boolean switches
			if name in ("Text", "Binary", "Encrypted"):
				converted[name] = True
				continue

			converted[name] = vals if vals else True

		options = converted


	if options is None:
		options = {}
	if 'AgoMode' in options:
		am = {
			'a': 'ad',
			'm': 'md',
			'c': 'cd',
		}
		if options['AgoMode'] in am:
			options['AgoMode'] = am[options['AgoMode']]

	if not os.path.isfile(path):
		return False

	# normalize path
	path = normalize_path(path)

	isValid = False

	# line filtering
	if show_line(path):

		# --- Text/Binary ---
		if not options.get("Text") and not options.get("Binary"):
			isValid = True
		else:
			if options.get("Text") and not options.get("Binary") and is_text(path):
				isValid = True
			if not options.get("Text") and options.get("Binary") and not is_text(path):
				isValid = True
			if not options.get("Text") and not options.get("Binary"):
				isValid = True

		# --- Ago ---
		if "Ago" in options:
			record = file_info(path)
			isValid = False
			run = options.get("AgoMode", "default")
			ago_vals = options["Ago"]

			agoRange = len(ago_vals) > 1 and isinstance(ago_vals[1], (float, int))

			if not agoRange:
				ts = ago_vals[0]
				if run in ("default", "resent", "md"):
					if record["date_modified_raw"] > ts:
						isValid = True
				elif run == "ad":
					if record["accessed_raw"] > ts:
						isValid = True
				elif run == "cd":
					if record["date_created_raw"] > ts:
						isValid = True
			else:
				t1, t2 = ago_vals[0], ago_vals[1]
				if run in ("default", "md"):
					if t2 < record["date_modified_raw"] < t1:
						isValid = True
				elif run == "resent":
					if any(t2 < record[k] < t1 for k in ["date_modified_raw", "date_created_raw", "accessed_raw"]):
						isValid = True
				elif run == "ad":
					if t2 < record["accessed_raw"] < t1:
						isValid = True
				elif run == "cd":
					if t2 < record["date_created_raw"] < t1:
						isValid = True

		# --- Size ---
		if isValid and "Size" in options:
			size_rule, size_limit = options["Size"]
			fsize = os.stat(path).st_size
			if size_rule == "l" and fsize < size_limit:
				isValid = True
			elif size_rule == "g" and fsize > size_limit:
				isValid = True
			else:
				isValid = False

		# --- Extensions ---
		if isValid and options.get("Extensions"):
			record = file_info(path)
			ext = record["ext"].lower() if record["ext"] else ""
			if f".{ext}" not in options["Extensions"]:
				isValid = False

		# --- Encrypted ---
		if isValid and options.get("Encrypted") and not is_crypt(path):
			isValid = False

		# --- Header ---
		if isValid and options.get("Header") and not has_any(record["header"], options["Header"]):
			isValid = False

		# --- Exclude .pyc ---
		if isValid and path.endswith(".pyc"):
			isValid = False

	# Callbacks
	if isValid and trigger:
		trigger(path)
	if not isValid and failTrigger:
		failTrigger(path)

	return isValid


# ---- Framework-dependent stubs ----
def normalize_path(path):
	# __.path(path)
	pass

def show_line(path):
	pass



def file_info(path):
	"""Should return dict with keys: date_modified_raw, date_created_raw, accessed_raw, ext"""
	# _dir.info(path)
	pass

def is_crypt(path):
	pass

def has_any(line: str, words: list[str]) -> bool:
	for w in words:
		if w in line:
			return True
	return False





def hex_string_to_bytes(data) -> bytes:
	"""
	Convert a space-separated hex string like:
		'41 45 53 02 00 00 1B'
	into a bytes object:
		b'\\x41\\x45\\x53\\x02\\x00\\x00\\x1B'

	If `data` is already bytes, it is returned unchanged.
	"""
	if isinstance(data, bytes):
		return data
	if isinstance(data, str):
		return bytes(int(x, 16) for x in data.strip().split())
	raise TypeError(f"Unsupported type {type(data)}: expected str or bytes")



import os

def is_text(path: str, sample_size: int = 65536) -> bool:
	"""
	Heuristic text/binary detector that:
	- Treats empty files as text
	- Flags NUL (0x00) as binary immediately
	- Accepts UTF-8 (incl. emoji) if strict decode works
	- Accepts UTF-16/32 if BOM is present
	- Otherwise uses a small control-byte ratio heuristic
	"""
	try:
		with open(path, 'rb') as f:
			chunk = f.read(sample_size)
	except Exception:
		# If we can't read it, be conservative.
		return False

	if not chunk:
		return True  # empty file -> text

	# 1) Hard stop: NUL bytes strongly indicate binary
	if b'\x00' in chunk:
		return False

	# 2) Known Unicode BOMs -> treat as text
	BOMS = (
		b'\xef\xbb\xbf',                  # UTF-8 BOM
		b'\xff\xfe', b'\xfe\xff',         # UTF-16 LE/BE
		b'\xff\xfe\x00\x00', b'\x00\x00\xfe\xff'  # UTF-32 LE/BE
	)
	if any(chunk.startswith(bom) for bom in BOMS):
		return True

	# 3) Fast path: strict UTF-8 decode (allows emoji & multibyte)
	try:
		chunk.decode('utf-8', errors='strict')
		return True
	except UnicodeDecodeError:
		pass

	# 4) Optional: try UTF-16 strict if it looks like alternating NULs (no BOM)
	# Quick pattern check: lots of zeroes at odd/even positions can indicate UTF-16 text.
	# We'll sample the first 4096 bytes (or the chunk length) for this quick test.
	probe = chunk[:4096]
	if len(probe) >= 4:
		zeros_even = sum(1 for i in range(0, len(probe), 2) if probe[i] == 0)
		zeros_odd  = sum(1 for i in range(1, len(probe), 2) if probe[i] == 0)
		# If one side has very high zero frequency and the other does not, it smells like UTF-16.
		# Thresholds are heuristic but cheap.
		if (zeros_even > len(probe) * 0.20 and zeros_odd < len(probe) * 0.05) or \
		(zeros_odd  > len(probe) * 0.20 and zeros_even < len(probe) * 0.05):
			try:
				chunk.decode('utf-16', errors='strict')
				return True
			except UnicodeDecodeError:
				pass

	# 5) Control-byte ratio heuristic (resource-cheap, avoids false positives)
	# Allow common whitespace controls; penalize other C0/C1 controls heavily.
	TEXT_WHITELIST = {0x09, 0x0A, 0x0D}  # \t, \n, \r
	control_suspects = 0
	total = len(chunk)

	for b in chunk:
		if b < 0x20 and b not in TEXT_WHITELIST:
			control_suspects += 1
		elif b == 0x7F:
			control_suspects += 1
		# Bytes >= 0x80 are fine (UTF-8 multibyte, emoji, etc.)

	# If too many suspicious control bytes, call it binary
	if total > 0 and (control_suspects / total) > 0.01:
		return False

	# Otherwise, treat as text
	return True



# ============================================
# File Signature (Magic Byte) Detection Suite
# ============================================

# ---- Global caches ----
_HEADER_CACHE_SINGLE: dict[object, bytes] = {}        # single spec -> bytes
_HEADER_CACHE_MULTI: dict[object, tuple[bytes, ...]] = {}  # multi spec -> tuple[bytes,...]


def is_crypt(path: str, header_spec=None) -> bool:
	"""
	Convenience wrapper for your AES default unless overridden.
	Accepts name | hex-string | bytes | list/tuple of those.
	"""
	return has_header(path, header_spec or "41 45 53 02 00 00 1B")


def has_header(path: str, header_spec) -> bool:
	"""
	True if the file at `path` starts with ANY header implied by `header_spec`.

	`header_spec` can be:
	- bytes
	- space-separated hex string: "41 45 53 02 00 00 1B"
	- library key/name (no spaces): e.g., "docx"
	- list/tuple of any combination of the above
	"""
	try:
		headers = _normalize_to_bytes_list(header_spec)
		if not headers:
			return False

		max_len = max(len(h) for h in headers)
		with open(path, "rb") as f:
			sig = f.read(max_len)

		for h in headers:
			hl = len(h)
			if hl and sig[:hl] == h:
				return True
		return False
	except Exception:
		return False


# ---------- Converters ----------

def hex_string_to_bytes(data):
	"""
	Accepts:
	- str (space-separated hex: '41 45 53 ...') -> bytes
	- bytes -> bytes (unchanged)
	- list/tuple of str/bytes -> tuple[bytes, ...]
	"""
	if isinstance(data, bytes):
		return data
	if isinstance(data, str):
		return bytes(int(x, 16) for x in data.strip().split())
	if isinstance(data, (list, tuple)):
		return tuple(hex_string_to_bytes(x) for x in data)
	raise TypeError(f"Unsupported type {type(data)}")


def bytes_to_hex_string(data):
	"""
	Reverse of hex_string_to_bytes:
	- bytes -> '41 45 53 ...'
	- list/tuple[bytes] -> tuple['..', '..', ...]
	"""
	if isinstance(data, bytes):
		return " ".join(f"{b:02X}" for b in data)
	if isinstance(data, (list, tuple)):
		return tuple(bytes_to_hex_string(x) for x in data)
	raise TypeError(f"Unsupported type {type(data)}")


# ---------- Core normalization ----------

def _normalize_to_bytes_list(spec) -> tuple[bytes, ...]:
	"""
	Normalize `spec` into a tuple[bytes, ...], using caches aggressively.

	Accepts:
	- bytes -> (bytes,)
	- "AA BB ..." -> (bytes_from_hex,)
	- "name" (no spaces) -> resolve via headerLib (string/bytes/list/tuple)
	- list/tuple of any combination above -> flattened tuple of bytes
	"""
	# Fast paths via caches for already-processed specs
	if spec in _HEADER_CACHE_MULTI:
		return _HEADER_CACHE_MULTI[spec]
	if spec in _HEADER_CACHE_SINGLE:
		return (_HEADER_CACHE_SINGLE[spec],)

	# bytes -> tuple
	if isinstance(spec, bytes):
		_HEADER_CACHE_SINGLE[spec] = spec
		return (spec,)

	# string
	if isinstance(spec, str):
		if " " in spec:
			# space-separated hex string
			b = _HEADER_CACHE_SINGLE.get(spec)
			if b is None:
				b = hex_string_to_bytes(spec)
				_HEADER_CACHE_SINGLE[spec] = b
			return (b,)
		else:
			resolved = get_header_spec_by_name(spec)  # implement below
			bytes_list = _coerce_list_of_bytes(resolved)
			_HEADER_CACHE_MULTI[spec] = bytes_list
			return bytes_list

	# list/tuple -> flatten & normalize each element
	if isinstance(spec, (list, tuple)):
		bytes_list = _coerce_list_of_bytes(spec)
		# Use tuple(spec) as a stable cache key when possible
		try:
			_HEADER_CACHE_MULTI[tuple(spec)] = bytes_list
		except TypeError:
			# Unhashable elements; skip caching this composite key
			pass
		return bytes_list

	raise TypeError(f"Unsupported header spec type: {type(spec)}")


def _coerce_list_of_bytes(obj) -> tuple[bytes, ...]:
	"""
	Take str/bytes/list/tuple of the above and return tuple[bytes, ...].
	Reuses single-cache for each element when possible.
	"""
	if obj is None:
		return tuple()

	# Single element
	if isinstance(obj, (bytes, str)):
		if obj in _HEADER_CACHE_SINGLE:
			return (_HEADER_CACHE_SINGLE[obj],)
		if isinstance(obj, bytes):
			_HEADER_CACHE_SINGLE[obj] = obj
			return (obj,)
		# str
		if " " in obj:
			b = hex_string_to_bytes(obj)
			_HEADER_CACHE_SINGLE[obj] = b
			return (b,)
		# name/key -> resolve recursively
		return _normalize_to_bytes_list(obj)

	# Multiple
	if isinstance(obj, (list, tuple)):
		out = []
		for item in obj:
			if item in _HEADER_CACHE_SINGLE:
				out.append(_HEADER_CACHE_SINGLE[item])
				continue
			if isinstance(item, bytes):
				_HEADER_CACHE_SINGLE[item] = item
				out.append(item)
			elif isinstance(item, str):
				if " " in item:
					b = hex_string_to_bytes(item)
					_HEADER_CACHE_SINGLE[item] = b
					out.append(b)
				else:
					out.extend(_normalize_to_bytes_list(item))
			else:
				raise TypeError(f"Unsupported element in header list: {type(item)}")
		return tuple(out)

	raise TypeError(f"Unsupported object for header list coercion: {type(obj)}")


# ---------- Library resolver ----------

def get_header_spec_by_name(name: str):
	"""
	Look up by key in headerLib. Return raw library value:
	- str (space-separated hex) OR bytes OR list/tuple of those, or None.
	"""
	if not isinstance(name, str):
		raise TypeError("name must be a string")
	if " " in name:
		# Not a library key; likely a hex string. Let caller handle it.
		return name
	return headerLib.get(name)


def coerce_headers(spec) -> tuple[bytes, ...]:
	"""
	Public helper: normalize any spec to tuple[bytes, ...].
	Accepts:
	- 'name' (no spaces) -> resolve via headerLib
	- 'AA BB CC' -> bytes
	- bytes -> bytes
	- list/tuple of any of the above -> flattened tuple
	"""
	if spec is None:
		return tuple()

	if isinstance(spec, bytes):
		return (spec,)

	if isinstance(spec, str):
		if " " in spec:
			return (hex_string_to_bytes(spec),)
		resolved = get_header_spec_by_name(spec)
		if resolved is None:
			return tuple()
		return coerce_headers(resolved)

	if isinstance(spec, (list, tuple)):
		out = []
		for item in spec:
			out.extend(coerce_headers(item))
		return tuple(out)

	raise TypeError(f"Unsupported header spec type: {type(spec)}")


# ---------- Example header library definition ----------

headerLib = {
	# --- Archives / Containers ---
	"zip":        "50 4B 03 04",                  # ZIP (also docx/xlsx/pptx/jar/apk/etc.)
	"jar":        "50 4B 03 04",
	"apk":        "50 4B 03 04",
	"docx":       "50 4B 03 04",
	"xlsx":       "50 4B 03 04",
	"pptx":       "50 4B 03 04",
	"odt":        "50 4B 03 04",
	"ods":        "50 4B 03 04",
	"odp":        "50 4B 03 04",
	"rar":        "52 61 72 21 1A 07 00",
	"rar5":       "52 61 72 21 1A 07 01 00",
	"7z":         "37 7A BC AF 27 1C",
	"gz":         "1F 8B 08",
	"bz2":        "42 5A 68",
	"xz":         "FD 37 7A 58 5A 00",
	"zstd":       "28 B5 2F FD",
	"lz4":        "04 22 4D 18",

	# --- Documents / Images ---
	"pdf":        "25 50 44 46",
	"png":        "89 50 4E 47 0D 0A 1A 0A",
	"jpg":       ("FF D8 FF E0", "FF D8 FF E1", "FF D8 FF E8"),
	"gif":       ("47 49 46 38 37 61", "47 49 46 38 39 61"),
	"tiff":      ("49 49 2A 00", "4D 4D 00 2A"),
	"bmp":        "42 4D",
	"ico":        "00 00 01 00",
	"cur":        "00 00 02 00",
	"psd":        "38 42 50 53",

	# --- Audio / Media ---
	"mp3":    ("FF FB", "FF F3", "FF F2", "49 44 33"),
	"mp3_id3":    "49 44 33",
	"mp3_frame": ("FF FB", "FF F3", "FF F2"),
	"flac":       "66 4C 61 43",
	"ogg":        "4F 67 67 53",
	"wav_riff":   "52 49 46 46",  # RIFF (needs offset check for 'WAVE' at +8)
	"avi_riff":   "52 49 46 46",  # RIFF (needs offset check for 'AVI '  at +8)
	"webp_riff":  "52 49 46 46",  # RIFF (needs offset check for 'WEBP' at +8)

	"mkv":        "1A 45 DF A3",  # EBML (Matroska/WebM—doc type parse to confirm)
	"webm":       "1A 45 DF A3",

	# --- Executables / Libraries ---
	"elf":        "7F 45 4C 46",
	"pe_mz":      "4D 5A",        # PE/EXE/DLL start with 'MZ'
	"mach_o":    ("FE ED FA CE", "FE ED FA CF", "CE FA ED FE", "CF FA ED FE"),

	# --- Databases / Class files ---
	"sqlite":     "53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00",  # "SQLite format 3\0"
	"java_class": "CA FE BA BE",
	"dex":        "64 65 78 0A 30",

	# --- Fonts ---
	"woff":       "77 4F 46 46",
	"woff2":      "77 4F 46 32",
	"ttc_otc":    "74 74 63 66",  # 'ttcf'
	"ttf":        "00 01 00 00",
	"otf":        "4F 54 54 4F",  # 'OTTO'

	# --- Crypto / Custom ---
	"aes_default": "41 45 53 02 00 00 1B",
	"aes": "41 45 53 02 00 00 1B",
	"isCrypt": "41 45 53 02 00 00 1B",      # framework’s default AES header

	"wav": "52 49 46 46",
	"avi": "52 49 46 46"

}