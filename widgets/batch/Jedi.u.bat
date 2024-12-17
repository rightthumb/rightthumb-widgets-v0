@echo off

if exist .folder.meta (
    rename .folder.meta .folder.meta.20eb51a0ba52
)

copy C:\Users\Scott\.rt\profile\documents\Jedi-Offsite\.folder.meta .folder.meta

call u. %*

if exist .folder.meta.20eb51a0ba52 (
    rename .folder.meta.20eb51a0ba52 .folder.meta
)

