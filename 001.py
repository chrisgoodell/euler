
results = []

for i in xrange(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        results.append(i)
# print results

total = 0

for i in results:
    total += i

print total