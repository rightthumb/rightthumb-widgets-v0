@echo off
if not exist .git (
        echo need to be in git root folder
        goto:eof
)
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch %1" --prune-empty --tag-name-filter cat -- --all
git rm -rf %1
