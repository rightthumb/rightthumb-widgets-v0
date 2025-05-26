#!/bin/bash

obf_php="/mnt/d/.rightthumb-widgets/widgets/obfuscators/php.php"
obf_py="/mnt/d/.rightthumb-widgets/widgets/obfuscators/python.php"
obf_js="/mnt/d/.rightthumb-widgets/widgets/obfuscators/javascript.php"

# Help menu
usage() {
    echo
    echo "Usage:"
    echo "  ./obfuscate.sh <lang> <input> <output>"
    echo
    echo "Languages:"
    echo "  php   - Obfuscate PHP and output eval(gzinflate(base64_decode(...)))"
    echo "  py    - Obfuscate and output Python code using zlib + base64"
    echo "  js    - Obfuscate and output JavaScript (requires pako.js)"
    echo
    echo "Example:"
    echo "  ./obfuscate.sh php script.php obf.php"
    echo "  ./obfuscate.sh py script.py obf.py"
    echo "  ./obfuscate.sh js script.js obf.js"
    echo
    exit 1
}

# Check argument count
if [ $# -ne 3 ]; then
    usage
fi

lang="$1"
input="$2"
output="$3"

# Routing based on language
case "$lang" in
    php)
        php "$obf_php" "$input" "$output"
        ;;
    py)
        php "$obf_py" "$input" "$output"
        ;;
    js)
        php "$obf_js" "$input" "$output"
        ;;
    *)
        usage
        ;;
esac
