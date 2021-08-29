#!/usr/bin/python3
ips = {}

fh = open("C:\Users\Scott\Desktop\qsort\qsort-2017.08.31-17.44-.txt", "r").readlines()
for line in fh:
    ip = line.split("\n")[0]
    print ip
    if 6 < len(ip) <=15:
        ips[ip] = ips.get(ip, 0) + 1
# print ips
# print fh