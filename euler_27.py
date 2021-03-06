# Problem 27
# Answer: -59231

'''
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

def isPrime(n):
    for m in xrange(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True

def numberConsecutive(a,b):
	n = 0
	while (n**2 + a * n + b) >= 0 and isPrime(n**2 + a * n + b):
		n += 1
	return n

max_a = 0
max_b = 0
max_primes = 0
for a in xrange(-999,1000):
	for b in xrange(-999,1000):
		r = numberConsecutive(a,b)
		if r > max_primes:
			max_primes = r
			max_a = a
			max_b = b

print max_a * max_b
