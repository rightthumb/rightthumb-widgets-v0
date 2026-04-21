@echo off

call pathAdd C:\GNAT\2021\bin
call pathAdd C:\GNAT\2021\libexec\spark\bin
call pathAdd C:\GNAT\2021\share\examples\spark\ipstack\build\gen
call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\support
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\a\
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c2
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c3
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c4
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c5
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c6
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c7
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c8
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\c9
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\ca
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\cb
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\cc
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\cd
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\ce
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\cz
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\d
@REM call pathAdd %USERPROFILE%\Downloads\gcc\gcc-11-20210131\gcc\testsuite\ada\acats\tests\ejp
call pathAdd %USERPROFILE%\.rt\profile\daily\2025\04\01-22\aes-ada

call pathAdd C:\msys64\ucrt64\include\gpr2.static
call pathAdd C:\msys64\ucrt64\include\gpr2.static-pic
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\cd
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\c8
call pathAdd C:\GNAT\2021\include\aws.static
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\c9
call pathAdd C:\GCC\gcc\testsuite\gnat.dg\specs
call pathAdd C:\GCC\gcc\ada\libgnarl
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\ce
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\c3
call pathAdd C:\GCC\gcc\testsuite\ada\acats\tests\c4
call pathAdd C:\msys64\ucrt64\include\xmlada\xmlada_unicode.static
call pathAdd C:\GCC\gcc\ada
call pathAdd C:\msys64\mingw64\lib\gcc\x86_64-w64-mingw32\14.2.0\adainclude
call pathAdd C:\GNAT\2021\lib\gcc\x86_64-w64-mingw32\10.3.1\adainclude
call pathAdd C:\QMK_MSYS\mingw64\lib\gcc\x86_64-w64-mingw32\13.2.0\adainclude
call pathAdd C:\msys64\ucrt64\lib\gcc\x86_64-w64-mingw32\14.2.0\adainclude
call pathAdd C:\GCC\gcc\ada\libgnat
call pathAdd C:\GCC\gcc\testsuite\gnat.dg


call pathAdd C:\adacf\src

set ADA_INCLUDE_PATH=C:\adacf\src