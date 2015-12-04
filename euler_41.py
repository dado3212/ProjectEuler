# Problem 41
# Answer: 7652413

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

def isPandigital(n):
	n = str(n)
	for i in xrange(1,len(n)+1):
		if str(i) not in n:
			return False
	return True

allPandigital = map(lambda x : ''.join(x), list(itertools.permutations(["1","2","3","4","5","6","7"])))

primePandigital = []
for x in allPandigital:
	if isPrime(x):
		primePandigital.append(int(x))

print sorted(primePandigital)[-1]