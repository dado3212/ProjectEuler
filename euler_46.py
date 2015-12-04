# Problem 46
# Answer: 5777

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

primes = []
for i in xrange(1,1000000):
	if isPrime(i):
		primes.append(i)

squares = []
for i in xrange(1,1000):
	squares.append(i**2)

for i in xrange(3,10000):
	if (i % 2 == 1 and not isPrime(i)):
		found = False
		for x in xrange(1,i):
			if primes[x] < i and int((float(i - primes[x])/2)**0.5) == (float(i - primes[x])/2)**0.5:
				found = True
				break
		if not found:
			print i
			break
