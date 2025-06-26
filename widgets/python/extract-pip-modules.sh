#!/bin/bash

# Usage: ./extract-pip-modules.sh [-r] [path]
# Outputs pip-installable modules (one per line)

RECURSIVE=false
TARGET="."

# Parse args
while [[ $# -gt 0 ]]; do
	case "$1" in
		-r|--recursive)
			RECURSIVE=true
			shift
			;;
		*)
			TARGET="$1"
			shift
			;;
	esac
done

# Get .py files
if $RECURSIVE; then
	FILES=$(find "$TARGET" -type f -name "*.py")
else
	FILES=$(find "$TARGET" -maxdepth 1 -type f -name "*.py")
fi

# Extract all import lines
IMPORT_LINES=$(grep -E '^\s*(import|from)\s+' $FILES 2>/dev/null)

# Extract imported module names (top-level only)
MODULES=$(echo "$IMPORT_LINES" \
	| sed -E 's/#.*//' \
	| sed -E 's/^\s*//' \
	| sed -E 's/^from\s+([a-zA-Z0-9_\.]+)\s+import.*/\1/' \
	| sed -E 's/^import\s+([a-zA-Z0-9_\.]+).*/\1/' \
	| tr ',' '\n' \
	| cut -d'.' -f1 \
	| sed -E 's/\s+//g' \
	| grep -v '^$' \
	| sort -u)

# Standard library exclusion list (short)
STD_LIBS="sys|os|re|math|json|time|subprocess|threading|http|urllib|email|base64|collections|itertools|functools|random|datetime|logging|argparse|typing|builtins|__future__|traceback|unittest|multiprocessing|asyncio|dataclasses|shlex|socket|pdb|inspect|platform|importlib|errno|selectors|signal|glob|gzip|tempfile|webbrowser|uuid|copy|abc|io|hashlib|hmac|pickle|queue|types|string|contextlib|warnings|stat|ssl|getpass|codecs|pathlib|configparser|fileinput|lzma|bz2|struct|csv|xml|xmlrpc|posixpath|site|marshal|distutils|tokenize|pprint|tabnanny|gettext"

# Filter non-stdlib, non-local, real modules
echo "$MODULES" \
	| grep -vE "^($STD_LIBS)$" \
	| grep -v '^_' \
	| sort -u