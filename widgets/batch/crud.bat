@echo off
CALL b payroll
CALL p crud -prefix _reph_signature_ -app signature -file payroll.sql