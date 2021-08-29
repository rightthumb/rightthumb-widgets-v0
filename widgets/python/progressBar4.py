#!/usr/bin/python3
from progress.bar import Bar
from time import sleep

bar = Bar('Processing', max=20)
for i in range(20):
    sleep(0.1)
    # Do some work
    bar.next()
bar.finish()