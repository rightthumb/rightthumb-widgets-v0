for /f "tokens=3" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path  ^|findstr /ri "REG_EXPAND_SZ"') do echo %%a
