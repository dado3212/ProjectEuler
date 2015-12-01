# Problem 5
# Answer: 232792560

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

check = range(2,21)

def isDivisible(x):
	for c in check:
		if (x % c != 0):
			return False
	return True

num = 1
for s in check:
	num *= s

done = False
while not done:
	done = True
	for i in check:
		if num % i == 0 and isDivisible(num/i):
			num /= i
			done = False
			break

print num