@echo off 

set pingb=google.com

if [%1] == [n] set pingb=alexandria.ninja
if [%1] == [a] set pingb=alderaan.m-eta.app
if [%1] == [e] set pingb=endor.m-eta.app
if [%1] == [t] set pingb=tatooine.m-eta.app
if [%1] == [c] set pingb=coruscant.m-eta.app
if [%1] == [b] set pingb=bespin.m-eta.app
if [%1] == [m] set pingb=mandalore.m-eta.app
if [%1] == [h] set pingb=hoth.m-eta.app
if [%1] == [y] set pingb=yavin.m-eta.app

if [%1] == [g] set pingb=google.com
if [%1] == [gg] set pingb=google.com
if [%1] == [bb] set pingb=bing.com
if [%1] == [yy] set pingb=yahoo.com

echo ping %pingb% -t
ping %pingb% -t