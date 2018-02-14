
# Problem #3: Largest Prime Factor

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def find_primes(number):
    divisor1 = []
    divisor2 = []
    factors = divisor1 + divisor2
    primes = []
    lower_val = 1
    upper_val = number

    for i in xrange(lower_val,upper_val):
        if number % i == 0:
            divisor1.append(i)
            if i in divisor2:
                break
            divisor2.append(number / i)
            lower_val += i
            upper_val /= i
            print "Factor added: %d" % i
            for j in xrange(2,i):
                if i % j == 0:
                    primes.append(j)

    print "The largest prime factor of %d: %d" % (number, primes[len(primes)-1])

#test output
find_primes(600851475143)
