# Problem 22
# Answer: 871198282

'''
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
'''

def score(name):
	s = 0
	for i in name:
		s += (ord(i)-64)
	return s

with open('names.txt','r') as f:
	names = sorted(map(lambda x: x[1:-1],f.readline().split(",")))

	total = 0
	for index, name in enumerate(names):
		total += score(name) * (index+1)
	
	print total