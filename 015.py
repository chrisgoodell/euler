
## optimized solution
import time

dim = int(raw_input("Enter a cube length: "))
def route(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j] + L[j - 1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
 
start = time.time()
n = route(dim)
elapsed = (time.time() - start)
print n
print "%s found in %s seconds" % (n,elapsed)


## using Pascal's triangle for runtime optimization 
import time
import math

start2 = time.time()
n2 = (math.factorial(2*dim)) / ((math.factorial(dim)) ** 2)
elapsed2 = (time.time() - start2)
print n2
print "%s found in %s seconds" % (n2,elapsed2)