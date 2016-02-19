#Copyright 2015
#This script was written to solve problem 9 on Project Euler
#The objective here was to find a Pythagorean triple (three numbers where a^2+b^2=c^2) whose sum was 1000.
#I decided to go with a brute-force method that tried basically every combination of numbers chosen at random until something fit

import random
import math

while True:
    a = random.randint(1,500)
    b = random.randint(1,500)
    c = math.sqrt((a*a) + (b*b))
    sum = a + b + c
    if sum == 1000: break
print a
print b
print c
print a*b*c
