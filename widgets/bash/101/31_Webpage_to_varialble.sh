#!/bin/bash

content=$(wget google.com -q -O -)
echo $content


content=$(curl -L google.com)
echo $content