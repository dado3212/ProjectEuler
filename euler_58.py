# Problem 58
# Answer: 26241

'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

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

spiral_prime = 3

def percentForSideLength(dim):
	global spiral_prime

	adding = dim-1
	curr = (dim-2)**2 + adding

	while curr < dim**2:
		for i in xrange(0,4):
			if isPrime(curr):
				spiral_prime += 1
			curr += adding

		adding += 2

	if isPrime(dim**2):
		spiral_prime += 1

	return float(spiral_prime)/float(2*(dim-1)+1)

side = 5
done = False
while not done:
	x = percentForSideLength(side)
	if x < 0.1:
		done = True
	else:
		side += 2
print side