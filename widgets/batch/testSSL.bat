@echo off
SET run=
SET /p run= About to open files: 
IF [%run%] == [y] CALL n testSSL.bat
IF [%run%] == [y] CALL epy ssl_socket_bridge_user_mgt_server_b
IF [%run%] == [y] CALL epy ssl_socket_bridge_client_user_b
IF [%run%] == [y] CALL epy ssl_socket_bridge_client_user_administrator_b
IF [%run%] == [y] CALL epy ssl_socket_bridge_client_user_administrator_c
IF [%run%] == [y] CALL epy ssl_socket_bridge_client_user_administrator_logs_b
IF [%run%] == [y] CALL epy ssl_socket_bridge_client_user_administrator_phone
SET run=
SET /p run= About to initiate server: 
IF [%run%] == [] start cmd /c cx p ssl_socket_bridge_user_mgt_server_b
SET run=
SET /p run= About to initiate user: 
IF [%run%] == [] start cmd /c cx p ssl_socket_bridge_client_user_b dennis
SET run=
SET /p run= About to initiate user: 
IF [%run%] == [] start cmd /c cx p ssl_socket_bridge_client_user_b dad
SET run=
SET /p run= About to initiate admin: 
IF [%run%] == [] start cmd /c cx p ssl_socket_bridge_client_user_administrator_b
SET run=
SET /p run= About to initiate sytem: 
IF [%run%] == [] start cmd /c cx p ssl_socket_bridge_client_user_administrator_logs_b
SET run=
rem SET /p run= About to initiate admin phone 
rem IF [%run%] == [] start cmd /c cy p ssl_socket_bridge_client_user_administrator_phone


GOTO:EOF

start cmd /c cx p ssl_socket_bridge_client_user_administrator_b


start cmd /c cx p ssl_socket_bridge_client_user_administrator_logs_b

start cmd /c cx p ssl_socket_bridge_client_user_administrator_phone

