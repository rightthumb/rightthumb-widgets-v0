#!/bin/bash

while read package; do
  pip3 install $package || true
  echo ''
done < full_requre.txt
