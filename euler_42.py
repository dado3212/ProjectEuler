# Problem 42
# Answer: 162

'''
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

def score(name):
	s = 0
	for i in name:
		s += (ord(i)-64)
	return s

max_score = 0
words = []
with open('words.txt','r') as f:
	words = sorted(map(lambda x: x[1:-1],f.readline().split(",")))

for i in words:
	l = score(i)
	if l > max_score:
		max_score = l

triangle = []
num = 1
while float(1)/2*num*(num+1) <= max_score:
	triangle.append(int(float(1)/2*num*(num+1)))
	num += 1

total = 0
for i in words:
	if score(i) in triangle:
		total += 1

print total