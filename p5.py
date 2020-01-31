################################################################################
# Project Euler Problem 5: Smallest multiple
# 
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?
################################################################################

# 2  : [2, 4, 8, 16]
# 3  : [3, 6, 9, 12, 18]
# 5  : [5, 10, 15, 20]
# 7  : [7, 14]
# 11 : [11]
# 13 : [13]
# 17 : [17]
# 19 : [19]
num = (2 * 2 * 2 * 2) * (3 * 3) * 5 * 7 * 11 * 13 * 17 * 19

print(num)
