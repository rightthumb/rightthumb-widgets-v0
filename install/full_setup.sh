#!/bin/bash

while read package; do
  pip3 install $package || true
done < full_requre.txt