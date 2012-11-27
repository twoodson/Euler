#!/usr/bin/env python
'''
Problem 4: A palindromic number reads the same both ways.  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. 

Find the largest palindrome made from the product of two 3-digit numbers.
'''

highest = 0

for y in xrange (999,500,-1):

    for i in xrange (999,500,-1):    
        testnum = str(i * y)
        
        if testnum[::1] == testnum[::-1] and testnum > highest:
            highest = testnum
       
print highest

