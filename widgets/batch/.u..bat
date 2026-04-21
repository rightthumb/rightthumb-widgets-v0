@echo off
echo h
call u. %1 -v h > nul 2>&1
echo c
call u. %1 -v c > nul 2>&1
rem echo b
rem call u. %1 -v b > nul 2>&1
rem echo m
rem call u. %1 -v m > nul 2>&1
rem echo e
rem call u. %1 -v e > nul 2>&1