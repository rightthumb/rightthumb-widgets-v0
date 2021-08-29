@echo off
driverquery /v
:: drivers > ~out.txt & cleanSpaces ~out.txt > ~out2.txt & parse ~out2.txt "," 2  & del ~out*