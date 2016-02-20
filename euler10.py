#Copyright 2016
#This script is written to solve Problem 10 on Project Euler
#My goal is to find the sum of all primes below 1 million

from math import sqrt

final = 17
for i in range(8,1000000): #Yes, I know that this will not include 1M in the loop. However, I also know that 1M isn't prime, so it doesn't matter
    if i % 2 == 0: continue
    limit = int(sqrt(i)) + 1
    prime = 1
    for j in range(2,limit):
        if i % j == 0:
            prime = 0
            break
    if prime == 1: final += i
print final
