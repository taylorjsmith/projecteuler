################################################################################
# Project Euler Problem 10: Summation of primes
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
################################################################################

import math

def sieveOfEratosthenes(maxNum):
    primeTable = [True] * (maxNum + 1)
    primeTable[0] = primeTable[1] = False

    if maxNum >= 2:
        for twoMultiple in range(4, (maxNum + 1), 2):
            primeTable[twoMultiple] = False

    if maxNum >= 3:
        for num in range(3, (maxNum + 1), 2):
            if num > math.sqrt(maxNum + 1):
                break
            elif primeTable[num] == False:
                continue
            else:
                for numMultiple in range((2 * num), (maxNum + 1), num):
                    primeTable[numMultiple] = False

    return primeTable

maxNum = 2000000
primeNums = sieveOfEratosthenes(maxNum)
primeSum = 0

for i in range(0, (maxNum + 1), 1):
    if primeNums[i] == True:
        primeSum = primeSum + i

print(primeSum)
