# Problem 3
# Answer: 6857

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import math

number = 600851475143
sqrt = int(math.floor(math.sqrt(number))) + 1
prime_factors = []

done = False
while not done:
	done = True
	for i in xrange(2,sqrt):
		if (number % i == 0):
			prime_factors.append(i)
			number = number/i
			done = False
			break

print prime_factors[-1]