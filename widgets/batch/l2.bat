@echo off
set who=paring.com
set in=~info~.txt
set out=~ns~.txt
echo :Type commands and hosts to lookup > %in%
echo set q=any >> %in%
echo google.com >> %in%
start notepad %in%
set /p yo~=Waiting for input Hit enter when done:
echo Names That resolved  > %out%
echo enter names to lookup then type exit when finished
echo                                                     (example google.com)
nslookup <%in% >> %out%
start notepad %out%
http://www.microsoft.com/windowsxp/home/using/productdoc/en/default.asp?url=/windowsxp/home/using/productdoc/en/redirection.asp