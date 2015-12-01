# Problem 7
# Answer: 104743

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def isPrime(x):
	for i in xrange(2,int(math.floor(math.sqrt(x))) + 1):
		if (x % i == 0):
			return False
	return True

number = 0
curr = 2

while number < 10001:
	if isPrime(curr):
		number += 1
	curr += 1

print curr - 1