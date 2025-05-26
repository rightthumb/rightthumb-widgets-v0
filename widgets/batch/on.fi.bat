@echo off
if [%2] == [] (
    CALL p. tag -trigger expires 1w -f %*
    CALL p. on -session %Session_id% -folder .
) else (
    CALL p. tag -trigger expires 1w -delete -f %*
    CALL p. on -session %Session_id% -folder . -delete
)