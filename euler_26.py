# Problem 26
# Answer: 983

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import math, decimal

def cycle(x):
	decimal.getcontext().prec = x * 2
	orig = x
	if x % 2 == 0 or x % 5 == 0:
		return -1
	else: # it does repeat
		base = decimal.Decimal(1) / decimal.Decimal(orig)
		for i in xrange(1,orig):
			x = (decimal.Decimal(1*10**i) / decimal.Decimal(orig) % 1)
			if str(x)[2:2+orig] == str(base)[2:2+orig]:
				return i

val = 0
largest = 0
for i in xrange(1,1000):
	z = cycle(i)
	if z > largest:
		largest = z
		val = i

print val