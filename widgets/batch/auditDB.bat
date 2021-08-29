@echo off
auditFMDB %1 > ~out.txt & cleanLines ~out.txt & del ~out.txt