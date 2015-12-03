# Problem 35
# Answer: 55

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def isPrime(n):
	n = int(n)
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

count = 0
for i in xrange(2,1000000):
	failed = False
	for x in xrange(0,len(str(i))):
		if not isPrime((str(i)+str(i))[x:x+len(str(i))]):
			failed = True
	if not failed:
		count += 1

print count