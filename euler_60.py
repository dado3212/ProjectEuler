# Problem 60
# Answer: 26033

'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

import itertools, sys

primes = {1:False}

def isPrime(n):
	n = int(n)
	if n in primes:
		return primes[n]
	else:
		for m in xrange(2, int(n**0.5)+1):
			if n % m == 0:
				primes[n] = False
				return False
		primes[n] = True
		return True

def validPool(arr):
	arr = [str(x) for x in arr]
	combos = map(lambda x: ''.join(x), list(itertools.permutations(arr,2)))
	for combo in combos:
		if not isPrime(int(combo)):
			return False
	return True

primePool = []

for i in xrange(1,10000):
	if isPrime(i):
		primePool.append(i)

for a_i in xrange(0,len(primePool)):
	a = primePool[a_i]
	secondPool = [p for p in primePool if validPool([a,p])]
	for b_i in xrange(0,len(secondPool)):
		b = secondPool[b_i]
		thirdPool = [p for p in secondPool if validPool([a,b,p])]
		for c_i in xrange(0,len(thirdPool)):
			c = thirdPool[c_i]
			fourthPool = [p for p in thirdPool if validPool([a,b,c,p])]
			for d_i in xrange(0,len(fourthPool)):
				d = fourthPool[d_i]
				fifthPool = [p for p in fourthPool if validPool([a,b,c,d,p])]
				if len(fifthPool) > 0:
					print a + b + c + d + fifthPool[0]
					sys.exit()