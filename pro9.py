#!/usr/bin/env python


import math

'''
A Pythagorean triplet is a set of three natural numbers, a< b<c, for which,

  a2 + b2 = c2
  For example, 32 + 42 = 9 + 16 = 25 = 52.

  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
  Find the product abc.

'''

end = False

iterations = 0
for a in range(300,1,-1):           
    for b in range(500, 300,-1):     
        c = math.sqrt(a*a +b*b) 
        if a+b+c == 1000:
            print a, b, c, a*b*c
            print "iterations = %s"%( iterations )
            end = True
            break
        iterations += 1
    if end:
        break
        


'''
I'm going to loop a to 1000
then i'm going to loop b to 1000
and also loop c up to 1000

if a+b+c = 1000 where a2 +b2 = c2
a2 + b2 = c2 sqrt
sqrt(sum(a^2 + b^2)) = c
'''
