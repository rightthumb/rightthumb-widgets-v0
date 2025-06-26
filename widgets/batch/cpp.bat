@echo off

cl /EHsc /MT /O2 /I"C:\vcpkg\installed\x64-windows-static\include" crypt.cpp ^
    /link /LIBPATH:"C:\vcpkg\installed\x64-windows-static\lib" ^
    libcurl.lib libcrypto.lib libssl.lib zlib.lib ^
    advapi32.lib crypt32.lib ws2_32.lib wldap32.lib user32.lib ^
    /OPT:REF /OPT:ICF /LTCG