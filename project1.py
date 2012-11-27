#!/usr/bin/env python

import time

a = time.time()

numtotal = 0

numtotal += sum(range(3,1000,3))

for i in range(5,1000,5):
    if i%3 != 0:
        numtotal += i   

print numtotal
print time.time() - a
