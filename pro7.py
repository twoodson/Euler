#!/usr/bin/env python

'''
By listing the first six prime numbers: 2,3,5,7,11,and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''


numofprimes = 2

for i in xrange(5,99999999,2):
 
    for y in xrange(3,int(i**.5)+1,2):
        if i%y ==0:
            break
    else:
        numofprimes +=1

    if numofprimes == 10001:
        print i
        print numofprimes
        break

    
