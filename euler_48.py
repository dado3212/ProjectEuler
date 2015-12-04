# Problem 48
# Answer: 9110846700

'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

s = 0
for i in xrange(1,1001):
	s += i**i

print str(s)[-10:]