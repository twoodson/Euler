#!/usr/bin/env python

'''
 The prime factors of 13195 are 5, 7, 13, and 29. 

 What is the largest prime factor of the number 600851475143?
'''

import prime

#print "What is the number you want prime numbers for? "
#num = int(raw_input()) 
#if num == 0:
num = 600851475143

count = 3

while count < ((num**.5)+1): #count up to num (inputed number) by 2 (5,7,9 ...) 
    #if prime.is_prime(count) and num % count == 0:
    if num % count == 0 and  prime.is_prime(count):
       print count	    
    count +=2


