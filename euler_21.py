# Problem 21
# Answer: 31626

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math

divisors = {}

def d(n):
	if n in divisors:
		return divisors[n]
	else:
		s = 0
		proper_divisors = []
		for i in xrange(2,int(math.ceil(math.sqrt(n)))):
			if (n % i == 0):
				proper_divisors.append(i)
				proper_divisors.append(n/i)

		if (int(math.sqrt(n)) == math.sqrt(n)):
			proper_divisors.append(int(math.sqrt(n)))

		if n > 1:
			proper_divisors.append(1)
		
		for i in proper_divisors:
			s += i
		divisors[n] = s
		return s

amicable = []
for i in xrange(1,10000):
	if i not in amicable:
		x = d(i)
		if d(x) == i and x != i:
			amicable.append(i)
			amicable.append(x)

t = 0
for z in amicable:
	print str(z) + " -> " + str(d(z))
	t += z

print t