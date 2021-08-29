@echo off
doskey /history > %tmpf%
type %tmpf% | p line %*