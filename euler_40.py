# Problem 40
# Answer: 210

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

giant = ""
for i in xrange(1,1000001):
	giant += str(i)

t = 1
for i in xrange(0,7):
	t *= int(giant[10**i-1])

print t