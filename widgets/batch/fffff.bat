@echo off
fff %1 %2 %3 %4 %5 %6 %7 %8 %9 > ~out.txt & parse ~out.txt : 1 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
