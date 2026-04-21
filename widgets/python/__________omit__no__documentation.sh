#!/bin/bash
source $HOME/.bashrc

export dex="$p search-indexDB-files -db index.db"

# echo $p

# $dex -has $1 | $p win-wsl | xargs grep -L 'thisApp.py'  | $p win-wsl

# $dex -has $1



$dex -has $1 | $p win-wsl | while IFS= read -r file; do
    [ -f "$file" ] && ! grep -q 'thisApp.py' "$file" && echo "$file"
done | $p win-wsl
