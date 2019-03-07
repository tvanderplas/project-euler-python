

# You are given the following information, but you may prefer to do some research for yourself.

	# 1 Jan 1900 was a Monday.
	# February has twenty-eight days
	# 	And on leap years, twenty-nine.
	# September, April, June and November have thirty days
	# All the rest have thirty-one days

	# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


def is_leap_year(year: int):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
		return True
	else:
		return False

def days_in_month(month: int = 4, year: int = 1900):
	num_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	num_days_ly = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return num_days[month] if not is_leap_year(year) else num_days_ly[month]

if __name__ == '__main__':
	day_count = 1
	starts_on_sunday = 0
	for year in range(1900, 2001):
		for month in range(1, 13):
			day_count += days_in_month(month, year)
			if day_count % 7 == 0 and year > 1900:
				starts_on_sunday += 1
	print(starts_on_sunday)