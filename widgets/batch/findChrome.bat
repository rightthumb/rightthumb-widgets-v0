@echo off

set chrome1="D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe"
IF EXIST %chrome1% ( set chrome=%chrome1% )

set chrome2="D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
IF EXIST %chrome2% ( set chrome=%chrome2% )

set chrome3="D:\Program Files\Google\Chrome\Application\chrome.exe"
IF EXIST %chrome3% ( set chrome=%chrome3% )



