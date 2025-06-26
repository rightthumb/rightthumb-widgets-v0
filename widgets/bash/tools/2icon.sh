#!/bin/bash

echo ex:   2ico icon.png favorite.ico

convert -resize x32 -gravity center -crop 32x32+0+0 $1 -flatten -colors 256 -background transparent $2
