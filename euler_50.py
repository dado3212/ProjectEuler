# Problem 50
# Answer: 997651

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def isPrime(n):
	n = int(n)
	if n == 1:
		return False
	for m in xrange(2, int(n**0.5)+1):
		if n % m == 0:
			return False
	return True

max_val = 1000000

primes = []
for i in xrange(1,max_val):
	if isPrime(i):
		primes.append(i)

summed = {}

# Generate sum list
s = 0
for i in xrange(-1,len(primes)):
	summed[i] = s
	s += primes[i]

longest = 0
pr = 0

for i in xrange(0,len(primes)):
	j = i - longest - 1
	while j > 0:
		if summed[i] - summed[j] > max_val:
			break
		if summed[i] - summed[j] in primes:
			longest = i-j
			pr = summed[i] - summed[j]
		j -= 1

print str(pr)
