# Problem 32
# Answer: 45228

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def isPandigital(n):
	x = str(n)
	for i in xrange(1,len(x)+1):
		if str(i) not in x:
			return False
	return True

def validProduct(n):
	for i in str(n):
		if str(n).count(i) > 1:
			return False
	return True

def getFactorPairs(n):
	pairs = []
	for i in xrange(2,int(n**0.5)+1):
		if (n % i == 0):
			pairs.append((i, n/i))
	return pairs

s = 0

for product in xrange(1000,100000): 
	if validProduct(product):
		pairs = getFactorPairs(product)
		for pair in pairs:
			concat = str(pair[0]) + str(pair[1]) + str(product)
			if isPandigital(concat) and len(concat) == 9:
				print str(pair[0]) + " x " + str(pair[1]) + " = " + str(product)
				s += product
				break

print s
		