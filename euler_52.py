# Problem 52
# Answer: 142857

'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def test(n,l):
	for i in xrange(1,l+1):
		if sorted(str(n)) != sorted(str(n*i)):
			return False
	return True

a = 1
while not test(a,6):
	a+=1
print a