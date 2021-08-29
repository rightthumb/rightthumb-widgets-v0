@echo off

type "%1" | find /i /v "\Windows" | find /i /v "RECYCLE.BIN" | find /i /v "\Program Files" | find /i /v "\Application Data"  | find /i /v "\LocalService" > i2