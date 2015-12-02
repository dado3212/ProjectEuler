# Problem 15
# Answer: 137846528820

'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

# Speeds up recursion by creating tons of base cases
cache = {}

def numberOfPaths(width, height):
	if width == 0 or height == 0:
		return 1
	else:
		if (width, height) in cache:
			return cache[(width, height)]
		else:
			x = numberOfPaths(width - 1, height) + numberOfPaths(width, height - 1)
			cache[(width, height)] = x
			return x

print numberOfPaths(20, 20)