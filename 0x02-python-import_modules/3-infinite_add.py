#!/usr/bin/python3
import sys

av = sys.argv
l_av = len(sys.argv)-1
tot = 0

if l_av > 0:
    for i in range(1, l_av + 1):
        tot += int(av[i])
    print(tot)
elif l_av == 0:
    print(0)
