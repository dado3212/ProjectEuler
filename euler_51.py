# Problem 51
# Answer: 121313

'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

import itertools, sys

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

counts = {}

def replaceCount(x):
	if x in counts:
		return counts[x]
	count = 0
	for i in xrange(0,10):
		l = x.replace("*",str(i))
		if len(str(int(l))) == len(x) and isPrime(l):
			count += 1
	counts[x] = count
	return count

family = 8
for i in xrange(6,10):
	reduced = filter(lambda y: y[-1] in "13579" and "*" in y and y[0] != "0", map(lambda x : ''.join(x), list(itertools.product("0123456789*", repeat=i))))
	for j in reduced:
		if replaceCount(j) == family:
			print j
			sys.exit()