@echo off
if exist WebigamiGateway.class (
    del WebigamiGateway.class
)
if exist WebigamiGateway.jar (
    del WebigamiGateway.jar
)
if exist WebigamiGateway (
    rmdir /s/q WebigamiGateway
)
if exist app (
    rmdir /s/q app
)
if exist temp-dir (
    rmdir /s/q temp-dir
)


call d
