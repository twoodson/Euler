#!/usr/bin/env python


'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

numbers = [19,17,13,11,18,16,15,14,12]

for i in xrange(2520,10000000000,2520):
    
    for y in numbers: #range(11,20,1):
        if i%y != 0:
            break

    else: 
        print i
        break

