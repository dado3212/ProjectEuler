# Problem 34
# Answer: 40730

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

total = 0
for i in xrange(3,1000000):
	s = 0
	for x in str(i):
		s += math.factorial(int(x))
	if s == i:
		print i
		total += i

print total