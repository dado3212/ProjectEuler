# Problem 53
# Answer: 4075

'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are greater than one-million?
'''

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

total = 0
for n in xrange(23,101):
	for r in xrange(0,n):
		if nCr(n,r) > 1000000:
			total += 1

print total