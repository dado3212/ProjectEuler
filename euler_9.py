# Problem 9
# Answer: 31875000

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for a in xrange(1,1001):
	for b in xrange(a,1001-a):
		c = 1000 - a - b
		if (a**2 + b**2 == c**2):
			print "(" + str(a) + ", " + str(b) + ", " + str(c) + ")"
			print a * b * c