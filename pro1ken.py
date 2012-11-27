#!usr/bin/env python

import time

a = time.time()

c = set(range(3,1000,3))

b = set(range(5,1000,5))

print sum(c&b)

print time.time() - a
