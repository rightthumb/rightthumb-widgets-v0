@echo off
CALL p ls -folder D:\tech\hosts\MSI\tickets -ago 1d -c p  --c -s md.d>%tmpf%
CALL p typeEach -f %tmpf%
