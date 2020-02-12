################################################################################
# Project Euler Problem 19: Counting Sundays
# 
# You are given the following information, but you may prefer to do some 
# research for yourself.
# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# - A leap year occurs on any year evenly divisible by 4, 
#   but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth 
# century (1 Jan 1901 to 31 Dec 2000)?
################################################################################

# 1 Jan 1901 = Tuesday (2 mod 7)
currDay = 2
sundaySum = 0

daysPerMonthNorm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysPerMonthLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(1901, 2001, 1):
    for month in range(0, 12, 1):
        if currDay == 0:
            sundaySum = sundaySum + 1

        if (year % 4 == 0) and (year % 400 != 0):
            currDay = (currDay + daysPerMonthLeap[month]) % 7
        else:
            currDay = (currDay + daysPerMonthNorm[month]) % 7
        
print(sundaySum)
