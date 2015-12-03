# Problem 37
# Answer: 748317

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

def hasProperty(n):
	if isPrime(n):
		for i in xrange(1,len(str(n))):
			if not (isPrime(str(n)[:-i]) and isPrime(str(n)[i:])):
				return False
		return True
	else:
		return False

s = 0
i = 10
count = 0
while count < 11:
	if hasProperty(i):
		s += i
		count += 1
	i += 1

print s