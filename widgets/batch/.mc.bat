@echo off
p pipe-or-paste | p. line --make "%*" | p. -copy
