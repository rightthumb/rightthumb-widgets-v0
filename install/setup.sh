#!/bin/bash

while read package; do
  pip3 install $package || true
done < ../require.txt
pip3 install --upgrade pycryptodome