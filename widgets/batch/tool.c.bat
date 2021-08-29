@echo off
call tool -3to2.3 %widgets%\widgets\bash\install\py\tool

rem call p py3to2 -file %widgets%\widgets\bash\install\py\tool -save %widgets%\widgets\bash\install\py\tool2

copy %widgets%\widgets\bash\install\py\tool D:\Users\Scott\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs\home\scott\.rt\tool /y
copy %widgets%\widgets\bash\install\py\tool2 D:\Users\Scott\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs\home\scott\.rt\tool2 /y

copy %widgets%\widgets\bash\install\py\tool D:\Users\Scott\.rt\tool /y
copy %widgets%\widgets\bash\install\py\tool2 D:\Users\Scott\.rt\tool2 /y



