# Problem 19
# Answer: 171

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

day = 1
month = 1
year = 1901
weekday = 2 # tuesday

num = 0

def isLeapYear(year):
	if (year % 4 == 0):
		if (year % 100 == 0 and year % 400 != 0):
			return False
		else:
			return True
	else:
		return False

def endOfMonth(day, month, year):
	# 31 days
	if day == 31 and month in [1,3,5,7,8,10,12]:
		return True

	# 30 days
	if day == 30 and month in [4,6,9,11]:
		return True
	
	# February (non leap year)
	if day == 28 and month == 2 and not isLeapYear(year):
		return True

	# February (leap year)
	if day == 29 and month == 2 and isLeapYear(year):
		return True

	return False

# 9, 1901

while not (day == 31 and month == 12 and year == 2000):
	if (weekday == 0 and day == 1):
		num += 1

	weekday = (weekday + 1) % 7

	if endOfMonth(day, month, year):
		day = 1
		if month == 12:
			month = 1
			year += 1
		else:
			month += 1
	else:
		day += 1

print num