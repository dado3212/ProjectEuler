# Problem 4
# Answer: 906609

'''
A palindromic number reads the same both ways.  The largest palindrom made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(x):
	return str(x) == str(x)[::-1]

largest = 0
for x in xrange(100,1000):
	for y in xrange(100,1000):
		if isPalindrome(x*y) and x*y > largest:
			largest = x*y

print largest