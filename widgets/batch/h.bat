@echo off
doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
CALL p singleLine -f "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt" > "%tmpf%"  2>&1
rem doskey /history > %tmpf%
type %tmpf% | p line -ln %*