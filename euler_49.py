# Problem 49
# Answer: 296962999629

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

def arePermutations(x,y):
	for a in str(x):
		if str(y).count(a) != str(x).count(a):
			return False
	return True

for i in xrange(1000,10000):
	if isPrime(i) and isPrime(i + 3330) and isPrime(i + 3330 * 2) and arePermutations(i, i+3330) and arePermutations(i,i+3330*2):
		print str(i) + str(i + 3330) + str(i + 3330 * 2)