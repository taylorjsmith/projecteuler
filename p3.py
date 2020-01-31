################################################################################
# Project Euler Problem 3: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
################################################################################

import math

value = 600851475143
rtValue = math.sqrt(value)

while value % 2 == 0:
    value = value // 2

fac = 3

while (fac <= rtValue) and (value > 1):
    if value % fac == 0:
        value = value // fac
    else:
        fac = fac + 2

print(fac)
