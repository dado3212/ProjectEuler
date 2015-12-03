# Problem 39
# Answer: 840

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

allMappings = {}

for a in xrange(1,1000):
	for b in xrange(1,1000-a):
		c = (a**2 + b**2)**0.5
		if c == int(c):
			c = int(c)
			if (a+b+c) in allMappings:
				z = allMappings[(a+b+c)]
				z.append((a,b,c))
				allMappings[(a+b+c)] = z
			else:
				allMappings[(a+b+c)] = [(a,b,c)]

m = 0
p = 0
for i in xrange(1,1001):
	if i in allMappings:
		temp = allMappings[i]
		real = []
		for x in temp:
			if sorted(x) not in real:
				real.append(sorted(x))
		if len(real) > m:
			m = len(real)
			p = i
print p
