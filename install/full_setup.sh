#!/bin/bash

while read package; do
  pip3 install --upgrade --no-cache-dir --break-system-packages $package || true
  echo ''
done < full_requre.txt
