# Problem 36
# Answer: 872187

'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def isDoublePalindromic(n):
	binary = bin(n)[2:]
	if str(n) == str(n)[::-1] and binary == binary[::-1]:
		return True
	return False

s = 0
for i in xrange(0,1000000):
	if isDoublePalindromic(i):
		s += i

print s