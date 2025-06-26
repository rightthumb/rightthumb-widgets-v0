@echo off
call lab %1
call g %1
@REM call c
IF NOT ["%lab%"] == [""] (
    TITLE loc-%Session_ID_Suffix% :: %lab%
) else (
    TITLE loc-%Session_ID_Suffix%
)
call refresh