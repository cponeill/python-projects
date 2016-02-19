#Copyright 2015
#This script was written to solve problem 9 on Project Euler

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
