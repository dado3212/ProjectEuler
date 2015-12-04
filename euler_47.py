# Problem 47
# Answer: 134043

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

import math

def primeFactorize(x):
	prime_factors = {}

	done = False
	while not done:
		done = True
		for i in xrange(2,int(x**0.5)+1):
			if (x % i == 0):
				if i in prime_factors:
					prime_factors[i] += 1
				else:
					prime_factors[i] = 1
				x = x/i
				done = False
				break
	
	if (x != 1):
		prime_factors[x] = 1

	return prime_factors

master = 4
consecutive = []
count = 1
while len(consecutive) != master:
	if len(primeFactorize(count)) == master:
		consecutive.append(count)
	else:
		consecutive = []
	count += 1

print consecutive[0]