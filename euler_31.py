# Problem 31
# Answer: 73682

'''
In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
It is possible to make $2 in the following way:

1 x $1 + 1 x 50p + 2 x 20p + 1 x 5p + 1 x 2p + 3 x 1p
How many different ways can $2 be made using any number of coins?
'''
import math

count = 0

for a in xrange(0,201):
	for b in xrange(0,int(math.ceil(float(201-a)/2))):
		for c in xrange(0,int(math.ceil(float(201-a-2*b)/5))):
			for d in xrange(0,int(math.ceil(float(201-a-2*b-5*c)/10))):
				for e in xrange(0,int(math.ceil(float(201-a-2*b-5*c-10*d)/20))):
					for f in xrange(0,int(math.ceil(float(201-a-2*b-5*c-10*d-20*e)/50))):
						for g in xrange(0,int(math.ceil(float(201-a-2*b-5*c-10*d-20*e-50*f)/100))):
							for h in xrange(0,int(math.ceil(float(201-a-2*b-5*c-10*d-20*e-50*f-100*g)/100))):
								if 1*a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == 200:
									count += 1

print count