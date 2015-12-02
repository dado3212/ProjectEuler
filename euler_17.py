# Problem 17
# Answer: 21124

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

first = {
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	0:""
}

second = {
	1:"ten",
	2:"twenty",
	3:"thirty",
	4:"forty",
	5:"fifty",
	6:"sixty",
	7:"seventy",
	8:"eighty",
	9:"ninety",
}

special = {
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen"
}

def stringify(i):
	string = ""

	ones = i % 10
	tens = (i % 100) / 10
	hundreds = (i % 1000) / 100
	thousands = (i % 10000) / 1000

	if (thousands > 0):
		string += first[thousands] + " thousand "
		if (hundreds == 0 and (ones != 0 or tens != 0)):
			string += "and "
		return string + stringify(hundreds * 100 + tens * 10 + ones)

	if (hundreds > 0):
		string += first[hundreds] + " hundred "
		if (ones != 0 or tens != 0):
			string += "and "
		return string + stringify(tens * 10 + ones)

	if (tens > 0):
		if i in special:
			return special[i]
		else:
			return second[tens] + "-" + first[ones]
	else:
		return first[ones]

	return "zero"

total = 0
for i in xrange(1,1001):
	total += len(stringify(i).replace(" ","").replace("-",""))

print total