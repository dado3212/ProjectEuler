# Problem 14
# Answer: 837799

'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

cache = {1:1}

def collatzLength(x):
	if x in cache:
		return cache[x]
	else:
		if (x % 2 == 0):
			n = x/2
		else:
			n = 3 * x + 1
		y = collatzLength(n)
		cache[x] = y + 1
		return y + 1

num = 0
longest = 0
for i in xrange(1,1000000):
	z = collatzLength(i)
	if z > longest:
		longest = z
		num = i

print num
print longest
