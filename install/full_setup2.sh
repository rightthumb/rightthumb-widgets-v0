#!/bin/bash

while read package; do
  echo 'sudo apt install python3-'$package
  sudo apt install python3-$package || true
  echo ''
done < full_requre.txt