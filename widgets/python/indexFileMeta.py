#!/usr/bin/env python3
# meta_to_unqlite.py
# Collect rich file metadata and save to UnQLite (KV store + lightweight secondary indexes).
# Indentation = 4 spaces (per user preference)

import argparse, os, sys, stat, json, hashlib, mimetypes, subprocess, shutil, time
from datetime import datetime, timezone

# ---------- Optional imports (best-effort) ----------
try:
	from unqlite import UnQLite
except Exception:
	UnQLite = None

try:
	from PIL import Image, ExifTags
except Exception:
	Image = None
	ExifTags = None

try:
	import mutagen  # audio/video tags
except Exception:
	mutagen = None

try:
	import PyPDF2
except Exception:
	PyPDF2 = None

# ---------- Small helpers ----------
def norm_path(p: str) -> str:
	# Normalize for a consistent key; keep case on *nix, lower drive on Windows
	p = os.path.abspath(p)
	if os.name == "nt":
		if len(p) >= 2 and p[1] == ':':
			p = p[0].lower() + p[1:]
	return p.replace('\\', '/')

def epoch(dt: float) -> float:
	# already epoch
	return float(dt)

def isoformat(ts: float) -> str:
	try:
		return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat().replace('+00:00', 'Z')
	except Exception:
		return None

def file_hash(path: str, algo: str = "sha256", chunk: int = 1024 * 1024) -> str | None:
	try:
		h = hashlib.new(algo)
	except Exception:
		return None
	try:
		with open(path, "rb") as f:
			while True:
				b = f.read(chunk)
				if not b:
					break
				h.update(b)
		return h.hexdigest()
	except Exception:
		return None

def run_tool(cmd: list[str], timeout: int = 20) -> tuple[int, str, str]:
	try:
		p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, text=True)
		return p.returncode, p.stdout, p.stderr
	except Exception as e:
		return 1, "", str(e)

def which_or(arg: str | None, fallback: str):
	if arg and arg not in ("", "auto"):
		return arg
	return shutil.which(fallback)

def safe_rel(root: str, path: str) -> str:
	try:
		return os.path.relpath(path, root)
	except Exception:
		return path

def split_list_csv(s: str | None) -> set[str]:
	if not s:
		return set()
	return set([x.strip().lower() for x in s.split(',') if x.strip()])

# ---------- Metadata extractors (best-effort) ----------
def fs_metadata(path: str) -> dict:
	d: dict = {}
	try:
		st = os.lstat(path)
	except Exception as e:
		return {"error": f"stat_failed: {e}"}

	d["size"] = st.st_size
	d["mode"] = stat.S_IMODE(st.st_mode)
	d["is_symlink"] = stat.S_ISLNK(st.st_mode)
	d["is_dir"] = stat.S_ISDIR(st.st_mode)
	d["is_file"] = stat.S_ISREG(st.st_mode)

	# Timestamps
	d["mtime"] = epoch(st.st_mtime)
	d["ctime"] = epoch(st.st_ctime)
	if hasattr(st, "st_atime"):
		d["atime"] = epoch(st.st_atime)

	# ISO timestamps
	for k in ("mtime", "ctime", "atime"):
		if k in d:
			d[k + "_iso"] = isoformat(d[k])

	# Owner (best-effort)
	if os.name != "nt":
		try:
			import pwd, grp
			d["uid"] = st.st_uid
			d["gid"] = st.st_gid
			d["user"] = pwd.getpwuid(st.st_uid).pw_name
			d["group"] = grp.getgrgid(st.st_gid).gr_name
		except Exception:
			pass
	else:
		# On Windows we can store owner via icacls (slow) or skip
		pass

	# Link target
	if d["is_symlink"]:
		try:
			d["symlink_target"] = os.readlink(path)
		except Exception:
			d["symlink_target"] = None

	return d

def mime_and_ext(path: str) -> dict:
	ext = os.path.splitext(path)[1].lower().lstrip('.')
	mt, enc = mimetypes.guess_type(path)
	return {"ext": ext or None, "mime_guess": mt, "encoding_guess": enc}

