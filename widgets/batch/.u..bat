@echo off
echo h
call u. %1 -v h > nul 2>&1
echo b
call u. %1 -v b > nul 2>&1
echo m
call u. %1 -v m > nul 2>&1
echo e
call u. %1 -v e > nul 2>&1