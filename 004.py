
# Problem #3: Largest Palindrome from Product of Two 3-Digit Numbers

"""
# A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""

def Palin(c):
    return int(str(c)[::-1]) == c

pal_max = 0

for a in xrange(999, 99, -1):
    for b in xrange(a, 99, -1):
        product = a * b
        if Palin(product) and product > pal_max:
            pal_max = product

print(pal_max)
