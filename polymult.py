#Python 2.7 based polynomial multiplier. 
#Copyright 2016
#Currently only supports two polynomials, planning on adding support for a user-defined number of polynomials.

#!/usr/bin/env python

import math, numpy

expo = int(raw_input("Highest exponent: "))

if expo < 1:
    print("Seriosly, dude? Just do it yourself.")
    exit()

loop = int(expo+1)

poly1 = []
poly2 = []
product = []

print "Coefficients of Polynomial 1:"

for i in range(0,loop):
    poly1.append(int(raw_input("x^{0}: ".format(expo-i))))

print "Coefficients of Polynomial 2:"

for i in range(0,loop):
    poly2.append(int(raw_input("x^{0}: ".format(expo-i))))

#Now that all of those have been gathered... Let's get the products!

for i in range(0,len(poly1)):
    for j in range(0,len(poly2)):
        product.append(poly1[i]*poly2[j])

#Now let's add the products...

#split list into rows
magic = lambda product, n=expo+1: [product[i:i+n] for i in range(0, len(product), n)]
new = magic(product)

#final.append(product[0])
#create diagonals with numpy, add them to list, AKA more magic
board = numpy.array(new)
n=len(board)
def diag_sum(i,b):
    s = 0
    if i >= 0:
        row = 0
        end = n
    else:
        row = -i
        end = n+i
        i = 0
    while i < end:
        s += b[row, i]
        i += 1
        row += 1
    return s

almost = [diag_sum(i,b)
       for b in (board, board[::-1])
       for i in range(-n+1, n)]
final = almost[len(almost)/2:]

#Okay, now I have to get into funny strings and stuff to make it look good

newex = expo*2

if final[0] == 0: result = ''
elif final[0] == 1: result = "x^{0}".format(newex)
else: result = "{0}x^{1}".format(final[0],newex)

for i in range(1, len(final)-1):
    curex = newex - i
    if final[i] == 1: result += " + x^{0}".format(curex)
    elif final[i] != 0: result += " + {0}x^{1}".format(final[i],curex)

if final[-1] != 0: result += " + {0}".format(final[-1])

if result == '': result = "0"

print "Your result is: "
print result.replace(" + -"," - ")
