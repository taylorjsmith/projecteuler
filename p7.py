################################################################################
# Project Euler Problem 7: 10001st prime
# 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
################################################################################

def generateListOfPrimes(maxLen):
    primeList = [2]
    currNum = 3

    while len(primeList) < maxLen:
        isPrime = True

        for i in primeList:
            if currNum % i == 0:
                isPrime = False
                break

        if isPrime:
            primeList.append(currNum)
        
        currNum = currNum + 2

    return primeList

primeNums = generateListOfPrimes(10001)

print(primeNums[-1])
