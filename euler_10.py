# Problem 10
# Answer: 142913828922

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def isPrime(x):
	for i in xrange(2,int(math.floor(math.sqrt(x))) + 1):
		if (x % i == 0):
			return False
	return True

total = 0
for i in xrange(2,2000000):
	if isPrime(i):
		total += i

print total