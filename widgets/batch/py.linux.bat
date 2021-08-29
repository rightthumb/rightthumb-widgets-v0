@echo off
call p f -in %widgets%\widgets\bash\history\*.* + "p *" | p line -p ";sp" 1 | sort | p countEach
