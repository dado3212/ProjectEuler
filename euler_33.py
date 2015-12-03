# Problem 33
# Answer: 100

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from fractions import Fraction

def getCommon(x,y):
	for i in str(x):
		if str(x).count(i) == 1 and str(y).count(i) == 1 and i != "0":
			return i
	return -1

num = 1
denom = 1

for numerator in xrange(10,100):
	for denominator in xrange(10,100):
		a = getCommon(numerator,denominator)
		if a != -1 and numerator < denominator:
			new_top = int(str(numerator).replace(a,""))
			new_bot = int(str(denominator).replace(a,""))
			if new_bot != 0 and float(new_top)/new_bot == float(numerator)/denominator:
				num *= numerator
				denom *= denominator

print Fraction(num,denom)