def image_exif_pillow(path: str) -> dict | None:
	if Image is None:
		return None
	try:
		with Image.open(path) as im:
			exif = getattr(im, "_getexif", lambda: None)()
			if not exif:
				return None
			out = {}
			tagmap = ExifTags.TAGS if ExifTags else {}
			for k, v in exif.items():
				tag = tagmap.get(k, str(k))
				# Convert bytes to string when useful
				if isinstance(v, bytes):
					try:
						v = v.decode('utf-8', 'ignore')
					except Exception:
						v = v.hex()
				out[tag] = v
			return out
	except Exception:
		return None

def exiftool_meta(path: str, exiftool_cmd: str | None) -> dict | None:
	if not exiftool_cmd:
		return None
	# JSON (-j) single output
	code, out, err = run_tool([exiftool_cmd, "-j", "-n", path], timeout=30)
	if code != 0 or not out.strip():
		return None
	try:
		data = json.loads(out)
		if isinstance(data, list) and data:
			# remove file path keys to avoid duplication
			data[0].pop("SourceFile", None)
			return data[0]
	except Exception:
		return None
	return None

def ffprobe_meta(path: str, ffprobe_cmd: str | None) -> dict | None:
	if not ffprobe_cmd:
		return None
	args = [ffprobe_cmd, "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path]
	code, out, err = run_tool(args, timeout=40)
	if code != 0 or not out.strip():
		return None
	try:
		return json.loads(out)
	except Exception:
		return None

def mediainfo_meta(path: str, mediainfo_cmd: str | None) -> dict | None:
	if not mediainfo_cmd:
		return None
	args = [mediainfo_cmd, "--Output=JSON", path]
	code, out, err = run_tool(args, timeout=40)
	if code != 0 or not out.strip():
		return None
	try:
		return json.loads(out)
	except Exception:
		return None

def mutagen_tags(path: str) -> dict | None:
	if mutagen is None:
		return None
	try:
		f = mutagen.File(path, easy=True)
		if not f:
			return None
		out = {}
		for k, v in (f.tags or {}).items():
			# list -> single str or list
			if isinstance(v, list) and len(v) == 1:
				out[k] = v[0]
			else:
				out[k] = v
		# duration if available
		try:
			out["_length_seconds"] = float(getattr(f.info, "length", None)) if getattr(f, "info", None) else None
		except Exception:
			pass
		return out or None
	except Exception:
		return None

def pdf_core(path: str) -> dict | None:
	if PyPDF2 is None:
		return None
	try:
		with open(path, "rb") as fh:
			r = PyPDF2.PdfReader(fh)
			info = r.metadata or {}
			out = {"pages": len(r.pages)}
			# Metadata keys typically like '/Title'
			for k, v in dict(info).items():
				k = str(k).lstrip('/')
				out[k] = str(v) if not isinstance(v, (int, float)) else v
			return out
	except Exception:
		return None

def office_zip_core(path: str) -> dict | None:
	# Extract minimal core props for docx/xlsx/pptx (Open Packaging Conventions)
	if not path.lower().endswith((".docx", ".xlsx", ".pptx")):
		return None
	import zipfile, xml.etree.ElementTree as ET
	try:
		with zipfile.ZipFile(path, 'r') as z:
			if "docProps/core.xml" not in z.namelist():
				return None
			with z.open("docProps/core.xml") as f:
				xml = f.read()
			ns = {
				"cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
				"dc": "http://purl.org/dc/elements/1.1/",
				"dcterms": "http://purl.org/dc/terms/",
				"xsi": "http://www.w3.org/2001/XMLSchema-instance"
			}
			root = ET.fromstring(xml)
			out = {}
			for tag in ("title", "subject", "creator", "keywords", "description", "lastModifiedBy"):
				el = root.find(f"dc:{tag}", ns) or root.find(f"cp:{tag}", ns)
				if el is not None and el.text:
					out[tag] = el.text
			for tag in ("created", "modified"):
				el = root.find(f"dcterms:{tag}", ns)
				if el is not None and el.text:
					out[tag] = el.text
			return out or None
	except Exception:
		return None

# ---------- UnQLite storage ----------
class KVStore:
	def __init__(self, db_path: str):
		if UnQLite is None:
			raise RuntimeError("unqlite module not installed. pip install unqlite")
		self.db = UnQLite(db_path)


	def put(self, key: str, doc: dict) -> None:
		# Always overwrite / upsert
		self.db[key] = json.dumps(doc, ensure_ascii=False).encode('utf-8')

	def get(self, key: str) -> dict | None:
		try:
			raw = self.db[key]
			return json.loads(raw.decode('utf-8'))
		except KeyError:
			return None
		except Exception:
			return None

	def put_index_member(self, index_name: str, member_key: str, value: str) -> None:
		k = f"index:{index_name}:{member_key}"
		try:
			cur = json.loads(self.db[k].decode('utf-8'))
		except Exception:
			cur = []
		if value not in cur:
			cur.append(value)
			self.db[k] = json.dumps(cur, ensure_ascii=False).encode('utf-8')



# ---------- Public helper ----------

def update_or_add(path: str,
				db_path: str = "meta.unqlite",
				algo: str = "sha256",
				exiftool_cmd: str | None = None,
				ffprobe_cmd: str | None = None,
				mediainfo_cmd: str | None = None) -> dict:
	"""
	Update or insert metadata for a single file into UnQLite.
	Returns the collected metadata dict.
	"""
	kv = KVStore(db_path)
	args = argparse.Namespace(
		src=os.path.dirname(path) or ".",
		hash=algo,
		no_hash=False,
	)
	doc = collect_one(path, args, exiftool_cmd, ffprobe_cmd, mediainfo_cmd)

	key = "file:" + doc["path"]
	kv.put(key, doc)

	# maintain indexes
	ext = (doc.get("type", {}).get("ext") or "").lower()
	if ext:
		kv.put_index_member("ext", ext, key)
	h = (doc.get("hash") or {}).get(algo)
	if h:
		kv.put_index_member("hash", h, key)

	return doc


# ---------- Core collector ----------
def collect_one(path: str, args, exiftool_cmd: str | None, ffprobe_cmd: str | None, mediainfo_cmd: str | None) -> dict:
	pnorm = norm_path(path)
	doc = {
		"path": pnorm,
		"name": os.path.basename(path),
		"parent": norm_path(os.path.dirname(path)),
		"rel": safe_rel(args.src, path),
		"collected_at": isoformat(time.time()),
	}

	# FS
	doc["fs"] = fs_metadata(path)

	# Guess
	doc["id"] = hashlib.sha1(pnorm.encode('utf-8')).hexdigest()
	doc["type"] = mime_and_ext(path)

	# Hashes
	if not args.no_hash:
		algo = args.hash.lower()
		doc["hash"] = {algo: file_hash(path, algo)}

	# Content-specific (best-effort)
	ext = (doc["type"]["ext"] or "").lower()

	# Images
	if ext in {"jpg", "jpeg", "tif", "tiff", "png", "webp", "heic", "heif"}:
		doc["image"] = {}
		if Image is not None:
			ex = image_exif_pillow(path)
			if ex:
				doc["image"]["exif_pillow"] = ex
		et = exiftool_meta(path, exiftool_cmd)
		if et:
			doc["image"]["exiftool"] = et

	# Audio/Video
	if ext in {"mp3", "flac", "m4a", "aac", "ogg", "wav", "wma",
			"mp4", "mkv", "mov", "avi", "webm"}:
		tags = mutagen_tags(path)
		if tags:
			doc["av_tags"] = tags
		ff = ffprobe_meta(path, ffprobe_cmd)
		if ff:
			doc["ffprobe"] = ff
		if not ff:
			mi = mediainfo_meta(path, mediainfo_cmd)
			if mi:
				doc["mediainfo"] = mi

	# PDF
	if ext == "pdf":
		core = pdf_core(path)
		if core:
			doc["pdf"] = core

	# Office zip
	if ext in {"docx", "xlsx", "pptx"}:
		core = office_zip_core(path)
		if core:
			doc["office"] = core

	return doc

def should_include(path: str, include_exts: set[str], exclude_exts: set[str]) -> bool:
	if not include_exts and not exclude_exts:
		return True
	ext = os.path.splitext(path)[1].lower().lstrip('.')
	if include_exts and ext not in include_exts:
		return False
	if exclude_exts and ext in exclude_exts:
		return False
	return True


def main():
	ap = argparse.ArgumentParser(description="Collect rich file metadata to UnQLite.")
	ap.add_argument("--src", help="Source folder")
	ap.add_argument("-r", "--recursive", action="store_true", help="Recurse into subfolders")
	ap.add_argument("--file", help="Single file to update/add")
	ap.add_argument("--update", action="store_true", help="Force update/overwrite if exists (default)")
	ap.add_argument("--db", default="meta.unqlite", help="UnQLite database file")
	ap.add_argument("--hash", default="sha256", choices=["md5","sha1","sha256"], help="Which content hash to compute")
	ap.add_argument("--no-hash", action="store_true", help="Skip content hashes")
	ap.add_argument("--exiftool", default="auto", help="Path to exiftool or 'auto'")
	ap.add_argument("--ffprobe", default="auto", help="Path to ffprobe or 'auto'")
	ap.add_argument("--mediainfo", default="auto", help="Path to mediainfo or 'auto'")
	ap.add_argument("--include", default="", help="Comma-separated list of extensions to include")
	ap.add_argument("--exclude", default="", help="Comma-separated list of extensions to exclude")
	ap.add_argument("--jsonl-fallback", default="", help="If unqlite unavailable, write JSONL to this path")
	args = ap.parse_args()

	# discover tools
	exiftool_cmd = which_or(args.exiftool, "exiftool")
	ffprobe_cmd = which_or(args.ffprobe, "ffprobe")
	mediainfo_cmd = which_or(args.mediainfo, "mediainfo")

	if args.file:
		# ---- Single file mode ----
		doc = update_or_add(args.file,
							db_path=args.db,
							algo=args.hash,
							exiftool_cmd=exiftool_cmd,
							ffprobe_cmd=ffprobe_cmd,
							mediainfo_cmd=mediainfo_cmd)
		print(json.dumps(doc, indent=2, ensure_ascii=False))
		return

	if not args.src:
		print("[error] must provide --src or --file", file=sys.stderr)
		sys.exit(2)

	# ---- Bulk folder mode ----
	src = os.path.abspath(args.src)
	include_exts = split_list_csv(args.include)
	exclude_exts = split_list_csv(args.exclude)

	# Storage init (same as before)
	kv = None
	jsonl = None
	using_unqlite = False
	if UnQLite is not None:
		try:
			kv = KVStore(args.db)
			using_unqlite = True
		except Exception as e:
			print(f"[warn] UnQLite unavailable ({e}); falling back to JSONL.", file=sys.stderr)

	if not using_unqlite:
		if not args.jsonl_fallback:
			print("[error] unqlite not installed and no --jsonl-fallback provided.", file=sys.stderr)
			sys.exit(3)
		jsonl = open(args.jsonl_fallback, "a", encoding="utf-8")
		print(f"[info] Writing JSONL to {args.jsonl_fallback}", file=sys.stderr)
	else:
		print(f"[info] Writing to UnQLite at {args.db}", file=sys.stderr)

	total = 0
	saved = 0
	t0 = time.time()

	def save_doc(doc: dict):
		nonlocal saved
		key = "file:" + doc["path"]
		if using_unqlite:
			kv.put(key, doc)
			# indexes
			ext = (doc.get("type", {}).get("ext") or "").lower()
			if ext:
				kv.put_index_member("ext", ext, key)
			h = (doc.get("hash") or {}).get(args.hash)
			if h:
				kv.put_index_member("hash", h, key)
		else:
			jsonl.write(json.dumps(doc, ensure_ascii=False) + "\n")
		saved += 1

	# walk
	if args.recursive:
		for root, dirs, files in os.walk(src):
			for name in files:
				path = os.path.join(root, name)
				total += 1
				if not should_include(path, include_exts, exclude_exts):
					continue
				doc = collect_one(path, args, exiftool_cmd, ffprobe_cmd, mediainfo_cmd)
				save_doc(doc)
	else:
		for name in os.listdir(src):
			path = os.path.join(src, name)
			if not os.path.isfile(path):
				continue
			total += 1
			if not should_include(path, include_exts, exclude_exts):
				continue
			doc = collect_one(path, args, exiftool_cmd, ffprobe_cmd, mediainfo_cmd)
			save_doc(doc)

	dt = time.time() - t0
	print(f"[done] scanned={total} saved={saved} elapsed={dt:.1f}s", file=sys.stderr)


'''
from meta_to_unqlite import update_or_add

doc = update_or_add("/home/scott/file.mp4", db_path="meta.unqlite")
print(doc["path"], "updated")

'''


if __name__ == "__main__":
	main()