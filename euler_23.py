# Problem 23
# Answer: 4179871

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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

		if (int(math.sqrt(n)) == math.sqrt(n) and n != 1):
			proper_divisors.append(int(math.sqrt(n)))

		if n > 1:
			proper_divisors.append(1)
		
		for i in proper_divisors:
			s += i
		divisors[n] = s
		return s

abundant_numbers = {}
generated = []
for i in xrange(1,28124):
	if d(i) > i:
		abundant_numbers[i] = 1
	else:
		abundant_numbers[i] = 0

t = 0
for x in xrange(1,28124):
	found = False

	for i in xrange(12,x):
		if abundant_numbers[i] == 1 and abundant_numbers[x-i] == 1:
			found = True
			break
	if not found:
		t += x

print t


