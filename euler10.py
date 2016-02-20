#Copyright 2016
#This script is written to solve Problem 10 on Project Euler
#My goal is to find the sum of all primes below 2 million

from math import sqrt

final = 17 #All Primes below 10 add to 17
for i in range(11,2000000,2): #Yes, I know that this will not include 2M in the loop. However, I also know that 2M isn't prime, so it doesn't matter
    limit = int(sqrt(i)) + 1
    prime = 1
    for j in range(2,limit):
        if i % j == 0:
            prime = 0
            break
    if prime == 1: final += i
print final
