#Python 2.7 based polynomial multiplier. 
#Copyright 2016
#Currently only supports two polynomials, planning on adding support for a user-defined number of polynomials.

import math, numpy

expo = int(raw_input("Highest exponent: "))
loop = expo+1

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
rows = magic(product)

#create diagonals with numpy, add them to list, AKA more magic
diags = numpy.array(rows)
n=len(diags)
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
       for b in (diags, diags[::-1])
       for i in range(-n+1, n)]
final = almost[len(almost)/2:]
#The way this diagonal sum thing works prints out two sets of sums going in different directions, we only want the second half.

#Okay, now I have to get into funny strings and stuff to make it look good

newex = expo*2
result = ''
if final[0] != 0: result += "{0}x^{1}".format(final[0],newex)

for i in range(1, len(final)-1):
    curex = newex - i
    result += " + {0}x^{1}".format(final[i],curex)

if final[-1] != 0: result += " + {0}".format(final[-1])

#Made things look better by removing terms with 0 coefficients. However, this could lead to a leading " + ". Let's get rid of that.
if final[0] == 0: result = result[3:]
if final[-1] == 0: result = result[:-3]

print "Your result is: "
print result
