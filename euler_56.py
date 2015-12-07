# Problem 56
# Answer: 972

'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''

largest = 0

def digitSum(x):
	s = 0
	for i in str(x):
		s += int(i)
	return s

for a in xrange(0,100):
	for b in xrange(0,100):
		s = digitSum(a**b)
		if s > largest:
			largest = s

print largest