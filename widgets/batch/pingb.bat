@echo off 

set pingb=google.com

if [%1] == [b] set pingb=bespin.eyeformeta.com
if [%1] == [m] set pingb=mandalore.eyeformeta.com
if [%1] == [h] set pingb=hoth.eyeformeta.com

if [%1] == [g] set pingb=google.com
if [%1] == [bb] set pingb=bing.com
if [%1] == [y] set pingb=yahoo.com

echo ping %pingb% -t
ping %pingb% -t