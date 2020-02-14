################################################################################
# Project Euler Problem 23: Non-abundant sums
# 
# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors 
# of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is 
# a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is 
# less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater 
# than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even 
# though it is known that the greatest number that cannot be expressed as the 
# sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the 
# sum of two abundant numbers.
################################################################################

import math

def isAbundant(num):
    factorSum = 0

    for i in range(1, (int(math.sqrt(num)) + 1), 1):
        if num % i == 0:
            factorSum = factorSum + i

            if ((i * i) != num) and (i != 1):
                factorSum = factorSum + (num // i)

    return (factorSum > num)

n = 28123
allNums = [i for i in range(1, (n + 1), 1)]
abundantNums = []

for i in range(1, (n + 1), 1):
    if isAbundant(i):
        abundantNums.append(i)

for j in range(0, len(abundantNums), 1):
    for k in range(j, len(abundantNums), 1):
        abundantSum = abundantNums[j] + abundantNums[k]

        if (abundantSum <= n) and (allNums[abundantSum - 1] != 0):
            allNums[abundantSum - 1] = 0

print(sum(allNums))
