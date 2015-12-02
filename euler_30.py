# Problem 30
# Answer: 443839

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

power = 5

glob_sum = 0
for i in xrange(2,10**(power + 1)):
	loc_sum = 0
	for x in str(i):
		loc_sum += int(x)**power
	if loc_sum == i:
		glob_sum += i
		print i

print glob_sum