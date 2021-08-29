#!/usr/bin/python3
import sys
from time import sleep


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

progress(0, 20, suffix = 'Complete')
for i in range(20):
    # Do stuff...
    sleep(0.1)
    # Update Progress Bar
    progress(i + 1, 20, suffix = 'Complete')
